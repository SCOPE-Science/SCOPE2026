# Independent mathematical audit

## correctness

PASS

For the deterministic one-point design, the Beta(n,1) weight is in the target, not in the sampling law. The bridge Green equation −C_n''=nt^{n−1} with zero boundary values gives C_n=t(1−t^n)/(n+1); integrating against nt^{n−1} gives V_n=n²/[(n+1)²(2n+1)]. Gaussian projection gives risk V_n−C_n²/[t(1−t)+η] with zero reduction at endpoints. Differentiating the reduction on (0,1) gives the sign of the stated F. For η>0 there are at most two Descartes sign changes, including after combining powers at n=1; F(0)>0, F(1)<0 and the positive leading term force one simple interior root and one root above 1. At zero noise, F/t has at most two positive roots, the simple root 1 and a sign-changing root below it. Thus the interior root is the unique global maximum. At n=1 it is identically 1/2. For n>1, r_n=(n+1)^(−1/n)>1/2 and F(r_n)=r_n n(2r_n−1)/(n+1)>0, so t_n>r_n. At the optimizer F_η<0 and F_t<0, giving strict leftward motion. The bound t_n>r_n gives u_n=n(1−t_n)=O(log n). In the balance identity on lines 55–59, bounded nη_n implies t_n^n≥a/(1+u_n) for a fixed a>0; t_n^n≤exp(−u_n) then forces u_n bounded. In the noiseless case u_n→0 along a subsequence would give explained fraction at most (2+1/n)u_n there, using 1−t_n^n≤n(1−t_n), but the trial t=1−c/n gives positive limiting gain. Noise monotonicity excludes the small branch for scaled noise and identifies the limit u_α on [c,∞). For fixed positive noise the same balance gives t_n^n∼(1+2η)/(2ηn); n log t_n=−u_n+O((log n)²/n) gives the additive logarithmic shift. Substitution into the exact explained fraction yields all three risk limits.

## originality

PASS

The inspected literature and indexed designs do not give or imply this finite optimizer and risk together with the high-order noise crossover for the normalized Beta-weighted scalar bridge integral. Gaussian conditioning and bridge covariance are standard ingredients; they are not the distinct claim.

## value

PASS

The normalized Beta family is a natural sequence of positive weights concentrating near a pinned endpoint. The exact Bayes design distinguishes zero noise, noise comparable to order-reciprocal, and fixed positive noise: the best location moves from 1−O(1/n) with a positive limiting explained fraction to a log-over-order layer with asymptotically vanishing explained fraction. The finite unique optimizer and noise ordering make the singular comparison usable when placing a single sensor, and the explicit crossover constant gives more than a generic error bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
