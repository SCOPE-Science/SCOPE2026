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
Run `python3 check.py` with SymPy available. The script checks the coordinate-shear identity, the oscillator-energy derivative, both inward barrier derivatives and the exact constants \(96\) and \(192\) at their critical faces. The analytical proof in `RESULT.md` separately verifies the finite-time continuation argument, positivity of every face margin, the escape-time upper bound and the Poincare-recurrence implication. Symbolic checks certify algebra, not an infinite-time trajectory theorem by themselves.

The parameter domain is \(a>0\), \(b\leq0\), \(c\in\mathbb R\). The public result does not supply a numerical enumeration of all initial states or an independent audit.
