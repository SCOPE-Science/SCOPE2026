---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Read full RESULT.md and the exact small-instance checker. The only perfect matchings are cycle alternations A,B, a unique single-chord matching for each odd chord, and possibly one joint two-chord perfect matching. An unused chord becomes a simplicial cone vertex. If even chords have opposite parity and interlace, the Alexander-dual facet nerve has triangle boundary; for two odd chords it is a tetrahedron boundary or tetrahedron glued to cone over a four-cycle, both S^2. Alexander duality on 2t+2 edge vertices puts unique free homology in degree 2t-2 or 2t-3. For t>=4 complete two-skeleton ensures simple connectivity, and for t=3 missing perfect-matching triangles have conable boundaries, so Hurewicz/Whitehead gives integral homotopy spheres. As an independent check, wrote a separate recursion enumerating perfect matchings from the 2t vertex set, checked complete dual nerve f-vectors for all 36,190,595 pairs at t=3,4,5: cone 27/142/440, even-crossing sphere 6/20/50, two-odd sphere 3/28/105. Finite enumeration corroborates but is not the t-uniform proof.

## originality

PASS

Prior exact even-crossing short-chord all-t case is fully covered and explicitly excluded from the new contribution; no accessible theorem has been shown to imply this entire odd/any-two-chord homotopy classification. A close 2026 primary full text remains inaccessible and priority is bounded.

## value

PASS

The two-chord perturbations of a cycle form a canonical finite structural family, and integral homotopy changes nonmonotonically with chord parity and endpoint interlacing. Completing the full all-t two-chord phase diagram, including odd chords sharing a vertex, is a mathematically motivated classification not mechanically implied by a single previously computed crossing case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
