#!/usr/bin/env python3
"""Exact representative checks and exhaustive Fourier-null tests for the commuting-pair cone."""
import itertools, math, numpy as np

def valuation(a,p,k):
 if a==0:return k
 v=0
 while v<k and a%p==0:a//=p;v+=1
 return v

def domain_indicator(n):
 x=np.array(list(itertools.product(range(n),repeat=3)), dtype=np.int64)
 D=np.zeros((n,)*6, dtype=np.int8)
 for u in x:
  w=x
  cond=(((u[0]*w[:,1]-u[1]*w[:,0])%n==0)&
        ((u[0]*w[:,2]-u[2]*w[:,0])%n==0)&
        ((u[1]*w[:,2]-u[2]*w[:,1])%n==0))
  for v in w[cond]: D[tuple(u)+tuple(v)]=1
 return D

def smith(s,t,k,p):
 if s==k:return (k,k)
 if t==k:return (s,k)
 return (s,t)

def predicted_H(p,k,s,t):
 q=p
 if t<k:
  if s+t <=k-2:return 0
  if s+t==k-1:return -(q**(3*k-2))
  return q**(2*k+s+t) -(q+1)*q**(3*k-2)
 if s==k:
  return q**(3*k)+(q**3-1)*sum(q**(4*k-h-3) for h in range(k))
 L=k-s
 return q**(3*k) +(q**3-1)*sum(q**(4*k-h-3) for h in range(L,k)) - q**(4*k-L-2)

def exact_cyclotomic_value(D,p,k,s,t):
 n=p**k
 hist=np.zeros(n,dtype=np.int64)
 for ix,v in np.ndenumerate(D):
  if v:
   e=((p**s*ix[0] if s<k else 0)+(p**t*ix[4] if t<k else 0))%n
   hist[e]+=1
 # Reduce modulo Phi_{p^k}(X)=sum_{j=0}^{p-1} X^{j*p^{k-1}}; no numerical error.
 d=n-p**(k-1);step=p**(k-1)
 c=hist.tolist()
 for j in range(n-1,d-1,-1):
  a=c[j]
  if a:
   for r in range(p):c[j-r*step]-=a
 assert all(u==0 for u in c[d:])
 if any(c[1:d]):raise AssertionError(('not rational',p,k,s,t,c[:d]))
 return c[0]

def cyclic(p,k):
 n=p**k
 D=domain_indicator(n)
 fourier=np.fft.fftn(D)
 false_positive=0;false_negative=0
 for ix in itertools.product(range(n),repeat=6):
  a=ix[:3];b=ix[3:]
  vanishing=all((a[i]*b[j]-a[j]*b[i])%p**max(k-1,0)==0 for i,j in ((0,1),(0,2),(1,2)))
  gotzero=abs(fourier[ix]) <1e-5
  if vanishing!= (not gotzero):
   if vanishing:false_positive+=1
   else:false_negative+=1
 assert false_positive==false_negative==0,(false_positive,false_negative)
 rank=int(np.count_nonzero(np.abs(fourier)>1e-5))
 dprev=1 if k==1 else int(p**(3*(k-1))+(p**3-1)*sum(p**(4*(k-1)-h-3) for h in range(k-1)))
 assert rank ==p**6 * dprev,(p,k,rank,p**6*dprev)
 # each Smith stratum: exact cyclotomic polynomial rational coefficient, and analytic formula.
 for s in range(k+1):
  for t in range(s,k+1):
   got=exact_cyclotomic_value(D,p,k,s,t)
   expected=predicted_H(p,k,s,t)
   assert got==expected,(p,k,s,t,got,expected)
 print('CYCLIC_OK',p,k,'ambient_quotient',n**6,'commuting_quotient',D.sum(),'fourier_support',rank,'smith_types',(k+1)*(k+2)//2)

def noncyclic_dual_numbers():
 # F_2[t]/t^2 in representation c0+2*c1 t. The generating character is (-1)^c1.
 n=4
 def mul(a,b):return ((a&1)*(b&1)) +2*((((a&1)*((b>>1)&1))+(((a>>1)&1)*(b&1)))&1)
 def wedge(u,v):return all(mul(u[i],v[j])==mul(u[j],v[i]) for i,j in ((0,1),(0,2),(1,2)))
 tensor=np.zeros(4096,dtype=np.int64)
 all3=list(itertools.product(range(n),repeat=3))
 def idx_tuple(z):return sum(c<<(2*i) for i,c in enumerate(z))
 for u in all3:
  for v in all3:
   if wedge(u,v):tensor[idx_tuple(u+v)]=1
 # Walsh--Hadamard transforms over the twelve independent F2 coordinates.
 w=tensor.copy()
 for bit in range(12):
  for i in range(4096):
   if i&(1<<bit):continue
   j=i|(1<<bit); a=w[i];b=w[j];w[i]=a+b;w[j]=a-b
 rank=0
 for f in itertools.product(range(n),repeat=6):
  mask=0
  for i,a in enumerate(f):
   # coefficient of t in a*z:  a0*z1 +a1*z0; swap frequency bit pair
   mask|=((a&1)<<(2*i+1)) | (((a>>1)&1)<<(2*i))
  got=w[mask]
  vanishing=all(mul(f[i],f[3+j])==mul(f[j],f[3+i]) for i,j in ((0,1),(0,2),(1,2)))
  # Independently classify Smith valuations over F2[t]/t^2.
  def val(v):return 2 if v==0 else (0 if v&1 else 1)
  s=min(map(val,f))
  if s==2:t=2
  elif s==0:
   minors=[mul(f[i],f[3+j]) ^ mul(f[j],f[3+i]) for i,j in ((0,1),(0,2),(1,2))]
   t=min(map(val,minors))
  else:
   # all entries are multiples of t; divide by t, reduce modulo t.
   p0=[v>>1 for v in f]
   minors=[(p0[i]*p0[3+j]-p0[j]*p0[3+i])&1 for i,j in ((0,1),(0,2),(1,2))]
   t=1 if any(minors) else 2
  exp=predicted_H(2,2,s,t)
  assert got==exp,(f,s,t,got,exp)
  rank+=(got!=0)
 assert rank==1408
 print('NONCYCLIC_OK','F2[t]/t^2','fourier_support',rank,'all_4096_exact_Walsh_coefficients')

if __name__=='__main__':
 for p,k in [(2,1),(3,1),(2,2),(3,2),(2,3)]:cyclic(p,k)
 noncyclic_dual_numbers()
 print('ALL_COMMUTING_CHAIN_CHECKS_PASSED')
