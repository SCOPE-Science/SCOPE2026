# Independent mathematical audit

## correctness

PASS

With common Poisson clock the coordinates are conditionally independent centered Gaussians of shared variance V=2D integral exp(2gamma u)(1-s)^(2N_u)du. Verified the generator on v^p gives -Delta_p v^p+2Dp v^(p-1), and the surrogate gives -barDelta_p v^p+2Dp v^(p-1). The integrability iff positive criterion follows from Minkowski for sufficiency and truncated-generator stationarity plus positivity for necessity. Products  (2D)^p p! /prod_j Delta_j and Gaussian Wick factors give all even mixed moments. Independently checked s=1/2, lambda=D=1, gamma=1/3 gives E[V]=12/5, E[V^2]=1152/65, Cov=3888/325, with Gaussian barDelta_2<0. High-order cutoff z_c solves (1-e^(-2z_c))/(2z_c)=gamma/lambda; Gaussian cutoff 1-gamma/lambda. No finite simulation was promoted to an all-p proof.

## originality

FAIL

FAIL from exact theorem implication, not a lack of search. October 26 published full RESULT.md already proves the identical one-coordinate jump-diffusion and surrogate tail indices via psi_s(u)=gamma*u+(lambda/s)((1-s)^u-1) and psi_DA(u)=(gamma-lambda)u+lambda*s*u(u-1)/2. Its tail theorems give all absolute moment finiteness thresholds by substituting u=2p, since -psi_s(2p)=Delta_p and -psi_DA(2p)=barDelta_p. It also proves the identical finite true/infinite surrogate fourth-moment wedge and 1/s tail-index separation. Multiple coordinates share a clock and are conditionally Gaussian, an established construction in Galla; the joint-even-moment threshold and covariance are immediate Gaussian tensorization/normalization of known one-particle moments. The new product notation does not evade stronger coverage.

## value

FAIL

The Brownian-gas question is naturally motivated, but the final advertised moment-loss window, fourth-order counterexample and high-order cutoff are direct consequences of the earlier exact one-particle tail theorem. The joint moment products and square covariance follow mechanically from the same conditional Gaussian variance already in the literature. This does not constitute a separately needed, non-implied mathematical fact; correctness and explicit formulas alone cannot rescue intrinsic duplication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
