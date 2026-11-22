# Mathematical review

## Correctness — PASS
The half-integral vertex characterization follows from tight edge equations and the odd-cycle-support criterion of Hamano--Hibi--Ohsugi (2016). Explicit maximization of a linear objective over those vertices proves the Gaussian sign/half-normal formulas, and summing squared angles proves the collision identity. Gaussian exponential moments and the binomial theorem give the claimed uniform exponential error, and an explicit coupling proves total-variation equidistribution and the conditional support-size binomial approximation. An independent linear-programming verifier checks 1,500 objectives in dimensions three through eight and normal-cone class frequencies in several dimensions; these finite checks do not replace the proof.

## Originality — PASS (best-knowledge, priority provisional)
Liu (arXiv:2409.11970v1), Hamano--Hibi--Ohsugi (arXiv:1603.09613v1), and the published complete-clique sphere-transition result all concern the same graph polytope. Their checked results address Ehrhart theory, vertices, and enclosing spheres; they do not calculate Gaussian exposed-vertex probabilities, two-objective collisions, or the limiting near-uniform normal-fan law. Related angular-spectrum studies concern nonidentical polytopes. A broader unindexed Gaussian-normal-fan theorem could still cover this statement; this is a residual literature-priority risk, not a claim of exhaustive discovery.

## Mathematical value — PASS
The polytope has exponentially many fractional vertices, while its minimum enclosing sphere is supported by only a handful of vertices. The theorem determines its *entire* spherical normal-cone spectrum up to exact one-dimensional/fixed-parameter probability definitions, proves that random objectives overwhelmingly select fractional vertices with approximately equal probabilities, and evaluates a natural angular collision/Rényi statistic with sharp leading constant. The concentration of collision support size is a nontrivial geometric sampling consequence. These facts are not routine restatements of vertex enumeration or minimum enclosing spheres.

## Limits
This concerns \(F_n=\operatorname{FRAC}(K_n)\) only in canonical coordinates, with independent isotropic directions. The Gaussian integrals are not evaluated in elementary closed form. The error rate is valid rather than optimal; finite computation is only corroborative. Independent mathematical validation is not performed.

Self-review: passed. Independent audit: not yet performed.
