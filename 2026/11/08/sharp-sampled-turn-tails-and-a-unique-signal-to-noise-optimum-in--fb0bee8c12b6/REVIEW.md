# Scientific self-review

## Correctness — PASS

The result is the single combined theorem on the physical sampled principal turn of the two-temperature Brownian gyrator. The stationary covariance and current follow from a positive stable Lyapunov equation. The critical nonstandard lemma is geometric: each sign of a fixed-threshold chord angle occupies area \(\ell^2 H(\alpha)/2\), allowing direct integration of Gaussian displacements in the \(O(\sqrt h)\) core. The exact result is distinguished from a finite-h simulation. Tail domination and annular angular linearization give the moment trichotomy with the logarithmic exponent-two boundary. Antisymmetrized stationary flux gives the signed mean; a derivative quadratic with one positive root gives the unique signal-to-variance maximizer. The special case of equal bath temperatures is explicitly excluded from unique SNR optimality, and all limits hold at fixed parameters.

A standalone checker uses independently integrated circle segments, symbolic differentiation, stationary Lyapunov identities, exact conditional Gaussian transitions and a bounded numerical optimizer. The checker passed 537 assertions when run against the packaged file; the numerical experiment does not prove infinite-time or asymptotic statements.

## Originality — PASS, qualified

Viot et al. (2023), https://arxiv.org/abs/2307.05248, already give the Brownian-gyrator model, mean angular velocity, and the \(|\mathcal W|^{-3}\) tail of an unbounded rational finite difference. They note that the actually sampled principal angle is bounded. The mean and velocity tail are *not* novelty claims; the leading log coefficient is compatible with the earlier tail and is not asserted independently new.

Le Doussal et al. (2009), https://arxiv.org/abs/0904.0582, give a two-time periodized angle law for reflection-symmetric rotationally invariant Gaussian processes; the isotropic special case is already covered. Vakeroudis, https://arxiv.org/abs/1007.4648, treats continuously unwrapped isotropic OU winding and hitting times. Afifi and Dusséaux (2021), https://doi.org/10.1049/mia2.12071, provide a proper Gaussian scattering phase-difference law with equal real/imaginary variances, not the improper nonreversible gyrator law. Buckley and Feldheim (2017), https://link.springer.com/article/10.1007/s00440-017-0816-7, require differentiable Gaussian paths. The assessed novelty is the explicit universal finite-principal-turn rare-angle coefficient for anisotropic dynamics, complete moment constants and exact operative coupling optimum. No dominating statement was found in the inspected material or accessible research records. General improper-Gaussian phase literature is a genuine residual priority risk.

## Mathematical value — PASS

The chord-angle statistic is a concrete and different physical observable from rational angular velocity, with a precise branch-cut regularization of heavy fluctuations. It yields measurable rare large-turn probabilities and a unique exact coupling setting optimizing the small-lag directional signal-to-noise ratio. The sharp threshold at moment order two separates typical Gaussian-scale motion from rare-origin events. The theorem is restricted to stationary single increments; no unsupported thermodynamic efficiency or independent-event conclusions are made.

## Literature and verification limitations

Primary full text and source equations were compared for scientific implications, including the source's supplementary sampling definition. A complex-Gaussian formula for more general improper covariance might implicitly dominate some parts of the result despite the negative bounded searches. The signed mean and the unbounded velocity PDF are established facts from the motivating paper. This is a self-review only; scientific priority and correctness have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
