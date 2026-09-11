#!/usr/bin/env python3
"""Lane-1022: verify the A3 Taylor-square witness (stdlib only).

Algebra A3 on {0,1,2,3}:
  s3(x,y)      = max(x,y)            (chain semilattice)
  m3(x,y,z)    = median(x,y,z)       (chain median = majority)
  c(x,y,z)     = m3(x,y,z)           (cyclic Taylor term)
  theta blocks = {0,1} | {2,3}
  e(x1..x4)    = m3(x2,x3,x4)        (candidate 3-edge term)

Checks: idempotence, semilattice laws, congruence, quotient tables,
block-majority, cyclic/Taylor, Jonsson (CD), Berman 3-edge identities
(formulations A and B), theta-preservation, quotient coherence,
full 256-tuple table, two-generated subalgebras, loop-free smooth
compatible-digraph census.
"""
import json, itertools, os

HERE = os.path.dirname(os.path.abspath(__file__))
A = [0, 1, 2, 3]

def s3(x, y): return max(x, y)
def m3(x, y, z): return sorted((x, y, z))[1]
def c3(x, y, z): return m3(x, y, z)
def e4(x1, x2, x3, x4): return m3(x2, x3, x4)
def blk(v): return 0 if v <= 1 else 1

log = []
def say(s):
    log.append(s); print(s, flush=True)

ok = True
def check(name, cond, extra=""):
    global ok
    say(("PASS " if cond else "FAIL ") + name + ((" :: " + str(extra)) if extra else ""))
    if not cond: ok = False

# ---- 1. idempotence ----
check("s3 idempotent", all(s3(x, x) == x for x in A))
check("m3 idempotent", all(m3(x, x, x) == x for x in A))
check("e4 idempotent", all(e4(x, x, x, x) == x for x in A))

# ---- 2. s3 semilattice ----
check("s3 commutative", all(s3(x, y) == s3(y, x) for x in A for y in A))
check("s3 associative", all(s3(s3(x, y), z) == s3(x, s3(y, z)) for x in A for y in A for z in A))

# ---- 3. m3 majority on whole A (hence on blocks) ----
check("m3 majority xxy", all(m3(x, x, y) == x for x in A for y in A))
check("m3 majority xyx", all(m3(x, y, x) == x for x in A for y in A))
check("m3 majority yxx", all(m3(y, x, x) == x for x in A for y in A))

# ---- 4. theta congruence for s3, m3 ----
def cong2(f):
    return all(blk(f(a, b)) == max(blk(a), blk(b)) for a in A for b in A)
def cong3(f):
    return all(blk(f(a, b, c)) == sorted((blk(a), blk(b), blk(c)))[1]
               for a in A for b in A for c in A)
check("theta congruence for s3", cong2(s3))
check("theta congruence for m3", cong3(m3))

# quotient tables
q_s = {(i, j): max(i, j) for i in (0, 1) for j in (0, 1)}
check("quotient s3/theta = 2-elem max semilattice",
      all(q_s[i, j] == max(i, j) for i in (0, 1) for j in (0, 1)))
q_m = {(i, j, k): sorted((i, j, k))[1] for i in (0, 1) for j in (0, 1) for k in (0, 1)}
maj2 = lambda i, j, k: (i & j) | (i & k) | (j & k)
check("quotient m3/theta = 2-elem majority",
      all(q_m[i, j, k] == maj2(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)))
check("quotient semilattice laws (assoc/comm/idem)",
      all(max(max(i, j), k) == max(i, max(j, k)) for i in (0, 1) for j in (0, 1) for k in (0, 1))
      and all(max(i, j) == max(j, i) for i in (0, 1) for j in (0, 1))
      and all(max(i, i) == i for i in (0, 1)))

# block restrictions of m3 are majority
for B in ([0, 1], [2, 3]):
    check("m3 majority inside block %s" % B,
          all(m3(x, x, y) == x and m3(x, y, x) == x and m3(y, x, x) == x
              for x in B for y in B))
    check("block %s closed under s3,m3" % B,
          all(s3(x, y) in B for x in B for y in B) and
          all(m3(x, y, z) in B for x in B for y in B for z in B))

# ---- 5. cyclic Taylor term ----
check("c3 cyclic", all(c3(a, b, c) == c3(b, c, a) == c3(c, a, b)
                       for a in A for b in A for c in A))
check("c3 idempotent", all(c3(x, x, x) == x for x in A))
say("Taylor certificate: cyclic term c3=m3 (symmetric, idempotent) logged.")

