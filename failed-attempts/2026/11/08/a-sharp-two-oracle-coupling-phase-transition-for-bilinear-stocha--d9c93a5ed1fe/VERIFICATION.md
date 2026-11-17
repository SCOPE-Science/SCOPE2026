---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

For random coefficients A,B∈{a,b}, exact squared-norm multiplier q=(1−sAB)^2+sB²; every binary uniform coupling is affine mixture Qp=pQsame+(1−p)Qanti. The difference is s(b−a)²(−1+s(a+b)²/2), while stable ceilings follow 1−A_p s+B_p s²<1. The quartic sign factor reduces through u=r+r^-1 to u²−2u−4, and completion of squares gives global fastest rate. Independently checked exact identities and rational qsame=10/9,qanti=17/18 at (a,b,s)=(1,2,1/3).

## originality

FAIL

Two older published exact theorems imply the sampling reversal, all stable ceilings, heterogeneity threshold and special-case witness. Only an elementary tuning corollary remains and is insufficiently distinct to make original theorem original.

## value

FAIL

Comparing fastest asymptotic contraction to maximum stable step is a meaningful design question, but the remaining result is a one-variable quadratic minimum of already-published exact risks; it does not survive the nontrivial-value bar as a separate final claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
