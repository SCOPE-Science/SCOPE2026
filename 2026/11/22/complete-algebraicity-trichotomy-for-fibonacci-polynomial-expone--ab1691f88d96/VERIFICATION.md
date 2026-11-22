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

# Reproducible exact checks

Run `python3 fibonacci_polynomial_degree_check.py` with Python 3, using the attached standalone file. The expected result is `FIBONACCI_POLYNOMIAL_DEGREE_EXACT_OK 111 cases 125_degree_example 625_degree_example`.

The checker constructs the exact polynomial-weight exponential by its coefficient recurrence; independently expands the Lucas linear/quadratic product; compares the two through a finite truncation in 111 cases; and checks the predicted denominator and primitive-order valuations. Included test cases cover zero, rational weights, mixed-sign weights, the integral mixed example of degree 125, and another of degree 625.

Finite checks are not proofs of the infinite statement. The infinite correctness argument is given in `RESULT.md`, using the rational-residue obstruction for odd terms and an isolating irreducible Lucas quadratic for exact extension degrees. The published integer-coefficient criterion is explicitly cited for integral examples. Independent audit: not performed.
