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
# Reproduction of exact \(R_{10}\) ellipsoid identities

With Python 3 and SymPy installed, execute `python verify_r10_ellipsoids.py` in the same directory. The code constructs the integral matrix from its modular-index definition rather than relying on stored arrays and verifies all 3,002 square minors for total unimodularity, all ten unsigned outer-contact equations, the full ternary polar enumeration (243 potential lattice points, 73 feasible, exactly 12 of active rank five), the exact polar covariance and quadratic contacts, and the five eigenvalues and determinant. It prints `R10_ELLIPSOIDS_EXACT_PASS` if and only if all assertions pass.

The only non-computational ingredients are the standard integer-vertex consequence of total unimodularity, the vertex criterion of full active-normal rank, the classical John/Löwner isotropic-contact criterion, and the polarity relation between a centered convex body's John and the polar body's Löwner ellipsoid. Those are explicitly used and their hypotheses checked in the proof.

This is exhaustive exact finite computation combined with standard mathematical theorems, not a floating-point simulation or proof of any generalized family beyond the specified matrix. Independent audit: not performed.
