"""Independent cross-check: brute-force pattern avoidance via itertools for n<=9,
plus witness verification. Independent algorithm from census.c (no shared code)."""
import itertools, json

def avoids(p, pats):
    n = len(p)
    for q in pats:
        if len(q) != 4:
            continue
        for idx in itertools.combinations(range(n), 4):
            vals = [p[i] for i in idx]
            s = sorted(vals)
            rank = tuple(s.index(v) + 1 for v in vals)
            if rank == q:
                return False
    return True

A = [(1,3,4,2),(1,4,2,3)]
B = [(1,3,4,2),(1,4,3,2)]
res = {}
for n in range(0, 10):
    ca = cb = 0
    for p in itertools.permutations(range(1, n+1)):
        if avoids(p, A): ca += 1
        if avoids(p, B): cb += 1
    res[n] = (ca, cb)
    print(n, ca, cb, "DIFF" if ca != cb else "same")
    assert ca == cb, f"split at {n}"

def check(p, cls):
    pats = A if cls=='A' else B
    return avoids(tuple(p), pats)

# witnesses recorded by census engine
witA = {6:[6,2,5,4,3,1],7:[7,3,6,5,4,2,1],8:[8,4,7,6,5,3,2,1],9:[9,5,8,7,6,4,3,2,1]}
witB = {6:[6,2,5,3,4,1],7:[7,3,6,4,5,2,1],8:[8,4,7,5,6,3,2,1],9:[9,5,8,6,7,4,3,2,1]}
for n,w in witA.items():
    assert check(w,'A') and not check(w,'B'), (n,w)
    print(f"witA n={n} ok: in A\\B")
for n,w in witB.items():
    assert check(w,'B') and not check(w,'A'), (n,w)
    print(f"witB n={n} ok: in B\\A")
print("CROSSCHECK_OK")
