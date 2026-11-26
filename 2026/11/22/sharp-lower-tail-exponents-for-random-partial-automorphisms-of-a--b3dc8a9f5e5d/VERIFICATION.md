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

A path subset of rank r has c runs, with c-1 compulsory vacant gaps, so c<=min(r,n-r+1)<=h_n, also valid for the empty set. For a fixed ordered pair of subsets, an induced isomorphism permutes equal-length components and chooses their orientations, yielding at most 2^c c! maps. The total count is at most 4^n 2^h_n h_n!, and a fixed maximum independent set supplies h_n! permutations. The same argument at c<=k bounds the component event by 4^n 2^k k!, and hence bounds the rank event from above. Permutations of a fixed independent k-set give the numerator lower bound k! for both, also at k=0. The resulting 8^n bounds give both exponents by Stirling, and the size estimate by the same denominator bounds. Low rank forces low c; high rank does too via c<=n-r+1. Combining that inequality with E=r-c gives 2c+E<=n+1 and the epsilon/2 coefficient in the edge-count bound. Removing all nonsingleton runs deletes at most 2E vertices on either side and leaves matched singleton vertices. These arguments use uniform sampling over maps, not uniform sampling over supports, and prove the all-size probability bounds. The uploaded verifier was inspected without execution. The separate /workspace/branches/review-replay.py checks exact finite bounds using a gap-composition count, including initial counts 2,7,22,71,252,935; this is not used to prove the limit.

## originality

PASS

The exact finite monoid order, run-type factors and rank-refined counts are prior and not credited. The supported distinct result is the sharp simultaneous n log n probability law for component and rank deficits under uniform maps on paths, including typical near-independence of supports. It interprets the factorial component symmetry asymptotically; the cited finite enumeration does not provide the requisite uniform tail estimates as stated. Crown asymptotics and the distinct same-day biclique rank/extension result concern different induced-isomorphism families and events; only their indexed content was available for the finer comparison.

## value

PASS

Rank is the natural size filtration and run count measures the supply of permutable induced components. The sharp linear-deficit exponents for both show quantitatively which maps dominate the classical exact enumeration. The match of two deficits on the factorial scale and the resulting near-independent supports give meaningful typical structure, not just log order or another finite count. This neither asserts exact independence of the original random supports nor gives sublinear fluctuations or the exact upper-tail rates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
