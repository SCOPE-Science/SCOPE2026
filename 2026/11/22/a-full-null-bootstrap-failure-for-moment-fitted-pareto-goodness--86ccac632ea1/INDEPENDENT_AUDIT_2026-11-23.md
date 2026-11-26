# Independent mathematical audit

## correctness

PASS

Truncated strong laws on a countable set of truncation levels force the observed sample mean to diverge, so the fitted shape converges to 1 from above. The fitted CDF varies uniformly near 1 (its shape derivative is bounded by sup over x≥1 of x^(-1/2)log x on a neighborhood of 1). Glivenko–Cantelli gives the uniform observed discrepancy limit; maximizing x^(-β)-x^(-1) gives x*=β^(-1/(1−β)) and dβ as stated. The CvM integrand converges uniformly to the square of a bounded continuous function, so one can also pass to the weak limit of the fitted integration measure. The substitution u=1/x gives cβ=2(1−β)^2/[3(β+2)(2β+1)], as obtained from the three displayed fractions. Conditional on almost every data path, each bootstrap row has its own fitted shape. For any fixed K, choose a common finite L with the truncated mean at shape 1 greater than 2K; continuity gives mean >3K/2 along the row sequence eventually. Bounded concentration gives row-average truncations >K with probability tending to one, without any triangular-array untruncated LLN. Thus the bootstrap refit also converges to 1, and distribution-free DKW shows D*n→0 in conditional probability and W*n/n≤(D*n)^2→0. Nonnegativity and any fixed upper quantile level strictly between 0 and 1 imply the quantile limits, hence eventual rejection almost surely on those paths. This verifies the stated known endpoint, fixed subunit shape, and ideal conditional refitting only. Independently checked d(1/2)=1/4 and c(1/2)=1/30 exactly; a bounded illustration sampled X=(1−U)^(-2) with 24 independently refitted bootstrap replicates per n using U uniform. At n=4000 and 50000 the observed (KS,CvM/n) were (0.262197,0.034498) and (0.248342,0.033061), against empirical .95 bootstrap pairs (0.059398,0.001488) and (0.040694,0.000834). Replay with NumPy default_rng(5015), sorted fitted CDF values u_i, one-sided KS jump-end formulas, and CvM/n=mean((u_i−(i−1/2)/n)^2)+1/(12n²). The uploaded checker was read, not run; its shape grid and special-case tolerances are floating-point and its simulated statistic is KS only. Those observations do not affect the exact theorem.

## originality

PASS

Qualified pass for the exact fixed-shape separation and asymptotic size-one theorem under ideal conditional refitting, not for identifying the moment-existence restriction or the possibility of distortion.

## value

PASS

For genuine heavy-tail null data, nominal calibration can fail as badly as possible even when every repetition refits. The two distinct exact EDF gaps and the conditional control distinguish this diagnostic from a generic warning about infinite means and specify which fitting workflow to avoid. It does not diagnose MLE, Fourier tests or boundary shape 1.

The dated certificate retains the supplied scientific assessment, sources and limitations.
