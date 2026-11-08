from itertools import permutations,product
from math import factorial
from collections import Counter

def parts(n,cap=None):
 if n==0:
  yield ()
 else:
  for i in range(min(n,cap or n),0,-1):
   for p in parts(n-i,i): yield (i,)+p

def calc(k, verbose=False):
 no_swap=0;with_swap=0
 details=[]
 for lam in parts(k):
  m=Counter(lam)
  z=1
  for ell,q in m.items(): z*=ell**q*factorial(q)
  ns=z*z
  for q in m.values():ns*=q+1
  sw=1
  for ell in range(1,k+1):
   fixed=m.get(ell,0) if ell%2 else 0
   pairs=m.get(2*ell,0)
   N=fixed+2*pairs
   if N==0:continue
   coeff=[0]*(N+1)
   for i in range(fixed+1):
    for j in range(pairs+1):
     from math import comb
     coeff[i+2*j]+=comb(fixed,i)*comb(pairs,j)
   sw*=ell**N*sum(coeff[r]**2*factorial(r)*factorial(N-r) for r in range(N+1))
  no_swap+=ns//z
  assert ns%z==0
  assert sw%z==0
  with_swap+=sw//z
  details.append((lam,ns//z,sw//z))
 assert (no_swap+with_swap)%2==0
 return (no_swap,with_swap,(no_swap+with_swap)//2,details)

def exhaustive(k):
 perms=list(permutations(range(k)))
 funcs=list(product((0,1),repeat=k))
 inv=lambda p:tuple(p.index(y) for y in range(k))
 all_tri=[]
 for e in funcs:
  for a in perms:
   for b in perms:
    if all(e[inv(a)[y]]==e[inv(b)[y]] for y in range(k)):
     all_tri.append((e,a,b))
 seen=set();orbit_reps=0
 for v in all_tri:
  if v in seen:continue
  orbit_reps+=1
  e,a,b=v
  for t in perms:
   it=inv(t)
   et=tuple(e[it[y]] for y in range(k))
   at=tuple(t[a[it[y]]] for y in range(k))
   bt=tuple(t[b[it[y]]] for y in range(k))
   seen.add((et,at,bt)); seen.add((et,bt,at))
 assert len(seen)==len(all_tri)
 return (len(all_tri),orbit_reps)
if __name__=='__main__':
 for k in range(1,10):
  ans=calc(k); print('k',k,'nonstate',ans[0],'stateswap',ans[1],'orbit',ans[2])
  if k<=4:
   n,v=exhaustive(k); print('  exhaustive',n,v)
   assert v==ans[2] and n==(k+1)*factorial(k)**2
