---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Independently reconstructed the fiber classification. With no fiber over the center, the map is an injection to leaves or has exactly one doubled fiber consisting of the source center and a leaf. A center fiber {0} allows only singleton leaf fibers; a center fiber {j} with j a leaf permits at most one extra fiber, namely {0}; a center fiber {0,j} permits none. These cases give all five terms of R including the empty map. Idempotents fix the image pointwise; if the image contains no center, only the source center can additionally map into the fixed leaf set, while a doubled center fiber gives the extra n rank-one idempotents. For regularity, restrict any generalized inverse to the image to obtain a continuous section, and conversely use such a section for fgf=f. A doubled leaf fiber allows a leaf representative; center-image cases allow an edge-respecting or one-point section. The forced inverse of an injection to leaves fails exactly when it takes two target leaves onto a source edge, equivalently when the domain contains the center and another point. Counting those domains and injections gives B. A separate exhaustive partial-map/section check matched R, E, B and the obstruction in all 25 rank strata for 1 <= n <= 5, including K2, where all nine maps are regular. Replay: python3 /workspace/branches/7a5cc781-1578-4fcc-a63f-131dd1a96ffd/independent_star_census.py 5. This is bounded corroboration, not the unrestricted proof.

## originality

FAIL

A distinct indexed Resultary record explicitly states the same three rank enumerators and nonregularity criterion for the full range n >= 1. Coefficient extraction converts it to the frozen formulas without a new mathematical result.

## value

FAIL

The rank-resolved census is a natural invariant, but this record repackages the already available full census and elementwise obstruction. It adds no new boundary case, structural consequence or exact statistic over that coverage; another finite check does not create a distinct scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
