"""Exact-rational checks for single-vertex protection on path contact networks.

Run: python3 verify_path_tail.py
Uses the Python standard library only. It checks small finite instances; the
all-order theorem is proved separately by a run-count identity and convexity.
"""
from fractions import Fraction
from itertools import product


def run_formula(m, h, p):
    if m < h:
        return Fraction(0)
    return p**(h - 1) * (h * (m - h + 1) - (h - 1) * (m - h) * p)


def expected_members_bruteforce(m, h, p):
    """Expected number of vertices in open components of cardinality >=h."""
    ans = Fraction(0)
    for edges in product((0, 1), repeat=max(0, m - 1)):
        lengths = []
        current = 1
        for edge in edges:
            if edge:
                current += 1
            else:
                lengths.append(current)
                current = 1
        lengths.append(current)
        weight = p ** sum(edges) * (1 - p) ** (len(edges) - sum(edges))
        ans += weight * sum(x for x in lengths if x >= h)
    return ans


def pair_formula(m, p):
    return sum((m - d) * p**d for d in range(1, m))


def pair_bruteforce(m, p):
    ans = Fraction(0)
    for edges in product((0, 1), repeat=max(0, m - 1)):
        lengths = []
        current = 1
        for edge in edges:
            if edge:
                current += 1
            else:
                lengths.append(current)
                current = 1
        lengths.append(current)
        weight = p**sum(edges) * (1-p)**(len(edges)-sum(edges))
        ans += weight * sum(x*(x-1)//2 for x in lengths)
    return ans


def expected_tail_optima(n, h):
    if n <= 2*h - 1:
        return set(range(max(1, n-h+1), min(n,h)+1))
    return {h, n-h+1}


def expected_mean_optima(n):
    return {(n+1)//2, (n+2)//2}


def checks():
    identities=0
    for m in range(1,12):
        for h in range(2,10):
            for edges in product((0,1), repeat=max(0,m-1)):
                components=[]
                length=1
                for bit in edges:
                    if bit: length+=1
                    else: components.append(length);length=1
                components.append(length)
                left=sum(c for c in components if c>=h)
                blocks_h=sum(all(edges[i:i+h-1]) for i in range(max(0,m-h+1)))
                blocks_h1=sum(all(edges[i:i+h]) for i in range(max(0,m-h)))
                right=h*blocks_h-(h-1)*blocks_h1
                assert left==right,(m,h,edges)
                identities+=1
    formulas = 0
    objectives = 0
    policy = 0
    for m in range(1, 13):
        for h in range(2, 9):
            for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
                a = expected_members_bruteforce(m, h, p)
                b = run_formula(m, h, p)
                assert a == b, (m, h, p, a, b)
                formulas += 1
            if h == 2:
                for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
                    assert pair_bruteforce(m,p) == pair_formula(m,p)
                    objectives += 1
    for n in range(2, 35):
        for h in range(2, 13):
            for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
                tails = [run_formula(v-1,h,p)+run_formula(n-v,h,p) for v in range(1,n+1)]
                means = [pair_formula(v-1,p)+pair_formula(n-v,p) for v in range(1,n+1)]
                assert {j+1 for j,x in enumerate(tails) if x == min(tails)} == expected_tail_optima(n,h), (n,h,p)
                assert {j+1 for j,x in enumerate(means) if x == min(means)} == expected_mean_optima(n), (n,h,p)
                assert bool(expected_tail_optima(n,h) & expected_mean_optima(n)) == (n <= 2*h), (n,h)
                policy += 1
    # Verify the sharp 7-vertex threshold-3 comparison as a concrete boundary.
    p = Fraction(1,2)
    n,h=7,3
    t_center = (run_formula(3,h,p)*2)/(n-1)
    t_off = (run_formula(2,h,p)+run_formula(4,h,p))/(n-1)
    assert t_center-t_off == Fraction(1,24)
    print('PASS: deterministic run-count identities:',identities)
    print('PASS: exact finite path component enumerations:',formulas)
    print('PASS: exact path pair connectivity enumerations:',objectives)
    print('PASS: cross-objective policy evaluations:',policy)
    print('PASS: n=7, h=3, p=1/2 tail gap:',t_center-t_off)


if __name__ == '__main__':
    checks()
