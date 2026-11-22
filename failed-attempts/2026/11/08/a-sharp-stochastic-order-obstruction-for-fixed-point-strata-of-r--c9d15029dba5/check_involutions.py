"""Direct finite verification of the two-fixed-point descent comparison.

Run with Python 3 standard library: python check_involutions.py
The infinite claim is proved in RESULT.md; enumerations are diagnostics only.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import factorial


def involutions(n):
    p = list(range(n))
    def visit(available):
        if not available:
            yield tuple(p)
            return
        a = available[0]
        p[a] = a
        yield from visit(available[1:])
        for b in available[1:]:
            p[a] = b
            p[b] = a
            yield from visit([c for c in available[1:] if c != b])
    yield from visit(list(range(n)))


def class_size(n, f):
    m = n - f
    assert 0 <= f <= n and m % 2 == 0
    return factorial(n) // (factorial(f) * (2 ** (m // 2)) * factorial(m // 2))


def one_descent_block(n, a, r):
    assert r >= 1 and 0 <= a <= n - 2*r
    p = list(range(n))
    for j in range(r):
        p[a+j] = a+r+j
        p[a+r+j] = a+j
    return tuple(p)


def cdf(hist, k):
    return Fraction(sum(v for d, v in hist.items() if d <= k), sum(hist.values()))


assertions = 0

def check(test, message):
    global assertions
    assertions += 1
    if not test:
        raise AssertionError(message)

for n in range(2, 13):
    classes = defaultdict(Counter)
    one_descent = defaultdict(set)
    total = 0
    for p in involutions(n):
        total += 1
        f = sum(p[i] == i for i in range(n))
        desc = sum(p[i] > p[i+1] for i in range(n-1))
        classes[f][desc] += 1
        if desc == 1:
            one_descent[f].add(p)
    for f, hist in sorted(classes.items()):
        check(sum(hist.values()) == class_size(n, f), f'class cardinality {n,f}')
        expected = Fraction(n*n-f*f, 2*n)
        observed = Fraction(sum(d*c for d,c in hist.items()), sum(hist.values()))
        check(observed == expected, f'conditional mean {n,f}')
        if f < n:
            check(hist[1] == f+1, f'one-descent count {n,f}')
            r = (n-f)//2
            explicitly = set(one_descent_block(n,a,r) for a in range(f+1))
            check(explicitly == one_descent[f], f'one-descent classification {n,f}')
        else:
            check(hist == {0:1}, f'identity class {n}')
    if n % 2 == 0:
        nofix, twofix = classes[0], classes[2]
        if n in (2,4,6):
            check(all(cdf(nofix,k) <= cdf(twofix,k) for k in range(n)), f'small n stochastic dominance {n}')
        if n >= 8:
            check(cdf(nofix,1) > cdf(twofix,1), f'lower-tail inversion {n}')
            check(Fraction(sum(d*c for d,c in nofix.items()), sum(nofix.values())) >
                  Fraction(sum(d*c for d,c in twofix.items()),sum(twofix.values())),
                  f'expected descent larger {n}')
            check(any(cdf(nofix,k)<cdf(twofix,k) for k in range(n)), f'CDF crossing {n}')
    print('n=%d complete involutions=%d fixed point strata=%d' % (n,total,len(classes)))

for n in range(4, 100):
    for f in range(0,n-3):
        if (n-f) % 2:
            continue
        m=n-f
        a=Fraction(f+1,class_size(n,f))
        b=Fraction(f+3,class_size(n,f+2))
        check((a>b) == (m>(f+2)*(f+3)), f'quadratic one-descent boundary {n,f}')
        mean_a=Fraction(n*n-f*f,2*n)
        mean_b=Fraction(n*n-(f+2)**2,2*n)
        check(mean_a>mean_b, f'mean ordering {n,f}')

print('PASS:', assertions, 'exact assertions')
