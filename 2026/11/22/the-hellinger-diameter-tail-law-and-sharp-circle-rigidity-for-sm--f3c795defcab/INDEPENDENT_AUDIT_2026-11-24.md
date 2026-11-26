# Independent mathematical audit

## correctness

PASS

The support equation gives opposing contact points with difference w times the common normal. A chord of length w saturates the support inequality in its direction, so it is one of these pairs. Compactness excludes all pairs outside a fixed neighborhood of the maximizing circle for sufficiently small deficits. The support parametrization has derivative rho times the unit tangent. In the transverse coordinate u about the opposite normal, the squared chord length is w^2-rho*rho_pi*u^2+O_K(|u|^3), with the coefficient bounded below at fixed K. The allowed interval has width 2 sqrt(2w epsilon/(rho*rho_pi))+O_K(epsilon). The independent arclength sampling density is rho*rho_pi/(pi w)^2 at u=0 because ds=rho dtheta and the integrated antipodal sum gives perimeter pi w. Multiplying and integrating gives precisely (2 sqrt(2)/pi) A sqrt(epsilon/w), with the claimed fixed-body error. Normalization gives 1-A=H^2; Cauchy–Schwarz gives the stated TV lower bound and equality in the affinity bound forces rho=w/2, hence a translated disk. The prescribed tanh radius has no first harmonics by threefold symmetry and solves the support equation, with positivity ensuring genuine supporting contacts and antipodal sum ensuring width. Dominated convergence at lambda=1 as M grows gives infimum zero; continuity at each sufficiently large fixed M gives every intermediate value with lambda<1. The single harmonic reduces to the complete elliptic integral stated. Independent numerical replay `python3 /workspace/checks/oval.py` checks the exact disk normalization, a fifth-harmonic example and a steep tanh example (affinity about 0.26446), by integrating chord components and solving finite-deficit equations. These are bounded corroborations, not proof of the remainder or sharp range; no uniform claim over degenerating bodies is made.

## originality

PASS

The supported distinct result is the variable-curvature coefficient for fixed smooth constant-width bodies with independent arclength endpoints, including disk rigidity and the full sharp range. The circle tail, elementary Hellinger inequalities and the general transverse-sublevel mechanism are not new by themselves. Available explicit prior comparisons do not give the stated coefficient and range for noncircular constant-width bodies.

## value

PASS

The result gives a natural sampling statistic distinguishing the disk among shapes of a common width and perimeter, with an information-geometric expression for its exact deficit. The full-range construction demonstrates how far this statistic can move from the disk under smooth positive curvature, rather than merely providing another asymptotic computation for the circle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
