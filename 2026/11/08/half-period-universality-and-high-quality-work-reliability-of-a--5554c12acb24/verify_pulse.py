"""Independent numerical checks of a two-jump harmonic-trap work protocol.

Run: python verify_pulse.py
Dependencies: numpy, scipy, sympy.
The global assertions are analytic in RESULT.md; finite checks are diagnostics.
"""
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.linalg import expm
from scipy.special import ndtr, log_ndtr

checks=0

def check(expr, label):
    global checks
    if not bool(expr):
        raise AssertionError(label)
    checks+=1

m_s,k_s,alpha_s,omega_s,t_s=sp.symbols('m k alpha omega t', positive=True)
# The identity for a harmonic fundamental matrix at sin(omega*t)=0.
q_s=sp.symbols('q', positive=True)
A_s,f_s=sp.symbols('A f', real=True)
K_s=sp.symbols('K', positive=True)
w_s=k_s*A_s*(A_s+f_s/k_s)*K_s
check(sp.simplify(sp.diff(w_s,A_s).subs(A_s,-f_s/(2*k_s)))==0,'mean-optimal amplitude')
check(sp.simplify(sp.diff(w_s,A_s,2))==2*k_s*K_s,'strict convexity')
check(sp.simplify(w_s.subs(A_s,-f_s/(2*k_s)))==-f_s**2*K_s/(4*k_s),'quadratic minimum')

cases=[(1.,1.,.1,1.,1.3),(2.,3.,.5,.7,2.),(.7,1.3,.8,2.5,1.1),(1.,4.,3.5,1.,.9)]
for m,k,gamma,theta,f in cases:
    assert 0<gamma<2*math.sqrt(m*k)
    alpha=gamma/(2*m)
    omega=math.sqrt(k/m-alpha*alpha)
    tau=math.pi/omega
    q=math.exp(-alpha*tau)
    def gb(t):
        return (math.exp(-alpha*t)*(math.cos(omega*t)+alpha/omega*math.sin(omega*t)),
                math.exp(-alpha*t)*math.sin(omega*t)/omega)
    def var(t):
        g,b=gb(t)
        return theta/k*(1-g*g-k/m*b*b)
    for t in np.linspace(.05*tau,5*tau,30):
        g,b=gb(t)
        B=np.array([[0.,1.],[-k/m,-gamma/m]])
        U=expm(B*t)
        check(np.allclose(U[0],(g,b),rtol=1e-10,atol=1e-11),'propagator')
        noisevar=2*gamma*theta/(m*m)*quad(lambda s:gb(s)[1]**2,0,t,epsabs=1e-11)[0]
        check(np.isclose(noisevar,var(t),rtol=1e-8,atol=2e-12),'variance response')
        check(var(t)>0,'positive position variance')
    g,b=gb(tau)
    check(np.isclose(g,-q,atol=1e-12) and abs(b)<1e-12,'half-period map')
    check(np.isclose(var(tau),theta/k*(1-q*q),rtol=1e-10),'half-period variance')
    A=-f/(2*k)
    mean=k*A*(A+f/k)*(1-g)
    workvar=k*k*A*A*var(tau)
    check(np.isclose(mean,-f*f/(4*k)*(1+q),rtol=1e-12),'work mean')
    check(np.isclose(workvar,f*f*theta/(4*k)*(1-q*q),rtol=1e-12),'work variance')
    z=-mean/math.sqrt(workvar)
    check(np.isclose(z,(f/(2*math.sqrt(k*theta)))*math.sqrt((1+q)/(1-q)),rtol=1e-12),'success probability')
    # Strict monotonicity of normalized extraction signal up to first half period.
    tt=np.linspace(.004*tau,tau,700)
    K=np.array([1-gb(t)[0] for t in tt])
    V=np.array([var(t) for t in tt])
    scores=K/np.sqrt(V)
    check(np.all(np.diff(scores)>-1e-10),'pre-peak success monotonicity')
    post=np.linspace(tau+1e-3,7*tau,900)
    check(np.all(np.array([(1-gb(t)[0])/math.sqrt(var(t)) for t in post])<scores[-1]+1e-10),
          'post-peak success dominance')
    # Ideal minimum-work benchmark from Yao-Bao-Hou, Eq. (10), for lambda_i=lambda_f=q_i=0.
    ideal=-f*f*tau/(2*(2*gamma+k*tau))
    check(ideal<=mean+1e-11,'restricted value below ideal work')
    check(0<ndtr(z)<1,'Gaussian sign probability')

# Singular small-friction limit and the logarithmic failure exponent.
m=k=theta=f=1.
omega0=math.sqrt(k/m)
C=f*f*m*omega0/(2*math.pi*k*theta)
for gamma in [.08,.04,.02,.01,.005,.002]:
    alpha=gamma/(2*m);omega=math.sqrt(k/m-alpha*alpha)
    h=math.pi/omega;q=math.exp(-alpha*h)
    mean=-f*f/(4*k)*(1+q)
    optimal=-f*f*h/(2*(2*gamma+k*h))
    z=(f/(2*math.sqrt(k*theta)))*math.sqrt((1+q)/(1-q))
    fail_log=log_ndtr(-z)
    check(abs(mean/optimal-1)<gamma,'near-optimal mean high-Q')
    pulse_var=f*f*theta/(4*k)*(1-q*q)
    ideal_var=2*gamma*theta*f*f*h/(2*gamma+k*h)**2
    check(abs(pulse_var/ideal_var-math.pi**2/8)<5*gamma,'universal variance ratio high-Q')
    check(abs(gamma*fail_log+C)<2*gamma*abs(math.log(gamma)),'failure rate exponential constant')
    if gamma <=.02:
        asymp=(math.sqrt(k*theta*gamma/(2*m*omega0))/f)*math.exp(-C/gamma)
        true=math.exp(fail_log)
        check(abs(true/asymp-1)<.18,'Mills prefactor high-Q')

print('PASS',checks,'independent algebraic/numeric checks')
