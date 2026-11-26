---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

On the mean-zero subspace the objective is a spectral trace. For f(x)=x^-p at p>0, or -log(x) at p=0, its Hessian in an eigenbasis is a sum of squared perturbation entries with strictly positive divided differences of f', including f'' for equal eigenvalues. The restriction of the simple-graph Laplacian is injective in conductances: extend by zero on the constants and recover weights from the off-diagonals. The compact budget simplex has connected feasible points and the objective tends to infinity at disconnection, so strict convexity gives a unique global optimum. Rotations force the two conductance classes and a>0 since rungs alone disconnect. The rim eigenvalue factor is 4 sin^2(pi k/(2n)); the antipodal matching contributes 2b exactly on odd modes. With a=(B-ncb)/(2n), increasing b along the affine budget segment has the same derivative sign at zero as increasing r=b/a. For p>0 this sign is that of c S/2 - 2T, for S=sum mu^-p and T=sum over odd modes of mu^-(p+1); the log case is S=2n-1 and the analogous T. Strict convexity gives deletion including equality, and a unique positive stationary allocation if the derivative is negative, because the other endpoint disconnects. Subtracting even modes from the full csc^2 and csc^4 sums gives the two rational endpoints; independently, at n=2 the spectrum factors (2,4,2) give C=4/(2+2^-p), agreeing with both rational cases. By reflecting the spectrum and bounding 2 sin(pi k/(2n)) below by 2k/n for k<=n, dominated convergence gives the odd zeta factor in T and the full zeta factor in S for p>1/2. Below half order an integrable endpoint cutoff and the beta integral give S~2n I_p. At half order, csc u=1/u+O(u) uniformly for 0<u<=pi/2 gives S=(2n/pi)log n+O(n); T~7 zeta(3)n^3/(4 pi^3) yields the claimed critical coefficient. At fixed n both smallest modes are odd, so the large-p ratio tends to 4/mu_1. The proof does not need a switch of fixed-order and fixed-size limits. The frozen checker was inspected, not executed; its finite pseudoinverse and Fourier checks and tolerance-based comparisons do not certify infinite-size asymptotics or unrestricted uniqueness.

## originality

PASS

The supported distinct contribution is the calibrated positive-real-order Möbius-ladder support-price threshold, particularly its explicit three-regime large-size scaling. The determinant threshold is covered exactly by a prior record and is properly credited. Spectral design criteria, the convex optimization framework and the endpoint-sum method are antecedents, not claims of novelty. The strongest related indexed statements differ in graph or observable and do not supply the three-regime priced Möbius frontier.

## value

PASS

Even with standard optimization tools, the explicit frontier decides exactly when a natural edge class is discarded in an unrestricted priced network. The calibrated dependence on inverse spectral order distinguishes bulk from low-frequency control and yields a logarithmically corrected critical law, which is not visible in either determinant or inverse-trace order alone. The value lies in the finite threshold together with these quantitative design regimes, not in rederiving the determinant endpoint or assuming a symmetric optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
