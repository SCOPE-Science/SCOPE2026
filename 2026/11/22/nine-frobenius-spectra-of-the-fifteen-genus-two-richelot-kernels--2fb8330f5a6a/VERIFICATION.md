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

# Verification

Run `python3 richelot_kernel_spectra.py` from the directory containing this file and the stand-alone Python program. It requires only the Python 3 standard library. The computed table has all 11 sextic factorization types, every 15-point matching orbit profile, counts of rational subgroup kernels and counts of rational two-torsion classes. The checks independently compare cycle lists with fixed-point counts for every power, check the number of distinct zeta profiles (nine) and all collisions (two), and verify the two explicit F7 sextics are squarefree with the claimed degrees of irreducible factors.

Success prints `RICHELOT_FROBENIUS_NINE_KERNEL_SPECTRA_VERIFIED`. The full uniform theorem uses the proved Frobenius-equivariant matching correspondence; a finite sample alone is not used to establish it. No external solver, hidden table, prior-run file or unprovided dependency is required. Neither the literature originality conclusion nor the value judgment has independent audit evidence.
