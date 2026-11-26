---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For anchor overlap s, the size n-2r+s of the ground-set complement of their union gives N11. For a mixed pattern one subtracts common neighbors and also the other anchor when s=0. For pattern 00 one uses inclusion-exclusion and removes both anchors if s>0. N11 increases with s. Among s>0 the mixed minimum at s=r-1 is M by Pascal's identity; at s=0 its excess over M is at least binom(n-2r,r-1)-1>0. For pattern 00 the jump from s=0 to 1 is binom(n-2r,r-1)-2>=0 and later values increase. Thus the least witness-set size is m, and deleting precisely such a set leaves its two anchors and destroys the pattern; no smaller deletion can do so. The graph after a deletion below threshold has at least three vertices (a minimizing witness set already excludes its two anchors). A three-pebble move then needs at most two anchors; the extension property supplies a fresh match for arbitrary rounds, with equality moves matched directly. Each missing pattern is detected by its universal-pair/existential-third sentence, so the threshold holds at unrestricted quantifier depth for counting-free FO3. The r=2 table follows by substitution. For fixed r the common-nonneighbor count has leading term r^2 binom(n-2r,r-2), by choosing exactly one point from each disjoint anchor. All three bottlenecks occur, e.g. (n,r)=(6,2),(14,3),(8,2) for J,M,Z respectively.

## originality

PASS

The extension-property/pebble-game bridge and witness-set deletion principle are general; they are not novel. The distinct result is the exact ordinary Kneser minimum across the four third-vertex pattern counts, including the competing mixed and common-nonneighbor bottlenecks. The closest resilience results use different vertex families or different adjacency.

## value

PASS

Two-point extension is the exact local requirement for these finite counting-free three-variable substitutes for the random graph. The natural robustness question has an exact answer, not just a sufficient bound: sparse common neighbors, asymmetric witnesses, and common nonneighbors can each determine failure. The minimum certifies a usable deletion budget, with a concrete matching way to lose the property and a different eventual obstruction for fixed r.

The dated certificate retains the supplied scientific assessment, sources and limitations.
