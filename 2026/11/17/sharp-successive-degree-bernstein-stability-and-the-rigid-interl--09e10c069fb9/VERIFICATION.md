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

# Reproducibility and limits

Run `python verify_bernstein.py` using a standard Python interpreter. No external library, data file or network access is required. The program reconstructs the interlacing tent spline and verifies its slopes and nodal values, calculates both Bernstein polynomials at rational arguments, and computes the corresponding \(W_1\) distance independently by finite cumulative-distribution integration. Every comparison uses `fractions.Fraction`, so printed pass statements refer to exact rational equality. It checks degrees one through 23 at eight evaluation probabilities (184 parameter pairs).

The verified analytical steps are the Bernoulli coupling, the exact first binomial moment, saturation of every coupling edge, and uniqueness of the Lipschitz extension along fully saturated adjacent intervals. The checker cannot certify unboundedly many degrees, every real evaluation parameter, or publication novelty. Those conclusions require the proof and literary comparison, respectively. No independent mathematical audit has been carried out.
