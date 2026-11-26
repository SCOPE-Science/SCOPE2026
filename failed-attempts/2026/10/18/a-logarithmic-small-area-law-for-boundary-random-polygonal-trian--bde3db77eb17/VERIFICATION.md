---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The frozen proof's distinct-side zero-set classification (RESULT.md line 37) is false and leaves out configurations needed for its compactness argument. For example, in the triangle with vertices (0,0),(1,0),(0,1), select (1/2,0) on the bottom edge and select (0,0),(1,0) on its two neighboring edges. This is a zero-area triple on three selected sides with no coincidence. Zero endpoint probability does not justify ignoring its neighborhoods in a sublevel-volume bound. The theorem itself is not contradicted. The atom follows from collinearity on a common supporting face, not from coincidences. The incident repeated-edge integral is exactly 2x log(1/x)+x^2 for x=2t/(ab sin theta) in (0,1); the assignment weight 3a^2b/L^3 gives the stated constant. Nonincident pairs have altitude bounded below. A valid repair of the distinct-side estimate would include both coincidence lines and the lines with the middle point on the supporting side and its endpoints occupied from the neighboring sides. On a coincidence line at V, the two incident-direction derivatives cannot both vanish since the third point is not V. On the omitted line, writing the middle point as (aw,0) on a side of length a, the inward arclength derivatives of signed doubled area at the other two points are a(1-w)E_y and aw F_y, with both inward heights E_y,F_y positive. Thus at least one derivative is nonzero everywhere on the compact zero set. A finite local cover and one-coordinate sublevel integration then give the O_K(t) needed by the theorem. The frozen checker was inspected, not executed; it only checks finite coefficient/atom normalization and cannot establish this bound. No corrected finding is submitted because the unchanged claim is covered in full.

## originality

FAIL

Two distinct indexed findings together cover the entire frozen claim: the November 22 general-polygon record states exactly the atom and small-area law for m>=4, and the October 25 complete boundary-triangle law implies the case m=3. This is demonstrated statement coverage, not a claim about who was first: both catalogue paths are dated later than the frozen assignment path, and neither date ordering nor the mathematical match establishes derivation or historical priority. The narrower 2018 OA paper alone would not justify this failure.

## value

PASS

The theorem itself is mathematically meaningful: it separates a collinearity atom from an angle-dependent logarithmic cusp in a natural geometric sampling law. An independently useful shape or conditional-limit refinement would be a different claim; no such refinement is contained in the frozen record. This intrinsic value does not cure the proof defect or the demonstrated coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
