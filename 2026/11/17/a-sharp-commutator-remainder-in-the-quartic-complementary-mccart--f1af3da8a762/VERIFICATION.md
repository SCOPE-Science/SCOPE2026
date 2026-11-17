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

# Verification

The main proof derives the two squared norms by cyclic trace expansion; positivity is then automatic. It proves all dimensions by Schatten Hölder and finite-rank approximation. For any positive Schatten-four pair, the relevant fourth-order trace products are trace class. This analytical argument verifies the theorem independently of finite enumeration.

`verify_quartic.py` is a standalone Python 3 program requiring only the standard library. Run `python verify_quartic.py`; the verified output was `QUARTIC_MCCARTHY_REMAINDER_OK 564 rational_matrix_pairs`. It checks exact-rational PSD Gram matrix pairs and both two-dimensional equality witnesses. Additional independent complex-Hermitian tests (200 positive-semidefinite pairs, sizes two, three, five and eight) numerically confirmed the same identity at relative tolerance \(10^{-9}\) and absolute tolerance \(10^{-6}\). These are diagnostic, not proof of the universal claim.

The full exact identity and rank-one witness establish the global coefficient \(6\); the zero-defect classification is proved, not inferred from finite checks. No independent audit or publication-priority certification has been performed. The result concerns the fourth exponent only.
