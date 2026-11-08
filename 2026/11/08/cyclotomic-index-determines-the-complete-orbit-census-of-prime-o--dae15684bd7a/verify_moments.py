"""Independent finite-field subgroup moments and first surviving cyclotomic coefficient."""
from math import comb, factorial

def primes(n):
 return [p for p in range(3,n+1,2) if all(p%d for d in range(3,int(p**.5)+1,2))]
count=0
for p in primes(127):
 for k in range(3,p):
  if (p-1)%k:continue
  d=(p-1)//k
  if d%2:continue
  subgroup={pow(x,k,p) for x in range(1,p)}
  assert len(subgroup)==d
  assert all(sum(pow(x,j,p) for x in subgroup)%p==0 for j in range(1,d))
  coeff=[sum(comb(x,j) for x in subgroup)%p for j in range(d+1)]
  assert coeff[0]==d%p
  assert coeff[1:d]==[0]*(d-1)
  assert coeff[d]==d*pow(factorial(d),-1,p)%p
  ell=next(t for t in range(1,p) if pow(d,t,p)==1)
  assert (p**d-1)%ell==0
  assert (p**p-p**d)%(p*ell)==0
  count+=1
print('PASS independent subgroup-moment families:',count,'odd primes through 127')
