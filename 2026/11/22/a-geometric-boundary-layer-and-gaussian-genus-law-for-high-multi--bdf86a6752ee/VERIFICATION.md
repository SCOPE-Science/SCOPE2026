---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Run `python3 verify_perfect.py` (Python 3 standard library only). The checks comprise 16 exhaustive all-subset additive semigroup censuses for \(F=3,\ldots,18\), covering 298 qualifying semigroups, alongside 17 symbolic polynomial-coefficient recurrences through length 18. The integer-moment transfer is evaluated at \(F=41,101,201,401,1001\), and the normalized genus mean, variance and multiplicity-boundary mass are compared with the theoretically derived constants. All checks passed on the included code before packaging.

The exhaustive finite tests are genuinely exhaustive only over the specified bounded ranges. The rational-generating-function identity, dominant-pole claims, and central limit theorem require the structural and analytic arguments presented in `RESULT.md`; the script alone cannot prove them.
