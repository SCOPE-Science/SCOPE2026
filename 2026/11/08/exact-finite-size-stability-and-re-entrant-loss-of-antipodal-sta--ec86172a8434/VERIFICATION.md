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

# Reproducibility and evidence limits

The attached `verify.py` is standalone and uses only the Python standard library. Run `python verify.py` alongside `RESULT.md` to reconstruct the exact rational Jacobian for the complete-graph system directly from the ordered distinct-triad derivatives.

The program checks all transverse eigenspaces as well as the neutral common-rotation mode for \(504\) small finite-size and rational-parameter cases. It independently evaluates signs against the sharp stability-window inequalities, evaluates exact zero crossings at the seven-node thresholds, and confirms the arithmetic of the \(29\) and \(8\) counts. It also computes centered numerical derivatives of the original nonlinear vector field for three small configurations. All checks executed successfully in the producing environment. They corroborate but do not constitute an exhaustive proof for arbitrary graph size.

The universal proof uses exact invariant subspace decomposition and elementary sign algebra, as written in `RESULT.md`. The status of dynamics exactly at nonhyperbolic parameter boundaries, global attraction, and other families of equilibria remains unproved. No independent scientific audit or external formal certification is claimed.
