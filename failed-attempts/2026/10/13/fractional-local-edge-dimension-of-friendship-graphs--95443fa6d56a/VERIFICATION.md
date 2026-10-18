---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For every pair of outer vertices u!=v, center edges cu,cv are adjacent and their local resolving neighborhood equals exactly {u,v}. Therefore any FLED weight satisfies all pair inequalities g(u)+g(v)>=1, forcing outer weight sum >=r. Conversely center zero and every outer vertex weight 1/2 satisfy all other adjacent-edge neighborhoods (weight r-1/2>=1), proving optimum r. At equality every pair constraint must be tight and all 2r outer weights equal 1/2, uniquely. Independent direct distance-neighborhood checks for r=2..8 confirmed formulas; proof holds for every r>=2.

## originality

FAIL

FAIL: a PUBLISHED earlier Resultary theorem, “All minimal fractional edge resolvers of friendship graphs” (2026-10-04), already proves that every global fractional edge-resolving constraint is EQUIVALENT to exactly the complete family of pair inequalities g(u)+g(v)>=1 for all outer u!=v, and the UNIQUE optimum is center zero and every outer weight 1/2. Its proof identifies all these necessary constraints as pairs of the adjacent center-spokes cu and cv. The local (adjacent-edge-only) feasible LP contains every prior pair constraint and is contained between this exact pairwise polytope and global feasible system; hence the local and global feasible polytopes are IDENTICAL. The present local optimum and uniqueness are an immediate logical corollary of the earlier complete feasible-polytope theorem, regardless of different invariant name. This is decisive known stronger coverage, not an access-uncertainty fail.

## value

FAIL

FAIL for the submitted original claim: once the prior exact feasible-polytope classification is applied, the local equality and optimizer follow automatically from retaining its already-adjacent generating constraints. There is no independently unknown exact fact, new classification, novel counterexample, or motivated gap beyond a short specialization of a dominating prior theorem. The correct calculation and prior global-vs-local terminology distinction alone cannot supply standalone mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
