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

# Reproducible mathematical checks

Run `python verify.py` with Python 3 and the SymPy package. The script verifies the rational cyclic identity, radical double-root values, exhaustive rational test triples on a finite grid, two threshold examples and selected strict-interior and off-grid trajectories. The exact general argument appears in RESULT.md; numerical trials are not used to establish its universal quantifiers. No independent validation has been conducted.

At exact thresholds the inverse step has a double positive root. Differentiability is not asserted there. The paper's original recurrence is interpreted using the **larger quadratic root** where it is real and strictly positive, not using arbitrary implicit branches.
