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

# Reproduction and verification

Run `python verify.py` with NumPy in the directory containing the extracted files. In this package it prints `VERIFY_OK 102 finite assertions`. The script assembles the exact grounded graph Laplacian from the two separate shift commutators, solves for the finite optimal diagonal, checks the Euler equations and \([0,1]\) bounds, checks the exact zero-coupling profile and energy, and compares scaled energies and parity values with the derived continuum formulas for multiple section sizes and couplings. It also tests a supercritical vanishing-coupling sequence.

These are finite numerical diagnostics only. The operator norm reduction, existence, uniqueness, continuum limit, strict transition, and two extreme regimes rely on the proof in `RESULT.md`. No independent mathematical certification or literature-completeness guarantee is claimed. Primary references and comparison boundaries are listed in `RESULT.md` and `AUDIT.json`.
