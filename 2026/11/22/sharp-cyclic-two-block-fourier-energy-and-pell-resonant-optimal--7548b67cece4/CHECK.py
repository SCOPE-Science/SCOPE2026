"""Direct exact checks of two-block cyclic Fourier fourth-moment design.

Python 3 standard library only. This script checks finite instances; the
universal assertions are established by the proof in RESULT.md.
"""
from math import isqrt


def direct_energy(n: int, a: int, s: int) -> int:
    """Count ordered two-sums directly, without the overlap formula."""
    assert a >= 2 and n >= 2*a and a <= s <= n-a
    blocks = list(range(a)) + list(range(s, s+a))
    assert len(set(x % n for x in blocks)) == 2*a
    histogram = [0] * n
    for x in blocks:
        for y in blocks:
            histogram[(x+y) % n] += 1
    return sum(r*r for r in histogram)


def B(m: int) -> int:
    return m*(m+1)*(m+2)//6


def predicted_near(a: int, t: int):
    assert 0 <= t <= a
    L = 2*a-1
    F = [8*B(u)+2*B(t-2*u) for u in range(t//2+1)]
    minimum = min(F)
    u_best = {u for u, v in enumerate(F) if v == minimum}
    return 4*a**3+2*a+minimum, {L-u for u in u_best}


def prediction_closed(t: int):
    """Exact selected minimizers using integer square/root comparisons."""
    vals = [8*B(u)+2*B(t-2*u) for u in range(t//2+1)]
    m = min(vals)
    return {u for u, v in enumerate(vals) if v == m}


def test_all():
    cases = 0
    for a in range(2, 14):
        L = 2*a-1
        for n in range(2*a, 4*L+1):
            results = {s: direct_energy(n, a, s)
                       for s in range(a, n-a+1)}
            actual = min(results.values())
            optimal = {min(s,n-s) for s, v in results.items() if v == actual}
            if n >= 3*L:
                assert actual == 4*a**3+2*a
                assert optimal == set(range(L, (n-L)//2+1))
            elif n >= 3*L-a:
                target, optimal_target = predicted_near(a, 3*L-n)
                assert (actual, optimal) == (target, optimal_target)
            else:
                assert actual > 4*a**3+2*a
            cases += 1
    assert cases == 504, cases

    # Separate family near a large Pell tie (avoids expensive full enumeration).
    for t in range(0, 500):
        minima = prediction_closed(t)
        # Exact finite differences; a tie is a negative-Pell solution.
        w = isqrt(2*(t+3)**2 - 1)
        pell = w*w == 2*(t+3)**2-1
        assert (len(minima) == 2) == pell
        if len(minima) == 2:
            left, right = sorted(minima)
            assert right == left+1
            assert w*w - 2*(t+3)**2 == -1
        if t >= 2:
            r = t+1.5-0.5*(2*(t+3)**2-1)**0.5
            if not pell:
                assert len(minima) == 1
                assert abs(next(iter(minima)) - r) < 1.01
    assert prediction_closed(2) == {0, 1}
    assert prediction_closed(26) == {7, 8}
    assert prediction_closed(166) == {48, 49}
    for a,t in ((26,26),(166,166)):
        L=2*a-1
        n=3*L-t
        energy, optimal = predicted_near(a,t)
        for s in optimal:
            assert direct_energy(n,a,s)==energy
        for s in range(min(optimal)-1,max(optimal)+2):
            if s not in optimal and s>=a:
                assert direct_energy(n,a,s)>energy
    print("PASS: two larger Pell ties verified by direct convolution and adjacent competitors")
    print("PASS: 504 exhaustive (n,a) cases with direct ordered two-sum counts")
    print("PASS: 500 independent exact tie/Pell checks and three named ties")
    print("Note: finite tests do not prove the universal theorem.")


if __name__ == "__main__":
    test_all()
