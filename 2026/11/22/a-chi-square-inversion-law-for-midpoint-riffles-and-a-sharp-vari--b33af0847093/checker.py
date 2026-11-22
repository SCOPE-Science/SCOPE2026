"""Exact finite checks for the one-step inversion-law theorem.
No external dependencies. Finite checks complement, rather than prove, the all-n statements.
"""
from fractions import Fraction
from math import comb, gcd
from collections import Counter
from itertools import product

checks = 0

def verify(ok, message=''):
    global checks
    assert ok, message
    checks += 1


def tie_count(n, k):
    if k in (0, n):
        return 0
    g = gcd(k, n-k)
    return g if (k // g) % 2 and ((n-k) // g) % 2 else 0


def conditional_inversions(n, k):
    if k in (0, n):
        return Counter({0: 1})
    rows = [(Fraction(2*i-1, 2*k), 'A', i) for i in range(1,k+1)]
    rows += [(Fraction(2*j-1, 2*(n-k)), 'B', k+j) for j in range(1,n-k+1)]
    coordinates = sorted(set(x[0] for x in rows))
    fixed = []
    tied = []
    for coord in coordinates:
        cards = [x for x in rows if x[0] == coord]
        if len(cards) == 1:
            fixed.append([cards[0][2]])
        else:
            verify(len(cards) == 2 and set(x[1] for x in cards) == {'A','B'}, 'bad tie')
            tied.append(len(fixed))
            fixed.append([x[2] for x in cards])
    histogram = Counter()
    for bits in product((0,1), repeat=len(tied)):
        tie_dir = dict(zip(tied,bits))
        output = []
        for j, cards in enumerate(fixed):
            output.extend(cards if j not in tie_dir or tie_dir[j] == 0 else cards[::-1])
        inv = sum(output[i] > output[j] for i in range(n) for j in range(i+1,n))
        histogram[inv] += 1
    return histogram

for n in range(2, 17):
    midpoint_num = Counter()
    moment1 = Fraction(0)
    moment2 = Fraction(0)
    for k in range(n+1):
        h = conditional_inversions(n, k)
        t = tie_count(n,k)
        verify(sum(h.values()) == 2**t, ('coin count',n,k))
        base = (k*(n-k)-t)//2
        expected = Counter({base+j:comb(t,j) for j in range(t+1)})
        verify(h == expected, ('law',n,k,h,expected))
        q = Fraction(comb(n,k),2**n)
        for inv,count in h.items():
            weight = q*Fraction(count,2**t)
            moment1 += weight*inv
            moment2 += weight*inv*inv
            midpoint_num[inv] += Fraction(comb(n,k)*count,2**(n+t))
    verify(sum(midpoint_num.values())==1, ('normalization',n))
    verify(moment1 == Fraction(n*(n-1),8), ('mean',n))
    extra = sum(Fraction(comb(n,k)*tie_count(n,k),2**n) for k in range(n+1))/4
    verify(moment2-moment1**2 == Fraction(n*(n-1),32)+extra, ('var',n))
    if n % 2:
        expected = Counter({Fraction(k*(n-k),2):Fraction(comb(n,k),2**(n-1)) for k in range((n+1)//2)})
        verify(midpoint_num==expected, ('odd mass',n))

for n in range(2,14):
    mean=Fraction(0)
    mean2=Fraction(0)
    for bits in product((0,1), repeat=n):
        inv=sum(bits[i] == 1 and bits[j] == 0 for i in range(n) for j in range(i+1,n))
        mean += Fraction(inv,2**n)
        mean2 += Fraction(inv*inv,2**n)
    verify(mean==Fraction(n*(n-1),8), ('GSR mean',n))
    verify(mean2-mean**2==Fraction(n*(n-1)*(2*n+5),96), ('GSR variance',n))

print(f'PASS: {checks} exhaustive exact-arithmetic structural/moment assertions')
print('Notes: finite checks only; all-size proof and weak convergence are in RESULT.md.')
