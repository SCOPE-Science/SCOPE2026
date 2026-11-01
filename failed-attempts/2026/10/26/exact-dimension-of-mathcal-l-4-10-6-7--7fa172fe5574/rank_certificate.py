#!/usr/bin/env python3
"""Exact modular-rank certificate for the seven-point system L_{4,10}(6^7)."""
from itertools import product
from math import comb

P = 101
POINTS = ((6, 56, 63, 3), (97, 130, 133, 106))

def rank_mod_pivots(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix]
    original_rows = list(range(len(a)))
    rank = 0
    pivot_columns = []
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        original_rows[rank], original_rows[pivot] = original_rows[pivot], original_rows[rank]
        inv = pow(a[rank][col], -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for i in range(rank + 1, len(a)):
            c = a[i][col]
            if c:
                a[i] = [(a[i][j] - c * a[rank][j]) % p for j in range(len(a[0]))]
        pivot_columns.append(col)
        rank += 1
        if rank == len(a):
            break
    return rank, original_rows[:rank], pivot_columns

def det_mod(matrix, p):
    a = [[int(x) % p for x in row] for row in matrix]
    n = len(a)
    det = 1
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = (-det) % p
        value = a[col][col]
        det = (det * value) % p
        inv = pow(value, -1, p)
        for i in range(col + 1, n):
            if a[i][col]:
                factor = (a[i][col] * inv) % p
                for j in range(col + 1, n):
                    a[i][j] = (a[i][j] - factor * a[col][j]) % p
                a[i][col] = 0
    return det % p

def main():
    # Five coordinate points impose e_i <= 4 on degree-10 monomials.
    basis = []
    for tail in product(range(5), repeat=4):
        e0 = 10 - sum(tail)
        if 0 <= e0 <= 4:
            basis.append((e0,) + tail)
    assert len(basis) == 381

    # Multiplicity six means all Taylor coefficients of total degree < 6 vanish.
    alphas = [alpha for alpha in product(range(6), repeat=4) if sum(alpha) < 6]
    assert len(alphas) == 126

    # The two extra points are in general position with the five coordinate points:
    # all coordinates are nonzero and all 2x2 minors of POINTS are nonzero.
    assert all(c != 0 for point in POINTS for c in point)
    minors = [POINTS[0][i] * POINTS[1][j] - POINTS[0][j] * POINTS[1][i]
              for i in range(4) for j in range(i + 1, 4)]
    assert all(x != 0 for x in minors)

    matrix = []
    for point in POINTS:
        for alpha in alphas:
            row = []
            for exponent in basis:
                coefficient = 1
                for j in range(4):
                    e = exponent[j + 1]
                    if alpha[j] > e:
                        coefficient = 0
                        break
                    coefficient *= comb(e, alpha[j]) * point[j] ** (e - alpha[j])
                row.append(coefficient)
            matrix.append(row)

    assert len(matrix) == 252 and len(matrix[0]) == 381
    rank, pivot_rows, pivot_columns = rank_mod_pivots(matrix, P)
    assert rank == 240
    minor = [[matrix[i][j] for j in pivot_columns] for i in pivot_rows]
    determinant = det_mod(minor, P)
    assert determinant == 9

    print("field=F_101")
    print("remaining_jet_matrix=252x381")
    print("rank_mod_101=240")
    print("selected_240x240_minor_determinant_mod_101=9")
    print("five_coordinate_point_conditions_rank=620")
    print("full_interpolation_rank_lower_bound=860")
    # Witness that the tangent fifth-power is outside the span of six chord
    # fifth-powers at a point of a rational normal quartic.
    directions = [(1, 0, 0, 0)] + [
        (j, j*j, j**3, j**4) for j in range(1, 7)
    ]
    degree_five_monomials = [
        exponent for exponent in product(range(6), repeat=4)
        if sum(exponent) == 5
    ]
    veronese = [
        [__import__("math").prod(directions[k][i] ** exponent[i] for i in range(4))
         for k in range(7)]
        for exponent in degree_five_monomials
    ]
    veronese_rank, veronese_rows, veronese_columns = rank_mod_pivots(veronese, P)
    assert veronese_rank == 7
    veronese_minor = [[veronese[i][j] for j in veronese_columns] for i in veronese_rows]
    veronese_determinant = det_mod(veronese_minor, P)
    assert veronese_determinant == 11

    print("full_vector_space_dimension_upper_bound=141")
    print("tangent_plus_six_chord_fifth_powers_rank_mod_101=7")
    print("selected_veronese_minor_determinant_mod_101=11")

if __name__ == "__main__":
    main()
