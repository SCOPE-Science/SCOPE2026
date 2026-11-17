"""Exact finite face and cut certificate for two-row isotonic grid variation.
Run: python verify_ladder.py (requires NumPy). All inequalities use signed 64-bit integers;
all means are scaled by lcm(1,...,12), so no floating-point step is used.
"""
from math import lcm
from fractions import Fraction
import numpy as np

EXPECTED = {2: Fraction(1), 3: Fraction(4,3), 4: Fraction(3,2),
            5: Fraction(19,10), 6: Fraction(9,4)}
FACE_COUNTS = {2:10,3:52,4:272,5:1424,6:7456}

def grid_edges(k):
    # Row-major: top vertices 0,...,k-1, bottom k,...,2k-1.
    return tuple((j, k+j) for j in range(k)) + tuple(
        (row*k+j, row*k+j+1) for row in range(2) for j in range(k-1))

def all_faces(k):
    """All realizable connected equality partitions of the grid order cone."""
    n=2*k
    edges=grid_edges(k)
    parts=set()
    for mask in range(1<<len(edges)):
        parent=list(range(n))
        def root(x):
            while parent[x]!=x: x=parent[x]
            return x
        for i,(u,v) in enumerate(edges):
            if mask>>i&1:
                a,b=root(u),root(v)
                parent[a]=b
        blocks={}
        for v in range(n):
            blocks.setdefault(root(v),[]).append(v)
        part=tuple(sorted(tuple(b) for b in blocks.values()))
        parts.add(part)
    faces=[]
    for part in sorted(parts):
        index={v:i for i,block in enumerate(part) for v in block}
        graph=[set() for _ in part]
        indegree=[0]*len(part)
        for u,v in edges:
            a,b=index[u],index[v]
            if a!=b and b not in graph[a]:
                graph[a].add(b)
                indegree[b]+=1
        sources=[i for i,x in enumerate(indegree) if x==0]
        count=0
        while sources:
            a=sources.pop()
            count+=1
            for b in graph[a]:
                indegree[b]-=1
                if indegree[b]==0:
                    sources.append(b)
        if count==len(part):
            faces.append(part)
    return faces

def tv_scaled(Y, edges):
    tv=np.zeros(Y.shape[0], dtype=np.int64)
    for a,b in edges:
        tv+=np.abs(Y[:,a]-Y[:,b])
    return tv

def certificate(k):
    n=2*k
    E=grid_edges(k)
    faces=all_faces(k)
    assert len(faces)==FACE_COUNTS[k], (k,len(faces))
    masks=np.arange(1,(1<<n)-1,dtype=np.int64)
    X=((masks[:,None]>>np.arange(n,dtype=np.int64))&1)
    den=tv_scaled(X,E)
    assert (den>0).all()
    scale=lcm(*range(1,n+1))
    target=EXPECTED[k]
    found=None
    tested=0
    for part in faces:
        Y=np.zeros_like(X)
        for block in part:
            blocksum=np.sum(X[:,block],axis=1)
            # average on each block = blocksum / len(block)
            Y[:,block]=((scale//len(block))*blocksum)[:,None]
        num=tv_scaled(Y,E)
        # Exact arithmetic: num/scale / den <= target.numerator/target.denominator.
        upper=target.numerator*scale*den
        lower=target.denominator*num
        assert bool(np.all(lower<=upper)),(k,part,int(masks[np.flatnonzero(lower>upper)[0]]))
        if found is None:
            ii=np.flatnonzero(lower==upper)
            if len(ii):
                j=int(ii[0])
                found=(part,int(masks[j]),int(num[j]),int(den[j]))
        tested+=len(masks)
    assert found is not None
    part,mask,num,den0=found
    assert Fraction(num,scale*den0)==target
    print(f'K={k} FACES={len(faces)} CUT_TESTS={tested} EXACT_SHARP={target} '
          f'WITNESS_BLOCKS={part} CUT_MASK={mask}')

def asymptotic_construct(k):
    # Top row pooled, bottom row singleton; cut after s columns in both rows.
    n=2*k
    s=k//2
    p=[tuple(range(k))]+[(j,) for j in range(k,2*k)]
    E=grid_edges(k)
    X=np.array([[int((j%k)>=s) for j in range(n)]],dtype=np.int64)
    scale=k  # only block sizes 1 and k occur in the witness
    Y=np.zeros_like(X)
    for block in p:
        Y[:,block]=(X[:,block].sum(axis=1)*(scale//len(block)))[:,None]
    gain=Fraction(int(tv_scaled(Y,E)[0]),scale*int(tv_scaled(X,E)[0]))
    formula=Fraction(1,2)+Fraction(s*(k-s),k)
    assert gain==formula
    print(f'ROW_POOL_K={k} EXACT_LOWER_WITNESS={gain}')

if __name__=='__main__':
    for k in EXPECTED: certificate(k)
    for k in (2,3,4,5,6,7,8,11,19,31): asymptotic_construct(k)
    print('ALL_EXACT_LADDER_ISOTONIC_VARIATION_CERTIFICATES_PASS')
