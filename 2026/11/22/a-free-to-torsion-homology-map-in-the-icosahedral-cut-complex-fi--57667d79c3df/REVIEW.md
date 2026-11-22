# Scientific review — icosahedral six-to-five cut transition

## Correctness: PASS
The vertex-labeled graph, all 4096 possible subsets, both ordinary cut complexes, signed boundaries and deterministic integer cancellation rule are provided in the executable verifier. All 638 cancellations for the six-cut complex are unimodular and leave six generators in degree three plus 26 in degree four with zero differential. The five-cut complex independently reduces through 1,293 unimodular cancellations to one boundary coefficient 2 and 30 free top generators. Exact mod-two chains supply a 44-simplex four-cycle in the six-cut complex whose image is not a boundary in the five-cut complex. Natural universal coefficients convert this nonzero mod-two map into an integral surjection onto the target \(\mathbb Z/2\). Full source code and recorded output were executed and inspected. These calculations certify integral homology, not geometric homotopy wedges.

## Originality: PASS against inspected evidence
The closest result, *Integral two-torsion in the five-cut complex of the icosahedral graph*, gives only the five-cut integral homology, with no six-cut group or connecting map. The 2023 foundational paper establishes the cut definition and nested stages; its graph-family results do not cover this special icosahedral adjacent-stage homomorphism. The 2024 sequel treats six-cut grid graphs, not the icosahedron. Exact-parameter, alias, equivalent-statement and broader-coverage searches in the indexed record and broader literature did not find a result that computes or implies the nontrivial map. An unindexed equivalent remains possible, and search absence alone is not a proof of novelty.

## Value: PASS
The known five-cut two-torsion motivates the natural next stage of the same decreasing graph-cut filtration. The exact calculation answers whether the preceding torsion class is detected by the earlier torsion-free integral homology: it is, through a surjection from \(\mathbb Z^{26}\), with index-two kernel. This is a genuine connecting-map invariant not derivable from either stage's separate Betti numbers; the finite computation has mathematical significance because the two adjacent natural stages are already singled out by a torsion event. It also determines the entire integral six-cut homology and gives nonshellability and non-Cohen–Macaulayness.

## Closest literature and limits
1. Bayer et al., *Topology of Cut Complexes of Graphs* (arXiv:2304.13675v1, 2023), Definitions 2.6–2.7 and the section-seven graph families.
2. Bayer et al., *Topology of Cut Complexes II* (arXiv:2407.08158v1, 2024), its grid section and conclusion.
3. *Integral two-torsion in the five-cut complex of the icosahedral graph* (public `RESULT.md`), determining the neighboring five-cut group but not its inclusion from stage six.

The computation is exact for this one finite labeled graph; it is not a general theorem on all polyhedral graphs, and it does not prove a wedge-of-spheres homotopy type. The searches cannot exclude unindexed equivalences. External independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
