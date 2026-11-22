# Scientific review: spectral-norm-ball maximum-entry stability

## Correctness — PASS
The proof derives the singular-value-clipped Euclidean projector, differentiates at smooth exterior points \((1+s)uv^{\mathsf T}\), and takes the justified limit to a rank-one tangent hyperplane projection. Exact absolute-row calculations and Cauchy equal-tail saturation prove the tangent maximum formula. The positive-contraction Jacobian bound for a Hilbert nearest-point projector yields a global maximum-entry upper bound; the two-sided inequality is exact at \(m=n=2\). Analytic estimates prove the tangential leading coefficient \(1/4\) as both dimensions grow. The NumPy checker passed 622 supplementary assertions; these are not infinite-dimensional certification or a substitute for the proof.

## Originality — PASS, qualified
The 2012 Lefkimmiatis--Ward--Unser Schatten projection theorem and the 2018 Sedghi--Gupta--Long use of operator-norm-ball projection supply the base SVD clipping operation, but the inspected primary sections do not give the entrywise Lipschitz bounds or rank-one tangent optimization. Semantic comparison to records on positive-semidefinite repair, Birkhoff projection and sign-constrained SVD does not imply the spectral-ball theorem; their feasible sets and stated conclusions differ. Search terms, comparisons, inspection materials and remaining risks are recorded in AUDIT.json. A historically earlier equivalent formulation under another alias remains possible.

## Mathematical value — PASS
The gap is an exact coordinatewise robustness analysis of a commonly used nonpolyhedral matrix projector. The proven lower and upper bounds show linear growth for square matrices despite Frobenius nonexpansivity; the tangent-family formula and exact \(2\times2\) coefficient provide structural, directly checkable benchmarks. This is not a claim of the globally sharp constant for higher dimensions.

## Boundaries and limitations
No exact unrestricted \(L_{m,n}\) for general matrices or unrestricted limiting leading constant is claimed. The \(1/4\) limit applies to the rank-one tangent family only, and numerical checks do not prove continuum bounds. The strongest priority risk is an earlier unlocated endpoint Lipschitz result. Independent mathematical validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
