---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone script `verify_queen_fixed.py` verifies the full finite board and group data with standard-library Python. Its executable computations have been run on the source packaged here, producing exactly `verify_output.txt`. No external certificate or independent mathematical audit is asserted.

The central orbit-realization argument is a direct consequence of barycentric uniqueness; the exact fixed orbit complex for each of ten subgroups is independently constructed by a compatible-orbit route and by the fixed faces of a direct enumeration of all queen placements. Four stated free collapses and an eleven-edge spanning tree prove the half-turn wedge-of-circles homotopy type. The calculations are exhaustive for board side six, not a proof of a uniform theorem over all board sizes.

The independent orientation-sign trace calculation verifies eight reduced Lefschetz numbers as a cross-check on fixed-space Euler characteristics. The known ambient Moore-space homotopy and rational character were obtained in earlier work and are not re-certified here. Public mathematical sources inspected: Chaiken–Hanusa–Zaslavsky, *A q-Queens Problem*, Parts I and II; full published result statements for the previously computed six-by-six and five-by-five queen complexes. A possibly unindexed equivalent fixed-space calculation remains a limitation of originality assessment.
