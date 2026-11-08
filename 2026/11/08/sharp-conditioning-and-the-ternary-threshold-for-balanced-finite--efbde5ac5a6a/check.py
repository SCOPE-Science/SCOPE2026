"""Exact cyclotomic verification of constant-weight ternary Fourier slice spectrum.
Runs with standard Python 3; NumPy is optional and not required.
All comparisons below are over Z[zeta_3], zeta_3^2+zeta_3+1=0.
"""
from itertools import combinations
from math import comb

def plus(x,y): return (x[0]+y[0],x[1]+y[1])
def times(x,y):
 a,b=x;c,d=y
 return (a*c-b*d,a*d+b*c-b*d)
def power(x,n):
 r=(1,0)
 for _ in range(n):r=times(r,x)
 return r
ONE=(1,0); Z=(0,1); OMZ=(-1,-1); MZ=(-1,1); ONEPZ=(1,1)
def ternary(m):
 if m==0:return 1
 a,b=1,1
 for j in range(1,m):
  v=( (2*j+1)*b+3*j*a )
  assert v%(j+1)==0
  a,b=b,v//(j+1)
 return b

def verify(n,k):
 assert 2*k<=n
 sub=[sum(1<<i for i in s) for s in combinations(range(n),k)]
 mx={b:i for i,b in enumerate(sub)}
 entries=(ONE,Z,OMZ)
 M=[[entries[(A&B).bit_count()%3] for B in sub] for A in sub]
 count=0
 for j in range(k+1):
  m=k-j; a=n-2*k
  # exact combinatorial coefficient for arbitrary a (nonzero test if balanced)
  term=(0,0)
  for l in range(m+1):
   scalar=comb(m,l)*comb(m+a,m-l)
   term=plus(term,(scalar*entries[l%3][0],scalar*entries[l%3][1]))
  eig=times(power(MZ,j),term)
  # check balanced closed central-trinomial eigenphase
  if a==0:
   assert eig==times(power(MZ,j),tuple(c*ternary(m) for c in power(ONEPZ,m)))
  v=[]
  for B in sub:
   c=1
   for i in range(j):
    a0=(B>>(2*i))&1; a1=(B>>(2*i+1))&1
    if a0+a1!=1:c=0;break
    if a1:c=-c
   v.append(c)
  assert any(v)
  for Aidx,row in enumerate(M):
   left=(0,0)
   for c,w in zip(v,row):
    if c:left=plus(left,(c*w[0],c*w[1]))
   right=tuple(c*v[Aidx] for c in eig)
   assert left==right,(n,k,j,Aidx,left,right)
   count+=1
 return count,len(sub)

def run():
 total=0
 for k in range(1,6):
  for n in range(2*k,2*k+2):
   if comb(n,k)>310: continue
   c,num=verify(n,k);total+=c
   print('matrix',n,k,'dimension',num,'rows_checked',c)
 for m in range(2,500):
  L0,L1=ternary(m-2),ternary(m-1)
  L2=ternary(m)
  assert (m*L2 == (2*m-1)*L1 +3*(m-1)*L0)
  assert L2*L2>=3*L1*L1
  assert L2>=0
 for k in range(2,500):
  L=[ternary(m) for m in range(k+1)]
  # compare squared singular magnitudes exactly; j=k-m
  vals=[3**(k-m)*L[m]**2 for m in range(k+1)]
  assert min(vals)==3**(k-1),(k,'minimum')
  assert max(vals)==L[k]**2,(k,'maximum')
 print('TERNARY_CONSTANT_WEIGHT_SLICE_EXACT_PASS rows=',total,'k_up_to=499')
if __name__=='__main__':run()
