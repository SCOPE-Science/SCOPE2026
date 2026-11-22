"""Independent analytic/numerical checks for a renewal-reset Brownian forcing theorem.
Run: python3 verification.py (requires scipy, numpy as listed in requirements.txt).
"""
import math
from scipy.integrate import quad
from scipy.special import erfc, gamma

D = 1.3
MU = 0.9
PASSED = 0


def check(cond, message):
    global PASSED
    if not cond:
        raise AssertionError(message)
    PASSED += 1


def h(t, d=D, mu=MU):
    if mu*t < 1.e-3:
        # Direct stable positive integral for the tiny-time regime.
        return 2*d*quad(lambda u: (-math.expm1(-mu*u))**2,0,t)[0]/mu**2
    return (d/mu**3)*(2*mu*t-3+4*math.exp(-mu*t)-math.exp(-2*mu*t))


def h_direct(t, d=D, mu=MU):
    return 2*d*quad(lambda u: (1-math.exp(-mu*u))**2,0,t,epsabs=1.e-12)[0]/mu**2


for t in [0.01,0.07,0.2,0.5,1,2,5,20,100]:
    check(math.isclose(h(t),h_direct(t),rel_tol=8.e-8,abs_tol=5.e-11), 'innovation variance')
    check(0<h(t)<2*D*t/MU**2,'variance positivity and bound')

# Renewal clocks: deterministic m, exponential m, gamma shape 2 m,
# and shifted two-point waiting times.
M=1.7
clocks=[
  ('periodic', lambda s:math.exp(-s*M), M*M,
   lambda t: 1.0 if t<M else 0.0),
  ('poisson',lambda s:1/(1+s*M),2*M*M,
   lambda t: math.exp(-t/M)),
  ('erlang2',lambda s:(1+s*M/2)**-2,1.5*M*M,
   lambda t: math.exp(-2*t/M)*(1+2*t/M)),
  ('two_point',lambda s:(math.exp(-s*M/2)+math.exp(-s*3*M/2))/2,1.25*M*M,
   lambda t: 1.0 if t<M/2 else (0.5 if t<1.5*M else 0.0)),
]


def predicted_variance(phi, second_moment, m=M):
    return D/(MU**2*m)*(second_moment-2*m/MU+2*(1-phi(MU))/MU**2)

for name,phi,et2,surv in clocks:
    # An independent stationary force-covariance route with explicit kernels.
    if name == 'periodic':
        c_force=lambda t:(D/M)*max(M-t,0)**2
        intervals=[(0,M)]
    elif name == 'two_point':
        c_force=lambda t:(D/(2*M))*(max(M/2-t,0)**2+max(3*M/2-t,0)**2)
        intervals=[(0,M/2),(M/2,3*M/2)]
    elif name == 'poisson':
        c_force=lambda t:2*D*M*math.exp(-t/M)
        intervals=[(0,60)]
    else:
        k=2/M
        c_force=lambda t:(2*D/(M*k*k))*math.exp(-k*t)*(3+k*t)
        intervals=[(0,60)]
    numeric=sum(quad(lambda t:math.exp(-MU*t)*c_force(t)/MU,l,r,epsabs=1e-12)[0] for l,r in intervals)
    exact=predicted_variance(phi,et2)
    check(math.isclose(numeric,exact,rel_tol=2.e-6,abs_tol=2.e-8), name+' covariance comparison')
    check(exact>0, name+' positive stationary variance')
    if name == 'periodic':
        e_h=h(M)
    elif name == 'two_point':
        e_h=(h(M/2)+h(3*M/2))/2
    elif name == 'poisson':
        e_h=quad(lambda t:h(t)*math.exp(-t/M)/M,0,70,epsabs=1e-10)[0]
    else:
        e_h=quad(lambda t:h(t)*(4*t/M**2)*math.exp(-2*t/M),0,70,epsabs=1e-10)[0]
    q_var=e_h/(1-phi(2*MU))
    age_damp=(1-phi(2*MU))/(2*MU*M)
    upper=2*M if name in ('periodic','two_point') else 70
    age_noise=quad(lambda t:surv(t)*h(t)/M,0,upper,epsabs=1e-9,limit=120)[0]
    check(math.isclose(q_var*age_damp+age_noise, exact, rel_tol=2e-7,abs_tol=1e-9),name+' independent embedded-affine check')

