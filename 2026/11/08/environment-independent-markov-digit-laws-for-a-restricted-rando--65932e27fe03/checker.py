"""Exact rational checks for the restricted Lüroth coarse-state theorem."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

B = [F(1, 3), F(7, 18), F(4, 9), F(1, 2), F(2, 3), F(5, 6), F(1)]
COARSE = [(F(1, 3), F(1, 2)), (F(1, 2), F(2, 3)), (F(2, 3), F(1))]
Q = [[F(1, 6), F(1, 6), F(2, 3)],
     [F(0), F(0), F(1)],
     [F(1, 4), F(1, 4), F(1, 2)]]
PI = [F(3, 16), F(3, 16), F(5, 8)]

def branch(i, environment):
    slope, intercept = ((F(6), F(-2)) if i < 3 else (F(2), F(-1)))
    alternate = i in ((0, 3) if environment == 0 else (0, 1, 3, 4))
    return (-slope, 1 - intercept) if alternate else (slope, intercept)

def coarse_index(v):
    return 0 if v < F(1, 2) else (1 if v < F(2, 3) else 2)

def branch_index(v):
    return min(5, max(0, sum(v >= x for x in B) - 1))

def exact_cylinder(env):
    """Independent direct interval integration on original starting points."""
    states = [(L, R, F(1), F(0), (j,)) for j, (L, R) in enumerate(COARSE)]
    for e in env:
        nxt = []
        for left, right, scale, shift, hist in states:
            cuts = [left, right]
            for bp in B[1:-1]:
                z = (bp - shift) / scale
                if left < z < right:
                    cuts.append(z)
            for u, v in zip(sorted(set(cuts))[:-1], sorted(set(cuts))[1:]):
                y = scale * (u + v) / 2 + shift
                aa, bb = branch(branch_index(y), e)
                nn, cc = aa * scale, aa * shift + bb
                # Split preimages of target-state boundaries as well as source-branch boundaries.
                refined = [u, v]
                for threshold in (F(1, 2), F(2, 3)):
                    z = (threshold - cc) / nn
                    if u < z < v:
                        refined.append(z)
                for a, b in zip(sorted(refined)[:-1], sorted(refined)[1:]):
                    j = coarse_index(nn * (a + b) / 2 + cc)
                    nxt.append((a, b, nn, cc, hist + (j,)))
        states = nxt
    out = defaultdict(F)
    for left, right, _, _, hist in states:
        weight = (F(9, 8) if hist[0] < 2 else F(15, 8)) * (right - left)
        out[hist] += weight
    return out

def expected_prob(hist):
    prob = PI[hist[0]]
    for a, b in zip(hist[:-1], hist[1:]):
        prob *= Q[a][b]
    return prob

def main():
    # Geometric transition calculation on each single branch (not a model fit).
    for e in (0, 1):
        for j, (L, R) in enumerate(COARSE):
            masses = [F(0) for _ in range(3)]
            for i in range(6):
                u, v = max(L, B[i]), min(R, B[i+1])
                if u >= v:
                    continue
                a, c = branch(i, e)
                yl, yr = sorted((a*u+c, a*v+c))
                for k, (s, t) in enumerate(COARSE):
                    masses[k] += max(F(0), min(yr, t)-max(yl, s)) / abs(a) / (R-L)
            assert masses == Q[j], (e, j, masses)
    assert sum(PI) == 1
    assert [sum(PI[i]*Q[i][j] for i in range(3)) for j in range(3)] == PI
    for n in range(1, 10):
        # Exact (Q^n) AA entry obeys its spectral formula.
        vec = [F(1), F(0), F(0)]
        for _ in range(n):
            vec = [sum(vec[k]*Q[k][j] for k in range(3)) for j in range(3)]
        cov = PI[0]*vec[0] - PI[0]*PI[0]
        assert cov == F(3,256)*(-F(1,3))**n
    for n in range(1, 12):
        variance = n * F(39,256) + 2 * sum((n-k)*F(3,256)*(-F(1,3))**k for k in range(1, n))
        assert variance == F(75,512)*n + F(9,2048)*(1-(-F(1,3))**n)
    total_paths = 0
    # Exact independent four-step integration over all 16 fixed switch words.
    for env in product((0,1), repeat=4):
        direct = exact_cylinder(env)
        for hist in product(range(3), repeat=5):
            assert direct[hist] == expected_prob(hist), (env, hist, direct[hist], expected_prob(hist))
            total_paths += 1
        assert sum(direct.values()) == 1
    print('PASS: exact branch images, stationarity, covariances, finite variances,')
    print('      and',total_paths,'four-step environment/state probabilities by direct integration.')

if __name__ == '__main__':
    main()
