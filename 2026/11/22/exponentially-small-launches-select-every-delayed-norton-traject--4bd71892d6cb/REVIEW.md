# Review of the finite-sphere launch selection theorem

## Correctness (PASS)

The theorem follows from the source's exact generalized meridian-offset geometry, now with strictly positive initial kinetic energy. Its key novelty in the proof is the uniform comparison of an inner rescaled integral with the elementary \(\operatorname{arsinh}\) integral: the discrepancy is bounded by an integrable weight \(y^{(a-1)/a-1}+s^2y^{2/a-1}\). The outer travel-time integral differs from its point-particle counterpart by \(O(\sqrt{\rho/g})\); matching the two regions yields a uniform error for every \(0<\eta\le1\). Inversion of monotone hitting-time maps selects all finite and infinite waiting times. The positive normal reaction checks the chosen contact model. Reproducible numerical checks from the embedded script pass 174 assertions but are not used as substitutes for the proof. The proof is local and has fixed exponent and geometry parameters.

## Originality (PASS, with residual risk)

Chen and Kuo, arXiv:2611.16797v1, equations (35)–(55) and Section 7, establish the exact geometry and no-departure statement at zero initial speed, but not the new velocity-dependent matched asymptotic or branch-selection classification. Vanpoucke and Wenmackers, Chaos 31 (2021), use hyperfinite-grid priors for point dynamics rather than rigid-sphere geometry. Eyink and Bandak, arXiv:2007.01333, examine stochastic regularization of a different non-Lipschitz system. Search comparisons used equivalent formulations (logarithmic launch delay, finite-radius singular limit, waiting-time selection), broader possible regularization theorems, and direct comparison with the source's exact equations. No covering published-finding corpus item or source statement was identified. Fletcher's *Minimal Approximations and Norton's Dome* has relevant thematic overlap but its full text was inaccessible; a genuinely equivalent result implicit in older regularization literature remains a risk, rather than being excluded by search alone.

## Value (PASS)

The motivating gap is the source's strict separation between finite-radius uniqueness from exact rest and instability under perturbations. The theorem determines the exact noncommuting limit of radius and launch velocity; it distinguishes zero-delay, arbitrary finite-delay and never-departing limits, with one universal exponential cutoff independent of the dome exponent after natural normalization. This gives a structural selection mechanism for the classical nonuniqueness example, beyond a restated fixed-radius uniqueness result.

Self-review: passed. Independent audit: not yet performed.
