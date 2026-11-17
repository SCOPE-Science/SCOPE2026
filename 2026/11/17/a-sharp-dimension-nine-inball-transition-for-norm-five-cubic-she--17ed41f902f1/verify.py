"""Exact finite checks for the norm-five integer-shell polytope theorem.

Run with Python 3.10+ and SymPy; the unrestricted proof is in RESULT.md.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from sympy import Matrix

assertions = 0

def check(condition, message):
    global assertions
    assert condition, message
    assertions += 1


def chamber_vertices(d):
    """Enumerate exact vertices of a nonnegative orthant cut by two inequalities."""
    a = [2] + [3] * (d - 1)
    b = [min(i, 5) for i in range(1, d + 1)]
    out = set()
    for i in range(d):
        z = [Q(0) for _ in range(d)]
        z[i] = Q(1, max(a[i], b[i]))
        out.add(tuple(z))
    out.add(tuple([Q(0)] * d))
    for i, j in combinations(range(d), 2):
        det = a[i] * b[j] - a[j] * b[i]
        if det == 0:
            continue
        x = Q(b[j] - a[j], det)
        y = Q(a[i] - b[i], det)
        if x <= 0 or y <= 0:
            continue
        check(a[i]*x + a[j]*y == 1 and b[i]*x + b[j]*y == 1,
              'failed active linear equations')
        z = [Q(0) for _ in range(d)]
        z[i], z[j] = x, y
        out.add(tuple(z))
    return out


def squared_norm_of_z(z):
    d = len(z)
    u = [sum(z[i:], Q(0)) for i in range(d)]
    return sum((t*t for t in u), Q(0))


def sign_orbit(d):
    # Each vector has squared coordinate norm exactly five.
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            for si, sj in product((-1, 1), repeat=2):
                w = [0] * d
                w[i], w[j] = 2 * si, sj
                yield tuple(w)
    for idx in combinations(range(d), 5):
        for signs in product((-1, 1), repeat=5):
            w = [0] * d
            for i, sign in zip(idx, signs):
                w[i] = sign
            yield tuple(w)


def norm_contact(d, w):
    return (sum(w[:3]), 3) if d <= 8 else (sum(w), 5)

for d in range(5, 21):
    values = [(squared_norm_of_z(z), z) for z in chamber_vertices(d)]
    top = max(v for v, _ in values)
    expected = Q(1, 3) if d <= 8 else Q(d, 25)
    check(top == expected, ('polar squared circumradius', d, top))
    winners = [z for v, z in values if v == top]
    check(len(winners) == 1, ('nonunique chamber maximum', d, winners))
    z = winners[0]
    target = [Q(0)] * d
    target[2 if d <= 8 else d-1] = Q(1, 3) if d <= 8 else Q(1, 5)
    check(list(z) == target, ('wrong chamber equality pattern', d))
    for z in chamber_vertices(d):
        a = [2] + [3] * (d-1)
        b = [min(i,5) for i in range(1,d+1)]
        check(sum(a[i]*z[i] for i in range(d)) <= 1,
              ('A support inequality', d))
        check(sum(b[i]*z[i] for i in range(d)) <= 1,
              ('B support inequality', d))

for d in (5, 6, 8, 9):
    shell = list(sign_orbit(d))
    check(len(shell) == 4*d*(d-1) + 32*comb(d, 5), 'shell count')
    check(len(set(shell)) == len(shell), 'duplicated shell vector')
    check(all(sum(t*t for t in w) == 5 for w in shell), 'non-shell vertex')
    if d <= 8:
        normals = []
        for inds in combinations(range(d), 3):
            for signs in product((-1,1), repeat=3):
                n = [0]*d
                for i,s in zip(inds,signs): n[i] = s
                normals.append(tuple(n))
        expected_count = 8*comb(d,3)
        rhs = 3
    else:
        normals = list(product((-1,1), repeat=d))
        expected_count = 2**d
        rhs = 5
    check(len(normals) == expected_count, ('normal count', d))
    # Check the entire primal generating set for each tangent facet.
    for normal in normals:
        values = [sum(x*y for x,y in zip(w,normal)) for w in shell]
        check(max(values) == rhs, ('support mismatch', d, normal))
    # Exact affine rank, using canonical positive normal and ALL its contacts.
    normal = ((1,1,1) + (0,)*(d-3)) if d <= 8 else (1,)*d
    contacts = [w for w in shell if sum(x*y for x,y in zip(w, normal)) == rhs]
    differences = Matrix([[w[i]-contacts[0][i] for i in range(d)]
                          for w in contacts[1:]])
    check(differences.rank() == d-1, ('not a facet', d, differences.rank()))

print('PASS:', assertions, 'exact rational / support / rank assertions')
print('Dimensional tests: dual chamber d=5..20, full vertex-support d=5,6,8,9')
print('Eight-dimensional norm-five cubic shell: 2016 vertices, 448 tangent facets')
