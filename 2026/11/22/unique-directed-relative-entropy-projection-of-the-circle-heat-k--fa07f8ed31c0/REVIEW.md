# Self-review

**Correctness — PASS.** The Fourier logarithm identity gives the exact directed-KL objective. The positive moment-ordering inequality forces a globally unique scalar crossing, not just a local stationary point. Gaussian–Cauchy rescaling with logarithmic uniform integrability yields a finite universal limiting optimal KL, while the moment-matched candidate has logarithmically divergent KL. An independent scalar and circle-quadrature checker passed 92 finite diagnostics; these do not replace the analytic arguments. The center, parameter boundaries, and large-time expansion were checked.

**Originality — PASS (best-knowledge, residual risk).** Read Bailey's 2020-deposited thesis Chapter 6 and Appendix C1: it gives analytic squared-L2 comparisons of circular mixtures and numerical KL grids for mixture fitting, not the unique heat-to-Poisson forward-KL all-time theorem. A recoverable earlier heat-to-Poisson result used squared L2, not KL. Other earlier Poisson-mixture KL and Poisson-to-von-Mises squared-L2 calculations involve different sources/models. Otani–Matsuda's 2026 article treats Wasserstein projection rather than this exact heat-to-Poisson KL projection. The full 2020 Bailey–Codling article could not be inspected; independent priority verification is needed.

**Value — PASS.** The strict optimum is a natural population information projection and its asymptotics quantify a genuinely nontrivial loss mismatch: calibrating to the first circular moment produces unbounded KL at small diffusion times even though the optimal KL stays finite. It supplies explicit reproducible constants and a global solution.

**Scope and risk.** Only forward KL of one circle heat source by one Poisson kernel; general mixtures and reverse KL are unproved. Numerical diagnostics are finite, and priority is provisional.

Self-review: passed. Independent audit: not yet performed.
