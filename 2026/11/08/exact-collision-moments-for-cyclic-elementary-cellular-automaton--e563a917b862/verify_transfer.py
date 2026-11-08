#!/usr/bin/env python3
"""Exact symbolic transfer and renewal validation for Rule-4 collision moments."""
import sympy as s
from fractions import Fraction
from math import gcd

t,z=s.symbols('t z')
A=s.zeros(16)
for a in range(4):
 for b in range(4):
  for c in range(4):
   x=lambda u:u&1
   y=lambda u:(u>>1)&1
   v1=x(b)*(1-x(a))*(1-x(c))
   v2=y(b)*(1-y(a))*(1-y(c))
   if v1==v2:A[4*a+b,4*b+c]+=1
P=t**6-3*t**5-t**3-2*t**2+2*t+2
C=t**3-t**2+2*t-1
assert s.expand(A.charpoly(t).as_expr()-t**7*C*P)==0
D=(z**3-2*z**2+z-1)*(z**3+3*z**2+2*z-1)
N=-z**5-z**4+2*z**3+2*z**2-2*z+1
f=[1,1,2]
for i in range(3,50):f.append(2*f[-1]-f[-2]+f[-3])
f2=[u*u for u in f]
G=s.cancel(N/D)
coeff=[s.expand(s.series(G,z,0,35).removeO()).coeff(z,i) for i in range(35)]
assert coeff==f2[:35]
H=s.cancel(z**2+z**3*G)
Q=2*z**6+2*z**5-2*z**4-z**3-3*z+1
assert s.cancel(1-H-Q/D)==0
# positive spacings, moments by marked cyclic renewal
weights=[0,0]+[1]+[f[d-3]**2 for d in range(3,48)]
# coeff of derivative log 1/(1-H) = H'/(1-H): n*coeff = recurrence
q=[0]*45
for n in range(1,45):
 q[n]=n*weights[n]+sum(weights[j]*q[n-j] for j in range(1,n))
# zero-output fibres from four-state DFA excluding 010
Z=s.zeros(4)
for a in range(2):
 for b in range(2):
  for c in range(2):
   if (a,b,c)!=(0,1,0):Z[2*a+b,2*b+c]+=1
assert s.expand(Z.charpoly(t).as_expr()-t*(t**3-2*t**2+t-1))==0
T=s.eye(16);U=s.eye(4)
for n in range(1,37):
 T=T*A;U=U*Z
 if n>=3:
  v=int(s.trace(T));g=int(s.trace(U))
  assert v==g*g+q[n],(n,v,g*g+q[n])
  if n<=18:print(f'n={n:2} transfer_moment={v:12} zero_fibre={g:7} renewal_nonzero={q[n]:12}')
roots=s.nroots(P,maxsteps=100)
rr=[complex(q) for q in roots]
large=max(rr,key=lambda q:abs(q))
assert large.real>3.1 and abs(large.imag)<1e-8
print('P(t)=',P)
print('largest root =',large.real,'collision_probability_base =',large.real/4)
print('all other abs roots <=',max(abs(x) for x in rr if x!=large))
print('PASS: symbolic characteristic polynomial and renewal identity through n=36')
