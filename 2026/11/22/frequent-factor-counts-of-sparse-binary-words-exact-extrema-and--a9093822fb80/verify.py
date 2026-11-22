#!/usr/bin/env python3
"""Standalone checks of the two-marker frequent-substring theorem.
Only Python standard library is needed. Historical literature is not part of this program.
"""
from collections import Counter
from fractions import Fraction
from math import floor


def formula(a,b,c):
    gaps=(a,b,c)
    N=sum(gaps)
    return 1+sum(sum(max(g-j+1,0) for g in gaps)>j for j in range(1,N+1))

def brute(a,b,c):
    w='0'*a+'1'+'0'*b+'1'+'0'*c
    occ=Counter(w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1))
    return sum(v>len(k) for k,v in occ.items())

def rt(gaps):
    """Solve the continuous threshold using sorted gap ratios; bisection is for checks only."""
    s=sum(gaps)
    if s==0: return 0.0
    lo,hi=0.0,1.0
    for _ in range(75):
        m=(lo+hi)/2
        if sum(max(g/s-m,0) for g in gaps)>m: lo=m
        else: hi=m
    return (lo+hi)/2

# Full literal, substring-by-substring test for all fixed-weight words up to length 19.
count=0
for N in range(18):
    vals=[]
    for a in range(N+1):
        for b in range(N-a+1):
            c=N-a-b
            v=formula(a,b,c)
            assert v==brute(a,b,c),(N,a,b,c,v,brute(a,b,c))
            vals.append(v)
            count+=1
    assert min(vals)==1+(N+2)//4
    assert max(vals)==1+N//2
print('Literal factor comparisons:',count, 'all passed')

# Uniform threshold convergence is O(1/N); check a stringent explicit bound.
for N in [19,30,61,100,150,225]:
    err=0.0
    for a in range(N+1):
        for b in range(N-a+1):
            c=N-a-b
            err=max(err,abs(formula(a,b,c)/N-rt((a,b,c))))
    print('N',N,'max scaled error',round(err,8))
    assert err<=5/N

# Exact CDF and moments of the proposed law: polynomial integration with fractions.
def integrate_poly_term(power,lo,hi):
    return (hi**(power+1)-lo**(power+1))/(power+1)
for k,expected in [(0,Fraction(1)),(1,Fraction(187,576)),(2,Fraction(1499,13824))]:
    low=Fraction(1,4); mid=Fraction(1,3); high=Fraction(1,2)
    moment=Fraction(1,16)*low**k + 66*integrate_poly_term(k+1,low,mid)-12*integrate_poly_term(k,low,mid)+12*integrate_poly_term(k,mid,high)-24*integrate_poly_term(k+1,mid,high)
    assert moment==expected,(k,moment,expected)
    print('Moment',k,'=',moment)
print('Variance =',Fraction(1499,13824)-Fraction(187,576)**2)
print('All checks passed')
