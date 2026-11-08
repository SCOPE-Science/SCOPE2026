"""Standalone arithmetic checks of the rank-conditioned polar-step frontier.

Run: python verify.py
Requires only the standard Python library and NumPy.
"""
from fractions import Fraction as F
from itertools import permutations
import random
import numpy as np


def top_sum_except(lam, i, k):
    return sum(sorted((x for j, x in enumerate(lam) if j != i), reverse=True)[:k], F(0))


def bound(lam, r, alpha):
    J = min(lam[i] * (2-alpha*(lam[i]+top_sum_except(lam, i, r-1)))
            for i in range(len(lam)))
    return 1-alpha*J


def checks():
    count = 0
    rng = random.Random(2045)
    for d in range(2, 7):
        for rep in range(10):
            lam = [F(rng.randrange(1, 30), rng.randrange(1, 5)) for _ in range(d)]
            for r in range(1, d+1):
                tmax = sum(sorted(lam, reverse=True)[:r], F(0))
                alpha = F(rng.randrange(1, 8), 5*tmax)
                if alpha*tmax >= 2:
                    continue
                q = bound(lam, r, alpha)
                J = (1-q)/alpha
                # Enumerates all vertices of the orthostochastic relaxation.
                for perm in permutations(range(d)):
                    lhs = alpha*sum((lam[perm[j]] for j in range(r)), F(0)) + J/lam[perm[0]]
                    assert lhs <= 2, (d, r, lam, perm)
                    count += 1
                witness = min(range(d), key=lambda i: lam[i]*(2-alpha*(lam[i]+top_sum_except(lam,i,r-1))))
                others = sorted((j for j in range(d) if j != witness), key=lambda j: lam[j], reverse=True)[:r-1]
                indices = [witness]+others
                total = sum((lam[i] for i in indices), F(0))
                assert alpha*total < 2
                for power in (2, 4, 6):
                    eps = F(1, 10**power)
                    ss = [F(1)]+[eps]*(r-1)
                    ratio = 1-alpha*(2-alpha*total)*sum(ss, F(0))**2 / sum((s*s/lam[i] for s,i in zip(ss,indices)), F(0))
                    if r > 1: assert ratio < q
                    else: assert ratio == q
                    assert q-ratio < F(2*r, 10**(power-1))
                    count += 1
                # An exactly critical step is not strictly decreasing.
                crit = F(2, tmax)
                assert 2-crit*tmax == 0
                count += 1
    # Explicit spectrum with an appreciable gap to the published trace bound.
    lam = [F(1), F(10), F(11)]
    alpha = F(2,25)
    q = bound(lam, 2, alpha)
    old = 1-2*alpha+alpha*alpha*sum(sorted(lam,reverse=True)[:2])
    assert q == F(573, 625) and old == F(609, 625)
    assert bound(lam,2,F(1,12)) == F(11,12)
    count += 3
    # Monotone penalty from allowing another arbitrarily small singular value.
    for d in range(3, 9):
        lam = [F(rng.randrange(1, 50)) for _ in range(d)]
        a = F(1, 3*sum(lam))
        for r in range(1, d):
            assert bound(lam,r+1,a) > bound(lam,r,a)
            count += 1
    # Direct matrix reconstruction, using rotated SPD curvatures and gradient frames.
    nrng = np.random.default_rng(1657)
    for it in range(2400):
        d = int(nrng.integers(2, 9))
        r = int(nrng.integers(1, d+1))
        n = int(nrng.integers(r, r+4))
        spectrum = np.sort(nrng.uniform(.3, 12.0, size=d))
        lam_rat = [F(float(x)).limit_denominator(10**7) for x in spectrum]
        tmax = sum(spectrum[-r:])
        alpha = float(nrng.uniform(.04, 1.95))/tmax
        q = float(bound(lam_rat, r, F(alpha)))
        R,_ = np.linalg.qr(nrng.normal(size=(d,d)))
        H = (R*spectrum)@R.T
        Hinv = (R*(1/spectrum))@R.T
        U,_ = np.linalg.qr(nrng.normal(size=(d,r)))
        V,_ = np.linalg.qr(nrng.normal(size=(n,r)))
        s = np.exp(nrng.uniform(-5,1,size=r))
        G = (U*s)@V.T
        P = U@V.T
        E = Hinv@G
        S = float(s.sum())
        Enew = E-alpha*S*P
        f = np.trace(E.T@H@E)/2
        fnew = np.trace(Enew.T@H@Enew)/2
        Q = float(fnew/f)
        direct = 1-alpha*(2-alpha*np.trace(U.T@H@U))*S*S/np.trace(G.T@Hinv@G)
        assert abs(Q-direct) < 2e-8
        assert Q <= q+2e-8, (d,r,Q,q)
        count += 2
    print('PASS:',count,'exact assignment/witness and numeric reconstruction checks')

if __name__=='__main__':
    checks()
