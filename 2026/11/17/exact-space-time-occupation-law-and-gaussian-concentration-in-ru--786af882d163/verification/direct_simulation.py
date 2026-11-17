#!/usr/bin/env python3
"""Independent direct binary simulation and weighted trace comparison, no graph library."""
import sympy as S
z=S.symbols('z');u=2
Q=S.Poly((1+u**5*z**4+u**6*z**5)**2*(1-u**6*z**3-u**6*z**4-2*u**5*z**4-2*u**6*z**5-u**11*z**7+(2*u**11-u**12)*z**8+2*u**12*z**9),z)
Q1=S.Poly(1-u**6*z**3-u**6*z**4,z)
def tr(q,maxn):
 cs=[int(q.nth(j)) for j in range(q.degree()+1)];v=[0]*(maxn+1)
 for n in range(1,maxn+1):
  v[n]=-n*cs[n] if n<len(cs) else 0
  v[n]-=sum(cs[j]*v[n-j] for j in range(1,min(n,len(cs)-1)+1))
 return v
T=tr(Q,17); F=tr(Q1,17)
def evolve(x,n):
 y=0
 for i in range(n):
  pattern=4*((x>>((i-1)%n))&1)+2*((x>>i)&1)+((x>>((i+1)%n))&1)
  y|=((73>>pattern)&1)<<i
 return y
for n in range(3,18):
 full=fixed=orbits=0; marked=set()
 for x in range(1<<n):
  a=evolve(x,n); b=evolve(a,n); c=evolve(b,n)
  if c!=x:continue
  w=2**(x.bit_count()+a.bit_count()+b.bit_count());full+=w
  if a==x:fixed+=w
  elif x not in marked:
   assert a!=x and b!=x
   marked.update([x,a,b]);orbits+=1
 assert full==T[n] and fixed==F[n] and (full-fixed)%3==0,(n,full,T[n],fixed,F[n])
 print('n',n,'orbit_count',orbits,'weighted_spacetime_total',full,'fixed_weighted',fixed)
print('all direct comparisons verified')
