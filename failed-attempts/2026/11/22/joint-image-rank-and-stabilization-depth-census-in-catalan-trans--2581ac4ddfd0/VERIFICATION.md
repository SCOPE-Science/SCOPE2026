---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Each fixed point starts a contiguous component interval, and monotonicity and regressivity keep parent edges in that interval. Successive inverse images of its root are initial segments of the block, so generations are contiguous; within each generation the order of parents is nondecreasing, giving the unique breadth-first plane-tree labeling. Conversely, a concatenation of such labelings gives a nondecreasing regressive map. Stabilization depth is the maximum component height and rank counts roots plus internal nonroots. The stated geometric-sequence recurrences therefore mark height and rank correctly, including singletons and the identity. The first d vertices of a deepest path all lie in the image. At d=r≥1 they exhaust it, so the forest is one tree with r consecutive internal vertices. The first r−1 each have two ordered sequences of off-spine leaves and the last has a nonempty leaf sequence; the generating function is x^{r+1}/(1−x)^{2r−1}. This gives the binomial and strict positivity in the claimed range. An independent enumeration of all 6917 maps through n=9 matched the coefficients and all boundaries.

## originality

FAIL

The all-coefficient claim is a direct specialization of the Roblet–Viennot height-specific peak/nonpeak Dyck path weighted continued fraction, applied to the already published Catalan-map forest correspondence and image-vertex criterion. The sharp boundary is the leading-in-rank coefficient of the difference between two consecutive truncations; it follows by a simple telescoping of the same continued fraction. This is demonstrated statement-level coverage, not a verdict based on inaccessible potency papers or on the known univariate marginals.

## value

FAIL

The two invariants form a natural finite census and the formulas are useful as an exposition. But the precise law and the rank-equals-depth count are both mechanically obtainable from the previously established flexible Dyck generating function and the published image/forest correspondence. No additional nonmechanical claim remains at the frozen scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
