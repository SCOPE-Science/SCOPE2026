---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The rooted integer-potential gauge for A_(n-1)^* is valid. Any feasible labeling with total range>m has extrema at a deleted edge. For a deleted star the distinguished vertex is one extreme and the opposite extreme among k nonneighbors; at gap m+h all r=n-k-1 core coordinates lie in [h,m], while k nonneighbors lie in [h,m+h] with a maximum. Counting gives the correction 2((m+1)^k-m^k) sum_(s=1)^m s^r, with baseline (m+1)^n-m^n. Leading coefficient and Gram determinant 1/n give Euclidean volume. For a matching, missing extreme pair is unique, yielding 2k sum s^(n-2). The binomial inequality proves strict all-m comparison. Independent rooted enumeration matched n,k,m=(4,2,1),(4,2,2),(5,2,1),(5,2,2),(6,3,1). m=0 and n-k-1>=1 addressed.

## originality

PASS

Prior graph-polar bounded-potential counts and a complete matching-deletion theorem are known. The present all-k deleted-star formula, as a different overlapping edge pattern, is not implied by the matching expression without additional combinatorial argument; strict comparison needs evaluating both structures.

## value

PASS

Natural family with a meaningful deletion-pattern comparison at identical k, classifies all two-edge deletions, and gives exact full Ehrhart/Euclidean volume for every admissible n,k, not a small arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
