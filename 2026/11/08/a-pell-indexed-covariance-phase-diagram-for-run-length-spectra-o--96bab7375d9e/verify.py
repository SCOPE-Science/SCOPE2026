"""Exact finite checks for covariances of fully bounded success runs.
Standard library only; no external data or numerical certificates required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, isqrt

COUNT = 0

def check(x, y, context):
    global COUNT
    if x != y:
        raise AssertionError((context, x, y))
    COUNT += 1

def fall(x, k):
    if k > x:
        return 0
    t=1
    for j in range(k):
        t *= x-j
    return t

def pattern_probability(N, a, ones, zeros):
    if ones+zeros > N:
        return Fraction(0)
    return Fraction(fall(a,ones)*fall(N-a,zeros),fall(N,ones+zeros))

def moment(N,a,r):
    return (N-r-1)*pattern_probability(N,a,r,2)

def mixed(N,a,r,s):
    assert r!=s and N>=r+s+4
    h=N-r-s-2
    return h*(h-1)*pattern_probability(N,a,r+s,4) + 2*h*pattern_probability(N,a,r+s,3)

def covariance(N,a,r,s):
    return mixed(N,a,r,s)-moment(N,a,r)*moment(N,a,s)

def counts(word,r):
    return sum(word[i:i+r+2]==(0,)+(1,)*r+(0,) for i in range(len(word)-r-1))

def exhaustive():
    # Enumerate the entire fixed-weight sample space, not Monte Carlo.
    for N in range(6,13):
        for a in range(1,N):
            for r in range(1,min(5,N-4)+1):
                for s in range(r+1,min(6,N-r-4)+1):
                    if N<r+s+4:continue
                    tot=ex=ey=exy=0
                    for ones in combinations(range(N),a):
                        w=[0]*N
                        for i in ones:w[i]=1
                        xr=counts(tuple(w),r); xs=counts(tuple(w),s)
                        ex+=xr; ey+=xs; exy+=xr*xs; tot+=1
                    check(Fraction(ex,tot),moment(N,a,r),(N,a,r,s,'mean_r'))
                    check(Fraction(ey,tot),moment(N,a,s),(N,a,r,s,'mean_s'))
                    check(Fraction(exy,tot),mixed(N,a,r,s),(N,a,r,s,'mixed'))
                    check(Fraction(exy,tot)-Fraction(ex,tot)*Fraction(ey,tot),covariance(N,a,r,s),(N,a,r,s,'cov'))

def critical():
    for N in range(15,181,3):
        a=2*N//3
        numerator=-256*N*(N-3)**2*(2*N-21)*(2*N-15)*(2*N-9)*(2*N-3)
        denominator=177147*(N-10)*(N-8)*(N-7)*(N-5)*(N-4)*(N-2)*(N-1)**2
        check(covariance(N,a,1,8),Fraction(numerator,denominator),(N,'critical identity'))
    # Degenerate Pell pairs and strict phase boundaries.
    x,y=3,2
    for _ in range(6):
        r=(x-1)//2
        s=3*r+1+2*y
        check((r-s)**2-4*r*s-2*(r+s)+1,0,(r,s,'discriminant'))
        x,y=3*x+4*y,2*x+3*y
    for r in range(1,13):
        for s in range(r+1,100):
            delta=(r-s)**2-4*r*s-2*(r+s)+1
            threshold=3*r+1
            positive=(s>threshold and (s-threshold)**2>8*r*(r+1))
            check(delta>0,positive,(r,s,'classification'))

if __name__=='__main__':
    exhaustive()
    critical()
    print(f'{COUNT} exact checks passed')
