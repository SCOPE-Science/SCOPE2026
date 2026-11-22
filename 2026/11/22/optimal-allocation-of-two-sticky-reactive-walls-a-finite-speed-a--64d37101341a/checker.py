"""Deterministic cross-checks for two-endpoint sticky run-and-tumble capture."""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def explicit_mean(v, L, alpha, beta, x, k0, kL):
    A = 1 + alpha * L / v
    B = 1 + beta * L / v
    c = F(1, 2) + alpha * x / v
    return L / (2 * v) + alpha * x * (L - x) / v**2 + B * (
        2 * beta + c * k0 + (A - c) * kL
    ) / (A * k0 * kL + beta * (k0 + kL))


def backward_mean(v, L, alpha, beta, x, k0, kL):
    """Independent solve for the two unknown mean/heading constants."""
    # In the bulk m_-(x) = u + (alpha*d+1)*x/v-alpha*x*x/v/v,
    # and m_+(x) = m_-(x)+d-2*x/v.
    # Left boundary: k0*u - beta*d = 1.
    # Right boundary: kL*m_-(L) + (beta+kL)*(d-2L/v) = 1.
    c = kL * (L / v - alpha * L**2 / v**2) - 2 * (beta + kL) * L / v
    dcoeff = kL * alpha * L / v + (beta + kL)
    # Solve k0*u-beta*d=1, kL*u+dcoeff*d=1-c.
    determinant = k0 * dcoeff + beta * kL
    u = (dcoeff + beta * (1 - c)) / determinant
    d = (k0 * (1 - c) - kL) / determinant
    mm = u + (alpha*d + 1)*x/v - alpha*x*x/v**2
    mp = mm + d - 2*x/v
    assert k0*u-beta*d == 1 if isinstance(k0, F) else isclose(k0*u-beta*d,1,abs_tol=1e-6)
    assert isclose(float(kL*(u+(alpha*d+1)*L/v-alpha*L**2/v**2)+(beta+kL)*(d-2*L/v)),1,abs_tol=1e-6)
    return (mm+mp)/2


def optimal_imbalance(v, L, alpha, beta, x, K):
    A = 1+alpha*L/v
    h = alpha*(2*x-L)/(2*v)
    c = 2*beta+A*K/2
    d = beta*K+A*K*K/4
    b = A*c/2
    disc = b*b-A*h*h*d
    assert disc>0
    return -2*h*d/(b+sqrt(disc))


def golden_min(fun, left, right):
    g=(sqrt(5)-1)/2
    c=right-g*(right-left)
    d=left+g*(right-left)
    fc,fd=fun(c),fun(d)
    for _ in range(200):
        if fc<fd:
            right,d,fd=d,c,fc
            c=right-g*(right-left)
            fc=fun(c)
        else:
            left,c,fc=c,d,fd
            d=left+g*(right-left)
            fd=fun(d)
    return (left+right)/2


def run():
    rng=Random(20230202)
    counts={'exact_backward':0,'numeric_backward':0,'independent_optimizer':0,'budget_monotonicity':0,'limits':0}
    def frac():return F(rng.randint(1,12),rng.randint(1,12))
    for _ in range(600):
        v,L,alpha,beta,k0,kL=[frac() for i in range(6)]
        x=L*F(rng.randrange(0,11),10)
        m1=explicit_mean(v,L,alpha,beta,x,k0,kL)
        m2=backward_mean(v,L,alpha,beta,x,k0,kL)
        assert m1==m2,(m1,m2)
        counts['exact_backward']+=1
    for _ in range(300):
        v,L,alpha,beta,K=[10**rng.uniform(-1.5,1.5) for _ in range(5)]
        x=L*rng.random()
        k0=K*rng.uniform(.01,.99)
        assert isclose(float(explicit_mean(v,L,alpha,beta,x,k0,K-k0)),float(backward_mean(v,L,alpha,beta,x,k0,K-k0)),rel_tol=1e-10,abs_tol=1e-6)
        counts['numeric_backward']+=1
        delta=optimal_imbalance(v,L,alpha,beta,x,K)
        assert abs(delta)<K
        f=lambda t:float(explicit_mean(v,L,alpha,beta,x,K*(1+t)/2,K*(1-t)/2))
        minimizer=golden_min(f,-1,1)
        assert abs(minimizer-delta/K)<2e-6,(delta/K,minimizer)
        counts['independent_optimizer']+=1
    for _ in range(120):
        v,L,alpha,beta=[10**rng.uniform(-1,1) for _ in range(4)]
        x=L*rng.random()
        Kvals=[.01,.1,1,10,100]
        t=[optimal_imbalance(v,L,alpha,beta,x,K)/K for K in Kvals]
        if x<L/2:
            assert all(t[i]<t[i+1] for i in range(4))
        else:
            assert all(t[i]>t[i+1] for i in range(4))
        counts['budget_monotonicity']+=1
        A=1+alpha*L/v
        h=alpha*(2*x-L)/(2*v)
        tw=-h/A
        ts=-2*h/(A+sqrt(A*A-4*h*h))
        Ktiny=1e-9*beta/(1+A)
        Kbig=1e10*beta*(1+A)
        assert abs(optimal_imbalance(v,L,alpha,beta,x,Ktiny)/Ktiny-tw)<1e-5
        assert abs(optimal_imbalance(v,L,alpha,beta,x,Kbig)/Kbig-ts)<1e-6
        counts['limits']+=1
    print('PASS',counts,'total',sum(counts.values()))

if __name__=='__main__':run()
