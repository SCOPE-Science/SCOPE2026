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

The exact argument uses Euclidean chord-square identities, an exhaustive classification of diameter edges, simplicial identification with a graph independence complex, and established homotopy classifications for cycles and Möbius ladders.

Run `python verify_twisted_prism.py` with Python 3. The recorded output `verify_output.txt` must end with `VERIFY_OK`. The script performs 672 direct floating-point Euclidean diameter-graph comparisons across integer widths 3 through 30, including the predicted critical-height values. It also directly enumerates independent faces and computes reduced mod-two homology for 54 parameter cases of widths 3 through 8.

These are finite numerical and field-homology checks, not complete proofs or independent verification. In particular they do not establish integral homotopy types, exact real-boundary equalities, or universal quantifiers. Those claims rely on the accompanying exact geometric proof and named published independence-complex theorems. No full persistence barcode is claimed.
