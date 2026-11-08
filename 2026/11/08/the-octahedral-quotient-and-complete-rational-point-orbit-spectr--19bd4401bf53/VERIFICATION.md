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

# Reproduction and scientific boundaries

Run `python3 verify_triangle.py` from this directory with a standard Python 3 interpreter. The verifier has no external dependencies. It performs exact quadratic-field arithmetic in characteristic eleven and enumerates all 122 rational points of the quotient x-line, the entire 24-element Möbius subgroup, the octahedral polynomial identity, and all rational affine lifts over nonspecial x-values. It prints `ARITHMETIC_OK`, `RATIONAL_ORBITS_OK`, and `VERIFY_OK` on success.

This finite enumeration is exhaustive for the specified finite-field objects and supplies exact numerical evidence, not an unsupported statistical extrapolation. The proof also uses the published genus, maximality, degree-eight Galois cover, and full order-192 automorphism theorem. Those cited geometric inputs are not rederived by the script. The exceptional x=0 and \(x^{12}=1\) fibers require local normalization; the explicit local argument is given in RESULT.md, and root tests alone are not substituted for it. No independent audit has been performed.
