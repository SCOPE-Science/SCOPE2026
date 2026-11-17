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

# Verification of the finite orbit-space calculation

`verify_colored_a5.py` computes from original labelled words, rather than assuming the predicted quotient incidence matrices. It checks all orbits and stabilizer-invariant orientations, constructs integral cellular differential matrices, checks their products vanish, calculates exact Smith normal forms with SymPy 1.14.0, and validates the two-skeleton color relations. The exact output in `verification_output.txt` records the counts and factors. The homotopy upgrade additionally uses the mathematical argument given in `RESULT.md`; the executable does not implement Hurewicz or Whitehead.

Execute with Python 3, SymPy 1.14.0 and `python verify_colored_a5.py`. The finite enumeration is exhaustive for the stated five-label binary-color object; neither untested infinite-parameter assertions nor independent external certification is claimed.
