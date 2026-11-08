"""Exact finite checks for randomized zero forcing on K_{a,2}.

Run: python check.py . Uses only the Python standard library.
Tests finite identities; it is not a proof of convergence.
"""
from fractions import Fraction
from math import comb


def advance(a, states):
    out = {}
    for (i, j), m in states.items():
        pa, pb = Fraction(j, 2), Fraction(i, a)
        for da in range(a - i + 1):
            wa = Fraction(comb(a - i, da)) * pa**da * (1 - pa)**(a - i - da)
            if wa == 0:
                continue
            for db in range(3 - j):
                wb = Fraction(comb(2 - j, db)) * pb**db * (1 - pb)**(2 - j - db)
                if wb:
                    key = (i + da, j + db)
                    out[key] = out.get(key, Fraction(0)) + m * wa * wb
    assert sum(out.values(), Fraction(0)) == 1
    return out


def small_first_stage(a, t):
    # White-vertex process while the second hub remains white.
    m = {a: Fraction(1)}
    for _ in range(t):
        out = {}
        for w, p in m.items():
            for w2 in range(w + 1):
                z = p * Fraction(w, a) * Fraction(comb(w, w2), 2**w)
                out[w2] = out.get(w2, Fraction()) + z
        m = out
    return sum(m.values(), Fraction())


def partitions(a):
    if not a:
        yield ()
        return
    z, rest = a[0], a[1:]
    for p in partitions(rest):
        yield (frozenset({z}),) + p
        for j in range(len(p)):
            yield p[:j] + (p[j] | {z},) + p[j+1:]


def finite_formula(a, t):
    if t == 0:
        return Fraction(1)
    ans = Fraction(0)
    for p in partitions(tuple(range(1, t))):
        k = len(p)
        ff = 1
        for h in range(k):
            ff *= a - h
        ans += Fraction(ff, 2**sum(max(block) for block in p))
    return ans / a**(t-1)


def run():
    tests = 0
    for a in range(2, 9):
        d = {(0,1):Fraction(1)}
        e = {(1,0):Fraction(1)}
        first = Fraction(1)
        for t in range(7):
            first = small_first_stage(a,t)
            assert first == finite_formula(a,t)
            assert first == sum(p for (i,j),p in d.items() if j == 1)
            tests += 2
            if t >= 1:
                tail = sum(p for (i,j),p in d.items() if i != a or j != 2)
                assert first <= tail <= small_first_stage(a,t-1)
                tests += 1
            missing = sum(p for (i,j),p in e.items() if j == 0)
            q = Fraction(2,a)-Fraction(1,a*a)
            assert missing == (1-q)**t
            tests += 1
            d, e = advance(a,d), advance(a,e)
        assert finite_formula(a,3)==Fraction(1,8)+Fraction(1,8*a)
        tests += 1
    assert abs(sum(2.0**(-t*(t-1)/2) for t in range(30))+1-3.641632560655154)<1e-12
    tests += 1
    for a in (20,40,80):
        for t in (2,3,4,5):
            z = small_first_stage(a,t)
            assert abs(float(z)-2.0**(-t*(t-1)/2)) <= t*(t-1)/(2*a)
            tests += 1
    print(f'PASS: {tests} assertions; exact finite-state/partition identities and finite-size diagnostics.')

if __name__ == '__main__':
    run()
