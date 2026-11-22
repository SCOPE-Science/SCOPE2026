# Scientific review

## Correctness — PASS

The normalization is checked under the Ito generator \(\mathcal L=\mathcal D(\theta):\nabla^2+q\partial_{\theta\theta}+r(\mathrm{reset}-I)\). The exact stationary mixed-moment identities supply the positive initial covariance and a nonzero orientation-energy cross moment. The Markov semigroup then gives a forced scalar linear covariance equation with precisely one negative forcing exponential. Factoring out the positive reset exponential reduces all sign assertions to one strictly decreasing integral bracket. Solving the single positive root of its algebraic limiting inequality produces the stated sharp rate. The exact resonant and critical limits and the isotropic boundary are treated separately. The standalone checker passed 1,477 assertions; those finite diagnostics are not the proof. Risks: only the stated positive-parameter passive diffusion model is covered.

## Originality — PASS, qualified

The closest foundational source, Chaki–Stølevik Olsen–Löwen (2024, arXiv:2406.17550), gives the same position-only resetting model but its complete relevant section derives one-time second moments and ordinary signed-coordinate covariance. The previously published *Hidden stationary anisotropy under position-only resetting* obtains the stationary fourth moment but not a two-time orthogonal squared-position correlation, a negative lag, or a sharp single-crossing threshold. The complete inspected results concerning orientation-only resets, joint resets, and independently resetting diffusivity have different dynamical generators and do not imply this particular sign law. Searches of the mathematical-results index and primary literature did not identify a stronger equivalent theorem. Publication priority is nonetheless not an independence claim: unidentified equivalent literature or a broad general formula could supersede the result.

## Mathematical value — PASS

The sign reversal is a nontrivial, directly observable temporal effect that the stationary rotation-invariant position law and positive simultaneous cross-energy covariance conceal. A sharp shape-dependent control threshold separates positive-only temporal correlations from exactly one delayed anticorrelation, with a calculable crossing time and limiting rate range. It distinguishes angular memory retained across positional resets from both synchronous resetting and scalar positive stochastic diffusivity, making it a useful fourth-order temporal diagnostic rather than a rephrasing of known one-point kurtosis. The result does not provide a two-time joint distribution or finite-sample inference bounds.

Self-review: passed. Independent audit: not yet performed.
