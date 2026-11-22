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

# Reproduction of the finite proof

Use Python 3.10 or newer. From the directory containing `check.py`, execute `python3 check.py`. The verifier reconstructs all 108 perfect matchings of the explicitly defined 18-vertex graph, every one of the 30,353 nonempty simplices, and checks the certificates located in `certificates/`.

The collapse certificate lists 14,436 pairs of integer face masks, one per line. Each free-face pair is verified against the *current* remaining simplicial complex before deletion; the remainder has only cells of dimensions zero through three. The fundamental-group certificate begins with 29 spanning-tree edge masks and continues with 241 pairs consisting of a triangle mask and its unique previously unknown edge mask, enabling a direct triangular relator elimination. The integer-boundary certificate lists 453 row-column pivot indices for the 694-by-487 degree-three boundary. Each chosen pivot must be exactly \(\pm1\); Schur complements are computed using arbitrary-precision integers, and the final matrix must be identically zero. Boundary-square vanishing is checked explicitly.

The resulting reduced integral homology is free of rank 34 in degree three and zero elsewhere. A simply connected, two-connected three-dimensional CW complex with this homology is a wedge of 34 three-spheres. This last deduction invokes the standard Hurewicz and homological Whitehead theorems; it is a mathematical proof step, not a simulated computer calculation.

The included `verification_output.txt` is a record of a successful execution, not a substitute for rerunning the checker. All artifacts required for verification are embedded with exact byte counts and hashes. No external proof-assistant or independent verification is claimed.
