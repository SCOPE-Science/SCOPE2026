"""Exact and independently quadrature-checked tetrahedral-cap concentration identity.

Run: python verify_tetra_caps.py ; requires sympy, numpy.
"""
import math
import numpy as np
import sympy as s

c,t=s.symbols('c t',real=True)
P4=(35*t**4-30*t**2+3)/8
Q=c*(1-c**2)*(7*c**2-3)
k4=s.integrate(P4,(t,c,1))/2
assert s.simplify(k4-Q/16)==0
# Uniform-sphere second and fourth moments, and tetrahedron evaluation sums.
mean_D=s.Rational(4,15) # q=x^2-y^2, squared
mean_O=s.Rational(1,15) # q=xy, squared
# Sum_{u in tetrahedron}q(u)^2 is respectively 0 and 4/9.
val_D=0
val_O=s.Rational(4,9)
# Tetrahedron is a degree-2 design: sum H_2(u)=0.
# Product q^2 has harmonic components in degrees 0,2,4.
lam_D=s.factor(2*(1-c)+k4*(val_D-4*mean_D)/mean_D)
lam_O=s.factor(2*(1-c)+k4*(val_O-4*mean_O)/mean_O)
assert s.simplify(lam_D-(2*(1-c)-Q/4))==0
assert s.simplify(lam_O-(2*(1-c)+Q/6))==0
assert s.simplify(2*lam_D+3*lam_O-10*(1-c))==0
assert s.simplify(lam_D-lam_O+5*Q/12)==0
assert s.simplify(lam_D-(c-1)**2*(7*c**3+14*c**2+11*c+8)/4)==0
assert s.limit(lam_O/lam_D*(1-c),c,1)==s.Rational(1,3)
cstar=s.sqrt(s.Rational(3,7))
assert 1/s.sqrt(3)<cstar<1
assert s.simplify(lam_D.subs(c,cstar)-lam_O.subs(c,cstar))==0
assert s.simplify(lam_D.subs(c,cstar)-2*(1-cstar))==0

U=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],dtype=float)/math.sqrt(3)

def basis(x):
    a,b,d=x
    return np.array([math.sqrt(15/4)*(a*a-b*b),
                     math.sqrt(5/4)*(a*a+b*b-2*d*d),
                     math.sqrt(15)*a*b,math.sqrt(15)*a*d,math.sqrt(15)*b*d])

def numerical_gram(cc, centers=U):
    z,w=np.polynomial.legendre.leggauss(10)
    tt=cc+(1+z)*(1-cc)/2
    wt=w*(1-cc)/2
    G=np.zeros((5,5),dtype=float)
    for u in centers:
        h=np.array([0.,0.,1.]) if abs(u[2])<0.9 else np.array([1.,0.,0.])
        v=np.cross(u,h)
        v/=np.linalg.norm(v)
        wv=np.cross(u,v)
        for k, tk in enumerate(tt):
            r=math.sqrt(max(0.,1-tk*tk))
            for j in range(24):
                ph=2*math.pi*j/24
                x=tk*u+r*(math.cos(ph)*v+math.sin(ph)*wv)
                b=basis(x)
                G+=np.outer(b,b)*(wt[k]/(2*24))
    return G

for cc in (1/math.sqrt(3),0.60,math.sqrt(3/7),0.70,0.88,0.975):
    G=numerical_gram(cc)
    expected=np.diag([float(lam_D.subs(c,cc))]*2+[float(lam_O.subs(c,cc))]*3)
    err=np.max(np.abs(G-expected))
    assert err<2e-13,(cc,err)
    print(f'CAP_CHECK c={cc:.12f} lambda_diagonal={expected[0,0]:.12f} lambda_mixed={expected[2,2]:.12f} max_matrix_error={err:.3e}')
# General isotropic-center law: normalize the cap mixture to a probability measure.
for centers in (U, np.eye(3), np.vstack([np.eye(3),-np.eye(3)])):
    G=numerical_gram(float(cstar), centers)
    mass=len(centers)*(1-float(cstar))/2
    assert np.max(np.abs(G/mass-np.eye(5)))<2e-13
    assert np.max(np.abs(centers.T@centers/len(centers)-np.eye(3)/3))<2e-15
print('ISOTROPIC_CAP_FILTER_PASS exact_symbolic=8 quadrature_radii=6 center_designs=3')
