import numpy as np
from itertools import product
mods={2:[1,0,1],4:[1,0,1,1,1]}
def field(n):
 q=3**n; mod=mods[n]
 vals=[[ (k//3**i)%3 for i in range(n)]for k in range(q)]
 idx={tuple(v):i for i,v in enumerate(vals)}
 plus=np.zeros((q,q),dtype=np.uint16)
 for a in range(q):
  for b in range(q):plus[a,b]=idx[tuple((u+v)%3 for u,v in zip(vals[a],vals[b]))]
 def mul(a,b):
  arr=[0]*(2*n-1)
  for i,u in enumerate(vals[a]):
   for j,v in enumerate(vals[b]):arr[i+j]=(arr[i+j]+u*v)%3
  for k in range(2*n-2,n-1,-1):
   cc=arr[k]
   for j in range(n):arr[k-n+j]=(arr[k-n+j]-cc*mod[j])%3
  return idx[tuple(arr[:n])]
 squares={mul(a,a)for a in range(q)}
 characters=np.array([0 if z==0 else 1 if z in squares else -1 for z in range(q)],dtype=np.int16)
 powers=np.empty((12,q),dtype=np.uint16)
 powers[0]=1
 for i in range(1,12):
  for a in range(q):powers[i,a]=mul(int(powers[i-1,a]),a)
 double=np.array([idx[tuple((2*x)%3 for x in vals[a])]for a in range(q)],dtype=np.uint16)
 return plus,characters,powers,double
fs={n:field(n)for n in (2,4)}
# for all 3^9 coefficient patterns, calculate using vectorized arrays n=4 and n=2
B4min=10000; candidates=[]; counts={}
for k in range(3**11):
 coeff=[];m=k
 for j in range(11):coeff.append(m%3);m//=3
 Ns={}
 for n in [2,4]:
  add,chi,powers,twice=fs[n]
  vals=powers[11].copy()
  for j,c in enumerate(coeff):
   if c:vals=add[vals,powers[j] if c==1 else twice[powers[j]]]
  Ns[n]=3**n+1+int(np.sum(chi[vals]))
 B4=(Ns[4]-Ns[2])//4
 counts[B4]=counts.get(B4,0)+1
 if B4<B4min:B4min=B4
 if B4<4:
  candidates.append((k,coeff,B4,Ns))

import sympy as sp
x=sp.symbols('x')
assert len(candidates)==21, (len(candidates), candidates)
assert set(c[2] for c in candidates)=={0,2}
for k,coeff,b4,Ns in candidates:
 f=sp.Poly(x**11+sum(c*x**i for i,c in enumerate(coeff)),x, modulus=3)
 assert sp.gcd(f,f.diff()).degree()>0, (k,coeff,b4)
assert sp.Poly(x*x+1,x,modulus=3).is_irreducible
assert sp.Poly(x**4+x**3+x**2+1,x,modulus=3).is_irreducible
wcoeff=[0,2,0,2,0,1,0,1,0,0,0]
assert sp.gcd(sp.Poly(x**11+sum(c*x**i for i,c in enumerate(wcoeff)), x,modulus=3),sp.Poly(11*x**10+sum(i*c*x**(i-1) for i,c in enumerate(wcoeff) if i),x,modulus=3)).degree()==0
assert B4min==0

observed = {}
for n in (2,4):
 add, chi, powers, twice=fs[n]
 values=powers[11].copy()
 for j,c in enumerate(wcoeff):
  if c: values=add[values,powers[j] if c==1 else twice[powers[j]]]
 observed[n]=3**n+1+int(np.sum(chi[values]))
assert observed == {2:18, 4:34}, observed
print('VERIFY_OK total_polynomials=177147 low_B4=21 all_low_singular=True witness_B4=4 witness_N2=18 witness_N4=34')
