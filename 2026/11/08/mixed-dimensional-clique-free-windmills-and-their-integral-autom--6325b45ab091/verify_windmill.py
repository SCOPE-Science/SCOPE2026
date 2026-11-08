#!/usr/bin/env python3
"""Direct simplicial enumeration and character checks for clique-free windmills.
Standard library only; runnable as: python verify_windmill.py
"""
from itertools import combinations, product, permutations
from math import comb, prod

CASES = [
    (3, (2,2)), (3,(3,3)), (3,(4,3)), (3,(4,4)),
    (3,(2,2,2)), (3,(2,3,2)), (3,(3,3,3)), (3,(3,3,2)),
    (4,(3,3)), (4,(3,4)), (4,(4,4)), (4,(5,3)),
    (5,(4,4)), (5,(5,5)), (4,(2,4)), (5,(3,5)),
]

def graph(t, sizes):
    blocks=[]; edges=set(); n=1
    for a in sizes:
        b=tuple(range(n,n+a)); n+=a; blocks.append(b)
        for x in b:
            edges.add((0,x))
        for x,y in combinations(b,2): edges.add((x,y))
    return n, blocks,edges

def free_faces(t,sizes):
    n,blocks,edges=graph(t,sizes)
    # independent definition: enumerate all induced t-cliques in graph
    forb=[]
    for F in combinations(range(n),t):
        if all(tuple(sorted(e)) in edges for e in combinations(F,2)):
            forb.append(sum(1<<i for i in F))
    faces=[[] for _ in range(n)]
    for mask in range(1,1<<n):
        if any(mask&f==f for f in forb):continue
        verts=tuple(i for i in range(n) if mask>>i&1)
        faces[len(verts)-1].append(verts)
    while faces and not faces[-1]:faces.pop()
    return n,blocks,faces

def rank_gf2(cols):
    piv={}
    for col in cols:
        while col:
            k=col.bit_length()-1
            if k in piv:col^=piv[k]
            else:piv[k]=col;break
    return len(piv)

def betti_mod2(faces):
    # augmented chain includes (-1)-chain of rank 1
    ranks=[]
    for dim, fset in enumerate(faces):
        if dim==0: ranks.append(1 if fset else 0);continue
        lower={F:i for i,F in enumerate(faces[dim-1])}
        cols=[]
        for F in fset:
            col=0
            for j in range(len(F)):
                col^=1<<lower[F[:j]+F[j+1:]]
            cols.append(col)
        ranks.append(rank_gf2(cols))
    return {d:len(faces[d])-ranks[d]-(ranks[d+1] if d+1<len(ranks) else 0)
            for d in range(len(ranks)) if len(faces[d])-ranks[d]-(ranks[d+1] if d+1<len(ranks) else 0)}

def predicted(t,sizes):
    k=len(sizes)
    a=prod(comb(n-1,t-1) for n in sizes)
    b=prod(comb(n-1,t-2) for n in sizes)
    out={}
    if a:out[k*(t-1)-1]=a
    if b:out[k*(t-2)]=b
    return out

def ext_trace(p,a):
    # coefficient of z^a in det(I+z perm representation)/(1+z)
    seen=set(); cycles=[]
    for i in range(len(p)):
        if i in seen:continue
        j=i; l=0
        while j not in seen:
            seen.add(j);l+=1;j=p[j]
        cycles.append(l)
    c=[1]+[0]*a
    for l in cycles:
        for j in range(a,l-1,-1):
            c[j]+=(-1)**(l+1)*c[j-l]
    e=0
    for j in range(a+1): e+=(-1)**(a-j)*c[j]
    return e

