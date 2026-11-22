#!/usr/bin/env python3
"""Exact type-profile enumeration and bounded-degree polynomial certificate."""
from itertools import product
from fractions import Fraction


def types(a, b):
    """(lower mask, upper mask) over two unrelated named chains."""
    n = a+b
    answer = []
    # A downset is a prefix of each chain; an upset is a suffix.
    for i,j,k,l in product(range(a+1),range(b+1),range(a+1),range(b+1)):
        L = sum(1 << q for q in range(i)) + sum(1 << (a+q) for q in range(j))
        U = sum(1 << q for q in range(k,a)) + sum(1 << (a+q) for q in range(l,b))
        if L & U:
            continue
        if L and U:
            if i and j: continue
            if k < a and l < b: continue
            if i and l < b: continue
            if j and k < a: continue
        answer.append((L,U))
    assert len(answer)==len(set(answer))
    return answer


def counts(a,b):
    ts=types(a,b)
    C = I = 0
    for L,U in ts:
        for K,V in ts:
            C += (L & ~K == 0) and (V & ~U == 0)
            I += not (U & K or V & L)
    return len(ts),C,I


def formula(a,b):
    N=Fraction(a*a+4*a*b+3*a+b*b+3*b+2,2)
    H=(a**3+b**3+6*a*b*(a+b)+5*(a*a+b*b)+14*a*b+8*(a+b)+4)
    C=(2*N*N+H)/6
    I=N*(2*N+1)/3
    assert N.denominator==C.denominator==I.denominator==1
    return int(N),int(C),int(I)


def polynomial_degree_certificate():
    # Directly enumerated values constitute a 5x5 interpolation grid.
    # Mathematical lemma supplied in accompanying proof: each of the
    # four cut variables per old chain has a finite order-pattern stratum;
    # each stratum has binomial-polynomial count of degree at most four.
    rows=[]
    for a,b in list(product(range(1,6),repeat=2)) + [(0,t) for t in range(1,6)] + [(t,0) for t in range(1,6)] + [(0,0)]:
        got=counts(a,b); want=formula(a,b)
        assert got==want, (a,b,got,want)
        rows.append((a,b,*got))
    print('POSITIVE_INTERPOLATION_GRID_AND_BOUNDARIES_OK',len(rows))
    print('GRID',rows)
    for a,b in [(0,7),(2,6),(3,7),(5,5),(7,3),(8,1),(9,0)]:
        assert counts(a,b)==formula(a,b), (a,b)
    print('OUT_OF_GRID_SPOT_CHECKS_OK',7)


def direct_consistency(a,b,typ1,typ2,relation):
    """Independent finite-poset transitive-closure check, not using formulas."""
    n=a+b;x=n;y=n+1;N=n+2
    L,U=typ1;K,V=typ2
    reach=[[False]*N for _ in range(N)]
    for c,d in [(0,a),(a,n)]:
        for i in range(c,d):
            for j in range(i+1,d): reach[i][j]=True
    for z,(lower,upper) in [(x,(L,U)),(y,(K,V))]:
        for i in range(n):
            if lower>>i&1:reach[i][z]=True
            if upper>>i&1:reach[z][i]=True
    if relation=='<':reach[x][y]=True
    if relation=='>':reach[y][x]=True
    for k in range(N):
        for i in range(N):
            if reach[i][k]:
                for j in range(N):
                    if reach[k][j]:reach[i][j]=True
    if any(reach[i][i] for i in range(N)):return False
    for i in range(n):
        for j in range(n):
            old=(i<a)==(j<a) and i<j
            if reach[i][j]!=old:return False
        for z,(lower,upper) in [(x,(L,U)),(y,(K,V))]:
            if reach[i][z]!=bool(lower>>i&1):return False
            if reach[z][i]!=bool(upper>>i&1):return False
    return ((reach[x][y],reach[y][x])==
            {'<':(True,False),'>':(False,True),'||':(False,False)}[relation])


def independent_extension_checks():
    tested=0
    for a,b in product(range(3),repeat=2):
        ts=types(a,b)
        for p in ts:
            for q in ts:
                L,U=p;K,V=q
                conditions={'<': (L & ~K == 0) and (V & ~U == 0),
                            '>': (K & ~L == 0) and (U & ~V == 0),
                            '||': not(U & K or V & L)}
                for relation,expect in conditions.items():
                    actual=direct_consistency(a,b,p,q,relation)
                    assert actual==expect,(a,b,p,q,relation,expect,actual)
                    tested+=1
    print('INDEPENDENT_TRANSITIVE_CLOSURE_OK',tested)

if __name__=='__main__':
    polynomial_degree_certificate()
    independent_extension_checks()
    print('VERIFICATION_OK')
