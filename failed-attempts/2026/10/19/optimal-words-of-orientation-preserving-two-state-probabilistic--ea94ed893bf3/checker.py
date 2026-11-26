"""Exact-rational tests for monotone two-state stochastic witnesses.

The mathematical proof covers all lengths. This program checks finite instances,
computes transition matrices, and tests the unique maximum directly.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def has_single_runs(word):
    last = None
    seen = set()
    for letter in word:
        if letter != last:
            if letter in seen:
                return False
            seen.add(letter)
        last = letter
    return True


def construct(word, alphabet):
    n = len(word)
    runs = []
    for a in word:
        if not runs or runs[-1][0] != a:
            runs.append([a, 1])
        else:
            runs[-1][1] += 1
    r = len(runs)
    assert n >= 1 and has_single_runs(word)
    eps = F(1, (2 ** (n + 4)) * r)
    accum = 0
    crossings = []
    for a, mult in runs[:-1]:
        accum += mult
        xprev = F(1, 2) * (1 - F(1, 2 ** (accum - 1)))
        xcurr = F(1, 2) * (1 - F(1, 2 ** accum))
        crossings.append((xprev + xcurr) / 2)
    mp = {}
    s = F(0)
    for i, (letter, mult) in enumerate(runs):
        slope = F(1, 2) + i * eps
        intercept = F(1, 4) - s * eps
        assert 0 < slope < 1 and 0 < intercept and slope + intercept < 1
        mp[letter] = (slope, intercept)
        if i < r - 1:
            s += crossings[i]
    for letter in alphabet:
        if letter not in mp:
            mp[letter] = (F(1, 2), F(0))
    assert all(0 <= b <= 1 and 0 <= a + b <= 1 for a,b in mp.values())
    common_denominator = r * (2 ** (2*n+5))
    assert all((common_denominator*entry).denominator == 1
               for slope,intercept in mp.values()
               for row in transition(slope,intercept) for entry in row)
    return mp


def transition(slope, intercept):
    a, b = slope, intercept
    return ((a + b, 1 - a - b), (b, 1 - b))


def matrix_score(word, mp):
    # Direct stochastic-matrix multiplication in exact rational arithmetic.
    p0, p1 = F(0), F(1)
    for letter in word:
        ((u, v), (x, y)) = transition(*mp[letter])
        p0, p1 = p0 * u + p1 * x, p0 * v + p1 * y
        assert p0 + p1 == 1
    return p0


def score(word, mp):
    p = F(0)
    for letter in word:
        a, b = mp[letter]
        p = a * p + b
    return p


def verify_one(word, alphabet):
    mp = construct(word, alphabet)
    values = sorted(((score(z,mp),z) for z in product(alphabet,repeat=len(word))), reverse=True)
    assert values[0][1] == word and values[0][0] > values[1][0], (word,values[:2])
    assert matrix_score(word,mp) == values[0][0]
    assert matrix_score(values[1][1],mp) == values[1][0]
    return values[0][0] - values[1][0]


def verify():
    total = 0
    min_gap = F(1)
    for q in (2, 3, 4):
        alpha = tuple(range(q))
        for n in range(1, 6 if q < 4 else 5):
            expected = sum(factorial(q)//factorial(q-r)*comb(n-1,r-1)
                           for r in range(1,min(q,n)+1))
            good = [w for w in product(alpha,repeat=n) if has_single_runs(w)]
            assert len(good)==expected, (q,n,len(good),expected)
            for w in good:
                gap = verify_one(w,alpha)
                min_gap = min(min_gap,gap)
                total += 1
            print(f'alphabet={q} length={n} run-distinct={expected} verified={len(good)}')
    # Check a representative with all five distinct letters and nontrivial blocks.
    word = (0,0,1,1,2,3,4)
    gap=verify_one(word, tuple(range(5)))
    print('five-distinct-letter witness:', ''.join(map(str,word)), 'gap=',str(gap))
    # Necessity sanity-check on rational orientation-preserving maps.
    from random import Random
    rnd=Random(13)
    for q in (2, 3, 4):
        for _ in range(120):
            maps={a:(F(rnd.randrange(0,6),10),F(rnd.randrange(0,5),10)) for a in range(q)}
            for n in range(1,7):
                scored=sorted((score(w,maps),w) for w in product(range(q),repeat=n))
                if len(scored)>1 and scored[-1][0]>scored[-2][0]:
                    assert has_single_runs(scored[-1][1]),(maps,n,scored[-1])
    print('grid necessity checks: PASS')
    print('total exact exhaustive rational checks:',total+1)
    print('smallest gap on grid:',str(min_gap))
    print('PASS')

if __name__=='__main__':
    verify()
