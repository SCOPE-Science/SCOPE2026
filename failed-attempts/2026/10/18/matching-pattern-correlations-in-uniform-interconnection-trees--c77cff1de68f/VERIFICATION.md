---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The quotient has weight product_i (n_i)_(deg(i)) under uniform sampling of physical matchings. Contracting a prescribed index matching in the weighted Prüfer sum gives (sum_i x_i)^(k−r−2) times product_(i,j in F)(x_i+x_j); singleton factors cancel. The chosen endpoint indices are distinct, so the falling-factorial evaluation consumes one unit of capacity at each chosen endpoint and leaves (M−r)_(k−r−2) completions in the aggregate. The unrestricted evaluator is (M)_(k−2); the ratio yields the displayed probabilities, and subtraction gives the stated covariance. There are at least two contracted components, and M≥k−2≥r. Zero-weight pairs are impossible; covariance denominators are only used when k≥4. An independent derivation by contracting the physical graph is given below. The two finite test methods in the supplied script were inspected, not executed.

## originality

FAIL

The cited prior exact counting theorem already yields this inclusion law as a direct corollary: after fixing the actual edges above the prescribed pairs, delete their used endpoints and merge the paired parts. The remaining problem is precisely another instance of the same complete multipartite interconnection-tree count, with no additional restrictions. The product, covariance and conditional law follow from that count by cancellation. This is an implication finding, not a claim that the probability display appears verbatim in the paper.

## value

FAIL

Positive rather than zero covariance is a useful contrast between two sampling laws. As a distinct scientific contribution, however, the proposed exact matching invariant is mechanically implied by the pre-existing arbitrary-profile count: fixing and contracting the required edges stays in exactly that class, with explicit residual capacities. The conditional and covariance readouts need no further result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
