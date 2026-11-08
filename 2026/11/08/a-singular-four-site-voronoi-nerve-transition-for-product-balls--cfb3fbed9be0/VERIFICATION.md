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

The result has an analytic proof in `RESULT.md`. The included Python 3 standard-library script `check.py` was run from the source file that was subsequently embedded. It checked 4,500 random bicone Voronoi triple witnesses and exclusions, 4,000 positive-exponent fourfold equidistance cases, and four specified asymptotic-rate values, reporting:

`FOUR_SITE_BICONE_VERIFIER_OK 8504 random_1= 4500 random_p= 4000 lower_defect_bound= 0.0002226513389433433`

For the fixed example \(R=11/20\), \(h=1/2\), the four sample exponents \(p\in\{1.03,1.02,1.015,1.01\}\) produced positive negative-height roots converging toward the predicted asymptotic ratio. The numerical output is a check on the derived equations, not a certificate over all positive parameters. The proof of the asymptotic uses a mean-value theorem estimate with a uniform error less than \(h\), and the proof of positive union-volume error uses an open gauge ball and its exact volume \(2\pi/3\).

The public note and structured scientific review state the known connection to the five-site bicone construction. External independent assessment has not been performed.
