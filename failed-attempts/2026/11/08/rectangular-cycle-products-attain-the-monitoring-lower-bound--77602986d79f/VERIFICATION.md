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

The additive distance in a Cartesian product shows that an edge can be monitored only by two points in its own factor fiber: for endpoints differing in both coordinates the two extreme orders of factor moves give edge-disjoint shortest paths, while a one-coordinate path cannot leave its fiber. Thus the m short-cycle fibers force 3m probes. In a cycle of order k≥5 a gap at most floor((k−1)/2) is monitored by its two endpoints on the unique shortest arc; one pair never covers the whole cycle. Each constructed column is a translate of the equally spaced triple. In each row the preimages of selected residues r under floor(nj/m) are consecutive nonempty blocks [ceil(rm/n),ceil((r+1)m/n)−1]; extending cyclically, a gap between blocks at residue distance g has length at most 1+ceil((g−1)m/n). The residue gaps are at most ceil(n/3), hence the bound B in RESULT.md lines 37–46. For m≥11 use ceil(m/3)+1≤floor((m−1)/2), checked at m=11,…,16 and extended by periods of six. Independently computing B by exact rational ceilings for m=5,…,10 and n=5,…,m gives respectively [2], [3,2], [3,3,3], [3,3,4,3], [3,3,4,4,3], [3,3,4,4,4,4]. Only (5,6) and (7,8) violate the allowable bound. Applying the two replacement shift lists to the column triple and computing consecutive row differences including wraparound gives maximum row gaps respectively 2 and 3, and column maxima 2 and 3. This bounded check can be replayed with the ceilings and shift tuples in RESULT.md lines 29–60; the general proof is not an extrapolation. The uploaded verifier was inspected, not executed. The result holds for 5≤n≤m with no assertion about smaller factors or the strong product.

## originality

FAIL

Three other indexed records explicitly state the all-rectangles formula on the same unordered range, and two already present the balanced three-per-column construction with small-case adjustments. Haslegrave's primary paper alone does not cover unequal lengths, but that does not negate the direct indexed coverage. This is demonstrated statement-level overlap, not a priority determination based on dates.

## value

FAIL

Sharpness for unequal tori is intrinsically a motivated question, but this record re-establishes the already indexed exact invariant with the same type of constructive witness. It does not add a new parameter regime, a distinct optimization of the witness, or a structural result beyond that documented coverage. No worthwhile independent remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
