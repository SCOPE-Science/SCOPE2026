"""Exact rational checks of five-agent Hegselmann-Krause odd cycles.

Usage: python check_hk.py
The unrestricted statement is established by the accompanying algebraic proof.
"""
from fractions import Fraction as Q


def verify(m, split):
    assert isinstance(m, int) and m >= 1
    q = Q(1, 10**m)
    low = [1 - Q(1, 10**j) / (2 - q) for j in range(m + 1)]
    left, right = low[-2], low[-1]
    assert left < right and right - left == 9 * q / (2 - q)
    assert Q(0) < low[0] <= left < right < Q(1)
    assert low[-1] == 2 * low[0]
    assert all(low[j] < low[j + 1] for j in range(m))
    assert all(2 * low[j] > 1 for j in range(1, m + 1))
    radius = 9 + (1 - split) * left + split * right
    pts = [(Q(0), Q(0), Q(0)), (Q(9), Q(0), Q(0)),
           (Q(0), Q(9), Q(0)), (Q(0), Q(0), Q(9)),
           (low[0],) * 3]
    radii = [Q(1, 10)] * 4 + [radius]
    seen = []
    five_count = 0
    two_count = 0
    for k in range(2 * m + 1):
        seen.append(pts[4])
        new_pts = []
        for i in range(5):
            nbrs = [j for j in range(5)
                    if sum(abs(pts[i][c] - pts[j][c]) for c in range(3)) <= radii[i]]
            if i < 4:
                assert nbrs == [i]
            else:
                expected = [0, 1, 2, 3, 4] if k < 2*m and k % 2 == 0 else [0, 4]
                assert nbrs == expected, (m, split, k, nbrs)
                five_count += len(nbrs) == 5
                two_count += len(nbrs) == 2
            new_pts.append(tuple(sum(pts[j][c] for j in nbrs) / len(nbrs)
                                 for c in range(3)))
        pts = new_pts
    assert len(set(seen)) == 2 * m + 1
    assert pts[4] == seen[0]
    assert five_count == m and two_count == m + 1
    assert Q(1, 5**m * 2**(m + 1)) == Q(1, 2 * 10**m)
    if m > 1:
        prevq = Q(1, 10**(m - 1))
        prev_right = 1 - prevq / (2 - prevq)
        assert prev_right < left
    return left, right


if __name__ == "__main__":
    for m in range(1, 31):
        for split in (Q(1, 4), Q(1, 2), Q(3, 4)):
            l, h = verify(m, split)
        if m <= 5:
            print(f"period={2*m+1}, lower_r={l}, upper_r={h}")
    print("PASS: 90 exact full-system rational periodic-orbit tests")
