"""Independent finite checks for balanced two-circle quadratic phase retrieval.
Requires numpy, scipy. The unrestricted theorem follows from the accompanying proof.
"""
import numpy as np
from scipy.integrate import quad

def grid(r,s,phi):
    return [rho*np.exp(1j*(ang+k*np.pi/2)) for rho,ang in ((r,0),(s,phi)) for k in range(4)]

def evalH(H,z):
    w=np.array([1,np.conj(z),np.conj(z)**2])
    return np.vdot(w,H@w).real

def mat_basis():
    E=[]
    for j in range(3):
        a=np.zeros((3,3),dtype=complex);a[j,j]=1;E.append(a)
    for j in range(3):
      for k in range(j+1,3):
        a=np.zeros((3,3),dtype=complex);a[j,k]=a[k,j]=1;E.append(a)
        a=np.zeros((3,3),dtype=complex);a[j,k]=1j;a[k,j]=-1j;E.append(a)
    return E

def matrix(zs): return np.array([[evalH(H,z) for H in mat_basis()] for z in zs])

for r,s,phi,rank in [(1,2,np.pi/4,8),(.4,1.8, np.pi/7,8),(2,1,-np.pi/4,8),(1,2,0,7),(1,2,np.pi/2,7),(1,1,np.pi/4,5),(1,1,0,4)]:
    M=matrix(grid(r,s,phi));actual=np.linalg.matrix_rank(M, tol=2e-10)
    print('r,s,phi,rank',r,s,phi,actual)
    assert actual==rank, (r,s,phi,actual,rank)
    K=np.diag([r*r*s*s,-r*r-s*s,1])
    assert max(abs(evalH(K,z)) for z in grid(r,s,phi))<1e-10

for r,s in [(.8,1.9),(1,2),(1.5,2.5)]:
  for phi in [0,np.pi/2,np.pi]:
    p=lambda z:z*z+1j*r*s
    q=lambda z:np.sqrt(r*r+s*s)*z
    assert max(abs(abs(p(z))**2-abs(q(z))**2) for z in grid(r,s,phi))<1e-8
  assert max(abs(abs(p(z))**2-abs(q(z))**2) for z in grid(r,s,np.pi/4))>0.05
for r in [.5,1.5,2.2]:
   for z in grid(r,r,.41):
      assert abs(abs(z-2*r)**2-abs(2*z-r)**2)<1e-9

# Fourier transform of Gaussian-modulated integrable convolution kernel:
# ∫ exp(-π a u²)exp(2πi(ν−ξ)u)du = a^-1/2 exp(-π(ξ−ν)²/a)
for a in [.7,1.5]:
 for shift in [-1.,.3,1.2]:
    re=quad(lambda u: np.exp(-np.pi*a*u*u)*np.cos(2*np.pi*shift*u),-8,8,epsabs=1e-11)[0]
    im=quad(lambda u: np.exp(-np.pi*a*u*u)*np.sin(2*np.pi*shift*u),-8,8,epsabs=1e-11)[0]
    exact=a**(-.5)*np.exp(-np.pi*shift*shift/a)
    assert abs(re-exact)+abs(im)<1e-9
print('BALANCED_QUADRATURE_CHECKS_PASSED')
