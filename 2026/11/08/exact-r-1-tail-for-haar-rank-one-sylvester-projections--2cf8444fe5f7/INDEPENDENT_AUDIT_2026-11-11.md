# Independent mathematical audit

## correctness

PASS

The displayed coupled Sylvester system has exact X=e₁e₁ᵀ and operator gaps −1,−3,1,−1, so its minimum singular value is one. Independent Haar u,v yield s=u₂²,t=v₂² independent arcsine. Reduced x=−u₁v₁/[2(s−t)−1] and Z=√((1−s)(1−t))/|2(s−t)−1|. Conditional on t<1/2, the r=√(1−s) tail interval has exact width √(1−t)/(2R), yielding RPr(Z>R)→(1/π²)∫₀^{1/2}dt/√(t(t+1/2))=2asinh(1)/π². The t>1/2 part is O(R⁻³); dominated convergence and layer cake prove p-moment finiteness iff p<1 for Z and error. Fresh symbolic/minimal-gap/integral checks support analysis, not simulation of infinite moments.

## originality

PASS

The original generalized Sylvester Petrov–Galerkin work requires disjoint numerical ranges to guarantee projected solvability; its [1,3] and [2,4] ranges overlap here. Positive-definite Kronecker-operator Galerkin bounds concern another hypothesis and structured Krylov spaces; other published sketching inverse tails reflect a related denominator mechanism but do not give the same independently Haar-projected coupled Sylvester matrix or explicit arcsinh constant. Best-of-knowledge originality, not independence/proven priority; abstracts of relevant secondary papers only.

## value

PASS

Even in a uniformly separated exact rank-one system, arbitrary independent Haar rank-one trial spaces have almost-sure solvability but infinite expected projected norm and error. The exact tail coefficient and sharp p=1 cutoff are a meaningful probabilistic robustness benchmark, explicitly not an assertion about structured Krylov algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
