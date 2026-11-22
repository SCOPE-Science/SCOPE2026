"""Exact small-size verification of the cycle-versus-first-defect inequality.
This checks finite instances; the all-size result follows from the proof in RESULT.md.
"""
from itertools import product
from fractions import Fraction

def cycle_count(word):
    n = len(word)
    rank = [0] * n
    for r, i in enumerate(sorted(range(n), key=lambda i: (word[i], i))):
        rank[i] = r
    seen = [False] * n
    count = 0
    for i in range(n):
        if not seen[i]:
            count += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = rank[j]
    return count

checks=0
for alphabet in (2,3,4):
    for n in range(1,9):
        for word in product(range(alphabet), repeat=n):
            j = next((i for i,c in enumerate(word) if c != 0), n)
            rare = sum(c != 0 for c in word)
            cycles = cycle_count(word)
            assert j <= cycles <= j+rare, (alphabet,word,cycles,j,rare)
            checks+=1

# Exact mean envelope under independent Bernoulli rare indicators;
# the rank of a rare label does not matter for the deterministic bound.
for n in range(1,9):
    for eps in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
        q = 1-eps
        expectation = Fraction(0)
        for word in product((0,1),repeat=n):
            r = sum(word)
            expectation += eps**r * q**(n-r) * cycle_count(word)
        j_mean = sum(q**i for i in range(1,n+1))
        assert j_mean <= expectation <= j_mean+n*eps
        checks += 2
print(f'PASS: {checks} exact checks')
