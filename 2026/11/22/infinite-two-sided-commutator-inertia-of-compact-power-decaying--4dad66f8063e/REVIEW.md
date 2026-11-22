# Scientific review: infinite two-sided commutator inertia of compact power-decaying Rhaly operators

## Correctness — PASS

The weight-ratio assumption gives a positive finite limit for \((n+1)^sa_n\), hence \(R_a\) is Hilbert–Schmidt and \(K_a\) is trace class. The exact self-commutator matrix (equation (1) in `RESULT.md`) has eventually negative diagonal entries with a strictly negative leading coefficient. Widely separated coordinate vectors provide negative definite subspaces of every finite dimension. Independently, the exact finite-support actions of the adjoint on second-difference vectors give strictly positive quadratic forms with the leading coefficient \(2s\); their normalized remote cross-terms tend to zero, giving positive definite subspaces of every dimension. Compact self-adjoint spectral theory then gives infinitely many eigenvalues on both sides of zero. The numerical checker replayed 182 supplementary finite/high-precision assertions; the asymptotic proof is the essential evidence for the unbounded dimension conclusion.

## Originality — PASS (qualified)

The directly relevant Gallardo-Gutiérrez–Partington paper (arXiv:2408.03182, 2024-08-06) reports compactness and nonhyponormality for power-decaying Rhaly operators and studies the spectrum of \(R_a\) and invariant subspaces. Its nonhyponormality implies only that the commutator has *some* negative spectrum; it does not imply infinite negative **and** positive inertia. The later Bellavita–Dellepiane–Stylogiannis paper (arXiv:2503.21930, 2025-03-27) characterizes compactness and Schatten properties of \(R_a\); it does not establish signed eigenvalue counts of \(K_a\). Related Cesàro commutator classifications concern nonidentical triangular kernels. No equivalent signed-inertia theorem was found in the examined literature, but this negative search is not a proof of global priority. Residual risk: older unindexed terraced-matrix/commutator literature or a broad factorable-matrix inertia theorem may contain the statement.

## Mathematical value — PASS

The natural family of compact Rhaly operators was previously known to be nonhyponormal, leaving the **dimension of the failure of hyponormality** open in the compared sources. A compact operator's commutator can have finite or infinite negative index, and trace zero does not distinguish these possibilities. This theorem establishes infinite negative as well as positive spectral inertia for every power-decay exponent above the Cesàro boundary, and proves a stable version under second-order ratio perturbations. It answers a structural operator-theoretic question beyond the already known qualitative compactness and nonhyponormality.

## Limitations and comparison risks

The result gives signs/inertia, not sizes or precise Weyl asymptotics of eigenvalues. It covers positive real weights with the stated second-order ratio condition; arbitrary complex, oscillatory, or merely first-order regularly varying weights remain outside the claim. Independent mathematical validation is not yet available. The checker is only supplementary to the analytic argument. Literature and equivalence searches cannot rule out inaccessible historical sources.

Self-review: passed. Independent audit: not yet performed.
