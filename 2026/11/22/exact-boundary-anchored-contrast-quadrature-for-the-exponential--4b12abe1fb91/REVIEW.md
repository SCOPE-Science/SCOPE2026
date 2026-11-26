# Independent mathematical audit

## correctness

PASS

Direct integration gives m(t)=ell(2-exp(-t/ell)-exp(-(1-t)/ell)); scalar Gaussian conditioning gives explained variance (m(v)-m(u))^2/[2(1-exp(-(v-u)/ell))+eta]. For fixed gap the covariance difference is strictly decreasing in the left location and antisymmetric under reflection, so the only maximizers are the boundary pairs. Their covariance magnitude C(d)=ell(1-exp(-d/ell))(1-exp(-(1-d)/ell)) is unchanged by d→1-d whereas contrast variance strictly increases with d. The full-span observation has zero covariance even at eta=0. In r=exp(-d/ell) the derivative of log gain is -2F_eta(r), with F_eta as stated; F_eta is strictly increasing, is negative at sqrt(q), and tends to +infinity at 1. This proves uniqueness, the cubic, and exclusion of the midpoint and the positive-gap limit d→0. The eta derivative of F_eta is positive, hence the gap grows strictly with noise; at zero noise the equation reduces to r^2+qr-2q=0. At large noise the smooth stationary equation 2C'/C=V'/V about d=1/2 and 1/eta=0 gives half-gap displacement C(1/2)/(2eta)+O_ell(eta^-2). For h=1/ell, factor 1-exp(-hd)=hd A_h(d), where A_h(d)=1+O(h) uniformly including d=0 by continuous extension. Then h^-1 times the reduced gain converges uniformly on [0,1/2] to d^2(1-d)^2/(2d+kappa), extended by zero at d=0 even for kappa=0. Its interior maximizer, the positive root of d-3d^2+kappa(1-2d)=0, is unique and simple; the smooth stationary equation near it also gives d*=D(kappa)+O_kappa(h). This verifies the crossover and the stated variance expansion, with coefficient 2/27 when kappa=0. Independent high-precision bisection on the derivative in gap coordinates agrees with the two examples (0.366256978874186 and 0.453518650447919) and sampled scaling limits; replay with Python and mpmath: /workspace/branches/independent_contrast.py. The calculation is supplementary to the continuous proof.

## originality

PASS

The exact constrained location theorem and its two quantitative noise limits survive the inspected comparisons. Gaussian conditional covariance, general kernel discrepancy, and distinct noisy two-point or derivative observation models are prior tools or problems, not new here.

## value

PASS

The observation model addresses genuine relative sensing, where absolute readings are unavailable. The theorem rules out the endpoint-to-endpoint contrast despite its maximal gap, and gives a usable exact site law for all correlation lengths and noise levels. The explicit transition from one third to one half and the explained-variance scaling distinguish when relative sensing is informative under long correlation. It is limited to the specified prior and one absolute-noise scalar contrast.

The dated certificate retains the supplied scientific assessment, sources and limitations.
