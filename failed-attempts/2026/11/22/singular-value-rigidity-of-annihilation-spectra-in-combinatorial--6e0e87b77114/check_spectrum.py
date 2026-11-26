"""Numerically checks the mutual-annihilation spectrum of finite zero Rees semigroups."""
import itertools,numpy as np

def check(Z):
 Z=np.asarray(Z,dtype=int); n,m=Z.shape
 B=np.zeros((m*n,m*n),dtype=int)
 for i,l,k,u in itertools.product(range(m),range(n),range(m),range(n)):
  x=i*n+l;y=k*n+u
  B[x,y]=int((None if Z[l,k] else (i,u)) is None and (None if Z[u,i] else (k,l)) is None)
 assert np.array_equal(B,B.T)
 s=np.linalg.svd(Z.astype(float),compute_uv=False)
 s=s[s>1e-8]
 r=len(s)
 pred=sorted([s[j]**2 for j in range(r)]+[a*s[j]*s[b] for a in (1,-1) for j in range(r) for b in range(j+1,r)]+[0.]*(n*m-r*r))
 actual=sorted(np.linalg.eigvalsh(B))
 assert np.allclose(pred,actual,atol=1e-7),(Z,pred,actual)
 z=int(Z.sum())
 assert int(B.trace())==z
 assert int(B.sum())==z*z
 assert int(np.sum(B*B))==z*z
 assert int(np.trace(B@B@B))==int(np.trace(Z@Z.T@Z@Z.T@Z@Z.T))
 assert np.isclose(sum(abs(v) for v in actual),sum(s)**2)
 return n,m,r,z
if __name__=='__main__':
 total=0
 for n in range(1,4):
  for m in range(1,4):
   for mask in range(1<<(n*m)):
    Z=np.array([(mask>>j)&1 for j in range(n*m)]).reshape((n,m))
    if any(np.all(Z[x,:]==1) for x in range(n)) or any(np.all(Z[:,y]==1) for y in range(m)):
     continue # P must have nonzero in each row/column
    check(Z)
    total+=1
 print(f'PASS: exhaustive regular sandwich zero patterns, dimensions 1..3 x 1..3: {total}')
 rng=np.random.default_rng(20261117)
 for n,m in [(4,4),(4,5),(5,4),(6,6)]:
  for j in range(100):
   Z=rng.integers(0,2,size=(n,m));check(Z)
 print('PASS: 400 independent rectangular/square random binary patterns')
