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

The exact proof is in `RESULT.md`. Run `python verify.py` with Python 3 and SymPy installed. The script tests the algebraic identity after exact reduction by the cubic contact polynomial, the unique-root isolating interval, the positivity conditions, and 5,001 supplementary sampled radial points. The expected success prefix is `HERMITE_123_MINIMAX_CERTIFICATE_PASS 5001`.

The computation does not independently establish originality or replace the analytical proof. The relative Gaussian factor is part of the exact theorem. No global unweighted noise-stability guarantee is asserted.
