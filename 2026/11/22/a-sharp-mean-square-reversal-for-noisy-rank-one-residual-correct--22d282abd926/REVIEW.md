# Scientific review

**Correctness: PASS.** The covariance map is exact for independent, centered equal-variance matrix entries. The rank-one nilpotent programmed mean gives a positive two-state transfer with the stated Perron radius; exact scalar products give the corrected-angle law. A nondegenerate Gaussian setup probe has positive probability on every angular arc, proving the unconditional rare-event result. The provided checker ran successfully; finite tests complement but do not prove the universal quantifiers.

**Originality: PASS (qualified).** The 2026 source proves single-application energy projection and analyzes averaged read/probing fluctuations, but explicitly leaves full iteration stability theory outside scope. The closest full-text nonsymmetric two-grid theory treats deterministic compatible transfer operators and does not imply an iid-read mean-square product spectrum. Searches for equivalent formulations and broader coverage did not reveal this exact pair of phase boundaries or Gaussian learned-space discontinuity. These searches are not a novelty proof; an older deflation projection article was available only as an abstract.

**Value: PASS.** The quantitative gap between samplewise energy improvement and long-run mean-square convergence is a substantial limitation when assessing unguarded stochastic stationary iterations. Exact orientation and noise safeguards, and the discontinuity introduced by even small full-support probe noise, provide a reusable benchmark for analyzing learned correction spaces rather than an arbitrary numerical example. The statement concerns a two-dimensional, highly nonnormal programmed mean; it is not a convergence conclusion for FGMRES, all matrix systems or actual hardware likelihoods.

## Primary literature and limits

- Shah, Li, Kalantzis, Xi, *Noise-Adaptive Analog–Digital Preconditioning*, arXiv:2611.17251v1, Sections 2-3 and 5 (full available HTML examined).
- Nabben and Rooch, *Optimal transfer operators for nonsymmetric two-grid methods*, arXiv:2604.21648v1, deterministic nonsymmetric two-grid theorems and normality discussion (full available HTML examined).
- García Ramos, Kehl and Nabben, *Projections, Deflation, and Multigrid for Nonsymmetric Matrices*, DOI 10.1137/18M1180268 (abstract only; priority risk explicitly retained).

Self-review: passed. Independent audit: not yet performed.
