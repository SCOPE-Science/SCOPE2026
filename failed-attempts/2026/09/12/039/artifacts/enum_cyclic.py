"""Enumerate cyclic STS(19) difference families, classify under multipliers."""
import itertools

V = 19
nonzero = set(range(1, V))

# normalized base triples {0,a,b}, 0<a<b, with 6 distinct nonzero differences
triples = []
for a in range(1, V):
    for b in range(a + 1, V):
        D = {a, (-a) % V, b, (-b) % V, (b - a) % V, (a - b) % V}
        if len(D) == 6 and 0 not in D:
            triples.append(((0, a, b), frozenset(D)))

print("num good triples:", len(triples))

# exact cover of nonzero residues by 3 diffsets
families = []
n = len(triples)
for i in range(n):
    for j in range(i + 1, n):
        if triples[i][1] & triples[j][1]:
            continue
        rest = nonzero - triples[i][1] - triples[j][1]
        for k in range(j + 1, n):
            if triples[k][1] == rest:
                families.append((triples[i][0], triples[j][0], triples[k][0]))
print("num families (ordered):", len(families))


def normalize(t):
    # translate so min is 0, sort
    m = min(t)
    return tuple(sorted((x - m) % V for x in t))


def mult_apply(fam, m):
    out = []
    for t in fam:
        out.append(normalize(tuple((m * x) % V for x in t)))
    return tuple(sorted(out))


def canon(fam):
    return min(mult_apply(fam, m) for m in range(1, V))


classes = {}
for f in families:
    c = canon(f)
    classes.setdefault(c, []).append(f)

print("num multiplier classes:", len(classes))
for c in sorted(classes):
    print(c, "count=", len(classes[c]))
