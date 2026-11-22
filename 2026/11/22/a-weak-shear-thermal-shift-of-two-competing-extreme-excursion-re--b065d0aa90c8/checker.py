"""Independent reproducibility checks for a two-age transition in reset shear diffusion.

Run: python checker.py
Requires scipy, sympy, numpy. Scientific input is the stationary Gaussian
propagator of two-dimensional Brownian motion in a linear shear flow.
"""
import math
import numpy as np
import sympy as sp
from scipy.optimize import root, root_scalar
from scipy.integrate import quad

s, q, eps = sp.symbols('s q eps', positive=True)
F_inf = s + q**2/s - 3*q/s**2 + 3/s**3
F_eps = s + (1-s*q+s*s*q*q/3+eps*q*q)/(s*(s*s/3+4*eps))
assert sp.simplify((F_eps-F_inf)+9*eps*(q*s-2)**2/(s**3*(s*s+12*eps))) == 0
assert sp.simplify(s**4*sp.diff(F_inf,s) + (q*s-s*s-3)*(q*s+s*s-3)) == 0
H = sp.simplify(sp.diff(F_eps,eps).subs(eps,0))
assert sp.simplify(H+9*(q*s-2)**2/s**5)==0
assert sp.simplify(F_inf.subs(q,0)-s-3/s**3)==0
F = sp.lambdify((s,q,eps),F_eps,'numpy')
Fs = sp.lambdify((s,q,eps),sp.diff(F_eps,s),'numpy')
Fss = sp.lambdify((s,q,eps),sp.diff(F_eps,s,2),'numpy')

def base(q0):
    a = (math.sqrt(q0*q0+12)-q0)/2
    b = (q0+math.sqrt(q0*q0-12))/2
    return a,b

def diff(q0):
    a,b=base(q0)
    return F(a,q0,0)-F(b,q0,0)
qc=root_scalar(diff,bracket=(2*math.sqrt(3)+1e-6,4.3),xtol=1e-14).root
a0,b0=base(qc)
assert 3.72<qc<3.73 and a0<1<b0 and abs(diff(qc))<1e-12
Dprime=3/a0**2-3/b0**2-4
Hf=sp.lambdify((s,q),H,'numpy')
coeff=-(Hf(a0,qc)-Hf(b0,qc))/Dprime
print('critical limiting q, age minima, correction',qc,a0,b0,coeff)
assert Dprime>0 and coeff>0

# Solve equal global branch costs and both stationarity equations.
sols=[]
for strength in [15, 25, 40, 60, 100]:
    ee=1./strength**2
    def eq(v):
        aa,bb,qq=v
        return [Fs(aa,qq,ee),Fs(bb,qq,ee),F(aa,qq,ee)-F(bb,qq,ee)]
    res=root(eq,[a0,b0,qc+coeff*ee],tol=1e-12)
    assert res.success or max(abs(z) for z in eq(res.x))<1e-9
    aa,bb,qq=res.x
    assert max(abs(z) for z in eq(res.x))<1e-8
    assert 0<aa<bb and Fss(aa,qq,ee)>0 and Fss(bb,qq,ee)>0
    # Verify these are the only global wells: dense independent grid scan
    grid=np.geomspace(0.13,7.0,15000)
    vals=F(grid,qq,ee)
    assert np.min(vals)>=F(aa,qq,ee)-1e-4
    for qq1 in [qq-.007, qq+.007]:
        wa=root_scalar(lambda t: Fs(t,qq1,ee),x0=aa,x1=aa+.002).root
        wb=root_scalar(lambda t: Fs(t,qq1,ee),x0=bb,x1=bb+.002).root
        assert (F(wa,qq1,ee)<F(wb,qq1,ee)) == (qq1<qq)
    sols.append((strength,aa,bb,qq))
    print('eta, coexisting ages, critical q, asymptotic scaled correction',strength,aa,bb,qq,(qq-qc)*strength**2)
assert abs(sols[-1][-1]-qc-coeff/10000)<.00005

# Independent Gaussian kernel/age-Laplace identity at several scales.
# Dimensionless r=D=1, shear gamma=eta/sqrt(R), endpoint (eta*sqrt(R),q*sqrt(R)).
for eta in (15.,40.):
  ee=1/eta**2
  _,aa,bb,qq=min(sols,key=lambda x:abs(x[0]-eta)) if eta==15 else sols[2]
  for R in (4.,16.,100.):
    for st in (aa,bb,1.3,3.1):
      t=st*math.sqrt(R)
      gamma=eta/math.sqrt(R)
      xx=eta*math.sqrt(R); yy=qq*math.sqrt(R)
      cov=np.array([[2*t+2*gamma**2*t**3/3,gamma*t*t],[gamma*t*t,2*t]])
      gaussian_exponent=np.array([xx,yy])@np.linalg.solve(cov,[xx,yy])/2
      assert abs(gaussian_exponent+t-math.sqrt(R)*F(st,qq,ee))<1e-9
print('PASS: symbolic limiting identities, coexisting minima, sided crossing, independent covariance exponent')

# Verify sharp two-saddle Laplace asymptotics by quadrature independent of the
# stationary equations. The integrals factor out the rare-event exponential.
for eta,aa,bb,qq in (sols[1], sols[3]):
    ee=1/eta**2
    im=F(aa,qq,ee)
    def weight(z):return 1./(z*math.sqrt(1+eta*eta*z*z/12))
    predicted=math.sqrt(2*math.pi)*(weight(aa)/math.sqrt(Fss(aa,qq,ee))+
              weight(bb)/math.sqrt(Fss(bb,qq,ee)))
    for R in (10000.,40000.,160000.):
        z=math.sqrt(R)
        integrand=lambda v:weight(v)*math.exp(-z*(F(v,qq,ee)-im))
        # The saddle tail outside [0.2,5] is exponentially negligible here.
        left=quad(integrand,.2,(aa+bb)/2,epsabs=1e-12,limit=180)[0]
        right=quad(integrand,(aa+bb)/2,5.,epsabs=1e-12,limit=180)[0]
        scaled=(left+right)*math.sqrt(z)
        assert abs(scaled/predicted-1)<.08,(eta,R,scaled,predicted)
    print('PASS: exact density quadrature at eta',eta,'scaled two-peak coefficient',predicted)
print('PASS: full independent quadrature and branch asymptotics')
