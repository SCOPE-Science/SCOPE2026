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

Run `python3 verify.py` with Python 3 and no third-party dependencies. The program has been executed from the packaged file and printed `EXACT_OK`. It confirms that the 48 nonzero short \(D_4\) vectors split into 24 norm-squared-two roots and 24 norm-squared-four vectors; it performs full exact Gram-determinant recursion with counts \((1,48,816,1728,0)\); checks the displayed basis determinant two; and checks the ball-center inequalities for all 24 permutation simplices, finding 12 of squared diameter four and 12 of squared diameter six.

The proof's inference from the finite search is valid because squared norms in \(D_4\) are even and any frame achieving packet radius smaller than \(\sqrt{3/2}\) has every subset sum of squared norm at most four. The search therefore covers every possible obstruction to the claimed lower bound. The midpoint criterion checks five simplex vertices and, by convexity of a Euclidean ball, their entire convex hull. Independent mathematical audit was not performed. This certificate does not resolve the historical-priority question.
