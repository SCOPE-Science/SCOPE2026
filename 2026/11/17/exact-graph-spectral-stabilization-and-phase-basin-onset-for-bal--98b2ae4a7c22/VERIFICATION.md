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

# Reproduction and boundaries

The proof is self-contained in `RESULT.md`. Its critical computations are the exact rank-one derivative of the unrestricted double sum, the signed graph Jacobian, the orthogonal quotient decomposition, the strict symmetric Schur-complement equivalence, and the exact two-community scalar reduction. These are checked algebraically in the proof.

Run `python checker.py` with NumPy available. On the current embedded code, all 452 finite-difference, spectral, and invariant-circle checks passed. Random samples do **not** prove the universal theorem, and the one-dimensional basin measure must not be interpreted as a basin measure in the entire phase space.

No independent mathematical audit has been performed. Priority among unindexed or differently phrased results remains subject to literature review.
