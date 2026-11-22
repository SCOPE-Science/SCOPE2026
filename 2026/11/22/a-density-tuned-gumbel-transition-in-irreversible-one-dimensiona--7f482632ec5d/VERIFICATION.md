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

The attached `verify.py` checks the Laplace transform and resonance limit symbolically. It constructs exact pure-death generators for lengths \(1\) through \(104\), integrates their finite-time survival by matrix exponentiation, and compares the geometric length mixture with the closed-form survival function. An unrelated site-by-site Markov simulation of a specified 12-spin ring is checked against independent-domain sampling. Finite Bernoulli ring trials at three starting densities compare empirical ordering-time CDFs with the limiting law. An additional deterministic normalization check evaluates critical-window tail intensities at increasingly large \(\log L\).

Execute `python verify.py` with NumPy, SciPy and SymPy. Its success banner means only that the listed finite and algebraic diagnostics passed; the proof of infinite-size convergence is in `RESULT.md`. No independent audit or independent validation has been performed.
