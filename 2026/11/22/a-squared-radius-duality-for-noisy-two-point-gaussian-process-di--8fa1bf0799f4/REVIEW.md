# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 35–78. The two normalized kernels have k''(0)=-1, and the derivative cross-covariance with the observations is (g,-g), g=-k'(h). Diagonalizing the observation covariance gives R=1-2g²/[c-k(2h)] with c=1+η. For z=h² (Gaussian) or z=h (Matérn), divide E'=d(1-R)/dz by the positive factors 2e^(-3z)/(c-e^(-2z))² and 4ze^(-4z)/(c-(1+2z)e^(-2z))², respectively: the remaining factor in both cases is c(1-z)e^(2z)-(1+z). It is negative at and past z=1; below 1 the log derivative of F=(1+z)e^(-2z)/(1-z) is 2z²/(1-z²), giving one global maximum t with F(t)=c. Substitution gives E_M=1-t and E_G=(1-t)e^t; the latter decreases strictly from 1 as t increases, so 0<R_G<R_M. The series log F=2t³/3+O(t⁵) gives the claimed low-noise powers, and (1-t)F(t)→2e^(-2) gives the high-noise endpoint. This proves the identity only for the stated symmetric, equally noisy sites and kernel normalization. VERIFICATION.md and the two scripts were inspected, not executed; their symbolic and finite numerical checks are supplementary.

## originality

PASS

The supported addition is the shared global design optimizer and resulting cross-kernel radii and risk laws, not Gaussian conditioning or noisy gradient sampling in general. No equivalent or dominating result was established by the inspected sources.

## value

PASS

The optimal radius is a design quantity one needs before collecting the two observations. The coincidence for all relative noise levels and the different low-noise exponents (1/3 versus 1/6 for spacing) are specific, nontrivial information about two standard priors; generic regression does not give it. Exact optimal risks quantify the consequence without suggesting estimator dominance on a common law or optimality among nonsymmetric designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
