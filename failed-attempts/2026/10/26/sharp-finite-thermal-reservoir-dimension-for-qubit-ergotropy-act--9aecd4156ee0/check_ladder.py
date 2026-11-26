"""Direct finite-dimensional checks of the thermal-ladder population theorem.

Run: python check_ladder.py  (requires NumPy).
All calculations use explicitly normalized density matrices and commuting unitaries.
Numerical checks support, but do not replace, the all-parameter proof.
"""
import math
import numpy as np


def thermal_weights(d, q):
    w = np.array([q ** k for k in range(d)], dtype=float)
    return w / w.sum()


def predicted_extrema(d, q, p):
    w = thermal_weights(d, q)
    lo = (1 - p) * w[-1]
    hi = lo
    for k in range(1, d):
        a, b = p * w[k], (1 - p) * w[k - 1]
        lo += min(a, b)
        hi += max(a, b)
    return lo, hi


def matrix_unitary(d, mixing):
    # Basis |system,bath> with system=0 (ground), 1 (excited).
    U = np.eye(2 * d, dtype=complex)
    for k, theta in enumerate(mixing, start=1):
        c, s = math.cos(theta), math.sin(theta)
        g, e = k, d + k - 1
        U[g, g] = c
        U[g, e] = -s
        U[e, g] = s
        U[e, e] = c
    return U


def density_excited(d, q, p, mixing):
    w = thermal_weights(d, q)
    diag = np.concatenate([p * w, (1 - p) * w])
    U = matrix_unitary(d, mixing)
    H = np.diag([k for k in range(d)] + [k + 1 for k in range(d)])
    assert np.max(abs(U.conj().T @ U - np.eye(2 * d))) < 5e-14
    assert np.max(abs(U @ H - H @ U)) < 5e-14
    X = (U * diag[np.newaxis, :]) @ U.conj().T
    # Summing only diagonal bath indices is the partial trace.
    out = np.array([[sum(X[s*d+k, t*d+k] for k in range(d))
                     for t in range(2)] for s in range(2)])
    assert abs(np.trace(out) - 1) < 5e-13
    assert abs(out[0, 1]) < 5e-13
    return out[1, 1].real


def q_threshold(d):
    a, b = 0.5, 1.
    for _ in range(80):
        m = (a + b) / 2
        if sum(m**k for k in range(1, d)) > 1:
            b = m
        else:
            a = m
    return (a + b) / 2


def main():
    rng = np.random.default_rng(20261024)
    checks = 0
    for d in (2, 3, 4, 5, 8, 13):
        for q in (.18, .45, .52, .61, .75, .97, 1.):
            for p in (.5, .57, .83, 1.):
                lo, hi = predicted_extrema(d, q, p)
                assert -1e-12 <= lo <= hi <= 1 + 1e-12; checks += 1
                val_0 = density_excited(d, q, p, [0.] * (d - 1))
                val_s = density_excited(d, q, p, [math.pi / 2] * (d - 1))
                assert abs(min(val_0, val_s) - lo) < 2e-12; checks += 1
                assert abs(max(val_0, val_s) - hi) < 2e-12; checks += 1
                if p*q > 1-p:
                    assert abs(hi - (p*(1-thermal_weights(d,q)[0]) +
                                     (1-p)*thermal_weights(d,q)[-1])) < 2e-12
                    checks += 1
                else:
                    assert abs(hi - (1-p)) < 2e-12; checks += 1
                for _ in range(4):
                    angles = rng.uniform(0, math.pi / 2, d-1)
                    v = density_excited(d, q, p, angles)
                    assert lo-2e-12 <= v <= hi+2e-12; checks += 1
    for d in range(3, 26):
        qd = q_threshold(d)
        assert .5 < qd < 1; checks += 1
        assert abs(sum(qd**k for k in range(1,d))-1) < 1e-12; checks += 1
        if d < 25: assert q_threshold(d+1) < qd; checks += 1
        q = min(0.999, qd + .005)
        assert predicted_extrema(d,q,1)[1] > .5; checks += 1
        q = max(.001, qd - .005)
        assert predicted_extrema(d,q,1)[1] < .5; checks += 1
    for q in (.501,.515,.55,.6,.65,.9,.999):
        D = math.floor(math.log(2*q-1)/math.log(q))+1
        assert D >= 3; checks += 1
        assert predicted_extrema(D,q,1)[1] > .5; checks += 1
        assert predicted_extrema(D-1,q,1)[1] <= .5 + 1e-12; checks += 1
    for d in (12,15,18,22,28):
        qd=q_threshold(d)
        assert abs((qd-.5)/2**(-d-1)-1)<0.01 if d>=12 else True
        checks+=1
    print('PASS',checks,'standalone assertions')

if __name__=='__main__':
    main()
