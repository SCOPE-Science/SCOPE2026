# Scientific assessment

## Correctness — PASS

**Precise domain:** Equilibrium-renewal simultaneous resetting; \(T>0\) almost surely with finite positive mean and finite second moment; fixed distinct extreme ranks as particle count tends to infinity. The stationary age density is the integrated renewal survival divided by \(\mathbb E T\). Conditional particle positions are independent Gaussian variables with common variance \(2DA\). The Gaussian Gumbel upper-gap theorem yields joint independent exponential gaps after \(k b_N\) scaling. The provided inverse-Mills bound on the high-probability uniform-tail-order-statistic event, with exponential tail-ratio control and negligible exceptional moments, establishes uniform integrability and hence convergence of covariances rather than just weak convergence.

The exact correlation follows by computing \(\mathbb E A=\mathbb E T^2/(2\mathbb E T)\) and \(\mathbb E\sqrt A=2\mathbb E T^{3/2}/(3\mathbb E T)\). Cauchy–Schwarz gives the complete sharp range and uniquely identifies deterministic clocks; a continuous two-point family provides every intermediate value and approaches the unattainable supremum. The checker independently passed all programmed diagnostics, including 10,000 random finite-moment inequality comparisons, 120 common-scale cancellations, and finite-size gap samples. None of those finite diagnostics is promoted to a proof of the infinite limit.

## Originality — PASS, with residual priority risk

Biroli et al., arXiv:2211.00563, present individual stationary gap laws for simultaneous Poisson resetting. De Mauro et al., arXiv:2509.06658, Sections III–V, explicitly present the general renewal conditional-independent Gaussian mixture and individual spacing scaling functions, including Eqs. (124)–(132). The general stationary density is prior art and is not claimed as a discovery. Nagaraja, Bharath and Zhang, arXiv:1702.05910, provide classical independent extreme-spacing limits. The new classification instead concerns **cross-gap Pearson correlation for two distinct extreme ranks** and a **sharp universal optimal interval across all finite-second-moment renewal laws**, with equality cases and complete attainability. The cited single-gap formulas do not state the cross-gap moments or the global optimized envelope. The shared-mixture and extreme-value ingredients are credited; a broader unindexed treatment of reset-clock optimization could affect priority, and independent literature review remains desirable.

## Mathematical value — PASS

Extreme-particle spacings are physical measures of local crowding in a correlated resetting gas. A single-gap density does not quantify how fluctuations of two separated edge gaps co-vary. The result supplies a distribution-free **strict lower bound** of \(1/10\) on common-clock-induced asymptotic correlation, identifies periodic clocks as the unique minimizer, shows why arbitrarily heterogeneous clocks can nearly reach \(1/2\), and classifies the full attainable interval. The result distinguishes common resetting from independently reset particles in a measurable, shape-free way without manufacturing a downstream theorem.

## Closest literature and limitations

- Biroli, Larralde, Majumdar and Schehr, arXiv:2211.00563 (2022), individual Poisson-reset gap statistics.
- De Mauro, Biroli, Majumdar and Schehr, arXiv:2509.06658 (2025), general renewal-reset stationary Gaussian mixtures and individual gap distributions.
- Nagaraja, Bharath and Zhang, arXiv:1702.05910 (2017), independent-sample joint extreme spacings.

Unproved extensions: finite-particle sharp correlation bounds, bulk or growing ranks, clocks with infinite second moment, and snapshots locked to reset times. The general exact stationary joint position law existed previously. Independent assessment of publication priority and proof has not been conducted.

Self-review: passed. Independent audit: not yet performed.
