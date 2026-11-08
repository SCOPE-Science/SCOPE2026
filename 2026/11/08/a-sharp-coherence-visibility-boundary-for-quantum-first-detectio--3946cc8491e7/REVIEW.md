# Scientific review: quantum first-detection ordering threshold

## Correctness

**PASS.** The claim specifies an arbitrary coupled two-level Hermitian Hamiltonian, independent exponential inter-measurement intervals, ideal projectors, both initial/target protocols, and strict ranges for all parameters. The two exact renewal equations yield a signed survival-difference kernel convolved with a strictly nonnegative renewal measure. The kernel sign is governed by the global minimum of the sinc function; its unique first negative-lobe extremum gives the claimed threshold. A fixed-time weak-rate expansion proves necessity and an early-time expansion guarantees survival crossing. An independent exact Laplace inequality establishes the weaker order for every visibility, so no conclusion rests solely on numerical sampling. The included source passed 3278 deterministic consistency assertions, including matrix-exp, kernel, transform and inverse-transform checks. The analytic argument, not those finite checks, establishes the universal quantifiers.

## Originality

**PASS, with residual publication-priority risk.** Kulkarni and Majumdar (arXiv:2305.15123, sections 4.1–4.2) provide the underlying two-scheme transforms and means, but do not give a sharp rate-uniform stochastic-order classification or the crossing-with-Laplace-order separation. Kessler, Barkai and Ziegler (arXiv:2012.01763, Appendix B) analyze return and arrival detection for the two-state case and their moments; the assessed theorem is not a restatement of these results. Del Vecchio Del Vecchio and Majumdar (arXiv:2509.08556, sections 5–7) analyze distributions and optimal time scales on fully connected graphs, not the visibility-dependent all-rate stochastic-order boundary. Related renewal-protocol optimization concerns minimum means rather than a comparison of full survival functions. An earlier exact transform mathematically permits the derivation, and unidentified equivalent order-theoretic analysis remains possible.

## Mathematical value

**PASS.** Mean-first-detection optimization and large-time tail optimization do not determine the ordering of finite-time success probabilities. This theorem gives a necessary-and-sufficient coherence/visibility boundary for an operationally meaningful question: whether detecting the preparation state is uniformly more reliable before every deadline than detecting its complement, regardless of interrogation rate. The regime beyond the threshold separates two stochastic orders and supplies explicit time-and-rate counterexamples. The critical constant is neither a fit nor an arbitrary slice; it is the global minimum of the sinc function forced by the renewal kernel.

## Scope and limitations

The result is restricted to single-qubit, time-independent, ideal projective interrogation at independent exponential epochs; it makes no higher-dimensional or non-Poisson claim. The first-order stochastic-order threshold is exact and uniform over rates, while the above-threshold crossing is proven for sufficiently small rates, not all rates. The 2023 source transforms, 2020 return formulas, 2025 graph analysis and independently motivated unpublished analyses remain the primary publication-priority risks. The numerical checker is reproducibility support, not an infinite-parameter proof.

Self-review: passed. Independent audit: not yet performed.
