"""Exact finite consistency checks for a binary-partition three-square gap law.

Run with Python 3.10 or newer: python verify_gap_law.py
The finite tests support, but do not prove, the infinite asymptotic theorem.
"""
from collections import Counter
from fractions import Fraction

GAPS = (6, 8, 10, 16, 18, 24)
P = dict(zip(GAPS, (Fraction(1,4),Fraction(1,4),Fraction(1,16),Fraction(3,16),Fraction(3,16),Fraction(1,16))))
TYPES = {'A':(0,10), 'E':(2,8), 'F':(2,), 'G':(10,)}
TRANS = {('A','F'):Fraction(1,12), ('E','G'):Fraction(1,4),
         ('F','E'):Fraction(1,6), ('F','G'):Fraction(1,12),
         ('G','A'):Fraction(1,12), ('G','E'):Fraction(1,12),
         ('G','F'):Fraction(1,6), ('G','G'):Fraction(1,12)}

def tm(n):
    assert n >= 0
    return n.bit_count() % 2

def chi_explicit(n):
    if n <= 0:
        return 0
    v = (n & -n).bit_length() - 1
    if v % 2 == 0:
        return 0
    h = n >> v
    if h % 4 != 1:
        return 0
    return tm((h-1)//4)

def chi_rec(n):
    if n == 0: return 0
    if n & 1: return 0
    if n % 4 == 0: return chi_rec(n//4)
    if n % 8 == 6: return 0
    return tm(n//8)  # n = 8m+2

def typ(n):
    if chi_explicit(n): return 'A'
    if tm(n): return 'E' if n%2==0 else 'F'
    return 'G'

def binary_partitions(limit):
    # b(0)=1, b(2m+1)=b(2m), b(2m)=b(2m-1)+b(m).
    b=[1]*(limit+1)
    for n in range(2,limit+1):
        b[n]=b[n-1] + (b[n//2] if n%2==0 else 0)
    return b

def excluded_three_squares(v):
    while v%4 == 0: v//=4
    return v%8 == 7

def check():
    # Full independent partition recurrence and Legendre criterion.
    small=4096
    parts=binary_partitions(2*small)
    for n in range(small+1):
        expected=int(excluded_three_squares(parts[2*n]))
        assert expected == chi_explicit(n) == chi_rec(n), (n,expected)
    blocks=1<<16
    for n in range(blocks+2):
        actual=tuple(i for i in range(16) if chi_rec(16*n+i))
        assert actual == TYPES[typ(n)], (n,actual,typ(n))
    observed_transition=Counter((typ(n),typ(n+1)) for n in range(blocks))
    assert set(observed_transition)==set(TRANS)
    for pair,p in TRANS.items():
        assert abs(observed_transition[pair]-p*blocks)<32, (pair,observed_transition[pair],p*blocks)
    # Enumerate true exceptional indices past final boundary for all intervening gaps.
    bound=16*blocks
    exceptional=(n for n in range(bound+64) if chi_explicit(n))
    previous=next(exceptional)
    gap_counts=Counter()
    total=0
    for nxt in exceptional:
        if previous>=bound: break
        gap=nxt-previous
        assert gap in GAPS, (previous,nxt)
        gap_counts[gap]+=1
        total+=1
        previous=nxt
    assert abs(total-Fraction(bound,12))<32
    for gap in GAPS:
        assert abs(gap_counts[gap]-P[gap]*total)<64,(gap,gap_counts[gap],P[gap]*total)
    print('VERIFY_OK independent_partitions=',small+1,
          'block_cases=',blocks+2,
          'transitions=',sum(observed_transition.values()),
          'enumerated_gaps=',total,
          'gap_counts=',dict(sorted(gap_counts.items())),
          'finite_rational_checks=passed')

if __name__=='__main__':check()
