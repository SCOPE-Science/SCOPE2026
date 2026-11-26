# Independent mathematical audit

## correctness

PASS

The repaired RESULT.md states explicitly the conditional normal law already used in the frozen proof: knowledge of conditional mean and variance alone does not imply the mixture. For example, an equal conditional mixture of centered normals with variances dV(s) and 3dV(s) has the stated variance but a heavier far tail. The repair also fixes the Bayes version for every x≠0; densities and conditional versions at zero are not needed. Integration of the positive variance kernel gives as-ac plus the positive remainder H(2H-1) exp(-s/tau) times the integral of r(s+r)^(2H-2) exp(-r/tau) over r>0. Thus the rescaled phase is u+w+1/(uR_q), with R_q<=w and q times the difference from u+w+1/(uw) tending to lambda*c/(uw^2) uniformly on positive compacts. The latter comparison phase has a unique minimum 3 and Hessian [[2,1],[1,2]]. For localization, putting v=1/(uR_q) makes the singular amplitude factor R_q^(-1/2)=sqrt(u)sqrt(v). One unit of the exponent absorbs sqrt(v), leaving integrable gamma weights and the uniform phase gap off the saddle. The convergent local Gaussian integral has factor 2*pi/(q sqrt(3)); the Jacobian and likelihood give q^(alpha+k-1) sqrt(lambda)/(sqrt(4*pi*a*beta) Gamma(alpha) Gamma(k)). The finite intercept produces exp(-lambda*c), not an extra power of q. Normalization of the same localized density gives inverse Hessian covariance and limiting Gaussian correlation -1/2.

## originality

PASS

The Gaussian mixture, the exactly linear-variance product reference law, and its generic stretched exponent are prior. The repaired statement credits those results precisely. The specific shifted-variance contribution to the sharp fixed-time equivalent and the simultaneous latent Gaussian limit are supported as the distinct contribution, subject to the bounded comparisons below; a general transfer argument for exponentially shifted product factors is a particular residual priority risk for the marginal part alone.

## value

PASS

The repaired result identifies the eventual fixed-time tail of a specified transport model rather than treating the clock as deterministic. The difference in limit orders is substantive. A sharp multiplier quantifies finite correlation time, and the joint limit shows that both hidden variables move to the large scale with negatively correlated fluctuations. Neither is a consequence of reporting a stretched exponent alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
