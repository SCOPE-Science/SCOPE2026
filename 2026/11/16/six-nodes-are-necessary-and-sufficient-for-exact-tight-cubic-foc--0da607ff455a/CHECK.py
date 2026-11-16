"""Exact symbolic consistency checks for the positive six-node cubic Fock sampler."""
from sympy import I, Rational as Q, sqrt, simplify, conjugate
from math import factorial
D=sqrt(17); u=(5-D)/2;v=(5+D)/2;A=(3*D+11)/(8*D);B=(3*D-11)/(8*D);C=Q(1,4)
assert float(u)>0 and float(v)>0 and float(A)>0 and float(B)>0
nodes=[sqrt(u),-sqrt(u),sqrt(v),-sqrt(v),I*sqrt(2),-I*sqrt(2)]
w=[A/2,A/2,B/2,B/2,C/2,C/2]
n=0
for j in range(4):
 for k in range(4):
  val=simplify(sum(wt*z**j*conjugate(z)**k for wt,z in zip(w,nodes)))
  assert simplify(val-(factorial(j) if j==k else 0))==0
  n+=1
for j in range(4):
 for k in range(4):
  val=simplify(sum(wt*z**j*conjugate(z)**k for wt,z in zip(w,nodes))/sqrt(factorial(j)*factorial(k)))
  assert simplify(val-(1 if j==k else 0))==0
  n+=1
for j,t in enumerate([Q(3,4),Q(1,2),Q(1),Q(4)]):
 assert simplify(A*u**j+B*v**j-t)==0;n+=1
for j,t in enumerate([Q(1,4),Q(1,2),Q(1),Q(2)]):
 assert simplify(C*2**j-t)==0;n+=1
m=[Q(3,4),Q(1,2),Q(1),Q(4)]
for j in range(2):
 assert simplify(m[j+2]-5*m[j+1]+2*m[j])==0;n+=1
assert simplify(u+v-5)==0;n+=1
assert simplify(u*v-2)==0;n+=1
print('EXACT_FOCK_CUBIC_SIX_NODE_CHECKS_PASS',n)
