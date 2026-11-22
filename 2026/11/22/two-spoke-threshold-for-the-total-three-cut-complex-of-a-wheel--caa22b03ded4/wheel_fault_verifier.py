"""Finite independent verification of two-spoke wheel total-three-cut theorem."""
from itertools import combinations

def all_faces(facets):
    ans={frozenset()}
    for f in facets:
        t=tuple(f)
        for k in range(len(t)+1):
            for x in combinations(t,k): ans.add(frozenset(x))
    return ans

def total3(n, faults):
    # rim 0,...,n-1, hub n; defect spokes h-i
    V=tuple(range(n+1))
    E={frozenset((i,(i+1)%n)) for i in range(n)}
    E.update(frozenset((n,i)) for i in range(n) if i not in faults)
    triples=[frozenset(t) for t in combinations(V,3) if all(frozenset(p) not in E for p in combinations(t,2))]
    return all_faces([frozenset(V)-t for t in triples])

def bettis(faces):
    # Reduced simplicial homology over F_2, including augmentation.
    fs=[sorted((x for x in faces if len(x)==i),key=lambda f:tuple(sorted(f))) for i in range(max(map(len,faces))+1)]
    ranks=[]
    for k in range(1,len(fs)):
        ids={f:j for j,f in enumerate(fs[k-1])}
        piv={}
        for f in fs[k]:
            v=0
            for x in f: v ^=1 <<ids[f-{x}]
            while v:
                b=v.bit_length()-1
                if b in piv:v ^=piv[b]
                else:piv[b]=v; break
        ranks.append(len(piv))
    return {k-1:len(fs[k])-ranks[k-1]-(ranks[k] if k<len(ranks) else 0) for k in range(1,len(fs)) if len(fs[k])-ranks[k-1]-(ranks[k] if k<len(ranks) else 0)}

def expected_t(n,a,b):
    A=set(range(n))-{a,b}
    Na={(a-1)%n,(a+1)%n};Nb={(b-1)%n,(b+1)%n}
    W=Na|Nb; U=A-W
    if len(U)==0:
        assert n==6 and ((a-b)%n==3)
        return all_faces([Na,Nb])
    F=[]
    # all subsets not containing U: facets (U-{u}) union W.
    for u in U:F.append((U-{u})|W)
    if Na&Nb:
        assert len(Na&Nb)==1
        F.append(U)
    else:
        F += [U|Na,U|Nb]
    return all_faces(F)

if __name__=='__main__':
    count=0
    for n in range(6,13):
        base=total3(n,set());assert base
        for a,b in combinations(range(n),2):
            fault=total3(n,{a,b})
            adjacent=(a-b)%n in (1,n-1)
            B=base
            A=set(range(n))-{a,b}
            if adjacent:
                assert fault==base,(n,a,b)
            else:
                D=all_faces([A]);assert fault==base|D,(n,a,b,'union')
                T={f for f in base if f<=A}
                assert T==expected_t(n,a,b),(n,a,b,'T')
                hs=bettis(fault)
                assert hs=={n-5:1},(n,a,b,hs)
            count+=1
        print('n',n,'checked',n*(n-1)//2)
    print('PASS',count,'two-spoke deletion pairs, exact face decompositions and mod-two homology')
