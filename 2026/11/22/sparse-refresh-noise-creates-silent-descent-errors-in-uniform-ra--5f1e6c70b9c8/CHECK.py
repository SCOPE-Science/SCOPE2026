"""Exact finite validation for coordinate-refresh descent statistics.

Use independent uniform relative ranks of all original and replacement scores;
no Monte Carlo or floating-point assertions appear in the checks.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def exact_case(n, a, b):
    """p=a/b, enumerate (2n)! orders and all 2^n masks exactly."""
    counts = {'D': 0, 'Dprime': 0, 'DDprime': 0, 'delta2': 0, 'H': 0}
    denom = factorial(2*n) * b**n
    for ranks in permutations(range(2*n)):
        x, u = ranks[:n], ranks[n:]
        d = sum(x[i] > x[i+1] for i in range(n-1))
        for mask in range(1<<n):
            nref = mask.bit_count()
            w = a**nref * (b-a)**(n-nref)
            if w == 0:
                continue
            y = [u[i] if mask & (1<<i) else x[i] for i in range(n)]
            dprime = sum(y[i] > y[i+1] for i in range(n-1))
            h = sum((x[i]>x[i+1]) != (y[i]>y[i+1]) for i in range(n-1))
            counts['D'] += w*d
            counts['Dprime'] += w*dprime
            counts['DDprime'] += w*d*dprime
            counts['delta2'] += w*(dprime-d)**2
            counts['H'] += w*h
    return {k:Fraction(v,denom) for k,v in counts.items()}


def test_exact():
    assertions = 0
    for n in range(2,5):
        for a,b in [(0,1),(1,3),(1,2),(1,1)]:
            p = Fraction(a,b)
            got = exact_case(n,a,b)
            assert got['D'] == got['Dprime'] == Fraction(n-1,2)
            assertions+=1
            cov = got['DDprime'] - got['D']*got['Dprime']
            assert cov == (1-p)*((n+1)-(n-1)*p)/12
            assertions+=1
            assert got['delta2'] == p*(2*n-(n-1)*p)/6
            assertions+=1
            assert got['H'] == (n-1)*(2*p/3-p*p/6)
            assertions+=1
    # One isolated interior refresh. Enumerate four independent ranks
    # (left neighbor, old center, right neighbor, new center).
    counter = {(0,0):0,(1,1):0,(-1,1):0,(0,2):0}
    for left,x,right,u in permutations(range(4)):
        old = int(left>x)+int(x>right)
        new = int(left>u)+int(u>right)
        h = int((left>x)!=(left>u))+int((x>right)!=(u>right))
        counter[(new-old,h)]+=1
    assert counter=={(0,0):12,(1,1):4,(-1,1):4,(0,2):4},counter
    assertions+=1
    print('PASS:', assertions, 'exact assertions; 12 exhaustive (n,p) cases with up to 8! * 16 configurations each; 24 single-refresh rank orders.')


if __name__ == '__main__':
    test_exact()
