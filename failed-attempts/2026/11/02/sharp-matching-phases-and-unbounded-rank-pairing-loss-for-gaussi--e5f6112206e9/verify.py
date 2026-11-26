#!/usr/bin/env python3
"""Reproduce numerical checks for the exact Gaussian pairing-gain theorem.

The theorem and its global optimality/limiting statements are proved analytically;
finite experiments below are only independent numerical sanity checks.
"""
import itertools
import math

ROOT_TWO = math.sqrt(2.0)
SQRT_TWO_OVER_PI = math.sqrt(2.0 / math.pi)


def gauss_abs(scale, distance):
    d = abs(float(distance))
    return scale * SQRT_TWO_OVER_PI * math.exp(-0.5 * (d / scale) ** 2) + d * math.erf(d / (ROOT_TWO * scale))


def gain(sigma, distance):
    # Return the difference of the positive Gaussian smoothing corrections.
    d = abs(float(distance))
    def extra(scale):
        return scale * SQRT_TWO_OVER_PI * math.exp(-0.5 * (d / scale) ** 2) - d * math.erfc(d / (ROOT_TWO * scale))
    return extra(2.0*sigma) - extra(ROOT_TWO*sigma)


def curvature(sigma, d):
    t = d/sigma
    return (math.exp(-t*t/8.0) - ROOT_TWO*math.exp(-t*t/4.0))/(sigma * math.sqrt(2.0*math.pi))


def assignment(sigma, a, b, perm):
    return sum(gain(sigma, a[i]-b[perm[i]]) for i in range(len(a)))


def check():
    count = 0
    for sigma in [0.25, 0.5, 1.0, 3.0]:
        dc = 2*sigma*math.sqrt(math.log(2.0))
        for ratio in [0, 0.1, 0.7, 0.99]:
            assert curvature(sigma, dc*ratio) < 0
            count += 1
        for ratio in [1.01, 1.1, 2.0, 5.0]:
            assert curvature(sigma, dc*ratio) > 0
            count += 1
        assert abs(curvature(sigma, dc)) < 1e-14 / sigma
        for d in [0, 0.2*sigma, 0.8*sigma, 2*sigma, 4*sigma]:
            h = 0.003*sigma
            second = (gain(sigma,d+h)-2*gain(sigma,d)+gain(sigma,d-h))/(h*h)
            assert abs(second-curvature(sigma,d)) < 1e-6 / sigma
            assert gain(sigma,d) > 0
            count += 1
        for n in [2,3,4,5]:
            aa = [0.1*sigma*i for i in range(n)]
            near = [sigma*(0.05+0.09*j) for j in range(n)]
            far = [sigma*(3.0+0.13*j) for j in range(n)]
            assert max(abs(x-y) for x in aa for y in near) < dc
            assert min(abs(x-y) for x in aa for y in far) > dc
            permutations = list(itertools.permutations(range(n)))
            identity = tuple(range(n))
            reverse = identity[::-1]
            near_values = [(p,assignment(sigma,aa,near,p)) for p in permutations]
            far_values = [(p,assignment(sigma,aa,far,p)) for p in permutations]
            assert max(near_values,key=lambda x:x[1])[0] == identity
            assert min(near_values,key=lambda x:x[1])[0] == reverse
            assert max(far_values,key=lambda x:x[1])[0] == reverse
            assert min(far_values,key=lambda x:x[1])[0] == identity
            count += 4*len(permutations)
    ratios = []
    for t in [3.0, 4.0, 5.0, 6.0]:
        delta=1.0
        a=[0.0,t]
        b=[t-delta,2*t]
        rank=assignment(1.0,a,b,(0,1))
        crossed=assignment(1.0,a,b,(1,0))
        assert sum(abs(x-y) for x,y in zip(a,b)) < abs(a[0]-b[1])+abs(a[1]-b[0])
        assert rank < crossed
        ratios.append(rank/crossed)
        count += 2
    assert all(ratios[i]>ratios[i+1] for i in range(len(ratios)-1))
    print('VERIFICATION_OK checks=',count,'critical_ratio=',2*math.sqrt(math.log(2.0)),'rank_to_best_ratios=',ratios)

if __name__ == '__main__':
    check()
