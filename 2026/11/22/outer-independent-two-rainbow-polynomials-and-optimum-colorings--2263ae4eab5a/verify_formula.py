"""Recompute the weight polynomial by intersecting-family classification and two-color inclusion-exclusion."""
from itertools import combinations
from math import comb
from collections import Counter

def poly(n,Z):
    edges=list(combinations(range(n),2))
    zs=set(Z)
    others=[e for e in edges if e not in zs]
    # allowed color bits: for a zero edge, 2-color absent if no disjoint color-labelled other edge
    # An event choice A, B enforces no 1/2 on neighbors of those zero edges.
    coeff=Counter()
    s=len(Z)
    for redmask in range(1<<s):
        for bluemask in range(1<<s):
            p=[1]
            for e in others:
                one=all(set(e)&set(Z[i]) for i in range(s) if redmask>>i&1)
                two=all(set(e)&set(Z[i]) for i in range(s) if bluemask>>i&1)
                v=int(one)+int(two)
                w=int(one and two)
                if not v: p=[];break
                nxt=[0]*(len(p)+2)
                for j,a in enumerate(p):
                    nxt[j+1]+=a*v
                    nxt[j+2]+=a*w
                p=nxt
            sign=-1 if (redmask.bit_count()+bluemask.bit_count())%2 else 1
            for k,v in enumerate(p):coeff[k]+=sign*v
    return coeff

def calc(n):
    E=comb(n,2)
    out=Counter()
    # (2z+z^2)^E = z^E (2+z)^E
    for t in range(E+1):out[E+t]+=comb(E,t)*2**(E-t)
    ones=poly(n,((0,1),))
    for k,v in ones.items():out[k]+=E*v
    for s in range(2,n):
        Z=tuple((0,j) for j in range(1,s+1))
        c=poly(n,Z)
        for k,v in c.items():out[k]+=n*comb(n-1,s)*v
    tri=poly(n,((0,1),(0,2),(1,2)))
    for k,v in tri.items():out[k]+=comb(n,3)*v
    return {k:v for k,v in sorted(out.items()) if v}

def min_formula(n):
    m=n-1
    C=comb(m,2)
    bad=1+C+m*(2**(m-1)-m)
    return n*(2**C-2*bad)

def main():
    for n in [5,6]:
        out=calc(n)
        k=min(out)
        assert k==comb(n,2)-n+1, (n,k)
        assert out[k]==min_formula(n), (n,out[k],min_formula(n))
        print('n=',n,'min=',k,'optimal=',out[k],'polynomial=',out)
    for n in [5,6,7,8,9]:print('optimal',n,min_formula(n))
if __name__=='__main__': main()
