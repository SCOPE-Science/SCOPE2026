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

# Verification record

The proof in RESULT.md is analytic. Its critical ingredients are the eigenvalue multiplicities of the page-difference spaces, the determinant and trace of the two-dimensional odd block, strict convexity of the trace inverse, the negative derivative ruling out unpurchased middle edges, and the bridge complementary-slackness condition.

Run the included `verify.py` with Python 3.10+; it uses only the standard library. The checked execution returned:

```
VERIFY_OK 124
M2 dcrit 99/35 ; limiting m*dcrit 5.598076211353316
```

The program reconstructs the full graph Laplacian, inverts the shifted Laplacian over exact rational numbers, checks the Kirchhoff-index expression at several positive and boundary conductance choices, checks the middle-edge descent formula, calculates the unique boundary ratio, and checks a collection of nonsymmetric feasible competitors. A separate optimization stress test across \(m\in\{2,3,4,6\}\) and multiple prices reproduced the predicted support regimes; solver outputs were not used as proof of global optimality.

The finite tests cannot establish a theorem over all integers and real prices, nor can literature searches establish universal novelty. The symbolic algebra and convex optimality argument in RESULT.md supply the claimed infinite-domain result. No external or independent mathematical verification has been performed.