def parity(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2

def tr_hom(t, blocks, perm, a):
    # Detect induced block permutation and composed monodromy at each orbit of blocks
    idx={v:i for i,b in enumerate(blocks) for v in b}
    bp=tuple(idx[perm[b[0]]] for b in blocks)
    assert sorted(bp)==list(range(len(blocks)))
    total=(-1)**(a*parity(bp))
    seen=set()
    for i in range(len(blocks)):
        if i in seen:continue
        j=i; cyc=[]
        while j not in seen:
            seen.add(j);cyc.append(j);j=bp[j]
        st=blocks[i]
        pos={v:z for z,v in enumerate(st)}
        mon=list(range(len(st)))
        for ii in cyc:
            target=blocks[bp[ii]]
            local={v:z for z,v in enumerate(target)}
            mon=[local[perm[blocks[ii][x]]] for x in mon]
        assert sorted(mon)==list(range(len(st)))
        total*=ext_trace(mon,a)
    return total

def perm_action(blocks, kind, extra=False):
    n=1+sum(len(b) for b in blocks)
    p=list(range(n))
    if kind=='identity':pass
    elif kind=='local_transposition':
        b=next(b for b in blocks if len(b)>=2);p[b[0]],p[b[1]]=p[b[1]],p[b[0]]
    elif kind=='local_cycle':
        b=next(b for b in blocks if len(b)>=2)
        for z in range(len(b)):p[b[z]]=b[(z+1)%len(b)]
    elif kind=='block_swap':
        pair=next(((a,b) for a,b in combinations(blocks,2) if len(a)==len(b)),None)
        if pair is None:return None
        for x,y in zip(*pair):p[x],p[y]=p[y],p[x]
    elif kind=='swap_twist':
        pair=next(((a,b) for a,b in combinations(blocks,2) if len(a)==len(b)),None)
        if pair is None:return None
        a,b=pair
        for x,y in zip(a,b):p[x],p[y]=p[y],p[x]
        p[a[0]],p[a[1]]=p[a[1]],p[a[0]]
    else:raise ValueError(kind)
    return p

def fixed_lefschetz(faces,p):
    s=-1
    for d,fs in enumerate(faces):
        for F in fs:
            T=[p[v] for v in F]
            if sorted(T)!=list(F):continue
            s+=(-1)**d*(-1)**parity(T)
    return s

def exhaustive_symmetry(t, sizes):
    _,blocks,faces=free_faces(t,sizes)
    k=len(blocks); n=1+sum(sizes); total=0
    localopts=[list(permutations(range(a))) for a in sizes]
    for bp in permutations(range(k)):
        if any(sizes[i]!=sizes[bp[i]] for i in range(k)):continue
        for maps in product(*localopts):
            p=list(range(n))
            for i,b in enumerate(blocks):
                target=blocks[bp[i]]
                for x,v in enumerate(b):p[v]=target[maps[i][x]]
            lf=fixed_lefschetz(faces,p)
            hi=k*(t-1)-1; lo=k*(t-2)
            pred=(-1)**hi*tr_hom(t,blocks,p,t-1)+(-1)**lo*tr_hom(t,blocks,p,t-2)
            assert lf==pred,(t,sizes,bp,maps,lf,pred)
            total+=1
    return total

def run():
    total_faces=0;total_cases=0;total_char=0
    for t,sizes in CASES:
        n,blocks,faces=free_faces(t,sizes)
        actual=betti_mod2(faces)
        expect=predicted(t,sizes)
        assert actual==expect,(t,sizes,actual,expect)
        for kind in ('identity','local_transposition','local_cycle','block_swap','swap_twist'):
            perm=perm_action(blocks,kind)
            if perm is None:continue
            lf=fixed_lefschetz(faces,perm)
            k=len(blocks); p=k*(t-1)-1; q=k*(t-2)
            rhs=(-1)**p*tr_hom(t,blocks,perm,t-1)+(-1)**q*tr_hom(t,blocks,perm,t-2)
            assert lf==rhs,(t,sizes,kind,lf,rhs)
            total_char+=1
        total_cases+=1
        count=sum(map(len,faces));total_faces+=count
        print(f'PASS t={t} sizes={sizes} faces={count} mod2={actual}')
    for t,sizes in [(3,(3,3)),(3,(4,3)),(3,(3,3,3)),(3,(4,4)),(4,(4,4))]:
        total=exhaustive_symmetry(t,sizes)
        print(f'PASS exhaustive t={t} sizes={sizes} automorphisms={total}')
        total_char+=total
    print(f'ALL_VERIFY_OK cases={total_cases} simplices={total_faces} character_tests={total_char}')

if __name__=='__main__':run()
