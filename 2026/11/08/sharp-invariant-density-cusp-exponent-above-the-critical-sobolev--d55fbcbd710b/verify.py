"""Numerical checks for local inverse branch asymptotics; not a proof of invariant-density regularity."""
from mpmath import mp
mp.dps = 100
cases = [('-0.4', '1.5'), ('-0.25', '1.3'), ('-0.1', '1.8')]
for bb, tt in cases:
    b, theta = mp.mpf(bb), mp.mpf(tt)
    A = (2**(1+b))*(1-theta/2)
    lam = theta+(2-theta)*(1+b)
    assert lam>1
    gamma = -b/(1+b)
    # For constant test function phi=1, P_phi(x) = 2 / p(t).
    # Exact local prediction: P_phi(1-delta) ~ [2/((1+b)*A**(1/(1+b)))] delta**gamma.
    C = 2/((1+b)*A**(1/(1+b)))
    ratios=[]
    for k in [10,30,60,90]:
        delta = mp.power(10,-k)
        lo, hi = mp.mpf(0), delta/theta
        for _ in range(550):
            mid=(lo+hi)/2
            if theta*mid+A*mid**(1+b)>delta: hi=mid
            else: lo=mid
        t=(lo+hi)/2
        assert t>0
        assert abs(theta*t+A*t**(1+b)-delta)/delta < mp.mpf('1e-60')
        density = 2/(theta+A*(1+b)*t**b)
        ratio = density/(C*delta**gamma)
        ratios.append(abs(ratio-1))
    assert ratios[-1] < ratios[0]
    assert ratios[-1] < mp.mpf('0.005')
    print('CASE_OK', bb, tt, 'gamma=',mp.nstr(gamma,12),'tail_err=',mp.nstr(ratios[-1],8))
print('VERIFY_OK three_power_cusp_cases=3 high_precision_only=1')
