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

# Exact finite verification

Run `python3 verification/symplectic_building_C9_verify.py` with Python 3 and no external dependencies. The script uses binary-polynomial multiplication modulo the primitive polynomial \(t^6+t+1\), derives all rank-one, rank-two and rank-three isotropic subspaces and all complete flags, computes cyclic orbits on all geometric simplices, checks the signed cellular chain condition, and row-reduces the quotient chain maps over three prime fields.

Observed check: `SYMPLECTIC_C9_BUILDING_VERIFIED`. Original building rank counts are 63, 315, 135; original 1- and 2-flag counts are 2835 each. For powers 1, 2, 4, 5, 7 and 8 of the order-nine generator no simplicial vertices are fixed; powers 3 and 6 fix exactly nine rank-two vertices each. Quotient vertices by rank are 7, 37, 15, yielding total orbit-cell counts 59, 315, 315 and Euler characteristic 59. Boundary ranks are 58 in dimension one and 257, 256, 257 in dimension two over prime fields 2, 3, 5 respectively. The boundary-of-boundary identity was checked for the 59-by-315 and 315-by-315 signed matrices.

**Scope of verification.** These finite computations are exact and exhaustive for the explicit 64-element field model. They are not themselves an integer Smith-normal-form proof or a proof of the full homotopy type. The integral homology and fundamental group follow from the separately displayed mathematical proof and standard orbit-space, building and cellular-homology theorems. Independent external mathematical auditing has not been performed.