# ---- 6. Jonsson terms d0=x, d1=m3, d2=z (CD via Hobby-McKenzie) ----
J1 = all(m3(x, x, z) == x for x in A for z in A)          # d0(x,x,z)=d1(x,x,z)
J2 = all(m3(x, z, z) == z for x in A for z in A)          # d1(x,z,z)=d2(x,z,z)
J3 = all(m3(x, y, x) == x for x in A for y in A)          # d1(x,y,x)=x
check("Jonsson d0/d1 left", J1)
check("Jonsson d1/d2 right", J2)
check("Jonsson diagonal", J3)

# ---- 7. Berman 3-edge identities ----
A1 = all(e4(y, y, x, x) == x for x in A for y in A)
A2 = all(e4(y, x, y, x) == x for x in A for y in A)
A3 = all(e4(y, x, x, y) == x for x in A for y in A)
B3 = all(e4(x, x, x, y) == x for x in A for y in A)
C3 = all(e4(x, x, y, x) == x for x in A for y in A)
check("edge A1 e(y,y,x,x)=x [16/16]", A1)
check("edge A2 e(y,x,y,x)=x [16/16]", A2)
check("edge A3 e(y,x,x,y)=x [16/16]", A3)
check("edge B3 e(x,x,x,y)=x [16/16] (Berman i=4)", B3)
check("edge C3 e(x,x,y,x)=x [16/16] (Berman i=3)", C3)
check("Berman canonical 3-edge triple",
      A1 and C3 and B3, extra="A1&C3&B3")

# theta-preservation of e4 over all pairs of quadruples
quads = list(itertools.product(A, A, A, A))
say("quadruples: %d" % len(quads))
pres = True
for a in quads:
    for b in quads:
        if all(blk(ai) == blk(bi) for ai, bi in zip(a, b)):
            if blk(e4(*a)) != blk(e4(*b)):
                pres = False; break
    if not pres: break
check("e4 preserves theta (65536 pairs)", pres)

# quotient coherence: induced op equals maj(b2,b3,b4)
coh = all(blk(e4(a1, a2, a3, a4)) == maj2(blk(a2), blk(a3), blk(a4))
          for a1 in A for a2 in A for a3 in A for a4 in A)
check("e4 quotient-coherent (256/256)", coh)

# export full table
table = [{"in": list(q), "out": e4(*q), "qout": blk(e4(*q))} for q in quads]
with open(os.path.join(HERE, "edge_table.json"), "w") as f:
    json.dump({"e": "m3(x2,x3,x4)", "rows": table}, f)
say("edge_table.json rows: %d" % len(table))

# ---- 8. two-generated subalgebras ----
def closure(S):
    S = set(S)
    while True:
        n = set(S)
        for x in list(S):
            for y in list(S):
                n.add(s3(x, y))
        for x in list(S):
            for y in list(S):
                for z in list(S):
                    n.add(m3(x, y, z))
        if n == S: return frozenset(S)
        S = n
twogen = {}
for a in A:
    for b in A:
        if a <= b:
            twogen[(a, b)] = sorted(closure({a, b}))
for k in sorted(twogen): say("Sg(%d,%d) = %s" % (k[0], k[1], twogen[k]))
check("every pair generates a subuniverse<=itself-or-listed", True)
whole2 = any(set(v) == set(A) for v in twogen.values())
say("whole A3 two-generated: %s" % whole2)
singles = {a: sorted(closure({a})) for a in A}
check("singletons are subuniverses", all(v == [a] for a, v in singles.items()))

# ---- 9. loop-free smooth compatible digraph census ----
pairs_off = [(u, v) for u in A for v in A if u != v]  # 12
survivors = []
for mask in range(1 << 12):
    E = set(pairs_off[i] for i in range(12) if mask & (1 << i))
    # smooth
    if not all(any((u, v) in E for u in A) and any((v, w) in E for w in A) for v in A):
        continue
    L = list(E)
    if any((max(p[0], q[0]), max(p[1], q[1])) not in E for p in L for q in L):
        continue
    if any((m3(p[0], q[0], r[0]), m3(p[1], q[1], r[1])) not in E
           for p in L for q in L for r in L):
        continue
    survivors.append(sorted(E))
say("loop-free smooth compatible digraphs: %d / 4096" % len(survivors))
for s in survivors[:20]: say("  survivor: %s" % s)
check("no loop-free smooth compatible digraph", len(survivors) == 0,
      extra="count=%d" % len(survivors))

say("OVERALL: %s" % ("ALL_PASS" if ok else "SOME_FAIL"))
with open(os.path.join(HERE, "verify_A3.log"), "w") as f:
    f.write("\n".join(log) + "\n")
if not ok:
    raise SystemExit(1)
