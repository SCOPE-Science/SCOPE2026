# Review: A shared insphere and a sharp incenter-dimension jump for partial alternating-sign-matrix polytopes

## Correctness — PASS

The proof explicitly states the full \(mn\)-dimensional Frobenius metric, the Heuer–Striker prefix-inequality premise, and all positive integer parameter ranges. The ball containment conditions include the correct \(\sqrt k\) normal factors for every prefix length. The two sharp first-row/first-column bounds and uniform attaining center prove the radius. The forced equality analysis and small-perturbation witnesses prove the affine dimension and generic facet contacts; comparison with the standard matching-polytope H-description proves uniqueness there. The one-by-one and one-row cases are handled. The finite LP program was run from the included source for 128 programs; its success is a check, not the infinite proof.

## Originality — PASS, provisional priority

The closest source is Heuer–Striker, arXiv:2012.09901, whose complete HTML text was examined for the defining inequalities, minimal facets, face-lattice description, and volume results. It supplies the **premise**, not an insphere/center-locus theorem. Heuer–Solhjem–Striker, arXiv:2403.02204, studies special faces and order/flow equivalences, with different conclusions. Relevant research-record searches used the exact matrix-polytope name, Chebyshev radius, the common matching insphere, and center dimensions. Nearby records on partial permutohedra, fixed-cardinality assignment polytopes, and the Frobenius *diameter* of the same matrix family do not imply the present inradius or center classification: these are different sets or different invariants. This is best-knowledge originality, not a claim that every historical source was available. Residual risk: an earlier equivalent insphere computation might exist under the vocabulary of sign-matrix/flow polytopes.

## Mathematical value — PASS

The theorem is a complete two-parameter metric classification for a natural, previously studied but generally difficult matrix-polytope family. In particular, it distinguishes the rigid matching polytope from its much larger partial-ASM extension: the optimal radius stays *exactly* fixed, while the incenter locus acquires up to quadratic affine dimension, and the square aspect ratio changes the dimension and contact pattern. This is an intrinsic shape comparison and exact, all-parameter classification, not a recomputation of the defining inequalities, an arbitrary numerical slice, or a trivial diameter bound.

## Limitations and closer literature

The geometry depends on the standard unweighted Frobenius embedding. The published facet description is assumed, not reproved. Generic facet contacts differ from additional contacts at special boundary incenters; the statement carefully restricts the count to relative-interior incenters. Historical priority is provisional pending outside review. The SciPy checker tests only finite sizes.

Self-review: passed. Independent audit: not yet performed.
