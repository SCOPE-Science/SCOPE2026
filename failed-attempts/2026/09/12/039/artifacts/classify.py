"""Classify cyclic STS(19) designs up to isomorphism (affine maps); pick A1..A4 reps."""
import itertools

V = 19
nonzero = set(range(1, V))
triples = []
for a in range(1, V):
    for b in range(a + 1, V):
        D = {a, (-a) % V, b, (-b) % V, (b - a) % V, (a - b) % V}
        if len(D) == 6 and 0 not in D:
            triples.append(((0, a, b), frozenset(D)))

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
print("families:", len(families))


def develop(fam):
    blocks = set()
    for t in fam:
        for s in range(V):
            blocks.add(frozenset((x + s) % V for x in t))
    return frozenset(blocks)


def canon(blocks):
    best = None
    for u in range(1, V):
        img = frozenset(frozenset((u * x) % V for x in b) for b in blocks)
        for t in range(V):
            img2 = tuple(sorted(tuple(sorted((x + t) % V for x in b)) for b in img))
            if best is None or img2 < best:
                best = img2
    return best


classes = {}
for f in families:
    B = develop(f)
    assert len(B) == 57, (f, len(B))
    # verify STS: pair cover
    pairs = set()
    for b in B:
        b = sorted(b)
        for e in itertools.combinations(b, 2):
            assert e not in pairs
            pairs.add(e)
    assert len(pairs) == 171
    c = canon(B)
    classes.setdefault(c, []).append(f)

print("isomorphism classes:", len(classes))

# automorphism order of each class rep + one family rep
for c, fs in sorted(classes.items()):
    B = develop(fs[0])
    aut = 0
    for u in range(1, V):
        img = frozenset(frozenset((u * x) % V for x in b) for b in B)
        for t in range(V):
            if frozenset(frozenset((x + t) % V for x in b) for b in img) == B:
                aut += 1
    print("fam_rep=", fs[0], "|Aut|=", aut, "num_fams=", len(fs))

with open("class_reps.txt", "w") as fh:
    for c, fs in sorted(classes.items()):
        fh.write(repr(fs[0]) + "\n")
