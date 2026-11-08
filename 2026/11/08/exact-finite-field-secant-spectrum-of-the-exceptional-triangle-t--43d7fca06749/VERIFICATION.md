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

# Exact arithmetic checks and limits

Run `python3 verify_toric_trisecants.py` using only Python 3's standard library. It constructs the fields of orders \(3,4,5,7,8,9,11,13,16,25,27\) explicitly as polynomial quotients, checks all nonzero inverses, enumerates each projectively normalized point of the monomial torus, classifies each chord through the identity point, verifies its third rational torus intersection or its tangent/boundary exception, and compares the resulting rational line counts to the closed formulas. The actual output is included verbatim in `verification_output.txt`, whose final line is `ALL_EXACT_CHECKS_PASSED`.

Run `python3 direct_line_census.py` in the same directory. It imports the self-contained finite-field arithmetic from `verify_toric_trisecants.py`, enumerates **all** row-reduced two-planes in a four-dimensional vector space over fields of orders \(3,4,5,7,8,9\), computes each line's actual intersection with the monomial torus, and matches the full zero-, one-, two- and three-secant counts. The independently generated output is `direct_line_output.txt`, ending in `DIRECT_LINES_PASS`.

The finite computations are exact and reproducible, but the uniform theorem for arbitrary finite fields is proved through the symbolic factorization, rational tangent-section parametrization, torus transitivity, and projective incidence double counting in `RESULT.md`. No finite collection of field tests alone establishes the universal claim or historical novelty.
