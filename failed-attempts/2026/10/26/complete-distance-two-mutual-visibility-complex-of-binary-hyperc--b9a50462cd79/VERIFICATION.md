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

The local criterion is diameter at most two and exclusion of the full square containing both geodesic midpoints of any selected distance-two pair. Normalize such a pair to 0 and e_1+e_2. With one midpoint selected every allowed point is in the ball about that midpoint; with neither, the nonzero points are weight-two supports which meet pairwise. If there is a common coordinate they yield a ball, and otherwise the edges must be exactly a triangle, giving a parity tetrahedron. The case with no distance-two pair has size at most two and is in a ball. Leaves in a ball have an alternative midpoint outside it, and both midpoints of each tetrahedron pair have the opposite parity. A tetrahedron is not contained in a ball, and distinct balls intersect in at most two points. Hence both kinds are facets (including d=3), and ball subfaces of size at least three are counted once. The number of distinct parity tetrahedra is 2^(d−2) times binom(d,3); the coefficients for sizes 0, 1, 2 follow by the direct unordered pair count. The independent geodesic test exhausts Q_3 and Q_4 and tests Q_5 up to size four; coefficient vectors are (1,8,24,32,10), (1,16,80,160,96,16), and (1,32,240,640,560) through size four, respectively. Direct augmentation gives facet counts {4:10} for Q_3 and {4:16,5:16} for Q_4. Replay: branches/4eb7a126-98b5-4c1f-a9ba-f27964bcd795/independent_check.py and independent_check.log. This is finite corroboration; the proof establishes all dimensions.

## originality

FAIL

The exact diameter-two anticode face and facet classification in distinct catalogue record 3ed418f43bd2 covers the entire frozen result by deletion of coordinate squares, the only diameter-two anticodes that violate 2-visibility. The broader q-ary catalogue entry 00ff5b1e991c also gives the size counts before that deletion. Their displayed path dates follow the frozen date; this shows stronger existing coverage as of review, not earlier publication or proven direction of provenance. The earlier 205d6ab586a0 already gives the scalar maximum.

## value

FAIL

The complete shape of this natural complex is useful in principle, particularly the small maximal faces missed by the extremal number. As a separate claim against the existing stronger catalogue result, the exact visibility data are a one-family deletion with no uncovered substantive remainder. No repair is warranted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
