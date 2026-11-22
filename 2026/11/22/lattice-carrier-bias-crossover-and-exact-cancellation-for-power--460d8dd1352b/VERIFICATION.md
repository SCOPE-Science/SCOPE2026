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

The theorem is proved in RESULT.md using a conditional survival sum, an absolutely summable binomial expansion, explicit denominator inversion, Euler–Maclaurin with remainder, and algebraic cancellation at \(p=2\). In particular the \(O(x^{-5})\) equality remainder follows from the structure of the even-index Hurwitz sums; the numerical script is not used as an infinite proof.

To reproduce finite diagnostics, use `python -m pip install -r requirements.txt`, then `python verify_mean_excess.py`. The script evaluates the exact binomial/Hurwitz series at 70 decimal-digit precision for two cancellation cases, both generic sides of the phase boundary and the unmodified discrete GPD. These checks establish numerical consistency at specified parameter points only.

Public-source dates and model formulas: https://arxiv.org/abs/2210.15253 and https://arxiv.org/abs/2409.18719. The unmodified discrete GPD baseline is https://arxiv.org/abs/1707.05033. Independent mathematical audit has not been performed.
