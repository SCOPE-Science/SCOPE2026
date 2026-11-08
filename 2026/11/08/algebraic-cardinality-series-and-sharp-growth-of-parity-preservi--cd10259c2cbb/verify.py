#!/usr/bin/env python3
"""Independent finite enumeration and exact series checks for a fence inverse-monoid count."""
from fractions import Fraction
from itertools import combinations
from math import comb, sqrt, pi


def actual_count(n):
    # Definition-level enumeration: every increasing map is uniquely determined
    # by two equicardinal subsets of [n], paired in increasing order.
    subsets = [tuple(c) for k in range(n+1) for c in combinations(range(1,n+1),k)]
    by_rank = [[] for _ in range(n+1)]
    for sub in subsets:
        by_rank[len(sub)].append(sub)
    count = 0
    for family in by_rank:
        for domain in family:
            for image in family:
                if any((a-b)&1 for a,b in zip(domain,image)):
                    continue
                # For fence adjacency: i and j are comparable precisely if |i-j|=1.
                # Because parity is preserved, the orientation is preserved whenever
                # the source and image adjacencies coincide. Check both directions.
                okay = True
                for i in range(len(domain)):
                    for j in range(i+1,len(domain)):
                        if (domain[j]-domain[i]==1)!=(image[j]-image[i]==1):
                            okay=False;break
                    if not okay:break
                if okay:count+=1
    return count


def coefficients_by_algebraic_identity(N):
    # P(z)=(1+z)(1-2z^2)(1-3z+2z^2-2z^3)
    # =1-2z-3z^2+4z^3+4z^6.
    P={0:1,1:-2,2:-3,3:4,6:4}
    # coefficients u_n for U(z)=P(z)^(-1/2)
    u=[Fraction(1)]
    for n in range(1,N+2):
        v=sum(2*P[j]*(n-j)*u[n-j] for j in P if 1<=j<=n-1)
        v+=sum(j*P[j]*u[n-j] for j in P if 1<=j<=n)
        u.append(-v/Fraction(2*n))
    # F(z)=((1-z^2)U(z)-1)/z.
    a=[]
    for n in range(N+1):
        y=u[n+1]-(u[n-1] if n>=1 else 0)
        assert y.denominator==1,(n,y)
        a.append(int(y))
    # Square identity P(z)(1+zF(z))^2=(1-z^2)^2;
    # checked through degree N+1 for the computed rational coefficients.
    g=[1]+a
    lhs=[0]*(N+2)
    for i,ai in enumerate(g):
        for j,bj in enumerate(g):
            for k,pk in P.items():
                if i+j+k<=N+1:
                    lhs[i+j+k]+=ai*bj*pk
    rhs=[0]*(N+2)
    for k,val in ((0,1),(2,-2),(4,1)):
        if k<=N+1: rhs[k]=val
    assert lhs==rhs,(lhs,rhs)
    return a


def independent_gap_count(n):
    if n==0:return 1
    # Dynamic enumeration using exactly three possible gap classes.
    D = {(0,0): 1}
    total=1 # empty map
    for start_a in range(1,n+1):
        for start_b in range(1,n+1):
            if (start_a-start_b)%2:continue
            # Each initial pair gives a rank-one map.
            total+=1
            levels={(start_a,start_b):1}
            for _ in range(1,n):
                nextlevels={}
                for (a,b),v in levels.items():
                    for da in range(1,n-a+1):
                        for db in range(1,n-b+1):
                            if (da==1 and db==1) or (da>=2 and db>=2 and da%2==db%2):
                                key=(a+da,b+db)
                                nextlevels[key]=nextlevels.get(key,0)+v
                if not nextlevels:break
                total+=sum(nextlevels.values())
                levels=nextlevels
    return total

if __name__=='__main__':
    coeff=coefficients_by_algebraic_identity(32)
    assert coeff[:17]==[1,2,4,10,22,52,120,286,678,1628,3912,9460,22924,55752,135872,331926,812310]
    print('EXACT_SERIES_OK n=0..32')
    for n in range(0,12):
        brute=actual_count(n)
        assert brute==coeff[n],(n,brute,coeff[n])
        print('DIRECT_MONOID_OK n=%d count=%d'%(n,brute))
    for n in range(0,7):
        gap=independent_gap_count(n)
        assert gap==coeff[n],(n,gap,coeff[n])
    print('GAP_CONSTRUCTION_OK n=0..6')
    import mpmath as mp
    mp.mp.dps=55
    rho=mp.findroot(lambda z:1-3*z+2*z*z-2*z**3, (mp.mpf('.39'),mp.mpf('.4')))
    deriv=-2-6*rho+12*rho**2+24*rho**5
    C=(1-rho**2)/(rho*mp.sqrt(-mp.pi*rho*deriv))
    assert mp.mpf('.396')<rho<mp.mpf('.397')
    assert mp.mpf('1.267')<C<mp.mpf('1.268')
    print('ASYMPTOTIC_CONSTANT_OK rho=%s C=%s'%(mp.nstr(rho,30),mp.nstr(C,30)))
    print('VERIFY_OK')
