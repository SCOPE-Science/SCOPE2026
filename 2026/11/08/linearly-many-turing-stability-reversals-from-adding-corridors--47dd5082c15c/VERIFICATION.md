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

# Mathematical verification

The full proof requires no computer algebra. It uses an explicit modal determinant, a decomposition of a hub graph into the hub/group-constant subspace and within-triple sum-zero subspaces, and the Courant–Fischer eigenvalue monotonicity theorem.

Execute `python corridor_verifier.py` (SymPy and NumPy installed). Actual replay completed with 72 exact Laplacian characteristic polynomial comparisons for \(1\le k\le4\), \(0\le r\le2\), \(0\le s\le2k\), and 24 independent assembled \(2n\)-Jacobian stability comparisons for \(1\le k\le2\). The script additionally asserts the exact rational determinant and trace of the modal matrix. These finite checks corroborate, but do not replace, the all-\(n\) proof.

The checker does not test nonlinear global stability, finite-time temporal rewiring, or ecological realism. No independent third-party validation has been performed.
