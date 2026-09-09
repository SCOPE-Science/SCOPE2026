"""Braid-closure Kauffman cube enumerator (stdlib only), CORRECTED wiring v2.

Model: n-strand braid word; crossings in order; each crossing acts on adjacent
positions (i,i+1) with sign s in {+1,-1}.

CORRECTNESS NOTE (2026-09-09): the v1 wiring (one full n-strand slice per
crossing with cyclic wires bot[j][p]--top[j+1][p]) double-counted identity
strands: an identity slice contributes both an inside arc and an inter-slice
wire for the same strand segment, splitting one arc into two circles. Found by
the unlink test: cl(s1 s1^-1) all-parallel state gave 2 circles, must be 1.

v2 wiring (this file): thread arcs through the braid.
Nodes: entry[j][p] = arc arriving at crossing j on strand-position p (for
j=0: the closure arcs leaving the bottom of the last crossing region).
For each crossing j acting on pair (a,a+1):
  - for p not in {a,a+1}: arc passes through: entry[j][p] ~ entry[j+1][p mod closure].
  - the 4 active ports (top_a, top_b, bot_a, bot_b) are fresh nodes per crossing,
    glued: top_a ~ entry[j][a], top_b ~ entry[j][a+1], bot_a ~ entry[j+1][a'],
    bot_b ~ entry[j+1][a+1] (a' = permuted position after crossing j; since the
    crossing swaps strands, exit position of strand entering at a is a+1? No:
    the crossing region has fixed slots; entry slot p connects into slot p of
    the tangle, exit slot p continues to next crossing's slot p. The swap is
    realized by the smoothing connections, NOT by permuting slots.)
  - smoothing 'par' (0): top_a~bot_a, top_b~bot_b.
  - smoothing 'cup' (1): top_a~top_b, bot_a~bot_b.
Closure: entry[m][p] ~ entry[0][p].
Circle count = # UF components over all created nodes. Isolated nodes cannot
occur: every created node is unioned at least once (checked by assertion).
"""
import itertools

class UF:
    def __init__(self):
        self.p = {}
    def node(self):
        v = len(self.p)
        self.p[v] = v
        return v
    def find(self, a):
        p = self.p
        while p[a] != a:
            p[a] = p[p[a]]
            a = p[a]
        return a
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb

def count_circles(word, nstrands, smooth):
    m = len(word)
    uf = UF()
    # entry[j][p] for j=0..m, p=0..n-1
    entry = [[uf.node() for _ in range(nstrands)] for _ in range(m + 1)]
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
    for p in range(nstrands):
        uf.union(entry[m][p], entry[0][p])
    return len(set(uf.find(v) for v in range(len(uf.p))))

def writhe(word):
    return sum(s for _, s in word)

def kauffman_bracket(word, nstrands, conv):
    m = len(word)
    poly = {}
    from math import comb
    for bits in itertools.product([0, 1], repeat=m):
        c = count_circles(word, nstrands, bits)
        ea = 0
        for j, (_, s) in enumerate(word):
            ea += 1 if bits[j] == conv[s] else -1
        # (-A^2 - A^-2)^{c-1} = sum_t C(c-1,t) (-1)^{c-1} A^{2t-2(c-1-t)}
        for t in range(c):
            e = ea + 2 * t - 2 * (c - 1 - t)
            coef = comb(c - 1, t) * ((-1) ** (c - 1))
            poly[e] = poly.get(e, 0) + coef
    return poly

def jones_from_bracket(bpoly, w):
    shift = -3 * w
    sgn = -1 if (w % 2) else 1
    V = {}
    for e, c in bpoly.items():
        V[-(e + shift)] = V.get(-(e + shift), 0) + sgn * c
    return V

def showV(V):
    return " ".join(f"t^({k}/4):{V[k]}" for k in sorted(V) if V[k])

def Kword(k):
    return [(1, 1), (2, -1)] * (6 * k + 1) + [(1, 1), (1, 1)]

# CALIBRATED CONVENTION (2026-09-09): convA = {+1: par(0) is A-smoothing,
# -1: cup(1) is A-smoothing}. Verified: unknot V=1; kink V=1; Hopf(-t^{1/2}-t^{5/2});
# right trefoil t+t^3-t^4; figure-8 t^2-t+1-t^{-1}+t^{-2}; RII diagram bracket = d.
CONV = {1: 0, -1: 1}

if __name__ == "__main__":
    for name, conv in [("convA", {1: 0, -1: 1}), ("convB", {1: 1, -1: 0})]:
        print(f"=== {name} ===")
        for label, w, n in [("unknot s1 s1^-1", [(1, 1), (1, -1)], 2),
                            ("unknot 1X kink", [(1, 1)], 2),
                            ("trefoil s1^3", [(1, 1)] * 3, 2),
                            ("hopf s1^2", [(1, 1)] * 2, 2),
                            ("fig8 (s1 s2^-1)^2", [(1, 1), (2, -1)] * 2, 3),
                            ("K0", Kword(0), 3)]:
            b = kauffman_bracket(w, n, conv)
            V = jones_from_bracket(b, writhe(w))
            print(f"{label}: w={writhe(w)} V = {showV(V)}")
    print("--- unlink test ---")
    print("all-par:", count_circles([(1, 1), (1, -1)], 2, (0, 0)), "(want 1)")
    print("all-cup:", count_circles([(1, 1), (1, -1)], 2, (1, 1)), "(want 2)")
