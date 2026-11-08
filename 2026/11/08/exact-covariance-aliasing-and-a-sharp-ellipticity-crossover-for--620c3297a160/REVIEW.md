# Scientific review: exact covariance aliasing for integrating-factor Lyapunov integrators

## Correctness — PASS

The two published integrating-factor methods reduce to composite trapezoidal and Simpson quadrature of a continuously rotating rank-one projector. The matrix trace is exactly the elapsed time, and the two-dimensional anisotropy is a geometric sum of doubled phase angles. Those facts yield both eigenvalue formulas without numerical approximation. A positive-sum spanning argument identifies *all* singular step phases and directly proves the odd-half-turn rank separation; a short trigonometric inequality proves exact continuous strict positivity. The comparison phase is exactly determined by a piecewise linear expression in cosine. The displayed near-resonance expansions follow by Taylor series with fixed iteration count. Direct-stage numerical checks passed 2940 comparisons. These diagnostics are supportive only, not an infinite-dimensional proof; the theorem itself is finite-dimensional and analytic.

## Originality — PASS, with stated historical risk

Zhang–Lan–Jing (arXiv:2606.15703v1) introduced IF-SSPRK2/3 and showed preservation of positive semidefiniteness, but their method, theorem and experiments do not state the exact two-method covariance spectra, strict-positivity resonances, or signed crossover at the half-turn phase sector. The general integrating-factor SSP literature (Gottlieb–Grant–Isherwood, arXiv:1708.02595) supplies the algorithmic framework but does not imply the oscillator-specific eigenvalues as a stated theorem. Standard continuous reachability theory already implies that the exact oscillator covariance is positive definite; no novelty is claimed for that fact alone. Related empirical-Gramian analysis (Grundel–Himpe–Saak, 2019) treats general reachability approximations. The earlier Gillis–Diehl positivity-preserving scheme uses a different discretization (only an abstract was accessible). Semantic mathematical-record searches addressing Simpson, trapezoid, exact covariance ranks, aliasing and SSP integrating factors did not identify the full comparison statement; failure to locate one is not proof of priority. Equivalent older sampled-Gramian results remain a meaningful residual risk.

## Value — PASS

A positive-semidefinite discretization can become singular despite a strictly positive-definite continuous covariance. Rank loss can break downstream control-energy and Kalman-type inverse-covariance calculations even when negative eigenvalues never occur. The exact classification shows that the higher-order scheme eliminates half-turn numerical rank failure, and the global crossover prevents an incorrect inference that higher order always gives a better minimum eigenvalue. This is a natural diagnostic for step selection and explains a structural stability distinction not measured by ordinary convergence order.

## Scope and limitations

The proof assumes a nonzero fixed planar angular velocity, zero initial covariance, a single constant rank-one forcing vector, exact exponentials, and fixed positive steps. It is not a characterization of arbitrary differential Lyapunov systems, floating-point positivity, statistical confidence accuracy, or universal higher-order superiority. Additional historical source coverage and independent mathematical assessment remain open.

Self-review: passed. Independent audit: not yet performed.
