"""Full census + Inn certificate for variant B (genuine mirror), to confirm n3=1 there too."""
from itertools import permutations, product
import itertools
from collections import deque, Counter

elems = list(permutations([0, 1, 2]))
idx = {p: i for i, p in enumerate(elems)}
one = (0, 1, 2)

def comp2(a, b):
    return tuple(b[a[i]] for i in range(3))

def inv(a):
    q = [0] * 3
    for i in range(3):
        q[a[i]] = i
    return tuple(q)

def mul(a, b):
    if a < 6 and b < 6:
        return idx[comp2(elems[a], elems[b])]
    elif a < 6 and b >= 6:
        return 6 + idx[comp2(elems[b - 6], elems[a])]
    elif a >= 6 and b < 6:
        return 6 + idx[comp2(elems[a - 6], inv(elems[b]))]
    else:
        return idx[comp2(inv(elems[b - 6]), elems[a - 6])]

e = idx[one]
assert all(mul(e, a) == a and mul(a, e) == a for a in range(12)), "identity fails"
mouf = all(mul(mul(x, y), mul(z, x)) == mul(x, mul(mul(y, z), x))
           for x, y, z in product(range(12), repeat=3))
nfail = sum(1 for x, y, z in product(range(12), repeat=3)
            if mul(mul(x, y), z) != mul(x, mul(y, z)))
print("B: moufang", mouf, "assoc failures", nfail)

def order(x):
    cur = x
    for k in range(2, 13):
        cur = mul(cur, x)
        if cur == e:
            return k
    return None
print("B: order distribution", dict(Counter(order(x) for x in range(12))))

subs = [set(c) for c in itertools.combinations(range(12), 3) if e in c
        and all(mul(a, b) in set(c) for a in c for b in c)]
print("B: n3 =", len(subs), [sorted(s) for s in subs])

# all subloop orders
allsubs = []
for r in range(1, 13):
    for c in itertools.combinations(range(12), r):
        if e not in c:
            continue
        s = set(c)
        if all(mul(a, b) in s for a in s for b in s):
            allsubs.append(sorted(s))
print("B: subloop order distribution:", dict(Counter(len(s) for s in allsubs)))

def perm(f):
    return tuple(f(a) for a in range(12))

L = [perm(lambda a, x=x: mul(x, a)) for x in range(12)]
R = [perm(lambda a, x=x: mul(a, x)) for x in range(12)]

def comp(p, q):
    return tuple(p[q[i]] for i in range(12))

def pinv(p):
    q = [0] * 12
    for i, v in enumerate(p):
        q[v] = i
    return tuple(q)

gens = set()
for x in range(12):
    gens.add(comp(R[x], pinv(L[x])))
    gens.add(comp(pinv(L[x]), R[x]))
for x in range(12):
    for y in range(12):
        gens.add(comp(pinv(L[mul(x, y)]), comp(L[x], L[y])))
        gens.add(comp(pinv(R[mul(x, y)]), comp(R[y], R[x])))
gens.discard(tuple(range(12)))
gl = list(gens)
seen = {tuple(range(12))}
dq = deque([tuple(range(12))])
gi = [pinv(g) for g in gl]
allg = gl + gi
while dq:
    cur = dq.popleft()
    for g in allg:
        nxt = comp(g, cur)
        if nxt not in seen:
            seen.add(nxt)
            dq.append(nxt)
print("B: |Inn| =", len(seen), "#gen perms:", len(gl))
S = subs[0]
print("B: every generator fixes S setwise:",
      all(sorted(g[a] for a in S) == sorted(S) for g in gl))
print("B: every Inn element fixes S setwise:",
      all(set(g[a] for a in S) == S for g in seen))
orbs = []
vis = [False] * 12
for i in range(12):
    if not vis[i]:
        s = set(g[i] for g in seen)
        for j in s:
            vis[j] = True
        orbs.append(sorted(s))
print("B: point orbits:", sorted(orbs))
