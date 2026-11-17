"""Exact rational checks for point-evaluation energy on parallel-path metric graphs.

The checks verify the independent Kirchhoff--Poisson construction and
compare its value and energy to the analytic embedding kernel.
Finite checks are corroboration, not a proof for all lengths.
"""
from fractions import Fraction as Q
from itertools import product


def integrated_square(d, length, left, right, shift):
    """Integral over [left,right] of (d + u/length - shift)^2."""
    w = d - shift
    return (w*w*(right-left)
            + w*(right*right-left*left)/length
            + (right**3-left**3)/(3*length*length))


def green_poisson(lengths, which, position):
    """Independent exact Green solution with -g'' = delta_position - 1/L."""
    r = len(lengths)
    L = sum(lengths)
    ell = lengths[which]
    C = sum((1/x for x in lengths), Q(0))
    delta = ((position/ell) - Q(1,2))/C
    slopes = [delta/x - x/(2*L) + ((x-position)/x if j==which else 0)
              for j,x in enumerate(lengths)]
    assert sum(slopes) == 0
    assert sum(slopes[j]+lengths[j]/L-(1 if j==which else 0)
               for j in range(r)) == 0
    moments_without_A = sum(
        (slopes[j]*x*x/2 + x**3/(6*L)
         - ((x-position)**2/2 if j==which else 0))
        for j,x in enumerate(lengths))
    A = -moments_without_A/L
    B = A+delta
    # Both endpoints and zero mean are checked independently.
    assert all(A+slopes[j]*x+x*x/(2*L)
               - (x-position if j==which else 0)==B
               for j,x in enumerate(lengths))
    assert A*L+moments_without_A==0
    g_at_point = A+slopes[which]*position+position*position/(2*L)
    energy = Q(0)
    for j,x in enumerate(lengths):
        if j==which:
            energy += integrated_square(slopes[j], L, Q(0), position, 0)
            energy += integrated_square(slopes[j], L, position, x, 1)
        else:
            energy += integrated_square(slopes[j], L, Q(0), x, 0)
    assert energy == g_at_point
    return g_at_point


def kernel_formula(lengths, which, pos):
    L=sum(lengths)
    C=sum((1/x for x in lengths), Q(0))
    x=lengths[which]
    cubic=sum((a**3 for a in lengths),Q(0))/(12*L*L)
    return (cubic+(pos/x-Q(1,2))**2/C
            +pos*(x-pos)*(1/x-1/L))


def sharp_constant(lengths):
    L=sum(lengths)
    biggest=max(lengths)
    return sum((a**3 for a in lengths),Q(0))/(12*L*L) + biggest*(L-biggest)/(4*L)


def verify():
    checks=0
    for r in range(2,6):
        for idx in product(range(1,4),repeat=r):
            # A nonuniform rational perturbation tests noninteger lengths.
            ls=tuple(Q(i, (j%3)+1) for j,i in enumerate(idx))
            L=sum(ls)
            c=sharp_constant(ls)
            for j,x in enumerate(ls):
                for pos in (Q(0), x/5, x/2, 4*x/5, x):
                    p=green_poisson(ls,j,pos)
                    assert p == kernel_formula(ls,j,pos)
                    assert p <= c
                    if len(ls)==2:
                        assert p==L/12
                    if r>=3 and pos==x/2:
                        assert (p==c) == (x==max(ls))
                    checks+=1
            if r>=3:
                assert L*(3*r-2)/(12*r*r) <= c < L/12
                if len(set(ls))==1:
                    assert c==L*(3*r-2)/(12*r*r)
    assert sharp_constant((Q(1),Q(1),Q(1)))==Q(7,36)
    assert sharp_constant((Q(1),Q(1),Q(1),Q(1)))==Q(5,24)
    print('EXACT_KIRCHHOFF_POISSON_AND_ENERGY_OK',checks)
    print('MAXIMAL_MIDPOINT_AND_LONGEST_PATH_OK')
    print('SHARP_EQUILATERAL_AND_CYCLE_SHAPE_BOUNDS_OK')
    print('ALL_PARALLEL_PATH_SOBOLEV_CHECKS_OK')

if __name__=='__main__':
    verify()
