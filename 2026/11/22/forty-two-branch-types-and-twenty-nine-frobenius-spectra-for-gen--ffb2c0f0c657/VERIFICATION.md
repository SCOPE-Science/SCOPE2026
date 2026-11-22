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

# Executed mathematical checks

From the complete local package, run `python3 verify_kernel_spectra.py`. The program executes two exhaustive enumerations, checks their equality, verifies all 42 stored rows in `kernel_spectra.csv`, confirms the two natural symmetric-group orbit sizes and the pair of explicit characteristic-five examples. It prints `GENUS_FOUR_2295_LAGRANGIANS_42_TYPES_29_SPECTRA_VERIFIED` on success.

The all-characteristic statement follows from the standard torsion correspondence plus the exhaustive ten-point permutation calculation. There is no reliance on random finite-field sampling. The program proves neither that every branch partition occurs over every small field nor that all quotient principally polarized abelian varieties are Jacobians. No independent audit has been performed.
