# Independent mathematical audit

## correctness

PASS

The sketched regression residual v=(G^TG)^-1G^Tw has a bivariate rotational t-law density (s-1)/(2pi)(1+|v|^2)^(-(s+1)/2), obtained from the Gaussian/Wishart mixture. Direct discriminant reduction gives Delta=delta^2-2sqrt(2)delta*t*b+2t^2u^2, so nonreal iff b>h+u^2/(4h) with h=delta/(2sqrt(2)t)>0. Polar integration of this parabola yields exactly the displayed 1D angular integral. A two-scale Laplace expansion u~s^-1/2 and b-h~s^-1 provides q/(h sqrt(3pi s)) q^(-s/2), with an integrable majorant. Independently evaluated the angular integral for s=3,8,40,160,640; p_3=0.19245008973 and asymptotic leading ratios approach one (0.8399 at 40, 0.9855 at 640). The deterministic SPD 3x3 witness gives discriminant -3 and open positive-probability nonreal region. The source code independently checks thousands of exact rational discriminants; finite Monte Carlo supports, not proves, the analytic probability.

## originality

PASS

Prior sketched Rayleigh–Ritz papers explicitly document qualitative nonreal Ritz pairs and introduce real-Schur processing, but do not produce the present exact fixed-matrix Gaussian nonreal-pair probability or sharp prefactor as sketch dimension grows. The closest published sharp one-quarter result assumes uniformly oriented *fixed-length* couplings, not Gaussian regression; the 2-row sharp bound concerns minimal s=2; the four-dimensional critical-gap law concerns shrinking or repeated Ritz gaps, rather than fixed delta>0. General Gaussian regression law is classical but does not itself evaluate this nonreal parabola and asymptotic. This is a narrowly motivated nonstandard exact risk law, with unindexed probability identity a residual originality risk.

## value

PASS

The inability of a symmetric original matrix to guarantee real sketched Ritz eigenvalues is a concrete numerical-stability issue. The exact Gaussian failure probability and sharp fixed-gap oversampling prefactor quantify the risk even for genuine dimension-reducing sketches; the reduction to a minimal SPD 3x3 coupled example is structurally motivated rather than arbitrary sampling. This is an exact, self-contained quantitative finding, not a global eigensolver guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
