"""Independent reproducible verification for sign-count-layer spherical Slepian spectra.
The theory proves the all-dimensional formula. These finite tests independently
construct the full matrix from individually enumerated sign patterns and angular
absolute moments, comparing eigenvalues to incidence-eigenvalue expressions.
"""
from itertools import combinations, product
from math import comb, pi
import numpy as np

def rho(d,s,m):
 q=d-s
 return sum((-1)**j * comb(m,j) * comb(d-m,q-j)
            for j in range(max(0,q-(d-m)),min(m,q)+1))/comb(d,q)

def prediction(d,k,s):
 c=2/pi; w=comb(d,s)/2**d
 b=[c**(k-r)*rho(d,s,2*(k-r)) for r in range(k+1)]
 a=[sum((-1)**(l-r)*comb(l,r)*b[r] for r in range(l+1)) for l in range(k+1)]
 ev=[w*sum(a[l]*comb(k-i,l-i)*comb(d-l-i,k-l) for l in range(i,k+1)) for i in range(k+1)]
 mult=[comb(d,i)-(comb(d,i-1) if i else 0) for i in range(k+1)]
 return ev,mult

def direct(d,k,s):
 """Compute without rho/inclusion diagonalization: sum actual sign contributions."""
 sets=[set(q) for q in combinations(range(d),k)]
 c=2/pi
 signs=[p for p in product((-1,1),repeat=d) if sum(z==1 for z in p)==s]
 M=np.empty((len(sets),len(sets)))
 for i,S in enumerate(sets):
  for j,T in enumerate(sets):
   E=S^T
   sig=sum(np.prod([sg[z] for z in E]) for sg in signs)
   M[i,j] = 2**(-d) * c**(k-len(S&T))*sig
 return M

def check(d,k,s):
 ev,mm=prediction(d,k,s); M=direct(d,k,s)
 want=np.array(sorted([e for e,n in zip(ev,mm) for _ in range(n)]))
 got=np.linalg.eigvalsh(M)
 err=np.max(abs(got-want))
 assert err<1e-12,(d,k,s,err)
 assert min(ev)>-1e-12 and max(ev)<1+1e-12
 assert abs(sum(e*m for e,m in zip(ev,mm))-comb(d,k)*comb(d,s)/2**d)<1e-12
 return err

cases=[(4,1,s) for s in range(5)]+[(6,2,s) for s in range(7)]+[(6,3,s) for s in (0,1,2,3,4,5,6)]+[(7,3,s) for s in (0,1,2,3,5,7)]+[(8,3,s) for s in (0,1,2,3,4,6,8)]+[(8,4,s) for s in (0,2,4,6,8)]
for d,k,s in cases:
 err=check(d,k,s)
 print(f'd={d} k={k} s={s} error={err:.2e} spectrum={np.round(prediction(d,k,s)[0],9).tolist()}')
for d in range(2,40):
 for s in range(d+1):
  lam,m=prediction(d,1,s)
  cond=abs(lam[0]-lam[1])<1e-14
  assert cond == ((2*s-d)**2==d),(d,s)
print('ALL TESTS PASSED',len(cases),'full matrix checks; dipole equality d=2..39')
