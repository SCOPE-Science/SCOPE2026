# Review of the coupled-reference Gaussian descent theorem

## Correctness — PASS

The derivation explicitly fixes the objective, reference construction, probe covariance, update, and independence between time steps. Isserlis pairings give the exact mean. Conditioning on one Gaussian probe reduces the squared-norm calculation to an identity for a noncentral Gaussian quadratic form; chi-square moment identities then yield two explicit invariant-block coefficients. Their difference is nonnegative, which identifies the exact least-favorable hinted direction. Elementary scalar optimization determines the entire strict one-step contraction range, while the conditional mean recurrence gives the exact mean-square impossibility at and above the coupling boundary. The dimension-free statements come from the algebra, not from extrapolation of finite checks. A standalone checker independently verifies both first and second moments in 105 rational-parameter cases.

## Originality — PASS, qualified

The 2026 directional-hint source gives the control-variate estimator and explicitly requires the exploratory Gaussian direction to be independent of the reference. Its separate practical reference-estimation stage and its oracle estimator do not imply a result for a *jointly Gaussian, same-iteration, one-probe* projected reference. Prior Gaussian projected-control analyses with known reference vectors or independently sampled probes use different dependence assumptions. Earlier general control-variate work establishes why dependence can introduce bias, so no claim is made to invent that principle. Targeted bibliographic and mathematical-record searches did not identify the exact rank-dependent drift reversal and minimax moment formula, but unindexed equivalent estimators and older dependence-bias analyses remain originality risks. These searches are not a proof of novelty.

## Value — PASS

The claim answers a concrete cost-versus-reliability question about eliminating separate reference-estimation directions. The safety threshold depends only on hint rank, holds for any ambient dimension, and cannot be repaired merely by decreasing a positive step once mean drift reverses. The positive-side moment formula also supplies an exact stepsize calibration rather than just a negative example. This constitutes a motivated structural boundary for the computational shortcut, with an explicitly limited quadratic scope.

## Closest literature and limits

Closest primary work: Ryabchenko, Qian and Mou, *Adaptively Incorporating Directional Hints into Zeroth-Order Optimization*, arXiv:2609.08277, Sections 3–4. Relevant control-variate background: Geffner and Domke, *Approximation Based Variance Reduction for Reparameterization Gradients*, arXiv:2007.14634. The theorem deliberately changes the reference/probe dependence in the first paper; it does not dispute its stated results. No extension to noisy or nonlinear settings is established.

Self-review: passed. Independent audit: not yet performed.
