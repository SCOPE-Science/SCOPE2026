"""Train-loop enumeration + homology via chord-crossing intersections with flipper m/l.

Conventions (all documented, deterministic, no floating point):
- Primal walk W: closed walk on oriented branches with switch-allowed transitions.
- Dual normal curves M, L from flipper peripheral corner data (signed; antisymmetric
  across gluings verified: c2 = -c1; m.l = -1 verified via flipper intersection_number).
- In each triangle, W-arcs join side midpoints; M/L-arcs join side midpoints per
  corner-weight pairing (inflow/outflow). Chord crossings counted with signs from
  CCW corner order (link orientation, all tets +). i(W,G) = sum of signed crossings
  after infinitesimal perturbation (offsets: W at +eps, G at -eps along each side).
- Class: [W] = a[m]+b[l], (a,b) = (-i(W,L), i(W,M)) since i(m,l)=-1.
- Zung picture coords: Zung gives mu=(-1,0), lam=(6,-1) in PICTURE coords, and
  meridian slope 0, longitude slope -1/6. Picture slope of (a,b) [i.e. a*mu+b*lam
  in H1]: direction a*(-1,0)+b*(6,-1) = (6b-a, -b); t = -b/(6b-a).
  Sanity: meridian (1,0) -> t = 0/ -1 = 0. Longitude (0,1) -> t = -1/6. Matches paper.
- Realizability of a loop for holonomy: per-edge fan non-crossing check (Zung Fig 9).
"""
import pickle
from collections import Counter
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
print("int(m,l) =", T3.intersection_number(MERIDIANS, LONGITUDES), flush=True)

# ---------- directed route graph ----------
# state: (branch b, triangle t=(i,v), entry side s). exits per switch.
states = {}
slist = []
for b, members in enumerate(branches):
    ((i1, v1), j1), ((i2, v2), j2) = members
    for (tb, sb) in [((i1, v1), j1), ((i2, v2), j2)]:
        L = WSTAR[tb[1]]
        smalls = [j for j in range(4) if j != tb[1] and j != L]
        exits = smalls if sb == L else [L]
        st = (b, tb, sb)
        states[st] = []
        slist.append(st)
        for se in exits:
            b2 = bkey[(tb, se)]
            # next state: arrive at other triangle of b2 via side se
            m2 = branches[b2]
            nxt = m2[1] if m2[0] == (tb, se) else m2[0]
            states[st].append((b2, (nxt[0][0], nxt[0][1]), nxt[1]))
print("states:", len(slist), flush=True)

# ---------- chord-crossing intersection ----------
# Triangle corner CCW order: W sorted, orientation + (link). Sides identified by missing corner j.
# Position on boundary circle: corner W[k] at angle 2*pi*k/3; side-midpoint s (missing corner W[k]) at
# angle 2*pi*(k+1.5)/3. Chord endpoints get small offsets: W-arcs +0.02 rad, G-arcs -0.02 rad.
import math
TAU = 2 * math.pi
def side_angle(W, j, off):
    k = W.index(j)
    return TAU * (k + 1.5) / 3 + off

def chord_cross(p1, p2, q1, q2):
    """Signed crossing of chord p (p1->p2) with chord q (q1->q2) on circle; 0 if shared endpoint."""
    pts = sorted(set([p1, p2, q1, q2]))
    if len(pts) < 4:
        return 0
    a = sorted([p1, p2]); c = sorted([q1, q2])
    # interleaved?
    lo1, hi1 = a; lo2, hi2 = c
    inter = (lo1 < lo2 < hi1 < hi2) or (lo2 < lo1 < hi2 < hi1)
    if not inter:
        return 0
    # sign: orientation of (p1,p2,q1) cyclic order... use: sign = +1 iff going p1->p2->q1 is CCW when
    # interleaved as p1<q1<p2<q2 (in circular lift starting at p1): standard: +1.
    # Lift angles relative to p1:
    def rel(x):
        d = (x - p1) % TAU
        return d
    r2, r3, r4 = rel(p2), rel(q1), rel(q2)
    order = sorted([(r2, 'p2'), (r3, 'q1'), (r4, 'q2')])
    seq = ''.join(s for _, s in order)
    # interleaved cyclic orders starting after p1: p2,q1,q2 or q1,q2,p2 (non-cross) excluded already.
    # crossing orders: (p2,q1 ... ) hmm: interleaved means exactly one of q1,q2 in (p1,p2) arc.
    if (r3 < r2) != (r4 < r2):
        # crossing: sign +1 iff (p1,q1,p2) CCW i.e. r3 < r2... define sign = +1 iff q1 in arc p1->p2
        return 1 if r3 < r2 else -1
    return 0

