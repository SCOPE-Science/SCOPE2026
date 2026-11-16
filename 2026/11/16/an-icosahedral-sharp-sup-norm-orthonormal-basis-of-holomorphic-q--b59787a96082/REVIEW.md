# Self-review

## Correctness — PASS

The normalized complex-sphere fourth moment gives \(\|z^{\mathsf T}Mz\|_2^2=\operatorname{tr}(MM^*)/6\) for symmetric \(3\times3\) matrices. Takagi factorization forces sup norm at least \(\sqrt2\) for any unit-\(L^2\) quadratic, and equality is exactly the symmetric-unitary case. The six displayed real axes have squared pairwise overlap \(1/5\); the phase \(\xi=(-7+i\sqrt{15})/8\) makes their symmetric-unitary phase reflections Hilbert–Schmidt orthogonal. Direct trace arithmetic yields exactly six normalized orthogonal polynomials, each with sup norm \(\sqrt2\). No statistical experiment or numerical convergence is required for the proof. The bundled checker independently tests the finite identities numerically.

## Originality — PASS relative to inspected sources

The primary 2026 papers arXiv:2610.14160 and arXiv:2610.29946 establish dimension-dependent **existence** bounds, and their relevant complete sections were inspected. They do not compute the finite-degree minimax constant or give the displayed icosahedral six-element basis. Sych–Leuchs 2009 supplies the related symmetric-unitary matrix viewpoint only at powers-of-two sizes. The actual statement involves the sharp constant for the entire degree-two space, rather than merely existence or single-polynomial bounds. Related published exact quadratic coefficient estimates concern a different optimization and do not imply an orthonormal minimax basis.

Residual risk: an older equivalent six-symmetric-unitary-matrix construction may occur in the quantum-entanglement or equiangular-line literature under different language; absence from the inspected record is not a comprehensive priority certificate.

## Mathematical value — PASS

The first nontrivial nonlinear homogeneous Hardy component in complex dimension three has six basis elements, so the exact minimax constant is a natural finite-dimensional benchmark for the just-solved general bounded-basis question. The construction simultaneously saturates the best individual-polynomial bound at **every** basis vector. Its bridge from six icosahedral equiangular lines to six complex symmetric unitary matrices provides a concrete exact and potentially reusable design mechanism, not a routine substitution in an existing basis.

## Limits

Only \(K=3\), degree two; no general dimensional optimality or complete classification of all optimizers. Full historical priority remains provisional pending a broader literature audit.

Self-review: passed. Independent audit: not yet performed.
