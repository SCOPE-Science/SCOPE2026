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

# Verification and limits

Run `python3 verify_circular_three_squares.py` using the Python standard library. `verification_output.txt` is the actual captured output from this program.

The program compares literal squares in doubled binary circles, an independent occurrence-by-gap construction, and the closed piecewise counting expression for all 7,140 ordered zero-gap triples of lengths 3 through 36. The maximization loop checks all 669,920 ordered zero-gap triples for lengths 3 through 160, including the complete small-length maximum vector and the exact optimizer permutation class for each length at least 25. Another 300 deterministic large-parameter tests check the sharp bound. It also tests the first length where square diversity exceeds circumference.

These tests are finite. The infinite assertion for all lengths at least 25 follows from the arithmetic proof in RESULT.md, including the congruence constraint on consecutive gap differences and strict exclusion of all competing repeated-gap regimes. Prior pointwise square counting is explicitly acknowledged. Independent audit remains unperformed.
