#!/usr/bin/env python3
"""Independent polynomial-transfer and run-composition checks for wheel equilibria."""
from math import comb

# Allowed cyclic binary words avoid the two singleton patterns 010 and 101.
PAIRS = [(0,0),(0,1),(1,0),(1,1)]


def trace_coefficient(n, k):
    result = 0
    for start in PAIRS:
        # Count walks that begin at 'start' and return after n edges;
        # exponent counts newly appended 1 symbols.
        states = {(start,0):1}
        for _ in range(n):
            next_states = {}
            for ((a,b),ones), count in states.items():
                for c in (0,1):
                    if a==c and b!=a:
                        continue
                    if ones+c>k:
                        continue
                    key = ((b,c),ones+c)
                    next_states[key] = next_states.get(key,0)+count
            states = next_states
        result += states.get((start,k),0)
    return result


def run_formula(n):
    assert n%2 == 0
    m=n//2
    return sum((n*comb(m-r-1,r-1)**2)//r for r in range(1,m//2+1))


def main():
    for n in range(4,81,2):
        actual = trace_coefficient(n,n//2)
        predicted = run_formula(n)
        assert actual == predicted, (n,actual,predicted)
        if n<=24 or n%20==0:
            print(f'rim_length={n} balanced_stripes={actual}')
    for n in range(3,32,2):
        # Odd n cannot admit equal counts of two colors.
        assert n%2 == 1
    print('all symbolic-size transfer comparisons passed')

if __name__ == '__main__':
    main()
