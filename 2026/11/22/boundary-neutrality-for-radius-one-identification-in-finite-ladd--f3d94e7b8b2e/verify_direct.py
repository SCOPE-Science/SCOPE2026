"""Independent exhaustive test: every identifying code at widths 2 through 9.

Run: python3 verify_direct.py (approximately seconds). No dependencies.
This check is finite corroboration; the all-length proof is in RESULT.md.
"""
from collections import Counter

EXPECTED = {2:(3,4), 3:(3,8), 4:(4,13), 5:(5,18),
            6:(6,64), 7:(6,2), 8:(8,353), 9:(9,836)}


def complete_census(n):
    closed_neighborhoods = []
    for col in range(n):
        for row in (0, 1):
            vertices = ((col,row),(col,1-row),(col-1,row),(col+1,row))
            closed_neighborhoods.append(sum(1 << (2*j+t) for j,t in vertices
                                             if 0 <= j < n))
    histogram = Counter()
    for chosen in range(1 << (2*n)):
        signatures = [neighborhood & chosen for neighborhood in closed_neighborhoods]
        if 0 in signatures or len(set(signatures)) < 2*n:
            continue
        histogram[chosen.bit_count()] += 1
    return histogram


if __name__ == '__main__':
    for width, expected in EXPECTED.items():
        hist = complete_census(width)
        actual = (min(hist), hist[min(hist)])
        assert actual == expected, (width, actual, expected)
        print(width, actual, 'total_codes', sum(hist.values()))
    print('DIRECT_OK')
