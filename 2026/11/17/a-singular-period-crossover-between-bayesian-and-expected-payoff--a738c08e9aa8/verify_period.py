"""Numerical consistency checks for the Hamiltonian period crossover.
Run with python3 verify_period.py (standard library only).
"""
import math


def logcosh(x):
    a = abs(x)
    return a + math.log1p(math.exp(-2*a)) - math.log(2)


def pot(theta, x):
    return (1-theta)*x*x/2 + 4*theta*logcosh(x/2)


def force(theta, x):
    return (1-theta)*x + 2*theta*math.tanh(x/2)


def period(theta, E, n=1500):
    assert 0 <= theta <= 1 and E > 0
    step = math.pi/(2*n)
    s = 0.0
    for i in range(n):
        a = (i+0.5)*step
        c, q = math.cos(a), math.sin(a)
        lo, hi = 0.0, max(1.0, E + 4.0)
        while pot(theta, hi*c)+pot(theta, hi*q)<E:
            hi *= 2
        for _ in range(44):
            m = (lo+hi)/2
            if pot(theta, m*c)+pot(theta, m*q)<E:
                lo=m
            else:
                hi=m
        r=(lo+hi)/2
        w=(c*force(theta,r*c)+q*force(theta,r*q))/r
        s+=1.0/w
    return 4*step*s


def crossover(e):
    return 8*math.atan(math.sqrt(1+e/2))-2*math.pi


def main():
    period_cases = 0
    for theta in (0.0,0.2,0.5,0.9,1.0):
        vals=[period(theta,E,400) for E in (0.05,1.0,5.0,20.0)]
        if theta==0:
            assert max(abs(v-2*math.pi) for v in vals)<1e-8
        else:
            assert all(a < b for a,b in zip(vals,vals[1:]))
        period_cases+=1
    low_checks = 0
    for theta in (0.3,0.7,1.0):
        E=0.008
        v=period(theta,E,800)
        approx=2*math.pi*(1+theta*E/8)
        assert abs(v-approx)<0.0001
        low_checks+=1
    boundary_checks=0
    for e in (0.4,1,3,8):
        t1=0.04*period(0.96,e/0.04,1200)
        t2=0.01*period(0.99,e/0.01,2400)
        target=crossover(e)
        assert abs(t2-target) < abs(t1-target)+0.005
        assert abs(t2-target) < 0.06
        boundary_checks+=1
    large_checks=0
    for theta,E in ((0.4,2000), (0.8,4000), (1.0,1500)):
        value=period(theta,E,1000)
        target=E if theta==1 else 2*math.pi/(1-theta)
        assert abs(value/target-1)<0.07
        large_checks+=1
    print(f'VERIFY_OK strict_period_cases={period_cases} small_energy_checks={low_checks} crossover_parameters={boundary_checks} high_energy_cases={large_checks}')

if __name__=='__main__':
    main()
