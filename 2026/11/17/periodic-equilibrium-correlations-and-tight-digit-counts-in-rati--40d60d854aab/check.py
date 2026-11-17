"""Independent finite exact-arithmetic checks of the stated frequency-shift identities.

The mathematical result for every integer parameter and infinite time is established
in the accompanying proof; these finite tests check its algebra and normalization.
"""
from fractions import Fraction as Q


def phase_law(N):
    return [Q(2 ** (N - a - 1), 2 ** N - 1) for a in range(N)]


def test_phase_convolutions():
    cases = 0
    for N in range(2, 23):
        q = phase_law(N)
        assert sum(q) == 1
        assert len(set(q)) == N
        for r in range(N):
            direct = sum(q[a] * q[(a + r) % N] for a in range(N)) / N - Q(1, N * N)
            closed = Q(2 ** (N - r) + 2 ** r, 3 * N * (2 ** N - 1)) - Q(1, N * N)
            assert direct == closed, (N, r, direct, closed)
            cases += 1
        assert sum(Q(2 ** (N - r) + 2 ** r, 3 * N * (2 ** N - 1))
                   - Q(1, N * N) for r in range(N)) == 0
    return cases


def test_geometric_origins():
    # Independent double finite sum of P(T=t)P(S=s) times the zero indicator.
    # Omitted mass is at most 2**(-H) for each geometric tail.
    cases = 0
    H = 28
    for N in range(2, 12):
        k = N - 1
        for a in range(N):
            partial = Q(0)
            for t in range(H):
                if k * t + a >= H:
                    break
                for s in range(k * t + a, H):
                    partial += Q(1, 2 ** (t + s + 2))
            expected = phase_law(N)[a]
            assert Q(0) <= expected - partial <= Q(2, 2 ** H), (N, a, expected, partial)
            cases += 1
    return cases


def test_symbolic_coboundary():
    count = 0
    lengths = [1, 3, 2, 5, 1, 4, 2, 1, 6, 3, 1, 4, 3, 2, 5, 1, 2]
    for N in range(2, 19):
        k = N - 1
        bits = []
        R = []
        for m in lengths:
            for j in range(N * m):
                bits.append(0 if j < m else 1)
                R.append(min(k * j, N * m - j))
        R.append(0)
        for j, b in enumerate(bits):
            assert R[j + 1] - R[j] == (N if b == 0 else 0) - 1
            count += 1
        for start in range(0, len(bits), max(1, N * 4)):
            for end in range(start, len(bits) + 1, max(1, N * 13)):
                zero_count = bits[start:end].count(0)
                assert N * zero_count - (end - start) == R[end] - R[start]
                count += 1
    return count


if __name__ == '__main__':
    exact = test_phase_convolutions()
    tails = test_geometric_origins()
    cob = test_symbolic_coboundary()
    print(f'VERIFY_OK exact_phase_convolutions={exact} finite_tail_checks={tails} coboundary_tests={cob}')
