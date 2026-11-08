#!/usr/bin/env python3
"""Independent finite-state checks of a two-location first-passage local-time law.

Standard library only. The continuum proof is in RESULT.md; finite-lattice
convergence checks are not used as a proof of its infinite-dimensional claim.
"""
import math


def continuum(D, rate, a, b, s, t):
    k = math.sqrt(rate / D)
    ua = math.sinh(k * a) / (D * k)
    ub = math.sinh(k * b) / (D * k)
    eta = math.sinh(k * (b - a)) / math.sinh(k * b)
    return 1.0 / (1.0 + ua*s + ub*t + eta*ua*ub*s*t)


def solve_tridiagonal(lower, diag, upper, rhs):
    """Thomas elimination, no dense matrix inversion or stochastic simulation."""
    n = len(diag)
    d = diag.copy()
    v = rhs.copy()
    for i in range(1, n):
        fac = lower[i-1] / d[i-1]
        d[i] -= fac*upper[i-1]
        v[i] -= fac*v[i-1]
    x = [0.0] * n
    x[-1] = v[-1] / d[-1]
    for i in range(n-2, -1, -1):
        x[i] = (v[i] - upper[i]*x[i+1])/d[i]
    return x


def lattice_laplace(D, rate, R, a, b, s, t, h, xmax=15.0):
    """Solve a finite birth-death/reset Feynman-Kac boundary value problem.

    States are j*h, j=1,...,N; 0 is absorbing, N*h is reflecting.
    Jump rates D/h**2 in each available direction, reset rate 'rate'.
    Local-time proxies are occupation times at a and b divided by h.
    """
    N = round(xmax / h)
    iR, ia, ib = (round(x/h) for x in (R, a, b))
    assert all(abs(round(x/h)*h-x)<1e-9 for x in (R,a,b,xmax))
    assert 0 < ia < ib <= iR < N
    diffusion = D / (h*h)
    diagonal = [(2.0 if j<N else 1.0)*diffusion+rate+
                (s/h if j==ia else 0.0)+(t/h if j==ib else 0.0)
                for j in range(1, N+1)]
    side = [-diffusion]*(N-1)
    rhs_boundary = [diffusion] + [0.0]*(N-1)
    rhs_reset = [rate]*N
    v = solve_tridiagonal(side, diagonal, side, rhs_boundary)
    u = solve_tridiagonal(side, diagonal, side, rhs_reset)
    return v[iR-1]/(1.0-u[iR-1])


def check():
    checks=0
    for D, rate, R, a, b in [(1.3, .8, 2.4, .8, 1.6),
                              (.7, 2.4, 2.4, .8, 1.6),
                              (1.5, .4, 2.4, .8, 1.6)]:
        k=math.sqrt(rate/D)
        ua=math.sinh(k*a)/(D*k)
        ub=math.sinh(k*b)/(D*k)
        eta=math.sinh(k*(b-a))/math.sinh(k*b)
        assert 0.0 < eta < 1.0
        # Exact resolvent entries and exact two-point Kac determinant.
        q=math.exp(-k*R)
        def G(x,y):
            return (math.exp(-k*abs(x-y))-math.exp(-k*(x+y)))/(2*D*k)
        def U(x,y):
            return G(x,y)+(1-math.exp(-k*x))*G(R,y)/q
        for x,y,z in [(R,a,ua),(R,b,ub),(a,a,ua),(b,b,ub),(b,a,ua),(a,b,(1-eta)*ub)]:
            assert abs(U(x,y)/z-1.0)<3e-12
            checks+=1
        for s,t in [(.3,.6),(1.7,.4),(.2,2.2)]:
            det=(1+s*U(a,a))*(1+t*U(b,b))-s*t*U(a,b)*U(b,a)
            # F_R derived from the two-point resolvent gauge equations.
            Fa=(1+t*U(b,b)-t*U(a,b))/det
            Fb=(1+s*U(a,a)-s*U(b,a))/det
            fR=1-s*U(R,a)*Fa-t*U(R,b)*Fb
            pred=continuum(D,rate,a,b,s,t)
            assert abs(fR-pred)<2e-12, (fR,pred)
            checks+=1
        # Compare an independently discretized Markov-generator equation.
        s,t=.4,.7
        exact=continuum(D,rate,a,b,s,t)
        errors=[]
        for h in (.2,.1,.05):
            value=lattice_laplace(D,rate,R,a,b,s,t,h)
            err=abs(value-exact)
            errors.append(err)
            checks+=1
        assert errors[2]<1.5e-3, errors
        assert errors[1]<errors[0] and errors[2]<errors[1],errors
    for a,b in [(.25,.75),(.8,1.6),(1.7,2.3)]:
        last=a/b
        for j in range(1,151):
            k=j*.04
            correlation=1-math.sinh(k*(b-a))/math.sinh(k*b)
            assert correlation>last-1e-13,(a,b,k,correlation,last)
            last=correlation
            checks+=1
        assert last> a/b
    # Zero-rate and high-rate limits; distinct detector locations fixed.
    a,b=.8,1.6
    for k in [1e-4,1e-5]:
        corr=1-math.sinh(k*(b-a))/math.sinh(k*b)
        assert abs(corr-a/b)<2e-8
        checks+=1
    for k in [25.,30.]:
        eta=math.sinh(k*(b-a))/math.sinh(k*b)
        assert abs(eta/math.exp(-k*a)-1)<1e-10
        checks+=1
    print(f'PASS: {checks} identities, finite-state comparisons and monotonicity/limit tests')


if __name__=='__main__':
    check()
