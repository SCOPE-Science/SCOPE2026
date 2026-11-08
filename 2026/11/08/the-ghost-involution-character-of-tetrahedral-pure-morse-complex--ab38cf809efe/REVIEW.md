# Self-review: tetrahedral pure Morse-complex character

## Correctness — PASS

The claim applies only to the rational reduced degree-three homology of the two tetrahedral pure Morse complexes and to the inherited \(S_4\times C_2\) action on the boundary version. Scoville [1, Theorem 22] proves that both pure spaces have the homotopy type of wedges of 81 three-spheres; Lin--Scoville [2, Definition 26, Theorem 32] establish the complement/ghost symmetry. The exact signed Lefschetz proof then requires a finite complete computation, not an asymptotic assumption. The included standalone Python program generates every possible incidence matching, checks disjointness and directed acyclicity, takes the pure downward closures, computes action orientation signs, and independently repeats all nonidentity signed traces by orbit enumeration. It checks every group element and irreducible multiplicity. Four face vectors reproduce the source's published tables. The ghost's signed contribution \(12-36+16=-8\) yields trace \(9\) on \(H_3\), with the full character calculated analogously. No higher-dimensional extrapolation is used.

## Originality — PASS, with stated residual uncertainty

The 2000 Chari--Joswig work [3] defines the complexes and the 2019 Lin--Scoville work [2] gives the automorphism group and reflection formula. Scoville's 2026 paper [1] gives the homotopy and ordinary Betti numbers (and a verification supplement computing those inputs), but does not state a ghost action, its top-homology trace, any \(S_4\times C_2\) character, or a rational-isomorphism comparison of the two pure top-homology modules. The nearest accessible mathematical-result records concern Morse complexes on other graphs, or strong rather than ordinary Morse matchings on simplex boundaries. Those do not imply the present full boundary ghost-character decomposition. The inference from rank \(81\) and group existence to eigenspace dimensions \(45\) and \(36\) is invalid without the new signed trace computation. Equivalence in unindexed literature remains possible; the literature search is not proof of uniqueness.

## Mathematical value — PASS

The tetrahedron and its boundary are the first well-documented nontrivial high-dimensional pure Morse-matching pair with a shared 81-sphere homotopy type and differing face vectors [1]. The boundary has a natural extra ghost involution that is absent from the ordinary four-vertex symmetry of the underlying tetrahedron [2]. Determining its complete rational character is an intrinsic equivariant invariant, separating the \(45\)- and \(36\)-dimensional eigenspaces and computing all five Specht multiplicities in each; neither the sphere count nor the abstract automorphism group determines this. The surprising equality of the two natural \(S_4\)-representations provides a sharp representation-level refinement of the known nonequivariant coincidence. The example is finite but mathematically motivated, with no artificial parameter restriction.

## Boundaries and evidence

The calculation does not prove an equivariant homotopy equivalence, an integral representation isomorphism, or character values for the two nonzero degrees of the full boundary Morse complex. Complete invariant matching enumeration and the published homology theorem are both needed; a computation log without its executable proof is not used as a substitute. Closest literature is [1] Scoville, arXiv:2604.18172; [2] Lin--Scoville, arXiv:1904.10907; and [3] Chari--Joswig, arXiv:math/0011234. The primary additional risk is unindexed equivalent work.

Self-review: passed. Independent audit: not yet performed.
