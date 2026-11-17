#!/usr/bin/env python3
"""Exact rational projection certificates for the zero-diagonal Birkhoff face."""
from fractions import Fraction
from itertools import permutations
from math import factorial


def perm_matrix(p):
    n=len(p)
    return [[int(j==p[i]) for j in range(n)] for i in range(n)]


def candidate(p):
    n=len(p)
    k=sum(i==p[i] for i in range(n))
    if k==0:
        return [[Fraction(int(j==p[i])) for j in range(n)] for i in range(n)]
    d=n+k*k-2
    b=Fraction(1,d)
    a=(k+2)*b
    c=1-k*b
    f={i for i in range(n) if i==p[i]}
    x=[[Fraction(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if i in f and j in f: x[i][j]=a
            elif (i in f)!=(j in f): x[i][j]=b
            elif j==p[i]: x[i][j]=c
    return x


def exact_check(p):
    n=len(p);k=sum(i==p[i] for i in range(n));x=candidate(p)
    assert all(x[i][i]==0 for i in range(n))
    assert all(z>=0 for row in x for z in row)
    assert all(sum(row)==1 for row in x)
    assert all(sum(x[i][j] for i in range(n))==1 for j in range(n))
    val=sum((Fraction(int(j==p[i]))-x[i][j])**2 for i in range(n) for j in range(n))
    want=Fraction(k) + (Fraction(k*(k+2),n+k*k-2) if k else 0)
    assert val==want,(p,val,want)
    if k:
        b=Fraction(1,n+k*k-2)
        # Residual of P-X has a row/column potential on positive X entries,
        # and a nonpositive gap on every zero allowed entry: projection KKT.
        t=[-Fraction(k+2,2)*b if i==p[i] else Fraction(k,2)*b for i in range(n)]
        for i in range(n):
            for j in range(n):
                if i==j: continue
                r=Fraction(int(j==p[i]))-x[i][j]
                if x[i][j]>0: assert r==t[i]+t[j],(p,i,j,r,t[i]+t[j])
                else: assert r<=t[i]+t[j],(p,i,j,r,t[i]+t[j])
    return k,val


def count_derangements(m):
    return sum((-1)**j * (factorial(m)//factorial(j)) for j in range(m+1))


def main():
    total=0
    for n in range(3,8):
        counts={}
        for p in permutations(range(n)):
            k,val=exact_check(p);total+=1
            counts[k]=counts.get(k,0)+1
        for k,num in counts.items():
            assert num==factorial(n)//factorial(k)//factorial(n-k)*count_derangements(n-k)
        assert max(counts)==n and n-1 not in counts
        assert all(Fraction(k)+Fraction(k*(k+2),n+k*k-2)<Fraction(n*n,n-1) for k in counts if k<n)
        assert Fraction(n*n,n-1)-(Fraction(n-2)+Fraction(n*(n-2),n+(n-2)**2-2))==2
        print('order',n,'perms',factorial(n),'fixed_point_shells',sorted(counts.items()))
    print('DERANGEMENT_PROJECTION_PASS exhaustive_permutations=',total,'exact_KKT=PASS','vertex_gap_squared=2')

if __name__=='__main__': main()
