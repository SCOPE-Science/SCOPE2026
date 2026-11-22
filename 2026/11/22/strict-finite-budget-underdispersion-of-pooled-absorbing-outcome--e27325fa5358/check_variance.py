#!/usr/bin/env python3
"""Independent finite-budget renewal-count moment tests.

Requires mpmath (and optionally sympy). Reconstructs moments via a two-state
Markov-additive tilted generator, not via the renewal-transform algebra.
"""
import mpmath as mp

mp.mp.dps = 45


def formulas(b, a, d, t):
    b,a,d,t=map(mp.mpf, (b,a,d,t))
    c=b*d+(1-b)*a
    L=a*d/c
    h=b*(1-b)*(a-d)
    u=-mp.expm1(-c*t)
    m=L*t+b*(1-b)*(a-d)**2/c**2*u
    q=b+h*u/(c*m)
    z=c*t
    # Compute the small-z sign factor using its convergent positive series.
    if z < mp.mpf('0.3'):
        negative=-2*z*mp.exp(-z)*mp.fsum((n-2)*z**(2*n)/mp.factorial(2*n) for n in range(3,42))
    else:
        negative=z*mp.exp(-z)*(4*(mp.cosh(z)-1)-z*mp.sinh(z)-z*z)
    J=h*h*L*L/(c**4*m*m)*negative
    exact=q*(1-q)*m+2*J
    return m,q,exact,2*J


def markov_moments(b, a, d, t, q):
    b,a,d,t,q=map(mp.mpf,(b,a,d,t,q))
    p0=1-b
    p1=b
    def mgf(s):
        # Each event at rate lambda_x is marked by the *departing* type x;
        # the next type is sampled afresh. Diagonal self-restarts are included.
        A=mp.matrix([
            [d*p0*mp.exp(-q*s)-d, d*p1*mp.exp(-q*s)],
            [a*p0*mp.exp((1-q)*s), a*p1*mp.exp((1-q)*s)-a],
        ])
        E=mp.expm(t*A)
        return p0*(E[0,0]+E[0,1])+p1*(E[1,0]+E[1,1])
    return mp.diff(mgf,0),mp.diff(mgf,0,2)


def near(x,y,tol='3e-25'):
    return abs(x-y) <= mp.mpf(tol)*(1+abs(y))


def run():
    checks=0
    cases=[
        ('0.25','6','1.2','1.333333333333333333333333'),
        ('0.5','6','1.2','2'),
        ('0.8','100','1','1.15'),
        ('0.45','2','1','4'),
        ('0.45','1','2','4'),
        ('0.1','1.2','1','0.1'),
        ('0.9','1','6','1'),
        ('0.25','3','1','1'),
        ('0.5','2','1','0.25'),
        ('0.2','3','2','3'),
    ]
    for b,a,d,t in cases:
        m,q,v,adjust=formulas(b,a,d,t)
        mean,second=markov_moments(b,a,d,t,q)
        assert near(mean,0),('mean',b,a,d,t,str(mean))
        assert near(second,v),('variance',b,a,d,t,str(second),str(v))
        checks+=2
        assert v > 0 and (v < q*(1-q)*m), ('underdispersion',b,a,d,t)
        checks+=1
    for b,a,d,t in [('0.3','1','1','0.1'),('0.3','1','1','10'),('0.3','6','6','1')]:
        m,q,v,adjust=formulas(b,a,d,t)
        assert near(adjust,0) and near(q,mp.mpf(b))
        checks+=2
    # The long-time absolute variance correction approaches -[b(1-b)(a-d)/c]^2.
    for b,a,d in [('0.25','6','1.2'),('0.5','3','1'),('0.9','4','1')]:
        b,a,d=map(mp.mpf,(b,a,d))
        c=b*d+(1-b)*a
        t=mp.mpf(60)/c
        _,_,_,adjust=formulas(b,a,d,t)
        expected=-(b*(1-b)*(a-d)/c)**2
        assert near(adjust,expected,'3e-2'),(str(adjust),str(expected))
        checks+=1
    # Series coefficients for the strict sign factor: 4(cosh z - 1)-z sinh z-z^2.
    for n in range(3,25):
        coeff=(mp.mpf(4)-2*n)/mp.factorial(2*n)
        assert coeff<0
        checks+=1
    print(f'PASS {checks} analytical/independent-generator tests')
    b,a,d,t=mp.mpf('.5'),mp.mpf(6),mp.mpf('1.2'),mp.mpf(2)
    m,q,v,adjust=formulas(b,a,d,t)
    print('sample m=',mp.nstr(m,16),'q=',mp.nstr(q,16))
    print('variance ratio=',mp.nstr(v/(q*(1-q)*m),16))
    return checks

if __name__=='__main__':
    run()
