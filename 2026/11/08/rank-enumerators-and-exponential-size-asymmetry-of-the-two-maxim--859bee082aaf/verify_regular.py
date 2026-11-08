"""Independent exhaustive check of rank-count claims on small block sizes."""
from itertools import product
from math import factorial,comb
from collections import Counter

def S(n,k):
 t=[[0]*(n+1) for _ in range(n+1)];t[0][0]=1
 for i in range(1,n+1):
  for j in range(1,i+1):t[i][j]=j*t[i-1][j]+t[i-1][j-1]
 return t[n][k]

def calc(m):
 q=lambda r:factorial(r)*S(m,r)
 F=[0]*(m+1)
 for r in range(1,m+1):F[r]=comb(m,r)*q(r)
 regs=Counter();m1=Counter();m2=Counter();inter=Counter()
 for a in range(1,m+1):
  for b in range(1,m+1):regs[a+b]+=2*F[a]*F[b];m1[a+b]+=2*F[a]*F[b]
 for r in range(1,m+1):
  C=4*comb(m,r)*q(r)*r**m-2*comb(m,r)*q(r)**2
  regs[r]+=C;m2[r]+=C
 m1[1]+=2*m;m2[2*m]+=2*factorial(m)**2
 inter[1]=2*m;inter[2*m]=2*factorial(m)**2
 return regs,m1,m2,inter

def all_maps(m):
 for targets in product(range(2),repeat=2):
  for first in product(range(targets[0]*m,targets[0]*m+m),repeat=m):
   for last in product(range(targets[1]*m,targets[1]*m+m),repeat=m):
    yield (*first,*last),targets

def is_regular_by_two_images(f,m,targets):
 if targets[0]!=targets[1]:return True
 A=set(f[:m]);B=set(f[m:]);return A<=B or B<=A

def brute_inverse(f,m,gset):
 im=set(f)
 for g in gset:
  if all(f[g[y]]==y for y in im):return True
 return False

def brute(m):
 fmaps=list(all_maps(m)); gs=[f for f,_ in fmaps] if m<=3 else []
 B=Counter();M1=Counter();M2=Counter();I=Counter(); inverse_tests=0
 for f,targets in fmaps:
  rank=len(set(f)); perm=targets[0]!=targets[1]; reg=is_regular_by_two_images(f,m,targets)
  is_unit=rank==2*m
  is_constant=rank==1
  mm1=perm or is_constant
  mm2=(reg and not perm) or is_unit
  if m<=3:
   assert brute_inverse(f,m,gs)==reg,('inverse mismatch',m,f)
   inverse_tests+=1
  if reg:B[rank]+=1
  if mm1:M1[rank]+=1
  if mm2:M2[rank]+=1
  if mm1 and mm2:I[rank]+=1
 assert B==calc(m)[0], ('reg',m,B,calc(m)[0])
 assert M1==calc(m)[1], ('m1',m,M1,calc(m)[1])
 assert M2==calc(m)[2], ('m2',m,M2,calc(m)[2])
 assert I==calc(m)[3], ('int',m,I,calc(m)[3])
 print('m',m,'maps',len(fmaps),'reg',sum(B.values()),'ranks',sorted(B.items()),'inverse_tests',inverse_tests, 'OK')
for n in (2,3,4):brute(n)
print('VERIFICATION_OK')
