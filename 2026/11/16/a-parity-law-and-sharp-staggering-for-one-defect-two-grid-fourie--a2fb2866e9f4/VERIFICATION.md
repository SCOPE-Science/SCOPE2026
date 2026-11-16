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

Run `python CHECK.py` with Python 3 and NumPy. In the packaged environment it printed `CHECKS_PASSED 1597`. The checker constructs the full complex Fourier sampling matrix independently of the proof's block formulation, diagonally reconstructs its Gram matrix, compares its numerical eigenvalues and checks many rank/optimal-shift and near-resonance instances. These finite checks cannot establish all-integer identities, global minimax, or novelty. Those are supported by the separate direct mathematical proof and literature comparisons in `RESULT.md` and `REVIEW.md`. No external or independent mathematical audit has been performed.
