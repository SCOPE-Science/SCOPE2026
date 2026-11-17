# Independent mathematical audit

## correctness

PASS

For a nearest-neighbor CT walk with absorption at zero, reflecting endpoint N suppressing attempted outward jumps, and independent rates redrawn each physical tau, the finite killed generator A_N has eigenvalues 1-cos(theta_m), theta_m=(2m+1)pi/(2N+1). Averaging the rate Laplace transform yields G(t)=(I+(t A_N)^alpha)^(-1). Renewal across refresh intervals gives h=(I-G(tau))^(-1)int_0^tau G(t)dt 1=F(A_N)1, with F(s)=tau^(1-alpha)s^(-alpha)+tau int_0^1[(1-u^alpha)/(1+(tau s)^alpha u^alpha)]du. Subordination makes the remainder nonnegative and <=tau alpha/(1+alpha). Eigenvector sine coefficients are exactly 2/(2N+1)sin(j theta_m)cot(theta_m/2). Independently diagonalized actual A_N for N=1,2,3,5,11 against explicit sine eigenpairs, and checked limiting alpha=1 leads to 2jN. The low-frequency singular summation yields finite alpha<1/2, (2sqrt(2tau)j/pi)log N at alpha=1/2, and the stated odd-zeta amplitude N^(2alpha-1) for alpha>1/2. Uniform near-half exponent alpha=1/2+u/logN yields the (exp(2u)-1)/(2u) scaling factor, with bounded physical-time correction. Finite numerics are corroborative only.

## originality

PASS

Best-of-knowledge: the half-line threshold alpha=1/2 under periodically refreshed heavy-tailed rates is from Levit–Reuveni, and the doubly stochastic walk spectral/renewal method is from Arutkin–Reuveni. The inspected published comparisons concern infinite half-line first passage or two absorbing finite endpoints with a different rate family. They do not state this exact finite mixed absorbing/suppressed-reflecting generator, all-site physical-time mean, uniformly bounded renewal correction, sharp three-regime finite-volume amplitudes, or logarithmic alpha=1/2+u/logN crossover.

## value

PASS

A finite absorbing/reflecting observation domain is a natural regularization of a known infinite-mean first-passage transition. Its sharp crossover, including physical-time correction and exact critical logarithmic amplitude, supplies quantities needed for finite experiments and boundary-sensitive stochastic models; the all-N spectral formula and uniform window are nontrivial and not mechanically implied by the half-line threshold alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
