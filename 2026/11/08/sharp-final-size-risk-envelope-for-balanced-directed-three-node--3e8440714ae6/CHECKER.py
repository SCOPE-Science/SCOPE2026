#!/usr/bin/env python3
"""Exact recurrence verification for a three-node continuous-time SIR model."""
from functools import lru_cache
import sympy as S
b,p=S.symbols('b p',positive=True)
W=S.zeros(3)
for i in range(3):
 W[i,(i+1)%3]=b*p
 W[i,(i-1)%3]=b*(1-p)
@lru_cache(None)
def hit_all(I,R):
 if (I|R)==7: return S.Integer(1)
 if I==0:return S.Integer(0)
 S_mask=7^(I|R)
 weighted=[]
 for j in range(3):
  if (S_mask>>j)&1:
   h=S.expand(sum(W[i,j] for i in range(3) if (I>>i)&1))
   if h!=0:weighted.append((h,hit_all(I|(1<<j),R)))
  if (I>>j)&1:weighted.append((S.Integer(1),hit_all(I^(1<<j),R|(1<<j))))
 return S.factor(sum(h*y for h,y in weighted)/sum(h for h,y in weighted))
P3=S.factor(hit_all(1,0))
P3_expected=S.factor(b/(1+b)*(1-1/((1+b*p)*(1+b*(1-p)))))
assert S.factor(P3-P3_expected)==0,(P3,P3_expected)
P1=1/(1+b)
P2=S.factor(1-P1-P3)
assert S.factor(P1+P2+P3-1)==0
Q=p*(1-p)
assert S.factor(P3-b**2*(1+b*Q)/((1+b)*(1+b+b*b*Q)))==0
Gap=S.factor(P3.subs(p,S.Rational(1,2))-P3.subs(p,0))
assert S.factor(Gap-b**3/((1+b)**2*(b+2)**2))==0
GapPrime=S.factor(S.diff(Gap,b))
assert S.factor(GapPrime + b*b*(b*b-3*b-6)/((b+1)**3*(b+2)**3))==0
Bstar=(3+S.sqrt(33))/2
Max=S.simplify(Gap.subs(b,Bstar))
assert S.simplify(Max-(33*S.sqrt(33)-189)/8)==0
assert S.simplify(P3.subs({b:1,p:S.Rational(1,2)})-S.Rational(5,18))==0
assert S.simplify(P3.subs({b:1,p:0})-S.Rational(1,4))==0
assert S.simplify(P2.subs({b:1,p:S.Rational(1,2)})-S.Rational(2,9))==0
assert S.simplify(P2.subs({b:1,p:0})-S.Rational(1,4))==0
print('PASS symbolic 3-node CTMC hitting probability:',P3)
print('PASS sharp difference:',Gap,'optimum:',Bstar,'maximum:',Max)
print('PASS exact b=1 endpoint probabilities, full distribution and derivative')
