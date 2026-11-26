#!/usr/bin/env python3
"""Independent numerical sanity tests for the exact Neumann heat BV-to-L1 norm.
The universal proof is analytical and contained in RESULT.md.
Requires only Python 3 standard library.
"""
import math
import random

PI = math.pi

def kernel(t, x, y, cutoff=1000):
    """Neumann cosine eigenfunction expansion; t is strictly positive."""
    z = 1.0
    for k in range(1, cutoff + 1):
        v = 2.0 * math.exp(-PI * PI * k * k * t)
        if v < 1e-17:
            break
        z += v * math.cos(k * PI * x) * math.cos(k * PI * y)
    return z

def jump_error(t, s, cutoff=1000):
    z = 2 * s * (1 - s)
    for k in range(1, cutoff + 1):
        a = math.exp(-PI * PI * k * k * t)
        if a < 1e-17:
            break
        z -= 4.0 * a * (math.sin(k * PI * s) / (k * PI))**2
    return z

def sharp(t, cutoff=1000):
    z = 0.5
    for j in range(cutoff):
        k = 2 * j + 1
        a = math.exp(-PI * PI * k * k * t)
        if a < 1e-17:
            break
        z -= 4.0 / (PI * PI) * a / (k * k)
    return z

def test():
    rng = random.Random(85242)
    for t in (0.0008, 0.003, 0.01, 0.035, 0.1, 0.6, 2.0):
        C = sharp(t)
        assert abs(jump_error(t, .5) - C) < 2e-13
        for j in range(1, 50):
            s = j / 100.0
            es = jump_error(t, s)
            assert es <= C + 3e-13
            assert abs(es - jump_error(t, 1-s)) < 5e-13
        # Discrete derivative positivity away from numerical roundoff regions.
        if t >= .02:
            seq = [jump_error(t, j / 100.0) for j in range(2, 49)]
            assert all(b >= a - 1e-13 for a,b in zip(seq, seq[1:]))
    print('SEVEN_TIME_SPECTRAL_SHARPNESS_SYMMETRY_CHECKS_PASS')
    # Spectral Neumann kernel is positive, symmetric, and integrates to one;
    # integral checked with midpoint quadrature, not used as a proof.
    for t in (0.01,0.07,0.3):
        for x in (.11,.35,.5,.92):
            midpoint = sum(kernel(t,x,(i+.5)/1200) for i in range(1200))/1200
            assert abs(midpoint-1) < 2e-9
            assert min(kernel(t,x,y) for y in (.01,.2,.53,.99)) > 0
            assert abs(kernel(t,x,.37)-kernel(t,.37,x)) < 1e-13
    print('NEUMANN_MARKOV_KERNEL_QUADRATURE_CHECKS_PASS')
    # Exact crossing formula evaluated independently using the kernel on a grid.
    for t,s in ((.02,.25),(.05,.4),(.1,.5),(.3,.2)):
        n=160
        cross=0.
        for i in range(n):
            x=(i+.5)*s/n
            for j in range(n):
                y=s+(j+.5)*(1-s)/n
                cross += kernel(t,x,y)
        cross *= 2*s*(1-s)/n**2
        assert abs(cross-jump_error(t,s)) < 2e-5, (t,s,cross,jump_error(t,s))
    print('CROSSING_INTEGRAL_INDEPENDENT_QUADRATURE_CHECKS_PASS')
    # BV signed-jump reduction for finite mixtures: integrate error on a grid.
    for t in (.01,.07,.3):
        C=sharp(t)
        for trial in range(150):
            locations=sorted(rng.uniform(.05,.95) for _ in range(rng.randint(1,8)))
            weights=[rng.uniform(-1,1) for _ in locations]
            n=256
            err=0.
            for i in range(n):
                x=(i+.5)/n
                actual=sum(w*(x>s) for s,w in zip(locations,weights))
                smooth=0.
                for s,w in zip(locations,weights):
                    v=1-s
                    for k in range(1,90):
                        a=math.exp(-PI*PI*k*k*t)
                        if a<1e-17:break
                        v -= 2*a*math.cos(k*PI*x)*math.sin(k*PI*s)/(k*PI)
                    smooth+=w*v
                err+=abs(actual-smooth)/n
            assert err <= C*sum(abs(w) for w in weights)+.02
    print('SIGNED_MULTIJUMP_NUMERICAL_INEQUALITY_CHECKS_PASS 450')
    # Time derivative and short/long time asymptotics.
    for t in (.005,.02,.08,.3):
        deriv=4*sum(math.exp(-PI**2*(2*j+1)**2*t) for j in range(150))
        h=1e-7
        approx=(sharp(t+h)-sharp(t-h))/(2*h)
        assert abs(deriv-approx)<3e-8
    for t in (.001,.002,.003):
        assert abs(sharp(t)/(2*math.sqrt(t/PI))-1)<1e-7
    for t in (.6,1.,2.):
        assert abs((.5-sharp(t))/(4/PI**2*math.exp(-PI**2*t))-1)<1e-7
    print('TIME_DERIVATIVE_AND_ASYMPTOTIC_CHECKS_PASS')
    print('ALL_NEUMANN_BV_L1_CHECKS_PASS')

if __name__=='__main__':test()
