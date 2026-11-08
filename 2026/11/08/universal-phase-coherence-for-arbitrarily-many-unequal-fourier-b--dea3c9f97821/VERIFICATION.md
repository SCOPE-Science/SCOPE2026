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

# Reproduction and limits

The proof is self-contained given Fourier inversion, Fubini and Lebesgue differentiation. Run `python3 check_unequal_multiband.py` with the Python standard library; the program prints `UNEQUAL_MULTIBAND_SIGN_CHECKS_PASS 6276` on success. It samples nonboundary configurations and constructive feasible configurations. It is not an exhaustive test and is not used to certify the theorem, which is proved analytically for every finite band count and positive width vector.

The boundary convention is equality permitted when a sinc zero occurs solely at a measure-zero endpoint of a spectral difference interval. The band-disjointness assumptions remain strict. The argument does not treat uncentered time intervals, other time masks, or irregular centers. Independent audit is not performed.
