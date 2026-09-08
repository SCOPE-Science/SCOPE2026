"""Symmetry reduction for unordered pairs of length-4 patterns.
Trivial Wilf-equivalences (dihedral + inverse) act diagonally on pairs.
Computes orbits, checks reps.txt covers each class exactly once, and prints
single-pattern classes + pair-class sizes. Stdlib only."""
import itertools

def rev(p):
    return p[::-1]

def comp(p):
    k = len(p)
    return tuple(k + 1 - x for x in p)

def inv(p):
    k = len(p)
    q = [0] * k
    for i, v in enumerate(p):
        q[v - 1] = i + 1
    return tuple(q)

GENS = (rev, comp, inv)

def orbit(p):
    seen = {p}
    stack = [p]
    while stack:
        q = stack.pop()
        for f in GENS:
            r = f(q)
            if r not in seen:
                seen.add(r)
                stack.append(r)
    return frozenset(seen)

def pair_orbit(a, b):
    start = tuple(sorted([a, b]))
    out = set()
    stack = [(a, b)]
    while stack:
        x, y = stack.pop()
        key = tuple(sorted([x, y]))
        if key in out:
            continue
        out.add(key)
        for f in GENS:
            stack.append((f(x), f(y)))
    return out

perms = list(itertools.permutations([1, 2, 3, 4]))
# single-pattern classes
seen = set()
sclasses = []
for p in perms:
    if p in seen:
        continue
    o = orbit(p)
    sclasses.append(sorted(o))
    seen |= set(o)
print("single classes:", len(sclasses), sorted(len(o) for o in sclasses))
# pair classes
seenP = set()
reps = []
for i in range(24):
    for j in range(i + 1, 24):
        key = tuple(sorted([perms[i], perms[j]]))
        if key in seenP:
            continue
        o = pair_orbit(perms[i], perms[j])
        reps.append(key)
        seenP |= o
print("pair classes:", len(reps))
# check reps.txt
mine = []
with open("output/artifacts/reps.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        a, b = line.split("|")
        pa = tuple(int(x) for x in a.split(","))
        pb = tuple(int(x) for x in b.split(","))
        mine.append(tuple(sorted([pa, pb])))
print("reps.txt entries:", len(mine))
assert len(set(mine)) == len(mine), "duplicate reps!"
covered = set()
for m in mine:
    covered |= pair_orbit(*m)
print("classes covered:", sum(1 for r in reps if r in covered), "/", len(reps),
      "| total pairs covered:", len(covered), "(expect 276)")
assert len(covered) == 276 and all(r in covered for r in reps)
# canonical-form check: is each rep the lex-min of its orbit?
nonmin = [m for m in mine if m != min(pair_orbit(*m))]
print("non-lex-min reps:", len(nonmin))
print("OK")
