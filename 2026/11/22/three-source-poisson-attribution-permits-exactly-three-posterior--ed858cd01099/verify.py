#!/usr/bin/env python3
"""Standalone exact-arithmetic checks for a three-tributary Poisson attribution example.
Only Python standard library; no external data are needed.
"""
from fractions import Fraction as Q
from math import factorial

def exp_interval(x, terms=80):
    """Rigorous rational bounds for exp(x), 0<=x<terms+2."""
    assert isinstance(x,Q) and 0 <= x < terms+2
    s=Q(0)
    term=Q(1)
    for k in range(terms+1):
        if k:
            term *= x/k
        s+=term
    nextterm=term*x/(terms+1)
    return (s,s+nextterm/(1-x/Q(terms+2)))

def signed_sum_interval(terms):
    """sum rational coefficient * exp(nonnegative rational argument)."""
    lo=hi=Q(0)
    for c,x in terms:
        a,b=exp_interval(x)
        if c>=0:lo+=c*a;hi+=c*b
        else:lo+=c*b;hi+=c*a
    return lo,hi

def H_interval(n):
    # 1000*exp(6)*(L_u(n)-10*L_v(n))
    assert isinstance(n,int) and n>=0
    return signed_sum_interval([
      (Q(999),Q(5)),
      (-Q(9990,10**n),Q(59,10)),
      (Q(6**n),Q(0)),
      (-Q(10)*Q(51,10)**n,Q(9,10)),
    ])

def run():
    expectations={1:-1,2:1,5:1,6:-1,19:-1,20:1}
    for n,sign in expectations.items():
        low,up=H_interval(n)
        assert (low>0 if sign>0 else up<0), (n,float(low),float(up))
        print('N=',n,'SIGN=', '+' if sign>0 else '-',
              'CERTIFIED H BOUNDS:',f'[{float(low):.8g},{float(up):.8g}]')
    # Independent direct enumeration of posterior probabilities at each selected count.
    # Uses only stdlib floating point as a diagnostic, not to certify signs.
    from math import exp
    for n,sgn in expectations.items():
        p1,p2,p3=1/11,1/2,1/1000
        rates=(1.,.1,5.)
        numer=denom=0.
        for x1 in (0,1):
         for x2 in (0,1):
          for x3 in (0,1):
           prob=(p1 if x1 else 1-p1)*(p2 if x2 else 1-p2)*(p3 if x3 else 1-p3)
           rate=x1*rates[0]+x2*rates[1]+x3*rates[2]
           pois=exp(-rate)*rate**n/factorial(n) if rate>0 else (1 if n==0 else 0)
           numer+=prob*pois*(x1-x2)
           denom+=prob*pois
        assert denom>0 and numer*sgn>0,(n,numer)
        print('DIRECT posterior difference',n,f'{numer/denom:.10f}')
    print('ALL EXACT WITNESS SIGNS AND INDEPENDENT BAYES CHECKS PASSED')

if __name__=='__main__':run()
