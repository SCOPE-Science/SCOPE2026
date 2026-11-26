# Independent mathematical audit

## correctness

PASS

Only the Brownian driver is reset. In the given units, W has a Gaussian mixture over its exponential reset age, hence all finite moments, and the stable filter Z=β∫ e^{-(s-u)}W_u du is stationary with the same moment property. A joint coupling erases W at the first shared reset and exponentially contracts the remaining Z difference; this gives uniqueness. Independent symbolic replay /workspace/energy_replay.py averages conditional Gaussian moments over the last-reset age, using the Poisson pre-reset Z law and conditional means (e^{-T}Z_old,0). It independently recovers the three displayed A,B,C, and verifies the exact critical formula by a matrix exponential. The centered generator equations for z²,zw,w² have diagonal −2,−(β+1),−β and superdiagonal 2β,β; centering removes the diffusion constant in L(w²). Exponential convolution gives the claimed H. All initial coefficients are positive and Φ_β≥Φ_(β+1)≥0, including s=0, so H is strictly positive at finite lags. The slowest mode has a nonzero positive leading coefficient on either side of β=2, including at β=1 where only a subleading resonance is possible. Substituting β=2+z/s gives Φ_β=s exp(−2s)(1−exp(−z))/z exactly, and Φ_(β+1)=O(exp(−2s)) uniformly on compact z-sets. This proves all three leading regimes and uniform crossover. The physical covariance is of X² with factor (D/μ)²; the covariance of μ X²/2 adds μ²/4. The frozen nested script and its logged checks were inspected, not executed.

## originality

PASS

Pass for the explicit stationary mixed-time quartic lag law with its sharp leading amplitudes and compact-uniform critical profile. Neither positivity alone nor the existence of a collision at r=2μ in this model is original in isolation. The closely related same-day four-time cumulant record directly gives positivity and an unevaluated harmonic-filter integral, but neither states nor immediately yields the evaluated kernel and its critical long-lag asymptotics. Its date does not resolve priority.

## value

PASS

The connected quadratic statistic supplies a finite-lag benchmark for energy-memory measurements in a non-Gaussian harmonic model. Its complete lag dependence and quantified near-critical crossover contain information not supplied by the linear correlation, equal-time moments, or a time integral. This is useful even though the rate mechanism itself is known for another observable and the sign is covered by the four-time theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
