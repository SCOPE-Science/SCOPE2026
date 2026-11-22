# Scientific review

## Correctness

PASS. The exact supporting-plane minimizer lies within distance \(s\) of the exit point, rather than the previous proof's \(2s\). Projection onto the certified tangent ball stays in the original local ball, and its distance from the relaxed minimizer is exactly \(\sqrt{\rho^2+\|p-q\|^2}-\rho\). The explicit two-dimensional disk family gives limiting ratio one against the proposed coefficient. Degenerate normal-only directions and already-feasible trial points are handled separately. The standalone verifier passed after extraction from the package.

## Originality

PASS, best knowledge with residual historical risk. Hazan, arXiv:2608.04321v2, §2.2, Lemma 2.3, proves the larger constant \(2/\rho\), not the structural strengthening or sharp lower witness. Levy--Krause's 2019 tangent construction concerns approximate projection, while Kolzenburg--Richtárik's 2026 short-step analysis assumes an exact local oracle. Searches covering synonyms for supporting-tangent repair, rolling-ball geometry, geometric oracle bounds, and sharp constants found no equivalent result. The accessible material for Richtárik--Mahran's 2026 exact local-LMO paper did not establish this approximate-oracle statement; its complete text was not accessible through the checked open routes.

## Value

PASS. The result determines an optimal universal constant for an explicitly used local oracle, sharpens the geometric term in the standard additive-oracle transfer bound by a factor of four, and proves the quadratic error order cannot be improved for this algorithm even on a disk. It does not claim a fourfold wall-time improvement or any improvement for alternative algorithms. The numerical and scientific scope is exact tangent access.

## Closest coverage and risks

The source paper's stated coefficient is known and is not itself novel. The new part is the stronger \(\|p-q\|\le s\) geometry together with a sharp lower family. Classical tangent-plane repair may have equivalent optimal-constant statements not surfaced by searches; historical priority requires external checking. The complete text of a later projection-equivalence article was not obtained, though its abstract concerns the exact oracle rather than a tangent-ball approximate one.

Self-review: passed. Independent audit: not yet performed.
