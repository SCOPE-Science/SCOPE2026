# Independent mathematical audit

## correctness

PASS

Conditioned on K=N_x, uniform past arrival times and independent future increments give E[J|K]=(1-x/2)K+lambda(1-x)^2/2; the Poisson area variance is lambda/3. For any two count reconstruction levels, replacing the bit by pointwise nearer-level assignment and then re-centering cannot increase squared error. Nondegenerate cells can therefore be represented by an integer cutoff; the h=1 score is positive for x>0, so a constant bit cannot maximize there. The Poisson shift gives Cov(K,1_{K>=h})=m p_{h-1}(m) and division by the Bernoulli variance gives the exact score. Cauchy–Schwarz and monotone coupling with Pois(L) give uniform vanishing tails over m in [0,L]; each score extends continuously at zero by the explained-variance bound m. This proves attainment by compactness. For standardized counts, CLT and matching second moments give W2 convergence, and Minkowski's inequality for distances to two reconstruction points passes optimal distortion to the limit. The normal score is uniquely maximized at zero by the strict cosh-integral comparison. Uniformly integrable standardized squares (bounded fourth moments for m>=1) exclude diverging optimal cutoffs; every bounded converging subsequence has by weak convergence and uniform integrability the threshold score at its limit, forcing limit zero. The per-lambda objective converges uniformly away from zero, and is at most delta on x<=delta after division by lambda. Hence every maximizing time converges to the unique maximum of x(1-x/2)^2 at 2/3, and the limiting explained fraction is 3*(2/pi)*(8/27)=16/(9*pi). The boundaries, fixed h=1 contrast, and full-count benchmark follow from the same formulas. The historical 1,182 finite checks are reported evidence only; verify.py was inspected, not executed.

## originality

PASS

The supported distinct claim is the deterministic all-encoder reduction and sharp joint high-rate optimizer law for the Poisson area. Neither the classical normal constant nor general nearest-level encoding/quantizer stability is credited as new.

## value

PASS

The exact objective removes the need to search arbitrary count encoders, and the sharp asymptotic benchmark distinguishes a cutoff that tracks the count mean from a saturated presence bit. It determines both where to observe and what to transmit, with a nonzero sharp risk improvement under the stated one-bit constraint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
