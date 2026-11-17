# Independent mathematical audit

## correctness

PASS

For both zero-velocity and rethermalizing position+velocity resets, exact free-segment covariance A_j(t)=2*kappa*(t-d_j)+O(exp(-gamma*t)), B_j(t)=kappa+O(exp(-gamma*t)), C_j(t)=Dv/gamma+O(exp(-gamma*t)); d0=3/(2gamma), dM=1/gamma. The stationary joint law is an exponential-age mixture of bivariate Gaussians. Conditional on X=x, replacing t by u+d_j gives an exponentially accurate kernel u^-1/2 exp[-r u-x^2/(4*kappa*u)]. Its integral sqrt(pi/r) exp[-x sqrt(r/kappa)] yields conditional mean age x/(2sqrt(kappa*r))+d_j+1/(2r), variance x/(4sqrt(kappa)r^1.5)+1/(2r^2), and Gaussian CLT. Conditional Gaussian regression gives velocity mean sqrt(kappa*r), variance Dv/gamma, asymptotic independence. The Laplace spatial tail yields an independent exponential overshoot for X>R. Independently numerically integrated the key inverse-Gaussian normalization at x=100 (relative discrepancy 1.6e-14). Analytic Laplace concentration, not finite quadrature, proves joint weak limits.

## originality

PASS

Franke–Sokolov 2026 (same two reset prescriptions) establishes their marginal exponential-position tail and core singularity; full primary text was accessed and its scope checked. Montero–Palassini–Masoliver derive the general stationary inertial joint-mixture and level-crossing intensity, not the fixed-reset-rate extreme-position conditional law and O(1) age difference in inspected text. Neighboring Resultary random-acceleration model has correlated age/velocity in a different dynamics.

## value

PASS

Conditioning on extreme stationary displacement reveals a hidden velocity-selection law and a protocol-identifying O(1) age delay invisible in leading spatial tail or CLT. The distinction from crossing-time velocity weighting is important and mathematically motivated by rare-event sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
