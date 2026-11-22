# Scientific review

## Correctness

**PASS.** The Bloch generator is strictly relaxing for positive dephasing and reset rates and has a unique full-rank stationary state. Direct application of the exact single-qubit QFI identity produces the rational frequency-information law. Exact differentiation reduces its positive-rate derivative to a polynomial with four positive and three negative consecutive coefficients, so Descartes' rule plus the endpoint signs proves one and only one global optimizer. Exact factorizations establish the zero-detuning root and the strict scaled lower bound; implicit-function and fixed-scale polynomial trapping prove both asymptotic laws. The accompanying checker independently verifies rational identities and matrix-SLD quadrature comparisons. No finite numerical test is used to infer a universal statement.

## Originality

**PASS, with residual priority risk.** The 2022 quantum stochastic-reset ensembles and 2024 discrete-time reset-state work do not state or imply this strictly dephased continuous-time steady-state QFI optimization. A publicly summarized discrete-time phase-information optimum is close but concerns a unitary gate with Bernoulli, rather than continuously dephased Poisson, resetting. Li–Tong–Bao (2026) develop broad QFI response theory and related frequency metrology, but their specifically treated frequency probe is transient and amplitude damped; their analytically optimized stationary task is thermal parameter estimation. Exact source passages are compared in the accompanying structured record. A general derivative identity could reduce the algebra but does not itself yield this all-frequency one-positive-root theorem. Independent publication-priority verification remains outstanding, and continuous-time QFI generalizations not captured in this comparison remain possible.

## Mathematical value

**PASS.** In open-quantum-frequency metrology the reset clock is a natural controllable resource: too rare resets permit dephasing, while too frequent resets obstruct phase accumulation. A rigorous unique global optimum, a strict nonzero-detuning frequency/dephasing lower bound, and sharp weak- and strong-detuning laws give a complete quantitative rate-design benchmark not provided by stationary-state formulas alone. This result is about locally optimal single-copy stationary QFI, not time-normalized metrology, measurement-record information, preparation overhead or adaptive frequency-global performance.

## Closest literature and limitations

Magoni et al., arXiv:2202.12655 (2022), provide continuous quantum-reset ensembles; Wald et al., arXiv:2410.11497 (2024), analyze unitary discrete-time resets; Li, Tong and Bao, arXiv:2610.31249 (2026), derive a broad QFI-response identity and study transient amplitude-damped frequency sensing. The published discrete-phase optimization record is especially close and its complete publicly accessible theorem/proof was compared by state generator, dephasing, clock and estimated parameter. The closest discrete stationary phase-QFI full theorem was inspected and does not address positive continuous dephasing. The possibility of another broader unpublished or implicitly specializing theorem is not excluded; only the newly stated claim received this scientific assessment.

Self-review: passed. Independent audit: not yet performed.
