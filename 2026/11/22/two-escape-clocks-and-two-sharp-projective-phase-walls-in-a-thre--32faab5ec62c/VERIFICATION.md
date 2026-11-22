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

# Verification and scope
The standalone `checker.py` uses exact rational iterates of the complete three-dimensional polynomial map and the derived scalar recurrence. It checks seed reconstruction, three-coordinate agreement, eventual negative signs in the constructed examples, and normalized finite logarithmic heights for twelve explicit rational parameter/seed cases. The check executed successfully with 312 assertions or height comparisons.

Infinite behavior follows instead from the explicit logarithmic-band induction and uniformly summable perturbation estimates in `RESULT.md`. No finite experiment establishes that induction. For every fixed real \(a,b\) with \(b
e0\), sufficiently large \(R\) satisfies the required dominance and error bounds. The proof makes no statement about escaping states outside the described chamber. Independent audit is not performed.
