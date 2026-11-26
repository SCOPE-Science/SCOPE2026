#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations, product
from collections import Counter


def antichains(n):
    subs = list(range(1, 1 << n))
    for mask in range(1, 1 << len(subs)):
        fam = [subs[i] for i in range(len(subs)) if (mask >> i) & 1]
        ok = True
        for i, a in enumerate(fam):
            for b in fam[i+1:]:
                if (a & b) == a or (a & b) == b:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            yield tuple(sorted(fam))


def value(fam, S):
    return int(any((m & S) == m for m in fam))


def proper(n, fam):
    N = (1 << n) - 1
    return all(not (value(fam, S) and value(fam, N ^ S)) for S in range(1 << n))


def pg_formula(n, fam):
    counts = tuple(sum(1 for S in fam if (S >> i) & 1) for i in range(n))
    total = sum(counts)
    return tuple(Fraction(c, total) for c in counts)


def pg_incidence(n, fam):
    inc = []
    for S in fam:
        inc.extend(i for i in range(n) if (S >> i) & 1)
    return tuple(Fraction(inc.count(i), len(inc)) for i in range(n))


def rank_frac(rows):
    if not rows:
        return 0
    M = [list(map(Fraction, row)) for row in rows]
    m, n = len(M), len(M[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        z = M[r][c]
        M[r] = [x / z for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                z = M[i][c]
                M[i] = [M[i][j] - z * M[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r


def solve_unique(A, b, nvars):
    M = [list(map(Fraction, row)) + [Fraction(bb)] for row, bb in zip(A, b)]
    r = 0
    piv = []
    for c in range(nvars):
        p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        z = M[r][c]
        M[r] = [x / z for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                z = M[i][c]
                M[i] = [M[i][j] - z * M[r][j] for j in range(nvars + 1)]
        piv.append(c)
        r += 1
    for row in M:
        if all(row[c] == 0 for c in range(nvars)) and row[nvars] != 0:
            return None
    if len(piv) != nvars:
        return None
    x = [Fraction(0)] * nvars
    for i, c in enumerate(piv):
        x[c] = M[i][nvars]
    return tuple(x)


def nucleolus_exact(n, fam):
    if n == 1:
        return (Fraction(1),), {}
    # Successive exact rational least-core LPs. At each stage the coalitions whose
    # excess is constant at the optimum over all optimal vertices are fixed.
    N = (1 << n) - 1
    coalitions = [S for S in range(1, N)]
    fixed = {}

    while True:
        nvars = n + 1  # allocation coordinates plus epsilon
        eqA = [[Fraction(1)] * n + [Fraction(0)]]
        eqb = [Fraction(1)]
        for S, eps_level in fixed.items():
            eqA.append(
                [Fraction(-1) if (S >> i) & 1 else Fraction(0) for i in range(n)]
                + [Fraction(0)]
            )
            eqb.append(Fraction(eps_level - value(fam, S)))

        inequalities = []
        for S in coalitions:
            if S in fixed:
                continue
            # v(S)-x(S) <= epsilon  <=> -x(S)-epsilon <= -v(S)
            inequalities.append((
                [Fraction(-1) if (S >> i) & 1 else Fraction(0) for i in range(n)]
                + [Fraction(-1)],
                Fraction(-value(fam, S)),
                ("excess", S),
            ))
        for i in range(n):
            row = [Fraction(0)] * (n + 1)
            row[i] = Fraction(-1)
            inequalities.append((row, Fraction(0), ("IR", i)))

        need = nvars - rank_frac(eqA)
        vertices = set()
        choices = [()] if need == 0 else combinations(range(len(inequalities)), need)
        for inds in choices:
            A = list(eqA)
            b = list(eqb)
            for j in inds:
                A.append(inequalities[j][0])
                b.append(inequalities[j][1])
            sol = solve_unique(A, b, nvars)
            if sol is None:
                continue
            if any(sum(a*x for a, x in zip(row, sol)) != bb for row, bb in zip(eqA, eqb)):
                continue
            if any(sum(a*x for a, x in zip(row, sol)) > bb for row, bb, _ in inequalities):
                continue
            vertices.add(sol)
        assert vertices
        eps_star = min(z[-1] for z in vertices)
        opt = [z for z in vertices if z[-1] == eps_star]

        newly = []
        for S in coalitions:
            if S in fixed:
                continue
            if all(
                Fraction(value(fam, S)) - sum(z[i] for i in range(n) if (S >> i) & 1) == eps_star
                for z in opt
            ):
                newly.append(S)
        assert newly
        for S in newly:
            fixed[S] = eps_star

        xrows = [[Fraction(1)] * n]
        xb = [Fraction(1)]
        for S, eps_level in fixed.items():
            xrows.append([Fraction(-1) if (S >> i) & 1 else Fraction(0) for i in range(n)])
            xb.append(Fraction(eps_level - value(fam, S)))
        if rank_frac(xrows) >= n:
            x = solve_unique(xrows, xb, n)
            assert x is not None
            return tuple(x), dict(fixed)


def weak_order(v):
    return tuple((v[i] > v[j]) - (v[i] < v[j])
                 for i in range(len(v)) for j in range(i+1, len(v)))


def relabel_family(fam, p, n):
    out = []
    for S in fam:
        T = 0
        for i in range(n):
            if (S >> i) & 1:
                T |= 1 << p[i]
        out.append(T)
    return tuple(sorted(out))


def canonical_family(fam, n):
    return min(relabel_family(fam, p, n) for p in permutations(range(n)))


def weighted_rep(n, fam, maxw=6):
    truth = [value(fam, S) for S in range(1 << n)]
    for w in product(range(maxw + 1), repeat=n):
        if not any(w):
            continue
        total = sum(w)
        for q in range(1, total + 1):
            if all(int(sum(w[i] for i in range(n) if (S >> i) & 1) >= q) == truth[S]
                   for S in range(1 << n)):
                return q, w
    return None


proper_counts = {}
class_counts = {}
div_counts = {}
div_orbits = Counter()
orbit_data = {}
nodummy_total = 0
nodummy_div = 0

for n in range(1, 5):
    classes = Counter()
    for fam in antichains(n):
        if proper(n, fam):
            classes[canonical_family(fam,n)] += 1
    proper_counts[n] = sum(classes.values())
    class_counts[n] = len(classes)
    dc = 0
    for c, orbit in classes.items():
        pg1 = pg_formula(n,c)
        pg2 = pg_incidence(n,c)
        assert pg1 == pg2 and sum(pg1) == 1
        nu,_ = nucleolus_exact(n,c)
        assert sum(nu) == 1 and all(x >= 0 for x in nu)
        if weak_order(pg1) != weak_order(nu):
            dc += orbit
            if n == 4:
                div_orbits[c] = orbit
                orbit_data[c] = (pg1,nu)
        if n == 4 and all(pg1[i] > 0 for i in range(n)):
            nodummy_total += orbit
            if weak_order(pg1) != weak_order(nu):
                nodummy_div += orbit
    div_counts[n] = dc

assert proper_counts == {1:1, 2:3, 3:11, 4:80}
assert class_counts == {1:1, 2:2, 3:5, 4:14}
assert div_counts == {1:0, 2:0, 3:0, 4:18}
assert div_orbits == Counter({(3,5):12, (3,13,14):6})
assert nodummy_total == 50
assert nodummy_div == 6

expected = {
    (3,5): {
        "orbit":12,
        "pg":(Fraction(1,2), Fraction(1,4), Fraction(1,4), Fraction(0)),
        "nu":(Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "weighted":(3,(2,1,1,0)),
    },
    (3,13,14): {
        "orbit":6,
        "pg":(Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(1,4)),
        "nu":(Fraction(1,3), Fraction(1,3), Fraction(1,6), Fraction(1,6)),
        "weighted":(4,(2,2,1,1)),
    },
}
for c,e in expected.items():
    assert orbit_data[c] == (e["pg"], e["nu"])
    assert weighted_rep(4, c) == e["weighted"]

# Direct independent certificates for the two divergent canonical games.
assert expected[(3,5)]["nu"] == (1,0,0,0)

a,b,c,d = expected[(3,13,14)]["nu"]
assert (a,b,c,d) == (Fraction(1,3),Fraction(1,3),Fraction(1,6),Fraction(1,6))
assert max(Fraction(1)-a-b, b, a) == Fraction(1,3)

# All three-player simple games, not merely proper ones, also agree ordinally.
all3_classes = Counter(canonical_family(f,3) for f in antichains(3))
all3div = 0
for c,orbit in all3_classes.items():
    if weak_order(pg_formula(3,c)) != weak_order(nucleolus_exact(3,c)[0]):
        all3div += orbit
assert sum(all3_classes.values()) == 18
assert all3div == 3
assert [c for c,o in all3_classes.items() if weak_order(pg_formula(3,c)) != weak_order(nucleolus_exact(3,c)[0])] == [(1,6)]
assert pg_formula(3,(1,6)) == (Fraction(1,3),)*3
assert nucleolus_exact(3,(1,6))[0] == (Fraction(1,2),Fraction(1,4),Fraction(1,4))

print("VERIFY_OK")
print("proper_counts", proper_counts)
print("proper_isomorphism_classes", class_counts)
print("divergence_counts", div_counts)
print("four_player_divergent_orbits", dict(div_orbits))
for c,e in expected.items():
    print("orbit", c, "count", e["orbit"], "PG", e["pg"], "nucleolus", e["nu"], "weighted", e["weighted"])
print("proper_nodummy", nodummy_total)
print("divergent_nodummy", nodummy_div)
print("all_three_player_simple_games", sum(all3_classes.values()), "divergent", all3div)
