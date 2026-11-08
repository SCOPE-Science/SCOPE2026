"""Independent modular sparse polynomial multiplication for the two complete intersections."""
from collections import defaultdict
E=((1,1,1,2),(1,1,2,1),(1,2,0,1),(2,1,1,1))
# Monomial key=(exponents of x,y,z,w,t).
P={(0,2,1,0,0):1,(3,0,0,0,0):-1,(0,0,3,0,0):-1}
Q={(0,0,0,2,0):1,(1,1,0,0,0):-1,(1,0,1,0,1):-1}
def mul(A,B,p):
 C=defaultdict(int)
 for a,ca in A.items():
  for b,cb in B.items():
   m=tuple(u+v for u,v in zip(a,b))
   C[m]=(C[m]+ca*cb)%p
 return {k:v for k,v in C.items() if v}
def power(A,n,p):
 v={(0,0,0,0,0):1}
 for i in range(n):v=mul(v,A,p)
 return v
expect={5:{(3,3):{0:3,2:1}},7:{(0,0):{0:3},(1,1):{1:5,3:3},(3,3):{1:5,3:1}}}
for p in (5,7):
 H=mul(power(P,p-1,p),power(Q,p-1,p),p)
 found={}
 for i,a in enumerate(E):
  for j,b in enumerate(E):
   v=tuple(p*u-w for u,w in zip(a,b))
   poly={m[4]:coeff for m,coeff in H.items() if m[:4]==v}
   if poly:found[i,j]=poly
 assert found==expect[p], (p,found)
 print('characteristic',p,'terms',len(H),'entries',found)
print('VERIFY_EXPANSION_PASS')
