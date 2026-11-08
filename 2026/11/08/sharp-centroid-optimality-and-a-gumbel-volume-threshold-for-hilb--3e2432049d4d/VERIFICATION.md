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

# Computational and analytical verification

The standalone `check.py` was executed with Python 3, NumPy and SciPy, from the actual checked artifact. All specified assertions passed and its final line was `HILBERT_SIMPLEX_EUCLIDEAN_BALL_MASS_OK`. The script tests direct Monte Carlo examples in dimensions with 2, 3 and 5 barycentric coordinates using 300,000 independent simplex samples per example, compares the exact integration with the beta-center expression for coordinates counts 2 through 10 and three radii, checks several majorization transfers, evaluates the short-radius coefficient, and compares the exact centroid beta law with the Gumbel threshold for n=1,000 and n=10,000. Direct Monte Carlo tolerance is based on six binomial standard errors plus a small absolute allowance.

The proof is not a numerical extrapolation. The critical exact steps are: (i) affine/projective reduction to barycentric coordinate ratios, (ii) the independent exponential representation, (iii) conditioning on which exponential ratio is smallest, (iv) integration by parts, (v) strict concavity of log(1−exp(−ax)), (vi) the beta recurrence, and (vii) convergence of exponential maxima and minima. The finite-sample tests neither certify historical originality nor prove infinite quantifiers.

Reproduction from embedded artifacts: install dependencies in `requirements.txt`, then run `python check.py`. No external data, unbundled machine state or archived log files are needed.
