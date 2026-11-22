#!/usr/bin/env python3
"""Exact integer dual certificates and independent finite-size check for a Potts strip."""
from fractions import Fraction
from itertools import product

COLORS = range(3)
STATES = list(product(COLORS, repeat=3))
INDEX = {state: i for i, state in enumerate(STATES)}
TRANSITIONS = []
for source, (u, p, q) in enumerate(STATES):
    for x, y in product(COLORS, repeat=2):
        target = INDEX[(x, y, p)]
        cost = int(u == x) + int(q == y) + int(x == y)
        count = int(x == 0) + int(y == 0)
        TRANSITIONS.append((source, target, cost, count))

# h, g(h), integral multiplier, exact 27-state dual potential
CERTIFICATES = [
    (Fraction(-1), Fraction(1, 2), 2,
     [0,0,0,0,-1,0,0,0,-1,0,-1,0,0,-1,0,-1,-2,-1,0,0,-1,-1,-1,-2,0,0,-1]),
    (Fraction(0), Fraction(0), 1, [0]*27),
    (Fraction(5,4), Fraction(-1), 4,
     [-4,-2,-2,-4,-1,-1,-4,-1,-1,-3,-2,-2,0,0,0,0,0,0,-3,-2,-2,0,0,0,0,0,0]),
    (Fraction(7,4), Fraction(-3,2), 4,
     [-8,-4,-4,-6,-3,-3,-6,-3,-3,-5,-4,-4,0,0,0,-2,0,0,-5,-4,-4,-2,0,0,0,0,0]),
    (Fraction(3), Fraction(-3), 1,
     [-3,-2,-2,-2,-1,-1,-2,-1,-1,-2,-1,-1,0,0,0,0,0,0,-2,-1,-1,0,0,0,0,0,0]),
]

# Each string encodes alternating outer, inner colors of one periodic cell.
WITNESSES = [
    ("11211222", 2, 0),
    ("01120221", 0, 2),
    ("0110200212", 0, 4),
    ("00100112", 1, 4),
    ("0010010110", 3, 6),
    ("00", 3, 2),
]

def energy_and_occupancy(word):
    assert len(word) % 2 == 0
    cells = [(int(word[i]), int(word[i+1])) for i in range(0, len(word), 2)]
    size = len(cells)
    cost = sum(int(cells[i][0] == cells[(i+1) % size][0])
               + int(cells[i][1] == cells[(i+2) % size][1])
               + int(cells[i][0] == cells[i][1]) for i in range(size))
    count = sum(int(u == 0) + int(v == 0) for u, v in cells)
    return cost, count

def exact_ground_energy(n, h):
    """Independent transfer minimization of all 27-state closed walks."""
    best = None
    for initial in range(27):
        scores = {initial: Fraction(0)}
        for _ in range(n):
            updated = {}
            for source, target, cost, count in TRANSITIONS:
                if source in scores:
                    candidate = scores[source] + cost - h * count
                    if target not in updated or candidate < updated[target]:
                        updated[target] = candidate
            scores = updated
        if initial in scores and (best is None or scores[initial] < best):
            best = scores[initial]
    return best

def main():
    assert len(TRANSITIONS) == 243
    for h, g, multiplier, potential in CERTIFICATES:
        assert len(potential) == 27
        assert all(multiplier * (cost - h*count - g) + potential[source] - potential[target] >= 0
                   for source, target, cost, count in TRANSITIONS)
    assert [energy_and_occupancy(word) for word, _, _ in WITNESSES] == [
        (cost, count) for _, cost, count in WITNESSES]
    assert [len(word)//2 for word,_,_ in WITNESSES] == [4,4,5,4,5,1]
    breakpoints = [Fraction(-1),Fraction(0),Fraction(5,4),Fraction(7,4),Fraction(3)]
    sampling = [Fraction(-2)] + breakpoints + [Fraction(-1,2),Fraction(1,2),
        Fraction(3,2),Fraction(2),Fraction(4)]
    phases = [(Fraction(c,len(word)//2),Fraction(k,len(word)//2))
              for word,c,k in WITNESSES]
    for h in sampling:
        predicted = min(cost-h*count for cost,count in phases)
        assert exact_ground_energy(20,h) == 20*predicted, ('size20',h)
    # Distinguishes the single middle transition on the ten-cell dodecahedron.
    assert exact_ground_energy(10,Fraction(3,2)) == Fraction(-12)
    print('POTTS_DUAL_CERTIFICATES_OK 1215')
    print('PERIODIC_WITNESSES_OK 6')
    print('INDEPENDENT_MINPLUS_CLOSURES_OK', len(sampling))

if __name__ == '__main__':
    main()
