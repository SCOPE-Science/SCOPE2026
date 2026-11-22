"""Exact finite enumeration of primitive binary LFSR degree-discrepancy peaks.

This standalone certificate uses integer arithmetic; no scientific data files required.
"""
from collections import Counter
from fractions import Fraction


def step(state, polynomial, degree):
    shifted = state << 1
    if shifted & (1 << degree):
        shifted ^= polynomial
    return shifted


def degree_cycle(polynomial, degree):
    """Return a nonzero orbit, requiring it to close on state 1."""
    state = 1
    seen = set()
    values = []
    while state not in seen:
        assert 0 < state < 1 << degree
        seen.add(state)
        values.append(state.bit_length() - 1)
        state = step(state, polynomial, degree)
    assert state == 1
    return values


def direct_range_scaled(degrees, r, k):
    """Slow direct method: scaled 2*M times window total variation."""
    M = len(degrees)
    scores = []
    for start in range(M):
        histogram = [0] * k
        for h in range(r):
            histogram[degrees[(start + h) % M]] += 1
        scores.append(sum(abs(M * histogram[j] - r * (1 << j))
                          for j in range(k)))
    return max(scores) - min(scores)


def sliding_range_scaled(degrees, r, k):
    """Independent update algorithm, with no window recounts."""
    M = len(degrees)
    histogram = [0] * k
    for j in degrees[:r]:
        histogram[j] += 1

    def score():
        return sum(abs(M * histogram[j] - r * (1 << j))
                   for j in range(k))

    low = high = score()
    for start in range(1, M):
        histogram[degrees[start-1]] -= 1
        histogram[degrees[(start+r-1) % M]] += 1
        s = score()
        low = min(low, s)
        high = max(high, s)
    return high - low


def spectrum(degree):
    M = (1 << degree) - 1
    peaks = []
    tested_windows = 0
    for poly in range((1 << degree) + 1, (1 << (degree+1)), 2):
        degrees = degree_cycle(poly, degree)
        if len(degrees) != M:
            continue
        assert Counter(degrees) == Counter({j: 1 << j for j in range(degree)})
        peak = 0
        horizons = []
        for r in range(1, M // 2 + 1):
            a = direct_range_scaled(degrees, r, degree)
            b = sliding_range_scaled(degrees, r, degree)
            assert a == b, (degree, poly, r, a, b)
            tested_windows += 1
            if a > peak:
                peak = a
                horizons = [r]
            elif a == peak:
                horizons.append(r)
            # Independent complement symmetry using full recount.
            if r in (1, M//2):
                assert a == direct_range_scaled(degrees, M-r, degree)
        peaks.append((poly, Fraction(peak, 2*M), min(horizons)))
    return peaks, tested_windows


def reciprocal(poly, k):
    return sum(((poly >> i) & 1) << (k-i) for i in range(k+1))


def main():
    expected = {
      2: [(0x7, Fraction(1,3),1)],
      3: [(0xb,Fraction(6,7),3),(0xd,Fraction(6,7),3)],
      4: [(0x13,Fraction(8,5),6),(0x19,Fraction(8,5),6)],
      5: [(0x25,Fraction(70,31),15),
          (0x29,Fraction(68,31),14),
          (0x2f,Fraction(80,31),9),
          (0x37,Fraction(86,31),15),
          (0x3b,Fraction(86,31),15),
          (0x3d,Fraction(80,31),9)],
    }
    tests = 0
    for k in range(2,6):
        rows, n = spectrum(k)
        assert rows == expected[k], (k, rows)
        assert len(rows) == [0,0,1,2,2,6][k]
        tests += n
        print(f'k={k} M={(1<<k)-1}: '+ ' '.join(
            f'0x{p:x}:{v} @r={h}' for p,v,h in rows))
    assert reciprocal(0x25,5) == 0x29
    print(f'LFSR_EXHAUSTIVE_DEGREE_FIVE_OK: {tests} primitive-polynomial/horizon pairs; '
          'direct + sliding independently agree')

if __name__ == '__main__':
    main()
