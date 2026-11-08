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

# Reproduction

Install Python 3.10+, NumPy and SciPy. In a directory containing `verify.py`, execute `python verify.py`. The observed output is `VERIFY_OK 35456 checks`.

The script checks exact-rational formulas for the oracle weight, variance and negative-event equivalences, tests the Gaussian rank-one reduction through direct matrix calculations, verifies finite-sample quadrature against the \(r=2\) modified-Bessel expression, and compares the \(r=20,40,80\) probabilities against the sharp asymptotic prefactor. These computations are finite and cannot establish the full asymptotic theorem alone; its proof is in RESULT.md. The formula assumes independent Gaussian sketches, exact real arithmetic, rank-one input for the tail law, and fixed or oracle-deterministic weights.
