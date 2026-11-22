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

# Verification and reproducibility

Run `python3 verify.py` with Python 3 and no external dependencies. The checker compares the complete predicted and directly enumerated fiber tables for the first nine ternary precisions; it also reconstructs selected deeper fibers through stepwise root lifting. The code checks exactly 29,773 target comparisons (29,523 exhaustive targets plus 250 additional larger-precision targets).

The infinite assertion rests on the proof: a bijective linear branch, two Hensel-simple branches of \(u^2(u+1)\), and a third branch conjugate to a square map via \(v\sqrt{1+3v}\). The square-root count formula and the parity-dependent maximizing values follow from the classification of quadratic residues modulo powers of three. Computations are corroboration, not a substitute for those arguments. An independent mathematical audit has not been conducted.
