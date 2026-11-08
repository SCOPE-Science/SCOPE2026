"""Finite checks for the open-neighborhood complex of K_2 square K_n.
The all-parameter statement is proved by the cover and homotopy-pushout argument,
not by these finite computations. Standard-library Python 3 only.
"""
from itertools import permutations
from collections import Counter

def faces_from_facet_masks(facets):
    faces = {0}
    for facet in facets:
        sub = facet
        while True:
            faces.add(sub)
            if sub == 0: break
            sub = (sub-1) & facet
    return faces

def get_complex(n):
    def A(i): return 1 << i
    def B(i): return 1 << (n+i)
    u = []
    v = []
    for k in range(n):
        u.append(sum(A(i) for i in range(n) if i != k) | B(k))
        v.append(sum(B(i) for i in range(n) if i != k) | A(k))
    fu, fv = faces_from_facet_masks(u), faces_from_facet_masks(v)
    x = fu | fv
    h = fu & fv
    return x, fu, fv, h

def rank_mod2(columns):
    pivots = {}
    for col in columns:
        while col:
            pivot=col.bit_length()-1
            if pivot in pivots: col ^= pivots[pivot]
            else:
                pivots[pivot]=col
                break
    return len(pivots)

def bettis(faces):
    by_dim = {}
    for f in faces:
        if f: by_dim.setdefault(f.bit_count()-1,[]).append(f)
    dims = sorted(by_dim)
    ranks={}
    for d in dims:
        if not d: ranks[d]=0;continue
        indices={f:k for k,f in enumerate(by_dim[d-1])}
        boundaries=[]
        for f in by_dim[d]:
            col=0
            subset=f
            while subset:
                bit=subset & -subset
                col ^= 1 << indices[f^bit]
                subset-=bit
            boundaries.append(col)
        ranks[d]=rank_mod2(boundaries)
    betti={d:len(by_dim[d])-ranks[d]-ranks.get(d+1,0) for d in dims}
    betti[0]-=1
    return {d:b for d,b in betti.items() if b}, [len(by_dim[d]) for d in dims]

def signed_trace(faces,p,sw,n):
    result=0
    for mask in faces:
        if not mask:continue
        src=[i for i in range(2*n) if mask>>i&1]
        dst=[(n if ((i>=n)^sw) else 0)+p[i%n] for i in src]
        if sum(1<<v for v in dst)!=mask: continue
        inversions=sum(a>b for i,a in enumerate(dst) for b in dst[i+1:])
        result += (-1)**(len(src)-1+inversions)
    return result-1 # reduced chain Lefschetz number, subtract trace on H_0

def cyc2(p):
    return sum(p[p[i]]==i and p[i]!=i for i in range(len(p)))//2

def fixed(p):return sum(i==a for i,a in enumerate(p))

def verify():
    for n in range(4,9):
        faces,u,v,h = get_complex(n)
        h_expected={0}|{1<<i for i in range(2*n)}|{(1<<i)|(1<<(n+j)) for i in range(n) for j in range(n) if i!=j}
        assert h==h_expected, ('intersection not crown graph',n)
        # Both side subcomplexes are a simplex boundary plus cones on its facets.
        for side,other in [(u,0),(v,n)]:
            base = {mask<<other for mask in range(1<<n) if mask!=(1<<n)-1}
            assert base <= side
            for i in range(n):
                tip = (n if other==0 else 0)+i
                with_tip={f for f in side if f>>tip&1}
                expected={((mask<<other)|(1<<tip)) for mask in range(1<<n) if not (mask>>i&1)}
                assert with_tip==expected
        rank=(n*n-3*n+1)
        expected = {2:rank,n-2:2}
        if n==4:expected={2:rank+2}
        b,fv=bettis(faces)
        assert b==expected, ('Betti mismatch',n,b,expected)
        assert sum(fv)==len(faces)-1
        assert len(h)-1==2*n+n*(n-1)
        print('n',n,'nonempty_faces',len(faces)-1,'f_vector',fv,'betti_mod2',b,'crown_cycle_rank',rank)
    for n in (5,6):
        faces,*_=get_complex(n)
        tests=0
        for p in permutations(range(n)):
            f=fixed(p)
            twos=cyc2(p)
            parity=(-1)**sum(a>b for i,a in enumerate(p) for b in p[i+1:])
            for sw in (0,1):
                t2=(2*twos-1) if sw else f*f-3*f+1
                ttop=0 if sw else 2*parity
                predicted=t2+(-1)**(n-2)*ttop
                observed=signed_trace(faces,p,sw,n)
                assert observed==predicted,('Lefschetz discrepancy',n,p,sw,observed,predicted)
                tests+=1
        print('n',n,'equivariant_lefschetz_checks',tests,'ALL_MATCH')
    print('ALL_CHECKS_PASS')
if __name__=='__main__':verify()
