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

# Reproducibility and verification

The exact projection identity and degree-\(2\beta\) polynomial are established algebraically in `RESULT.md`. The normalized analytic root equation has exactly \(\beta\) branches about each of two limiting points. The decisive borderline case \(\cos(2\pi j/\beta)=1/2\) contributes a strictly positive second-order difference \(\varepsilon^2+O_\beta(\varepsilon^{{\beta+2}})\), so no boundary zeros are counted spuriously.

Run `python CHECK.py` in a directory containing the standalone `CHECK.py` file (requires Python and `mpmath`). The packaged source was run successfully and reported `ANTIPODAL_KERNEL_CHECKS_PASS 2448`. The program checks 24 integer exponents and two radii, verifying branch residuals, predicted disk membership, and exact per-cluster counts. The numerical work does not certify all integer exponents or all sufficiently near-boundary radii; these follow from the proof. Independent mathematical verification is not performed.
