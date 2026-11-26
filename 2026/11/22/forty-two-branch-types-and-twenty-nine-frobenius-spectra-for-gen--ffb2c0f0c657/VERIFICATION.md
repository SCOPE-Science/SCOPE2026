---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical checks

From the complete package, run `python3 verify_kernel_spectra.py` beside `kernel_spectra.csv` to recompute all rows and both components of the kernel action. The two finite enumerations agree. Run `python3 verify_split_profiles.py` in the same directory to check the matching component by fixed counts of powers, both zeta spectra for the witness, the 38 ordered component profiles, and the irreducibility of the factors realizing the witness over \(\mathbb F_5\). The latter prints `42 branch types; 29 aggregate and 38 ordered component profiles; collision checked`.

The symplectic correspondence and finite group action establish the result uniformly in odd characteristic for each realized branch type. The calculation gives neither universal small-field realization nor a classification of the principally polarized quotient targets.
