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

# Independent reproducibility instructions

Run `python verify.py` with Python 3, NumPy and SciPy, using `requirements.txt` for minimum compatible versions. The script directly integrates a Gaussian kernel against a Gaussian density, constructs two-node Gram matrices and computes their unconstrained weight vectors, compares the signs against the claimed algebraic inequalities, estimates positivity probabilities from independent random nodes, and checks exact beta formulas, tail constants, and the dimension-six threshold. The replay completed 6,163 finite tests and exited successfully.

For mathematical verification beyond numerical examples, check the four logical bridges in `RESULT.md`: (i) exact Gaussian kernel means and the two-by-two inverse; (ii) independent standard Gaussian sum and difference coordinates and the conditional normal law; (iii) the beta law of a ratio of independent chi-square variables; (iv) incomplete-beta endpoint asymptotics and the layer-cake moment formula. These together prove the claim for every integer dimension, positive kernel shape and positive moment exponent. Sampling and finite checks do not prove universal assertions.

The proof concerns two independent Gaussian nodes with a kernel whitened by the integration covariance. At zero shape the kernel matrix is singular and the reported value is only a one-sided limit. Near that limit direct floating-point inversion can be ill-conditioned. Positivity of unconstrained quadrature weights is not a guarantee of accurate numerical integration or of optimal bandwidth. No external independent mathematical audit has been performed.