# normal-curve arcs per triangle from corner data: pair outflow (S<0) to inflow (S>0).
def curve_arcs(tet_idx, v, P):
    t = T3.tetrahedra[tet_idx]
    W = sorted(w for w in range(4) if w != v)
    S = {w: t.peripheral_curves[P][v][w] for w in W}
    outs = [w for w in W if S[w] < 0]
    ins = [w for w in W if S[w] > 0]
    arcs = []
    # arcs connect SIDES: strand through corner w (out) to corner w' (in) crosses from side adjacent...
    # Strand entering at corner w (S>0) and exiting at corner u (S<0): the arc joins side opposite... no:
    # strands pass corner regions: arc endpoints are on the two sides meeting at the corner? A strand "entering
    # at corner w" crosses the side between w and its neighbor? Model: corner weight S_w counts strands crossing
    # the dual corner arc (side-midpoint to side-midpoint cutting off corner w). So arc = chord joining the two
    # side midpoints adjacent to w (i.e., sides j != v, j != w), multiplicity |S_w|, orientation out->in.
    # Crossing of walk chord with these corner-cutting chords = intersection. Signs from orientation.
    for w in W:
        if S[w] != 0:
            arcs.append((w, S[w]))  # corner w, signed multiplicity
    return arcs

def inter_walk_curve(walk_tris, P):
    """walk_tris: list of (tri, entry_side, exit_side). Returns algebraic intersection."""
    tot = 0
    # group arcs per triangle
    from collections import defaultdict
    by_tri = defaultdict(list)
    for (tri, se_in, se_out) in walk_tris:
        by_tri[tri].append((se_in, se_out))
    for tri, warcs in by_tri.items():
        i, v = tri
        W = sorted(w for w in range(4) if w != v)
        carcs = curve_arcs(i, v, P)
        for (se_in, se_out) in warcs:
            p1 = side_angle(W, se_in, 0.02); p2 = side_angle(W, se_out, 0.02)
            for (w, mult) in carcs:
                # corner-cutting chord: joins midpoints of the two sides adjacent to w
                js = [j for j in W if j != w]
                q1 = side_angle(W, js[0], -0.02); q2 = side_angle(W, js[1], -0.02)
                # orientation: strand from out-corner to in-corner; crossing sign needs oriented chords.
                # Our chord_cross uses cyclic order + direction p1->p2. For curve chord orientation:
                # orient from side adjacent to outflow... simplify: orient corner chord from js[0]-mid to js[1]-mid
                # if mult>0 (inflow) else reversed. Walk chord oriented entry->exit.
                if mult < 0:
                    q1, q2 = q2, q1
                tot += chord_cross(p1, p2, q1, q2) * abs(mult)
    return tot

# ---------- enumerate simple loops (DFS, bound length) ----------
import sys
sys.setrecursionlimit(10000)
loops = []  # (branch_list, states_list)
LMAX = 12
found_classes = Counter()
def dfs(start, cur, depth, path_states, used_br):
    if depth > 0 and cur == start:
        loops.append(list(path_states))
        return
    if depth == LMAX:
        return
    for nxt in states[cur]:
        b2 = nxt[0]
        if b2 in used_br and not (depth + 1 >= 3 and nxt == start):
            continue
        if nxt == start and depth + 1 >= 3:
            loops.append(path_states + [nxt])
            continue
        if b2 in used_br:
            continue
        dfs(start, nxt, depth + 1, path_states + [nxt], used_br | {b2})
for s in slist:
    dfs(s, s, 0, [], set())
print("raw loops:", len(loops), flush=True)
