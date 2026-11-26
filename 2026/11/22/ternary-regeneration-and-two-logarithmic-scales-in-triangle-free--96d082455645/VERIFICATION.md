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

Exchangeability of 2n distinct ranks makes all (2n-1)!! matchings equiprobable, and interval Helly reduces triangle-freeness to sweep height at most two. After the initial opening, at every birth there are exactly three possibilities: close the carrier then open (B), open and close the newcomer (O), or open and close the previous carrier (N). Close the final carrier. This proves the bijection even for the empty code at n=1. Each non-B birth adds one earlier edge, O adds a leaf and N extends the carrier path. Component size k<n has two one-boundary placements and n-k-1 two-boundary placements; at k=n there is no boundary. Bounded finite-dependence gives the fixed-k component LLN. A typical degree is 1, R+J, or 1+R+J equiprobably, where R is the run of O before B/N with P(R=r)=(2/3)3^-r, and the independent terminal-edge indicator J is fair. Its generating function is z/3+(1+z)^2/[9(1-z/3)], giving 1/9, 16/27 and 16/3^(d+2) for d>=2. Truncating forward runs at h gives a finite-dependence variance bound and discarded expectation at most 3^(-h) plus negligible boundary, establishing the empirical rather than just single-vertex law. Deterministically M_n=1+L_non-B and L_O<=Delta_n<=L_O+2. For each run length, a union bound gives the upper limit; disjoint all-success blocks give the lower via (1-p^m)^floor((n-1)/m) tending to zero at m=(1-epsilon)log_(1/p)n. This supplies both constants and the ratio. Replay: python3 /workspace/branches/interval_reproduction.py, which independently computes the intersection graph and tests triangles by triples through n=6 (10395 matchings, 243 accepted at n=6), the bijective code counts, component means, caterpillar cores, and deterministic extreme bounds. The frozen checker actually uses ternary words of length n-1 for n<=10 (longest word length 9); the prose's 'through length ten' does not affect any theorem. Finite replay is not the asymptotic proof.

## originality

PASS

Credit the known matching/path framework and its implications for the height-two count, component distribution and component-run extreme. The distinct finding is the conditional interval graph with tracked survivor identity, giving the explicit empirical degree law and maximum-degree scale and its separation from the component-size scale. This is a qualified statement-level judgment, not a priority certificate.

## value

PASS

Triangle-freeness is a natural rare constraint on this dense endpoint ensemble. Knowing that the result is a caterpillar forest or knowing its component count does not determine how the graph distributes degree. The carrier code gives an exact conditional sampler and identifies why degrees and connected components grow at distinct scales even in the same forest. The result is ensemble-specific and only first-order for extremes, but the separate scales and degree spectrum are useful exact benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
