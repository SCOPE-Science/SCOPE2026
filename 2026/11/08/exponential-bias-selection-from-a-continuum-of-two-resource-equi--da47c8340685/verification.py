"""Numerical checks for the exact logit equilibrium identity and singular limit.

Run with Python 3.11 or later. Uses only the Python standard library.
The asymptotic theorem is proved analytically, not by these finite tests.
"""
from decimal import Decimal, localcontext
from math import exp

with localcontext() as ctx:
    ctx.prec = 120
    D = Decimal
    HALF = D('0.5')

    def log1pexp(z):
        return z + (1 + (-z).exp()).ln() if z > 0 else (1 + z.exp()).ln()

    def asinh(z):
        return (z + (z*z + 1).sqrt()).ln() if z >= 0 else -asinh(-z)

    def qclosed(s, d):
        if d < 0: return 1 - qclosed(s, -d)
        if d == 0: return HALF
        t = d/(2*s)
        sh = (t.exp() - (-t).exp())/2
        return HALF + d/4 - s/2*asinh((1/s).exp()*sh)

    def balance(y, s):
        return s*(log1pexp(-2*y/s) - log1pexp(-2*(1-y)/s))

    def qbisect(s, d):
        lo, hi = D(-2), D(3)
        for _ in range(440):
            mid = (lo + hi)/2
            if balance(mid,s) > d: lo = mid
            else: hi = mid
        return (lo + hi)/2 + d/2

    cases=0
    for s in map(D, ['0.8','0.3','0.1','0.07']):
        for d in map(D, ['-0.19','-0.003','0','0.003','0.19']):
            q=qclosed(s,d)
            assert D(0) < q < D(1)
            assert abs(q-qbisect(s,d)) < D('1e-85'), (s,d,q)
            assert abs(qclosed(s,-d)-(1-q)) < D('1e-85')
            cases+=1
    print(f'PASS: {cases} exact-root vs balance-bisection tests')

    # Separate quadrature directly evaluates the original integral at ordinary noise.
    def simpson_q(s,d,q,n=2000):
        s,d,q = float(s),float(d),float(q)
        def f(x):
            z=(2*(x-q)+d)/s
            if z > 0: return exp(-z)/(1+exp(-z))
            return 1/(1+exp(z))
        tot=f(0)+f(1)
        for j in range(1,n): tot+=(4 if j%2 else 2)*f(j/n)
        return tot/(3*n)
    quadratures=0
    for s in map(D, ['0.8','0.3','0.1']):
        for d in map(D, ['-0.19','0','0.19']):
            q=qclosed(s,d)
            assert abs(simpson_q(s,d,q)-float(q))<2e-9
            quadratures+=1
    print(f'PASS: {quadratures} direct logit-integral comparisons')

    # The finite probes below check rate and reflection; they are not a limit proof.
    limit_cases=0
    for alpha in map(D,['0.2','0.6','1.2']):
        for s in map(D,['0.04','0.02','0.01']):
            d=(-alpha/s).exp()
            q=qclosed(s,d)
            target=min(alpha/2,HALF)
            assert 0 < q < HALF
            if alpha <= 1:
                next_order=target+(s/2)*s.ln()+d/4
                assert abs(q-next_order) < D('0.0002'), (s,alpha,q,next_order)
            else:
                correction=(-((alpha-1)/s)).exp()/4
                assert abs((HALF-q)-correction) < D('0.0002')
            assert abs(qclosed(s,-d)-(1-q))<D('1e-85')
            limit_cases+=1
    print(f'PASS: {limit_cases} small-noise correction and reflection checks')
    print('ALL CHECKS PASS')
