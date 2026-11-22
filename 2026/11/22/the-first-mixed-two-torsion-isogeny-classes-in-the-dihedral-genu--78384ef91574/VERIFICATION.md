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

Run `python3 verify.py` from this directory. It performs exact computations in \(\mathbb F_5\) and \(\mathbb F_{13}\), using two independently implemented point-count routes (genus-two sextic and genus-one quotient), complete quadratic factor searches, Frobenius fixed-even-subset enumeration, and quadratic twist checks. It also checks the all-parameter prime-five exclusion, the eleven unit-square-class prime-thirteen rows, and the seven trace bins across twenty-two equations.

Expected first output: `D4_F13_WEIL_TORSION_FIRST_PRIME_VERIFIED`. This tests only the finite portions of the proof; the uniform split-parameter formula is proved symbolically in `RESULT.md`. The elliptic-square Jacobian isogeny is a cited established theorem, not independently reproved by this script.

Independent audit has not been performed. No conclusion concerning the stronger double-isogeny condition is tested.
