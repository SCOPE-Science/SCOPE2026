# Self-review

## Correctness — PASS
The two original matrix equations have exact rank-one solution and a four-dimensional Sylvester operator with absolute eigen-gaps \(1,3,1,1\), hence minimal singular value one. Independent Haar coordinates give two arcsine variables; elimination of the scalar projected equations yields the stated reciprocal gap. Changing the conditional variable to \(r=\sqrt{1-s}\) produces a root interval of **exact width** \(\sqrt{1-t}/(2R)\). Bounded convergence on \(t<1/2\) and an \(O(R^{-3})\) estimate on \(t>1/2\) prove the coefficient \(2\operatorname{arsinh}(1)/\pi^2\). Tail comparison and layer cake prove both error tails and moment classification. Exact symbolic checks and numerical quadrature were run. No finite simulation is used as an infinite-tail proof.

## Originality — PASS (with residual priority risk)
The motivating full-text source proves disjoint-field-of-values sufficiency, while its global spectral-disjointness hypothesis holds here but its field-of-values condition fails. It does not provide an independent Haar projection probability or inverse-moment law. The accessible full text of Beckermann–Kressner–Tobler (2013) proves results for a positive definite Kronecker operator and rational Krylov subspaces; those assumptions exclude this indefinite Sylvester difference. The Beckermann (2011) paper concerns rational Krylov residual bounds, while Fasi–Hashemi (2026) concerns conditioning of the exact solution; only abstracts of those two papers were accessible in this review. Their uninspected details and less direct inverse-moment literature are residual historical-priority risks. The novelty asserted is the concrete exact tail constant and moment frontier, not the familiar small-denominator principle.

## Mathematical value — PASS
Random trial bases are a natural benchmark for projection robustness. This exact, already-rank-one problem separates full-system conditioning (operator separation one), almost-sure projected solvability, and the much stronger integrability required by expected-error guarantees. The sharp cutoff and explicit constant provide a test case for probabilistic well-posedness safeguards; a prescribed structured trial basis would instead avoid the failure. The theorem is scoped to this precise mechanism and is not represented as a guarantee about an actual Krylov algorithm.

## Closest literature and limitations
See the four sources in `RESULT.md`; the field-of-values hypothesis and the positive-definite-operator hypothesis are decisive differences, rather than merely differing titles. The infinite moment claims concern independent real Haar one-dimensional trial spaces and exact arithmetic only. Broad historical-priority uncertainty remains, and no independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
