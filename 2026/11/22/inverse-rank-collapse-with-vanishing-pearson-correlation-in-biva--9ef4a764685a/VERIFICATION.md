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
# Verification record

The theorem is supported by explicit integral identities and dominated-convergence arguments in `RESULT.md`. In particular, finite tests are not substituted for uniform or infinite-domain limits.

## Reproduction

Execute `python check.py` with Python 3 and NumPy/SciPy installed. The standalone script directly evaluates the inverse-Lindley-hazard integrals, checks the scaling of exact marginal moments at \(\kappa=10^4\) and \(10^8\), and uses exact conditional exponential sampling with numerical marginal inversion to compare empirical rank and Pearson coefficients. Fixed pseudorandom seed and explicit numerical acceptance ranges are included in the script.

On the included execution, it returned \(A=1.6584519762515066\), \(B=2.2706861125004743\), and \(A^2/B=1.2112915749961253\) for the symmetric unit-parameter example; simulated Pearson/Kendall/Spearman values at \(\kappa=10^8\) were approximately \(-0.07450,-0.86010,-0.97413\). All numerical assertions passed.

## Limits of verification

Numerical integration and Monte Carlo corroborate, but cannot establish, limiting logarithmic constants or copula convergence for arbitrary parameters. The proof uses the positive integrable majorants, an all-range mixed-moment bound, exact conditional laws, and weak convergence of logarithmic coordinates. Historical priority remains subject to review of the original 1988 article, whose full text was not accessible. Independent mathematical audit has not been performed.
