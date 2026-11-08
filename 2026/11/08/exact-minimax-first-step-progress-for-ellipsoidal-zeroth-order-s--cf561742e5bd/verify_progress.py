"""Standalone deterministic numerical cross-checks for the two-dimensional POEM-ES first-step frontier.

Requires Python 3.9+ standard library only. These checks illustrate finite cases;
the exact formulas and asymptotic assertion have analytic proofs in RESULT.md.
"""
import math


def closed_progress(delta, q):
    assert 0 < delta < 1 and 0 <= q <= 1
    s = math.sqrt(max(0.0, 1-q*q))
    H = math.hypot(q, math.sqrt(delta)*s)
    cA = q/H
    sA = math.sqrt(delta)*s/H
    return (2.0/(math.pi*math.sqrt(1-delta))) * (
        math.sqrt(delta)*q*math.asinh(math.sqrt((1-delta)/delta)*cA)
        + s*math.asin(max(-1., min(1., math.sqrt(1-delta)*sA)))
    )


def angular_integral(delta, q, n=32000):
    s = math.sqrt(max(0.0, 1-q*q))
    alpha = math.atan2(math.sqrt(delta)*s, q)
    a = alpha-math.pi/2
    h = math.pi/n
    def integrand(t):
        ct = math.cos(t); st = math.sin(t)
        return (q*ct+s*st/math.sqrt(delta))/math.hypot(ct, st/math.sqrt(delta))
    tot = integrand(a)+integrand(a+math.pi)
    for k in range(1, n):
        tot += (4 if k%2 else 2)*integrand(a+k*h)
    return h*tot/(3*math.pi)


def uphill_probability(delta, q):
    s2=1-q*q
    cosine = 1/math.sqrt(1+q*q*s2*(1-delta)**2/delta)
    return math.acos(cosine)/math.pi


def golden_min(delta):
    a=0.; b=1.
    ratio=(math.sqrt(5)-1)/2
    c=b-ratio*(b-a); d=a+ratio*(b-a)
    fc=closed_progress(delta,c); fd=closed_progress(delta,d)
    for _ in range(135):
        if fc<fd:
            b=d;d=c;fd=fc;c=b-ratio*(b-a);fc=closed_progress(delta,c)
        else:
            a=c;c=d;fc=fd;d=a+ratio*(b-a);fd=closed_progress(delta,d)
    q=(a+b)/2
    return q,closed_progress(delta,q)


def main():
    checks=0
    for delta in (0.05, 0.15, 0.50, 0.85):
        for q in (0.,.125,.5,.875,1.):
            expr=closed_progress(delta,q)
            numeric=angular_integral(delta,q)
            assert abs(expr-numeric)<2e-8, (delta,q,expr,numeric)
            assert 0<expr<1.00000001
            checks+=2
    # The sign-disagreement probability maximizes at equal direction weights.
    for delta in (.0001,.01,.2,.8):
        bound=math.acos(2*math.sqrt(delta)/(1+delta))/math.pi
        assert abs(uphill_probability(delta,1/math.sqrt(2))-bound)<1e-13
        for j in range(101):
            assert uphill_probability(delta,j/100.) <= bound+1e-14
            checks+=1
    # Numerical minima approach the proved analytic scale and orientation law.
    for delta,tol in ((1e-8,.03),(1e-12,.02),(1e-24,.01)):
        q, minimum=golden_min(delta)
        L=math.log(1/delta)
        scale=2*math.sqrt(2)/math.pi*math.sqrt(delta*L)
        assert abs(minimum/scale-1)<tol, (delta, minimum/scale)
        assert abs(q*math.sqrt(L)/math.sqrt(2)-1)<tol, (delta, q)
        assert 0<q<1 and minimum<=closed_progress(delta,0.) and minimum<=closed_progress(delta,1.)
        checks+=5
    # Isotropic limiting mean signed progress is E|cos(angle)| = 2/pi.
    assert abs(closed_progress(1-1e-7,.4)-2/math.pi)<1e-7
    checks+=1
    print('CHECKS_OK',checks)

if __name__=='__main__':
    main()
