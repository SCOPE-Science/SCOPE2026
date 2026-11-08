# Scientific review: spectral memory threshold for time averages

## Correctness — PASS
The finite-time Beta expectation follows from the exact two-moment jump/Dynkin system for equilibrium-initialized eigenobservables and a convergent power-series solution. The three asymptotic constants follow from explicit Beta inverse-moment and endpoint calculations. The standard-library verifier independently solves the moment ODE and discretizes the underlying memory-reset trajectory. All 16 packaged checks passed. Numerical checks support, but do not replace, the analytical proof. The claim does not assert a limit distribution or extend to arbitrary non-eigenobservables.

## Originality — PASS (best-knowledge assessment)
The closest directly relevant full texts are Boyer–Majumdar 2024 (arXiv:2405.10283) and Boyer–Evans–Majumdar 2024 (arXiv:2411.00641); both analyze marginal position laws and their spectral relaxation, not the physical-time integrated eigenobservable variance. The earlier Boyer–Solis-Salas preferential-relocation walk concerns unconfined displacement/visit statistics. Stojkoski and collaborators (arXiv:2107.11686) explicitly analyze time-average variance but under fixed-position, renewal resetting; their Markov renewal covariance does not imply the nonrenewal uniform-history Beta law. Searches of published mathematics results and literature covering time averages, beta mixtures, eigenmodes and anomalous variance scaling did not identify a dominating statement. The precise novelty claim is limited to the integrated-observable Beta identity and its transition, not the already known Gibbs stationary marginal or marginal relaxation exponent. An unindexed general reinforced-process fluctuation theorem remains a genuine priority risk.

## Mathematical value — PASS
The theorem identifies a sharp spectral threshold separating ordinary, logarithmically critical and anomalously slow mean-square averaging despite exact Gibbs one-time equilibrium. Its exact finite-time formula and constants quantify the observation-time cost of long-range memory. Unlike a mere reformulation of a marginal relaxation exponent, it addresses path-dependent fluctuations whose law requires two-time information and whose transition is not fixed by the one-time stationary density.

## Closest literature and scientific limitations
The model is the uniform-past relocation protocol of arXiv:2405.10283; arXiv:2411.00641 places it within a family of memory kernels. The proof only controls second moments for equilibrium-initialized eigenobservables; full fluctuation distributions, rates for non-eigenfunctions and general kernels remain unproved. Publication priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
