# Scientific review

## Correctness — PASS
The normalized Boolean-cube Laplacian diagonalizes in Walsh degree, with eigenvalues \(2|S|/d\). Restriction to a coordinate face identifies hidden-index Walsh modes having equal outside index; time variation separates their hidden Hamming weights by a distinct-node Vandermonde matrix and cannot separate modes of equal hidden weight. This directly establishes the exact rank for all \(d,c,K,m\). In codimension one, the Gram matrices are explicitly two by two and positive definite, and a one-variable derivative gives the unique determinant optimizer. Full unnormalized vertex counting norms and the factor \(1/\sqrt2\) in the block matrix were checked. The standalone finite checker separately corroborates 405 rank instances and six singular-spectrum instances; no finite enumeration is used as an unrestricted proof.

## Originality — PASS relative to checked literature
The 2014/2017 general orbit-frame criterion and the 2024 graph-space-time characterization give necessary/sufficient eigenspace conditions; they are credited as stronger abstract results. Their statements do not provide an exact all-cutoff rank formula on coordinate faces nor compute these blocks' determinant-optimal two-time heat parameter. The motivating 2026 graph Paley–Wiener study treats path graph numerics and general finite-frame formulas, not the Boolean-cube face family. A 2026 published arithmetic-spectrum D-optimality result uses amplitude/derivative observables, unlike the spatially restricted heat Walsh operator. The exact outcomes here follow after a new object-specific evaluation; priority over all older sources cannot be guaranteed.

## Value — PASS
The hardware-versus-time question is natural for diffusion on a product network: observing half its nodes twice is sufficient for any initial signal, while observing a quarter or fewer in a fixed coordinate face fails even after indefinitely many heat snapshots for a nonconstant band. The exact rank across all bands quantifies what fails, and the full singular spectrum and unique sharp optimal sampling time specify the best two-frame determinant design and its noise interpretation. This is a complete, motivated classification rather than an arbitrary small-number computation, despite the elementary Walsh/Vandermonde ingredients.

## Closest literature and limits
See arXiv:2609.25472, arXiv:2411.12670, arXiv:1409.8333, and the published arithmetic-spectrum optimal-horizon result linked in `RESULT.md`. The proof concerns coordinate faces and scalar heat dynamics only, with fixed-time D-optimality rather than minimum-singular-value optimality. An alternative prior statement of this concrete specialization in the control/observability literature remains a residual risk.

Self-review: passed. Independent audit: not yet performed.
