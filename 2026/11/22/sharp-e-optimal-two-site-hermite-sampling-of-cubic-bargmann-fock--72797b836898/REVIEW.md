# Scientific review

## Correctness: PASS
The displayed parity Gram matrices follow from direct evaluation of the standard orthonormal Gaussian monomials at opposite sites and covariant first derivatives. Each trace/determinant is explicit; the global optimization is bounded by the smaller odd-sector eigenvalue. The odd-sector stationary equation factors as the cubic times the explicit sextic. Exact rational Sturm root counting, rational isolation and branch-sign certificates from `CHECKER.py` establish a unique lower-branch stationary maximum. At its sextic root, both parity lower eigenvalues coincide, making the upper bound attained. The result is valid for every complex cubic, every nonzero site radius and arbitrary common rotation; it does not assert unconstrained two-site optimality.

## Originality: PASS, best-knowledge
The fully inspected 2020 Fock multiple-sampling density paper and 2024 polynomial-array paper establish existence/density and asymptotic array results, rather than this finite four-measurement E-optimal extremum. The 2019 shift-invariant derivative-sampling paper addresses a different model. Published finding searches for coherent first-jet cluster collision asymptotics, cubic tight point-only Fock sampling and paired point-only Gaussian sampling did not yield the finite cubic antipodal Hermite frame optimization or algebraic parity crossing. A classical finite Hermite design or exact conditioning result might nevertheless be indexed differently, so historical priority is provisional.

## Value: PASS
This is the minimal square Hermite sampling configuration for cubic polynomials, with two data types at two sites. The problem addresses worst-case stability, a different and more stringent criterion than invertibility or determinant maximization. The determinant for the same two-site data is maximized at squared radius \(1\), at which the lower squared frame bound is only \(e^{-1}\); the true E-optimum improves this bound by about 32%. The unique optimal node spacing is an algebraic, nonsymmetric spectrum-balance point where two parity error modes tie; the complete equality space and exact sharp bound make it a reusable finite benchmark for Fock sampling.

## Boundaries
The certified optimum is restricted to antipodal pairs with canonical Gaussian value/covariant-derivative normalization. There is no general assertion about arbitrary-site E-optimality, higher-degree polynomial spaces, weighted channel choices or uniqueness among other design families. Historical novelty is subject to independent priority review.

Self-review: passed. Independent audit: not yet performed.
