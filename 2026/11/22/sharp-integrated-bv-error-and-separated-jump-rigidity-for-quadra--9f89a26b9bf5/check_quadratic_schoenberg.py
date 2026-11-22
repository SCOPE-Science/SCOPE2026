"""Exact-rational checks for the quadratic Greville spline error theorem.

Run: python3 check_quadratic_schoenberg.py
No third-party packages required. Finite checks corroborate, not replace, the proof.
"""
from fractions import Fraction as F


def knots(n):
    h = F(1, n)
    return [F(0)] * 3 + [i * h for i in range(1, n)] + [F(1)] * 3


def basis(n, x):
    """Cox--de Boor recurrence, rational including repeated endpoint knots."""
    t = knots(n)
    if x == 1:
        return [F(0)] * (n+1) + [F(1)]
    low = [F(1) if t[i] <= x < t[i + 1] else F(0)
           for i in range(len(t) - 1)]
    for p in (1, 2):
        new = []
        for i in range(len(low)-1):
            val = F(0)
            if t[i+p] != t[i]:
                val += (x-t[i])/(t[i+p]-t[i])*low[i]
            if t[i+p+1] != t[i+1]:
                val += (t[i+p+1]-x)/(t[i+p+1]-t[i+1])*low[i+1]
            new.append(val)
        low = new
    return low


def step_spline(n, j, x):
    return sum(basis(n, x)[j:], F(0))


def integral_step_error(n, j, s):
    """Exact integral using Simpson on all knot/jump subintervals."""
    t = sorted(set(knots(n) + [s]))
    total = F(0)
    for a, b in zip(t, t[1:]):
        if a == b:
            continue
        m = (a+b)/2
        # Use exact quadratic polynomial integration; one-sided endpoint values
        # do not matter for the integral.
        if m < s:
            f = lambda x: step_spline(n, j, x)
        else:
            f = lambda x: F(1) - step_spline(n, j, x)
        total += (b-a) * (f(a) + 4*f(m) + f(b)) / 6
    return total


def nodes(n):
    t=knots(n)
    return [(t[i+1]+t[i+2])/2 for i in range(n+2)]


def check():
    count = 0
    for n in range(2, 22):
        h=F(1,n); xi=nodes(n)
        assert len(xi) == n+2 and xi[0] == 0 and xi[-1] == 1
        for j in range(1,n+2):
            # right-continuous step is sampled from nodes >= s
            left,right=xi[j-1],xi[j]
            for k in (1,2,3,4,5,6):
                s=left+(right-left)*F(k,7)
                e=integral_step_error(n,j,s)
                assert e < F(13,24)*h,(n,j,s,e)
                count += 1
            if 2 <= j <= n:
                a = knots(n)[j]
                for k in range(1, 24):
                    x = a + 2*h*F(k,24)
                    if x <= a+h:
                        predicted = (x-a)**2/(2*h*h)
                    else:
                        predicted = 1 - (a+2*h-x)**2/(2*h*h)
                    assert step_spline(n,j,x) == predicted, (n,j,x)
                e=integral_step_error(n,j,xi[j]); assert e == F(13,24)*h,(n,j,e)
                count += 1
            elif j==1:
                assert integral_step_error(n,j,xi[j]) == h/4
            else:
                # j=n+1 at s=1 is a forbidden endpoint jump.
                assert integral_step_error(n,j,(left+right)/2) < h/3
        # Test B-spline partition and affine reproduction at rational points.
        for k in range(1,29):
            x=F(k,29); w=basis(n,x)
            assert sum(w)==1,(n,x,sum(w))
            assert sum(a*b for a,b in zip(w,xi))==x,(n,x)
    print('EXACT_RATIONAL_STEP_BOUNDS_PASS',count)
    print('EXACT_INTERIOR_QUADRATIC_RESPONSE_PASS')
    print('EXACT_EXTREMAL_NODES_AND_AFFINE_REPRODUCTION_PASS',20)
    print('QUADRATIC_SCHOENBERG_BV_L1_CHECKS_PASS')


if __name__=='__main__':
    check()
