# Self-review

## Correctness — PASS
The graph, ordinary three-cut convention and integral boundary orientations are explicit. Its Alexander dual has exactly 11 vertices, 55 edges, 42 path triangles and 9 square tetrahedra, and no higher faces. Complete unimodular unit-pivot reductions of all three signed boundary matrices give ranks 10, 32, 9 and all nonzero invariant factors equal to 1, proving both integral homology ranks and freedom from torsion. Equivariant Alexander duality supplies the ambient orientation sign. The explicit 18-triangle integral cycle is nonzero mod 3; testing its transforms recovers the rank-one dual character, while signed Lefschetz yields the rank-13 character. All twelve original-complex Lefschetz checks match the derived character differences. No homotopy equivalence is claimed.

## Originality — PASS with limitations
The original and sequel cut-complex papers do not contain this finite Herschel calculation. The closest published square-correction theorem requires **edge-disjoint** four-cycles, whereas all 18 Herschel edges belong to two of its nine four-cycles. The no-short-cycles representation formula likewise does not apply, while a published Herschel independence-complex classification concerns a different object. Primary full-text mathematical statements and the main published full papers were inspected. Unindexed or unpublished equivalent computations remain a residual risk, not a proof of uniqueness.

## Value — PASS
The Herschel graph is a canonical smallest non-Hamiltonian polyhedral graph. This calculates a natural full integral and equivariant invariant in the first geometric regime missed by the private-edge collapse hypothesis: interacting squares create persistent non-top-dimensional homology. The complete six-class rational character, with both invariant subspaces vanishing, is not implied by ranks and supplies meaningful symmetry information. The result does not assert a broader graph-family theorem or claim an unproved homotopy decomposition.

## Limits and references
References: Bayer et al., arXiv:2304.13675 and arXiv:2407.08158; published full mathematical statements on triangle-free edge-disjoint-square cut complexes, four-cycle-free cut complexes and Herschel independence complexes; the SageMath Herschel generator. Full source identifiers and direct proof comparisons are in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
