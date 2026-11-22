"""Exact and numerical checks for periodically forced two-species patch occupancy."""
from fractions import Fraction as F
import numpy as np
from scipy.integrate import solve_ivp
import sympy as s

K=F(1,2); ell=F(1,2); b0=F(3,10); mu=F(9,100); om=F(1,10)
gamma=K*b0-mu
m0=K-mu/b0
assert gamma==F(3,50) and m0==F(1,5)
assert mu==K*b0*b0/ell
u_cos=s.simplify(m0*(mu/b0)*gamma/(gamma**2+om**2))
u_sin=s.simplify(m0*(mu/b0)*om/(gamma**2+om**2))
assert u_cos==s.Rational(9,34) and u_sin==s.Rational(15,34)
v_mean=-u_cos/(2*b0)
c_epsilon=s.simplify(-ell*v_mean)
c_eta=s.simplify(c_epsilon/s.Integer(25))
assert c_eta==s.Rational(3,340)
print('exact quadratic coefficient',c_eta)

kf=.5; lf=.5; bf=.3; muf=.09; omega=.1; period=2*np.pi/omega
for eta in [0.08,0.10]:
    def b(t): return bf + eta/5*np.cos(omega*t)
    # Poincare map for linear Z equation: z' = mu-(K*b-mu)*z
    def rhs(t,y): return [muf-(kf*b(t)-muf)*y[0]]
    sol0=solve_ivp(rhs,[0,period],[0.],rtol=3e-12,atol=1e-13)
    sol1=solve_ivp(rhs,[0,period],[1.],rtol=3e-12,atol=1e-13)
    q=sol1.y[0,-1]-sol0.y[0,-1]
    z0=sol0.y[0,-1]/(1-q)
    sol=solve_ivp(rhs,[0,period],[z0],rtol=2e-12,atol=2e-13,dense_output=True)
    ts=np.linspace(0,period,25001)
    z=sol.sol(ts)[0]
    M=kf/(1+z)
    Y=kf-M
    invY=np.trapezoid(1/Y,ts)/period
    avgY=np.trapezoid(Y,ts)/period
    lam=np.trapezoid(lf*Y-np.array([b(t) for t in ts])*M-muf,ts)/period
    lam_identity=lf*avgY-kf*bf
    lam_difference=lf*(avgY-1/invY)
    assert abs(muf*invY-bf)<1e-9
    assert abs(lam-lam_identity)<1e-9
    assert abs(lam-lam_difference)<1e-9
    assert lam>0
    def rhs_v(t, vv):
        mt=kf/(1+sol.sol(t)[0])
        at=lf*(kf-mt)-b(t)*mt-muf
        return [-at*vv[0]+lf]
    v0_sol=solve_ivp(rhs_v,[0,period],[0.],rtol=1e-11,atol=1e-12)
    v1_sol=solve_ivp(rhs_v,[0,period],[1.],rtol=1e-11,atol=1e-12)
    pv=v1_sol.y[0,-1]-v0_sol.y[0,-1]
    assert 0<pv<1
    vperiod=v0_sol.y[0,-1]/(1-pv)
    Lperiod=1/vperiod
    assert 0<Lperiod<kf-kf/(1+z0)
    print('positive coexistence L(0)',Lperiod)
    print('eta',eta,'periodic z closure',abs(z[-1]-z0),'Lambda',lam,'quadratic prediction',(3/340)*eta**2,'relative',lam/((3/340)*eta**2))
print('ALL_CHECKS_PASS')
