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

# Reproduction

The included `verify.py` is a standalone Python standard-library checker, runnable as `python3 verify.py` from the extracted package. On the reviewed source it passed 600 exact `Fraction` comparisons or algebraic identities and 16 floating-point regime/asymptotic diagnostics, including the critical logarithmic correction. It uses no internet or external dependencies.

Mathematical verification rests on the proof in `RESULT.md`: exact \(p=uy\) recurrence, monotone sign classes, a telescoping contradiction for boundedness, and convergent tail estimates. The finite checker cannot establish the universal theorem, uniqueness of the global separating curve, or asymptotic limits by itself. The exact equations and inequalities in that proof supply those assertions. No independent audit was performed.
