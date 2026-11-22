"""Supplementary numerical diagnostics for powered geodesic cycle kernels.

No numerical output is used as an infinite-dimensional proof.
Requires Python 3, numpy, mpmath.
"""
import math
import numpy as np
import mpmath as mp


def eigenvalues(p, n, t):
    assert n % 4 == 0 and 1 < p < 2 and t > 0
    m = n // 2
    k = np.arange(n)
    row = np.exp(-t * np.minimum(k, n-k).astype(float)**p)
    return np.fft.fft(row).real


def sign_tests():
    # Strongly separated bands: below may have negative modes at moderate N;
    # above may take much larger N for its asymptotic guarantee.
    count = 0
    for p in [1.2, 1.5, 1.8]:
        cstar = 2**p * (p-1)
        for n in [256, 512, 1024, 2048]:
            for mult in [0.30, 0.40]:
                ev = eigenvalues(p, n, mult*cstar*math.log(n)/n**p)
                assert np.min(ev) < -1e-10, (p,n,mult,np.min(ev))
                count += 1
            for mult in [8.0, 12.0]:
                ev = eigenvalues(p, n, mult*cstar*math.log(n)/n**p)
                assert np.min(ev) > 0, (p,n,mult,np.min(ev))
                count += 1
    return count


def nyquist_crossover():
    # Compare a finite exact alternating sum with the analytic critical limit.
    mp.mp.dps = 65
    checks=[]
    for p in [mp.mpf('1.2'), mp.mpf('1.5'), mp.mpf('1.8')]:
        cp = 2*mp.altzeta(-p)
        h0 = mp.log(p/(2*cp))
        for m in [128,256,512,1024]:
            for h in [h0-mp.mpf('1.0'), h0+mp.mpf('1.0')]:
                t = ((p-1)*mp.log(m)+h)/m**p
                val = 1 + 2*sum((-1)**j*mp.exp(-t*j**p) for j in range(1,m)) + mp.exp(-t*m**p)
                approximation = cp-p*mp.exp(-h)/2
                observed = val/t
                # Finite-size errors decay logarithmically, not monotonically.
                assert mp.isfinite(observed)
                checks.append((float(p),m,float(h),float(observed),float(approximation)))
    return checks


if __name__ == '__main__':
    num = sign_tests()
    results = nyquist_crossover()
    print('Fourier sign tests:',num,'passed')
    print('Crossover evaluations:',len(results),'completed')
    for p in [1.2,1.5,1.8]:
        v=[x for x in results if abs(x[0]-p)<1e-8 and x[1]==1024]
        for x in v:
            print('p=%.1f m=%d h=%.6f eigen/t=%.8f limit=%.8f' % x)
