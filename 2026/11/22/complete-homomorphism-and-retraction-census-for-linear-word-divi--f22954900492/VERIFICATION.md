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

# Reproducibility and limits

Run `python3 verify.py` from the extracted package directory, with Python 3 and no external packages. It prints the four independently exhausted source-to-target full-function checks and all endomorphism image-rank distributions for source ranks 1 through 5, ending with `VERIFY_OK`. In the four full-function tests, every set map is tested directly against both operations, without assuming the predicted normal form. In the larger-rank tests, the admissible image tuples are enumerated and checked against both operations, image-cardinalities, idempotence and bijectivity.

These finite tests do not certify all positive integer ranks and are not a substitute for the universal combinatorial argument in RESULT.md. No independent audit has yet been performed.
