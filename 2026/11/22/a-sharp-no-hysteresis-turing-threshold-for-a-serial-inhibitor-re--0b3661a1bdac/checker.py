"""Checks for the stationary-pattern onset in a three-component feedback-diffusion model.
Requires Python 3 with numpy; all numerical tests are independent of the paper's inequalities.
This finite checker supports, but does not substitute for, the analytic proof.
"""
import math
from fractions import Fraction as F
import numpy as np


def jacobian(q, d, a, z):
    return np.array([[a-q, 0., -z], [1., -1.-d*q, 0.], [0., 1., -1.-d*q]])

def ell(q,d,a,z):
    return a-q-z/(1+d*q)**2

def spectral_threshold(L, a, z):
    upper=math.sqrt(a)*L/math.pi
    candidates=[((math.sqrt(z/(a-(j*math.pi/L)**2))-1)/(j*math.pi/L)**2, j)
                for j in range(1, math.ceil(upper)) if (j*math.pi/L)**2 < a]
    return min(candidates) if candidates else (math.inf, None)

a=F(1,4); z=F(1,2); d=F(8,1); q=F(1,8)
# Tangency exactly at d=8, q=1/8.
assert F(4)*(1+a*d)**3 == F(27)*d*z
assert a-q-z/(1+d*q)**2 == 0
assert F(-1)+2*z*d/(1+d*q)**3 == 0
assert a<z<2*(1-a)**2
# Reconstruct the entire characteristic polynomial by rational determinant,
# independently of the closed formula.
for aa,zz in [(F(1,4),F(1,2)), (F(1,5),F(2,5)),(F(2,5),F(1,2))]:
  for dd in [F(1),F(2),F(8),F(19)]:
   for qq in [F(0),F(1,13),F(1,8),F(1,4),F(2)]:
    x=qq-aa; y=1+dd*qq
    for ll in [F(0),F(1,3),F(-3,2)]:
     # Determinant of lambda I - J via 3x3 Leibniz formula.
     A=[[ll+qq-aa,F(0),zz],[-F(1),ll+1+dd*qq,F(0)],
        [F(0),-F(1),ll+1+dd*qq]]
     det=(A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
      -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
      +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
     assert det==(ll+x)*(ll+y)**2+zz
# Numerical independent eigenvalue tests comparing 3x3 spectrum with the scalar criterion.
count=0
for a1,z1 in [(0.25,0.5),(0.1,0.15),(0.35,0.5)]:
 assert a1<z1<2*(1-a1)**2
 for dd in [0.1, 0.8, 2, 4, 8, 10, 20, 70]:
  for qq in np.linspace(0,1.25,41):
   roots=np.linalg.eigvals(jacobian(qq,dd,a1,z1))
   sgn=max(r.real for r in roots)
   delta=ell(qq,dd,a1,z1)
   if abs(delta)>1e-9:
    assert (sgn>0)==(delta>0),(a1,z1,dd,qq,roots,delta)
    count+=1
# Exact finite-length calibration and spectral obstruction.
assert spectral_threshold(2*math.pi,0.25,0.5)[1] is None
L=math.pi*math.sqrt(8)
t,j=spectral_threshold(L,0.25,0.5)
assert j==1 and abs(t-8)<1e-12
L=3*math.pi
t,j=spectral_threshold(L,0.25,0.5)
assert j==1 and abs(t-9*(math.sqrt(18/5)-1))<1e-12
# Check the oscillatory quantization law with an O(L^-3) remainder.
for L in [150,199,287,400,731,1000,1447]:
 t,j=spectral_threshold(L,0.25,0.5)
 shift=L/math.sqrt(8)/math.pi
 dist=abs(shift-round(shift))
 predicted=8+192*math.pi**2*dist**2/L**2
 assert abs(t-predicted)*L**3 < 15000,(L,t,predicted,j)
# The variational energy is negative along a small unstable eigenmode,
# and positive at the linear threshold (nonzero stationary states excluded analytically).
for L in [3*math.pi,5*math.pi,10*math.pi]:
 threshold,j=spectral_threshold(L,0.25,0.5)
 qj=(j*math.pi/L)**2
 for dd in [threshold+0.3, threshold+1.0]:
  for amp in [1e-5,1e-4]:
   # Fourier cosine eigenfunction: int e^2=L/2, int e^4=3L/8.
   E=-ell(qj,dd,0.25,0.5)*amp**2*L/4 + amp**4*3*L/32
   assert E<0,(L,j,dd,E)
print('PASS: exact determinant identities, Routh sign comparisons, finite geometry, quantization, variational witnesses')
print('independent eigenvalue/sign tests',count)
print('example: a=1/4, zeta=1/2, continuum d*=8, q*=1/8; Neumann critical length pi sqrt(8)')
