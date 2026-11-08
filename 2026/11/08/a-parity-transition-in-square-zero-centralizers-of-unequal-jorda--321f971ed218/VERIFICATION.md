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

The self-contained finite-field tests use `checker.py` and `checker_gf4.py`. Run both with Python 3.11+ from the directory containing the scripts. Both compute genuine matrix squares, matrix commutators, and matrix ranks; they do not use the theoretical rank formula to determine ranks.

`checker.py` exhausts the centralizer for prime fields of sizes 2, 3 and 5 in the block lengths printed in `checker_output.txt`. It verifies the predicted full rank histogram, including the zero matrix, and directly tests the reduction of the square-zero equations. `checker_gf4.py` separately implements the field with four elements and checks block lengths 2–5, with its output in `gf4_output.txt`.

The geometric assertions are proved symbolically through a normal-form coordinate description and a polynomial hypersurface analysis, not through finite enumeration. The original unreduced defining ideal may contain nilpotents and is not assessed. The independent audit remains unperformed.
