#!/usr/bin/env python3
"""Exact finite topology certificate for the dodecahedral first forest complex.

Standard-library Python 3.10+. Graph vertices 0..9 (outer decagon),
10..19 (inner pentagon-star), with edges i--i+1, i--(10+i),
(10+i)--(10+i+2), subscripts modulo 10.

All incidence matrices use sorted-mask simplex orientations. All checks are
performed anew from graph definition; no external result files are read.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 20

def graph():
    edges=set()
    for i in range(10):
        for u,v in ((i,(i+1)%10),(i,i+10),(i+10,10+(i+2)%10)):
            edges.add(tuple(sorted((u,v))))
    adj=[0]*N
    for u,v in edges:
        adj[u]|=1<<v
        adj[v]|=1<<u
    assert len(edges)==30 and all(a.bit_count()==3 for a in adj)
    return adj,edges

def valid_maxdeg_one(x,adj):
    y=x
    while y:
        b=y&-y; y-=b; v=b.bit_length()-1
        if ((adj[v]&x).bit_count()>1):
            return False
    return True

def enumerate_faces(adj,stage):
    # Hereditary constructive enumeration, valid for stages 0 and 1.
    good=bytearray(1<<N);good[0]=1
    for x in range(1,1<<N):
        b=x&-x;v=b.bit_length()-1;y=x^b
        if not good[y]:continue
        if stage==0:
            if not (adj[v]&y): good[x]=1
        else:
            neighbors=adj[v]&y
            if neighbors.bit_count()<=1 and (not neighbors or not (adj[neighbors.bit_length()-1]&y)):
                good[x]=1
    return {x for x,yes in enumerate(good) if yes}

def validate_faces_independently(F,adj):
    # Forbidden centered length-two paths: a subset is a face iff no path triple.
    trip=set()
    for v in range(N):
        nv=[w for w in range(N) if adj[v]>>w&1]
        for a,b in combinations(nv,2):
            trip.add((1<<a)|(1<<b)|(1<<v))
    assert len(trip)==60
    forbidden=tuple(trip)
    hits=0
    for mask in range(1<<N):
        q=not any(mask&t==t for t in forbidden)
        assert (mask in F)==q,(mask,q)
        hits+=q
    assert hits==63143
    return len(trip)

def boundaries(x):
    bits=[];y=x
    while y:
        b=y&-y;y^=b;bits.append(b)
    return [(x^b,1 if i%2==0 else -1) for i,b in enumerate(bits)]

def match(F,order):
    live=set(F);pairs=[]
    for v in order:
        b=1<<v
        # For each vertex, every remaining eligible pair is disjoint; order irrelevant.
        for x in tuple(live):
            if not (x&b) and x|b in live:
                live.remove(x);live.remove(x|b);pairs.append((x,x|b))
    assert len(live)+2*len(pairs)==len(F)
    assert all(a in F and b in F and (b^a).bit_count()==1 for a,b in pairs)
    return live,pairs

def verify_acyclic(F,pairs):
    # Forman matching: reverse the matched Hasse edge, orient every other
    # Hasse edge from a simplex to its codimension-one face.
    low={a:b for a,b in pairs};up={b:a for a,b in pairs}
    indeg={x:0 for x in F};edgecount=0
    for u in F:
        for a,_ in boundaries(u):
            edgecount+=1
            if low.get(a)==u: indeg[u]+=1
            else: indeg[a]+=1
    dq=deque(x for x in F if indeg[x]==0);visited=0
    while dq:
        u=dq.popleft();visited+=1
        if u in low:
            v=low[u];indeg[v]-=1
            if indeg[v]==0:dq.append(v)
        for a,_ in boundaries(u):
            if up.get(u)==a:continue
            indeg[a]-=1
            if indeg[a]==0:dq.append(a)
    assert visited==len(F),(visited,len(F))
    return edgecount

def morse_boundaries(critical,pairs):
    crit=set(critical);lower={a:b for a,b in pairs};upper={b:a for a,b in pairs}
    @lru_cache(maxsize=None)
    def projected(q):
        if q in crit:return ((q,1),)
        if q in upper:return ()
        u=lower[q]
        flip=u^q
        epsilon=(-1)**((q&(flip-1)).bit_count())
        out={}
        for p,sgn in boundaries(u):
            if p==q:continue
            for c,v in projected(p):out[c]=out.get(c,0)-epsilon*sgn*v
        return tuple((c,v) for c,v in out.items() if v)
    dims={}
    for c in crit:dims.setdefault(c.bit_count()-1,[]).append(c)
    for d in dims:dims[d].sort()
    matrices={}
    for d in sorted(dims):
        if d-1 not in dims:continue
        target=dims[d-1]
        matrix=[[0]*len(dims[d]) for _ in target]
        idx={c:i for i,c in enumerate(target)}
        for j,u in enumerate(dims[d]):
            for p,sgn in boundaries(u):
                for c,val in projected(p):
                    matrix[idx[c]][j]+=sgn*val
        matrices[d]=matrix
    return matrices, {d:len(a) for d,a in dims.items()}, projected.cache_info()

def determinant(A):
    # Fraction-free Bareiss elimination, exact over Z.
    n=len(A)
    if not n:return 1
    a=[list(row) for row in A];sign=1;prev=1
    for k in range(n-1):
        j=next((j for j in range(k,n) if a[j][k]),None)
        if j is None:return 0
        if k!=j:a[k],a[j]=a[j],a[k];sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for h in range(k+1,n):
                z=a[i][h]*p-a[i][k]*a[k][h]
                assert z%prev==0
                a[i][h]=z//prev
        for i in range(k+1,n):a[i][k]=0
        prev=p
    return sign*a[-1][-1]

def unit_minor(A,rank):
    m=len(A);n=len(A[0])
    for rows in combinations(range(m),rank):
        for cols in combinations(range(n),rank):
            if abs(determinant([[A[i][j] for j in cols] for i in rows]))==1:
                return (rows,cols)
    raise AssertionError('No unit maximal minor')

def multiply(A,B):
    return [[sum(A[i][h]*B[h][j] for h in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def execute():
    adj,edges=graph()
    F=enumerate_faces(adj,1)
    assert len(F)==63143
    triplecount=validate_faces_independently(F,adj)
    fvector=Counter(x.bit_count()-1 for x in F)
    expected={-1:1,0:20,1:190,2:1080,3:3985,4:9772,5:15870,6:16640,7:10770,8:4000,9:750,10:60,11:5}
    assert fvector==expected
    print('STAGE1 faces',len(F),'forbidden_triplets',triplecount,'face_vector',dict(sorted(fvector.items())))
    for direction,order in (('ascending',range(N)),('descending',range(N-1,-1,-1))):
        crit,pairs=match(F,order)
        edges_hasse=verify_acyclic(F,pairs)
        assert len(pairs)==31566
        matrices,crit_counts,cache=morse_boundaries(crit,pairs)
        assert edges_hasse==sum(x.bit_count() for x in F)
        assert set(matrices)=={6,7}
        A,B=matrices[6],matrices[7]
        assert all(not v for row in multiply(A,B) for v in row)
        if direction=='ascending':
            assert crit_counts=={5:1,6:6,7:4}
            assert A==[[0,0,-1,0,1,0]]
            assert B==[[1,1,0,0],[0,0,0,-1],[0,1,0,0],[0,-1,1,0],[0,1,0,0],[0,0,-1,0]]
            ra,rb=1,4
        else:
            assert crit_counts=={5:2,6:6,7:3}
            assert A==[[-1,-1,0,-1,1,1],[0,-1,-1,0,0,1]]
            assert B==[[1,0,0],[-1,0,1],[1,0,0],[0,1,0],[0,1,0],[0,0,1]]
            ra,rb=2,3
        a_minor=unit_minor(A,ra);b_minor=unit_minor(B,rb)
        assert 6-ra-rb==1
        print('STAGE1',direction,'pairs',len(pairs),'hasse',edges_hasse,'critical',crit_counts,'unit_minors',a_minor,b_minor,'H6=Z','all_other_reduced_H=0')
    F0=enumerate_faces(adj,0)
    assert len(F0)==5828 and F0 <= F
    crit0,pairs0=match(F0,range(N))
    assert Counter(x.bit_count()-1 for x in crit0)=={5:4}
    hasse0=verify_acyclic(F0,pairs0)
    print('STAGE0 faces',len(F0),'pairs',len(pairs0),'hasse',hasse0,'critical',{5:4},'homotopy_4S5')
    print('COFIBER null_inclusion_F0_to_F1 since pi5_S6_zero; wedge_5S6')
    print('DODECAHEDRAL_FIRST_FOREST_S6_VERIFIED')
if __name__=='__main__':execute()
