# Independent mathematical audit

## correctness

PASS

Coordinate rotations diagonalize a radial compression in the monomials; the eigenvalue on degree k is the stated beta quotient with N=k+d-1 and block dimension binom(k+d-1,d-1). With A=N+1 and a=-ic, the change of variable y=t/(1-t) gives exactly exp(ic) Gamma(A+alpha+1) U(A,-alpha,a)/Gamma(alpha+1) by the defining Laplace integral, first for Re(a)>0 and then by an Abel limit dominated by y^N(1+y)^(-N-alpha-2). Equations 13.8.11 and 10.40.2 of DLMF give a leading factor sqrt(pi) exp(a/2) a^((2alpha+1)/4) A^(-(2alpha+3)/4) exp(-2 sqrt(aA))/Gamma(A) for U. The complex arguments meet the sector hypotheses; A to N costs only a relative 1+o(1). The gamma normalization and exp(ic+a/2)=exp(ic/2) recover the claimed formula, including the phase and polynomial exponent. The frozen gamma-average derivation is consistent: on S in [N/2,2N], the normalized large-s integrand is bounded by a constant times exp(C|S-N|/sqrt(N)); the exact mgf gives uniform integrability. Off this interval, the bound |H_a(s)|<=Gamma(alpha+1) s^(-alpha-1) and gamma tails with shape shifted by alpha+1 give exponentially small unnormalized error, so they remain negligible after root-exponential normalization. The complex Gaussian correction is exp(a/2). Taking moduli gives -log|lambda_k|~sqrt(2|c| k), so eventual nonvanishing, all S_p, and the counting constant follow by summing degree-block dimensions between quadratic log thresholds; no monotonicity or distinctness of eigenvalues is required. The comparison with T_|phi|=I is exact. Independent finite replay: rotated-contour quadrature in /workspace/review_checks.py (chirp), at N=512,2048,8192 for three parameter pairs including both signs of c, gave final complex relative errors 0.00692, 0.01141 and 0.02047 or smaller; it supplements, not establishes, the asymptotic. Supplied script inspected, not executed.

## originality

FAIL

Verified broader prior coverage, not a false result or merely a title match. The entire fixed-phase spectral law is a direct specialization of the standard large-first-parameter Tricomi expansion after the elementary radial beta-moment substitution. Multiplicity and singular-value counting require only the standard monomial dimensions. The later signed Resultary record contains the exact disk moment calculation but is not the basis of the priority decision.

## value

FAIL

The unimodular example is illustrative, but the only candidate advance beyond the standard radial reduction is the fixed-parameter exact asymptotic and its consequences. The existing Tricomi expansion already supplies that entire asymptotic under an exact change of variable; block counting and Schatten membership are routine consequences. There is no surviving independent estimate, classification, or new boundary in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
