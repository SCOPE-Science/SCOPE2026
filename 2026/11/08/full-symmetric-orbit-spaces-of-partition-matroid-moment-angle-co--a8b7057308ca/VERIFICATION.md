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

# Reproducibility and verification

Run `python3 verify.py` in the directory containing `verify.py`. The script uses only Python's standard library. The complete expected output is stored in `verification_output.txt`.

It checks the determinant \(-1\) of the degree-one map from the boundary torus to the two circle pieces, automorphism group orders by exhaustive permutations for eight finite block profiles, the rational symmetric-exterior invariants for multiplicities one through ten, and the resulting product Betti coefficients for zero through seven distinct nonsingleton sizes.

These tests are **not** a finite enumeration of all possible block profiles. The uniform mathematical argument is in the proof of `RESULT.md`; in particular the crucial geometric input is the product-map homotopy equivalence \(\operatorname{SP}^q(S^1)\to S^1\) for every integer \(q\ge1\). The accessible geometric proof and original bibliographic citation are included in `RESULT.md`.

No independent audit, external certification, or automated proof-assistant project was undertaken. Computed and conjectural limits are not confused: no unproved case is presented as certified.
