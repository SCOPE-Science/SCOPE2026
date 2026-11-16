"""Reproduce the icosahedral qutrit orbit spectrum and its 30-projector 2-design.
Run: python check_icosahedral_design.py  (requires NumPy and SciPy).
The theorem's all-fiducial assertion is proved by character theory in RESULT.md;
the checks below test independent numerical instances and the explicit design.
"""
import numpy as np
from scipy.spatial.transform import Rotation

G = Rotation.create_group('I').as_matrix()
assert len(G) == 60
assert np.max(np.abs(np.linalg.det(G)-1)) < 1e-12
Z = np.diag([-1., -1., 1.])
assert min(np.linalg.norm(R-Z) for R in G) < 1e-12

H=[]
for i in range(3):
    m=np.zeros((3,3),complex); m[i,i]=1;H.append(m)
for i in range(3):
  for j in range(i+1,3):
    m=np.zeros((3,3),complex);m[i,j]=m[j,i]=2**-.5;H.append(m)
    m=np.zeros((3,3),complex);m[i,j]=1j*2**-.5;m[j,i]=-1j*2**-.5;H.append(m)
assert max(abs(np.trace(x@y)-(i==j)) for i,x in enumerate(H) for j,y in enumerate(H))<1e-12

def projectors(v):
  return [np.outer(R@v,np.conjugate(R@v)) for R in G]

def matrix_of(Ps):
  A=np.array([[np.trace(Q@h).real for h in H] for Q in Ps])
  assert np.max(abs(A.imag))<1e-12
  return A.T@A

def test(v):
  v=np.array(v,complex);v/=np.linalg.norm(v)
  t=abs(np.dot(v,v))**2
  expected=np.sort([20]+[10*(1-t)]*3+[2*(1+3*t)]*5)
  got=np.linalg.eigvalsh(matrix_of(projectors(v)))
  assert np.max(abs(got-expected))<2e-11, (t,got,expected)
  return t

rng=np.random.default_rng(20261114)
for _ in range(80):
   test(rng.normal(size=3)+1j*rng.normal(size=3))
test([1,0,0]);test([1,1j,0]);test([1/np.sqrt(2),0,1j/np.sqrt(2)])
a=np.sqrt((1+1/np.sqrt(2))/2)
b=np.sqrt((1-1/np.sqrt(2))/2)
v=np.array([a,1j*b,0])
assert abs(test(v)-0.5)<1e-13
full=projectors(v)
unique=[]
for P in full:
 if all(np.linalg.norm(P-Q)>1e-9 for Q in unique):unique.append(P)
assert len(unique)==30
assert all(sum(np.linalg.norm(P-Q)<1e-9 for Q in full)==2 for P in unique)
K=matrix_of(unique)
assert np.max(abs(np.linalg.eigvalsh(K)-np.sort([10]+[2.5]*8)))<1e-11
for X in H:
 lhs=sum(np.trace(X@P).real*P for P in unique)
 rhs=2.5*(X+np.trace(X).real*np.eye(3))
 assert np.linalg.norm(lhs-rhs)<2e-11
 assert np.linalg.norm(.4*lhs - .1*sum(np.trace(X@P).real for P in unique)*np.eye(3)-X)<2e-11
print('PASS: icosahedral order 60, 83 fiducials, exact spectral levels, 30-line projective 2-design and recovery identity')
