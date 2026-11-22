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

# Verification of the conditional entrance theorem

The self-contained `checker.py` was executed successfully with 3,622 exact-rational and numerical assertions. These check the Bessel reflection-kernel Taylor coefficients against finite killed generators, a telescoping Bessel recurrence, normalization of the terminal minimal QSD and selected constants. The optional `numerical_check.py`, using NumPy and SciPy, evaluated the survivor-conditioned entrance law at horizons 100, 1,000 and 10,000 with the explicit test rates \(a=2,b=1/2\). At \(t=10,000\) its reported probabilities were approximately 0.521303 for \(\beta=1\) and the event \(I\le\sqrt t\) (limit 0.5205); 0.523999 for \(\beta=2\) and \(I\le t^{1/4}\) (limit 0.5); and 0.6112 for \(\beta=3\) and \(I=1\) (limit \(6/\pi^2\approx0.607927\)).

The limits are **proved by the uniform Fourier-kernel and summation arguments in `RESULT.md`**, not by those finite tests. The exact source model and publication date come from Pollett, arXiv:2611.17791v1 (submitted November 13, 2026). The 1991 van Doorn work was compared on relevant accessible PDF material; other historical analogues were accessed only at abstract level. No independent mathematical audit, reproducible certified formalization or universal novelty guarantee is claimed.
