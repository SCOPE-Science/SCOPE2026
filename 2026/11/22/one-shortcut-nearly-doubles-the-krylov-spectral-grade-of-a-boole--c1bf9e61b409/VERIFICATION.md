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

# Reproducibility and mathematical limits

Run `OPENBLAS_NUM_THREADS=1 python verify_hypercube_edge.py` with Python 3, NumPy, and SymPy. The tested script reports `PASS: 524 spectral masses, eigenvalue and exact-rank assertions`.

The program calculates spectral masses both by direct Walsh sums and by combinatorial counting for dimensions three through eight; diagonalizes actual \(2^d\)-vertex Laplacians around each positive resonance, checks the explicit distance-two formula through dimension 29 using rational arithmetic, and verifies selected critical eigenspace multiplicities by exact symbolic rank. Floating eigenvalue clustering is an experimental check, not a proof of the theorem for arbitrary dimension or arbitrary real edge weight.

The general result is established by the all-dimension projection-mass identity, a strict secular monotonicity argument, and a binomial-integral evaluation. The claim does not cover antipodal links, multiple edge updates, or finite-precision CG iteration complexity. The complete text of the older Wasin So paper could not be inspected; an equivalent bibliographic result remains a priority risk.
