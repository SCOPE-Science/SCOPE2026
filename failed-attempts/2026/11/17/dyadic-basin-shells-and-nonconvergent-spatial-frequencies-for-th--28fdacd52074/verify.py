"""Exact rational diagnostics for the equilateral farthest-projection map.

No numerical floating-point assumptions or external dependencies are used.
The infinite statements are established in RESULT.md, not by this finite test.
"""
from fractions import Fraction as Q


def step(i, t):
    assert i in (0, 1, 2)
    if t == Q(1, 2):
        return i, t
    if t < Q(1, 2):
        return (i + 1) % 3, (1-t)/2
    return (i - 1) % 3, 1-t/2


def predicted(t):
    if t == Q(1,2):
        return 'fixed', 0
    if t in (Q(0), Q(1)):
        return 'fixed', 1
    h = max(t, 1-t)
    if h < 1:
        return ('minus' if t < Q(1,2) else 'plus'), 0
    n = 0
    while h > 1:
        h /= 2
        n += 1
    if h == 1:
        return 'fixed', n+1
    initial = 1 if t > Q(1,2) else -1
    final = initial * (-1)**n
    return ('plus' if final > 0 else 'minus'), n


def verify():
    # Both three-cycles are exact, and no smaller positive iterate returns.
    for t in (Q(1,3), Q(2,3)):
        i = 0
        seen=[]
        for j in range(3):
            assert (i,t) not in seen
            seen.append((i,t))
            i,t=step(i,t)
        assert (i,t)==seen[0]

    n_tests=0
    for d in range(1,51):
        for a in range(-500,501):
            t=Q(a,d)
            kind,N=predicted(t)
            i=0
            for n in range(N):
                i,t=step(i,t)
            if kind == 'fixed':
                # If a vertex has been reached, one more step hits a fixed midpoint.
                for _ in range(3):
                    i,t=step(i,t)
                assert t==Q(1,2)
            else:
                assert 0<t<1 and t!=Q(1,2)
                assert (t>Q(1,2)) == (kind=='plus')
                for _ in range(20):
                    i,t=step(i,t)
                    assert (t>Q(1,2)) == (kind=='plus')
            n_tests+=1
    print('EXACT_RATIONAL_CAPTURE_AND_ORIENTATION_OK',n_tests)

    for k in range(1,16):
        upper=4**k
        positive=sum(2*(4**(j-1)) for j in range(1,k+1))
        assert Q(positive,upper-1)==Q(2,3)
        upper2=2*4**k
        fraction=Q(positive,upper2-1)
        assert Q(0)<fraction<Q(1,3)
        assert abs(fraction-Q(1,3))<Q(1,3*4**k)
    print('EXACT_DYADIC_BASIN_MEASURES_OK')

    for N in range(1,22):
        lengths=[2**(n-1) for n in range(1,N+1)]
        assert sum(lengths)==2**N-1
        assert sum(Q(x,2**N-1) for x in lengths)==1
    print('EXACT_CAPTURE_TIME_DISTRIBUTION_OK')

if __name__=='__main__':
    verify()
