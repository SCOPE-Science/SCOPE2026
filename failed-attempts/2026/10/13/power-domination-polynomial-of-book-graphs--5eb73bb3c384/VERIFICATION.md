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

A selected spine vertex observes both spine vertices and at least one nonspine vertex on each page; each missing page vertex is then forced. Without a selected spine vertex, a hit page is fully observed by the initial step and supplies whichever spine vertex is not yet observed. If exactly one page was missed, each spine vertex can force its neighbor there. For two or more missed pages both spine vertices have at least two unobserved neighbors there and no observed nonspine vertex is adjacent to a missed page, so none can be entered. The empty set fails. With q=2x+x², the disjoint cases count as q(1+x)^(2n), q^n and n q^(n−1). At x=1 and in degree one this gives the claimed total and minimum layers. At n=2 the criterion is exactly nonemptiness; at n=1 the formula would add a spurious constant, so the exclusion is necessary and C₄ has all nonempty sets. An independent replay exhausted 349,504 subsets for 2≤n≤8 and matched the classification, all coefficients, total counts and singleton counts. The case analysis, not the finite replay, proves the result for all n.

## originality

FAIL

A distinct, earlier-dated indexed record, 646ff77569c3, states the exact same all-orders criterion and polynomial, with matching totals and minimum layers. The change of parameter symbol does not distinguish the claims. The comparison shows exact coverage without adjudicating external publication priority or provenance. Incomplete access to literature and finite tables is not the failure reason.

## value

FAIL

An all-cardinality power-domination enumerator for this natural graph family is a meaningful kind of result. Here that exact enumerator and structural explanation are already covered by a distinct index record; confirmation on more finite orders does not contribute a new theorem or exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
