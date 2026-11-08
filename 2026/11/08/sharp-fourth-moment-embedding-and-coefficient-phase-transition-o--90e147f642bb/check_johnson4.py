#!/usr/bin/env python3
"""Exact-rational independent subset enumeration for degree-one Johnson slice moments.
No external packages required. Usage: python check_johnson4.py
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb


def mean_power(a,k,power):
    n=len(a)
    return sum((sum(a[i] for i in s)**power for s in combinations(range(n),k)),Q(0))/comb(n,k)

def model(n,k):
    p=lambda j: Q(0) if j>k else Q(1)*__import__('math').prod(k-i for i in range(j))/__import__('math').prod(n-i for i in range(j))
    A=3*(p(2)-2*p(3)+p(4))
    B=p(1)-7*p(2)+12*p(3)-6*p(4)
    c=Q(k*(n-k),n*(n-1))
    assert B==Q(k*(n-k)*(n*n+n-6*k*(n-k)),n*(n-1)*(n-2)*(n-3))
    return A,B,c

samples=0
for n in range(4,15):
  for k in range(2,n-1):
    A,B,c=model(n,k)
    for t in range(1,n):
      a=[Q(n-t,n) if i<t else Q(-t,n) for i in range(n)]
      S2=sum(x*x for x in a)
      S4=sum(x**4 for x in a)
      assert sum(a)==0
      assert mean_power(a,k,2)==c*S2
      assert mean_power(a,k,4)==A*S2*S2+B*S4
      samples+=1
    spike=Q(n*n-3*n+3,n*(n-1))
    lo=n//2
    hi=n-lo
    balanced=Q(n,lo*hi)-Q(3,n)
    branch=spike if B>0 else balanced
    pred=(A+B*branch)/c**2
    for t in range(1,n):
      a=[Q(n-t,n) if i<t else Q(-t,n) for i in range(n)]
      ratio=mean_power(a,k,4)/mean_power(a,k,2)**2
      assert ratio<=pred
    if B>0:
      t=1
    else:
      t=lo
    a=[Q(n-t,n) if i<t else Q(-t,n) for i in range(n)]
    assert mean_power(a,k,4)/mean_power(a,k,2)**2==pred
    # Three-valued local stationary candidates have value 1/2, below spike.
    assert Q(1,2)<spike
print('EXACT_HYPERGEOMETRIC_MOMENT_IDENTITIES_OK',samples)
for n,k in [(8,2),(10,2),(10,3),(12,2),(12,3),(12,4)]:
 A,B,c=model(n,k)
 plus=Q(n*n-3*n+3,n*(n-1)); minus=Q(1,n)
 print('PHASE_SAMPLE',n,k,'sign',('+ ' if B>0 else '- ' if B<0 else '0 '),'sharp_norm_fourth_power',(A+B*(plus if B>0 else minus))/c**2)
print('ALL_FIRST_JOHNSON_FOURTH_MOMENT_CHECKS_OK')
