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
# Verification of hypersimplex projection-width fluctuations

The proof reduces the random width to a normalized Gaussian top-minus-bottom order-statistic functional, derives its influence function and second moment, and uses uniform spherical concentration to justify convergence of variances. No finite experiment is treated as a proof of an asymptotic claim.

Executed `python3 hypersimplex_width_check.py` against the standalone script in the same package. It uses exact `fractions.Fraction` interval operations, a Machin formula for pi, alternating-series tail bounds, and integer square-root enclosures. The checked scientific bounds, in threshold order \(t=1/2,1,5/4,3/2,2\), were \((0.01488,0.01489)\), \((0.00581,0.00582)\), \((0.00787,0.00789)\), \((0.00870,0.00872)\), and \((0.00541,0.00543)\). All enclosure and strict-ordering assertions succeeded.

A separately executable pure-stdlib sampling script, `hypersimplex_sample_check.py`, was run with a fixed seed, sample size \(n=600\), and 3,000 Haar directions per threshold. For \(t=0.5,1,1.5,2\), the empirical variances were 0.01528243, 0.00568868, 0.00847442 and 0.00509819, versus limiting values 0.01488462, 0.00581403, 0.00870885 and 0.00541904. The finite-sample tolerances passed. This numerical comparison is only corroborative; exact rational enclosures establish the qualitative nonmonotonicity.

Limits: The proof establishes Gaussian limits and asymptotic variances for fixed positive fractional rank. It does not establish that there are exactly two critical points, provide a uniform rate as rank tends to zero, or assess historical priority independently. The 2015 cube limit at half rank is prior work, not new evidence of originality. Independent audit: not performed.
