"""Reproducibility checks for stationary intermittent Brownian/ballistic protocols.
No external network, files or special services are required. Needs sympy and numpy.
The universal statements are proved algebraically in RESULT.md, not by this grid.
"""
from math import exp, log, sqrt, gamma, isclose
import numpy as np
import sympy as sp

r, a, b, D, v, z = sp.symbols('r a b D v z', positive=True)
ell, S = r+b, r+a+b
Q = sp.expand((r+a+D*z)*(ell**2+v**2*z)-a*b*ell)
Q2=sp.expand((r+D*z)*(ell**2+v**2*z)+a*(r*ell+v**2*z))
F_D=r*(ell*S+v**2*z)/Q
F_B=r*ell*(S+D*z)/Q
checks=0

def check(statement, why):
    global checks
    if not statement:
        raise AssertionError(why)
    checks += 1

check(sp.simplify(Q-Q2)==0,'Fourier denominator')
check(sp.simplify(F_D-F_B-r*(v**2-D*ell)*z/Q)==0,'characteristic difference')
check(sp.simplify(Q.subs(z,0)-r*ell*S)==0,'positive constant term')
check(sp.simplify(Q.subs(z,-ell**2/v**2)+a*b*ell)==0,'spectral interlacing')
check(sp.simplify(Q.subs(z,-(r+a)/D)+a*b*ell)==0,'second interlacing')
check(sp.simplify(Q.subs(z,-ell*S/v**2)+a*ell*S*(v**2-D*ell)/v**2)==0,'diffusive numerator spectral sign')
check(sp.simplify(Q.subs(z,-S/D)-b*S*(v**2-D*ell)/D)==0,'ballistic numerator spectral sign')
check(sp.simplify((F_D-F_B).subs(v**2,D*ell))==0,'alias Fourier balance')
# substitution v^2 is a separate symbol, so rational expression is used here.
check(sp.simplify((F_D.subs(v**2,D*ell))-r/(r+D*z))==0,'diffusive pure Laplace')
check(sp.simplify((F_B.subs(v**2,D*ell))-r/(r+D*z))==0,'ballistic pure Laplace')
check(sp.simplify((-2*sp.diff(F_D-F_B,z)).subs(z,0)+2*(v**2-D*ell)/(ell*S))==0,'stationary variance order')

# Independent 3-by-3 stationary Markov Fourier solve; all numerical tests compare
# these linear equations with inverse-transform formulas, not just two formulas
# copied from the same source.
parameters=[
 (1.,2.,3.,2.,sqrt(8.)),  # exact alias r+b=4, v^2=8, D=2
 (0.2,1.4,1.1,1.,2.0), # diffusive better
 (1.9,0.8,1.4,2.1,1.), # ballistic better
 (0.8,2.4,0.4,0.3,1.),
 (4.2,0.4,0.5,1.6,2.5),
]
rng=np.random.default_rng(41051)
for _ in range(60):
 parameters.append(tuple(np.exp(rng.uniform(-1.7,1.7,5))))

