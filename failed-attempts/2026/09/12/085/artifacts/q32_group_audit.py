"""Q32 structural audit: center, classes, subgroups, abelianization, cyclic subgroups."""
els = [(i, j) for i in range(16) for j in range(2)]

def mul(x, y):
    i, j = x; k, l = y
    if j == 0:
        return ((i + k) % 16, l)
    else:
        if l == 0:
            return ((i - k) % 16, 1)
        else:
            return ((i - k + 8) % 16, 0)

def inv(x):
    i, j = x
    if j == 0:
        return ((-i) % 16, 0)
    else:
        return ((i + 8) % 16, 1)

import itertools
center = [x for x in els if all(mul(x, y) == mul(y, x) for y in els)]
print("center:", center)
seen, classes = set(), []
for x in els:
    if x in seen:
        continue
    cl = {mul(mul(g, x), inv(g)) for g in els}
    seen |= cl
    classes.append(sorted(cl))
print("num classes:", len(classes))
for c in classes:
    print(len(c), c)
subs = set()
for r in range(1, 4):
    for tup in itertools.combinations(els, r):
        S = {(0, 0)} | set(tup)
        changed = True
        while changed:
            changed = False
            for p in list(S):
                q = inv(p)
                if q not in S:
                    S.add(q); changed = True
                for q2 in list(S):
                    m = mul(p, q2)
                    if m not in S:
                        S.add(m); changed = True
        subs.add(tuple(sorted(S)))
print("num subgroups:", len(subs))

def normalize(S):
    S = set(S)
    return [g for g in els if all(mul(mul(g, s), inv(g)) in S for s in S)]

reps, used = [], set()
for S in subs:
    if S in used:
        continue
    orb = {tuple(sorted([mul(mul(g, s), inv(g)) for s in S])) for g in els}
    used |= orb
    reps.append(S)
print("subgroup conjugacy reps:", len(reps))
for S in sorted(reps, key=len):
    print(f"order {len(S)} N-order {len(normalize(S))}")
# abelianization
comm = {mul(mul(mul(g, h), inv(g)), inv(h)) for g in els for h in els}
S = {(0, 0)}
while True:
    nS = set(S)
    for p in list(S):
        for q in comm:
            nS.add(mul(p, q))
    added = True
    while added:
        added = False
        for p in list(nS):
            for q in list(nS):
                m = mul(p, q)
                if m not in nS:
                    nS.add(m); added = True
    if nS == S:
        break
    S = nS
print("derived order:", len(S), "|Gab| =", 32 // len(S))
