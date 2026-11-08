from itertools import product
from math import gcd
p=3;q=9
# F_9 = F_3[w]/(w^2+1)
def add(a,b):return ((a%p+b%p)%p)+p*((a//p+b//p)%p)
def neg(a):return ((-a)%p)+p*((-(a//p))%p)
def mul(a,b):
 x,y=a%p,a//p;u,v=b%p,b//p
 return ((x*u+2*y*v)%p)+p*((x*v+y*u)%p)
def pw(a,n):
 z=1
 for _ in range(n):z=mul(z,a)
 return z
elts=list(range(q));Q=set(elts[1:])
g=next(a for a in Q if set(pw(a,k) for k in range(8))==Q)
print('generator',g,'powers',[pw(g,i) for i in range(8)])
for ell in (1,2):
 m=(q-1)//ell
 cosets=[[pw(g,i+ell*j) for j in range(m)] for i in range(ell)]
 assert set(sum(cosets,[]))==Q
 counts={'total':0,'zero':0,'full':0,'other':0,'additive_non_frob':0}
 for r in range(m):
  for a in product(range(1,q),repeat=ell):
   f=[0]*q
   for i,coset in enumerate(cosets):
    for x in coset:f[x]=mul(a[i],pw(x,r))
   periods=[u for u in elts if all(add(f[add(x,u)],neg(f[x]))==f[u] for x in elts)]
   counts['total']+=1
   if len(periods)==1:counts['zero']+=1
   elif len(periods)==q:
    counts['full']+=1
    # frobenius monomials have exponent 1 or 3; verify
    if not any(all(f[x]==mul(c,pw(x,e)) for x in elts) for c in range(1,q) for e in (1,3)):
     counts['additive_non_frob']+=1
   else:counts['other']+=1
 print('ell',ell,counts)
 assert counts['other']==0 and counts['additive_non_frob']==0
 assert counts['total']==m*(q-1)**ell
# sharpness F9, ell=p+1=4, n=2
for c in range(1,9):
 if mul(c,pw(c,3))==2:
  f=[add(x,mul(c,pw(x,3))) for x in range(9)]
  assert set(f)==set(range(9))
  print('sharpness c',c,'values',f,'norm',mul(c,pw(c,3)))
  # For both smaller admissible indices, no power exponent and coset coefficient representation exists.
  for low in (1,2):
   mm=(q-1)//low
   classes=[[pw(g,i+low*j) for j in range(mm)] for i in range(low)]
   assert not any(all(len({mul(f[x],pw(x,q-1-r)) for x in C})==1 for C in classes) for r in range(mm))
  break
else: raise AssertionError('no norm-2 coefficient')
print('VERIFY_OK F9_ALL_PRESENTATIONS=320 no_intermediate_periods=yes non_frobenius_maximal=yes sharpness_ell4=yes')
