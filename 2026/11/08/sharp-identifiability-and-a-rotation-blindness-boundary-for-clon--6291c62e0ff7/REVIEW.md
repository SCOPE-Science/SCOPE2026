# Scientific review: clonal covariance rotation identification

## Correctness — PASS

The model is fixed: finite \(d\ge2\), \(S=S^T\succ0\), \(\Omega^T=-\Omega\), root law \(\mathcal N(0,I_d)\), binary rate-one Yule branching, and independent OU noises after division. The Lyapunov relation proves that \(I_d\) is stationary covariance; stationary covariance whitening also transports the proof to general positive-diffusion OU models; the many-to-two decomposition yields \(K(t)=I_d+2\int_0^t e^u e^{-Au}e^{-A^Tu}\,du\) with the correct factor \(2\) and growth normalization. Three exact differentiations produce \(K''(0)=2I_d-4S\) and \(K'''(0)=2(I_d-2S)^2+4[\Omega,S]\). Orthogonal diagonalization recovers every rotation coefficient for pairwise distinct eigenvalues. A nearest-pair skew perturbation saturates the inverse Lipschitz bound \(1/(4\delta)\). A nonzero skew action within a repeated eigenspace commutes with damping and is invisible for every time; its steady current has strictly positive quadratic entropy production. The standalone checker passed 287 rational checks in specified finite-dimensional instances. These checks support but do not replace the symbolic proof.

## Originality — PASS, qualified

Michoel (2026), Appendix B.1, equation (19), is the directly relevant source of the general branching covariance formula, with two-dimensional nonequilibrium examples in B.2–B.3. This foundational integral is not claimed as original. A close reading of those sections did not identify the claimed full rotation-identifiability dichotomy, short-time jet reconstruction, sharp smallest-gap stability constant, or all-age invisible-current construction. Godrèche and Luck (2018) treat stationary current/entropy production and **single-particle two-time** correlations; Adamczak and Miłoś (2011) establish branching OU limit laws rather than this inverse observation map. External research searches and mathematical research-record searches also targeted alternate notions of generator reconstruction, covariance Gramian inversion, circulations and rotational identifiability. No identified result dominates the four-part theorem, but a general system-identification theorem could do so. No finite search proves novelty or independent publication priority.

## Value — PASS

The observation is a natural one in growing clonal populations: covariance of whole-population totals at different ages, without tracking individual lineages. Recovering an irreversible antisymmetric drift from that symmetric observation has an actual structural obstacle. The theorem gives a complete spectral criterion in all dimensions, also applicable after stationarity whitening to general nondegenerate OU diffusions, identifies the first informative derivative and optimal inverse amplification, and constructs physically irreversible processes that cannot be distinguished by this observable at any age. This is an experimentally relevant observability/no-go boundary, not an arbitrary finite example or mere restatement of a source formula.

## Closest literature and residual risks

The first exact covariance formula predates this theorem and is explicitly attributed to Michoel (2026). The stationary entropy-production formula is classical and attributed to Godrèche and Luck (2018). The normalized theorem extends by exact whitening to positive-diffusion stationary OU processes; known rate, stationary root law and full matrix observation remain essential. A stronger, not-yet-located general matrix-exponential/Gramian inverse theorem might subsume the jet reconstruction. Exact derivatives of noisy experimental data are unstable and no estimator is claimed.

Self-review: passed. Independent audit: not yet performed.
