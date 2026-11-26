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

For 2<=r<n and r<=k<n, with [n] retained, the zero stage is the cone on the rooted downset. Exterior rank r enters at 1; an exterior rank-(r+1) point has weight r+1 if it contains exactly one outside element, and r+2 otherwise. A rank-(r+2) point containing an outside element has at most r+1 elements in the center, so its downset difference is at least binom(r+2,r)+1; passing to a subset containing an outside element yields the same lower bound for every higher rank. In the early window any chain touching the exterior is at most an edge because nothing inside the center lies above an exterior point. The core is a contractible CW subcomplex, and its compatible collapses give a graph at each stage. At r+1 and for each chosen exterior element there are binom(k,r) new points and binom(k,r-1) adjacent exterior rank-r points; each new point has r+1 incident edges, one to the core. Subtracting the increased vertex count from the edge count gives (k-r)binom(k,r-1) circles per exterior element, and exactly i=d-a rank-r points remain isolated. At r+2 the rank-r Johnson swap paths through rank r+1 prove connectivity; if E is the number of exterior rank-(r+1) points, the quotient has d+E+1 vertices and (r+1)E edges, giving c=rE-d. The old cycle lattice embeds and is saturated because a nonzero multiple cannot have support only in old edges unless the original cycle already does. This proves the integral split injection. On H0 use the class of S and, for each exterior rank-r point v, the difference [v]-[S] until it merges; these form integral bases at every stage. The differences die precisely at r+1 and r+2 in the claimed multiplicities. Each later entering point contains an already present rank-r subset, so there are no more births. The argument includes k=r and n=r+1, when some multiplicities or circle ranks vanish.

## originality

PASS

Credit the general degree-zero birth theorem and the earlier full all-degree nonempty-Boolean barcode. The distinct contributions are the early integral graph homotopy and map, and the exact degree-zero deaths for r>=2 with downsets computed after truncation. No inspected result covers those claims.

## value

PASS

Removing the bottom ranks of the Boolean inclusion poset is a natural change of finite space, not a numerical slice of the full-Boolean result. It gives two distinct component-merger thresholds tied to how many elements lie outside the center, an integral cycle lattice with a controlled inclusion, and a complete coefficient-independent H0 invariant across all thresholds. These are explicit useful refinements of general birth-only results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
