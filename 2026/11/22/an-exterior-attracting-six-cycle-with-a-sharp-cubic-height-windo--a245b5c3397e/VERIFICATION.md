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

Frozen proof line 38 incorrectly asserts strict contraction for each displayed affine-coordinate slope: b_01=2/(1+q)>1 for q<1. The full corrected RESULT.md under /workspace/repairs/1/ fixes this justification using unit tangents and cancellation of coordinate scales on each return. All lines are pairwise nonparallel for h>0, so every nonconstant cyclic branch itinerary has a strict affine return; repeated shorter words cannot encode primitive multiples. At a vertex labeling by the incoming branch works because the other incident line is at distance zero. Ties are fixed and cannot occur on a six-cycle. Independently reconstructed the projections from line normals in x,y/h coordinates and solved all strict squared-distance inequalities by exact univariate polynomial sign sets for all nine primitive cyclic words without quotienting by reflection: python /workspace/branches/audit1.py. Eight are empty, and precisely 012021 has Interval.open(CRootOf(q^3+q^2-1,0),1). The cubic is strictly increasing on q>0, with opposite signs at 3/4 and 4/5. On this interval the listed affine coordinates give distinct base points, one interior and one beyond-apex point on each inclined line, and no vertices. Reflection gives the three-step shift. Exact differentiation reproduces the stated multiplier; strict branch inequalities and modulus <1 give a locally attracting return. Both endpoints are excluded by an equality in a switching gap, not by a numerical test. No theorem, phase-space scope, or evidence checker was changed.

## originality

PASS

The repaired proof supports the same distinct claim: the complete primitive period-six census on unbounded supporting lines and the two exterior points. Credit Everett for the defining map and convergence, and the earlier exact other-period records for their counts and coexistence inputs. No demonstrated prior coverage of the distinct six-cycle result was identified in the bounded comparison.

## value

PASS

A sharp all-height census for a natural missing primitive period on a published map exposes what the commonly plotted bounded boundary version omits. Existence at just one sample would not determine the exact cubic onset and tie endpoints or the region where this additional attracting period coexists with the already known four-cycle. The proof repair preserves this result, rather than trying to rescue an intrinsically narrow or already covered computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
