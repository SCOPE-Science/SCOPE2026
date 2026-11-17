"""Finite independent checks for triangle-avoidance complexes of common-clique books.
Run with Python 3.10+, no third-party libraries required.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def build(s, sizes):
    core = tuple(range(s)); pages=[]; cursor=s
    for n in sizes:
        pages.append(tuple(range(cursor,cursor+n))); cursor+=n
    # Explicit graph edges; no cross-page edges.
    edges=set()
    for p in pages:
        for a,b in combinations(core+p,2): edges.add((min(a,b),max(a,b)))
    triangles=[]
    for a,b,c in combinations(range(cursor),3):
        if (a,b) in edges and (a,c) in edges and (b,c) in edges:
            triangles.append((1<<a)|(1<<b)|(1<<c))
    assert len(triangles)==comb(s,3)+sum(comb(s+n,3)-comb(s,3) for n in sizes)
    by_dim=defaultdict(list)
    for mask in range(1,1<<cursor):
        if all((mask&t)!=t for t in triangles):
            by_dim[mask.bit_count()-1].append(mask)
    return by_dim,tuple(range(cursor))


def rank_mod_two(rows,cols):
    idx={v:i for i,v in enumerate(rows)}; piv={}
    for face in cols:
        z=0
        m=face
        while m:
            bit=m&-m; m-=bit
            z^=1<<idx[face^bit]
        while z:
            key=z.bit_length()-1
            if key not in piv:
                piv[key]=z; break
            z^=piv[key]
    return len(piv)


def betti(by_dim):
    ds=max(by_dim)
    ranks={d:rank_mod_two(by_dim[d-1],by_dim[d]) for d in range(1,ds+1)}
    # Reduced homology only; one augmentation rank in dimension zero.
    out={}
    for d in range(ds+1):
        z=len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)-(1 if d==0 else 0)
        if z: out[d]=z
    return out


def theory(s,sizes):
    r=len(sizes)
    alpha=1; beta=1
    for q in sizes:
        alpha*=comb(q-1,2); beta*=q-1
    return {1:comb(s,2),r:s*beta,2*r-1:alpha}


def fixed_lefschetz(by_dim,n,perm):
    tr=-1  # reduced augmentation empty simplex
    for d,fs in by_dim.items():
        for face in fs:
            images=[perm[i] for i in range(n) if face&(1<<i)]
            if sum(1<<j for j in images)!=face:continue
            inversion=sum(a>b for i,a in enumerate(images) for b in images[i+1:])
            tr+=(-1)**(d+inversion)
    return tr


def check(s,sizes):
    r=len(sizes); assert r>=2 and s>=2 and min(sizes)>=3
    fs,vs=build(s,sizes)
    calc=betti(fs); want={k:v for k,v in theory(s,sizes).items() if v}
    assert calc==want,(s,sizes,calc,want)
    euler=sum((-1)**d*len(v) for d,v in fs.items())-1
    pred=sum((-1)**d*v for d,v in want.items())
    assert euler==pred
    # Swap two common vertices and compare signed chain Lefschetz with
    # independently derived rational characters of the three homology degrees.
    perm=list(vs);perm[0],perm[1]=perm[1],perm[0]
    f=s-2; tr1=comb(f,2)-1
    beta=1;alpha=1
    for q in sizes:beta*=q-1;alpha*=comb(q-1,2)
    predicted=-tr1+(-1)**r*f*beta-alpha
    trace=fixed_lefschetz(fs,len(vs),perm)
    assert trace==predicted,(s,sizes,trace,predicted)
    # A private-vertex transposition has eigenvalues +1 (multiplicity q-2)
    # and -1 (multiplicity one) on the augmentation lattice.
    p0=s; q0=sizes[0]
    private=list(vs);private[p0],private[p0+1]=private[p0+1],private[p0]
    private_utrace=q0-3
    private_ext2trace=comb(q0-2,2)-(q0-2)
    other_beta=1; other_alpha=1
    for q in sizes[1:]:
        other_beta*=q-1;other_alpha*=comb(q-1,2)
    private_pred=-comb(s,2)+(-1)**r*s*private_utrace*other_beta-private_ext2trace*other_alpha
    private_actual=fixed_lefschetz(fs,len(vs),private)
    assert private_actual==private_pred,(s,sizes,private_actual,private_pred)
    # Exchange two identically sized complete-graph pages; induced graded
    # swap has Koszul sign - on joins of discrete sets, + on joins of circles.
    if len(sizes)>=3 and sizes[0]==sizes[1]:
        swap=list(vs);q0=sizes[0]
        for i in range(q0):swap[s+i],swap[s+q0+i]=swap[s+q0+i],swap[s+i]
        other_beta=1;other_alpha=1
        for q in sizes[2:]:
            other_beta*=q-1;other_alpha*=comb(q-1,2)
        page_hr=-s*(q0-1)*other_beta
        page_hhigh=comb(q0-1,2)*other_alpha
        page_pred=-comb(s,2)+(-1)**r*page_hr-page_hhigh
        page_actual=fixed_lefschetz(fs,len(vs),swap)
        assert page_actual==page_pred,(s,sizes,page_actual,page_pred)
    print('OK',s,sizes,'faces',sum(map(len,fs.values())),
          'betti',sorted(calc.items()),'common_transposition_reduced_lefschetz',trace)

if __name__=='__main__':
    for data in [(3,(3,3)),(3,(3,3,3)),(4,(3,3)),(4,(3,3,3)),
                 (3,(4,3,3)),(5,(3,3)),(3,(3,4)),(3,(4,4)),(3,(3,3,3,3))]:
        check(*data)
    print('COMMON_CORE_CLIQUE_BOOK_PASS')
