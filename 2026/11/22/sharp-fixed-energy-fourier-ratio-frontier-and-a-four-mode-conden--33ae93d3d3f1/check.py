"""Supplementary numerical checks for the sharp finite-grid Fourier ratio."""
import math
import random


def spectrum(n):
    assert n >= 4
    sines = [math.sin(math.pi*j/n)**2 for j in range(n)]
    vals = [4*n*n*(sines[i]+sines[j]) for i in range(n) for j in range(n) if i or j]
    low = 4*n*n*sines[1]
    assert sum(abs(v-low) <= 1e-8 for v in vals) == 4
    return low, vals


def frontier(n, budget):
    low, vals = spectrum(n)
    avg = sum(vals)/len(vals)
    if budget <= low + 1e-9:
        return 2.0, 0.0, low
    if budget >= avg:
        return math.sqrt(len(vals)), 1.0, avg
    tail = [v-low for v in vals if v > low + 1e-7]
    delta = budget-low

    def energy_gap(eps):
        zlow = 4/(eps*eps)
        ss = sum(1/(v+eps)**2 for v in tail)
        bs = sum(v/(v+eps)**2 for v in tail)
        return bs/(zlow+ss)

    l, r = 0.0, 1.0
    while energy_gap(r) < delta:
        r *= 2.0
    for _ in range(80):
        mid = (l+r)/2
        if energy_gap(mid) < delta:
            l = mid
        else:
            r = mid
    eps = (l+r)/2
    aa = 4/(eps*eps)+sum(1/(v+eps)**2 for v in tail)
    bb = 4/eps + sum(1/(v+eps) for v in tail)
    q = sum(1/(v+eps)**2 for v in tail)/aa
    assert abs(energy_gap(eps)-delta) < 3e-7
    return bb/math.sqrt(aa), q, eps


def test():
    rng = random.Random(1729)
    trials = 0
    for n in (4,5,6,8,11,17):
        lo, vals = spectrum(n)
        avg = sum(vals)/len(vals)
        assert abs(avg-4*n**4/(n*n-1))<1e-6
        assert abs(frontier(n, lo)[0]-2)<1e-10
        assert abs(frontier(n, avg)[0]-math.sqrt(n*n-1))<1e-10
        for factor in (0.12,0.40,0.70,0.93):
            e = lo+factor*(avg-lo)
            mx, q, eps = frontier(n, e)
            assert 2 < mx < math.sqrt(n*n-1)
            assert 0 < q < 1 and eps > 0
            for _ in range(150):
                a = [rng.random()**2 for _ in vals]
                z = sum(a)
                p = [x/z for x in a]
                energy = sum(x*v for x,v in zip(p,vals))
                if energy <= e:
                    value = sum(math.sqrt(x) for x in p)
                    assert value <= mx + 1e-8
                    trials += 1
    for n in (11,31,101,201,401):
        E=60
        mx,q,eps=frontier(n,E)
        lo,vals=spectrum(n)
        gap=E-lo
        tt=[(v-lo) for v in vals if v>lo+1e-7]
        S=sum(1/x for x in tt)
        T=sum(1/(x*x) for x in tt)
        upper=2+math.sqrt(gap*S)
        lower=2*math.sqrt(1-gap*T/S)+math.sqrt(gap*S)
        assert lower-1e-8<=mx<=upper+1e-8
        print('N=',n,'frontier=',round(mx,8),'pred=',round(upper,8),'gap=',round(upper-mx,8),'tail_mass=',round(q,8),'T=',round(T,8))
    print('Supplementary assertions passed, feasible random profiles checked:',trials)

if __name__ == '__main__':
    test()
