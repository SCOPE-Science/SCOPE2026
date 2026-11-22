"""Reproduce the finite-noise Brownian-local-time quadrature risk and high-noise timing checks.
Only supplementary numerical verification; proofs appear in RESULT.md.
"""
import math


def ak(k, t):
    # Numerically stable positive representation, including near t=1.
    a = k - 0.5
    return t ** (k + .5) / (k + .5) + t ** (k+.5) * (-math.expm1(a * math.log(t))) / a if t>0 else 0.0


def akprime(k,t):
    if t == 0.0: return 0.0
    a=k-.5
    return 2*k*t**(k-.5)*(-math.expm1(a*math.log(t)))/a


def explained(t,eta,K=200):
    if not (eta>0 and 0<=t<=1):raise ValueError('eta>0, 0<=t<=1 required')
    if t == 0: return 0.0
    acc=0.
    coeff=1.
    for k in range(1,K+1):
        coeff *= (2*k-1)/(2*k)
        v=ak(k,t)/(eta+t)**k
        term=coeff*v*v
        acc+=term
        if k>12 and term<1e-18*max(1.,acc):break
    return acc/(2*math.pi)


def derivative(t,eta,K=200):
    if t<=0 or t>1:raise ValueError
    v=eta+t
    coeff=1.; acc=0.
    for k in range(1,K+1):
        coeff *= (2*k-1)/(2*k)
        a=ak(k,t);ap=akprime(k,t)
        term = coeff*2*a*(ap-k*a/v)/(v**(2*k))
        acc+=term
        if k>12 and abs(term)<1e-17*max(1.,abs(acc)):break
    return acc/(2*math.pi)


def optimize(eta):
    lo,hi=0.05,1.
    for _ in range(100):
        mid=(lo+hi)/2
        if derivative(mid,eta)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def midpoint_integral(t,eta,n=250):
    # Two-dimensional Riemann integration in transformed sqrt time coordinates.
    v=t+eta
    arr=[]
    for i in range(n):
        u=(i+.5)/n
        arr.append(min(u,t/u))
    total=0.
    for f in arr:
        for g in arr:
            r=f*g/v
            total += 1/math.sqrt(1-r*r)-1
    return 2/math.pi*total/(n*n)


def test():
    cases = [(.2,.1),(.5,.2),(.7,1.),(.9,3.),(.98,10.)]
    for t,eta in cases:
        a=explained(t,eta)
        b=midpoint_integral(t,eta)
        assert abs(a-b)<5e-5,(t,eta,a,b)
        eps=1e-5
        d=(explained(t+eps,eta)-explained(t-eps,eta))/(2*eps)
        assert abs(d-derivative(t,eta))<2e-9,(t,eta,d,derivative(t,eta))
    # Integral of the covariance kernel against s^-k-1/2 compared with a closed expression.
    for k in range(1,9):
        for t in [.2,.65,.99]:
            assert ak(k,t)>0
            closed=2*k*t**(k+.5)/(k*k-.25)-t**(2*k)/(k-.5)
            assert abs(ak(k,t)-closed)<2e-12
    for eta in [1,3,10,30,100,1000]:
        t=optimize(eta)
        assert .5<t<1
        if eta>=30:
            approx=1-1/(3*eta)+11/(36*eta*eta)
            assert abs(t-approx)<.7/eta**3,(eta,t,approx)
        if eta>=100:
            lead=1/(9*math.pi*eta**2)-2/(9*math.pi*eta**3)
            assert abs(explained(t,eta)-lead)<2/eta**4,(eta,t)
        print(f'eta={eta:5}  t_opt={t:.12f}  eta*(1-t)={eta*(1-t):.9f}  info={explained(t,eta):.12g}')
    print('All independent integral, derivative, closed-form and asymptotic checks passed.')

if __name__ == '__main__':test()
