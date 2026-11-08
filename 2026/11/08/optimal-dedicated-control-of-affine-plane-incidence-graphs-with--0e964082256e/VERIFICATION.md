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

# Reproducibility and proof boundary

Execute `python3 verify_affine.py` from the directory containing this file and the verifier. It requires only the Python standard library. The script confirms the incidence Gram identity, exact modular ranks of the constraints associated with the two large Laplacian eigenspaces, the selected line-kernel rank, both count formulas, and the stalled initial zero-forcing process for the prime orders \(2,3,5,7,11\). It terminates with `VERIFY_OK` if every assertion passes.

The rank calculation modulo \(1000003\) is exact in each sampled instance: a full-rank reduction implies nonzero rational determinant. The script does not enumerate or certify all possible finite affine planes and does not prove all orders. The general proof uses only the affine-plane axioms, the exact identity \(MM^{\mathsf T}=qI+J\), and the PBH criterion. No input-energy or robustness guarantee is inferred from controllability.