for ri,ai,bi,Di,vi in parameters:
    elli=ri+bi; Si=ri+ai+bi; Delta=vi**2-Di*elli
    B=(ri+ai)/Di + elli**2/vi**2
    C=ri*elli*Si/(Di*vi**2)
    u,w=np.sort(np.roots([1.,-B,C]).real)
    lo,hi=np.sqrt(u),np.sqrt(w)
    check(0<u<w and lo<elli/vi<hi,'strict spectral roots')
    check(lo**2<(ri+ai)/Di,'secondary spectral bracket')
    tD=elli*Si/vi**2;tB=Si/Di
    check(tD>u and tB>u,'slow exponential coefficients positive')
    cD=ri/Di; cB=ri*elli/vi**2
    AD=cD*(tD-u)/(2*lo*(w-u)); BD=cD*(w-tD)/(2*hi*(w-u))
    AB=cB*(tB-u)/(2*lo*(w-u)); BB=cB*(w-tB)/(2*hi*(w-u))
    check(AD>0 and AB>0,'positive slow coefficients')
    if abs(Delta)>1.e-9:
        check(np.sign(BD)==np.sign(Delta),'diffusive log curvature sign')
        check(np.sign(BB)==-np.sign(Delta),'ballistic log curvature sign')
    check(isclose(2*(AD/lo+BD/hi),1.,rel_tol=1e-9,abs_tol=1e-9),'diffusive normalization')
    check(isclose(2*(AB/lo+BB/hi),1.,rel_tol=1e-9,abs_tol=1e-9),'ballistic normalization')
    K=ri*Delta/(2*Di*vi**2*(w-u))
    check(isclose(AD-AB,-K*lo,rel_tol=1e-8,abs_tol=1e-9),'slow difference')
    check(isclose(BD-BB,K*hi,rel_tol=1e-8,abs_tol=1e-9),'fast difference')
    check(isclose(hi*AB+lo*BB,cB*tB/(2*lo*hi),rel_tol=1e-8,abs_tol=1e-9),'Wronskian positivity')
    xcross=log(hi/lo)/(hi-lo)
    check(xcross>0,'unique density-crossing radius')
    for k in (0.0,0.5,2.,4.):
        A=np.array([[ri+ai+Di*k*k,-bi,-bi],[-ai/2,ri+bi+1j*k*vi,0],[-ai/2,0,ri+bi-1j*k*vi]],dtype=complex)
        for source,formula in (([ri,0,0], (ri*(elli*Si+vi**2*k*k))/(Di*vi**2*(k*k+u)*(k*k+w))),
                               ([0,ri/2,ri/2],(ri*elli*(Si+Di*k*k))/(Di*vi**2*(k*k+u)*(k*k+w)))):
            actual=sum(np.linalg.solve(A,np.array(source,dtype=complex)))
            check(abs(actual-formula)<2e-10,'independent Fourier matrix solve')
    if abs(Delta)>1e-9:
        theta_star=(vi**2-elli*Si/w)/Delta
        check(0<theta_star<1,'unique interior mixed-reset Laplace weight')
        aa=(1-theta_star)*AD+theta_star*AB
        bb=(1-theta_star)*BD+theta_star*BB
        check(abs(bb)<1e-8 and isclose(aa,lo/2.,rel_tol=1e-8,abs_tol=1e-8),'exact Laplace state from phase mixing')
    else:
        for theta in (0.,.3,.9,1.):
            check(abs((1-theta)*BD+theta*BB)<1e-8,'all mixed protocols pure Laplace at balanced rates')
    for th1,th2 in ((0.,.3),(.17,.82),(.5,1.),(0.,1.)):
        A1,B1=(1-th1)*AD+th1*AB,(1-th1)*BD+th1*BB
        A2,B2=(1-th2)*AD+th2*AB,(1-th2)*BD+th2*BB
        determinant=B1*A2-B2*A1
        if abs(Delta)>1e-9:
            check(np.sign(determinant)==np.sign(Delta),'whole mixture family has strict likelihood ratio order')
        for xx in (0.,.5,3.):
            p1=A1*exp(-lo*xx)+B1*exp(-hi*xx)
            p2=A2*exp(-lo*xx)+B2*exp(-hi*xx)
            check(p1>0 and p2>0,'mixed protocol densities are positive')
            check(isclose(p1-p2,(th2-th1)*K*(hi*exp(-hi*xx)-lo*exp(-lo*xx)),rel_tol=2e-8,abs_tol=1e-9),'mixed protocol common crossing')
    for x in (0.02,xcross*0.5,xcross,2*xcross,2.,6.):
        pd=AD*exp(-lo*x)+BD*exp(-hi*x)
        pb=AB*exp(-lo*x)+BB*exp(-hi*x)
        check(pd>0 and pb>0,'both densities positive')
        check(isclose(pd-pb,K*(hi*exp(-hi*x)-lo*exp(-lo*x)),rel_tol=2e-8,abs_tol=2e-9),'density difference')
        sd=2*(AD/lo*exp(-lo*x)+BD/hi*exp(-hi*x))
        sb=2*(AB/lo*exp(-lo*x)+BB/hi*exp(-hi*x))
        expected=ri*Delta/(Di*vi**2*(w-u))*(exp(-hi*x)-exp(-lo*x))
        check(isclose(sd-sb,expected,rel_tol=2e-8,abs_tol=2e-9),'survival difference')
        if abs(Delta)>1e-9:
            check(np.sign(sd-sb)==-np.sign(Delta),'strict radial stochastic ordering')
            # The derivative of the likelihood ratio has the sign of -Delta.
            dy=-(hi-lo)*exp(-(hi-lo)*x)
            numer=(BD*AB-BB*AD)*dy
            check(np.sign(numer)==-np.sign(Delta),'MLR direction')
            check(np.sign(AD*BD)==np.sign(Delta) and np.sign(AB*BB)==-np.sign(Delta),'opposite log curvature')
        else:
            check(abs(pd-pb)<1e-9,'balanced densities identical')
    for m in (1.,2.,3.,4.,5.5):
        momentdiff=2*gamma(m+1)*((AD-AB)/lo**(m+1)+(BD-BB)/hi**(m+1))
        rhs=ri*Delta/(Di*vi**2*(w-u))*gamma(m+1)*(hi**(-m)-lo**(-m))
        check(isclose(momentdiff,rhs,rel_tol=2e-8,abs_tol=1e-8),'positive real-order moment formula')
print(f'PASS: {checks} symbolic and independent numerical assertions')
