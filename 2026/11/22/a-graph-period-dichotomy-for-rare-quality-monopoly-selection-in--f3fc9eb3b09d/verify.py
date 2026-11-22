"""Finite-state corroboration for the two-channel popularity theorem.

Run: python verify.py
Requires NumPy. This finite checker is not a proof of claims for arbitrary n.
The universal proof uses support periodicity and singular Markov perturbation.
"""
import itertools
import numpy as np


def compute(P, eps=1e-5):
    P = np.asarray(P, dtype=float)
    n = len(P)
    assert n == 3 and np.allclose(P.sum(axis=1), 1)
    states = tuple(itertools.product((0, 1), repeat=2*n))
    loc = {s: i for i, s in enumerate(states)}
    one = tuple((1, 0) * n)
    two = tuple((0, 1) * n)
    tr = [i for i, s in enumerate(states) if s != one and s != two]
    mat = np.array(states, dtype=float)
    qs = (0.8, 0.6)

    def transition(strength):
        M = np.empty((len(states), len(states)))
        for i, s in enumerate(states):
            sums = [sum(s[2*v+c] for v in range(n)) for c in (0,1)]
            tot = sum(sums)
            probabilities = np.array([
                (1-strength)*(0.5*sum(P[v,w]*s[2*w+c] for w in range(n))
                +0.5*(sums[c]/tot if tot else 0.5))+strength*qs[c]
                for v in range(n) for c in (0,1)
            ])
            M[i] = np.prod(mat*probabilities+(1-mat)*(1-probabilities), axis=1)
        assert np.max(abs(M.sum(axis=1)-1)) < 1e-13
        return M

    P0 = transition(0)
    h = np.zeros(len(states))
    h[loc[two]] = 1
    h[tr] = np.linalg.solve(np.eye(len(tr))-P0[np.ix_(tr,tr)],
                            P0[np.ix_(tr, [loc[two]])].ravel())
    a = []; b = []
    for v in range(n):
        add = list(one); add[2*v+1] = 1
        drop = list(one); drop[2*v] = 0
        a.append(h[loc[tuple(add)]])
        b.append(h[loc[tuple(drop)]])
    A = sum(a); B = sum(b)
    pred = (A*qs[0]+B*(1-qs[1])) / (A*sum(qs)+B*(2-sum(qs)))
    Pe = transition(eps)
    eq = np.eye(len(states))-Pe.T
    eq[-1, :] = 1
    rhs = np.zeros(len(states)); rhs[-1] = 1
    nu = np.linalg.solve(eq, rhs)
    assert np.min(nu) > -1e-10
    return A, B, pred, nu[loc[one]], 1-nu[loc[one]]-nu[loc[two]]


if __name__ == '__main__':
    path = [[0, 1, 0], [.5, 0, .5], [0, 1, 0]]
    triangle = [[0, .5, .5], [.5, 0, .5], [.5, .5, 0]]
    AP, BP, pP, epP, outP = compute(path)
    AT, BT, pT, epT, outT = compute(triangle)
    assert AP > 0 and abs(BP) < 1e-12
    assert abs(pP - 4/7) < 1e-12
    assert AT > 0 and BT > .006 and pT > 4/7
    assert abs(pT - .5718683358010358) < 2e-10
    assert abs(epP-pP) < 2e-4 and abs(epT-pT) < 2e-4
    assert 0 < outP < .0003 and 0 < outT < .0003
    print('P3:', {'A': AP, 'B': BP, 'limit': pP, 'finite_eps': epP, 'transient': outP})
    print('K3:', {'A': AT, 'B': BT, 'limit': pT, 'finite_eps': epT, 'transient': outT})
    print('PASS: all finite corroboration assertions')
