# Scientific review

## Correctness — PASS

The one-dimensional zero-source equilibrium makes the assembled finite-element flux constant, and summing nodal differences proves an exact reciprocal-resistance identity. Each mesh-cut interface contributes one independent centered Bernoulli correction, with explicitly signed resistivity jump. Uniform boundedness and positive resistances justify the expansions, Jensen's inequality gives the upward mean bias, and the arithmetic-versus-harmonic mean identity proves the deterministic Galerkin comparison. Rational independence, compactness and Kronecker–Weyl theory give the *complete*, not merely sampled, subsequential/Cesàro limit families. Reproducibility: \(\texttt{verify.py}\), 136 exact/arithmetic and finite asymptotic checks at review. The analytic proofs, not finite experiments, establish the universal quantifiers.

## Originality — PASS, with bounded historical-priority risk

The closest method-level source is Kruse–Polydorides–Wu, arXiv:1908.08901 (first public 2019, even though journal publication is 2026), especially their randomized stiffness bilinear form and error bounds in Section 3.2. Their paper treats an elliptic equation on a planar polygon, provides general mean-square estimates and numerical experiments, and does not furnish the exact one-dimensional sampled-flux distribution or its arithmetic phase diagram. Yang–Zhai, arXiv:2606.01814 (first public June 1, 2026), considers interface-aware immersed finite elements and motivates accurate treatment of cut geometry, not the random quadrature model. Related published phase results concern direct indicator quadrature or random Euler forcing, not inversion of sampled elliptic stiffness. Searches of semantic mathematical records, source aliases, method reductions and external literature identified no implication covering the joint flux theorem. The published-finding corpus matches supplied short summaries rather than full documents, and an unindexed equivalent calculation remains possible; neither a search miss nor a partition is claimed as proof of uniqueness.

## Value — PASS

This is a motivated distributional benchmark for a method that uses only one coefficient sample in each element in the presence of unresolved material interfaces. It explains how the same random stiffness construction yields a small mean bias but a non-Gaussian, mesh-phase-sensitive first-order random error. The full family of phase limits, its exact triangular Cesàro average and the contrast with exact-stiffness Galerkin flux supply structural facts useful for uncertainty assessment and for separating sampling effects from interface discretization. The value concerns this precise model, without unsupported claims about superior runtime, higher-dimensional accuracy or mean-square domination.

## Closest literature and limits

Yang–Zhai (2026) is a recent eligible interface-numerics motivation, not a predecessor of random stiffness quadrature. Kruse–Polydorides–Wu (2019 preprint, 2026 journal) is the key earlier randomized-assembly method and explicitly retains its priority. The nearest mathematical-record comparisons include published mesh-phase laws for quadrature of indicators and a Bernoulli jump-phase law for coupled Euler grids. No inspected source establishes the complete 1D sampled-elliptic-flux phase classification, but summary-only record access leaves residual priority uncertainty. The exact theorem requires positive finitely layered coefficients, zero volume forcing and rationally independent interfaces for the complete limit description.

Self-review: passed. Independent audit: not yet performed.
