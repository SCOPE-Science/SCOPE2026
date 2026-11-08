#!/usr/bin/env python3
"""Exact finite-field checks for the ternary Hermitian cubic line boundary.

No external dependencies; finite fields are polynomial quotients over F_2.
The general arithmetic identities are proved mathematically in RESULT.md;
this program checks geometric input and several extension fields.
"""
from itertools import product, combinations
from collections import Counter

MODULI = {1: 0b11, 2: 0b111, 3: 0b1011, 4: 0b10011, 5: 0b100101, 6: 0b1000011}
MATCHINGS = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]

class FiniteField:
    def __init__(self, m):
        self.m = m
        self.q = 1 << m
        self.poly = MODULI[m]
        self.mult = [[self._mul(a, b) for b in range(self.q)] for a in range(self.q)]
        self.cubes = [self.mult[self.mult[a][a]][a] for a in range(self.q)]
        self.inv = [0] * self.q
        for a in range(1, self.q):
            self.inv[a] = next(b for b in range(1, self.q) if self.mult[a][b] == 1)

    def _mul(self, a, b):
        x = 0
        while b:
            if b & 1:
                x ^= a
            a <<= 1
            if a & self.q:
                a ^= self.poly
            b >>= 1
        return x

    def norm(self, v):
        nonzero = next((i for i, c in enumerate(v) if c), None)
        if nonzero is None:
            raise ValueError("zero vector")
        inv = self.inv[v[nonzero]]
        return tuple(self.mult[inv][c] for c in v)

    def points(self):
        for pivot in range(4):
            for rest in product(range(self.q), repeat=3-pivot):
                yield ((0,)*pivot + (1,) + rest)

    def roots3(self):
        return [a for a in range(1, self.q) if self.cubes[a] == 1]

    def lines(self):
        roots = self.roots3()
        if self.m % 2 == 0:
            assert len(roots) == 3
        else:
            assert roots == [1]
        return [(pairs, a, b) for pairs in MATCHINGS for a in roots for b in roots]

    def incidence(self, p, line):
        pairs, a, b = line
        (i,j),(k,l)=pairs
        return p[i] == self.mult[a][p[j]] and p[k] == self.mult[b][p[l]]

    def on_surface(self, p):
        return self.cubes[p[0]] ^ self.cubes[p[1]] ^ self.cubes[p[2]] ^ self.cubes[p[3]] == 0


def check_f4_geometry():
    f = FiniteField(2)
    surf = set(p for p in f.points() if f.on_surface(p))
    assert len(surf) == 45
    lines = f.lines()
    assert len(lines)==27
    for line in lines:
        assert sum(f.incidence(p, line) for p in surf)==5
    inc = {p:tuple(i for i,L in enumerate(lines) if f.incidence(p,L)) for p in surf}
    assert Counter(map(len,inc.values())) == {3:45}
    assert sum(len(inds)*(len(inds)-1)//2 for inds in inc.values())==135
    pairs = {}
    for p, ids in inc.items():
        for i,j in combinations(ids,2):
            assert (i,j) not in pairs
            pairs[i,j] = p
    assert len(pairs)==135
    rational = {p for p in surf if all(x in (0,1) for x in p)}
    assert len(rational)==7
    fix_lines = [line for line in lines if all(a==1 for a in line[1:])]
    assert len(fix_lines)==3
    assert {p for p in rational if any(f.incidence(p,L) for L in fix_lines)} == rational
    assert len({p for p in surf if any(f.incidence(p,L) for L in fix_lines)}) == 13
    # F_2 Frobenius action on the incidence graph of the 45 triple points:
    point_fixed = sum(f.norm(tuple(f.mult[x][x] for x in p)) == p for p in surf)
    line_fixed = sum(a == f.mult[a][a] and b == f.mult[b][b] for _,a,b in lines)
    branch_fixed = sum(
        f.norm(tuple(f.mult[x][x] for x in p)) == p and
        lines[i][1] == f.mult[lines[i][1]][lines[i][1]] and
        lines[i][2] == f.mult[lines[i][2]][lines[i][2]]
        for p, ids in inc.items() for i in ids)
    assert (point_fixed, line_fixed, branch_fixed) == (7,3,9)
    # Geometric graph: 27 component vertices + 45 singular-point vertices,
    # 135 branch edges, hence first Betti number 135-72+1=64.
    euler_betti = len(inc)*3 - len(inc) - len(lines) + 1
    frobenius_trace_H1 = branch_fixed - point_fixed - line_fixed + 1
    assert (euler_betti, frobenius_trace_H1)==(64,0)
    print('Incidence graph H1: dim 64, Frobenius eigenmultiplicities +1:32, -1:32')
    assert sum(p.count(0)==2 for p in surf)==18
    assert sum(p.count(0)==0 for p in surf)==27
    # All F4-lines from full projective ambient enumeration: 357 candidate lines.
    ambient = list(f.points())
    candidate_lines=set()
    for i, v in enumerate(ambient):
        for w in ambient[i+1:]:
            points = frozenset(f.norm(tuple(v[t]^f.mult[b][w[t]] for t in range(4)))
                for b in range(f.q))
            points = points.union({f.norm(w)})
            assert len(points)==5
            candidate_lines.add(points)
    assert len(candidate_lines)==357
    on_X = {L for L in candidate_lines if L <= surf}
    assert len(on_X)==27
    matching_lines = {frozenset(p for p in surf if f.incidence(p, line)) for line in lines}
    assert matching_lines==on_X
    print('F4: ambient lines 357, Fermat lines 27, surface points 45, triple points 45')
    print('F2 fixed points 7, fixed lines 3, all fixed points on those lines')
    print('pairwise intersections 135, no additional geometric intersections (all lines F4-defined)')


def check_field(m):
    f = FiniteField(m)
    q = f.q
    lines = f.lines()
    total = boundary = 0
    for p in f.points():
        if not f.on_surface(p):
            continue
        total+=1
        if any(f.incidence(p,line) for line in lines):
            boundary+=1
    # The degree-nine product cuts out the complete reduced 27-line divisor.
    # On points, its vanishing must agree with the union of geometric lines.
    for p in f.points():
        if not f.on_surface(p):
            continue
        product9 = 1
        for j in (1,2,3):
            product9 = f.mult[product9][f.cubes[p[0]] ^ f.cubes[p[j]]]
        assert (product9 == 0) == any(f.incidence(p,L) for L in lines)
    exp_s = q*q+1+q*(7 if m%2==0 else 1)
    exp_d = 27*q-63 if m%2==0 else 3*q+1
    exp_u = (q-4)*(q-16) if m%2==0 else q*(q-2)
    assert total==exp_s, (m, total, exp_s)
    assert boundary==exp_d, (m, boundary, exp_d)
    assert total-boundary==exp_u
    print(f'F_{q}: surface={total}, boundary={boundary}, open={total-boundary}; expected={exp_u}')

if __name__ == '__main__':
    check_f4_geometry()
    for m in range(1,7):
        check_field(m)
    print('VERIFY_OK')
