#!/usr/bin/env python3
"""Reproducible symbolic and finite checks for alternating-grid BDF2.
Scientific proof of the infinite-time result is in RESULT.md; these tests
are supplementary and do not constitute an exhaustive certificate.
Requires Python 3.10+ and SymPy >= 1.11.
"""
from fractions import Fraction as F
from itertools import product
from sympy import symbols, Matrix, factor, simplify

x,y = symbols('x y', positive=True)
s,p = x+y,x*y
Dx = x*x+x*y+2*x+y
Dy = x*y+x+y*y+2*y
H = Dx*Dy
A_y=s*s/(x*Dy); B_y=y*y/(x*Dy)
A_x=s*s/(y*Dx); B_x=x*x/(y*Dx)
P=Matrix([[A_x*A_y-B_x,-A_x*B_y],[A_y,-B_y]])
N=s*s*(2-s)+2*p*(s+1)
Delta=(s-2)**2-4*p
z=(x+2*y-y*y)/((1+x)*Dy)
identities={
 'trace':factor(P.trace()-N/H),
 'determinant':factor(P.det()-p/H),
 'discriminant':factor((P.trace()**2-4*P.det())-s**4*Delta/H**2),
 'starter':factor(2*H*z-N-(s*s/(1+x))*(2*x*x+(2-s)*(1+x))),
 'step_entry_A':factor(A_y-(1+y/x)**2/(1+2*y/x+(1+y/x)*y)),
 'step_entry_B':factor(B_y-(y/x)**2/(1+2*y/x+(1+y/x)*y)),
}
for name,resid in identities.items():
 assert resid==0,(name,resid)
print('Symbolic identities:',len(identities),'PASS')

def classify(a,b):
 s=a+b
 return s<2 and (a-b)**2-4*(s-1)>=0

def trajectory(a,b,n=100):
 vals=[F(1),F(1)/(1+a)]
 for k in range(2,n+1):
  next_step = b if (k%2==0) else a
  prev_step = a if (k%2==0) else b
  r=next_step/prev_step
  D=1+2*r+(1+r)*next_step
  vals.append(((1+r)**2*vals[-1]-r*r*vals[-2])/D)
 return vals

# Deterministic rational positive-phase grid: each entry must remain positive.
positive_tests=0
for i,j in product(range(1,28),repeat=2):
 a,b=F(i,20),F(j,20)
 if classify(a,b):
  arr=trajectory(a,b,60)
  assert all(u>0 for u in arr),(a,b,'wrong positive phase')
  assert all(arr[k]<arr[k-1] for k in range(1,len(arr))), (a,b,'not decreasing')
  positive_tests+=1
print('Finite positive-phase trajectory checks:',positive_tests,'PASS (60 steps each)')

# Exact rational points including repeated-root boundaries and heavy contrast.
critical=[(F(1,2),F(1,2)), (F(1,8),F(9,8)),
          (F(1,18),F(25,18)), (F(1,10000),F(19,10))]
for a,b in critical:
 assert classify(a,b)
 arr=trajectory(a,b,120)
 assert all(u>0 for u in arr)
 assert all(arr[k]<arr[k-1] for k in range(1,len(arr)))
print('Critical/contrast trajectory checks:',len(critical),'PASS (120 steps each)')

# Outside-domain witnesses: negative values found, not presumed from timeouts.
fail_cases=[(F(1,10),F(7,5)), (F(1,2),F(3,2)),
            (F(1,4),F(7,4)), (F(1,10),F(3,1)),
            (F(1,1),F(1,1)), (F(3,1),F(1,10))]
for a,b in fail_cases:
 assert not classify(a,b)
 arr=trajectory(a,b,160)
 first=next((k for k,u in enumerate(arr) if u<0),None)
 assert first is not None,(a,b,'no finite witness in chosen test budget')
 print('  Negative witness:',str(a),str(b),'at index',first)
print('Negative witness cases:',len(fail_cases),'PASS')
print('Verification complete; no finite test is asserted to prove the all-index theorem.')
