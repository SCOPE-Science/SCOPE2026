---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The RESULT.md reduction is sound: mapping centered vertex vectors to leaf differences gives diag(v_i-1)+11^T/(m+1) PSD for lambda_2≥1. At most one edge may be deficient; Schur complement gives d≤1/(m+1+sum 1/a_j) and Cauchy–Schwarz minimizes cost at C_*=sum c_i-Delta²/(m+1). The equality conditions uniquely force the displayed weights, including the boundary Delta=0 and m=2. Homogeneity gives B/C_*. For unit comparison rows (e0-ei)/sqrt(2), the one-step expected error decrease is L(p)/2 and normalized price yields 1/(2C_*). Independently checked price vectors (25,1,1), (16,9,4), (4,1) against cost and formula. Inspected complete verifier code, which checks rational principal minors; its reported log is not used as proof.

## originality

FAIL

FAIL: the October 12 published Polygon-imbalance law proves, already for every m≥2 and arbitrary positive real prices, the *identical* C_* formula and unique conductance allocation in both regimes; budget B is immediate scale. The extra Kaczmarz statement substitutes p_i for conductances and a normalization by expected price; combined with established eigenvalue-based sampling criteria it is a routine direct corollary, not an independently novel mathematical claim.

## value

FAIL

Although optimal spectral design is intrinsically motivated, all substantive star threshold and uniqueness content is already established, and the appended norm-one incidence-row one-step projection certificate is a direct rescaling of the prior spectral identity. It is not a meaningful new invariant or independently motivated advance beyond that prior result. Therefore the submitted final combined result has no surviving independently valuable original part.

The dated certificate retains the supplied scientific assessment, sources and limitations.
