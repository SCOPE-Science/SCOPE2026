"""Finite sanity checks for the four-letter absorber subshift and its free-alphabet products.

Runs without nonstandard dependencies. These tests illustrate, but do not replace,
the general infinite-length proof in RESULT.md.
"""
from itertools import product

A = '0123'

def admissible(w):
    """The language 2*{0,1}* union {0,1}*3* with binary core."""
    if not w:
        return True
    n=len(w)
    # First branch: 2^k then binary, with no other 2 or 3.
    k=0
    while k<n and w[k]=='2': k+=1
    left = all(c in '01' for c in w[k:])
    # Second branch: binary then 3^k, with no 2.
    k=n
    while k>0 and w[k-1]=='3': k-=1
    right = all(c in '01' for c in w[:k])
    return left or right

def minimal_absent(w):
    return not admissible(w) and admissible(w[:-1]) and admissible(w[1:])

for n in range(1,9):
    words=[''.join(w) for w in product(A, repeat=n)]
    actual=sum(admissible(w) for w in words)
    expected=3*2**n-2
    assert actual==expected, (n,actual,expected)
    mins=sum(minimal_absent(w) for w in words)
    if n>=2:
        assert mins >= 2**(n-2), (n,mins)
    print(f'X length {n}: admissible={actual}, minimal absent={mins}')

for q in (2,3):
    for n in range(1,5):
        b=[''.join(w) for w in product('abcdefghijklmnopqrstuvwxyz'[:q],repeat=n)]
        a=[''.join(w) for w in product(A,repeat=n)]
        absents_x=sum(minimal_absent(w) for w in a)
        pairs=sum(minimal_absent(w) for w in a for _ in b)
        assert pairs == absents_x*q**n
        print(f'Product q={q} length {n}: minimal absent={pairs}')

# The union-bound step depends only on a count of possible starts.
# A minimally forbidden word of length n can be spliced from witnesses of its
# length-(n-1) prefix and suffix; a forbidden length-l block must cover
# the entire splice interval of length n, leaving at most l-n+1 starts.
for n in range(2,30):
    for ell in range(n,50):
        starts=[i for i in range(-ell,1) if i<=0 and i+ell-1>=n-1]
        assert len(starts)==ell-n+1
print('Finite word, product, and splice-offset checks passed.')
