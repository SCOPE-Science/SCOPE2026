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
# Verification of the first cut-locus distance law

The formal proof is in `RESULT.md`. The geometric steps requiring attention are the five-cycle/no-triple-overlap statement for \(r\le\frac12\arccos(-1/4)\), the exact two-spherical-ball intersection integral, the normalized quotient volume \(2\pi^2/5\), and the uniform-Haar variable \(|z_1|^2\). All are derived there. The CDF is claimed exactly only for \(0\le r\le\frac12\arccos(-1/4)\); no full-radius law is asserted.

Run `python checker.py` with packages in `requirements.txt`. The code compares the closed formula with direct numerical integration of two-ball overlap at six radii, checks the cubic-contact coefficient at four offsets, then samples 2,000,000 independent pairs of normalized Gaussian four-vectors. For every pair it computes the quotient geodesic distance by maximizing over five separate complex inner products. Random tests are bounded by statistical tolerances, not treated as proof of an infinite claim. The successful observed message was:

`LENSSPACE_FIRST_CUT_LOCUS_LAW_OK samples=2000000 quadrature_tests=6`

At \(r=0.7\), the closed formula yields \(F(r)\approx0.329358033\) and the sampled frequency was \(0.329602000\). At \(r=0.9\), the corresponding values were approximately \(0.621532151\) and \(0.621497000\). The sampled mean distance was \(0.8035719054\), consistent with the literature's approximate \(0.80378\) on this space, but the theorem does not claim the exact mean. The explicit limit coefficient computed in the checker is \(1.3115088574446212898\).

No independent expert audit was performed. Numerical reproducibility does not certify originality or the proof independently.
