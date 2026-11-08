# Scientific review: moment-preserving softmax rounding

## Correctness — PASS

The exact domain fixes integers \(K\ge n\ge3\), positive rounding bins and interior Bernoulli marginals, and imposes \((n-1)\)-wise independence. The feasible-law derivation is the one-dimensional alternating nullspace of all proper-subset product-moment constraints. Each candidate probability is nonnegative exactly on the displayed closed parameter interval. For softmax log-loss, label-dependent linear terms have fixed expectation and the only changing term is a mixed difference of log-sum-exp. The identity \(\partial_1\cdots\partial_n\log\sum_j e^{z_j}=(-1)^{n-1}(n-1)!\prod_{i=1}^n\pi_i\) has been derived by induction and has strict sign, establishing a unique minimizing endpoint and exact gain. The fair-parity and common-bin-width formulas follow by exact substitution. The standalone finite checker produced `PASS 4283 checks`, including 100 SciPy linear programs; tests do not replace the general proof.

## Originality — PASS, with a clearly bounded priority risk

Natarajan, Ramachandra and Tan (arXiv:2211.01596, Section 2 and Theorem 9) **already derive the entire \((n-1)\)-wise-independent law family**; Bernstein parity examples are also known. Neither the Boolean-lattice parametrization nor the existence of fair parity couplings is new here. The new claim is the loss-specific sign theorem, sharp label-universal coupling choice, exact analytic softmax risk increment, and all-dimensional unbounded fair-grid gap. Chatelain and de Oliveira Castro (arXiv:2610.01889, Sections 5.1–5.3) analyze mean-independent operational rounding and second-order Fisher loss, without choosing dependence at a simultaneous output-logit rounding step. Ramachandra and Natarajan (arXiv:2006.00516) provide general probability bounds, not the softmax optimization. Accessible mathematical-record searches did not identify an equivalent statement. An unindexed generic higher-order supermodular-order theorem specialized to log-sum-exp could dominate this result; this residual historical-priority possibility remains.

## Value — PASS

The problem is motivated by stochastic rounding of multiple softmax logits: independently sampled rounding indicators are not the only unbiased coupling, and preserving every covariance is not sufficient to determine expected log-loss. The structural all-order derivative rule picks a unique coupling *uniformly over labels and positive bin widths*, without solving a separate linear program for each input. The exact fair-grid gap \(h/2^n+O(1)\) shows the discrepancy from a second-order covariance-based surrogate can be arbitrarily large in an expressly defined benchmark, and the three-coordinate formula quantifies it at finite bin widths. This is a mathematical calibration benchmark, not evidence for a production implementation or replacement for mean-independent operation-level stochastic rounding.

## Sources and limitations

Full relevant paper text/sections inspected: Chatelain–de Oliveira Castro, arXiv:2610.01889, Sections 1, 5.1–5.3 and conclusions (accessible textual rendering); Natarajan–Ramachandra–Tan, arXiv:2211.01596, especially pages 1–8 and Theorem 9 (PDF). Abstract/metadata checked for Ramachandra–Natarajan, DOI:10.1137/21M1408294; Blanchard–Higham–Higham, https://eprints.maths.manchester.ac.uk/2765/ . The same-source mathematical comparisons were made at the level of theorems, not titles. Potential uncovered equivalent softmax coupling theorems cannot be excluded by unsuccessful searches. All calculations concern a single logit-rounding stage; no conclusions are claimed for full training, top-1 prediction, or nested arithmetic operations.

Self-review: passed. Independent audit: not yet performed.
