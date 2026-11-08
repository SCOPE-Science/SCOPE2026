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

Reproduce with `python3 verify.py` (Python standard library only). It independently enumerates all circular words of lengths 2 through 10 without equal adjacent letters and groups them under directed digram profiles; it compares full cyclic fiber sizes with the proposed criterion. It separately enumerates the balanced loop-free directed matrices at lengths 2 through 29 and calculates each exact cyclic fiber by directed matrix-tree arborescence counting plus a Burnside divisor average. The checker confirms the generating-function coefficient at every tested length. Both approaches are finite checks and cannot replace the all-length Eulerian excursion proof.

Independent scientific validation is not performed. The code does not handle profiles allowing repeated adjacent symbols or alphabets larger than three.
