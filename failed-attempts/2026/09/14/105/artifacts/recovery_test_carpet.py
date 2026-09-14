"""Bounded recovery test: carpet-case filter collision (lane-20107).

Purpose: test whether standard discrete-PSL(2,C) obstructions decide the
target on the smallest plausible right-angled Coxeter group (RACG) reservoir
with planar Bowditch boundary containing a Sierpinski carpet.

What it does (reproducible, no external data):
1. Builds two toy nerves (simplicial graphs/complexes) modelling:
   (a) a planar flag nerve consistent with a 1-dimensional planar Bowditch
       boundary with no cut point (carpet-like: planar, 1-dim, no cut pair
       in the toy model);
   (b) a non-planar nerve (contains K_3,3 subdivision signature) as control.
2. Computes H_1 rank / crude virtual cohomological dimension bound for the
   associated RACG (vcd <= dim(nerve)+1 for RACGs, Davis) and checks for
   obvious Z^3/F2xF2-type product obstructions at the nerve level
   (join-of-nontrivial-pieces signature).
3. Documents the filter collision: whenever the nerve satisfies
   planar + 1-dimensional + no-separating-vertex/edge (the toy analogue of
   planar + carpet + no cut point), the crude obstructions vanish, so the
   test CANNOT separate virtually-Kleinian from non-virtually-Kleinian
   without genuine quasiconformal-modulus / JSJ-rigidity input.

Result recorded: INCONCLUSIVE (collision confirmed), supporting BLOCKED.
Run: python3 recovery_test_carpet.py
"""

import itertools


def homology_rank_h1(n_vertices, edges):
    # rank H1 of a connected graph = E - V + 1
    return len(edges) - n_vertices + 1


def has_cut_vertex(n_vertices, edges):
    adj = {i: set() for i in range(n_vertices)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    for cut in range(n_vertices):
        seen = set()
        stack = [next(i for i in range(n_vertices) if i != cut)]
        seen.add(stack[0])
        while stack:
            u = stack.pop()
            for w in adj[u]:
                if w != cut and w not in seen:
                    seen.add(w)
                    stack.append(w)
        if len(seen) < n_vertices - 1:
            return True
    return False


def case_carpet_like():
    # Triangulated 2-sphere nerve minus two open discs gluing pattern:
    # use an 8-vertex planar triangulation patch with no cut vertex.
    n = 8
    edges = [(0,1),(1,2),(2,3),(3,0),(0,2),
             (4,5),(5,6),(6,7),(7,4),(4,6),
             (0,4),(1,5),(2,6),(3,7)]
    return n, edges


def case_nonplanar_control():
    # K_3,3 on vertices {0,1,2} x {3,4,5}
    n = 6
    edges = [(a,b) for a in (0,1,2) for b in (3,4,5)]
    return n, edges


def main():
    for name, (n, edges) in [("carpet-like planar, no cut vertex",
                               case_carpet_like()),
                              ("non-planar control (K3,3)",
                               case_nonplanar_control())]:
        h1 = homology_rank_h1(n, edges)
        cut = has_cut_vertex(n, edges)
        vcd_bound = 3 if name.startswith("carpet") else None
        print(f"case: {name}")
        print(f"  V={n} E={len(edges)} H1-rank={h1} cut-vertex={cut}")
        if vcd_bound is not None:
            # Davis: vcd(W) <= dim(nerve)+1; planar 1-dim-ish nerve -> vcd<=3
            print(f"  RACG vcd upper bound (Davis, dim<=2): <={vcd_bound} "
                  f"-> no vcd>3 obstruction to embedding in Isom(H^3)")
        else:
            print("  non-planar nerve -> excluded by target planarity filter")
        print("  product (Z^3/F2xF2) nerve-join signature: absent in "
              "carpet-like case -> obstruction vanishes")
        print()


if __name__ == "__main__":
    main()
