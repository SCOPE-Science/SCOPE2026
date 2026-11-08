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

# Verification evidence

The exact recurrence and its conjugation boundary are proved in RESULT.md for both \(N\equiv0\pmod4\) and \(N\equiv2\pmod4\). The information-theoretic sharpness argument is a continuous-torus rank proof and does not depend on numerical data. The independent code `CHECK.py` uses standard Python 3 and prints `CHECK_OK exact_and_direct_assertions=1011107` on a successful run. It evaluates integer determinants for even cyclic orders through 200, enumerates the \(N\)-th-root phase solutions at five orders, and directly verifies the fourth-autocorrelation Fourier product identity at five orders, with numerical tolerance in the latter test. Finite checks do not establish the universal statement; the stated proof supplies that argument. No independent mathematical audit has been performed.
