# Independent mathematical audit

## correctness

PASS

For A=diag(a,b), a>b>0, real Gaussian g, the rank-one Nyström matrix has nonzero eigenvalue mu=(a^2+b^2T)/(a+bT), T=g2^2/g1^2 with square-Cauchy CDF. The logarithmic function-after-Nyström excess H=log((1+a)(a+bT)/(a(1+a)+b(1+b)T)) is strictly increasing in T and inverts to the exact displayed CDF; no finite endpoint atom. The angular mean-log identity gives E H=2log[(sqrt a+sqrt b)/(sqrt a+sqrt(b(1+b)/(1+a)))]. Direct Nyström applied to log(I+A) gives error E_D=L_a L_b(1+T)/(L_a+L_b T) and expected value sqrt(L_a L_b), L_i=log(1+eigenvalue). Holding b fixed and coupling same g across a→infinity yields aH→bT a.s., sqrt(a) E H→2sqrt b, E_D→L_b(1+T) a.s., E E_D~sqrt(L_b log a) while the limiting law has a nonintegrable y^-1/2 tail. Independent angular quadrature and exact scalar comparisons validate sample spectra only; proofs are analytic.

## originality

PASS

PASS qualified. Persson and Kressner establish the function-after-Nyström method and expected bounds with oversampling assumptions, but not its exact one-column 2x2 log-trace error CDF and two contrasting high-spike mean/quantile scales. A prior Resultary 2026-10-13 sharp power-function funNyström theorem analyzes f(x)=x^theta and power iteration, not the logarithm, and does not logically imply this CDF. Other Gaussian Nyström matrix power and preconditioner results have distinct estimators. The direct log-matrix Nyström comparator mean sqrt(L_aL_b) is known rank-one residual algebra, explicitly not counted separately as new. Unindexed specialized log-Nyström work remains a risk.

## value

PASS

The one-column unoversampled model is the smallest natural stress test for the actual matrix-function-after-Nyström trace estimator, precisely where generic oversampled bounds do not apply. Its complete error law, quantile-vs-mean asymptotic separation and fair same-random-direction (but not same-cost) direct-function contrast provide an exact diagnostic for nonuniform integrability and spectral-spike risk. This is a motivated exact natural benchmark, not an optimal large-matrix estimator claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
