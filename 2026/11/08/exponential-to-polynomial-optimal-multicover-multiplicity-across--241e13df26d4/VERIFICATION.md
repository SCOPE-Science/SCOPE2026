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

The code in `artifacts/verify.py` implements two exact finite tests of the proposed enumeration: an independently written branch-state minimum-cost dynamic program and a direct enumeration of all vertex weights in five small instances. These tests exercise all three claimed arm lengths, several numbers of arms, and several integer demands. The independent test logic does not use the mathematical equality-characterization cases as an input.

Run `python3 artifacts/verify.py`. Its last line is `VERIFY_OK` when all tested equalities pass. The unlimited-parameter proof in `RESULT.md` uses leaf-forcing, summation lower bounds, and explicit characterization of equality cases. Finite testing alone does not prove the theorem, nor does it certify novelty or independent validation.
