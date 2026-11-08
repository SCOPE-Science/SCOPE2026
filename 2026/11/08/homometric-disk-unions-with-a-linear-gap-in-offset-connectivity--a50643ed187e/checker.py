"""Deterministic certificate checks for the homometric disk-offset construction.

Only finite arithmetic assertions are tested; the theorem for every m follows
from the difference-multiset convolution and the explicit gap argument.
"""
from collections import Counter
from fractions import Fraction

A = (0, 1, 4, 10, 12, 17)
B = (0, 1, 8, 11, 13, 17)
HSTEP = 22


def differences(points):
    return Counter(y-x for x in points for y in points)


def gaps(points):
    return tuple(y-x for x,y in zip(points, points[1:]))


def centers(base, m):
    return tuple(sorted(x + HSTEP*k for k in range(m) for x in base))


def components(points, radius):
    threshold = 2*radius
    return 1 + sum(g>threshold for g in gaps(points))


def check():
    assert len(set(A)) == len(A) == len(set(B)) == len(B) == 6
    a_gaps, b_gaps = gaps(A), gaps(B)
    assert a_gaps == (1,3,6,2,5) and b_gaps == (1,7,3,2,4)
    assert HSTEP - max(A) == HSTEP - max(B) == 5
    a_diff, b_diff = differences(A), differences(B)
    assert a_diff == b_diff
    assert a_diff[0] == 6
    for d in range(1,18):
        expected = 0 if d in (14,15) else 1
        assert a_diff[d] == expected == a_diff[-d]
    assert sum(a_diff.values()) == 36
    for m in list(range(1,60)) + [100,200]:
        am,bm=centers(A,m),centers(B,m)
        assert len(am)==len(bm)==6*m
        assert differences(am)==differences(bm)
        assert min(gaps(am))>=1 and min(gaps(bm))>=1
        assert components(am, Fraction(13,4))==1
        assert components(bm, Fraction(13,4))==m+1
        for rad in (Fraction(3),Fraction(301,100),Fraction(349,100)):
            assert components(am,rad)==1
            assert components(bm,rad)==m+1
    # Area of 6m disjoint disks of radius 1/4: 6m*pi/16.
    # At offset r=3 their radius is 13/4. 2*(13/4)=6.5.
    assert 2*(Fraction(1,4)+3)==Fraction(13,2)
    assert Fraction(13,2)>6 and Fraction(13,2)<7
    print("HOMOMETRIC_DISK_OFFSET_LINEAR_COMPONENT_GAP_OK 61")

if __name__ == '__main__':
    check()