# Jensen optimization: all examples with equal mean lie strictly above deterministic.
min_var=predicted_variance(clocks[0][1],clocks[0][2])
for name,phi,et2,surv in clocks[1:]:
    check(predicted_variance(phi,et2)>min_var,name+' greater than periodic')

# Pareto survival (1+t/tau)^(-alpha), mean tau/(alpha-1).
# Direct stationary-age numerical mixture WITHOUT the previous-cycle X:
# mean-age tail integrated against erfc(x/sqrt(2h(a))).
def pareto_core_tail(alpha,tau,x):
    m=tau/(alpha-1)
    # Integrate in logarithmic time a=exp(y)-1 (prevents huge time cutoffs).
    def integrand(y):
        a=math.expm1(y)
        ha=h(a)
        if ha<=0:return 0.0
        return (1+a/tau)**(-alpha)*math.exp(y)*erfc(x/math.sqrt(2*ha))/m
    return quad(integrand,0,40,epsabs=1.e-12,epsrel=2.e-8,limit=250)[0]


def pareto_constant(alpha,tau):
    delta=alpha-1
    return (4*D*tau/MU**2)**delta*gamma(delta+0.5)/math.sqrt(math.pi)

for alpha in [1.5, 1.8, 2.5]:
    tau=1.2
    c=pareto_constant(alpha,tau)
    for x in [15,30,60,120,250]:
        ratio=pareto_core_tail(alpha,tau,x)*x**(2*(alpha-1))/c
        # convergence is not uniform; checks direction and approximate approach.
        check(0<ratio<1.035, f'Pareto core prefactor overshoot alpha={alpha},x={x}, ratio={ratio}')
    ratio=pareto_core_tail(alpha,tau,250)*250**(2*(alpha-1))/c
    check(ratio>0.95, f'Pareto core asymptotic, alpha={alpha}: ratio={ratio}')

# For Pareto alpha>2, finite variance from the stationary covariance identity.
for alpha in [2.3,2.8,4.0]:
    tau=1.2
    mean=tau/(alpha-1)
    et2=2*tau**2/((alpha-1)*(alpha-2))
    phi=quad(lambda t: math.exp(-MU*t)*alpha/tau*(1+t/tau)**(-alpha-1),0,500,epsabs=1e-10)[0]
    ans= D/(MU**2*mean)*(et2-2*mean/MU+2*(1-phi)/MU**2)
    check(ans>0, 'Pareto finite second moment')
    direct=(2*D/MU**2)*quad(lambda a: (1+a/tau)**(-alpha)*(a-2*(1-math.exp(-MU*a))/MU+(1-math.exp(-2*MU*a))/(2*MU)),0,math.inf,epsabs=5e-8,limit=250)[0]/mean
    eh=quad(lambda t:h(t)*alpha/tau*(1+t/tau)**(-alpha-1),0,math.inf,epsabs=5e-8,limit=250)[0]
    qv=eh/(1-quad(lambda t:math.exp(-2*MU*t)*alpha/tau*(1+t/tau)**(-alpha-1),0,500)[0])
    age_damp=(1-quad(lambda t:math.exp(-2*MU*t)*alpha/tau*(1+t/tau)**(-alpha-1),0,500)[0])/(2*MU*mean)
    check(math.isclose(direct+qv*age_damp,ans,rel_tol=1e-5,abs_tol=1e-7), 'Pareto independent affine stationary decomposition')

print(f'PASS {PASSED} deterministic consistency checks')
