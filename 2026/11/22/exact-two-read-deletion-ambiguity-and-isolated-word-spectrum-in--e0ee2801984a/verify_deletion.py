#!/usr/bin/env python3
"""Independent direct channel enumerator for finite two-read ambiguity graphs."""
from itertools import product


def words(n):
    return [''.join(bits) for bits in product('01', repeat=n)
            if '010' not in ''.join(bits)]


def ball(word):
    return {word[:j] + word[j+1:] for j in range(len(word))}


def swap_neighbors(word):
    result = set()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            other = word[:j] + word[j+1] + word[j] + word[j+2:]
            if '010' not in other:
                result.add(other)
    return result


def count_formula(n):
    a = [1, 2, 4]
    for j in range(3, n+1):
        a.append(2*a[-1] - a[-2] + a[-3])
    u = [1]
    for j in range(1, n+1):
        u.append(1 if j == 1 else a[j-2])
    return sum(u[i]*u[n-2-i] for i in range(n-1)) if n >= 2 else 0


def main():
    for n in range(1, 14):
        vs = words(n)
        b = {w:ball(w) for w in vs}
        expected = {tuple(sorted((w, u))) for w in vs for u in swap_neighbors(w)}
        actual = set()
        for i, w in enumerate(vs):
            for u in vs[i+1:]:
                if len(b[w] & b[u]) >= 2:
                    actual.add((w,u))
        assert actual == expected, (n, sorted(actual ^ expected)[:5])
        assert len(actual) == count_formula(n), (n, len(actual), count_formula(n))
        print('direct',n,len(vs),len(actual))
    print('VERIFY_DIRECT_OK')

if __name__=='__main__': main()
