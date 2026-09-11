"""E3 definition sanity: Gamma=Z*Z2=<a,b|b^2>, S={a,a^-1,b}.
Checks: 3-regularity, Cayley balls are trees (acyclicity), bipartiteness
via parity homomorphism, Borel edge upper bound <=5 (KST on line graph),
non-hyperfiniteness witness (free subgroup), graphing setup for measurable side.
Stdlib only.
"""
import json
from collections import deque

# Free product Z*Z2 normal forms: words in a^{k} alternating with b.
# Represent element as tuple of tokens: ints (a-power, nonzero) and 'b'.
# Identity = empty tuple. Multiply by a^{+-1} or b with reduction (b^2=1,
# a-powers combine). a-tokens and b-tokens must alternate; two a-tokens merge.

def normalize(tokens):
    # tokens: list of int/'b'; reduce b^2 and merge adjacent ints
    out = []
    for t in tokens:
        if t == 'b':
            if out and out[-1] == 'b':
                out.pop()
            else:
                out.append('b')
        else:  # int
            if t == 0:
                continue
            if out and isinstance(out[-1], int):
                s = out[-1] + t
                out.pop()
                if s != 0:
                    out.append(s)
            else:
                out.append(t)
    return tuple(out)

IDENT = ()

def mul(elem, gen):
    # gen in {'a','A','b'} with A=a^{-1}
    if gen == 'a':
        return normalize(list(elem) + [1])
    if gen == 'A':
        return normalize(list(elem) + [-1])
    if gen == 'b':
        return normalize(list(elem) + ['b'])
    raise ValueError

GENS = ['a', 'A', 'b']
INV = {'a': 'A', 'A': 'a', 'b': 'b'}

def ball(radius):
    seen = {IDENT: 0}
    q = deque([IDENT])
    while q:
        x = q.popleft()
        d = seen[x]
        if d == radius:
            continue
        for g in GENS:
            y = mul(x, g)
            if y not in seen:
                seen[y] = d + 1
                q.append(y)
    return seen

def cayley_edges(seen):
    E = set()
    for x in seen:
        for g in GENS:
            y = mul(x, g)
            if y in seen:
                E.add(frozenset((x, y)))
    return E

results = {}
for R in [1, 2, 3, 4, 5]:
    seen = ball(R)
    E = cayley_edges(seen)
    n, m = len(seen), len(E)
    # tree check on induced subgraph: connected? acyclic? m == n-1
    results[R] = {"n": n, "m": m, "tree": (m == n - 1)}

# degree of identity (distinct neighbors)
nbrs = set(mul(IDENT, g) for g in GENS)
results["deg_e"] = len(nbrs)
assert len(nbrs) == 3, "must be 3-regular"

# bipartiteness: parity homomorphism phi(a)=1, phi(b)=1 mod 2
def parity(elem):
    p = 0
    for t in elem:
        if t == 'b':
            p += 1
        else:
            p += (t % 2)  # a^k contributes k mod 2
    return p % 2

seen5 = ball(5)
E5 = cayley_edges(seen5)
bip_ok = all(parity(u) != parity(v) for e in E5 for (u, v) in [tuple(e)])
results["bipartite_ball5"] = bool(bip_ok)

# non-backtracking closed walk check (acyclicity beyond tree counts):
# BFS non-backtracking returns to origin: count closed NB walks length<=8
def count_closed_nb(L):
    # state (node, prev_gen_used_to_arrive); start with None
    cur = { (IDENT, None): 1 }
    closed = {}
    for step in range(1, L + 1):
        nxt = {}
        for (x, pg), c in cur.items():
            for g in GENS:
                if pg is not None and g == INV[pg]:
                    continue  # no backtrack
                y = mul(x, g)
                k = (y, g)
                nxt[k] = nxt.get(k, 0) + c
        cur = nxt
        closed[step] = cur.get((IDENT, None), 0)  # can't return with None prev; use any-prev at IDENT
        # sum over prev at IDENT
        closed[step] = sum(c for (x, pg), c in cur.items() if x == IDENT)
    return closed

results["closed_nb_walks_len1_8"] = count_closed_nb(8)

# F2 subgroup witness: u=a^2, v=b a^2 b. Verify no short relation =1.
u = normalize([2])
v = normalize(['b', 2, 'b'])
def word_in_uv(syms):
    # syms: list of ('u',e) with e=+-1
    toks = []
    for name, e in syms:
        base = list(u) if name == 'u' else list(v)
        if e == -1:
            # invert: reverse order, negate ints (b self-inverse)
            inv = []
            for t in reversed(base):
                inv.append(t if t == 'b' else -t)
            base = inv
        toks.extend(base)
    return normalize(toks)

from itertools import product
free_ok = True
checked = 0
for L in range(1, 7):
    for w in product(['u', 'v'], repeat=L):
        for signs in product([1, -1], repeat=L):
            # skip unreduced (adjacent same generator opposite signs cancel trivially? still check)
            syms = list(zip(w, signs))
            # skip words with immediate cancellation u u^{-1}
            red = True
            for i in range(len(syms) - 1):
                if syms[i][0] == syms[i+1][0] and syms[i][1] == -syms[i+1][1]:
                    red = False
                    break
            if not red:
                continue
            checked += 1
            if word_in_uv(syms) == IDENT:
                free_ok = False
results["F2_witness"] = {"u": "a^2", "v": "ba^2b", "no_relation_upto_len6": bool(free_ok), "words_checked": checked}

# Borel upper bound <=5: line graph max degree = 2(Delta-1) = 4 -> KST chi_B <= 5.
results["borel_upper_le5"] = {"Delta": 3, "Delta_line": 4, "KST_bound": 5}
# Measurable setup: Bernoulli graphing, invariant product measure.
results["graphing"] = {"group": "Z*Z2 nonamenable (contains F2 above)",
                        "space": "Free(2^Gamma) conull, product measure",
                        "degree": 3, "bipartite": True,
                        "measurable_upper": "<=4 via Csoka-Lippner-Pikhurko/Grebik-Pikhurko Vizing-type bound"}

print(json.dumps(results, indent=1, default=str))
with open("output/artifacts/e3_definition.json", "w") as f:
    json.dump(results, f, indent=1, default=str)
print("WROTE output/artifacts/e3_definition.json")
