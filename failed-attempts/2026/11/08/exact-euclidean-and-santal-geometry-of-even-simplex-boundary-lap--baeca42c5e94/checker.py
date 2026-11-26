"""Standalone finite numerical cross-checks of Euclidean formulas for simplex-boundary top Laplacian polytopes.
Requires numpy/scipy; exact identities in the proof hold in every dimension."""
import math
import numpy as np
from numpy.linalg import norm
from scipy.linalg import null_space
from scipy.spatial import ConvexHull

def test(N):
 s=np.array([1 if i%2==0 else -1 for i in range(N)],dtype=float)
 L=N*np.eye(N)-np.outer(s,s)
 assert norm(L@L-N*L)<1e-7
 C=L-np.outer(L@np.ones(N),np.ones(N))/N
 cov=C@C.T/(N*(N+1))
 if N%2==0:
  k=N//2; d=N-2
  m=(L@np.ones(N))/N
  assert norm(m-np.ones(N))<1e-8
  U=null_space(np.array([np.ones(N),s]))
  coords=(L-np.ones((N,N))).T@U
  hull=ConvexHull(coords)
  V=k*N**d/math.factorial(d)
  r=math.sqrt(N/(k-1))  # = sqrt(2k/(k-1))
  R=math.sqrt(N*(N-2))
  assert abs(hull.volume/V-1)<1e-7,(N,hull.volume,V)
  assert len(hull.simplices)==k*k,(N,len(hull.simplices),k*k)
  assert np.max(np.abs(hull.equations[:,-1]+r))<1e-7,(N,hull.equations[:,-1],r)
  assert np.max(np.abs(norm(coords,axis=1)-R))<1e-7
  # Independently integrate exact second moments over all equal-volume
  # simplices joining the origin to every hull facet (each is a d-simplex).
  second=np.zeros((d,d))
  for facet in hull.simplices:
   P=coords[facet,:]
   total=P.sum(axis=0)
   second+=(P.T@P+np.outer(total,total))/((d+1)*(d+2))
  second/=len(hull.simplices)
  assert np.max(np.abs(second-N/(N-1)*np.eye(d)))<1e-7,(N,second)
  polar=np.array([-a[:-1]/a[-1] for a in hull.equations])
  polar_volume=ConvexHull(polar).volume
  formula_polar=k**(2*k-1)/(N**d*math.factorial(k-1)**2)
  assert abs(polar_volume/formula_polar-1)<1e-7,(N,polar_volume,formula_polar)
  print('even d=',d,'V=',V,'polar=',formula_polar,'radius=',r,'cov=',N/(N-1),'facets=',len(hull.simplices))
 else:
  U=null_space(s.reshape(1,-1))
  spec=np.linalg.eigvalsh(U.T@cov@U)
  goal=[1/(N*(N+1))]+[N/(N+1)]*(N-2)
  assert np.max(np.abs(spec-goal))<1e-8,(N,spec,goal)
  print('odd d=',N-2,'full dimension=',N-1,'cov eigenvalues=',goal)
for N in range(3,11):test(N)
print('LAPLACIAN_METRIC_FINITE_CHECKS_PASSED')
