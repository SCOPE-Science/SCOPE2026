# Review: preparation-dependent superdiffusion in an orientationally reset swimmer

**Correctness: PASS.** The proof reduces longitudinal fluctuations by an exact Itô cosine identity to a heavy-tailed renewal count, controls the angular-reward and Brownian remainder in \(L^2\), and derives both initial-condition count coefficients from the Lomax renewal density. A separate sine identity bounds transverse fluctuations. The independent reward quadratures and fixed-seed count diagnostics in checker.py passed; these finite tests supplement, rather than replace, the analytical proof.

**Originality: PASS, qualified.** Baouche et al. (arXiv:2405.06769) give the orientational-reset renewal framework but evaluate Poisson late-time transport; Kumar et al. (arXiv:2008.03294) treat Poisson resets. Horii et al. (arXiv:2203.08584) establish critical heavy-tail count variance methods, explicitly credited. The new statement joins the angular-reward reduction, the noncritical exact superdiffusive coefficient, the stationary-to-fresh ratio, and the transverse contrast. A previous finite-third-moment swimmer analysis does not cover this Lomax regime. General renewal-reward priority coverage remains a genuine risk.

**Mathematical value: PASS.** The theorem supplies an exact, testable physical distinction between stationarity-prepared and freshly reset swimmers, and establishes a directional transport contrast. The exact ratio depends on a natural heavy-tail index rather than a handpicked finite configuration.

**Limits.** The proof concerns the Lomax survival with \(1<lpha<2\), positive angular diffusivity, heading-only resetting and the preparation definitions in RESULT.md. No position-stationarity or Gaussian limit is asserted. An independent scientific audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
