# Independent mathematical audit

## correctness

PASS

Both count laws follow from independence of the latent Poisson streams: given male lifetimes the number is Bin(n,1−Y), Y=exp(−a sum T_i), while female search gives Bin(n,1−q), q=E exp(−naT). E[Y^n]=q^n proves the exact tie. For an independent strictness check, let H_k(s)=P(Bin(n,1−s^(1/n))≥k). Differentiating the binomial tail and cancelling adjacent terms gives H'_k(s)=−choose(n−1,k−1)[(1−s^(1/n))/s^(1/n)]^(k−1) on (0,1). H_1 is affine, and H_k is strictly convex on [0,1] for k≥2 by continuity and the strictly increasing derivative. Apply Jensen to Y^n; it is nonconstant when T is nonconstant, since the independent bounded positive factors Y_i=exp(−aT_i) satisfy E[Y_i²]>(E[Y_i])² and Var(product Y_i)>0. This also covers mass at T=0. Deterministic T and n=1 give the claimed equal laws. The tilted probability-mass ratio in the source also proves the result: positive moments are log-convex, R_0=1, R_1<1 by strict power-mean, normalization forces R_n>1, and either the upper sum contains only nonnegative terms with a strictly positive last term or its complement after zero contains only nonpositive terms with the strictly negative first term. The n=2 exponential example follows from E[Y]=1/4 and E[Y²]=1/9. The frozen script was inspected, not executed; it covers finite rational examples but contains no explicit exponential example despite the supporting review's description. The analytic review does not use that script. This is a count comparison only in the stated idealized Poisson system.

## originality

FAIL

The prior coverage is mathematical, not a duplicate insect title. Yu's Example 2 gives the exact stochastic-order criterion for a fixed binomial versus an arbitrary same-size binomial mixture, and also gives a stronger hazard-rate order. In the frozen model its criterion is the equality E[Y^n]=q^n. Strictness is a routine endpoint refinement of the same prior single-crossing proof (or a direct strict Jensen inequality). The sex-search interpretation is not claimed in Yu, but the frozen record does not identify a new stochastic law beyond the elementary Poisson reduction to this covered case.

## value

FAIL

The tie at any mating versus differences at higher thresholds is a clear illustrative interpretation, but the frozen finding applies an already available general zero-mass criterion once elementary conditional Poisson laws are written down. The exact strictness requires only the usual power-mean strictness or convexity of a binomial tail under the zero-mass coordinate. It does not establish an additional invariant, resolve the spatial trapping problem, or justify a new research result as distinct from a useful applied example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
