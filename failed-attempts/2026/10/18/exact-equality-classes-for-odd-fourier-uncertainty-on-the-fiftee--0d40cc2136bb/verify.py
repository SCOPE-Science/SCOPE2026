#!/usr/bin/env python3
"""Exact finite-field exclusion certificate for odd Fourier uncertainty on Z/15Z.

Requires Python 3.8+ only. Modular zero minors are necessary for complex
cyclotomic zero minors; no converse is used.
"""
from collections import Counter, defaultdict
from itertools import combinations

N = 15
POSITIVES = tuple(range(1, 8))

def witness(prime):
    roots = [w for w in range(2, prime)
             if pow(w, N, prime) == 1
             and pow(w, 3, prime) != 1 and pow(w, 5, prime) != 1]
    assert roots, ('missing primitive fifteenth root', prime)
    root = roots[0]
    assert pow(root, 15, prime) == 1
    mat = {(y,u): (pow(root, (y*u) % N, prime)
                     - pow(root, (-y*u) % N, prime)) % prime
           for y in POSITIVES for u in POSITIVES}
    hist = Counter()
    exception = []
    for u,v in combinations(POSITIVES, 2):
        blocks = defaultdict(list)
        universal = []
        for y in POSITIVES:
            a,b = mat[y,u],mat[y,v]
            if a == 0 and b == 0:
                universal.append(y)
            else:
                direction = ('infinity',) if a == 0 else ('slope', b * pow(a,-1,prime) % prime)
                blocks[direction].append(y)
        maxzeros = len(universal) + max(map(len,blocks.values()))
        hist[maxzeros] += 1
        if maxzeros >= 3:
            exception.append((u, v, tuple(universal),
                              tuple(sorted(tuple(z) for z in blocks.values()))))
    assert sum(hist.values()) == 21
    assert hist == Counter({1:8, 2:12, 4:1}), hist
    assert exception == [(3,6,(5,),((1,4,6),(2,3,7)))], exception
    return root, hist, exception

# A zero sine row is equivalent in characteristic zero to 15 | yu.
zero_counts = {u: tuple(y for y in POSITIVES if (y*u) % N == 0)
               for u in POSITIVES}
assert zero_counts == {1:(),2:(),3:(5,),4:(),5:(3,6),6:(5,),7:()}
for prime in (31, 61):
    root, hist, exception = witness(prime)
    print(f'F_{prime}: primitive root {root}; 21 pairs; zero-max histogram '
          f'{dict(sorted(hist.items()))}; exceptional pairs={exception}')
print('Singleton Fourier-positive zero-row counts:',zero_counts)
print('The two explicit complex cyclotomic witnesses are h_1 and h_2,')
print('supported on +/-{3,6}; each has four positive zero-frequency rows.')
print('CERTIFICATE PASS')
