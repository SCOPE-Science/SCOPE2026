"""Independent finite-time numerical checks for the fractional telegraph cumulant law.

Python 3 standard library only. This is a finite diagnostic, not a proof of
asymptotic exponents or strict inequalities for all times.
"""
import math


def rhs(n, rate, speed, t, y):
    f1, g1, f2, g2 = y
    w = speed * t ** (n - 1) / math.gamma(n)
    return (w * g1, w - 2 * rate * g1, w * g2, w * f1 - 2 * rate * g2)


def step(n, rate, speed, t, y, h):
    k1 = rhs(n, rate, speed, t, y)
    k2 = rhs(n, rate, speed, t + h / 2, [a + h*b/2 for a,b in zip(y,k1)])
    k3 = rhs(n, rate, speed, t + h / 2, [a + h*b/2 for a,b in zip(y,k2)])
    k4 = rhs(n, rate, speed, t + h, [a + h*b for a,b in zip(y,k3)])
    return [a + h*(b + 2*c + 2*d + e)/6 for a,b,c,d,e in zip(y,k1,k2,k3,k4)]


def moments(n, duration, rate=1., speed=1.):
    start = 1e-7
    z = speed * start ** n / math.gamma(n+1)
    # Zero-flip leading terms; initialization error is of relative order rate*start.
    y = [z*z/2, z, z**4/24, z**3/6]
    t = start
    while t < duration:
        h = min(0.012, .03*t, duration-t)
        y = step(n, rate, speed, t, y, h)
        t += h
    f1,g1,f2,g2 = y
    return 2*f1, 24*f2-12*f1*f1


def exact_n1(t, rate=1., speed=1.):
    e = math.exp(-2*rate*t)
    variance = speed**2*(t/rate-(1-e)/(2*rate**2))
    fourth = speed**4*( (60-48*e-12*e*e)/(16*rate**4)
                           - t*(24+48*e)/(8*rate**3))
    return variance, fourth


def close(a,b,rtol):
    assert abs(a-b) <= rtol*max(abs(a),abs(b),1e-10), (a,b,rtol)


def run():
    checked=0
    for n in (.35,.5,.65,.75,.9,1.,1.5,2.):
        prior=0.
        for t in (1.,5.,20.,90.):
            variance, fourth = moments(n,t)
            assert variance>0 and fourth<0,(n,t,variance,fourth)
            assert fourth<prior,(n,t,prior,fourth)
            assert -2 < fourth / variance**2 < 0,(n,t)
            prior=fourth
            checked+=4
    for rate,speed in ((1.,1.),(.7,2.),(2.,.6)):
        for t in (2.,11.,45.):
            observed=moments(1.,t,rate,speed)
            exact=exact_n1(t,rate,speed)
            close(observed[0],exact[0],3e-5)
            close(observed[1],exact[1],8e-5)
            checked+=2
    for n,t in ((1.,160.),(1.5,160.),(2.,160.)):
        var,fourth=moments(n,t)
        leading=-3/(math.gamma(n)**4*(4*n-3))*t**(4*n-3)
        assert abs(fourth/leading-1)<.04,(n,fourth,leading)
        leading_variance=t**(2*n-1)/(math.gamma(n)**2*(2*n-1))
        assert abs(var/leading_variance-1)<.04,(n,var,leading_variance)
        checked+=2
    # Critical logarithmic slope; additive constant cancels.
    a=moments(.75,100.)[1]
    b=moments(.75,400.)[1]
    slope=(b-a)/math.log(4.)
    close(slope,-3/math.gamma(.75)**4,.015)
    checked+=1
    # Finite fourth-cumulant limit for n < 3/4, with decreasing drift.
    for n in (.35,.5,.65):
        a=abs(moments(n,100.)[1]-moments(n,400.)[1])
        b=abs(moments(n,400.)[1]-moments(n,1200.)[1])
        assert b<a, (n,a,b)
        checked+=1
    print('PASS:',checked,'independent deterministic numerical assertions')

if __name__=='__main__':
    run()
