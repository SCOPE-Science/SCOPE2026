"""Finite numerical diagnostics for the hyperplane-crossing radius law.

Run: python check.py. These checks supplement, not replace, the proof.
"""
import math
import numpy as np


def cdf(q):
    if q <= 0.5:
        return 0.0
    if q >= 1.0:
        return 1.0
    return 4.0 * math.atan(math.sqrt(2.0*q - 1.0)) / math.pi


def direct_sample(d, count, seed):
    rng = np.random.default_rng(seed)
    total = 0.0
    total_sq = 0.0
    count_06 = count_08 = count_below_half = 0
    count_done = 0
    for i in range(0, count, 2000):
        n = min(2000, count-i)
        u = rng.normal(size=(n,d))
        v = rng.normal(size=(n,d))
        u /= np.linalg.norm(u,axis=1)[:,None]
        v /= np.linalg.norm(v,axis=1)[:,None]
        # Reflection of the second endpoint puts it in the opposite hemisphere;
        # the conditional distribution remains independent and surface-uniform.
        a = np.abs(u[:,-1])
        b = np.abs(v[:,-1])
        z = (b[:,None]*u[:,:-1] + a[:,None]*v[:,:-1]) / (a+b)[:,None]
        q = np.sum(z*z, axis=1)
        assert np.all((q>=-1e-12) & (q<=1+1e-12))
        total += float(np.sum(q))
        total_sq += float(np.sum(q*q))
        count_06 += int(np.count_nonzero(q<=0.6))
        count_08 += int(np.count_nonzero(q<=0.8))
        count_below_half += int(np.count_nonzero(q<0.5))
        count_done += n
    return total/count_done, total_sq/count_done, count_06/count_done, count_08/count_done, count_below_half/count_done


def main():
    # Integrate using the nonsingular W=sqrt(2Q-1) coordinate.
    w = (np.arange(500_000,dtype=float)+0.5)/500_000
    density = 4.0/(math.pi*(1+w*w))
    q = (1+w*w)/2
    vals = [float(np.mean(density*q**k)) for k in [0,1,2]]
    expected = [1.0, 2/math.pi, 4/(3*math.pi)]
    assert all(abs(a-b)<2e-6 for a,b in zip(vals,expected)), (vals,expected)
    assert abs(cdf(.6)-4/math.pi*math.atan(math.sqrt(.2)))<1e-14
    assert abs(cdf(.8)-4/math.pi*math.atan(math.sqrt(.6)))<1e-14
    print('NORMALIZATION_AND_MOMENTS_OK',vals)
    rng = np.random.default_rng(912341)
    x = np.abs(rng.normal(size=210_000))
    y = np.abs(rng.normal(size=210_000))
    w_ratio = np.abs(x-y)/(x+y)
    for threshold in (0.2,0.5,0.8):
        exact = 4*math.atan(threshold)/math.pi
        assert abs(np.mean(w_ratio<=threshold)-exact)<0.008, (threshold,exact)
    print('HALF_CAUCHY_TRANSFORM_CHECK_OK')

    d3 = direct_sample(d=3,count=75_000,seed=12345)
    assert abs(d3[0]-.5)<.014, d3  # known 3-dimensional sanity check
    assert abs(d3[3]-.8)<.019, d3
    print('THREE_DIMENSION_BASELINE_OK',d3)

    d500 = direct_sample(d=500,count=95_000,seed=23456)
    assert abs(d500[0]-2/math.pi)<.013, d500
    assert abs(d500[2]-cdf(.6))<.028, d500
    assert abs(d500[3]-cdf(.8))<.025, d500
    assert d500[4]<.15, d500  # finite-dimensional transition is broad near q=1/2
    print('HIGH_DIMENSION_CROSSING_DIAGNOSTICS_OK',d500,
          {'limit_mean': 2/math.pi,'cdf06':cdf(.6),'cdf08':cdf(.8)})
    print('SPHERICAL_CHORD_EQUATORIAL_LIMIT_CHECKS_OK')

if __name__ == '__main__':
    main()
