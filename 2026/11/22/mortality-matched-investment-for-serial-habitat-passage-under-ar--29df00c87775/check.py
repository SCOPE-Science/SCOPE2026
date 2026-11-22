"""Independent finite checks for a two-stage passage and mortality model.
The analytic argument is in RESULT.md; these tests do not certify it.
Run: python check.py
"""
import math
import random
from scipy.integrate import quad
from scipy.optimize import minimize_scalar


def sinhc(z):
    if abs(z) < 1.e-4:
        return 1 + z*z/6 + z**4/120 + z**6/5040
    return math.sinh(z)/z


def weighted(u, C, d1, d2, weight, upper):
    v = C-u
    K = C+d1+d2
    delta = u-v+d1-d2
    def integrand(s):
        # Two nonnegative exponentials are evaluated separately for stability.
        if abs(delta*s) < 0.1:
            return s*math.exp(-K*s/2)*sinhc(delta*s/2)*weight(s)
        A = (K-abs(delta))/2
        B = (K+abs(delta))/2
        return (math.exp(-A*s)-math.exp(-B*s))/abs(delta)*weight(s)
    return u*v*quad(integrand,0,upper,epsabs=1.e-12,epsrel=1.e-11,limit=180)[0]


def deadline(u,C,d1,d2,T):
    return weighted(u,C,d1,d2,lambda s:1,T)


def independent_deadline(u,C,d1,d2,T):
    v=C-u
    # Integrate over time of first successful passage, and calculate the
    # second passage by a separate elementary exponential integration.
    def term(x):
        return u*v*math.exp(-(u+d1)*x)*(-math.expm1(-(v+d2)*(T-x)))/(v+d2)
    return quad(term,0,T,epsabs=1.e-12,epsrel=1.e-11)[0]


def optimize(C,d1,d2,T):
    return minimize_scalar(lambda x:-deadline(x,C,d1,d2,T),bounds=(0,C),method='bounded',options={'xatol':1e-11}).x


def infinite_optimum(C,d1,d2):
    return C/(1+math.sqrt(d2*(C+d1)/(d1*(C+d2))))


def infinite_value(u,C,d1,d2):
    v=C-u
    return u*v/((u+d1)*(v+d2))


def run():
    rng=random.Random(440023)
    n=0
    weights=[(lambda t:1.0,8), (lambda t:math.exp(-0.7*t),8),
             (lambda t:float(0.3<=t<=1.7),6)]
    for _ in range(270):
        C=10**rng.uniform(-1,0.8)
        d1=10**rng.uniform(-1,0.7)
        d2=10**rng.uniform(-1,0.7)
        if abs(d1-d2)<1e-7: continue
        x=rng.uniform(.05,.48)*C
        u1,u2=C/2+x,C/2-x
        for w,upper in weights:
            higher=weighted(u1,C,d1,d2,w,upper)
            lower=weighted(u2,C,d1,d2,w,upper)
            assert (higher-lower)*(d1-d2)>0, (C,d1,d2,x,higher,lower)
            n+=1
    for _ in range(180):
        C=10**rng.uniform(-1,.7)
        d1=10**rng.uniform(-1,.6)
        d2=10**rng.uniform(-1,.6)
        T=10**rng.uniform(-1,1)
        u=rng.uniform(.05,.95)*C
        x=deadline(u,C,d1,d2,T)
        y=independent_deadline(u,C,d1,d2,T)
        assert abs(x-y)<2e-9*max(x,y,1.e-9),(x,y)
        n+=1
    for _ in range(500):
        C=10**rng.uniform(-.6,.5)
        d=10**rng.uniform(-.4,.5)
        T=10**rng.uniform(-.5,.8)
        x=rng.uniform(.02,.46)*C
        assert deadline(C/2,C,d,d,T)>deadline(C/2-x,C,d,d,T)
        n+=1
    # Exact late-horizon algebra, and numerical finite-horizon approach.
    C,d1,d2=3,3,.2
    inf=infinite_optimum(C,d1,d2)
    assert abs(infinite_value(inf,C,d1,d2)-max(infinite_value(inf-1.e-3,C,d1,d2),infinite_value(inf+1.e-3,C,d1,d2)))>1.e-10
    for T in [0.02,0.04,0.08]:
        x=optimize(C,d1,d2,T)
        prediction=C/2+C*C*(d1-d2)*T*T/96
        assert abs(x-prediction)<.02*T*T, (T,x,prediction)
        n+=1
    x=optimize(C,d1,d2,60)
    assert abs(x-inf)<1e-4,(x,inf)
    n+=1
    T=2
    x=optimize(C,d1,d2,T)
    balance=deadline(C/2,C,d1,d2,T)
    opt=deadline(x,C,d1,d2,T)
    assert C/2<x<inf and opt>balance
    print(f'PASSED {n} independently checked cases')
    print('Witness C=3,d1=3,d2=.2,T=2:',f'u_T={x:.12f}',f'P_T={opt:.12f}',f'P_balanced={balance:.12f}',f'u_infty={inf:.12f}',f'gain={(opt/balance-1)*100:.6f}%')

if __name__=='__main__':run()
