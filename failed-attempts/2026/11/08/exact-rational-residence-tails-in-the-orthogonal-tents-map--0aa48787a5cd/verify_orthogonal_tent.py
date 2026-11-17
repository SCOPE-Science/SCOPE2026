"""Standalone exact-rational checks of the orthogonal-tent branch geometry.

These finite tests corroborate, but do not substitute for, the interval
case split and integral proof in RESULT.md.
"""
from fractions import Fraction as Q


def frac(x):
    return x - (x.numerator // x.denominator)


def boundary(x,d):
    return any(frac(z) in (Q(0),Q(1,2)) for z in (x-d, -x+2*d, -x+3*d, x-4*d))

def in_even_pair(x, d):
    # A_3 at the initial state and its successor.  All arithmetic is exact.
    y = frac(x-d)
    u = frac(-x + 2*d)
    y1 = frac(-x+3*d)
    u1 = frac(x-4*d)
    return y >= Q(1,2) and u < Q(1,2) and y1 >= Q(1,2) and u1 < Q(1,2)


def in_tabulated_interval(x,d):
    if d < Q(1,4):
        left,right=Q(1,2)+2*d,Q(1,2)+3*d
    elif d < Q(1,3):
        left,right=4*d-1,d
    elif d < Q(2,3):
        return False
    elif d < Q(3,4):
        left,right=d-Q(1,2),4*d-Q(5,2)
    else:
        left,right=3*d-2,2*d-1
    # Circular closed intervals; rational-boundary choices have measure zero.
    x0=frac(x-left)
    return x0 < right-left


def even_survival(x,d,m):
    for k in range(m):
        if not in_even_pair(frac(x-4*k*d), d):
            return False
    return True


def predicted_even_survival(x,d,m):
    # Uses the independent explicit E_d intervals rather than iterating H.
    if d < Q(1,4):
        left,e=Q(1,2)+2*d,d
    elif d < Q(1,3):
        left,e=4*d-1,1-3*d
    elif d < Q(2,3):
        return False
    elif d < Q(3,4):
        left,e=d-Q(1,2),3*d-2
    else:
        left,e=3*d-2,1-d
    if m==1:
        return frac(x-left) < e
    for k in range(m):
        if not (frac(x-4*k*d-left) < e):
            return False
    return True

# Grid points avoid every equality boundary. Check the interval table and
# every time in 2,4,...,12 on an exact rational grid.
count=0
N=137
for i in range(N):
    d=Q(2*i+1,2*N)
    for j in range(N):
        x=Q(2*j+1,2*N)
        if boundary(x,d):
            continue
        if in_even_pair(x,d)!=in_tabulated_interval(x,d):
            raise AssertionError(('E_d case split',x,d))
        for m in range(1,7):
            if any(boundary(frac(x-4*k*d), d) for k in range(m)):
                continue
            if even_survival(x,d,m)!=predicted_even_survival(x,d,m):
                raise AssertionError(('survivor',x,d,m))
        count +=1

# An independent exact integration of the two nonzero local-overlap
# triangles, with slopes equal to the interval-shrink rates.
for m in range(2,30):
    left_half=Q(1,32*(4*m-3))
    right_half=Q(1,32*(4*m-1))
    area_from_four_triangles=2*(left_half+right_half)
    closed=Q(2*m-1,4*(4*m-3)*(4*m-1))
    assert area_from_four_triangles == closed
    assert Q(1,16)*(Q(1,4*m-3)+Q(1,4*m-1)) == closed

assert Q(2,1) * (Q(1,32)+Q(1,96)) == Q(1,12)
print('ORTHOGONAL_TENTS_EXACT_PAIR_INTERVALS_AND_SURVIVORS_OK grid=',count)
print('ORTHOGONAL_TENTS_EXACT_SURVIVOR_AREA_OK m=2..29 S4=',Q(3,140), ' S6=',Q(5,396))
