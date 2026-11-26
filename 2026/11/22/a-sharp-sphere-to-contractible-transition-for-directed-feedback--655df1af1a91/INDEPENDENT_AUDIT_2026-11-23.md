# Independent mathematical audit

## correctness

PASS

The frozen one-long-arm proof has a false simplicial equality at RESULT.md lines 36–40: removing only the long diagonal from H leaves each short diagonal in H₀, but that diagonal is an entire short arm and is forbidden in K′. For m=2 and lengths (3,2), the incorrect model counts 17 forward faces in K′ instead of 15; the short diagonal alone is a counterexample. The original proof thus fails as written, not the homotopy claim. Complete corrected affected files are in /workspace/repairs/5/. Re-audit: the only local restrictions are the first/last arc quotas, and every directed cycle is one full forward arm plus the full return. Partitioning on whether the return is full gives the stated gluing. For h≥1, both pieces are cones and their common subcomplex is nonempty; the homotopy pushout gives an unreduced suspension of the intersection. The r=1 join with the empty-face complex leaves K′; for r≥2 the intersection is K′ joined with S^(r−2), so X≃Σ^r K′. For h=1 use the bipartite endpoint complex containing all vertices but only off-diagonal edges. With the private simplex this is one cone; the other is the long diagonal joined to the private simplex boundary. Exactly their common boundary is S^(L−3), including S⁰ for L=3. Thus K′≃S^(L−2). For h≥2, the two private-arc closed stars cover: adding a private arc can only complete its own branch, and faces cannot hold both endpoint pairs. Adding both arcs introduces no joint obstruction, so the intersection is the nonempty edge star. The two stars and their intersection are cones. This proves the unchanged assertion for every allowed parameter, as ordinary homotopy. The frozen finite checker was inspected only; its 33-face minimal example is independently recovered as 18+15, and neither it nor its mod-two homology proves homotopy equivalence.

## originality

PASS

The corrected proof establishes the same distinct h≥1 claim. Examined same-family multipath results treat h=0. The broader polygon, module and one-feedback-edge results and the same-family calculations for other invariants do not give the mixed-length classification. The repair changes the proof, not the scope or overlap.

## value

PASS

This is an ordinary homotopy classification for a natural infinite graph family. A single long forward arm yields a sphere of a precise dimension, but a second removes even that homotopy type independently of lengths and other arms. It is stronger than sampled homology and adds a structural transition to the known all-short baseline. The repaired forward-face model establishes exactly this distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
