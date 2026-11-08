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

`verify.py` checks the two exact rooted generating functions against exhaustive edge-state enumeration for \(b=2,3,4\); verifies symbolic mean and variance polynomials on \(K_{2,3}\), the single coefficient sign change after the positive-odds substitution, and an exact rational root bracket; verifies leading endpoint coefficients for \(b=3,4,5\); and reports `VERIFY_OK` upon success. Run with `python verify.py` in an environment with Python 3 and SymPy.

The complete claims for every integer \(b\ge3\) follow from the analytic rare-event and low-density arguments in `RESULT.md`, not from the finite enumerations. The numerical root decimal is an approximation; the exact rational bracket and transformed-polynomial sign certificate are the verified statements. No independent scientific validation was performed.
