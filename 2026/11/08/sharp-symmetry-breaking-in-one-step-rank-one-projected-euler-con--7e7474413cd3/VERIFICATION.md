---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The tangent projector P0Z+ZP0-P0ZP0 fixes E. A(u)=[[1,u],[u,0]] has eigenvalues (1±sqrt(1+4u²))/2, best Frobenius rank-one retraction lambda_plus P_plus, and singular-value gap exactly 1. The exact cost in s=u² has derivative proportional to strictly increasing T_gamma(delta)-q, so threshold q_c=1+gamma/2 yields unique zero below, two symmetric global controls above. Direct expansion gives (q_c-q)s+(2q-1/2)s²+O(s³), quartic at criticality, near-critical split, cost gap and vanishing retraction error; the unreduced cost is strictly convex. Independently confirmed Taylor coefficients and spectral identities.

## originality

PASS

The complete one-step global minimizer classification, threshold and vanishing-error/nonvanishing singular-gap phenomenon is not a corollary of Carrel–Vanzan general continuous DLRA gradient error estimates or observed local minima, nor of general rank-one projector formulas alone.

## value

PASS

Constructs a rigorously quantified smallest-dimensional counterexample to transferring convex control uniqueness through best-rank-one projection without singular-value degeneracy; exact threshold and small-error scaling are meaningful to low-rank control design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
