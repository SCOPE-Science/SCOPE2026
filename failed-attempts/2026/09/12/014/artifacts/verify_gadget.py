"""Finite-level audit of graph->Toeplitz coding gadget for lane-1084 target.

Checks:
 (a) naive bit-coding is NOT invariant under letter-flip pointed conjugacy
     (explicit star-vs-complement collision on 4 vertices);
 (b) pair-coding repair restores flip-invariance (verified over all 2^6 graphs);
 (c) marker-based scale-fixing yields separated holes (computed, demo skeleton);
 (d) hole-density table shows zero-entropy constraint is satisfiable (not blocker).
Implication (cited, not proved here): Kaya/Li separated-holes+growing-blocks =>
 hyperfinite, and hyperfinite (<= E0) is strictly below graph isomorphism,
 so marker-fixed gadgets cannot witness Borel completeness.
"""
import itertools

PAIRS = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def complement_edges(edges):
    s = set(tuple(sorted(e)) for e in edges)
    return [p for p in PAIRS if p not in s]


def deg_seq(edges):
    d = [0] * 4
    for a, b in edges:
        d[a] += 1
        d[b] += 1
    return sorted(d)


def perm_iso(edges1, edges2):
    s2 = set(tuple(sorted(e)) for e in edges2)
    for perm in itertools.permutations(range(4)):
        if {tuple(sorted((perm[a], perm[b]))) for a, b in edges1} == s2:
            return True
    return False


def code_naive(edges):
    s = set(tuple(sorted(e)) for e in edges)
    return [1 if p in s else 0 for p in PAIRS]


def decode_naive(bits):
    return [p for p, b in zip(PAIRS, bits) if b == 1]


# (a) naive flip collision
STAR = [(0, 1), (0, 2), (0, 3)]
CSTAR = complement_edges(STAR)
print("STAR degs:", deg_seq(STAR), "complement degs:", deg_seq(CSTAR))
print("STAR iso complement?", perm_iso(STAR, CSTAR))
w = code_naive(STAR)
wflip = [1 - b for b in w]
print("code(STAR) =", w, "flip =", wflip, "decode(flip) =", decode_naive(wflip))
assert decode_naive(wflip) == CSTAR
assert not perm_iso(STAR, CSTAR)
print("RESULT (a): naive decoder NOT flip-invariant: letter-flip pointed")
print("  conjugacy sends code(STAR) to code of non-isomorphic complement. COLLISION CONFIRMED.")


# (b) pair-coding repair: present -> 01, absent -> 00;
# flip maps 01 <-> 10 (both decode 'present'), 00 <-> 11 (both 'absent').
def code_pair(edges):
    s = set(tuple(sorted(e)) for e in edges)
    out = []
    for p in PAIRS:
        out += [0, 1] if p in s else [0, 0]
    return out


def decode_pair(bits):
    edges = []
    for i, p in enumerate(PAIRS):
        pat = (bits[2 * i], bits[2 * i + 1])
        if pat in ((0, 1), (1, 0)):
            edges.append(p)
        elif pat in ((0, 0), (1, 1)):
            pass
        else:
            raise ValueError(pat)
    return edges


ok = True
for m in range(64):
    edges = [PAIRS[i] for i in range(6) if (m >> i) & 1]
    wf = [1 - b for b in code_pair(edges)]
    if decode_pair(wf) != edges:
        ok = False
        print("  pair-code FAIL at mask", m)
        break
print("RESULT (b): pair-coding flip-invariant over all 64 graphs on 4 vertices:", ok)
assert ok

# (c) separated holes in a marker-fixed skeleton (period 16 demo)
N = 16
fixed = {0: 0, 4: 0, 8: 0, 12: 0, 2: 1, 6: 1, 10: 1, 14: 1}
holes = [i for i in range(N) if i not in fixed]
gaps = [holes[i + 1] - holes[i] for i in range(len(holes) - 1)]
print("holes:", holes, "gaps:", gaps, "min gap:", min(gaps))
assert min(gaps) >= 2
print("RESULT (c): marker skeleton holes isolated, min gap %d >= 2 (separated-holes form)." % min(gaps))

# (d) density table: n-vertex graph, m edges, pair-coding costs 2m holes at period 2^t
print("n : edges m : holes 2m : level t : period : density")
for n in range(4, 13):
    m = n * (n - 1) // 2
    t = max(4, 2 * n)
    print("%d : %d : %d : %d : %d : %.5f" % (n, m, 2 * m, t, 2 ** t, 2 * m / 2 ** t))
print("RESULT (d): hole density -> 0 along spaced levels; zero-entropy satisfiable, NOT the blocker.")
print("VERIFY_OK")
