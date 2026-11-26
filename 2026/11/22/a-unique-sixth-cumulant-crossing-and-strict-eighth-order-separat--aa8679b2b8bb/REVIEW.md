# Independent mathematical audit

## correctness

PASS

Both invariant laws give mean m and centered variance 2m^2. Their centered diffusivities f are stationary reversible Markov observables with conditional decay exp(-q lag); for OU this is the second Hermite eigenfunction. Thus the covariance is the stated exponential. At ordered triples, conditioning the two ends on the middle (using reversibility for the left end) gives exp(-q times the full span) E[f^3]. The skew moments are 8m^3 for squared OU and 2m^3 times (2/u-u) for the binary law. The ordered integral is 6J_q(t)>0 for t>0; the Gaussian-mixture conversion factor 6!/3!=120 gives the two stated sixth cumulants. Matching skew selects the unique u=sqrt(6)-2 in (0,1), since 2/u-u is strictly decreasing there. Conditional Gaussian Wick pairings depend on at most three integrated diffusivities through tracer total degree six (at most two through degree four); odd total degrees vanish. Matching diffusivity joint moments, not merely single-time cumulants, therefore proves the claimed multi-time equalities. Independently, for ordered gaps a,b,c the raw centered four-point moment equals exp(-q(a+c)) E[f_0^2 f_b^2]. For squared OU, f^2=2m^2+4mf+H_4(Y), with H_4(y)=y^4-6my^2+3m^2, variance 24m^4, orthogonal to f and decaying at 2q. For the two-state law, f^2=2m^2+m(2/u-u)f with no residual. At the matching u, raw four-point differences thus equal 24m^4 exp(-q(a+2b+c)); the covariance-pair corrections cancel. Integrating over all 24 orderings gives the strictly positive time-window difference. The dimensionless transform of H is 24/[s^2(s+1)^2(s+2)], independently checked symbolically along with H=z^4-4z^5/5+O(z^6). Scaling q and multiplying the integrated gap by 8!/4!=1680 gives the stated coefficient and dimensions. The rank-two joint covariance integration likewise gives the stated fourth cumulant. Conditioning is valid because the tracer noise is independent; the OU integrated-diffusivity MGF exists near zero by Jensen and the one-time Gaussian-square MGF (the two-state one is bounded on each finite window). The supplied generator-hierarchy code was inspected, not executed.

## originality

PASS

Best of current knowledge: the exact cross-mechanism moment-matching boundary and uniform positive eighth-order gap are distinct. Exact forward transforms and two-state single-time cumulants are credited as prior coverage, as are generic Gaussian-mixture and Markov tools. The comparative classification is not a new individual forward formula, a treatment of all diffusing diffusivities, or a priority certification.

## value

PASS

Mean and covariance matching alone often obstruct identification of random environments. Here even all multi-time statistics of polynomial degree at most six fail to distinguish two qualitatively different stationary mechanisms at a unique parameter, while one eighth cumulant succeeds at every positive window. The time-uniform sign and explicit residual mode show why the separation holds and identify the first distinguishing even order. This is a motivated identifiability boundary, not just a numerical comparison of forward moments or a promise of robust estimation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
