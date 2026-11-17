---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The theorem is mathematically correct in the full-choice adaptive offered-vertex model. For triangle-free connected components, components with at most two edges have 0 or 2 closable vertices, while every component with at least three edges has v<=e+1<=4e/3. Thus a(G)<=4e(G)/3, with equality on disjoint 4-vertex paths. The one-step conditional success probability of any builder is at most 4j/(3n), and the product lower bound has logarithm -2m²/(3n)+O_L(n^-1/2). The constructive reserved-P4 strategy creates a full template per three productive offers, loses expected O(1) productive rounds by time O(sqrt(n)), and obtains the matching uniform error. Independent exhaustive simple-graph checks corroborated the exposure bound. This is an asymptotic optimal probability law, not finite-n exact optimality.

## originality

FAIL

A complete published theorem covering all fixed simple cycles in exactly the same full-choice, with-replacement, online graph process establishes survival exp(-(ell-1)x²/(2ell-3)) with the same O_{ell,L}(n^-1/2) uniform window and a matching (2ell-2)/(2ell-3) exposure bound and path-template strategy. Substituting ell=3 yields exp(-2x²/3), the 4/3 exposed-vertex ratio and P4 construction verbatim. This is a direct mathematically dominating published statement; the same-day UTC posting order is unknown and not asserted.

## value

FAIL

The triangle constant and extremal P4 argument are interesting and correct in isolation, but the entire submitted final theorem is a direct special case of the full fixed-cycle theorem, with no distinct limitation, stronger rate, or independent invariant. The package does not supply a separate un-covered mathematical advance; reproducibility alone does not confer independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
