"""Standalone arithmetic diagnostics for cyclic rational-delay period-two spectra.

Run: python verify_floquet.py (requires numpy).
These finite tests complement, not replace, the analytical proof.
"""
import cmath
import math
import numpy as np


def spatial_shift(k):
    s = np.zeros((k, k))
    for i in range(k):
        s[i, (i + 1) % k] = 1
    return s


def one_step_jacobian(current, previous):
    k = len(current)
    j = np.zeros((2*k, 2*k))
    for i in range(k):
        nxt = (i + 1) % k
        j[i, nxt] = -previous[nxt] / current[nxt]**2
        j[i, k+nxt] = 1/current[nxt]
    j[k:, :k] = np.eye(k)
    return j


def predicted(k, r):
    d = (r-1)/r**2
    vals = [complex(1), complex(d)]
    for j in range(1, k):
        q = cmath.exp(2j * math.pi * j/k)
        tr = q + q*q*d
        disc = cmath.sqrt(tr*tr - 4*q*q*d)
        vals.extend([(tr+disc)/2, (tr-disc)/2])
    return np.array(vals, dtype=complex)


def spectral_gap_coefficient(d):
    return 2*math.pi**2*d*(1-3*d)/(1-d)**3


def verify():
    trials = 0
    for k in range(2, 17):
        for r in [1.01, 1.25, 2, 2.9, 9, 100]:
            s = r/(r-1)
            e = np.full(k, r)
            o = np.full(k, s)
            # First move at even phase, then at odd phase.
            return_jac = one_step_jacobian(o, e) @ one_step_jacobian(e, o)
            obtained = np.linalg.eigvals(return_jac)
            expected = predicted(k, r)
            for z in expected:
                if min(abs(z-v) for v in obtained) > 5e-7:
                    raise AssertionError((k,r,z,obtained))
            stable = [z for z in expected if abs(z-1)>1e-7]
            assert max(map(abs, stable)) < 1-1e-10, (k,r,stable)
            trials += 1
    for r in [1.01, 1.5, 2, 3, 30]:
        d = (r-1)/r**2
        c = spectral_gap_coefficient(d)
        for k in [200, 400]:
            lam = predicted(k, r)
            rho = max(abs(v) for v in lam if abs(v-1)>1e-10)
            normalized = k*k*(1-rho)
            assert abs(normalized/c - 1)<0.002, (r,k,normalized,c)
            trials += 1
    # Sample explicit recurrence (three-site published case) from perturbed phase.
    for k in [3, 5, 9]:
        r = 3.0
        s = r/(r-1)
        prev = np.full(k,s)+np.linspace(-.001,.001,k)
        curr = np.full(k,r)+np.linspace(.001,-.001,k)
        for _ in range(2500):
            nxt = 1+np.roll(prev,-1)/np.roll(curr,-1)
            prev,curr=curr,nxt
        assert np.ptp(curr)<1e-9 and np.ptp(prev)<1e-9
        assert abs((curr[0]-1)*(prev[0]-1)-1)<1e-9
        trials += 1
    print('PASS',trials,'return-spectrum, gap, and trajectory test groups')

if __name__=='__main__':
    verify()
