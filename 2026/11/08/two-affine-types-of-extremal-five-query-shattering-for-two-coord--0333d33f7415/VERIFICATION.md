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

Run `python3 verify_sparse_parity.py` to enumerate the affine-normalized candidate sets and affine frames using integer XOR only. The 2,600 nine-set and 14,950 ten-set cases are exhaustive after normalizing an affine-independent six-point frame (whose existence is proved in RESULT.md). The checker reports the covering 80 ten-sets, their complete image from one representative, the exact stabilizer, its two point orbits, and the affine-plane invariant. It also checks all 32 five-query responses. This is a finite mathematical certificate coupled to the proof of normalization, not a proof of historical novelty or an independent audit.
