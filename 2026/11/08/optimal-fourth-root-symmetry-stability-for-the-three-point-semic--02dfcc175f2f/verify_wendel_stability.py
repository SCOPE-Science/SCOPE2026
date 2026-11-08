"""Independent numerical checks of a three-point circular hull stability law.

Python 3 standard library only. This is a finite numerical supplement, not a proof.
"""
import math
import random

TAU = 2 * math.pi
rng = random.Random(20261102)

def density(t, amps):
    return (1 + sum(a * math.cos(k*t) for k, a in amps.items())) / TAU

def semicircle_mass(t, amps):
    return 0.5 - sum(a * math.sin(k*t) / (math.pi*k)
                     for k, a in amps.items() if k % 2)

def quadrature(amps, steps=16384):
    step = TAU / steps
    p = 0.0
    defect = 0.0
    for j in range(steps):
        theta = step * j
        f = density(theta, amps)
        q = semicircle_mass(theta, amps)
        p += f*q*q*step
        defect += f*(q-0.5)**2*step
    return 3*p, 3*defect

def sample_angle(amps):
    height = 1 + sum(abs(a) for a in amps.values())
    while True:
        t = rng.random() * TAU
        if rng.random()*height <= TAU*density(t, amps):
            return t

def empirical(amps, trials=70000):
    count = 0
    for _ in range(trials):
        p = sorted(sample_angle(amps) for i in range(3))
        gaps = [p[1]-p[0], p[2]-p[1], p[0]+TAU-p[2]]
        count += max(gaps) >= math.pi
    return count/trials

cases = [({1:0.7}, 'odd-first'), ({3:0.65}, 'odd-third'),
         ({2:0.70}, 'even-second'), ({1:0.35,3:0.2}, 'mixed-odd')]
for amps, label in cases:
    p, defect = quadrature(amps)
    assert abs(p-0.75-defect) < 1e-12
    if len(amps)==1:
        k, eps = next(iter(amps.items()))
        exact = 0.75 + (3*eps*eps/(2*math.pi**2*k*k) if k%2 else 0)
        assert abs(p-exact)<1e-11, (label, p, exact)
    obs = empirical(amps)
    assert abs(obs-p)<0.012, (label, obs,p)
    print('CHECK', label, 'exact_integral=', format(p,'.10f'),
          'empirical=', format(obs,'.6f'))

# Quantitative exponent: hold derivative bound and positivity uniform as k varies.
c = 0.8
for k in (5,11,29,101):
    eps = c/k
    amps = {k:eps}
    p, delta = quadrature(amps)
    tv = 2*eps/math.pi
    m = (1-eps)/TAU
    L = c/TAU
    lower = 3*m*tv**4/(2*math.pi**3*L**2)
    assert abs(delta-3*c*c/(2*math.pi**2*k**4))<1e-12
    assert delta+1e-14>=lower
    print('SCALE', k, 'defect=', format(delta,'.12g'),
          'tv=',format(tv,'.9g'), 'fourth_power_ratio=',format(delta/tv**4,'.9g'))
print('VERIFY_OK formulas=4 simulated_samples=280000 spectral_exponent_cases=4')
