---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks

Run `python3 check_modular_cusps.py` with SymPy. It computes the invariants of the ordinary marked-point Tate form, checks the identities for the radicand and \(j=1728\), evaluates the two cusp residual constants, and enumerates the lifts of all 42 base cusp denominators. It specifically tests the two rational lifts at \(d=1\) and the single quadratic lift at \(d=25\); the aggregate degree spectrum alone would not distinguish the two twists. The expected last line is `PASS: canonical square class 5, denominator-wise cusp lifts, and degree spectrum`.

The modular interpretation identifying the canonical double cover, local ramification and nonzero divisor class are mathematical arguments in RESULT.md, not consequences of a finite computation. The verification does not certify priority or the full rational torsion of the Jacobian.
