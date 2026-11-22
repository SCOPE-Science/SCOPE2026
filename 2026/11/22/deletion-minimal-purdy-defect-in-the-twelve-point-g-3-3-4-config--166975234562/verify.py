"""Exact reproducibility of the deletion profile for the root-of-unity 12-point set.

Uses (1) explicit classification of flats and (2) determinants in Q(zeta_3).
Only Python's standard library is required.
"""
from itertools import combinations
from collections import Counter, defaultdict
from fractions import Fraction

EDGES = ((0, 2), (0, 3), (1, 2), (1, 3))
GROUPS = tuple(sum(1 << (3 * g + a) for a in range(3)) for g in range(4))
ALL = (1 << 12) - 1

# Combinatorial span criteria, using the classified flats.
line_spans = list(GROUPS)
for g, h in combinations(range(4), 2):
    line_spans += [(1 << (3*g+a)) | (1 << (3*h+b))
                   for a in range(3) for b in range(3)]
assert len(line_spans) == 58

face_pairs = [(g, h) for g, h in combinations(range(4), 2)
              if set(EDGES[g]) & set(EDGES[h])]
opposite_pairs = [(g, h) for g, h in combinations(range(4), 2)
                  if not set(EDGES[g]) & set(EDGES[h])]
assert len(face_pairs) == 4 and len(opposite_pairs) == 2
balanced = [(1 << a) | (1 << (3 + b)) | (1 << (6 + c)) |
            (1 << (9 + ((b+c-a) % 3)))
            for a in range(3) for b in range(3) for c in range(3)]
assert len(balanced) == 27

def combinatorial_profile(mask):
    sizes = [(mask & s).bit_count() for s in GROUPS]
    f1 = sum(sz >= 2 for sz in sizes) + sum(sizes[g] * sizes[h]
                                              for g, h in combinations(range(4), 2))
    faces = sum((sizes[g] >= 2 and sizes[h] >= 1) or
                (sizes[h] >= 2 and sizes[g] >= 1) for g, h in face_pairs)
    opposite = sum(sizes[h] * (sizes[g] >= 2) + sizes[g] * (sizes[h] >= 2)
                   for g, h in opposite_pairs)
    balanced_planes = sum((mask & quad).bit_count() >= 3 for quad in balanced)
    f2 = faces + opposite + balanced_planes
    n = mask.bit_count()
    return n, f1, f2, f2 - f1 + n + 2

# Independent determinant-based enumeration, exact in Q[zeta]/(zeta^2+zeta+1).
class Cyclo:
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)
    def __add__(self, rhs): return Cyclo(self.a+rhs.a, self.b+rhs.b)
    def __neg__(self): return Cyclo(-self.a, -self.b)
    def __sub__(self, rhs): return self + (-rhs)
    def __mul__(self, rhs):
        return Cyclo(self.a*rhs.a-self.b*rhs.b,
                     self.a*rhs.b+self.b*rhs.a-self.b*rhs.b)
    def __truediv__(self, rhs):
        n = rhs.a**2-rhs.a*rhs.b+rhs.b**2
        if not n: raise ZeroDivisionError
        return self * Cyclo((rhs.a-rhs.b)/n, -rhs.b/n)
    def __bool__(self): return bool(self.a or self.b)
    def key(self): return self.a, self.b

Z, ONE, ZETA = Cyclo(), Cyclo(1), Cyclo(0, 1)
POWERS = (ONE, ZETA, Cyclo(-1, -1))
POINTS = []
for i, j in EDGES:
    for a in range(3):
        vec = [Z] * 4
        vec[i], vec[j] = ONE, -POWERS[a]
        POINTS.append(vec)

def determinant(M):
    if len(M) == 1: return M[0][0]
    out = Z
    for i, x in enumerate(M[0]):
        minor = [row[:i]+row[i+1:] for row in M[1:]]
        out += x*determinant(minor) if i % 2 == 0 else -(x*determinant(minor))
    return out

def projectivize(coords):
    pivot = next((x for x in coords if x), None)
    if pivot is None: return None
    return tuple((x / pivot).key() for x in coords)

exact_lines, exact_planes = defaultdict(list), defaultdict(list)
for i, j in combinations(range(12), 2):
    v = [determinant([[POINTS[i][a], POINTS[i][b]],
                      [POINTS[j][a], POINTS[j][b]]])
         for a, b in combinations(range(4), 2)]
    exact_lines[projectivize(v)].append((1 << i) | (1 << j))
for i, j, k in combinations(range(12), 3):
    v = [determinant([[POINTS[r][a] for a in range(4) if a != b]
                      for r in (i, j, k)]) for b in range(4)]
    key = projectivize(v)
    if key is not None:
        exact_planes[key].append((1 << i) | (1 << j) | (1 << k))
assert len(exact_lines) == 58 and len(exact_planes) == 43

def determinant_profile(mask):
    n = mask.bit_count()
    f1 = sum(any((pair & mask) == pair for pair in pairs)
             for pairs in exact_lines.values())
    f2 = sum(any((triple & mask) == triple for triple in triples)
             for triples in exact_planes.values())
    return n, f1, f2, f2-f1+n+2

profiles = []
for mask in range(1 << 12):
    a, b = combinatorial_profile(mask), determinant_profile(mask)
    assert a == b, (mask, a, b)
    profiles.append(a)

negative = {mask: profile for mask, profile in enumerate(profiles) if profile[3] < 0}
expected = {ALL: (12, 58, 43, -1)}
for g, h in face_pairs:
    expected[GROUPS[g] | GROUPS[h]] = (6, 11, 1, -2)
assert negative == expected, (negative, expected)
assert all(profiles[ALL ^ (1 << a)][3] == 6 for a in range(12))
assert sum(1 for p in profiles if p[3] < 0) == 5
print('all subsets:', len(profiles))
print('independent flats:', len(exact_lines), 'lines;', len(exact_planes), 'planes')
print('full configuration:', profiles[ALL])
print('negative configurations:', sorted(negative.items()))
print('every single deletion has defect 6')
print('all exact-arithmetic assertions passed')
