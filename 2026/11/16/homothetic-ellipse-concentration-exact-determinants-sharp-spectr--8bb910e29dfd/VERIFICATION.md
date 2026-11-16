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

The analytical certificate is the sequence of exact identities \(G(t)=t^2D_tGD_t\), \(\lambda_0\cdots\lambda_{k-1}\sim\Delta_k t^{k(k+1)}\), and \(\Delta_{N+1}/\Delta_N=H_N/M_N\); all normalizations are specified in `RESULT.md`.

The standalone `CHECK.py` checks exact moments and ellipse monic-Chebyshev orthogonality for two rational ellipses and degrees \(1\) through \(6\), checks the determinant identity at two rational scales, then uses 90-digit arithmetic to compare all spectral asymptotic coefficients and the scaled least-eigenvector polynomial at two shrinking scales. It reports `HOMOTHETIC_ELLIPSE_CONCENTRATION_PASS` on success. Install the dependencies from `requirements.txt` and run `python CHECK.py` from the folder containing these files.

The finite checks validate algebraic examples and normalization; they do not prove the general statement or establish historical originality. The proof covers every fixed integer degree and every noncircular ellipse with positive semiaxes, without a uniform-in-degree assertion. Independent audit remains unperformed.
