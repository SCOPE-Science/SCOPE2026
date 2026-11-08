from itertools import product, combinations
from fractions import Fraction
from math import prod

def es(vals,k):
    if k==0: return 1
    if not 0<=k<=len(vals): return 0
    return sum(prod(v) for v in combinations(vals,k))
checks=0; equality=0
for d in range(2,8):
  for K in (2,3,4):
    for lam in product(range(1,K+1),repeat=d):
      if min(lam)!=1 or max(lam)!=K:continue
      for n in range(1,d+1):
        den=es(lam,n)
        pis=[Fraction(lam[i]*es(lam[:i]+lam[i+1:],n-1),den) for i in range(d)]
        assert sum(pis)==n
        low=min(pis); high=max(pis)
        bl=Fraction(n,n+(d-n)*K)
        br=Fraction((d-n)*K+n-1,d-1)
        assert low>=bl,(d,n,K,lam,pis,bl)
        assert high/low<=br,(d,n,K,lam,pis,br)
        checks+=4
        if list(lam).count(1)==1 and list(lam).count(K)==d-1:
          assert low==bl and high/low==br,(d,n,K,lam,pis)
          equality+=2
print('PASSED exact rational assertions:',checks+equality, 'examples', 'all d=2..7, K=2..4, all spectra with smallest 1 largest K; n=1..d')
