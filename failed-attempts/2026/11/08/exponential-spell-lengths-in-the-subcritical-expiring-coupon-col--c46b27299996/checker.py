#!/usr/bin/env python3
"""Exact finite occupancy and contiguous-window checks for expiring-coupon spell law.
No stochastic simulations, no external dependencies.
"""
from fractions import Fraction
from itertools import product, combinations
from math import comb, factorial


def stirling2(v, k):
    if k < 0 or v < 0 or k > v: return 0
    a = [0]*(k+1); a[0] = 1
    for i in range(1, v+1):
        b = [0]*(k+1)
        for j in range(1, min(i,k)+1): b[j] = j*a[j] + a[j-1]
        a = b
    return a[k]


def onto_words(N, m):
    return [u for u in product(range(N), repeat=m) if len(set(u))==N]


def singleton_prefix(u,k):
    return sum(u.count(c)==1 for c in u[:k])


def survive(u, a, v, n):
    M = len(u) + 1
    word = u + (a,) + v
    return all(len(set(word[j:j+M]))==n for j in range(len(v)+1))


def checks(n,M,k):
    N,m=n-1,M-1
    U=onto_words(N,m)
    assert len(U)==factorial(N)*stirling2(m,N)
    rho=Fraction(stirling2(m-1,N-1),stirling2(m,N))
    cnt=sum(singleton_prefix(u,k) for u in U)
    assert Fraction(cnt,len(U)) == k*rho
    for r in range(1,min(3,k)+1):
        num=sum(sum(all(u.count(u[i])==1 for i in ids) for ids in combinations(range(k),r)) for u in U)
        exp = Fraction(comb(k,r)*stirling2(m-r,N-r),stirling2(m,N))
        assert Fraction(num,len(U)) == exp, (n,M,k,r,Fraction(num,len(U)),exp)
    num_h=sum(singleton_prefix(u,k)==0 for u in U)
    num_l=0
    for u in U:
        for v in product(range(n), repeat=k):
            num_l+=survive(u,N,v,n)
    P_h=Fraction(num_h,len(U))
    P_l=Fraction(num_l,len(U)*n**k)
    # A rigorous two-event sandwich; no asymptotic approximations.
    rescue_upper = k*k*rho/Fraction(n)
    bad_upper = rho*sum(Fraction(comb(k,j),(N-1)**(j-1)) for j in range(2,k+1)) if N>=2 else Fraction(0)
    assert abs(P_l-P_h) <= rescue_upper+bad_upper, (n,M,k,P_l,P_h,rescue_upper,bad_upper)
    return (n,M,k,str(rho),str(P_h),str(P_l),str(rescue_upper+bad_upper))


def main():
    tests=[]
    for n in [3,4,5]:
        for M in range(n,n+(4 if n<5 else 2)):
            for k in range(1,min(4,M)):
                if n**(M-1+k)>1_000_000:continue
                tests.append(checks(n,M,k))
    for a in tests: print('PASS',*a)
    print('EXACT_CASES_PASSED',len(tests))

if __name__=='__main__':main()
