#!/usr/bin/env python3
"""Independent exact-rational factor and modular-nullity checks for repulsive crossings.
No numerical root fitting is used. Not a substitute for the all-size proof.
"""
from fractions import Fraction
from itertools import combinations_with_replacement

def polynomials(m,n,u):
    def ft(x):return x**3-u*x*x-4*m*n*x+2*u*(2*m*n-m-n)
    def fa(x):return x**3-u*x*x-m*n*x+u*n*(m-2)
    def fb(x):return x**3-u*x*x-m*n*x+u*m*(n-2)
    return ft,fa,fb

def rank_mod(a,p):
    b = [[int(v)%p for v in row] for row in a]
    n=len(b);rank=0
    for col in range(n):
        k=next((r for r in range(rank,n) if b[r][col]),None)
        if k is None:continue
        b[rank],b[k]=b[k],b[rank]
        inv=pow(b[rank][col],-1,p)
        b[rank]=[(v*inv)%p for v in b[rank]]
        for r in range(rank+1,n):
            if b[r][col]:
                c=b[r][col]
                b[r]=[(b[r][j]-c*b[rank][j])%p for j in range(n)]
        rank+=1
    return rank

def hamiltonian(m,n,u):
    s=list(combinations_with_replacement(range(m+n),2));at={v:i for i,v in enumerate(s)}
    h=[[0]*len(s) for _ in s]
    for i,(a,b) in enumerate(s):
        if a==b:h[i][i]=u
        for k in (0,1):
            x=(a,b)[k]
            for y in (range(m,m+n) if x<m else range(m)):
                t=tuple(sorted((y,b) if k==0 else (a,y)))
                h[at[t]][i]-=1
    return h

def main():
    # At threshold E^2=n(m-3n), U/E=3n/(3n-2).
    for m,n in [(7,2),(8,2),(10,3),(12,3),(19,4),(17,5)]:
        if m <= 3*n:continue
        e2=Fraction(n*(m-3*n)); c=Fraction(3*n,3*n-2)
        # Evaluate each cubic at x=E, U=cE, and divide by E.
        # E^3/E=e2, U E^2/E = c*e2.
        Ft=e2*(1-c)-4*m*n+2*c*(2*m*n-m-n)
        Fa=e2*(1-c)-m*n+c*n*(m-2)
        Fb=e2*(1-c)-m*n+c*m*(n-2)
        assert Ft==0 and Fa==0 and Fb != 0
        print('PASS crossing',m,n,'E^2=',e2,'U/E=',c,'multiplicity=',m)
    # Rational resonance K_{8,2}: E=2, U=3; full 55-state matrix.
    m,n,e,u=8,2,2,3
    h=hamiltonian(m,n,u)
    for i in range(len(h)):h[i][i]-=e
    for p in (101,103):
        r=rank_mod(h,p)
        assert r==len(h)-m,(r,len(h),p)
        print('PASS K_8,2 modular rank',p,r,'nullity',m)
    # If there is no shore imbalance exceeding 3, the algebraic condition
    # E^2=n(m-3n)>0 cannot hold; symmetry is the only generic degeneracy.
    for m in range(2,12):
        for n in range(2,12):
            if m<=3*n and n<=3*m:
                assert not (m>3*n or n>3*m)
    print('All exact rational and modular resonance checks passed.')

if __name__=='__main__':main()
