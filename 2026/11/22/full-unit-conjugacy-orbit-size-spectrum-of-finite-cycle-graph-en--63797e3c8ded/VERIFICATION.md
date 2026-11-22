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

# Verification record

The complete proof is in `RESULT.md`. The program `check_cycle_units.py` can be executed using Python 3 without additional packages. The calculations were performed with exact integers. For \(n=4,6,8,10,12\), they enumerate all strict cycle endomorphisms via balanced closed walks and direct function compositions and reproduce all unit centralizers and the Burnside orbit count. For \(n\le10\), they also construct actual conjugacy orbits and compare their size histograms to the theorem. Direct exhaustive enumeration of arbitrary functions at \(n=4,6\) independently tests completeness of the walk encoding. Odd cycles \(n=5,7,9,11\) are independently checked using the full dihedral unit group.

Observed even-cycle orbit totals: \(10,18,48,140,491\) in lengths \(4,6,8,10,12\). The program completes with `CYCLE_ENDOMORPHISM_UNIT_COMMUTANT_CHECKS_PASSED`. The universal statements depend on the mathematical proof, not finite extrapolation. The priority comparison is limited by lack of access to the full Michels–Knauer 2009 paper.
