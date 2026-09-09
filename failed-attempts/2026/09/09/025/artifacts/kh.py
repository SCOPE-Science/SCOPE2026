"""Khovanov complex builder over Z (and F_p) from the cube enumerator.
Grading conventions (unreduced, integral):
  For a state with hamming weight h (number of B-smoothings) and r circles:
    homological grading i = h - n_-.
    The chain group at height h is V^{otimes r}{h + n_+ - 2 n_-} with
    deg(v_+) = +1, deg(v_-) = -1 (q-shift UP by h+n_+-2n_- ... standard:
    C^{i,j} with j = h + n_+ - 2n_- + (#plus - #minus)).
  Differentials: for each edge (flip one A-smoothing to B at crossing j):
    if two circles merge into one: m: v_+\otimes v_+ -> v_+, v_+\otimes v_-/v_-\otimes v_+ -> v_-, v_-\otimes v_- -> 0.
    if one circle splits into two: Delta: v_+ -> v_+\otimes v_- + v_-\otimes v_+, v_- -> v_-\otimes v_-.
    Sign: (-1)^{# B-smoothings before j}.
  We need, per state, the actual circle arcs (which arc-segment belongs to which
  circle) to determine merge/split and the tensor-slot mapping. circle_labels()
  returns per-state: list over UF nodes of root ids + the 4 active port nodes per
  crossing + entry arcs. From this, for an edge flipping crossing j, compare
  circle partitions before/after restricted to arcs away from crossing j.
Implementation: represent each state's circles via frozensets of 'arc ids'.
Arc ids: entry[j][p] ids (shared) + crossing-internal ports. Simpler: recompute
UF per state (as in cube.count_circles) but ALSO return mapping. Then for edge
j: circles of state0 restricted to nodes not internal to crossing j give a
partition; count how the two circles through the 4 ports merge/split.
"""
import itertools
from cube import UF, CONV

def build_state(word, nstrands, smooth):
    """Returns (uf_roots dict node->root, entry ids, ports per crossing)."""
    m = len(word)
    uf = UF()
    entry = [[uf.node() for _ in range(nstrands)] for _ in range(m + 1)]
    ports = []
    for j, (i, s) in enumerate(word):
        a = i - 1
        ta, tb, ba, bb = uf.node(), uf.node(), uf.node(), uf.node()
        uf.union(ta, entry[j][a]); uf.union(tb, entry[j][a + 1])
        uf.union(ba, entry[j + 1][a]); uf.union(bb, entry[j + 1][a + 1])
        if smooth[j] == 0:
            uf.union(ta, ba); uf.union(tb, bb)
        else:
            uf.union(ta, tb); uf.union(ba, bb)
        for p in range(nstrands):
            if p != a and p != a + 1:
                uf.union(entry[j][p], entry[j + 1][p])
        ports.append((ta, tb, ba, bb))
    for p in range(nstrands):
        uf.union(entry[m][p], entry[0][p])
    return uf, entry, ports

def state_circles(word, nstrands, smooth):
    """Circle partition as frozenset of frozensets of entry-arc ids + internal ports.
    Uses canonical node ids (same construction each call, so ids comparable across
    states with the same word)."""
    uf, entry, ports = build_state(word, nstrands, smooth)
    groups = {}
    for v in range(len(uf.p)):
        r = uf.find(v)
        groups.setdefault(r, []).append(v)
    return frozenset(frozenset(g) for g in groups.values())

def edge_map(word, nstrands, s0, j):
    """Flip crossing j (A->B). Returns (kind, circles_before, circles_after, slot info).
    kind 'merge' or 'split'. Circles identified by frozensets; slot maps give ordered
    tensor factors for m/Delta. We order circles canonically by min element."""
    m = len(word)
    A = tuple(CONV[s] for _, s in word)
    assert s0[j] == A[j], "edge must start at A-smoothing"
    s1 = list(s0); s1[j] = 1 - s1[j]; s1 = tuple(s1)
    C0 = state_circles(word, nstrands, s0)
    C1 = state_circles(word, nstrands, s1)
    # circles through crossing j's ports: find circles containing the port nodes
    _, entry0, ports0 = build_state(word, nstrands, s0)
    ta, tb, ba, bb = ports0[j]
    # map node -> circle
    n2c0 = {}
    for c in C0:
        for v in c:
            n2c0[v] = c
    c_ta = n2c0[ta]; c_tb = n2c0[tb]
    if c_ta == c_tb:
        kind = "split"
    else:
        kind = "merge"
    return kind, C0, C1, s1

def chain_basis(word, nstrands, n_plus, n_minus):
    """Enumerate basis: dict (h, q) -> list of basis elements; each element is
    (state_tuple, signs_tuple) with signs per circle (ordered by canonical circle order).
    Returns also state circle orders: dict state -> ordered circle list."""
    m = len(word)
    A = tuple(CONV[s] for _, s in word)
    basis = {}
    orders = {}
    for bits in itertools.product([0, 1], repeat=m):
        h = sum(1 for j in range(m) if bits[j] != A[j])  # #B-smoothings
        C = state_circles(word, nstrands, bits)
        order = sorted([sorted(c) for c in C], key=lambda c: c[0])
        order = [frozenset(c) for c in order]
        orders[bits] = order
        r = len(order)
        for signs in itertools.product([1, -1], repeat=r):
            q = h + n_plus - 2 * n_minus + sum(signs)
            i = h - n_minus
            basis.setdefault((i, q), []).append((bits, signs))
    return basis, orders
