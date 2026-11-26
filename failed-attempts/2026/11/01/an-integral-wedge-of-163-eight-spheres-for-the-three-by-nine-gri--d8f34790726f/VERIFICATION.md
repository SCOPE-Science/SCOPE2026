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

I generated the ordinary matchings of the 27-vertex grid independently by mask/endpoint occupancy, then reproduced the prescribed matching by simultaneous upper-face deletion at each pivot. The augmented face count is 7,594,361, Euler characteristic 164, with 3,797,088 pairs and critical dimensions/counts 0:1, 8:173, 9:10. Acyclicity also follows without assuming the recorded Hasse-sort output: on a directed cycle the up and down steps must alternate, since up steps are matching incidences and cannot be consecutive, and cardinality changes by one. Let i be the smallest pivot label among its up steps. Some down step deletes i; its endpoints both participate in cycle matches with pivots at least i, so they were available before pivot i and had to be paired at that stage, contradicting the down edge. I independently eliminated each critical 9-cell boundary by forward substitution of the signed unit relations in dependency order over Python integers. On columns (2,53,49,72,20,87,148,166,17,16) the resulting matrix is I with the stated changes (7,7) and (8,7) to −1, so det=−1. All intermediate coefficients in these ten reductions had absolute value at most 2. The Morse CW complex has one vertex and no cells in dimensions 1 through 7. The transpose as a boundary map Z^10→Z^173 is a split injection (the displayed row-oriented array defines the transpose surjection), so H8 is free of rank 163 and no other reduced homology remains. By Hurewicz choose sphere maps representing a basis in degree 8; their wedge induces integral homology isomorphisms, and both spaces are simply connected CW complexes, so Whitehead gives the stated homotopy equivalence.

## originality

FAIL

The September 23 preprint arXiv:2609.27366v1 proves the same finite-range homotopy statement, not merely a Betti table or all-width conjecture. Its p. 22 Table 1 gives integral Z^163 in degree 8 at n=9, and the paragraph after the table explicitly concludes the sphere-wedge homotopy equivalence for 3≤n≤9 using simple connectivity. This covers the exact frozen Finding. The explicit discrete-Morse and unit-minor verification is a different proof of that finding, not a new homotopy classification. No repair is offered as a new claim.

## value

FAIL

The 3×9 boundary case is well motivated by the failed all-width recurrence; a transparent integral certificate is useful corroboration. But as submitted the sole mathematical contribution is the exact wedge for the same case already settled in the earlier preprint. It neither extends the proven finite range nor proves a new structural reduction or exact invariant. Reproducing the known classification by another finite computation is insufficient as a new scientific finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
