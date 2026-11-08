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

The source `verify.py` uses only the Python 3 standard library. Execute `python3 verify.py` from this directory. Its separate enumerator checks the defining square-zero condition in a basis of the coefficient ring, computes ranks of expanded matrices by exact elimination over the small prime fields, and compares with independently computed Gaussian-product predictions. It checks six complete finite examples and gives `VERIFY_OK` on success. It also checks the algebraic support extremum for small parameter values. Universal correctness uses the block-matrix proof in `RESULT.md`; finite tests alone are not an infinite proof. The direct matrix arithmetic uses integer reduction modulo a prime and therefore is not a direct implementation of extensions such as \(\mathbb F_4\), although the proof covers all prime powers. No independent audit has been performed.
