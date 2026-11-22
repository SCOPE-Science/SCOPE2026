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

# Verification of the mathematical claim

Run `python check_fixed_sink.py` from the same directory. Dependencies are NumPy and SciPy.

Analytic checks: independent boundary degrees are binomial; the centered internal Laplacian's matrix-Bernstein variance proxy is \(2p(1-p)(mI-\mathbf1\mathbf1^{\mathsf T})\); the orthogonal block remains invertible with high probability; its inverse gives a leading factor \((pm)^{-1}\); and the sample boundary-degree variance tends to \(sp(1-p)\). The binomial central limit theorem and Slutsky's theorem complete the infinite-size argument.

Computational checks from the delivered standalone script: 253 deterministic finite eigenvalue brackets, 60 exact Schur-identity numerical comparisons, and 216 sampled random habitat eigenvalues. At \(s=2\) and \(p=0.4\) the correction means for total graph sizes 96, 192 and 384 were 1.228406, 1.219869 and 1.205519, versus the proved limit 1.2. The script's sampled Gaussian variances were 0.424736, 0.630719 and 0.404032, versus limiting variance 0.48. These are finite numerical diagnostics, not an infinite-dimensional certificate.

Limits: no exact finite-\(n\) distribution is claimed; no assertion applies to network-adaptive absorbing sites, nonconstant \(p\), or growing \(s\). Independent scientific validation has not been performed.
