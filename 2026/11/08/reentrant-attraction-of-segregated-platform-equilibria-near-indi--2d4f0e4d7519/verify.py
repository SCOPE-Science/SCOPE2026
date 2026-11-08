"""Reproduce the two-platform counterfactual-learning stability calculation.

Python 3 standard library only. Numerical checks supplement the analytic proof.
"""
import math


def bisect(f, lo, hi, iterations=90):
    vlo = f(lo)
    vhi = f(hi)
    assert vlo * vhi < 0, (lo, hi, vlo, vhi)
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        vmid = f(mid)
        if vlo * vmid < 0:
            hi = mid
        else:
            lo, vlo = mid, vmid
    return (lo + hi) / 2.0


def B(b):
    return 1.0 / (b * (1.0 - b * b)) + math.atanh(b) / b


def N(b):
    return -1.0 + 3.0 * b * b + b * (1.0 - b*b) - (1.0 - b*b)**2 * math.atanh(b)


def reward_flow(x, y, beta, mu):
    p1p = 1.0 / (1.0 + math.exp(beta * x))
    p1m = 1.0 / (1.0 + math.exp(beta * y))
    p2p, p2m = 1.0 - p1p, 1.0 - p1m
    o1 = (p1p - p1m) / (p1p + p1m)
    o2 = (p2p - p2m) / (p2p + p2m)
    f1p = (1.0 - mu) * o1 + mu * (1.0 - abs(o1))
    f2p = (1.0 - mu) * o2 + mu * (1.0 - abs(o2))
    f1m = -(1.0 - mu) * o1 + mu * (1.0 - abs(o1))
    f2m = -(1.0 - mu) * o2 + mu * (1.0 - abs(o2))
    return (f2p - f1p - x, f2m - f1m - y)


def branch_b(beta, mu):
    assert beta * (1.0 - mu) > 1.0
    return bisect(lambda b: math.atanh(b)/b - beta*(1.0 - mu), 1e-8, 0.999999999999)


if __name__ == '__main__':
    bstar = bisect(N, 0.1, 0.9)
    betastar = B(bstar)
    assert abs(bstar - 0.5526617952530661) < 1e-12
    assert abs(betastar - 3.7309540014225287) < 1e-12
    print('critical beta:', f'{betastar:.15f}')

    beta = 8.0
    blo = bisect(lambda b: B(b) - beta, 0.001, bstar)
    bhi = bisect(lambda b: B(b) - beta, bstar, 0.99999)
    mu_lo = 1.0 - math.atanh(bhi) / (beta * bhi)
    mu_hi = 1.0 - math.atanh(blo) / (beta * blo)
    assert abs(mu_lo - 0.790799809632571) < 1e-11
    assert abs(mu_hi - 0.8740987424930559) < 1e-11
    assert 0.0 < mu_lo < mu_hi < 0.875
    print('mu thresholds:', f'{mu_lo:.15f}', f'{mu_hi:.15f}', '0.875')

    # Full Jacobian is evaluated in (X,Y), rather than the (U,V) eigenbasis.
    for mu, expected in [(0.7, 'sink'), (0.83, 'saddle'), (0.8745, 'sink')]:
        b = branch_b(beta, mu)
        v = 2.0*(1.0-mu)*b
        fp, fm = reward_flow(v, -v, beta, mu)
        assert max(abs(fp), abs(fm)) < 2e-12
        transverse = beta*mu*b*(1.0-b*b)-1.0
        longitudinal = beta*(1.0-mu)*(1.0-b*b)-1.0
        assert longitudinal < 0
        assert (transverse < 0) == (expected == 'sink')
        h = 1e-6
        f_xplus = reward_flow(v+h, -v, beta, mu)
        f_xminus = reward_flow(v-h, -v, beta, mu)
        f_yplus = reward_flow(v, -v+h, beta, mu)
        f_yminus = reward_flow(v, -v-h, beta, mu)
        a = (f_xplus[0]-f_xminus[0])/(2*h)
        c = (f_xplus[1]-f_xminus[1])/(2*h)
        d = (f_yplus[0]-f_yminus[0])/(2*h)
        e = (f_yplus[1]-f_yminus[1])/(2*h)
        assert abs((a+e)-(transverse+longitudinal)) < 2e-8
        assert abs((a*e-c*d)-(transverse*longitudinal)) < 2e-8
        print(f'mu={mu:.4f}, b={b:.12f}, eigU={transverse:.12f}, eigV={longitudinal:.12f}, {expected}')

    for beta in [3.0, 3.731, 4.0, 8.0, 12.0]:
        for mu_fraction in [0.05, 0.25, 0.5, 0.75, 0.95]:
            mu = mu_fraction*(1.0-1.0/beta)
            b = branch_b(beta, mu)
            assert abs((beta*mu*b*(1-b*b)-1) - b*(1-b*b)*(beta-B(b))) < 4e-14
    print('PASS: exact analytical identities and independent numerical checks')
