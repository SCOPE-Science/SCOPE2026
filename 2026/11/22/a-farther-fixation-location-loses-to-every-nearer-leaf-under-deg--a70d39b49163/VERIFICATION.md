---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Uniform selection among mutants is the jump chain of independent rate-one clocks, with null events retained. Thinning by destination gives independent edge clocks of rate 1/deg(source). On the rooted tree only the parent can first occupy a child, so independent outward waiting times can be started when each parent is reached. The far time is Gamma(3,1/2); each short terminal time is the same hub wait plus an independent Exp(1/(k+1)) wait. The hub wait must not be treated as independent across short leaves. Only leaves other than the root can finish last; ties have probability zero. Integrating out the hub wait gives the stated binomial–Laplace expression, including at jb=1/2 where -a L'(a)=3/16. Symmetry then gives the near-leaf probabilities. Independently recomputed with labeled-set states and exact fractions: at k=4 the far probability is 40122073072/243729729243, a near leaf has 203607656171/974918916972, and near minus far is 43119363883/974918916972. Replay: make adjacency lists, memoize on the occupied bitmask S, return the indicator of the far leaf when exactly one vertex remains, and otherwise average over S union {v} with weights sum_{u in S adjacent to v} 1/deg(u), normalizing by their sum. The labeled recursion visited 67 states at k=4 and also checked k=1,2,3,5,10. The all-k claim follows separately by bounding the conditional product by (T/(k+1))^k; the gamma moment is 2^(k-1)(k+2)! and Stirling yields O(k^(5/2)(2/e)^k). An open set of clock realizations gives q_k>0 for each k. The conclusion is reversal at k=4 and for sufficiently large k, not for all k; the exponential statement is an upper bound, not an exact decay rate. The frozen checker was inspected as text.

## originality

PASS

Best-of-knowledge pass for the explicit rooted-tree reversal and all-k formula/separation, not for the fixation-location statistic, the generic computation method, or the observation that a farthest vertex can lose a ranking on some graph.

## value

PASS

The original distance intuition has a particularly clean failure on a tree: the path to the uniquely farthest leaf is longer, yet the fixed reproduction budget is divided among the hub's children, making each nearer leaf more likely to finish last. The exact nine-vertex comparison and the ratio diverging along a family distinguish a robust mechanism from a distance tie or a tiny finite fluctuation. Useful as an exact check on fixation-location methods in this infinite-selection model, not as a finite-fitness or empirical prediction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
