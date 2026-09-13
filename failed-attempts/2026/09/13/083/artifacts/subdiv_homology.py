"""Subdivision-chain homology: exact integer H1 classes for train loops and m/l.

Complex: vertices = 12 original + 36 side-midpoints (one per branch). Edges:
- half-branches: 72 (vertex -> midpoint), oriented vertex->midpoint arbitrarily fixed;
- corner segments: in each triangle, 3 segments joining adjacent side midpoints
  (these cut off corners). Oriented CCW.
Chains: train loop = sequence of half-branch traversals (vertex->mid->vertex ...);
normal curve (m/l) = corner segments with multiplicities from corner data.
Boundary maps integer; quotient ker/im over Z via exact rational arithmetic +
rounding with verification. Intersection of train loop with m/l = signed crossings
in triangles (corner segment vs half-branch pairs share midpoint endpoints; perturb:
train loop pushed slightly toward large side... instead count crossings of SEGMENTS:
corner segments and half-branch segments meet only at midpoints (shared endpoints) --
not transverse. Perturb normal curve off midpoints: shift corner-segment endpoints by
eps along sides; then crossings with half-branches occur near midpoints, counted
combinatorially. Equivalent: use triangle chord model (already have) but VERIFY signs
by checking i(m,l) = -1 in the chord model!
"""
import pickle, math
from collections import defaultdict
import snappy, flipper
from flipper.kernel.triangulation3 import MERIDIANS, LONGITUDES

WDIR = "output/artifacts"
D = pickle.load(open(f"{WDIR}/track_data.pkl", "rb"))
branches, switches, NV = D["branches"], D["switches"], D["NV"]
NB = len(branches)
M = snappy.Manifold('10_145')
mono = flipper.monodromy_from_bundle(M)
B = mono.bundle(veering=True)
V = snappy.Manifold(B.snappy_string())
data = V._get_tetrahedra_gluing_data()
NT = len(data)
T3 = B.triangulation3
WSTAR = {0: 2, 1: 3, 2: 0, 3: 1}
bkey = {}
for b, members in enumerate(branches):
    for s in members:
        bkey[s] = b

TAU = 2 * math.pi
def side_angle(W, j, off):
    return TAU * (W.index(j) + 1.5) / 3 + off

def chord_cross_oriented(p1, p2, q1, q2):
    """Crossing sign of oriented chords; endpoints assumed distinct."""
    def rel(x):
        return (x - p1) % TAU
    r2, r3, r4 = rel(p2), rel(q1), rel(q2)
    if (r3 < r2) != (r4 < r2):
        return 1 if r3 < r2 else -1
    return 0

def inter_chord_model(walk_tris, P, woff=0.03, goff=-0.03):
    """walk_tris: list of (tri, entry_side, exit_side). P: peripheral type.
    Normal-curve corner chords oriented from outflow corner to inflow corner."""
    by_tri = defaultdict(list)
    for (tri, se_in, se_out) in walk_tris:
        by_tri[tri].append((se_in, se_out))
    tot = 0
    for tri, warcs in by_tri.items():
        i, v = tri
        W = sorted(w for w in range(4) if w != v)
        t = T3.tetrahedra[i]
        S = {w: t.peripheral_curves[P][v][w] for w in W}
        for (se_in, se_out) in warcs:
            p1 = side_angle(W, se_in, woff); p2 = side_angle(W, se_out, woff)
            for w in W:
                if S[w] == 0:
                    continue
                js = [j for j in W if j != w]
                q1 = side_angle(W, js[0], goff); q2 = side_angle(W, js[1], goff)
                # orient corner chord: outflow->inflow. Corner w with S[w]>0 = inflow (entering).
                # chord endpoints: midpoints of sides adjacent to w; direction should go from the
                # side where strand exits to side where it enters... For a corner-cutting strand at
                # inflow corner w: it connects the two adjacent sides; orient from js[1] to js[0] or
                # reverse depending on rotation direction of flow. Convention: strands circulate CCW
                # around inflow corners? Unknown; TRY both and calibrate with i(m,l)=-1.
                tot += chord_cross_oriented(p1, p2, q1, q2) * abs(S[w])
    return tot

# SELF-TEST: compute i(M, L) in chord model: represent M as walk-like arc collection?
# M is not a train route; but its arcs per triangle are corner chords. Compute i(M_arcs, L_arcs)
# with two different offsets and check equals flipper's -1 (up to conventions).
def inter_curve_curve(P, Q):
    tot = 0
    for i in range(NT):
        for v in range(4):
            W = sorted(w for w in range(4) if w != v)
            t = T3.tetrahedra[i]
            S = {w: t.peripheral_curves[P][v][w] for w in W}
            T_ = {w: t.peripheral_curves[Q][v][w] for w in W}
            for w in W:
                if S[w] == 0:
                    continue
                js = [j for j in W if j != w]
                p1 = side_angle(W, js[0], 0.03); p2 = side_angle(W, js[1], 0.03)
                for u in W:
                    if T_[u] == 0:
                        continue
                    ks = [j for j in W if j != u]
                    q1 = side_angle(W, ks[0], -0.03); q2 = side_angle(W, ks[1], -0.03)
                    tot += chord_cross_oriented(p1, p2, q1, q2) * abs(S[w]) * abs(T_[u])
    return tot

print("chord-model i(M,L) =", inter_curve_curve(MERIDIANS, LONGITUDES), "(flipper: -1)", flush=True)
print("chord-model i(L,M) =", inter_curve_curve(LONGITUDES, MERIDIANS), "(expect +1)", flush=True)
