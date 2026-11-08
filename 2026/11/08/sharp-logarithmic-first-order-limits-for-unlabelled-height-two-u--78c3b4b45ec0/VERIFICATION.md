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

# Verification and reproducibility

Run `python3 checker.py` with Python 3 standard library. The script independently derives coefficients from the Euler product and logarithmic-derivative recurrence through size 48, exhaustively enumerates isomorphism classes of unary functions satisfying the identity through carrier size five, checks known database initial terms, and reports `ALL_CHECKS_OK` when successful. The extracted checker has been run against the embedded code.

The analytic statements rely on the proof in `RESULT.md`: standard partition asymptotics, an explicitly bounded noncentral Fourier integral, a central cumulant expansion, the exact component deletion bijection, and a finite-profile Ehrenfeucht–Fraïssé strategy. Small-case enumeration and asymptotic diagnostics do **not** certify the uniform asymptotic estimate or historical priority.

No external independent audit or mathematical certification was performed.
