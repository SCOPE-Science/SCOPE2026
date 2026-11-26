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

The ladder distance is absolute column displacement plus the rail-change indicator, so geodesics are monotone and use at most one rung. The four forbidden triple types follow and each can be realized with suitable endpoints. With two same-rail horizontals at a<c, allowable rungs lie in (a,c]; a single opposite-rail horizontal inside [a,c] removes that entire interval through its two cross-rail pairs. A second two-horizontal rail must use the identical pair. These checks give the face partition. A facet must fill all available rungs. With one horizontal on each rail at least two rungs remain, preventing a (2,1) extension; with two on one rail and none on the other a nonempty rung interval prevents such an extension. In the rung-free (2,1) case a horizontal at an endpoint can be extended, whereas a strict-interior horizontal cannot; (2,2) is already maximal. Profiles with no pair of horizontals extend to a same-cut pair. Summing by separation gives both stated polynomials and hence the total and full facet-size spectrum, including the n=2 Boolean case. An independently written full-width geodesic test checks every coefficient for n=2 through 8: face/facet totals at n=8 are 8855/182. It examines every admissible set by increasing-edge augmentation, not just maximum sets. Replay: python3 /workspace/branches/independent_checks_2_5.py. This bounded check supplements the all-order proof; the frozen checker was inspected, not executed.

## originality

PASS

Best-of-knowledge pass for the full labelled face and inclusion-maximal size distributions and the all-facet classification. The previously published maximum n+2 and the previously classified n−1 maximum sets are not original contributions of this record. The residual inaccessible product paper is not evidence either for or against priority.

## value

PASS

The ladder is the first Cartesian grid family with both a growing maximum and shorter inclusion-maximal configurations. Knowing only its maximum cannot answer what sizes greedy edge addition can terminate at or how those sizes are distributed. The proof explains the full range of maximal sizes by an exact separation-and-interval mechanism and gives all face coefficients, not just isolated small cases. This has concrete structural value even without topological or wider-grid conclusions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
