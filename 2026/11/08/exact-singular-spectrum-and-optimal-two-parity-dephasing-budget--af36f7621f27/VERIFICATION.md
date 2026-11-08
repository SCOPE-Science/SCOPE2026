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

# Verification of stated singular spectrum and budget law

The analytic proof derives the exact commuting conditional-expectation product on the scalar, first diagonal-traceless, second diagonal-traceless, and doubly orthogonal sectors, then proves the global schedule bound and sharpness. These arguments cover all finite dimensions and parameter values under the hypotheses, including dephasing endpoints.

Run `python check.py` with NumPy available. This independently constructs each matrix-channel superoperator in a matrix-unit basis and checks singular multisets, traceless contraction norms and a finite-grid minimax allocation. The finite experiments only test the claimed formulas in sampled cases; they are not a proof for all dimensions or budgets. The proof does not cover nonmonomial-square unitaries or channel distances in trace/diamond norm. The two-complete-measurement erasure case is previously known in mutually unbiased bases theory.
