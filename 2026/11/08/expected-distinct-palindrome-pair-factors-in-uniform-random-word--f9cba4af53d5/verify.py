"""Finite checks for counting two-palindrome words and the uniform occurrence bound.

All infinite-length statements in the accompanying proof are established symbolically;
these exhaustive tests only cross-check the finite combinatorial primitives.
"""
from itertools import product
from fractions import Fraction


def pal(w):
    return w == w[::-1]


def cuts(w):
    return [j for j in range(len(w)) if pal(w[:j]) and pal(w[j:])]


def primitive(w):
    return all(w != w[:d] * (len(w) // d)
               for d in range(1, len(w)) if len(w) % d == 0)


def verify_language():
    for q, lengths in [(2, [3, 5, 7, 9, 11]), (3, [3, 5, 7, 9])]:
        for m in lengths:
            words = [w for w in product(range(q), repeat=m) if cuts(w)]
            primitive_words = [w for w in words if primitive(w)]
            assert all(len(cuts(w)) == 1 for w in primitive_words)
            for j in range(m):
                assert sum(pal(w[:j]) and pal(w[j:]) for w in product(range(q), repeat=m)) == q ** ((m+1)//2)
            assert len(primitive_words) <= len(words)
            print(f"LANGUAGE q={q} m={m} all={len(words)} primitive={len(primitive_words)}")


def verify_occurrences():
    for q in (2, 3):
        for m in range(1, 5):
            for n in range(m, m+4):
                denom = q ** n
                for w in product(range(q), repeat=m):
                    count = 0
                    for text in product(range(q), repeat=n):
                        if any(text[i:i+m] == w for i in range(n-m+1)):
                            count += 1
                    actual = Fraction(count, denom)
                    mu = Fraction(n-m+1, q**m)
                    lower = mu / (mu + 1 + Fraction(2, q-1))
                    upper = min(Fraction(1), Fraction(n, q**m))
                    assert lower <= actual <= upper, (q,m,n,w,actual,lower,upper)
    print("OCCURRENCES finite uniform probability inequalities verified")


if __name__ == '__main__':
    verify_language()
    verify_occurrences()
    print('PASS: all finite cross-checks')
