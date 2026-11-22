from itertools import product
from collections import Counter

def mat(A):
 a,b,c=A
 return ((a,b),(c,-a))
def br(A,B,q):
 a,b,c=A;d,e,f=B
 return ((b*f-e*c)%q,(2*(a*e-b*d))%q,(2*(c*d-a*f))%q)
def vec(A,B,u,v,q):
 a,b,c=A;d,e,f=B
 return ((a*v[0]+b*v[1]-d*u[0]-e*u[1])%q,(c*v[0]-a*v[1]-f*u[0]+d*u[1])%q)
def check(q):
 vs=list(product(range(q),repeat=2))
 mats=list(product(range(q),repeat=3))
 out=Counter()
 for A in mats:
  for B in mats:
   C=br(A,B,q)
   image=Counter(vec(A,B,u,v,q) for u in vs for v in vs)
   for w,mult in image.items(): out[(C,w)]+=mult
 for C in mats:
  for w in vs:
   if C!=(0,0,0): f=q**3*(q*q-1)
   elif w!=(0,0): f=q**3*(q+1)*(q*q-1)
   else:f=q**6+q**3*(q+1)*(q*q-1)
   assert out[(C,w)]==f,(q,C,w,out[(C,w)],f)
 assert sum(out.values())==q**10
 print(f'q={q}: {q**5} targets, {q**10} ordered input pairs, all fiber counts verified; zero={out[(0,0,0),(0,0)]}; nonzero Lie part={out[(1,0,0),(0,0)]}; zero Lie part nonzero vector={out[(0,0,0),(1,0)]}')
for q in (3,5):check(q)
