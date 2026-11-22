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

The proof is an explicit two-phase sequence of elementary collapses, followed by an integral homotopy argument. The standalone checker `checks/check_tolerance_path_square.py` independently reconstructs the simplices. It ran successfully for n=4 through 50 (47 instances, 35,720 collapse pairs), with mod-two chain-rank checks for n=4 through 12. No claim of independent mathematical validation is made.

The exact number of tetrahedral faces is `(n-3)**2`; these are exactly the faces paired away. The reduced two-dimensional integral homology follows from the proven collapse, connectivity and Euler identity, not from any finite extrapolation.

Reproduction: `python3 checks/check_tolerance_path_square.py` (Python standard library only).
