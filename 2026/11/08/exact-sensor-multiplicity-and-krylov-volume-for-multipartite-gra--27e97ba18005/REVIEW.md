# Scientific assessment

## Correctness — PASS
On the invariant part-constant subspace, the random-walk evolution is exactly the diagonal-plus-rank-one quotient matrix stated in RESULT.md. Its equal-size eigenspaces are zero-sum coordinates within repeated groups; all remaining eigenvalues are simple with nowhere-zero eigenvectors. The distinct-eigenvalue Vandermonde decomposition proves the complete sensor condition, and the Krylov monic-polynomial recurrence proves the single-sensor determinant. Exact rational checks of 15,308 assertions independently exercise rank, determinant and enumeration identities on bounded cases. Finite checks are not used as infinite proofs.

## Originality — PASS relative to checked evidence
The closest general precursor is Cabrelli et al. (2017), Theorem 4.1, which gives the finite-dimensional spectral criterion but does not evaluate the complete multipartite quotient, count minimum sensor sets, or produce the exact determinant. Mousavi et al. (2018/2020) treat cograph controllability for full combinatorial-Laplacian dynamics, not this invariant random-walk Fourier band or its measurement-volume invariant. The 2026 graph Paley--Wiener paper motivates the finite graph-sampling question; only its abstract was accessible, so full-text overlap remains an explicit risk. Searches for repeated-part-size sensor criteria and one-sensor Krylov-volume formulas did not identify exact coverage. This is a graph-specific exact classification with quantitative volume, not an assertion that general spectral observability is new.

## Value — PASS
Equal-size graph communities create genuine eigenvalue multiplicities, and sensor placement must defeat those symmetries. The theorem translates that phenomenon into a closed all-parameter minimum-budget rule, counts every optimal physical placement, and gives an exact stability-volume product that detects failures when community sizes collide. The one-sensor versus many-sensor transition is meaningful for planning repeated-time graph measurements, including when nearly equal community sizes cause small determinants. These are natural complete classifications, not an arbitrary finite census.

## Limitations and scientific risks
The graph subspace excludes within-part signals, and one cannot deduce full-vertex recovery. The determinant is not an exact minimum-singular-value bound. Novelty relative to inaccessible full text or alternate observability terminology is not independently certified. Comparisons to a general theorem do not confer novelty by absence of matching wording alone; the distinctive result is the explicit multipartite placement law together with the product determinant.

Self-review: passed. Independent audit: not yet performed.
