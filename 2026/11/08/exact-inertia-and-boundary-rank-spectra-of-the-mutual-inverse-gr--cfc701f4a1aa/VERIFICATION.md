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

# Verification record

The argument is a mathematical proof for all integer parameters \(n\geq1\), \(1\leq r\leq n\). A separate finite checker reconstructs the order-preserving monoid, evaluates the mutual inverse equations directly on every ordered pair within each Green rank, and compares with the independently constructed crossed-square adjacency. It verifies the exact full-row-rank triangular certificate and the two exact Gram identities. Numerical diagonalization tests the full predicted spectrum, with tolerance justified by the small finite matrices; it cannot replace the symbolic proof.

Reproduce by running `OPENBLAS_NUM_THREADS=1 python verify_inverse_inertia.py` with Python 3, NumPy, and SymPy. The recorded output includes 21 rank classes, 637 transformations in aggregate, and 75,225 ordered-pair checks. It ends with `VERIFY_OK rank_classes=21 elements=637 checked_ordered_pairs=75225 inertia_and_full_spectrum=match`.

Scope: looped adjacency only, not the loop-erased simple graph; no proof concerning involution-matching existence or any uncomputed general-rank Gram eigenvalue formula. The finite script is independent of its recorded output and was executed from the actual packaged source text.
