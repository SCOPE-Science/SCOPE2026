---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For integers a,b>=3, parallel outdegree-one chip firing sends the two holes one step around disjoint cycles, giving exact period lcm(a,b). CRT identifies their simultaneous omission pairs with i≡j mod d=gcd(a,b), hence the disjoint union of d complete bipartite graphs K_{a/d,b/d}. Firing facets are complements of these edges, i.e. Y(H)=Ind(H)^*. The claimed false-twin suspension lemma follows because link(new vertex) is Y(J) and deletion is a cone based at its twin; cofibration pushout yields a suspension. For d>=2 the base matching dual has d facets whose nerve is boundary of (d-1)-simplex; d=1 explicitly starts with a void geometric realization and first duplication yields S^0. Exactly a+b-2d duplications give S^(a+b-d-2). All stated boundary cases a,b>=3 are handled; finite simulation is corroborative, not proof of the infinite assertion.

## originality

PASS

Best-of-knowledge comparison of precise scientific statements supports originality of the new refinement; all described known premises are credited. The stated unexamined-primary and unindexed-coverage risks remain real.

## value

PASS

Gives an all-parameter topology formula for a natural first disjoint-union operation in avalanche homology, with a genuinely arithmetic gcd dependence instead of a naive product. Exact sphere dimension and simultaneous period give a useful structural test case and interaction between graph dynamics, CRT and Alexander duality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
