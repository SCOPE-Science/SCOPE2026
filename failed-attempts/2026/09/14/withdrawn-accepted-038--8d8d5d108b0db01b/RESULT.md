# Precise obstruction to the Eisenstein specialization of Jana's GL(n) x GL(n) second moment (n >= 3)

## Context
For fixed n >= 3, let F_X^gen be generic automorphic representations of PGL_n(Z) with analytic conductor C(pi) < X. The target asks for the random-matrix-predicted sharp asymptotic, including leading arithmetic constant and full log-polynomial, for S(X) = sum_{C(pi)<X} |L(1/2,pi)|^{2n}/L(1,pi,Ad), in particular the sharp Lindelof-on-average bound, equivalently extending Jana's GL(n) x GL(n) second-moment method from fixed cuspidal pi_0 to the minimal Eisenstein point pi_0 = E_0. Jana (Forum Math. Sigma 2022) proves the cuspidal case and explicitly defers E_0 to future work.

## Definitions
Let E(t) be the Borel minimal Eisenstein series with parameters t, t -> 0 the singular point E_0 (maximally non-tempered, order-(n-1) pole). Formally L(s,pi x E(t)) = prod_j L(s+t_j,pi), so the shifted second moment tends to the 2n-th power. Let d_n(m) be the n-fold divisor function (E_0 coefficients), theta_eff = (n-1)/2 its effective Ramanujan parameter. Let M(X) = sum_pi h(C(pi)/X)/L(1,pi,Ad) with smooth compact h. AFE length Y = X^{n/2}.

## Result
The specialization is precisely obstructed. (a) Diagonal: D_n(s) = sum_m d_n(m)^2 m^{-s} = zeta(s)^{n^2} H_n(s) with H_n holomorphic for Re(s) > 1/2 and H_n(1) > 0, giving diagonal log-power (log X)^{n^2} with positive constant H_n(1)/(n^2-1)!; verified in exact integer arithmetic for n = 3,4 with H_3(1) >= 0.042, H_4(1) >= 3.6e-7, elementary for all n. (b) Family mass M(X) ~ c(h) X^{a_n}, a_n = (n-1)(n+2)/(2n) (standard Plancherel-volume sketch). (c) Off-diagonal counting gap: trivial X^n vs X^{a_n} gap g_1 = n-a_n > 1; after Weil-only modulus saving X^{3n/4} vs X^{a_n} gap g_w = (n^2-2n+4)/(4n) > 1/2 for all n >= 3 (7/12 at n=3). (d) GL(n) Voronoi dual M* = c^n/Y satisfies M*/Y >= 1 for all c >= X, so the dual never shortens in the Kuznetsov range c ~ Y >> X; theta_eff >= 1 reverses cuspidal error estimates. (e) The order-(n-1) polar tower with residual-spectrum subtraction and small denominators must be resolved before any main term can be read. Hence neither the sharp asymptotic nor S(X) << M(X)(log X)^{n^2+eps} follows along this route without three named new inputs: uniform degree-n shifted-convolution power saving, regularized polar-tower subtraction, degenerate-Kuznetsov archimedean analysis.

## Proof / evidence
T1: a_j = d_n(p^j)^2 = C(n+j-1,j)^2 is j-polynomial of degree 2n-2; (1-X)^{n^2} kills the zeta^{n^2} polar part giving fixed polynomial R_n of degree <= n^2-1 with R_n(0)=1, R_n'(0)=0 checked coefficientwise exactly (J=80); positivity R_n(1/p) > 0 for p <= 500 plus tail exp(-2K/P_0) gives H_n(1) > 0. T2: exact rational identities g_1, g_w and inequalities via (n-1)(n-2) > 0, (n-2)^2 > 0. T3: exponent identity M*/Y = X^{n(sigma-1)}. All in output/artifacts/recovery_test.py (ALL CHECKS PASSED), independently re-executed by audit including exact-Fraction recheck.

## Limitations
Resolves the admitted precise-obstruction branch only; does not prove the sharp asymptotic or upper bound. Lemma A is a standard volume sketch, not a reproduced Plancherel computation. Structural items (ii)-(iii) are deductions from standard pole/residual-spectrum facts. Positivity bounds use floating partial products with large rigorous margins. Proof of uniform shifted-convolution saving would falsify the blocked verdict.

## Reproducibility
Run: python3 output/artifacts/recovery_test.py. Checks T1-T3, d_3 sanity values, gap and Voronoi tables for n = 3,4,5,6.

## References
S. Jana, The second moment of GL(n) x GL(n) Rankin-Selberg L-functions, Forum Math. Sigma 10:e47 (2022), doi:10.1017/fms.2022.39; CFKRS moment conjectures; Luo-Rudnick-Sarnak / Muller-Speh bounds (cuspidal theta < 1/2 reference).
