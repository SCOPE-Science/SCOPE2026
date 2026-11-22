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

The accompanying `verify.py` script (Python 3 standard library) was executed as `python verify.py` against the exact packaged source bytes. It reported successful Dijkstra-based Apéry comparisons, genus formula, type and symmetry checks for every parameter \(6\le m\le1000\); exhaustive gap/PF/genus checks covered \(6\le m\le160\). No external packages or data files are required. Finite checks alone are not an infinite proof: the mathematical derivation appears in `RESULT.md`. The status above records no independent mathematical audit.
