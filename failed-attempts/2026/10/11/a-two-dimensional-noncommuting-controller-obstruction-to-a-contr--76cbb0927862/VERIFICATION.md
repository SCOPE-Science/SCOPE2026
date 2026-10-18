---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The journal theorem is exactly Theorem 3.7 (pp. 162-163) and assumes K commutes with T,U and SΛ commutes with T, not SΛ with U. Exact rational evaluation of S=diag(4,1), T=K=I, U=[[1,9/10],[9/10,1]] gives eigenvalues 1/10,19/10, ordinary bounds 1,4, and for f=(1,-2) mixed energy <ΛUf,ΛTf>=-1. This contradicts any positive lower controlled bound. Under additional pairwise commutation, c_- S≤T S U≤c_+ S with c_-=||T^-1||^-1||U^-1||^-1, c_+=||T||||U||, proving the sufficient two-sided transfer, not optimality.

## originality

FAIL

Although identifying the defect in Ghosh–Samanta Theorem 3.7 is theorem-specific, the fixed-frame mixed-operator characterization and noncommuting-positive-controller counterexample are already covered by the more general published continuous g-frame result. Taking a one-block g-fusion frame W=H and K=T=I is its direct specialization; changing a rational matrix and cited theorem does not yield an uncovered mathematical claim.

## value

PASS

Checking and correcting the explicit hypotheses of a published controlled-frame equivalence is substantively motivated. The negative quadratic witness exposes a genuine positivity gap and the commutation repair restores quantitative frame bounds; this judgment does not cure the independent originality failure.

The dated certificate retains the supplied scientific assessment, sources and limitations.
