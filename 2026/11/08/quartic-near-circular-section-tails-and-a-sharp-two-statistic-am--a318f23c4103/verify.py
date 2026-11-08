"""Independent numerical and exact-algebra diagnostics for near-circular ellipsoid sections.

Requires numpy and scipy. Run: python verify.py
"""
from fractions import Fraction as F
from math import pi, sqrt
import numpy as np
from scipy.stats import qmc


def eccentricity_squared(normals, d):
    """Stable characteristic-polynomial formula for restriction of diag(d)."""
    n = np.asarray(normals, dtype=float)
    d = np.asarray(d, dtype=float)
    s1 = np.sum(n*n*d, axis=-1)
    s2 = np.sum(n*n*d*d, axis=-1)
    tr = d.sum()-s1
    tr2 = np.sum(d*d)-2*s2+s1*s1
    gap = np.sqrt(np.maximum(0, 2*tr2-tr*tr))
    return 2*gap/(tr+gap)


def independent_eccentricity(n,d):
    v=np.cross(n, [0.,0.,1.])
    if np.linalg.norm(v)<1e-7: v=np.cross(n,[1.,0.,0.])
    v=v/np.linalg.norm(v)
    w=np.cross(n,v)
    mat=np.array([[np.dot(d*v,v),np.dot(d*v,w)],
                  [np.dot(d*w,v),np.dot(d*w,w)]])
    eig=np.linalg.eigvalsh(mat)
    return 1-eig[0]/eig[1]


def coeff(a,b,c): return b*b/(4*(b-a)*(c-b))

rng=np.random.default_rng(7614)
for d in ([1.,2.,4.],[1.,1.6,3.7],[0.15,3.,5.]):
    nn=rng.normal(size=(1500,3));nn/=np.linalg.norm(nn,axis=1)[:,None]
    e2=eccentricity_squared(nn,d)
    alt=np.array([independent_eccentricity(n,np.array(d)) for n in nn])
    assert max(abs(e2-alt))<1e-10

for d in ([1.,2.,4.],[1.,1.6,3.7]):
    a,b,c=d;u=(b-a)/(c-a);v=(c-b)/(c-a)
    for signs in ((1,1),(-1,1),(1,-1),(-1,-1)):
        normal=np.array([signs[0]*sqrt(u),0.,signs[1]*sqrt(v)])
        assert abs(eccentricity_squared(normal,d))<1e-7

# Exact ambiguity: two distinct sets of inverse-square axes have identical
# maximum eccentricity and fourth-order rare-section coefficient.
R=F(4);t=F(2)
t2=R*t/((R+1)*t-R)
assert t2==F(4,3)
cf=lambda x: x*x/(4*(x-1)*(R-x))
assert cf(t)==cf(t2)==F(1,2)
assert 1-F(1,R)==F(3,4)
assert (2*R/(R+1))==F(8,5)
assert cf(F(8,5))==F(4,9)

# Uniform normals on the sphere (Sobol inverse cylindrical coordinates).
s=qmc.Sobol(d=2,scramble=True,seed=61).random_base2(m=20)
z=2*s[:,0]-1
ang=2*pi*s[:,1]
normals=np.column_stack((np.sqrt(1-z*z)*np.cos(ang),
                         np.sqrt(1-z*z)*np.sin(ang),z))
tri=eccentricity_squared(normals,[1.,2.,4.]);C=coeff(1.,2.,4.)
ratios=[]
for eps in (0.40,0.30,0.22):
    observed=np.mean(tri<=eps**2)
    ratios.append(observed/eps**4)
assert ratios[0]>ratios[1]>ratios[2]>C
assert abs(ratios[-1]-C)<0.065

# Closed-form axisymmetric laws, tested in both types.
for d,rate,formula in [
 ([1.,1.,4.], F(1,6), lambda y:1-np.sqrt(1-(y/(3*(1-y))))),
 ([1.,2.,2.], F(1), lambda y:1-np.sqrt(1-2*y)),
]:
    vals=eccentricity_squared(normals,d)
    for y in (0.025,0.05,0.10):
        assert abs(np.mean(vals<=y)-formula(y))<0.002
    assert abs(formula(1.e-5)/1.e-5-float(rate))<5.e-5

print('VERIFY_OK alternative_plane_bases=4500 circular_normals=8 sobol_normals=1048576 exact_ambiguity=1 axisymmetric_CDF_cases=6 quartic_coeff=0.5')
