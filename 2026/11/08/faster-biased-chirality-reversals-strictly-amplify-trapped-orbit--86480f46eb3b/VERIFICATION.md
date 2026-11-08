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

The result is proved analytically in RESULT.md by a two-state complex resolvent, harmonic-filter cross moments, and strictly signed derivatives. A standalone numerical replay is included as `checks.py`, requiring Python 3 and no external packages.

Run `python checks.py` from a directory containing the file. The prepared scientific package completed 1,082 deterministic assertions, including direct Runge–Kutta evolution of the two-state angular characteristic functions followed by Simpson integration. The program checks selected finite parameter sets only; exact nonnegativity of the full polynomial and global strict inequalities are proved in RESULT.md.

No statistical data, fitted model, human expert confirmation, or independent scientific audit is supplied. The slow- and fast-switching endpoint statements refer to limits of positive-rate stationary models.
