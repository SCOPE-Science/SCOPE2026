# Review status

Independent audit date: 2026-10-01 UTC

Disposition: **failed**.

- Correctness: **PASS** — The geometric construction checks out. The short-root zonotope is full dimensional, F has dimension two, and M,N,F lie in the same two-dimensional subspace so the mixed-volume vanishings required for a degenerate pair follow. The reflection diag(1,-1,1,...) preserves the reference tuple and swaps M,N, giving the normalization. At u*=(e1+e2)/sqrt(2) and w*=(e1-e2)/sqrt(2), the zonotope face spans have dimensions n-1, the F-face has dimension 1, and the combined face span has dimension n-1 for n=4,5,6. These directions lie in the mixed-area-measure support, while the support-function values force incompatible dilations 1+sqrt(2) and sqrt(2)-1. Thus the claimed AF equality and failure of translation/support-only explanation are correct.
- Originality: **FAIL** — The final mathematical mechanism is directly covered by Shenfeld-van Handel's general degenerate-pair lemma and, more pointedly, by their published Example 2.12: a two-dimensional reference body with two segment directions, symmetry swapping the segments, and a mixed-area-support check yields an AF equality that cannot be reduced to translation/support. The root-system choice changes the ambient full-dimensional polytope and requires elementary face-span verification, but the claimed 'dimensional mechanism is active' is a finite specialization of that already-published construction pattern.
- Scientific value: **FAIL** — The C_n choice is natural, but after the published general mechanism and Example 2.12 are in hand, the n=4,5,6 result is a short finite specialization with the same two-segment geometry. It does not establish a new boundary, classification, or invariant and is mechanically checkable from standard root-face spans. Under the common C/O/V bar this is not enough scientific value for a validated finding.

The detailed source comparisons and residual risks are recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
