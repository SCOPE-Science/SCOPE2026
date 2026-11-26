---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Use independently sampled vertex probabilities with independent outgoing Bernoulli trials conditional on the probability at their common source. A path uses a different source for each edge, giving p^depth. An ancestor-descendant pair has joint indicator equal to the deeper indicator. For an incomparable pair, the only repeated source in the two paths is their lowest common ancestor, so the joint probability is E[Theta²] times p raised to the combined distinct-edge count minus two. This proves the baseline covariance formula and the variance excess after subtracting the deterministic-source case. Grouping pairs by lowest common ancestor gives the product of the two child-subtree sums for each child pair, multiplied by p to the ancestor depth. All terms are positive and at most 2, and there are at most binomial(n-1,2) pairs. No incomparable pair means an endpoint-rooted path; all nonroot pairs incomparable means a center-rooted star, where every exponent is zero. For convex order, condition on all other potential trials in the oriented tree. Reachability of the selected vertex does not depend on its outgoing trials, and its disjoint child subtrees have fixed nonnegative weights in the conditional count. The diagonal second derivative in the common Bernoulli parameter sums ordered mixed differences of the convex function over pairs of child activations, all nonnegative. Single-vertex replacements thus prove the order for the final count. The two-point abstract law attains the upper bound. The scope phrase about a supremum only in the finite-duration representation needs the qualification B>0: when B=0 the bound is attained by every law. At n=2 the whole count is 1 plus a Bernoulli(p) trial. Both supplied exact-rational scripts were read, not executed; the reported checks through n=6 corroborate finite cases, not the theorem for arbitrary size.

## originality

FAIL

The earlier Resultary finding 1d4b8a70bdd4 gives the same final-count convex order, mean, exact variance excess and weighted incomparable-pair index with the same path/star extrema. The endpoint-inclusive abstraction is the continuous closure of that result: the same mean and convex order can be preserved in the approximation. The n=2 addition is just one Bernoulli trial. The earlier record b769c52b1efb gives the variance formula directly even on the closed interval.

## value

FAIL

For the abstract probability problem, the final-count convex order and exact variance sensitivity are meaningful observables. Here those same results are already present, including the sharp topology classification. Admitting a probability of one gives boundary attainment by a routine closure of the earlier model; n=2 and re-expressing the baseline do not constitute a separate finding of comparable scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
