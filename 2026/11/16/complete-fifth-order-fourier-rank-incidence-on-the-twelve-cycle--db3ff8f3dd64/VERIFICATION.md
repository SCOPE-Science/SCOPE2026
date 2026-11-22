---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Every 5-subset of Z_12 has trivial translation stabilizer (gcd(5,12)=1), leaving exactly C(12,5)/12=66 orbit representatives in each index. For each pair, the determinant expanded in Q[z]/(Phi_12), Phi_12=z^4-z^2+1, vanishes iff all four exact integer coefficients vanish. Testing all 5x5, 4x4, 3x3 minors gives full complex rank. Independently recomputed all 4,356 representative ranks from the actual census12.json representative sets using exact integer polynomial reduction, finding zero discrepancies and counts 27 rank3, 757 rank4, 3572 rank5. Orbit size 144 gives 3888,109008,514368; 2 all-full-rank representative row sets give 24 full-spark rows. Finite order-twelve enumeration is an exhaustive proof of this finite claim; mod1009 corroboration is not used as complex-rank certification.

## originality

PASS

Best-of-knowledge: a new complete fifth-order 66x66 positional rank-incidence array and two-dimension defect count, not determined by prior row full-spark, existence, support-profile, or aggregate zero-minor results. Exact old tabulations might hide the same data and remain a concrete priority risk.

## value

PASS

The natural order-twelve harmonic design problem asks exactly which five-frequency masks lose dimensions and by how much. The complete exact incidence matrix and explicit two-dimensional losses distinguish recoverability beyond the prior full-spark yes/no classification. This bounded, exhaustive exact invariant is independently useful without a general order-n theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
