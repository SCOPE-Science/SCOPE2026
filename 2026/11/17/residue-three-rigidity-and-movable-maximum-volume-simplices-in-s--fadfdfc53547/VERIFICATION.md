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

# Exact checks and limits

Run `python3 second_hypersimplex_checker.py` with the Python standard library. This program uses fraction-free integer determinants to enumerate all selected edge subsets of sizes n for 3 <= n <= 7. It verifies the nonzero odd-unicyclic determinant formula and the maximal numbers 1, 12, 162, 10, 420. In divisible-by-three test dimensions it also excludes distinct maximal vertex sets sharing n-1 vertices.

The proof in RESULT.md, not the finite checker, establishes arbitrary-dimensional rigidity from determinant multiaffinity and exhibits the full triangle-product equality constructions with exact cofactor signs. The verifier does not independently audit the older 1995 determinant lemma and does not classify all flexible simplex families. This is not independent validation.
