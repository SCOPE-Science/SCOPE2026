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

The self-contained `verify_net3.py` generates the three complete integer Laplacians from the ternary Latin square and the within-class concurrence rule. It verifies the 36-edge counts, the respective vertex counts 18, 19 and 21, the corresponding genera 19, 18 and 16, and minimum vertex valence at least three. It independently enumerates the 36 pairwise intersections of each of two rational-coordinate representatives derived from the published equations, obtaining exactly 9 triple/9 double and 10 triple/6 double points. The Ceva realization is checked separately by enumerating every pair of its nine lines over the exact quadratic field with a primitive cubic root of unity, obtaining precisely twelve triple points and no double points.

For each graph, it checks an exact characteristic polynomial and reduced determinant. Two different root deletions yield matching integer Smith forms. An independent, explicit local row–column algorithm works modulo \(3^9\) and \(5^9\), with every pivot valuation strictly below nine. Its exponent multisets reproduce those Smith forms, and exact determinant factorization certifies that no other prime can occur. These are exhaustive calculations on the stated finite integer matrices; a floating-point spectrum or sampled congruences alone is not used to infer invariant factors.

Command: `python verify_net3.py` (Python 3 with SymPy). The successful completion marker is `THREE_NINE_LINE_NET_INTEGRAL_BOUNDARIES_OK`.

The classification of realizable net incidences is taken from a published primary theorem; the verifier does not independently reprove that theorem. The Néron component-group interpretation uses a published general theorem and requires a proper regular split semistable smoothing with all node thicknesses one. The distinct resolved boundaries are not claimed to form a flat family. Independent mathematical audit has not been performed.
