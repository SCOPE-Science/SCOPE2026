# Scientific review of the zero-initialized Ornstein–Uhlenbeck single-sensor theorem

## Correctness — PASS

The Gaussian conditioning criterion follows directly from a single-observation covariance update. The closed-form squared-covariance integral is independently differentiated and integrated. The key identity for \(G_a''+2aG_a'\) gives exactly one change of sign, hence a one-dimensional monotone inverse for the optimality condition. The derivative signs cover both ends of the design interval and prove uniqueness globally. The stated high-noise expansion and zero-reversion limit follow from Taylor expansion and the same stationarity condition. Symbolic and numerical checks in `verify.py` support, but do not replace, the proof.

## Originality — PASS, qualified

The 2016 full text of Ji and Müller treats the general Gaussian integrated-variance design criterion, without the exact one-site zero-initialized OU theorem. The 2013 full text of Baran, Sikolya and Stehlík is for stationary OU sheets on monotone sets, and the 2018 full text of Sikolya and Baran covers stationary complex OU Kriging. Published records inspected for optimal noisy OU observation placement did not show this same theorem or a stronger result that implies it. The 2010 exact Kriging designs paper concerns stationary exponential covariance and was inspectable only through its abstract and references, so an equivalent undocumented specialization remains a publication-priority risk. Search absence alone was not taken as a proof of novelty.

## Value — PASS

The theorem resolves the complete one-measurement trajectory-recovery design for the zero-start OU family, identifies strict noise monotonicity, and exposes a qualitative singular limit: a finite high-noise interior time for every positive reversion rate, versus terminal approach under Brownian covariance. The decisive identity offers a reusable analytical method for related Gaussian design kernels. This is a motivated exact design classification, not a fixed-parameter arithmetic example.

Independent proof review and publication-priority verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
