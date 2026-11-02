#!/usr/bin/env python3
"""Exact rational checks of the directional-arc covering construction.
This is finite verification only; see the separate analytical proof.
"""
from fractions import Fraction


def interval_data(theta):
    m = len(theta)
    out = []
    for i in range(m):
        before = theta[i - 1] if i else theta[-1] - 1
        out.append((theta[i] + Fraction(1, 4), before + Fraction(3, 4)))
        assert 0 < out[-1][1] - out[-1][0] < Fraction(1, 2)
    return out


def in_arc(x, ab):
    a, b = ab
    return any(a < x + n < b for n in range(-2, 4))


def max_overlap(intervals):
    ends = sorted({v % 1 for ab in intervals for v in ab})
    points = ends[:] + [((ends[j] + (ends[j + 1] if j + 1 < len(ends) else ends[0] + 1)) / 2) % 1 for j in range(len(ends))]
    return max(sum(in_arc(x, ab) for ab in intervals) for x in points)


def block_beams(theta, k, reference_theta=None):
    m = len(theta)
    if reference_theta is None:
        reference_theta = theta
    ref = interval_data(reference_theta)
    result = []
    for j in range(m):
        shifted = []
        for t in range(j, j + k):
            i = t % m
            turn = t // m
            a, b = ref[i]
            shifted.append((a + turn, b + turn))
        start = max(a for a, _ in shifted)
        end = min(b for _, b in shifted)
        assert start < end
        beam = (start + end) / 2 % 1
        for t in range(j, j + k):
            assert in_arc(beam, interval_data(theta)[t % m]), (m, j, t)
        result.append(beam)
    arcs = interval_data(theta)
    assert all(sum(in_arc(beam, arc) for beam in result) >= k for arc in arcs)
    return result


def main():
    assertions = 0
    for m in range(3, 28):
        theta0 = [Fraction(i, m) for i in range(m)]
        intervals = interval_data(theta0)
        k = (m - 1) // 2
        assert max_overlap(intervals) == k, ('equiangular', m)
        beams = block_beams(theta0, k)
        assert len(beams) == m
        assertions += 3
        if m % 2:
            # Angular displacement is strictly less than 1/(4m) of a full turn,
            # i.e., strictly less than pi/(2m) radians.
            for phase in range(3):
                offsets = [Fraction(((5 * i + 3 * phase) % 7) - 3, 28 * m) for i in range(m)]
                theta = [x + shift for x, shift in zip(theta0, offsets)]
                for i in range(m):
                    delta = theta[i] - (theta[i-1] if i else theta[-1] - 1)
                    assert 0 < delta < Fraction(1, 2)
                arcs = interval_data(theta)
                assert max_overlap(arcs) == k, ('perturbed', m, phase)
                beams = block_beams(theta, k, reference_theta=theta0)
                assert len(beams) == m
                assertions += m + 2
    print(f'VERIFY_OK exact_fractional_polygon assertions={assertions}')


if __name__ == '__main__':
    main()
