# Scientific review: co-located value–derivative Wiener quadrature

## Correctness — PASS

The theorem quantifies over every real precision budget \(P>0\), site \(z\in[0,1]\), and allocation \(p,q\ge0\) with \(p+q=P\). Gaussian orthogonality gives an exact error-minimization formula with penalty \((|a|+|b|)^2/P\). Explicit sign arguments show that the derivative coefficient is positive and that the mixed branch activates precisely after a scalar site threshold. The derivative of the mixed-branch information is a rational function whose numerator has a verified degree-eight Descartes transform; signs at the activation site, a double-root boundary and a positive shifted expansion exclude interior mixed-branch maxima. An envelope-derivative comparison then proves a unique crossover between the derivative-only interior maximum and the mixed endpoint maximum. The exact endpoint allocation has derivative precision \(2\) and value precision \(P-2\), and both are positive above the crossover.

The standalone checker verifies the symbolic factorizations and polynomial identities, 21 independent numerical white-noise covariance integrations and 131,599 supplementary Gaussian-design comparisons. These computations check algebra and implementation, while the analytic arguments provide the infinite-domain uniqueness proof.

## Originality — PASS (limited claim)

Wu–Aoi–Pillow, arXiv:1704.00060, develops Gaussian-process quadrature using gradients and selects locations but does not give this once-integrated Brownian path target with one co-located two-channel total precision budget. Prüher–Särkkä, DOI:10.1109/MLSP.2016.7738903, provides earlier derivative Gaussian-process quadrature context; accessible abstract material concerns probabilistic moment transformations rather than the precise global allocation classification. Foster–Lyons–Oberhauser, arXiv:1904.06998, concerns Brownian polynomial approximation and time integrals. Karvonen–Kanagawa–Särkkä, arXiv:1812.08509, concerns kernel quadrature weights and point placements rather than derivative/value precision splitting. Related single-channel instrument-choice designs for this path target are strictly narrower than simultaneous two-channel precision design; a related Matérn value/gradient budget result has a different process, functional and coverage. No covering implication was found in the inspected material or claim searches. Historical priority remains uncertain, especially for incompletely accessible derivative-observation design literature.

## Value — PASS

This is a complete structural solution to the natural resource-constrained design problem: does one invest scarce precision in path level, in path slope, or both? The exact answer features a mathematically genuine discontinuous change of location and the invariant post-threshold slope-precision allocation \(q=2\). It supplies the full risk frontier rather than a local numerical optimizer. The model is specific and does not automatically extend to separate sites, correlated errors or general Gaussian kernels.

Self-review: passed. Independent audit: not yet performed.
