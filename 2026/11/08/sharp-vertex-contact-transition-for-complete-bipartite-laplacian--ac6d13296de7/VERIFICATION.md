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

Execute `python check_circumball.py` with NumPy and SciPy installed. This reconstructs original graph Laplacians, checks the stated centers and squared vertex distances, independently verifies convex-contact weights, and compares against unconstrained numerical minimum-sphere problems. Observed marker: `BIPARTITE_LAPLACIAN_CIRCUMBALL_CHECKS_PASSED 138 77`. The code covers finite cases only; the analytical derivation in RESULT.md proves all admissible integer parameters. The parameter boundary was also checked exactly for the adjacent pair `(3,13)` and `(3,14)`.

The geometry uses the ordinary Euclidean metric in the zero-sum subspace; the program does not transform to a potentially nonisometric lattice basis. No independent mathematical audit has been performed.
