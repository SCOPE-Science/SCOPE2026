---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For n>=4, coordinate distances at cyclic separation k are q_k=4R^2 sin^2(kπ/(2n))+[k odd]h^2. Within parity classes q_k strictly increases. For odd n the unique maximal q_n is a perfect matching of opposite indices and q_(n-1) the penultimate; for even n the unique maximal q_(n-1) has separation n-1, gcd(n-1,2n)=1 so the forbidden graph is C_(2n) and q_n is second-largest, with triple-angle inequality ensuring the gap. Inclusive penultimate clique complex is Ind(forbidden graph); Kozlov recurrence proves integral wedge types and at diameter all edges yield a simplex. Independent coordinate enumeration n=4..21 reproduced shell values and exact forbidden graphs. Universal proof is analytic, not finite enumeration.

## originality

FAIL

A simultaneously published more-general theorem for arbitrary twisted two-layer regular n-gons directly specializes to this uniform antiprism case at half-step twist t=1/2 and its unit-edge separation height. Its stated case split gives precisely the matching/cycle, spherical/wedge conclusions and critical diameter. This is a covered special case regardless of nonidentical wording or parameter normalization; extracting the penultimate exact shell from q_k is a short trigonometric computation. Therefore the final claimed standalone result does not pass independent originality as assessed against the published larger theorem.

## value

PASS

Exact terminal Rips homotopy of a uniform antiprism is a natural geometric-topology classification, with a genuine parity and mod-three transition and useful explicit distance thresholds; it is valuable mathematically even though that content is covered by a larger published theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
