---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For finite K_{a,b}, each A-A walk compresses into core two-step segments of cost at least M_{ij}; conversely concatenated argmin segments attain the metric closure, giving exact equality. At one peripheral vertex, P(two-spoke sum<=t/sqrt b)=t²/(2b)+O(b^{-3/2}), and overlap of two distinct pair events is O(b^{-3/2}) since at least three independent spokes are small. Independence across b periphery sites yields joint upper-orthant convergence to a product Rayleigh survival function; finite-dimensional path closure is continuous. For a marked periphery vertex, W=min_a Exp(1) is Exp(a), and distances lie between W and W+core diameter, similarly two marks W_l+W_h and +diameter. Excluding finitely many tags leaves asymptotically the same Rayleigh pair minima and independent marks; chance a tagged vertex changes scaled pair minima is O(1/b). Reconstructed the proof and independently checked core closure/peripheral inequalities on 384 random integer-weight graph instances.

## originality

PASS

No matching fixed-a growing-b joint Rayleigh-edge metric closure and independent marked exponential-star limit found. Gerke–Mezei–Sorkin full article addresses many edge-disjoint shortest paths on complete graphs as n grows, not the unbalanced bipartite two-scale joint geometry. Ross 2012 provides general finite-network joint shortest-path distributions from one source, potentially enough to specialize, but full paper unavailable; an unavailable plausible source is documented as risk rather than automatic failure. Best-of-knowledge PASS, with this source pending human-access resolution.

## value

PASS

The result pinpoints a nontrivial two-scale decomposition: magnified core distances retain correlated metric closure from independent Rayleigh edge costs, while finitely many unscaled peripheral distances form an independent exponential star. This is a natural joint limit beyond an isolated expectation or elementary shortest-path estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
