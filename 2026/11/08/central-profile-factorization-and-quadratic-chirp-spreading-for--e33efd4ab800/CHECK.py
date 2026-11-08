"""Exact integer-cyclotomic checks of the finite Heisenberg STFT claim.

Run: python CHECK.py
The general theorem rests on finite character orthogonality and a quadratic Gauss-sum argument;
these finite checks are independent small-parameter tests, not an infinite proof.
"""
from itertools import product


def vectors(p, d):
    return list(product(range(p), repeat=d))


def verify_prime(p, n, alpha, beta):
    d = 2 * n + 1
    N = p ** d
    half = pow(2, -1, p)
    vecs = vectors(p, d)
    freqs = vecs
    # All linear phases, independently of the nonlinear translated chirp.
    linear = [tuple(sum(s * t for s, t in zip(freq, point)) % p
                    for point in vecs) for freq in freqs]
    counts = {"one": 0, "wide": 0, "zero": 0}
    for tr in vecs:
        aa, bb, cc = tr[:n], tr[n:2*n], tr[-1]
        horizontal = any(aa) or any(bb)
        qdiff = []
        for pt in vecs:
            xx, yy, zz = pt[:n], pt[n:2*n], pt[-1]
            w = (cc + half * (sum(x * b for x, b in zip(xx, bb))
                                - sum(y * a for y, a in zip(yy, aa)))) % p
            qdiff.append((alpha * (2 * zz * w - w * w) + beta * w) % p)
        expected_magnitude_squared = N * N // (p * p) if horizontal else N * N
        for phase in linear:
            hist = [0] * p
            for ph, lin in zip(qdiff, phase):
                hist[(ph - lin) % p] += 1
            is_zero = len(set(hist)) == 1
            if is_zero:
                counts["zero"] += 1
                continue
            # The coefficient array of |sum_r hist[r] zeta^r|^2.
            cyclic = [sum(hist[r] * hist[(r - k) % p]
                          for r in range(p)) for k in range(p)]
            assert len(set(cyclic[1:])) == 1, (p, n, tr, phase, cyclic)
            assert cyclic[0] - cyclic[1] == expected_magnitude_squared, (
                p, n, tr, phase, cyclic, expected_magnitude_squared)
            counts["wide" if horizontal else "one"] += 1
    assert counts["one"] == p, (p, n, counts)
    assert counts["wide"] == (N - p) * p * p, (p, n, counts)
    assert counts["zero"] == N * N - p - (N - p) * p * p, (p, n, counts)
    print("EXACT_P", p, "N", n, "ALPHA", alpha, "BETA", beta, "TOTAL", N,
          "ONE", counts["one"], "WIDE", counts["wide"],
          "ZERO", counts["zero"])


if __name__ == "__main__":
    for p, n, alpha, beta in [(3, 1, 1, 0), (3, 1, 2, 1),
                              (5, 1, 1, 0), (5, 1, 2, 3),
                              (3, 2, 1, 0)]:
        verify_prime(p, n, alpha, beta)
    print("ALL_EXACT_STFT_CHECKS_PASSED")


def verify_general_profile(p):
    """Independent direct summation test for an arbitrary complex central profile."""
    import cmath
    U = [1 + 0.37 * (z % 2) + 0.2j * z for z in range(p)]
    E = sum(abs(v)**2 for v in U)
    roots = [cmath.exp(-2j * cmath.pi * t / p) for t in range(p)]
    F = [sum(U[z] * roots[(k*z) % p] for z in range(p)) for k in range(p)]
    half = pow(2, -1, p)
    points = vectors(p, 3)
    for a,b,c in points:
        data = []
        for x,y,z in points:
            h = (c + half * (x*b-y*a))%p
            data.append((x,y,z,U[z]*U[(z-h)%p].conjugate()))
        for P,Q,W in points:
            direct = sum(v*roots[(P*x+Q*y+W*z)%p] for x,y,z,v in data)/(p*p*E)
            if a == b == 0:
                pred = (sum(U[z]*U[(z-c)%p].conjugate()*roots[(W*z)%p]
                            for z in range(p))/E) if P==Q==0 else 0
            else:
                lam = next((lam for lam in range(p)
                            if P == (lam*b*half)%p and Q == (-lam*a*half)%p), None)
                pred = 0 if lam is None else (roots[(-lam*c)%p]*F[(W+lam)%p]*F[lam].conjugate()/(p*E))
            assert abs(direct-pred)<1e-10, (p,(a,b,c),(P,Q,W),direct,pred)
    print('GENERAL_PROFILE_DIRECT_FACTOR_CHECK_PASSED',p)


if __name__ == '__main__':
    for p in (3, 5):
        verify_general_profile(p)
    print('ALL_GENERAL_PROFILE_CHECKS_PASSED')
