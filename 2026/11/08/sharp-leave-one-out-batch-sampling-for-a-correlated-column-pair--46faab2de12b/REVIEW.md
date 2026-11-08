# Scientific review

## Correctness (C): PASS

The domain is exact-arithmetic full-rank least squares with \(n\ge3\), \(0<\rho<1\), one correlated column pair and iid size-\(n-1\) blocks. The proof independently derives all residual projectors, their expected operator and spectral radius, the unique minimizer (including boundary distributions), determinant-volume comparison and the all-iteration fixed-residual induction. The finite SymPy verifier passes 646 exact checks but does not substitute for the proof. No convergence claim is made at the singular endpoint or in floating point.

## Originality (O): PASS, with substantive access risk

The known general volume-sampling projection identity [2,3] is expressly not new. The candidate claim is the explicit unique minimax law for this leave-one-out correlated-pair benchmark, the strictly suboptimal determinant-volume law, and a fixed initial residual with an exact all-iteration gap. Searched semantic published-finding corpus records and accessible own historical claims; closest include an inverse-positive quadratic singleton-sampling result, randomized-pivoting examples, and two-row Kaczmarz results, none implying this optimized block distribution. The full text of the directly related 2026 batch-sampling paper [1] and of the 2019 volume-sampling original [2] were inaccessible; their uninspected portions may cover a special case and independent priority checking is advisable. The 2026 spectral-equalization paper [3] was inspected substantially via lawful public HTML; its general volume-expectation formulas are acknowledged as prior knowledge.

## Value (V): PASS

The benchmark is the first genuinely distinct dimension with an omitted coordinate and a correlated pair. Determinant sampling strongly favors ill-conditioned near-complete spans, while the unique one-step minimax design allocates mass to the orthogonal directions; the exact witness gives an unbounded iteration-count separation at fixed target reduction as \(\rho\uparrow1\). This concrete failure mode motivates optimizing sampling distributions independently of determinant or volume criteria.

## Scope and residual limitations

The result applies only to a correlated-pair square geometry, exact block solves, one-step worst-case expected squared residual and one fixed-data multi-step comparison. No all-matrix or finite-precision superiority is claimed. Main publication risk is an undiscovered earlier algebraically equivalent special case in inaccessible originals.

Self-review: passed. Independent audit: not yet performed.
