#!/usr/bin/env python3
"""Direct point-count check for three explicit genus-four curves over F_2."""
from itertools import product

# Irreducible binary polynomial reductions for extension degrees 1, 2, 3, 4.
REDUCTIONS = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011}


def table(m):
    q = 1 << m
    mod = REDUCTIONS[m]
    result = [[0] * q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            v = 0
            c, d = a, b
            while d:
                if d & 1:
                    v ^= c
                c <<= 1
                if c & q:
                    c ^= mod
                d >>= 1
            result[a][b] = v
    assert all(all(table_value < q for table_value in row) for row in result)
    return result


def terms(expr, variables):
    monomials = []
    for chunk in expr.replace(' ', '').split('+'):
        exponents = [0] * len(variables)
        for factor in chunk.split('*'):
            if factor == '1':
                continue
            if '^' in factor:
                var, pow_str = factor.split('^')
                exponent = int(pow_str)
            else:
                var, exponent = factor, 1
            exponents[variables.index(var)] += exponent
        monomials.append(tuple(exponents))
    return monomials


def evaluate(poly, coordinates, mtable):
    powers = [[1] for _ in coordinates]
    for ind, exps in enumerate(powers):
        for _ in range(max(t[ind] for t in poly)):
            exps.append(mtable[exps[-1]][coordinates[ind]])
    value = 0
    for mono in poly:
        prod = 1
        for i, e in enumerate(mono):
            prod = mtable[prod][powers[i][e]]
        value ^= prod
    return value

# Source: Xarles's published genus-four F2 census, Weil-group index 67 (zero based).
Q_CONE = 'X*Y + T^2'
F_CONE = 'X^3 + X^2*Y + Y^3 + X^2*Z + X*Y*Z + Z^3 + X^2*T + X*Y*T + X*Z*T'
Q_NONSPLIT = 'X^2 + X*Y + Y^2 + Z*T'
F_NONSPLIT = 'X^3 + X^2*Y + Y^3 + X^2*Z + Y^2*Z + X*Z^2 + Z^3 + X*Y*T + X*T^2'
P_HYP = 'x^9 + x + 1'
Q_HYP = 'x^3 + x + 1'


def points_canonical(m, equation_q, equation_f):
    q = 1 << m
    multiplication = table(m)
    eq1 = terms(equation_q, 'XYZT')
    eq2 = terms(equation_f, 'XYZT')
    count = 0
    for pivot in range(4):
        for suffix in product(range(q), repeat=3-pivot):
            coords = (0,) * pivot + (1,) + suffix
            if evaluate(eq1, coords, multiplication) == 0 and evaluate(eq2, coords, multiplication) == 0:
                count += 1
    return count


def points_hyperelliptic(m):
    q = 1 << m
    multiplication = table(m)
    qpoly = terms(Q_HYP, 'x')
    ppoly = terms(P_HYP, 'x')
    n = 1  # unique geometric point at infinity: odd-degree 9 Artin-Schreier model
    for x in range(q):
        qx = evaluate(qpoly, (x,), multiplication)
        px = evaluate(ppoly, (x,), multiplication)
        for y in range(q):
            if multiplication[y][y] ^ multiplication[qx][y] ^ px == 0:
                n += 1
    return n


def main():
    counts = []
    for m in (1, 2, 3, 4):
        triple = (points_hyperelliptic(m),
                  points_canonical(m, Q_CONE, F_CONE),
                  points_canonical(m, Q_NONSPLIT, F_NONSPLIT))
        assert triple == ((1, 1, 1), (5, 5, 5), (10, 10, 10), (17, 17, 17))[m-1], (m,triple)
        counts.append(triple)
    print('GENUS4_F2_THREE_GONALITIES_SAME_ZETA_VERIFIED')
    print('point counts by degree 1,2,3,4:', counts)


if __name__ == '__main__':
    main()
