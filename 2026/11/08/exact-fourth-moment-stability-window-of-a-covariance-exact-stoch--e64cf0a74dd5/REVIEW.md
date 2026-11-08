# Scientific review

## Correctness — PASS

The invariant density is explicitly normalizable and its tail exponent determines the exact fourth-moment threshold. The numerical update is an independent random affine recursion with strict \(L^2\) contraction; the fourth moment exists exactly when its multiplier has fourth moment below one. Expanding Gaussian moments gives the closed-form formula and the polynomial stability factor. Dividing by the positive step parameter and using \(t+t^{-1}\ge2\) establishes the exact threshold \(2/\sqrt3\), including all equality cases. The accompanying exact-rational verifier passed 3,028 assertions. Tests corroborate but do not establish the proof for all real parameters.

## Originality — PASS, with residual precedence risk

The central comparison is Liu–Mao–Wu, arXiv:2206.09970 (first posted 20 June 2022): its main results concern backward Euler-Maruyama invariant measures, not the all-step exact fourth-moment phase diagram for drift midpoint. Qiu–Liu–Hu (2014) treat second-moment and small-moment boundedness for stochastic theta integration, but not an exact fourth-moment phase classification. Higham (2000) considers homogeneous multiplicative-noise mean-square/asymptotic stability, without a nondegenerate forced stationary law; its full text was not retrieved and is an explicit residual risk. Li–Liu–Xiao (2026) prove small-step invariant-measure convergence for strict \(\theta>1/2\), rather than this endpoint classification. General random-affine moment criteria are acknowledged as standard. Searches for equivalent fourth-order formulas and noise-step windows found no stronger statement among inspected accessible sources, which is not an independent novelty guarantee.

## Value — PASS

Exact matching of stationary covariance is a widely used diagnostic of long-time stochastic integrators. This complete classification shows that covariance accuracy can conceal a qualitatively false fourth-moment tail, and identifies the exact intermediate-step window in which a scheme artificially regularizes a physically infinite fourth moment. It also gives the strict finite-regime bias for every step. This matters for tail-sensitive observables, adaptive stepsize choices and invariant-law benchmarking rather than being merely a recomputation of a known Gaussian moment.

## Boundaries and remaining risks

The result assumes a scalar linear drift, independent Gaussian additive and multiplicative driving noises, explicit diffusion treatment and \(0<b^2<2a\). The all-step conclusions do not extend automatically to correlated driving noises, fully implicit diffusion, variable steps or other theta parameters. The specialist stability literature is extensive; exact earlier coverage cannot be ruled out from accessible sources. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
