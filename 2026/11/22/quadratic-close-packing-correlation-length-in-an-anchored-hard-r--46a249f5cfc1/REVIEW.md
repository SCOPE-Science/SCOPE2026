# Independent mathematical audit

## correctness

PASS

With ε=d/δ, the Jacobian δ and the gauge e^(−x/ε) on [0,1] give K similar to ed times the interval-killed ε(Exp(1)−1) transition. For fixed ε, midpoint step kernels converge in Hilbert–Schmidt norm by bounded convergence away from the jump line. Their matrices are totally nonnegative (a square Ferrers minor is zero unless the nested rows give triangular pivots), so their eigenvalues are real and nonnegative, and norm convergence of the spectral projections transfers this to each isolated nonzero point. Nonzero eigenfunctions are bounded by the kernel, and the probability of a jump beyond the upper endpoint is at least exp(−1−1/ε), giving eigenvalues strictly below one. The gamma return density tends to (2πt)^−1/2. Given zero endpoint displacement, exponential increments have the normalized iid exponential-spacing law; writing S_k for fresh iid exponential partial sums, the bridge has positions ε(m S_k/S_m−k). Donsker and S_m/m→1 give the Brownian bridge; its extrema have no atoms at the killing thresholds for interior starting points. The trace-class identity for products of Hilbert–Schmidt kernels gives the integral of the cyclic return kernel, dominated by the free gamma density, and Lidskii gives the sum of powers with algebraic multiplicity. For the log-rescaled spectra the floor and ceiling powers squeeze their Laplace transforms (or use trace limits at t±η and send η to zero); the tail beyond R at t is bounded by e^(−tR/2) times the transform at t/2. Vague convergence and Laplace uniqueness identify the first two isolated single atoms π²/2 and 2π², proving positivity near packing, the log-gap constant, and the free-energy term. Separately, /workspace/review_checks/rods.py reconstructs the reciprocal polynomial via ν f′(x)=−f(x−ε), initial flatness and νf(0)=∫f. Exact integer sign variations isolate its first two roots at five integer δ/d values. At δ/d=80 the scaled log exponents are 4.774725665782 and 19.10363383013 and ξ/(δ/d)²≈0.0697889880 (ξ≈446.65). This checks the same model and contradicts the primary paper's asserted ξ<n even allowing either interval index at the integer boundary; continuity gives nearby interior examples. The finite computations do not establish the limit.

## originality

PASS

Credit the identical model, exact finite-ε spectrum and definition of ξ to Mizani et al. The distinct result is the controlled two-root close-packing asymptotic, including its sharp constants and the correction to the conflicting contact-count bound. Exact parameter-dependent polynomials do not supply this limit without new analysis as their degree diverges.

## value

PASS

The subleading eigenvalue sets a natural equilibrium length not determined by the pressure or the one-well profile. The sharp gap reveals that long-range correlation extends parametrically beyond the contact count and corrects a concrete prior assertion for the same model. The two-mode mechanism and free-energy term are usable quantitative predictions, not extrapolated mesh estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
