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

# Exact verification and limits

Run `python3 verify.py` with a standard Python 3.9+ interpreter, from the same directory as this file; no downloaded libraries or ancillary assets are necessary. The verifier reconstructs the forbidden graph for the Rips model, recursively enumerates every independent face, applies the fixed vertex-toggle matching, checks all directed Hasse covers for acyclicity, enumerates every affine group element, and checks signed fixed-simplex Lefschetz traces against independent coset-augmentation traces.

The recorded replay in `verification_output.txt` is reproduced by the included `verify.py`. Expected exact counts are 25,531 augmented faces, 142,050 Hasse covers, 12,761 matching pairs, nine critical dimension-four faces and 200 successful elementwise character comparisons, with character value multiplicities \(9:1,4:8,1:75,-1:116\). The absence of other critical cells in the unaugmented matching is essential to the integral wedge conclusion. The invariant rank is exactly zero by averaging the character.

All finite objects in the stated theorem are exhaustively enumerated; there is no unverified limiting extrapolation. This is not an independent mathematical audit. It does not certify priority against inaccessible or unindexed material, integral quotient torsion, equivariant homotopy type, or larger torus-grid cases.
