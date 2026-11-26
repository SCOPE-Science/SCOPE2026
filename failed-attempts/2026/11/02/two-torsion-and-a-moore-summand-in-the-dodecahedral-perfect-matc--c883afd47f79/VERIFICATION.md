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

The complex has the graph's edges as vertices; its faces are precisely the edge sets extendible to perfect matchings. A separate tuple-based enumeration (without running the supplied code) reproduced 36 perfect matchings, 30,503 nonempty faces, the full face vector, 15,231 matched pairs, critical-cell counts 1,10,30 in dimensions 0,2,3, and acyclicity across all 163,650 Hasse incidences. Signed projection cancels unit incidences: for a matched lower face a of b, imposing that the projected boundary of b vanish gives the displayed recursion, along directed gradient paths. The reproduced 10 by 30 boundary has 69 nonzero entries, mod-two rank 9 and the specified exact minors -1 and 2. The minors give integer rank ten and nine Smith units; mod-two rank forces every maximal minor even, and the minor 2 forces the last factor to be 2. The original mod-two boundary ranks also agree. For the homotopy claim, Forman's theorem gives a CW model with no one-cells, two-skeleton a wedge of ten 2-spheres, and thirty 3-cells. The attaching maps are classified by their degree columns via Hurewicz. Row and column basis changes are realized by homotopy equivalences on target and source wedges of 2-spheres, respectively; taking their homotopy cofibers justifies the Smith-form splitting, not merely the homology. The nine unit cofibers are contractible, the degree-two cofiber is the Moore space, and the twenty zero columns give 3-spheres.

## originality

FAIL

Two distinct earlier indexed Resultary records (2c09902bba79 and efd05431d7b5) already state the same full integral homotopy equivalence M(Z/2,2) wedge twenty S^3 for precisely the same perfect-matching complex of GP(10,2), with the same integral homology. This is exact result-level coverage, not an inference from similar titles, different matching complexes, or matching dimensions. The independent reproduction supports correctness but does not supply a distinct frozen finding.

## value

FAIL

The invariant is intrinsically meaningful: torsion in a canonical cubic graph's extendability complex distinguishes this topology from examples that are wedges of spheres. However, the frozen scientific contribution is only an already catalogued exact invariant, with no distinct consequence or method claim identified as a new contribution. Its recomputation is useful validation, not a substantive new finding under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
