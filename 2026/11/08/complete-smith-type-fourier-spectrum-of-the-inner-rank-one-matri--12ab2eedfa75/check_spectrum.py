"""Exact numerical and combinatorial checks for inner-rank-one Cayley graph spectra.
This script uses only standard Python and NumPy and performs finite tests only.
"""
from collections import Counter
import numpy as np

def order(p,k):
 return p**k

def primitive_size(p,n):
 return p**(3*n-3)*(p-1)*(p+1)**2

def eigenvalue(p,k,a,b):
 assert 0<=a<=b<=k
 D=sum(primitive_size(p,n) for n in range(1,min(a,k)+1))
 if a==b==k: return D
 if a==b: return D-p**(3*a)*(p+1)
 if b==k:
  return D +p**(3*a)*(p*p-p-1)+sum((p-1)*p**(2*n+a-1) for n in range(a+2,k+1))
 return D+p**(3*a)*(p*p-p-1)+sum((p-1)*p**(2*n+a-1) for n in range(a+2,b+1))-p**(2*b+a+1)

def multiplicity(p,k,a,b):
 if a==b==k:return 1
 if b==k:return primitive_size(p,k-a)
 if a==b:return p**(4*(k-a-1)+1)*(p-1)**2*(p+1)
 return p**(4*k-3*a-b-4)*(p-1)**2*(p+1)**2

def expected(p,k):
 v=Counter()
 for a in range(k+1):
  for b in range(a,k+1):
   v[eigenvalue(p,k,a,b)]+=multiplicity(p,k,a,b)
 assert sum(v.values())==p**(4*k)
 assert 0 not in v
 return v

def direct(p,k):
 q=p**k
 gen=set()
 for n in range(1,k+1):
  qq=p**n;scale=p**(k-n)
  vec=[(u,v) for u in range(qq) for v in range(qq) if u%p or v%p]
  for a,b in vec:
   for c,d in vec:
    gen.add(tuple(scale*t for t in ((a*c)%qq,(a*d)%qq,(b*c)%qq,(b*d)%qq)))
 assert (0,0,0,0) not in gen
 f=np.zeros((q,)*4,dtype=np.float64)
 for a in gen: f[a]=1
 z=np.fft.fftn(f)
 assert np.max(np.abs(z.imag))<1e-6
 assert np.max(np.abs(z.real-np.rint(z.real)))<1e-5
 return Counter(int(v) for v in np.rint(z.real).astype(np.int64).ravel()),len(gen)

for p,k in [(2,1),(2,2),(2,3),(2,4),(3,1),(3,2),(3,3),(5,1)]:
 obs,degree=direct(p,k);pred=expected(p,k)
 assert obs==pred,(p,k,obs,pred)
 assert degree==sum(primitive_size(p,n) for n in range(1,k+1))
 print(f'p={p} k={k} degree={degree} vertices={p**(4*k)} distinct={len(pred)} spectrum={sorted(pred.items())} PASS')
for p in [2,3,5,7]:
 for k in range(2,9):
  spec=expected(p,k)
  assert min(abs(v) for v in spec)==p+1
  assert spec[-(p+1)]==p**(4*(k-1)+1)*(p-1)**2*(p+1)
  assert all(abs(v)>=p+1 for v in spec)
print('INNER_RANK_ONE_CAYLEY_SPECTRUM_PASS')
