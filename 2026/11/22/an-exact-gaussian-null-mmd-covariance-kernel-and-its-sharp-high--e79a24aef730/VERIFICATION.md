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

# Verification and reproducibility

The analytical result is established in `RESULT.md` by Gaussian integration, canonical U-statistic degeneracy, strict-kernel nonproportionality and three rigorous dimension asymptotics. The finite-\(d\), finite-\(n\) formula is exact, not an empirical fit. The coded checks support, but cannot establish, the universal mathematical claims.

`proof_check.py` requires Python 3.11+ standard library only. Run `python3 proof_check.py` from the unpacked finding directory. This execution passed 91 assertions, including 40,000 seeded direct-sample replications and independent one-dimensional Gaussian quadrature. At \(n=4,d=3,a=0.17,b=0.51\), the exact covariance is \(0.0055762051103331245\), versus simulated \(0.005549713806394831\). The simulation tolerance is statistical and does not assert certified error bounds.

Mathematical limits: the underlying law is an exactly specified \(N_d(0,I_d)\), sample size is any integer \(n\ge2\), and the power-law bandwidth exponents use fixed distinct positive \(u,v\). Inverse-square bandwidth \(a\) should not be confused with a Gaussian kernel standard-deviation bandwidth. No fitted-nuisance, two-sample, multiplicity-adjusted or power theorem is included. The high-dimensional proof does not rely on the numerical examples.
