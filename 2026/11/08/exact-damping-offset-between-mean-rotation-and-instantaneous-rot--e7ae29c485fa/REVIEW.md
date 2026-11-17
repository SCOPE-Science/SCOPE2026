# Independent mathematical audit

## correctness

PASS

The 4x4 drift A is Hurwitz for a in (0,1), g>0, so the Lyapunov equation has one stationary Gaussian covariance. Independently calculated all 16 entries of A Sigma+Sigma A^T+Q=0 with the explicit Sigma; Isserlis gives Var(x v_y-y v_x)=Sigma_xx Sigma_vyvy+Sigma_yy Sigma_vxvx+2 z^2. The rational F(g) numerator is positive and denominator alpha*g^4+beta*g^2+gamma with alpha,beta,gamma>0. Its derivative has sign gamma-alpha*g^4, proving unique global optimum; g_mean=a maximizes ga/(g^2+a^2). The inequalities a^2 S^2<alpha<S^2 follow from HC>0, J>0, a<1 and prove sharp strict separation. Exact symbolic independent checker verified full covariance/variance/derivative/optimal substitution.

## originality

PASS

Martins et al derive stationary covariance and mean optimal damping for the same model; neither those ingredients nor long-time integrated-current variance of Bae et al are claimed new. The claim is single-snapshot angular momentum precision optimum and strict universal gap, a different observable from integrated current precision. Dutta–Saha 2026 ellipsoid study has a highly relevant mean/fluctuation and SNR optimization but is not the same fixed spherical/isotropic-friction 2D model in the inspectable abstract, and its exact full text could not be obtained; no accessible statement of the identical g_precision or sharp temperature inequality was found. Best-of-knowledge PASS with serious unresolved priority risk, not a certificate of historical novelty.

## value

PASS

Optimizing instantaneous rotation detection and mean rotation at different damping rates gives a natural physical measurement design distinction and a sharp closed-form threshold and bound. Objective, normalization, Gaussian covariance and exact strict domain are specified; not merely optimizing an already known mean or a time-integrated current.

The dated certificate retains the supplied scientific assessment, sources and limitations.
