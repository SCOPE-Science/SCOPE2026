"""Exact small-instance check of root connectivity decomposition for clique bouquets."""
from fractions import Fraction
from itertools import combinations
from math import comb

def check_block(s, p):
    vertices = range(s)
    edges = list(combinations(vertices,2))
    all_edges=[(-1,v) for v in vertices]+edges
    q=1-p
    checks=0
    total_A=total_Z=total_B=total_B2=Fraction(0)
    total_err=Fraction(0)
    for mask in range(1<<len(all_edges)):
        opened={e for idx,e in enumerate(all_edges) if mask>>idx&1}
        h={v for v in vertices if (-1,v) in opened}
        intr={e for e in edges if e in opened}
        k=mask.bit_count()
        wt=p**k*q**(len(all_edges)-k)
        visited={-1}; frontier=[-1]
        while frontier:
            u=frontier.pop()
            for a,b in opened:
                if a==u and b not in visited:
                    visited.add(b);frontier.append(b)
                if b==u and a not in visited:
                    visited.add(a);frontier.append(a)
        B=len((visited-{-1})-h)
        N={v:sum(1 for u in h if u!=v and tuple(sorted([u,v])) in intr) for v in vertices if v not in h}
        B2=sum(k>=1 for k in N.values())
        Z=sum(N.values())
        assert B2 <= B and B2 <= Z
        total_A+=wt*len(h)
        total_B+=wt*B
        total_Z+=wt*Z
        total_B2+=wt*B2
        total_err+=wt*abs(B-Z)
        checks+=3
    assert total_A == s*p, (s,p,total_A,s*p)
    assert total_Z == s*(s-1)*p*p*q, (s,p,total_Z,s*(s-1)*p*p*q)
    assert total_B <= s
    if s*p<1:
        upper=Fraction(s**3)*p**3/(1-s*p)+Fraction(s**3)*p**4
        assert total_err<=upper, (s,p,total_err,upper)
    checks+=4
    print('s',s,'p',p,'E(A)',total_A,'E(B)',total_B,'E(Z)',total_Z,'E(B2)',total_B2,'E|B-Z|',total_err,'assertions',checks)
    return checks

if __name__=='__main__':
    total=0
    for s in range(1,6):
        for p in (Fraction(1,2*s+1), Fraction(1,3*s+2)):
            total+=check_block(s,p)
    print('PASS assertions',total)
