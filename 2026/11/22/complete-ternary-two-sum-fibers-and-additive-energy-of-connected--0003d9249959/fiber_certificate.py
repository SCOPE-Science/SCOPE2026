"""Exact, dependency-free finite-state certificate for ternary weight-two index sums.

Run: python fiber_certificate.py
All counts are integer arithmetic. Digits are read least-significant first.
"""
from collections import Counter, defaultdict, deque
from itertools import product
from math import comb

MONOMIALS = [(i, j) for i in range(3) for j in range(3)]
INDEX = {(carry, i, j): 9*carry+3*i+j
         for carry in range(2) for i, j in MONOMIALS}
DIGIT_MOVES = {}
for digit in range(3):
    for carry in range(2):
        DIGIT_MOVES[digit, carry] = tuple(
            ((a+b+carry)//3, a, b) for a, b in product(range(3), repeat=2)
            if (a+b+carry) % 3 == digit
        )

def transition(state, digit):
    result = [0]*18
    for carry, i, j in INDEX:
        coefficient = state[INDEX[carry, i, j]]
        if not coefficient:
            continue
        for carry_out, a, b in DIGIT_MOVES[digit, carry]:
            if i+a <= 2 and j+b <= 2:
                result[INDEX[carry_out, i+a, j+b]] += coefficient
    return tuple(result)

def count_fiber(state):
    return sum(state[INDEX[c, i, j]] for c in range(2)
               for i in (1, 2) for j in (1, 2))

# Each triple lists next-state IDs on ternary digits 0,1,2.
EXPECTED_TRANSITIONS = (
    (1,2,3),(1,4,5),(6,7,8),(3,8,9),(10,11,8),(5,8,9),
    (6,12,8),(7,13,14),(8,14,15),(9,15,15),(10,16,8),
    (11,13,14),(12,13,14),(13,17,15),(14,15,15),
    (15,15,15),(16,13,14),(17,15,15)
)
EXPECTED_FIBERS = (0,2,1,1,3,3,2,3,4,3,4,5,4,6,4,0,6,6)

def automaton():
    initial = (1,) + (0,)*17
    states = [initial]
    ids = {initial: 0}
    trans = []
    for state in states:
        targets = []
        for digit in range(3):
            target = transition(state, digit)
            if target not in ids:
                ids[target] = len(states)
                states.append(target)
            targets.append(ids[target])
        trans.append(tuple(targets))
    assert len(states) == 18
    assert tuple(trans) == EXPECTED_TRANSITIONS
    assert tuple(count_fiber(s) for s in states) == EXPECTED_FIBERS
    return states, trans

def multiply(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for k, a in enumerate(A[i]):
            if a:
                for j, b in enumerate(B[k]):
                    if b:
                        result[i][j] += a*b
    return result

def minus_scalar_identity(A, v):
    B = [row[:] for row in A]
    for i in range(len(B)):
        B[i][i] -= v
    return B

def power(A, exponent):
    n = len(A)
    result = [[int(i==j) for j in range(n)] for i in range(n)]
    base = A
    while exponent:
        if exponent % 2:
            result = multiply(result, base)
        exponent //= 2
        if exponent:
            base = multiply(base, base)
    return result

def choose(n,k):
    return comb(n,k) if n>=k>=0 else 0

def predicted_histogram(r):
    if r==0: return {0:1}
    if r==1: return {1:2, 2:1}
    h = {
        1: 1,
        2: 2,
        3: 1+r+choose(r,2),
        4: 3*choose(r,3)+r*r+r-4,
        5: r-2,
        6: choose(r,4)+choose(r,3)+choose(r-2,2),
    }
    h[0] = 3**r-sum(h.values())
    return {k:v for k,v in h.items() if v}

def energy_formula(r):
    if r == 0: return 0
    q = 3*r**4 + 10*r**3 + 26*r*r - 51*r + 24
    assert q%2 == 0
    return q//2

def verify():
    states, transitions = automaton()
    n = len(states)
    T = [[0]*n for _ in range(n)]
    for i, successors in enumerate(transitions):
        for j in successors:
            T[i][j] += 1
    # Exact matrix annihilation, stronger than checking a finite sample:
    # T^2 (T-3I)(T-I)^5 = 0.
    annihilator = multiply(multiply(power(T,2),
                                  minus_scalar_identity(T,3)),
                           power(minus_scalar_identity(T,1),5))
    assert all(x==0 for row in annihilator for x in row)
    population = [0]*n
    population[0] = 1
    for r in range(18):
        histogram = Counter()
        for i, weight in enumerate(population):
            if weight: histogram[count_fiber(states[i])] += weight
        assert dict(histogram) == predicted_histogram(r), (r,histogram)
        assert sum(v*j*j for j,v in histogram.items()) == energy_formula(r)
        next_population = [0]*n
        for i, weight in enumerate(population):
            if weight:
                for target in transitions[i]:
                    next_population[target] += weight
        population = next_population
    # All-depth proof: both histogram formulae and actual histogram
    # satisfy the order-eight linear recurrence given by the annihilator.
    # They agree at r=0,...,7. The subsequent tests are redundancy.
    print('PASS: exactly 18 reachable symbolic carry states.')
    print('PASS: exact 18x18 matrix annihilator T^2(T-3I)(T-I)^5=0.')
    print('PASS: full multiplicity histograms and energy r=0,...,17.')
    print('PASS: recurrence plus 8 initial depths certify every r>=0.')
    print('R multiplicities on represented residues lie in {1,...,6}.')

if __name__=='__main__':
    verify()
