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

The exact active-constraint path-component argument proves the claimed smoothness cutoff for all integer parameters \(s\ge2\). An independent finite checker reconstructs the constraints, enumerates integer points, performs rational Gaussian elimination on active facets, and counts nonsimple vertices in both orientations for \(\(s=2,3\)\) through the first singular dimensions. It reports `CHECK_OK cases=26 feasible_points=68589 witnesses=57`.

Run `python3 verify.py` in the same folder. The script uses the Python standard library only. Finite enumeration provides consistency checks, not an infinite proof. Source coverage remains incomplete in the latest preprint versions; no independent audit has been performed.
