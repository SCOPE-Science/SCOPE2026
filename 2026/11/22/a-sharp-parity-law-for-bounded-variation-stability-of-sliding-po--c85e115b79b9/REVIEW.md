# Review of the sliding population-variance stability theorem

**Correctness — PASS.** The derivative of the second central moment along a step is derived explicitly. The sharp sign-pair lemma is proven by linear-program extremality on a cube: it counts opposite-sign pairs exactly, giving the upper bound for every window length. The balanced-block binary baseline and symmetric interior perturbations prove sharpness without assuming attainment. The actual standalone checker passed exact finite-chamber, sign-duality, extremizer, and randomized two-input tests.

**Originality — PASS, with residual risk.** The accessible full 2015 Wu–Chang article uses local variance as a statistical estimator but supplies no exact two-input adjacent-variation Lipschitz theorem. The 2011 Tamburo landing-page description identifies the neighborhood-variance implementation, but the full manuscript was inaccessible and is not characterized as non-covering on abstract evidence. Indexed searches for sliding variance, second central moments, bounded variation and even/odd stability yielded no matching theorem. Related sliding standard-deviation work addresses a different nonlinear operator (the square root) and, in accessible historical comparisons, no all-width amplitude-normalized parity constant. Historical priority is not independently established.

**Mathematical value — PASS.** The interval-normalized theorem is a dimension-free, all-window stability guarantee for local variance features used in intensity and texture analysis. The exact sign-pair formula gives a non-obvious parity distinction: even windows have sharp coefficient one and odd windows have the strictly smaller coefficient \(1-1/m^2\). The full-length regime \(n\ge2m\) is natural because it contains the complete response of a single input step.

**Limits and risks.** Shorter signals may have strictly smaller best constants; this is not classified. The full manuscript of the 2011 implementation could not be inspected, and unindexed equivalent work could exist. No independent review or certification is claimed.

Self-review: passed. Independent audit: not yet performed.
