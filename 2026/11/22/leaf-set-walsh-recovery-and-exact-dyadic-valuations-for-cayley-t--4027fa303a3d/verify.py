"""Exact checks of the labelled-tree leaf-profile Walsh multiplier formula.

Standard-library-only script. All comparisons are integer exact.
The bounded checks are supplementary to the all-order proof in RESULT.md.
"""
from itertools import product
from math import comb, factorial, gcd

checks = 0

def check(test, note):
    global checks
    checks += 1
    if not test:
        raise AssertionError(note)


def valuation2(x):
    assert x != 0
    a = abs(x)
    return (a & -a).bit_length() - 1


def stirling2(m):
    arr = [0] * (m+1)
    arr[0] = 1
    for i in range(1,m+1):
        cur = [0] * (m+1)
        for j in range(1,i+1):
            cur[j] = arr[j-1] + j * arr[j]
        arr = cur
    return arr


def from_inclusion_exclusion(n,k):
    return sum(comb(k,j)*(-2)**j*(n-j)**(n-2) for j in range(k+1))


def from_leaf_counts(n,k,stirling):
    # Exactly r leaves: multiplicity (n-r)! S(n-2,n-r) per r-set.
    total = 0
    for r in range(n+1):
        h = n-r
        if h > n-2: continue
        weight = factorial(h) * stirling[h]
        for j in range(max(0,r-(n-k)),min(k,r)+1):
            total += weight * (-1)**j * comb(k,j) * comb(n-k,r-j)
    return total


def fwht(data):
    a = data[:]
    h = 1
    while h < len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v = a[j],a[j+h]
                a[j] = u+v
                a[j+h] = u-v
        h *= 2
    return a


# Three independent constructions: direct Pruefer sequences, Stirling
# multiplicities, and the inclusion-exclusion multiplier formula.
for n in range(2,9):
    brute = [0] * (1<<n)
    for word in product(range(n),repeat=n-2):
        present = 0
        for x in word:
            present |= 1<<x
        brute[((1<<n)-1)^present] += 1
    s = stirling2(n-2)
    f = [factorial(n-mask.bit_count())*s[n-mask.bit_count()] if n-mask.bit_count()<=n-2 else 0 for mask in range(1<<n)]
    for mask in range(1<<n):
        check(f[mask] == brute[mask],f'leaf-mask count n={n}, mask={mask}')
    transform = fwht(brute)
    for mask in range(1<<n):
        check(transform[mask] == from_inclusion_exclusion(n,mask.bit_count()),f'Walsh n={n}, mask={mask}')
    check(sum(brute)==n**(n-2),f'Cayley total n={n}')

# Separate symbolic combinatorial transform and exact arithmetic checks.
for n in range(2,35):
    s = stirling2(n-2)
    for k in range(n+1):
        check(from_leaf_counts(n,k,s)==from_inclusion_exclusion(n,k),f'Krawtchouk n={n},k={k}')

for n in range(2,129):
    arr = [from_inclusion_exclusion(n,k) for k in range(n+1)]
    for k,x in enumerate(arr):
        check(x!=0,f'nonzero n={n},k={k}')
        if n%2 or n==2:
            check(valuation2(x)==0,f'odd order valuation n={n},k={k}')
        elif k==0:
            check(valuation2(x)==(n-2)*valuation2(n),f'zero character valuation n={n}')
        else:
            check(valuation2(x)==1+valuation2(k),f'nontrivial character valuation n={n},k={k}')
    g=0
    for x in arr:
        g=gcd(g,x)
    check(g==(2 if n%2==0 and n>=4 else 1),f'Walsh gcd n={n}')

print(f'PASS: {checks:,} exact assertions; direct codes n<=8; Stirling and Walsh transforms n<=34; valuations n<=128.')
