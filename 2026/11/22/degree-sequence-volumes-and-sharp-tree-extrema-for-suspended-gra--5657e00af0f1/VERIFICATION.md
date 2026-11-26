---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For prescribed hub correlations x_i, subtract the hub component and normalize the residual vectors. The edge residual correlations can be chosen independently in [−1,1]: root the tree and construct a new child residual using its parent and a fresh perpendicular vector. A zero residual at x_i=±1 simply forces incident edge correlations to x_i x_j; choose any auxiliary unit residual vector there. Each of the n−1 edge widths is 2 sqrt((1−x_i²)(1−x_j²)). Fubini groups the powers as d_i/2, and rescaling all 2n−1 coordinates multiplies by 2^{−(2n−1)}, leaving 2^{−n} times the J product. Strict Hölder gives strict convexity of log J_d. Nonnegative excess degrees sum to n−2; their sorted vector lies between the 0/1 vector with n−2 ones and the concentrated vector, in the majorization order. Strict equality yields only path or star. The sample n=4 and n=5 values and the constant in the ratio follow by J_1=π/2, J_2=4/3 and J_{n−1}~sqrt(2π/n). At n=2,3 the two trees coincide up to isomorphism.

## originality

PASS

The known triangular-book formula is exactly the star specialization and is expressly credited. Inspected sources do not cover the evaluated coordinate volume for arbitrary suspended trees, the equality for repeated degree profiles, or the sharp tree extremal comparison. The decision is bounded to the evidence found.

## value

PASS

The formula removes the need to integrate a high-dimensional PSD projection separately for each labeled tree and shows exactly how the degree multiset controls its volume. The uniqueness of the two extrema and the sharp exponential contrast quantify a structural difference among trees of identical order and ambient dimension. The novelty/value is not the familiar leaf completion or the book formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
