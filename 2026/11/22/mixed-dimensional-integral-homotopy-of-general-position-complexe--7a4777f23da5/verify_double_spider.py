"""Independent finite verification of geodesic-general-position complexes of double spiders.
The source construction and graph-distance test do not use the homotopy proof.
Run: python3 verify_double_spider.py
"""
from collections import deque,defaultdict
from itertools import combinations,product
from math import comb,prod

def construct(aa,bb):
    if len(aa)<2 or len(bb)<2 or min(aa+bb)<1:
        raise ValueError('Need at least two positive-length arms at each hub.')
    adj=[set(),set()]; adj[0].add(1);adj[1].add(0)
    arms=[[],[]]
    for side,Ls in enumerate((aa,bb)):
        for L in Ls:
            chain=[]; last=side
            for j in range(L):
                idx=len(adj);adj.append({last});adj[last].add(idx);chain.append(idx);last=idx
            arms[side].append(chain)
    return adj,arms

def all_distances(adj):
    ds=[]
    for src in range(len(adj)):
        d={src:0}; q=deque([src])
        while q:
            x=q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y]=d[x]+1;q.append(y)
        assert len(d)==len(adj)
        ds.append(d)
    return ds

def geodesic_faces(adj):
    n=len(adj); ds=all_distances(adj)
    bad=[]
    for a,b,c in combinations(range(n),3):
        if any(ds[x][y]+ds[y][z]==ds[x][z] for x,y,z in [(a,b,c),(b,a,c),(a,c,b)]):
            bad.append((1<<a)|(1<<b)|(1<<c))
    faces=defaultdict(list)
    for m in range(1,1<<n):
        if all(m&b != b for b in bad):
            faces[m.bit_count()-1].append(m)
    return faces

def structural_faces(adj,arms):
    n=len(adj); A=[v for a in arms[0] for v in a]; B=[v for a in arms[1] for v in a]
    allarms=arms[0]+arms[1]; faces=defaultdict(set)
    for m in range(1,1<<n):
        b0=bool(m&1);b1=bool(m&2)
        if b0 and b1: ok=(m==3)
        elif b0:
            bcount=(m & sum(1<<v for v in B)).bit_count()
            acount=(m & sum(1<<v for v in A)).bit_count()
            if acount: ok=(acount==1 and bcount==0)
            else: ok=all((m & sum(1<<v for v in arm)).bit_count()<=1 for arm in arms[1])
        elif b1:
            acount=(m & sum(1<<v for v in A)).bit_count()
            bcount=(m & sum(1<<v for v in B)).bit_count()
            if bcount: ok=(bcount==1 and acount==0)
            else: ok=all((m & sum(1<<v for v in arm)).bit_count()<=1 for arm in arms[0])
        else: ok=all((m & sum(1<<v for v in arm)).bit_count()<=1 for arm in allarms) or m.bit_count()<=2
        if ok:faces[m.bit_count()-1].add(m)
    return faces

def f2_rank(cols):
    basis={}
    for a in cols:
        while a:
            b=a.bit_length()-1
            if b in basis:a^=basis[b]
            else:
                basis[b]=a;break
    return len(basis)

def reduced_betti(faces):
    dims=sorted(faces); bounds={}
    for d in dims:
        if d==0:
            bounds[d]=1;continue
        lower={m:i for i,m in enumerate(faces[d-1])}
        cols=[]
        for m in faces[d]:
            a=0;bit=m
            while bit:
                bit0=bit&-bit; bit-=bit0
                a^=1<<lower[m^bit0]
            cols.append(a)
        bounds[d]=f2_rank(cols)
    return {d:len(faces[d])-bounds.get(d,0)-bounds.get(d+1,0) for d in dims}

def predicted(aa,bb):
    P,Q=len(aa),len(bb); N=sum(aa+bb)
    u,v=prod(L-1 for L in aa),prod(L-1 for L in bb)
    b=defaultdict(int);b[1]+=N+1+sum(comb(L,2) for L in aa+bb);b[P]+=u;b[Q]+=v;b[P+Q-1]+=u*v
    return {k:v for k,v in b.items() if v}

def check(aa,bb):
    adj,arms=construct(aa,bb)
    actual=geodesic_faces(adj)
    expected=structural_faces(adj,arms)
    actualset={d:set(v) for d,v in actual.items()}
    assert actualset==dict(expected), (aa,bb,'face mismatch',[(d,len(actualset.get(d,set())^expected.get(d,set()))) for d in set(actualset)|set(expected)])
    actual={d:sorted(v) for d,v in actual.items()}
    betti=reduced_betti(actual)
    target=predicted(aa,bb)
    assert {k:v for k,v in betti.items() if v}==target,(aa,bb,betti,target)
    return sum(map(len,actual.values())),betti

if __name__=='__main__':
    checks=0;total_faces=0;examples=[]
    for p,q in product((2,3),repeat=2):
        for aa in product((1,2),repeat=p):
            for bb in product((1,2),repeat=q):
                nf,b=check(aa,bb);checks+=1;total_faces+=nf
                if (aa,bb) in [((2,2),(2,2)),((2,2),(2,2,2)),((2,2,2),(2,2,2))]:
                    examples.append((aa,bb,nf,b))
    for aa,bb in [((3,3),(3,3)),((2,3),(1,2,3)),((3,1,2),(2,2))]:
        nf,b=check(aa,bb);checks+=1;total_faces+=nf;examples.append((aa,bb,nf,b))
    print('PASS: cases',checks,'total_nonempty_faces',total_faces)
    for x in examples:print('example',x)
