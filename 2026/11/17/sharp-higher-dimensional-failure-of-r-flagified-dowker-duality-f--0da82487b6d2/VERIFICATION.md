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

# Verification and limits

Run `python3 VERIFY.py` with a standard Python 3 interpreter. The checker constructs all original witness-intersection faces as unions of point-stars, independently evaluates the literal higher-flag condition on vertex families of size at most \(r+2\), and computes all mod-two boundary ranks on the completed complexes for five small parameter pairs.

The provided `VERIFY_OUTPUT.txt` is a recorded replay and includes the exact vertex, face, new-facet and reduced-homology counts. The finite computations do **not** prove the theorem for untested parameters or establish integral homotopy equivalence. Those conclusions follow from the minimal-obstruction lemma, natural nerve attaching comparison and simplex-skeleton Morse matching in `RESULT.md`.

Independent audit: not performed. No external certification is asserted.
