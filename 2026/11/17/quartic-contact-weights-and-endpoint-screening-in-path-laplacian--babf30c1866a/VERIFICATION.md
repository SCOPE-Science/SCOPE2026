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

# Reproducibility and limitations

Run `python check_path_ball.py` using Python 3.9+ and only the standard library. The script directly reconstructs the full path Laplacian matrix, proposed optimal barycentric weights, centers and distances in exact rational arithmetic for 78 graph orders, all integers from 3 to 80. It checks the three-vertex exception, the sharp four-vertex contact tie, strict endpoint screening afterward, and the exact clearance and center formula.

A second integer recurrence check verifies the quartic finite-difference identity and Vandermonde normalization in 997 graph orders from 4 through 1000, involving 498,500 recurrence positions. Expected status: `PATH_LAPLACIAN_BALL_EXACT_PASS`.

Those finite tests do not prove statements for every order. The analytical proof uses a monic quartic finite-difference identity, a binomial convolution and the weighted-distance optimality certificate, all explicitly given in RESULT.md. These algebraic steps establish the theorem for every integer in its scope. The original graph is unweighted and the Euclidean embedding fixed; no assertion about other embeddings or independent validation is made.
