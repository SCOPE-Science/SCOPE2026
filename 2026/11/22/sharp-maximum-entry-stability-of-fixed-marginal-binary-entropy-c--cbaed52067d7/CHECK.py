"""Supplementary numerical checks for a fixed-marginal binary entropy-coupling modulus.

Run: python3 CHECK.py. This is numerical evidence, not a universal proof.
"""
import math
import random


def interval(r, c):
    return max(0.0, r + c - 1.0), min(r, c)


def reciprocal_curvature(z, r, c):
    return sum(1.0 / x for x in (z, r-z, c-z, 1-r-c+z))


def curvature_derivative(z, r, c):
    return -1/z**2 + 1/(r-z)**2 + 1/(c-z)**2 - 1/(1-r-c+z)**2


def optimal_z(r, c):
    lo, hi = interval(r, c)
    for _ in range(95):
        mid = (lo + hi)/2
        if curvature_derivative(mid, r, c) < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def plan(r, c, x):
    """x is 2 by 2 flattened logarithmic kernel, in row-major order."""
    h = x[0]-x[1]-x[2]+x[3]
    lo, hi = interval(r, c)
    for _ in range(95):
        z = (lo+hi)/2
        odds = math.log(z) + math.log(1-r-c+z) - math.log(r-z) - math.log(c-z)
        if odds < h:
            lo = z
        else:
            hi = z
    z = (lo+hi)/2
    return (z, r-z, c-z, 1-r-c+z)


def main():
    rng = random.Random(724291)
    checks = 0
    cases = [(0.5,0.5),(0.5,0.2),(0.3,0.5),(0.2,0.2),
             (0.3,0.7),(0.1,0.9),(0.3,0.4),(0.1,0.4),
             (0.8,0.8),(0.8,0.2)]
    cases += [(rng.uniform(0.025,0.975),rng.uniform(0.025,0.975)) for _ in range(1600)]
    for r,c in cases:
        z = optimal_z(r,c)
        l,u=interval(r,c)
        assert l < z < u
        assert abs(curvature_derivative(z,r,c)) < 2e-5*(1+reciprocal_curvature(z,r,c)**2)
        checks+=2
        L = 4/reciprocal_curvature(z,r,c)
        bound = min(r*(1-r), c*(1-c))
        assert L <= bound+2e-12
        checks+=1
        if abs(r-0.5)<1e-12 or abs(c-0.5)<1e-12:
            assert abs(L-bound)<2e-12
        else:
            assert L<bound
        checks+=1
        association=(z-r*c)*(1-2*r)*(1-2*c)
        assert association > -2e-13
        checks+=1
        x=[rng.uniform(-3,3) for _ in range(4)]
        y=[rng.uniform(-3,3) for _ in range(4)]
        px,py=plan(r,c,x),plan(r,c,y)
        inp=max(abs(a-b) for a,b in zip(x,y))
        out=max(abs(a-b) for a,b in zip(px,py))
        assert out<= L*inp+4e-12
        checks+=1
    # Almost equality from a checkerboard perturbation at an optimized plan.
    for r,c in [(0.3,0.4),(0.2,0.2),(0.5,0.3),(0.3,0.5),(0.5,0.5)]:
        z = optimal_z(r,c)
        p = (z,r-z,c-z,1-r-c+z)
        x = tuple(math.log(v) for v in p)
        L=4/reciprocal_curvature(z,r,c)
        for h in (1e-3, 1e-4, 1e-5):
            v=(x[0]+h,x[1]-h,x[2]-h,x[3]+h)
            out=max(abs(a-b) for a,b in zip(plan(r,c,v),p))
            ratio=out/h
            assert abs(ratio-L)<(h*3+3e-8)
            checks+=1
    print('PASS supplementary numerical assertions:',checks)
    print('Sample r=0.3,c=0.4: optimal z=',optimal_z(.3,.4),'L=',4/reciprocal_curvature(optimal_z(.3,.4),.3,.4))


if __name__ == '__main__':
    main()
