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

# Reproducibility

Run `python3 verify_softlink.py` with Python and SymPy. The checker independently enumerates permitted binary occupation configurations on even chains of 4 to 20 sites, builds the bivariate fugacity–soft-bond polynomial, and compares the resulting coefficients exactly with the claimed closed identity. In a distinct check it counts real roots by exact Sturm computations on 64 chain-size/parameter combinations and verifies nonvanishing pairwise polynomial greatest common divisors in 18 further sizes. Expected output: `SOFT_LINK_EXACT_VERIFICATION_PASSED 9 64 18`.

The finite tests alone are not a proof for infinitely many lengths. The global proof rests on the independent-half partition identity, real symmetric Jacobi spectra, recurrence-based coprimality, and a local implicit-function expansion. No independent external audit or validation has been performed.
