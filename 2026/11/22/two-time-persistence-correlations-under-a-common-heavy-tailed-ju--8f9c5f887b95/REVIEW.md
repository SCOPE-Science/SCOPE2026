# Scientific review: two-time persistence with one common rate clock

## Correctness — PASS

The claim is for two conditionally independent rate-one symmetric walks killed at zero, with a shared nonnegative rate resampled independently at deterministic intervals. The conditional survival factorization is exact. A reflection/spectral argument gives the single-walk asymptotic \(q_x(a)\sim x\sqrt{2/(\pi a)}\). Independence of rate intervals and their specified Laplace transform yield the joint stable limit at times \(t\) and \(ct\) with the exact clock normalization. Uniform negative moments justify taking expectations of the product rather than invoking weak convergence alone. Double Mellin inversion, a radial substitution and an angular substitution give the stated integral. Association of two strictly decreasing functions of the shared positive stable increment gives the strict common-clock enhancement. Independent stable increments give the large-time-ratio decoupling. The half-stable double-time integral is \(4/3\); a standalone executable numerical consistency check passed. No finite-time or uniform-in-\(c\) assertion is proved.

## Originality — PASS, qualified

The primary full-text source (Levit and Reuveni, arXiv:2609.26925) gives **one-walker** asymptotic first-passage laws in the same rate environment. The earlier full-text model source (Arutkin and Reuveni, arXiv:2302.07041) establishes the doubly stochastic clock framework, not unequal-time two-walker survival. An already published **equal-time** shared-clock multiwalker enhancement includes \(R_{1/2}(1)=\pi/2\); that is excluded from the new contribution and cannot alone determine the function of the observation ratio \(c>1\). Searches for unequal-time first-passage, joint negative stable-clock moments, shared jump-rate random walks and two-observation persistence did not identify a theorem giving the exact two-time profile or the \(4/3\) constant. The integration method is classical; priority may be affected by a multitime stable-moment identity in specialist literature that was not comprehensively indexed.

## Value — PASS

The first observed survivor and the second survivor at a later specified instant provide a natural sequential-reliability and multiparticle-persistence statistic. The result describes *how long* a common random transport environment couples the two probabilities: strict enhancement for every fixed finite observation ratio and an explicit loss of enhancement as that ratio separates. The explicit half-stable ratio \(4/3\) at a double observation horizon is a calibrated exact case not inferred from the known equal-time \(\pi/2\) enhancement. The clock-dependent joint negative-moment kernel, not a routine substitution in a one-walker formula, underlies this genuine unequal-time observable.

## Closest literature and scientific limitations

Levit and Reuveni (2026, arXiv:2609.26925); Arutkin and Reuveni (2023, arXiv:2302.07041); published equal-time multiseracher shared-clock result. The new asymptotic holds for fixed \(c\ge1\), fixed positive lattice starts and deterministic refresh interval, with independent conditional jump noises; it does not quantify finite-time errors, allow simultaneous \(c\)-and-\(t\) limits, or establish monotonicity of the enhancement. The reference integrals and one simulation-free numerical consistency program can be reproduced from the package; the program alone is not an infinite-proof certificate.

Self-review: passed. Independent audit: not yet performed.
