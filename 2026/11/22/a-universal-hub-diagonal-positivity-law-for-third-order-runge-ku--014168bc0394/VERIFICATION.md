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

Multiplying the generator gives the four displayed entry types. C' is an everywhere negative quadratic, by T2<=S^2 and its negative discriminant. Each hub-leaf quadratic has positive leading coefficient and negative discriminant, also ruling out negative h if steps are interpreted on the whole real line. Independently expanded the leaf-minus-hub quadratic discriminant and -2(S+x+y)^3 C(3/(S+x+y)) in /workspace/checks/scalar_checks.py. The former is strictly negative since the residual spokes have B>0 and 0<U2/B^2<=1; the latter is strictly positive even at B=0 by xy<=(x+y)^2/4. These checks force the hub root to precede both other obstruction types strictly. The normalized cubic at beta is negative since beta>3/2, and at alpha it is positive since r3<=r2<1. A dominant spoke and increasingly many equal spokes converge to the respective strictly crossing scalar cubics; both limits are sharp. The code supplied with the record was inspected, not executed. This verifies the completed polynomial, not any stagewise bound.

## originality

PASS

The supported distinct claim is the universal strict ordering of obstructions on arbitrary symmetric positively weighted stars and the sharp improved lower constant alpha. The same-day bipartite record already gives the exact minimum-of-cutoffs rule and non-reentry for the entire weighted-star class, as well as the same sharp upper constant and the equal-spoke limiting sequence. Credit that overlap explicitly; the blanket prior-work comparison about the lack of an arbitrary-weight degree-three criterion should be qualified. The actual hub-only theorem is not the unsimplified minimum rule and does not follow by merely substituting star degrees.

## value

PASS

The arbitrary-weight hub-first ordering replaces a scan over all local candidates by one scalar cubic, establishes which entry fails without numerical step searches, and yields a sharp improvement uniformly over natural heterogeneous stars. These remaining facts are useful even with the broader bipartite cutoff rule available; the previously covered upper bound and no-reentry are not the reason to pass value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
