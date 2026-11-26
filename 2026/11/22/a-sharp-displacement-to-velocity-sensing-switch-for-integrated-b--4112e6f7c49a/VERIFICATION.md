---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

# Reproducibility and limits

The included `verification.py` integrates the two explicit covariance kernels, uses exact rational arithmetic for the crossover bracket and derivative Bernstein certificate, and checks a rational enclosure for the degree-seven polynomial root. Bounds on the numerator and denominator of the crossover formula then give the certified decimal enclosure \(0.03486395077318212468<\eta_*<0.03486395077318212469\). An independent recomputation checked this enclosure. The script additionally provides 32 numerical quadratures of original covariance products and 10 numerical comparisons across sample noise levels; those are not used to certify the decimal digits.

The proof of uniqueness for *all* positive noise levels is analytic: the time derivatives have the stated one-crossing structure, and the logarithm of the two optimized gains has a strictly negative derivative. Finite numerical tests illustrate and stress-test but do not establish that universal claim. The scope is one scalar observation with one of two calibrated modes, common noise variance, and integrated posterior risk for an integrated standard Brownian bridge. No formal proof verification or external attestation is claimed.
