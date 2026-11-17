---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For A_kappa=[[1,1/2,0],[1/2,1,0],[0,0,kappa]], kappa>=1, its SPD eigenvalues are 1/2,3/2,kappa. One exact Lanczos step leaves the diagonal compressed complement diag(1,kappa). Schur boundary gamma=1/4 produces correction +1/3 and boundary subtraction -4/3; two-node Gaussian P-SLQ then evaluates Z_1^2+Z_2^2/kappa exactly, giving (chi_N^2 + kappa^-1 chi_N^2)/N -1. Independently checked rational Schur entries and the exact N=2 exponential convolution. At all finite N the lower tail is positive. CLT+Slutsky give Phi(-tau/sqrt(2)) for sqrt(N)/kappa -> tau finite; variance/Chebyshev treats infinity, subsequences prove iff N/kappa^2 -> infinity. Continuity and SPD Sylvester determinant for epsilon^2<3kappa/4 extend finite risk to irreducible tridiagonals. No simulation is used for asymptotic proof.

## originality

PASS

Best-of-knowledge: the original 2026 P-SLQ method provides the Schur-corrected bulk variance and consistency but the accessible abstract/references and related published results do not establish the exact finite-chi-square sign law or the joint square-root probe/conditioning frontier, even when Lanczos quadrature is exact. Relevant full primary text could not be inspected due to arXiv/OA retrieval difficulty and authorized Oxford VPN disconnection; that is a concrete residual risk, not an automatic rejection.

## value

PASS

Finite-sample covariance indefiniteness is a concrete algorithmic correctness failure even if Krylov quadrature and boundary moments are exact. Its exact failure probability and the necessary-and-sufficient N >> kappa^2 frontier quantify what probe budget prevents the defect, rather than merely exposing a trivial negative type or numerical roundoff. The irreducible SPD persistence makes the diagnostic relevant beyond a block-decomposed toy model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
