# Review: sharp resetting fingerprints in collective energy tails

## Correctness — PASS

The result is restricted to independent one-dimensional Ornstein–Uhlenbeck particles with one common Poisson reset clock, fixed \(r,\mu,D>0\), and the stationary empirical squared-position observable. Its exact beta–chi-square representation is reconstructed directly from the exponential backward reset age and the Gaussian OU transition law. The critical-window theorem follows from the chi-square central limit theorem with a Chernoff-dominated endpoint integral; the exact threshold coefficient is evaluated by Tonelli's theorem and a Gaussian moment. The fixed supercritical theorem follows from Stirling's formula for gamma tails and an endpoint Laplace calculation, yielding the full \(N^{-b-1/2}\) prefactor. The standalone verifier passed 105 finite numerical and algebraic checks from the supplied source file. Finite checks are supporting evidence only; the universal claims rest on the analytical argument.

## Originality — PASS, with residual priority risk

The closest model paper is de Mauro–Majumdar–Schehr (2026), arXiv:2606.31634v1. Its stationary joint distribution, OU propagator, density and positional extreme-value analysis provide the starting point and are not claimed as new. Biroli–Larralde–Majumdar–Schehr (2023), arXiv:2307.15351, proves a broad conditional-iid bulk sum law that subsumes the bulk Beta limit for the energy; this covered limit is not part of the accepted originality claim. The precise equilibrium-energy crossover of width \(N^{-1/2}\), its \(N^{-b/2}\) amplitude and integral, and the full supercritical exponential-times-power tail were not located in the inspected relevant sections or in closest available research records. Equivalent product-mixture and endpoint-Laplace descriptions were searched by implication rather than by title alone. A prior generic theorem for moving-threshold conditional-iid sums, or an uninspected appendix, might imply some or all of these asymptotics; complete publication priority remains unestablished. Relevant 2025 non-Poissonian resetting and 2023 switching-trap papers concern different models or observables.

## Value — PASS

The normalized sum of squared displacements is a natural collective energy/extent observable, complementary to positional maxima and pair correlations. Its equilibrium-energy threshold separates typical reset-clock fluctuations from exponentially rare over-equilibrium excursions. The derived sharp law identifies a physical resetting-rate fingerprint visible in the *polynomial* large-deviation factor even when the exponential rate is insensitive to resetting, and gives a finite-size critical crossover with explicit, independently checkable coefficients. This is a motivated structural distinction for an exactly specified statistical-mechanical observable, rather than an arbitrary finite table or a restatement of the prior joint distribution.

## Closest literature and limitations

- G. de Mauro, S. N. Majumdar, G. Schehr (2026), arXiv:2606.31634v1: exact stationary common-reset harmonic gas; prior input to the proof.
- M. Biroli, H. Larralde, S. N. Majumdar, G. Schehr (2023), arXiv:2307.15351: generic conditional-iid sum law already covers the bulk limit.
- G. de Mauro, M. Biroli, S. N. Majumdar, G. Schehr (2025), arXiv:2509.06658: non-Poissonian common resets and positional statistics.
- M. Biroli, M. Kulkarni, S. N. Majumdar, G. Schehr (2023), arXiv:2312.02570: switching harmonic stiffness rather than hard reset to the origin.

The proof does not provide an all-threshold uniform asymptotic matching theorem, a nonharmonic extension, or independent mathematical certification. Relevant primary-paper sections were inspected, but complete appendix coverage and a definitive priority search remain incomplete.

Self-review: passed. Independent audit: not yet performed.
