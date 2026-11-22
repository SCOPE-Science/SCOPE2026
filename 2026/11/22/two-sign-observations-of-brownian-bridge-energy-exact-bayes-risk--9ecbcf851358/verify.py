"""Standalone verification of the Brownian-bridge two-sign quadratic-energy identities.

Run with Python 3.10+, sympy and mpmath. These checks supplement the proof in RESULT.md.
"""
import sympy as sp
import mpmath as mp

s, t, u, r, A, B, C = sp.symbols('s t u r A B C', real=True)

# Exact integration of the squared bridge Green kernel for 0 < s < t < 1.
I = (sp.integrate((u * (1 - s)) * (u * (1 - t)), (u, 0, s))
    + sp.integrate((s * (1 - u)) * (u * (1 - t)), (u, s, t))
    + sp.integrate((s * (1 - u)) * (t * (1 - u)), (u, t, 1)))
assert sp.simplify(I - s * (1-t) * (2*t-t*t-s*s) / 6) == 0
I_ss = sp.factor(I.subs(t,s))
assert sp.simplify(I_ss - s*s*(1-s)**2/3) == 0

# Wick's identity: variance of the integral of squared bridge values.
v = sp.symbols('v', real=True)
varQ = 4*sp.integrate(sp.integrate((u*(1-v))**2,(u,0,v)),(v,0,1))
assert sp.simplify(varQ-sp.Rational(1,45)) == 0

# Exact matrix reduction of the Gaussian sign second moments.
Sigma = sp.Matrix([[1,r],[r,1]])
M = sp.Matrix([[A,C],[C,B]])
T = sp.Matrix([[r,1],[1,r]])
assert sp.simplify(sp.trace(Sigma.inv()*M*Sigma.inv()*T) - (2*C-r*(A+B))/(1-r*r)) == 0

# Bridge-specific kernel collapse, before substituting the correlation value.
A_b = s*(1-s)/3
B_b = t*(1-t)/3
C_b = r*(2*t-t*t-s*s)/6
assert sp.simplify(2*C_b-r*(A_b+B_b)-r*(t-s)/3) == 0
assert sp.simplify((t-s)*s*(1-t)/(t*(1-s)) - (s*(1-t)/(t*(1-s)))*(t-s)) == 0

# Fixed-correlation geometry: with z=ac and b=kz, the AM-GM feasibility
# boundary is strictly decreasing on 0<z<1/k.
z,k = sp.symbols('z k', positive=True)
obstacle=(1-k*z)**2/4-z
assert sp.simplify(sp.diff(obstacle,z)+1+k*(1-k*z)/2) == 0
rho = sp.symbols('rho', positive=True)
a_ref = rho/(1+rho)
b_ref = (1-rho)/(1+rho)
assert sp.simplify(a_ref*2 + b_ref -1) == 0
assert sp.simplify(a_ref*a_ref/(a_ref*a_ref+b_ref)-rho*rho) == 0

# Monotonicity of the scalar numerator up to the trisection correlation.
q = rho**2*(1-rho)/(1+rho)**3
assert sp.simplify(sp.diff(q,rho)/q - 2*(1-2*rho)/(rho*(1-rho*rho))) == 0

# Direct one-dimensional conditional-normal integrals independently check
# the folded Gaussian moment identities used in the proof.
mp.mp.dps=35
phi=lambda x: mp.exp(-x*x/2)/mp.sqrt(2*mp.pi)
Phi=lambda x: (1+mp.erf(x/mp.sqrt(2)))/2
for rv in ['0.15','0.36','0.57','0.81']:
    rr=mp.mpf(rv);sig=mp.sqrt(1-rr*rr)
    condsign=lambda x: 2*Phi(rr*x/sig)-1
    observed_u2=2*mp.quad(lambda x: (x*x-1)*phi(x)*condsign(x),[0,1,3,mp.inf])
    wanted_u2=2*rr*sig/mp.pi
    assert abs(observed_u2-wanted_u2)<mp.mpf('1e-27')
    condabs=lambda x: sig*mp.sqrt(2/mp.pi)*mp.exp(-(rr*x/sig)**2/2) + rr*x*condsign(x)
    Eabs=2*mp.quad(lambda x: x*phi(x)*condabs(x),[0,1,3,mp.inf])
    observed_uv=Eabs-rr*2*mp.asin(rr)/mp.pi
    wanted_uv=2*sig/mp.pi
    assert abs(observed_uv-wanted_uv)<mp.mpf('1e-27')

# The risk formula and independent-moment calculation agree at distinct sites.
for sv,tv in [('.2','.55'),('0.333333333333333333333333333333','.666666666666666666666666666667'),('.36','.64'),('.27','.71')]:
    ss=mp.mpf(sv);tt=mp.mpf(tv)
    rr=mp.sqrt(ss*(1-tt)/(tt*(1-ss)))
    mat=mp.matrix([[1,rr],[rr,1]])
    mm=mp.matrix([[ss*(1-ss)/3,rr*(2*tt-tt*tt-ss*ss)/6],
                  [rr*(2*tt-tt*tt-ss*ss)/6,tt*(1-tt)/3]])
    ttmat=2*mp.sqrt(1-rr*rr)/mp.pi*mp.matrix([[rr,1],[1,rr]])
    calc=mp.trace(mat**-1*mm*mat**-1*ttmat) if hasattr(mp,'trace') else sum((mat**-1*mm*mat**-1*ttmat)[i,i] for i in range(2))
    target=2*mp.sqrt(ss*(tt-ss)*(1-tt))/(3*mp.pi)
    assert abs(calc-target)<mp.mpf('1e-28')

fraction=lambda x: 20/mp.pi**2 * (x*x*(1-x)/(1+x)**3)/(1-(2*mp.asin(x)/mp.pi)**2)
assert abs(fraction(mp.mpf('.5'))-5/(6*mp.pi**2)) < mp.mpf('1e-30')

# Non-proof optimization diagnostic: a stationary point is near 0.567.
stationary=mp.findroot(lambda x: mp.diff(fraction,x), (mp.mpf('.55'),mp.mpf('.59')))
assert mp.mpf('.566')<stationary<mp.mpf('.568')
assert fraction(stationary)>fraction(mp.mpf('.5'))
print('PASS: symbolic Green-kernel and covariance identities, 8 Gaussian integrals, 4 exact-risk comparisons')
print('PASS: fixed-correlation reflection identity and rational-trisection benchmark')
print('Illustrative stationary point (uniqueness not certified):',mp.nstr(stationary,20))
print('Illustrative explained fraction:',mp.nstr(fraction(stationary),20))
