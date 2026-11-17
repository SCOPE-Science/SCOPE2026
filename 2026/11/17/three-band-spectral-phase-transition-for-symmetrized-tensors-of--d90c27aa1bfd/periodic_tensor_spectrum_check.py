"""Finite-dimensional checks for alternating-shift tensor spectra.

Run: python periodic_tensor_spectrum_check.py
Requires numpy. These are finite checks, not a proof of the infinite spectrum.
"""
import math
import numpy as np


def matrices(n, a, b):
    d = n + 1
    j = np.zeros((d, d))
    for i in range(n):
        wi = a if i % 2 == 0 else b
        wj = a if (n - i - 1) % 2 == 0 else b
        j[i, i+1] = j[i+1, i] = wi*wj/2
    refl = np.eye(d)[:, ::-1]
    bases = []
    for sign in (1, -1):
        cols = []
        for i in range(d // 2):
            v = np.zeros(d)
            v[i] = 1 / math.sqrt(2)
            v[n-i] = sign / math.sqrt(2)
            cols.append(v)
        if sign == 1 and d % 2:
            v = np.zeros(d)
            v[d // 2] = 1
            cols.append(v)
        bases.append(np.stack(cols, axis=1) if cols else np.zeros((d, 0)))
    assert np.allclose(refl @ j, j @ refl)
    return j, bases


def allowed(e, a, b, tol=1e-9):
    t = abs(e)
    lo = abs(a*a-b*b)/2
    hi = (a*a+b*b)/2
    return t <= a*b+tol or lo-tol <= t <= hi+tol


def run():
    tests = 0
    for a, b in ((5.,1.), (1.,5.), (1.,1.), (3.,1.), (1.,3.), (0.5,4.), (4.,0.5), (1.4,1.1)):
        top = (a*a+b*b)/2
        low = abs(a*a-b*b)/2
        for n in range(0,50):
            j, sectors = matrices(n, a, b)
            eig = np.linalg.eigvalsh(j)
            for v in eig:
                assert allowed(v,a,b), (n,a,b,v)
                tests += 1
            for q in sectors:
                if not q.shape[1]:
                    continue
                assert np.allclose(q.T @ q,np.eye(q.shape[1]))
                assert np.allclose(j @ q @ q.T,q @ q.T @ j)
                ev = np.linalg.eigvalsh(q.T @ j @ q)
                for v in ev:
                    assert allowed(v,a,b), (n,a,b,v)
                    assert abs(v) < top + 1e-10
                    tests += 1
            if n % 2 == 1:
                m = (n+1)//2
                c = np.eye(m)*a*a/2
                c[np.arange(1,m), np.arange(m-1)] = b*b/2
                pos = np.linalg.svd(c,compute_uv=False)
                assert np.allclose(np.sort(abs(eig)),np.sort(np.r_[pos,pos]))
                tests += 1
                if a>=b:
                    assert min(pos) >= low-1e-9
                else:
                    assert min(pos) <= a*a/2+1e-9
                    if m>1:
                        assert sorted(pos)[1] >= low-1e-9
                tests += 1
    # The sector maxima tend to the predicted (unattained) spectral edge.
    for a,b in ((5.,1.),(1.,5.),(1.,1.),(3.,1.)):
        maxima=[]
        for n in (19,59,199):
            j,q = matrices(n,a,b)
            maxima.append(min(np.linalg.eigvalsh(x.T@j@x)[-1] for x in q))
        assert maxima[0] < maxima[1] < maxima[2] < (a*a+b*b)/2
        tests += 1
    print('PASS', tests, 'finite matrix and singular-value assertions')


if __name__ == '__main__':
    run()
