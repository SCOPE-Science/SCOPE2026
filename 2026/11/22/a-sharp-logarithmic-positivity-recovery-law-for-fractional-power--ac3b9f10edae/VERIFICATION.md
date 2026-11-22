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

`verify.py` requires Python 3, NumPy and mpmath. Invoke `python verify.py` from the directory containing the file. The script independently computes the discrete Fourier spectrum from the full circulant first row; it does not use the proof's infinite-series error estimate or assume the theorem in its numerical algorithm.

The observed output was 48 passing sign tests and 24 successful high-precision crossover evaluations. For \(p=1.5\), \(M=1024\), the two evaluated critical-window values of the normalized Nyquist eigenvalue were approximately \(-0.40783949\) and \(0.15006307\), versus theoretical limits \(-0.40785437\) and \(0.15004124\). The differences were consistent with the derived asymptotics. The tests are a finite diagnostic, not a proof of any universal quantifier.

The infinite proof is given in `RESULT.md`: standard stable-density positivity and two-sided polynomial heat-kernel estimates, exact Abel wrap-error formula, uniform comparison, and an alternating difference expansion. No external independent audit or certification was performed.
