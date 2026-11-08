"""Checks of an explicit family of planar polynomial circle bifurcations.
Run: python verify.py (requires sympy, scipy, numpy)."""
from math import pi, sqrt, exp
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad

x,y,s,eps,b,c,h=sp.symbols('x y s eps b c h',real=True)
F=(s-1)*(s-4)
C=c+h*x
P=eps*F.subs(s,x*x+y*y)+C*y
Q=b*F.subs(s,x*x+y*y)-C*x
rad=sp.expand(2*x*P+2*y*Q)
assert sp.simplify(rad-2*F.subs(s,x*x+y*y)*(eps*x+b*y))==0
# Neutral first-integral d/dt[I(s)-(2b/h)log(C)]=0 when eps=0.
assert sp.simplify(rad.subs(eps,0)/F.subs(s,x*x+y*y)-2*b*(sp.diff(C,x)*P.subs(eps,0)+sp.diff(C,y)*Q.subs(eps,0))/(h*C))==0
# Correct Jacobian formula.
J=sp.Matrix([P,Q]).jacobian([x,y]);
assert sp.simplify(J[0,0]-2*eps*x*sp.diff(F,s).subs(s,x*x+y*y)-h*y)==0
assert sp.simplify(J[1,0]-2*b*x*sp.diff(F,s).subs(s,x*x+y*y)+C+h*x)==0
# Variational integral compared with closed form for m=2,3,4 and several eps signs.
for radii in [[1.,2.],[0.5,1.,2.],[0.3,0.7,1.2,2.]]:
    roots=[r*r for r in radii]
    c0=5.;h0=0.9;b0=1.7
    for i,r in enumerate(radii):
        fp=np.prod([roots[i]-roots[j] for j in range(len(roots)) if j!=i])
        for e in [-0.5,0,0.2]:
            numeric=2*fp*r*quad(lambda th:(e*np.cos(th)+b0*np.sin(th))/(c0+h0*r*np.cos(th)),0,2*pi,epsabs=1e-13)[0]
            closed=(4*pi*e*fp/h0)*(1-c0/sqrt(c0*c0-h0*h0*r*r))
            assert abs(numeric-closed)<2e-11,(r,e,numeric,closed)

# Integrate original planar flow and its variational matrix over one exact orbit period.
for ri in [1.,2.]:
    e0=0.25; b0=1.3; c0=5.; h0=0.8
    def rhs(t,z):
        X,Y=z[:2]; S=X*X+Y*Y; FF=(S-1)*(S-4); FP=2*S-5; CC=c0+h0*X
        vel=np.array([e0*FF+CC*Y,b0*FF-CC*X]);
        A=np.array([[2*e0*X*FP+h0*Y,2*e0*Y*FP+CC],
                    [2*b0*X*FP-CC-h0*X,2*b0*Y*FP]])
        return np.r_[vel,(A@z[2:].reshape(2,2)).ravel()]
    period=2*pi/sqrt(c0*c0-h0*h0*ri*ri)
    z0=np.r_[ri,0.,np.eye(2).ravel()]
    sol=solve_ivp(rhs,(0.,period),z0,rtol=5e-12,atol=5e-13,method='DOP853')
    assert sol.success
    assert np.linalg.norm(sol.y[:2,-1]-z0[:2])<3e-9
    eig=np.sort(np.linalg.eigvals(sol.y[2:,-1].reshape(2,2)).real)
    fp=-3 if ri==1 else 3
    L=4*pi*e0*fp/h0*(1-c0/sqrt(c0*c0-h0*h0*ri*ri))
    expect=np.sort([1.,exp(L)])
    assert np.max(abs(eig-expect))<3e-8,(ri,eig,expect)

# Verify near-circle neutral first return: all nearby levels are periodic to numerical precision.
for radius0 in [0.97, 1.04, 1.96, 2.03]:
    b0=1.0;c0=5.0;h0=0.8
    def rad_theta(theta, yvec):
        S=float(yvec[0]);R=sqrt(S); F0=(S-1)*(S-4)
        YY=R*np.sin(theta);XX=R*np.cos(theta)
        omega=-(c0+h0*XX)+b0*F0*np.cos(theta)/R
        return [2*b0*YY*F0/omega]
    sol=solve_ivp(rad_theta,[0.,-2*pi],[radius0**2],method='DOP853',rtol=1e-12,atol=1e-13)
    assert sol.success and abs(sol.y[0,-1]-radius0**2)<1e-9,(radius0,sol.y[0,-1])
print('VERIFY_OK symbolic_radial=1 symbolic_neutral_integral=1 symbolic_jacobian=2 exact_floquet_cases=27 full_monodromy_cases=2 neutral_closed_orbits=4')
