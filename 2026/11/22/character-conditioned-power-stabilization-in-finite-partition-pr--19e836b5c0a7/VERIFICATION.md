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

# Verification of the finite algebraic identities

Run `python3 verify.py` using a Python 3 standard-library interpreter. It calculates the multivariate EGF coefficients over exact rational arithmetic and independently brute-enumerates the transformations with each prescribed character. For 2,441 combinations of block profiles, block characters and height bounds (up to 3 nonempty blocks and 6 total vertices), it checks the full coefficient identity. For each finite-stabilizing character, it also tests every index in the predicted closed interval and equality between the coefficient saturation and the product formula. Nontrivial character cycles are checked to contribute zero.

A verified run printed `CHARACTER_HEIGHT_EGF_BRUTE_FORCE_PASSED` and `profiles_characters_heights 2441`. Sample profiles for block sizes \((2,2)\) were character \((0,0)\) with cumulative counts \((0,6,12,12,12)\), character \((0,1)\) with \((1,9,9,9,9)\), and character \((1,0)\) with all counts zero.

The code checks only finite instances. The universal result follows from the rooted-forest and sharp-depth proofs in RESULT.md, not from extrapolation. No independent audit or certification is asserted.
