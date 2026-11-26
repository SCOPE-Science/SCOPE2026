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

PASS

The affine incidence graph has nine vertices on each shore, degree three, and 27 edges. Closed neighborhoods have size four, so four vertices cannot dominate. For five vertices with t points, point coverage forces t<=3 and line coverage forces t>=2. With three points, two selected lines must cover six different unselected points; thus they are parallel and the three points fill the omitted line. With two points, the six retained lines they meet must be distinct and disjoint from the three selected lines; the two points lie on one removed-direction line and the three remaining lines meet at its third point. Both forms dominate. Each vertex occurs five times, and line/point geometry gives 0 for 27 incident pairs, 1 for 72 same-shore pairs and 2 for 54 cross-shore nonedges. The four pair-trace counts are c,5-c,5-c,8+c; every triple contains a same-shore pair and cannot realize both extensions where that pair is positive. The one-skeleton is connected (each shore is a clique and there are 54 cross-shore edges), so contracting a spanning tree gives a homotopy equivalence to a wedge of 109 circles. The frozen proof's phrase 'deformation-retracts' is too strong literally; tree contraction gives the claimed homotopy equivalence, which is the Finding. The root positive branch has only five hypotheses, excluding depth four. For depth three, a point root, followed by a nonincident line on yes and an incident line on no, leaves four groups of sizes 2,3,5,8, each separable by some third query. An independent LCF replay confirmed the affine isomorphism, exhausted all 12,616 subsets through size five, and checked all queried supports through size three and the exact adaptive dimension by recursion on version spaces.

## originality

FAIL

The strongest overlap is not the earlier locating-domination six-set result but the distinct same-day Pappus odd-domination record b2c8ce57e775. It reports the exact metric five-set family, its full center-intersection table, and explicitly treats the ordinary minimum census of eighteen size-five sets as already available. Since odd domination implies ordinary domination, the eighteen exhibited odd five-sets exhaust the eighteen ordinary optima. The incidence matrix indexed by centers and coordinates is symmetric, so that record's center-intersection table is exactly the coordinate concurrence table under transposition, not merely numerically similar. The remaining shattering, topology and adaptive conclusions follow directly from that table and the common frequency five; the formulas were not found verbatim in the comparator, but the comparison establishes substantive coverage. The affine proof provides a separate explanation of ordinary exhaustiveness; the record does not establish a distinct uncovered structural claim beyond that overlap and its immediate consequences. This verdict concerns mathematical coverage, not which of the same-date records appeared first. The odd-domination record does not identify the origin of the earlier ordinary census precisely enough to assign temporal priority.

## value

FAIL

Pappus optimum domination and adaptive membership queries are natural objects, and the short affine argument is useful as an explanation. But for this single graph the shared exact symmetric design already supplies the central structural information: reconstruction is a zero test on its intersection table, the entire support complex follows from positive concurrence and the same-shore multiplicity one, and the depth witness uses two entries and the common frequency. These narrow consequences are mechanically implied by the shared exact data once the reported ordinary optimum census is used. The record gives no further structural separation beyond those consequences of this particular design. The judgment is based on the exact same-graph overlap, not on a presumption that finite shattering calculations lack value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
