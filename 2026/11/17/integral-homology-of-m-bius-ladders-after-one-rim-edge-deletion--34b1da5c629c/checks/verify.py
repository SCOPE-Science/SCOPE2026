"""Standalone checks for rim-edge fault independence homology, n=4,...,10.
Finite evidence; the unrestricted theorem is established by the accompanying proof.
Run: python checks/verify.py
"""
from collections import defaultdict


def mobius_minus_rim(n):
    vertices = set(range(2 * n))
    edges = {frozenset((i, (i+1) % (2*n))) for i in range(2*n)}
    edges |= {frozenset((i, i+n)) for i in range(n)}
    edges.remove(frozenset((n-1,n)))
    # Map cyclic 0,...,n-1,n,...,2n-1 to ladder columns.
    return vertices,edges


def ladder(n):
    edges={frozenset((i,i+n)) for i in range(n)}
    edges|={frozenset((i,i+1)) for i in range(n-1)}
    edges|={frozenset((i+n,i+n+1)) for i in range(n-1)}
    return set(range(2*n)),edges


def rim_ladder(n):
    V,E=ladder(n)
    E.add(frozenset((0,2*n-1)))
    return V,E


def link_graph(n):
    V,E=ladder(n)
    u,v=0,2*n-1
    killed={u,v}
    for e in E:
        if u in e or v in e:killed.update(e)
    V=V-killed
    return V,{e for e in E if e <= V}


def fold(V,E,v,w):
    N=lambda a:{next(iter(e-{a})) for e in E if a in e}
    assert v in V and w in V and v!=w and N(w)<=N(v), (v,w,N(w),N(v))
    V.remove(v)
    E.difference_update(e for e in list(E) if v in e)


def folds_ladder(n):
    V,E=ladder(n)
    for j in range(0,n-1,2):
        fold(V,E,j+1,n+j)
        fold(V,E,n+j+1,j)
    expected={frozenset((i,n+i)) for i in range(0,n,2)}
    assert E==expected and len(V)==2*len(expected)
    return len(expected)


def folds_link(n):
    V,E=link_graph(n)
    if n==4:
        assert len(V)==2 and not E
        return
    if n==5:
        assert len(V)==4 and len(E)==3
        degrees={v:sum(v in e for e in E) for v in V}
        assert sorted(degrees.values())==[1,1,2,2]
        return
    fold(V,E,2,n+1)
    fold(V,E,n+3,n+1)
    if n>=7:
        fold(V,E,5,3)
        fold(V,E,n+4,3)
    if n==6:
        assert len(V)==4 and len(E)==2
        return
    if n==7:
        assert len(V)==4 and len(E)==2
        return
    first={frozenset((n+1,n+2)),frozenset((3,4))}
    W,F=link_graph(n-4)
    tr=lambda v:v+4 if v<n-4 else v+8
    assert V=={n+1,n+2,3,4}|{tr(v) for v in W}
    assert E==first|{frozenset(map(tr,e)) for e in F}


def faces(V,E):
    vertices=sorted(V)
    n=len(vertices);ix={v:i for i,v in enumerate(vertices)}
    neigh=[0]*n
    for e in E:
        a,b=map(ix.get,e)
        neigh[a]|=1<<b;neigh[b]|=1<<a
    dims=defaultdict(list)
    def rec(i,chosen,forbidden,p):
        if i==n:
            if chosen:dims[p].append(chosen)
            return
        rec(i+1,chosen,forbidden,p)
        if not ((forbidden>>i)&1):
            rec(i+1,chosen|(1<<i),forbidden|neigh[i]|(1<<i),p+1)
    rec(0,0,0,0)
    return dims


def gf2_rank(columns,rowindex):
    piv={};rank=0
    for face in columns:
        x=0;f=face
        while f:
            low=f&-f;f-=low
            x^=1<<rowindex[face^low]
        while x:
            j=x.bit_length()-1
            if j not in piv:
                piv[j]=x;rank+=1;break
            x^=piv[j]
    return rank


def reduced_betti(d):
    ranks={}
    for p in sorted(d):
        if p>1:
            prev={x:i for i,x in enumerate(d[p-1])}
            ranks[p]=gf2_rank(d[p],prev)
    values={p-1:len(d[p])-ranks.get(p,0)-ranks.get(p+1,0) for p in d}
    if values:values[0]-=1
    return {k:v for k,v in values.items() if v}


def expected(n):
    k=n//4
    if n%4==0:return {2*k-1:1}
    if n%4==1:return {2*k:1}
    if n%4==2:return {2*k:2}
    return {}


def primitive_check(n):
    V,E=ladder(n);U,F=link_graph(n)
    sL={i if ((i//2)%2==0) else n+i for i in range(0,n,2)}
    sB=sL-{0,2*n-1}
    def independent(s,edges):return all(not e<=s for e in edges)
    assert independent(sL,E) and independent(sB,F)
    assert all(not independent(sL|{v},E) for v in V-sL)
    assert all(not independent(sB|{v},F) for v in U-sB)
    assert len(sL)==(n+1)//2 and len(sB)==(n-3)//2


for n in range(4,11):
    V,E=mobius_minus_rim(n)
    assert (V,E)==rim_ladder(n)
    folds_ladder(n)
    folds_link(n) if n>=6 else None
    b=reduced_betti(faces(V,E))
    assert b==expected(n),(n,b,expected(n))
    print(f"n={n}: faces={sum(len(v) for v in faces(V,E).values())}, reduced_mod2={b}, graph_models=equal, ladder_folds=pass")
for n in (7,11,15):
    primitive_check(n)
    print(f"n={n}: primitive maximal-face certificates=pass")
print("RIM_DELETION_HOMOLOGY_CHECK_PASS")
