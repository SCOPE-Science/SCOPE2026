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

`VERIFY.py` reconstructs the parameterized Neumann-mode linearization, exact rational characteristic polynomial, all-mode Routh–Hurwitz margin, two crossing parameters and imaginary-frequency squares. Its symbolic identities check polynomial equalities for arbitrary modal square \(q\) and directed-movement sensitivity \(w\), not just sampled values. The proof in RESULT.md uses \(q=k^2\) to settle all infinitely many integer modes. Numeric eigenvalue examples are diagnostic only. At exact thresholds the affected mode is spectrally neutral, and no nonlinear periodic-solution stability or independent scientific audit is claimed.
