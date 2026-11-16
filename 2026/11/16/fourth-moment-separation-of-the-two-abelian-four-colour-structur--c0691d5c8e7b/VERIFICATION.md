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

The complete 64-state difference table is embedded as `T_TABLE.csv` and enumerated independently by `verify_energy.py`. The script checked the complete histograms {2:2,4:12,6:30,8:1,10:18,21:1} for the cyclic group and {4:18,6:24,8:3,10:18,21:1} for the Klein group, and checked the all-length formula using a finite set of additional evaluations (not a substitute for the proof). An independent tensor-character implementation, `verify_fourier.py`, reconstructed all Fourier coefficients at lengths one through four and matched the corresponding additive energies. Both commands completed successfully without third-party dependencies. Generality for every length comes from the stated exact 64-state identity, not from extrapolation. No external independent audit is claimed.
