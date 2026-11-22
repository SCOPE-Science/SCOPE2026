#!/usr/bin/env python3
"""Exact transition and stationary-law checks for a zealot voter count chain.

Standard Python only; these tests complement (but do not replace) the proofs.
"""
from fractions import Fraction as F
from math import comb

def rising(x,k):
    ans=F(1)
    for i in range(k): ans*=x+i
    return ans

def pmf(n,a,b,r):
    d=n-1+a+b
    t=(1-r)*d/(2*r-1)
    theta,beta=a+t,b+t
    return [F(comb(n,k))*rising(theta,k)*rising(beta,n-k)/rising(theta+beta,n) for k in range(n+1)]

def jumps(n,a,b,r,k):
    d=n-1+a+b
    up=F(n-k,n)*(r*(k+a)+(1-r)*(n-k-1+b))/d if k<n else F(0)
    down=F(k,n)*(r*(n-k+b)+(1-r)*(k-1+a))/d if k>0 else F(0)
    return up,down

checks=0
for n in (1,3,5,7,9,11):
 for a,b in [(F(2),F(1)),(F(3,2),F(2,3)),(F(5),F(3)),(F(1,3),F(4,3))]:
  for r in [F(3,5),F(2,3),F(3,4),F(9,10),F(1)]:
   p=pmf(n,a,b,r)
   assert sum(p)==1
   checks+=1
   for k in range(n):
    up=jumps(n,a,b,r,k)[0]
    down=jumps(n,a,b,r,k+1)[1]
    assert p[k]*up==p[k+1]*down
    checks+=1
   if a>b:
    def maj(rr):return sum(pmf(n,a,b,rr)[(n+1)//2:])
    assert maj(F(3,5))<maj(F(2,3))<maj(F(3,4))<maj(F(9,10))<maj(F(1))
    checks+=1
   elif a<b:
    def maj(rr):return sum(pmf(n,a,b,rr)[(n+1)//2:])
    assert maj(F(3,5))>maj(F(2,3))>maj(F(3,4))>maj(F(9,10))>maj(F(1))
    checks+=1
print('exact_fraction_checks',checks)

# Evaluate exact critical limiting formula for a=2,b=1 at t=0,1,2,3.
for t in range(4):
    from math import factorial
    beta=F(factorial(t)*factorial(t), factorial(2*t+1))
    c=F(1,4**(t+1)*(t+1))/beta
    print('limiting_lam',t,'P_majority',str(F(1,2)+c))
    assert F(0)<c<=F(1,4)

# Non-equality in critical window: r_n = 1-lam/(n-1), with lam=1.
# The limit for a=2,b=1 is 11/16; compare exact finite sample values.
for n in [21,51,101,201]:
    r=F(n-2,n-1)
    if r>F(1,2):
        m=sum(pmf(n,F(2),F(1),r)[(n+1)//2:])
        print('n',n,'majority',f'{float(m):.9f}','limit',float(F(11,16)))

# Exhaustively classify all self-dual monotone Boolean aggregators on up to
# four voters and check the strict sign of their conformity response.
from itertools import product
rule_checks=0
for n in (1,2,3,4):
    N=1<<n
    def monotone_selfdual(table):
        for x in range(N):
            if table[x]+table[(N-1)^x]!=1:
                return False
            for i in range(n):
                if not (x>>i)&1 and table[x]>table[x|(1<<i)]:
                    return False
        return True
    for bits in range(1<<N):
        table=tuple((bits>>x)&1 for x in range(N))
        if not monotone_selfdual(table):
            continue
        for a,b in [(F(2),F(1)),(F(1),F(2)),(F(3,2),F(2,3)),(F(1),F(1))]:
            vals=[]
            for r in (F(3,5),F(2,3),F(3,4),F(9,10),F(1)):
                p=pmf(n,a,b,r)
                vals.append(sum(F(table[x],comb(n,x.bit_count()))*p[x.bit_count()] for x in range(N)))
            if a>b: assert all(x<y for x,y in zip(vals,vals[1:])),(n,a,b,vals)
            elif a<b: assert all(x>y for x,y in zip(vals,vals[1:])),(n,a,b,vals)
            else: assert all(x==F(1,2) for x in vals)
            rule_checks+=1
    print('selfdual_monotone_n',n,'checks_to_date',rule_checks)
print('selfdual_rule_checks',rule_checks)

# Closed beta-function expression for two versus one exogenous weights.
from math import factorial
closed_form_checks=0
for n in (1,3,5,7,9,11):
    m=(n-1)//2
    for c in (1,2,3,4,5):
        beta_cc=F(factorial(c-1)**2,factorial(2*c-1))
        beta_cm=F(factorial(c+m)**2,factorial(2*(c+m)+1))
        excess=F(n*comb(n-1,m),c)*beta_cm/beta_cc
        brute=sum(F(comb(n,k))*rising(F(c+1),k)*rising(F(c),n-k)/rising(F(2*c+1),n) for k in range(m+1,n+1))
        assert brute==F(1,2)+excess
        closed_form_checks+=1
print('closed_form_checks',closed_form_checks)
