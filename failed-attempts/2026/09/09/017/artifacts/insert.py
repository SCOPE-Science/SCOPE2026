"""Local twist insertion into a 2-braid region at X-notation PD level.

Region model: two parallel directed strands through crossings X_1..X_k in order.
Between consecutive crossings, two parallel edges (eL, eR). To add one half-twist:
pick parallel pair (eA, eB) between X_j and X_{j+1}; subdivide: new crossing Y with
ports: A-in -> Y -> A-out (over), B-in -> Y -> B-out (under) [or swapped for handedness].
Implementation: fresh edge ids for the 4 new half-edges + new crossing id.
"""
import sys
sys.path.insert(0, '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-314/output/artifacts')
from pdcal import build_from_X, bracket_X
from math import comb
import cmath

P0 = lambda a, b, c, d: [(a, c), (b, d)]
P1 = lambda a, b, c, d: [(a, d), (b, c)]


def occ_map(chords):
    occ = {}
    for ci, (a, b, c, d) in enumerate(chords):
        for x in (a, b, c, d):
            occ.setdefault(x, []).append(ci + 1)
    return occ


def insert_twist(chords, eA, eB, overA=True):
    """Insert one crossing between parallel edges eA, eB. Returns new chords list.
    New crossing Y=(nA_in..., ): wire: eA splits into eA1 (into Y) and eA2 (out of Y);
    eB splits into eB1, eB2. Y = X[eA1, eB1, eA2, eB2] if A over, else X[eB1, eA1, eB2, eA2]
    (using working convention over=(positions 0,2)? We use build_from_X over_choice
    consistently; here define Y so that strand A is the (a,c) strand and B is (b,d).)
    """
    mx = max(max(t) for t in chords)
    n = len(chords)
    eA1, eA2, eB1, eB2 = mx + 1, mx + 2, mx + 3, mx + 4
    out = []
    for (a, b, c, d) in chords:
        na = eA1 if a == eA else (eB1 if a == eB else a)
        nb = eA1 if b == eA else (eB1 if b == eB else b)
        nc = eA2 if c == eA else (eB2 if c == eB else c)
        nd = eA2 if d == eA else (eB2 if d == eB else d)
        # careful: an edge could appear twice in one crossing? (loop) — handle: if both
        # eA and eB in same tuple positions... our parallel edges are distinct and each
        # appears in exactly 2 crossings; substitution per-endpoint is what we want, but
        # X-tuples list edges not endpoints. Since eA connects X_j and X_{j+1}, it appears
        # once in each tuple. Replace occurrence in X_j-side with eA1/eB1 and X_{j+1} with eA2/eB2?
        # We don't track sides here; instead caller passes oriented info. SIMPLIFY: replace
        # ALL occurrences of eA with eA1 on the 'low' crossing and eA2 on the 'high' one.
        out.append((na, nb, nc, nd))
    # Fix orientation below in caller; here just append Y with A=(a,c), B=(b,d):
    if overA:
        out.append((eA1, eB1, eA2, eB2))
    else:
        out.append((eB1, eA1, eB2, eA2))
    return out
