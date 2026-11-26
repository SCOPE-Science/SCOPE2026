# Independent mathematical audit

## correctness

PASS

The corrected claim is an explicit collapse in the once-bisected unordered discrete model, composed with a deformation retraction from the continuous space. Prue–Scrimshaw Theorem 3.2 applies at three particles: there are at least three graph vertices, the essential-to-essential path bound is two, and every essential loop has length at least ten, above the required four. Closed cubes embed because the three factors have disjoint closures, so each surviving square in exactly one cube is a genuine free face. Independent construction in KG(5,2) labels verifies cell counts (2300,7590,8190,2880); deleting only the 2880 free square–cube pairs leaves (2300,7590,5310,0). Replay `python3 /workspace/repairs/4/verify.py`; stdout matches the corrected package. Its connected 1-skeleton and Euler characteristic 20, together with Ko–Park for a triconnected nonplanar Petersen graph, give H2 free of rank 25 and minimal dimension two. Independently the integral cubical calculation in /tmp/opencode/graph_triples_audit.py verifies both signed boundary compositions and gives 5284 unit pivots and a rank-one residual of entry gcd 2 after the alternate top-only collapse and removal of a 2299-edge tree. Thus H1=Z^6 plus Z/2, H2=Z^25, and higher groups vanish. The frozen collapse and Smith reasoning were mathematically sound as inspected: its distinct choice of also collapsing lower-dimensional pairs changes the cell counts and pivot counts, not the invariant. No assertion of an elementary collapse directly on an unspecified CW structure of the continuous space is made in the repair.

## originality

PASS

For the frozen version, the novelty claim for the numerical degree-two rank is defeated by the October 18 and November 1 Petersen symmetry records. The corrected version explicitly credits their rational Betti number and Ko–Park's integral H1, and claims the concrete two-dimensional cubical spine. The inspected antecedents compute homology or representations, not that spine or this collapse. Best-of-knowledge assessment of the corrected claim only; no absolute priority claim.

## value

PASS

The existence of a specific minimal-dimensional deformation retract is more informative than rank or torsion data alone and is not implied by the prior rank calculations. Here it removes all top cells of a natural 3-dimensional model without changing the 1-skeleton, yielding a reusable concrete 2-complex for the graph braid group on a canonical nonplanar graph. H2 nonzero proves sharpness; the repaired claim is not a reassertion of a known numerical Betti invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
