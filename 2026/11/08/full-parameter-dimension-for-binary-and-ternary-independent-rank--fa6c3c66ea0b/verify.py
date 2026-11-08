"""Exact finite witnesses for low-support independent ranking-law dimensions.

Requires Python 3, standard library only. This checks the combinatorial
permutation witnesses and the rational three-variable Jacobian certificate.
The arbitrary-n dimension theorem additionally uses the proof in RESULT.md.
"""
from itertools import permutations, product
from fractions import Fraction


def move(n, i, after):
    """Move label i just after `after`, or to front if after=0."""
    seq = [x for x in range(1, n+1) if x != i]
    if after == 0:
        return (i, *seq)
    j = seq.index(after)
    seq.insert(j+1, i)
    return tuple(seq)


def binary_witnesses(n):
    if n < 3:
        raise ValueError("n>=3 required")
    out = [move(n, 1, n)]
    out.extend(move(n, i, 0) for i in range(2, n+1))
    return out


def ternary_witnesses(n):
    if n < 4:
        raise ValueError("n>=4 required")
    # Each pair corresponds to two different nonbaseline atoms for label i.
    out = [move(n, 1, 3), move(n, 1, 4)]
    out += [move(n, 2, 0), move(n, 2, 4)]
    out += [move(n, 3, 0), move(n, 3, 1)]
    out += [move(n, 4, 0), move(n, 4, 1)]
    for i in range(5, n+1):
        out.extend([move(n, i, 0), move(n, i, 1)])
    return out


def determinant(mat):
    n = len(mat)
    a = [[Fraction(x) for x in row] for row in mat]
    prod = Fraction(1)
    for j in range(n):
        ix = next((i for i in range(j, n) if a[i][j] != 0), None)
        if ix is None:
            return Fraction(0)
        if ix != j:
            a[j], a[ix] = a[ix], a[j]
            prod *= -1
        pivot = a[j][j]
        prod *= pivot
        for i in range(j+1, n):
            factor = a[i][j] / pivot
            for k in range(j+1, n):
                a[i][k] -= factor*a[j][k]
            a[i][j] = 0
    return prod


def ternary_three_jacobian():
    """Returns 9 times the exact Jacobian at equal masses for word aabc bacbc."""
    word = (0, 0, 1, 2, 1, 0, 2, 1, 2)
    positions = {i: [j for j,x in enumerate(word) if x == i] for i in range(3)}
    perms = list(permutations(range(3)))
    out = [[0]*6 for _ in range(6)]
    for indices in product(range(3), repeat=3):
        order = tuple(sorted(range(3), key=lambda i:positions[i][indices[i]]))
        row = perms.index(order)
        for i in range(3):
            for j in range(2):
                out[row][2*i+j] += int(indices[i] == j)-int(indices[i] == 2)
    return out


def main():
    count = 0
    for n in range(3, 101):
        b = binary_witnesses(n)
        assert len(b) == n and len(set(b)) == n
        assert all(x != tuple(range(1, n+1)) for x in b)
        count += 2*n+1
    for n in range(4, 101):
        t = ternary_witnesses(n)
        assert len(t) == 2*n and len(set(t)) == 2*n
        assert all(x != tuple(range(1, n+1)) for x in t)
        count += 4*n+1
    j = ternary_three_jacobian()
    expected = [
        [5,5,3,1,-5,-3],
        [2,2,-5,-3,4,3],
        [-4,-4,2,2,-2,0],
        [-1,-1,1,0,1,0],
        [-1,-1,-1,-1,1,0],
        [-1,-1,0,1,1,0],
    ]
    assert j == expected
    minor = [[j[r][c] for c in (0,2,3,4,5)] for r in range(5)]
    assert determinant(minor) == -54
    # Rank at most 5 because all 6 ranking probabilities sum to 1.
    assert all(sum(row[col] for row in j) == 0 for col in range(6))
    # Verified 5x5 minor of Jacobian, including 1/9 factor.
    assert determinant([[Fraction(j[r][c], 9) for c in (0,2,3,4,5)]
                        for r in range(5)]) == Fraction(-2,2187)
    print(f"PASS: binary and ternary distinct-permutation witnesses, n<=100; "
          f"{count} scalar witness conditions; exact 3-variable Jacobian minor=-2/2187")


if __name__ == '__main__':
    main()
