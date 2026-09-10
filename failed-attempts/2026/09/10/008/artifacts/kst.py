# kst.py — target-directed: rigorous KST upper bound for linear Berge-K_{s,t} (lane-507)
# Theorem route (TARGET upper-bound leg):
# Let H be 3-uniform linear on n vertices, G = shadow graph (pairs covered).
# |E(G)| = 3|E(H)| (linearity => pairs disjoint).
# If H contains Berge-K_{3,3} on core (A,B), then all 9 cross pairs are covered
# in DISTINCT hyperedges (9 distinct edges each containing one cross pair; linearity
# gives distinctness: a hyperedge containing 2 cross pairs from a 3+3 bipartition
# would contain 2 vertices from A side... check: e={ai,aj,bk} contains cross pairs
# (ai,bk),(aj,bk) sharing bk => two pairs in one edge. So distinctness of the 9 edges
# is NOT automatic from linearity! Must prove via witness structure.)
# KEY LEMMA (proved here computationally for the record): linearity does NOT force
# distinctness. Verify with explicit small certificate below.
# Instead the usable rigorous reduction: fix a transversal choice.
from fractions import Fraction

def kst_exponent_bound(s, t):
    # ex(n,K_{s,t}) <= (1/2)(t-1)^{1/s} n^{2-1/s} + O(n). Standard KST.
    import math
    c = 0.5 * (t - 1) ** (1.0 / s)
    return c, 2 - 1.0 / s

if __name__ == "__main__":
    import sys
    sys.path.insert(0, "/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-507/output/artifacts")
    from berge import pair_map, is_linear
    # Counterexample to naive "linearity => 9 distinct edges" claim:
    # A={0,1,2}, B={3,4,5}; hyperedges {0,1,3},{2,4,6},{2,5,7},{0,4,8},{1,5,9},{0,5,10},{1,4,11},{2,3,12},{...}
    # Simply: edges {0,1,3} covers pairs (0,3),(1,3) — two cross pairs in ONE edge, linear still possible.
    E = [(0,1,3),(2,4,9),(2,5,10),(0,4,11),(1,5,12),(0,5,13),(1,4,14),(2,3,15),(0,2,16)]
    print("linear:", is_linear([tuple(sorted(e)) for e in E]))
    print("edge (0,1,3) covers TWO cross pairs (0,3),(1,3) of core A={0,1,2},B={3,4,5}")
    print("=> naive shadow-distinctness reduction INVALID; recorded as target-directed finding.")
    c, e = kst_exponent_bound(3, 3)
    print(f"KST(3,3): c={c:.6f}, exponent={e:.6f}")
    print("Consequence: IF distinctness held, linear rate m/n^2 <= sqrt(2)/6 n^{-1/3} -> 0.")
    print("Since distinctness FAILS in general, upper bound needs flag-SDP leg, not bare KST.")
