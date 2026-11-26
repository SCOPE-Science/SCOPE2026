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

Each target height v fixes x=−(v+dy)/h. The remaining graph g_v(y) tends to minus and plus infinity at the respective ends, so it is onto. It is concave left of 0 and convex right of 0. For v≤−K the levels in increasing y-order are B at the crease and L at the active minimum; for −K<v<K they are U,B,L; for v≥K they are U,B. Counting open monotone intervals plus each endpoint once yields the claimed strict three-root intervals, two roots at the interval endpoints, and one outside. At v=±K the zero-slope vertex is at the crease and is counted once. In the middle region at u=B there are two nonzero roots in addition to y=0. Completing squares gives the stated quadratic separations. Off the crease det DF=h g_v′, so regular triples have signs +,−,+ and regular singletons have positive sign. For the origin the nonsmooth term x|y| is of second order at (0,0) and the determinant there is −ad; the two remaining determinants are +ad. Thus the signed count applies to regular targets, not to the nonsmooth central switching-image targets away from the origin. A separate exact rational monotone-interval count corroborates representative thresholds and fold/crease levels; the uploaded root solver uses floats and is only regression evidence.

## originality

PASS

Zhou et al. define exactly this map family and study this sign sector in forward dynamics, without giving this inverse classification in the inspected relevant sections. General critical-curve theory and related exact counts explain the vocabulary and generic pair-merger mechanism, not these particular crease and fold levels or their changes across v=±K.

## value

PASS

Global state-reconstruction ambiguity is a natural invariant of this published map. The count at every target, the merger thresholds, and the crease segment that lies inside rather than on the three-sheet boundary distinguish the geometry more sharply than detecting a local fold or giving a single multi-preimage target. The complete classification has a use in backward observation; it is not evidence about encryption or forward attraction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
