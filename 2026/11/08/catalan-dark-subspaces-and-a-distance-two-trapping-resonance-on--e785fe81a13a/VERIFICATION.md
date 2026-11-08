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

# Verification information

Run the included `verify.py` with Python 3 and SymPy: `python verify.py`. The program carries out exact integer/rational calculations only. It tests row ranks and equal row spaces for 14 \(n,k\) cases with at most 36 untrapped vertices, verifies symmetry, rank, idempotence, adjacency eigenspace equations and the explicit projector kernel, and checks the entire 15-by-20 boundary block for the distance-two seven-point example. In the latter case the 10-by-10 Gram matrix is verified exactly to be \(4I_{10}+5\mathbf1\mathbf1^\top\).

`VERIFY_OK cases= 14` and `J_2(7,3) resonance: (15, 20, 10)` indicate all finite tests passed. The dimension-unbounded argument is proved separately by the inclusion-rank induction and invariant-subspace calculation in `RESULT.md`. Finite checking does not certify novelty or substitute for an infinite theorem. The checks do not establish finite-time decay bounds, robustness under imperfect detector placement, or external independent validation.
