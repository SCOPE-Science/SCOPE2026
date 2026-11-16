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

# Reproduction checks

Run `python3 check_binary.py` and `python3 check_palettes.py` with Python 3.8 or later; neither needs third-party packages, floating-point arithmetic, or network access. The scripts construct primitive words by independent cyclic-period tests. The first computes exact integer Walsh–Hadamard coefficients at every frequency for binary lengths 2 through 15. The second constructs exact tensor character transforms with Gaussian integers and Eisenstein integers, and separately for the noncyclic Klein four-group, for the listed finite ranges. It verifies that imaginary/Eisenstein components vanish, the coefficient support equals the predicted annihilator, the rank is exact, and both positive singular-value endpoints match the theorem.

The proof in RESULT.md establishes the theorem for every length and finite abelian alphabet; the finite tests cannot establish an infinite result alone. The calculations compare exact integers and do not use timing or cached logs as scientific evidence. Literature searches and source-inspection limits are recorded in the scientific review.
