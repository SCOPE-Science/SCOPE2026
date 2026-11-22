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

# Verification and reproducibility

Run `python verify.py` in the directory containing this file. It requires Python's standard library only. The diagnostic confirms the rational example \((t,\alpha,\beta)=(1,1,25/16)\), including exact trace and Hilbert–Schmidt identities; it samples a parameter grid on both sides of the Schatten transitions and checks several near-critical rank profiles. The expected output is `GAUSSIAN_FOCK_SCHATTEN_DIAGNOSTIC_OK 850`.

The continuum theorem and strictness are *not* certified by finite sampling. They follow from the exact monomial and Mehler singular-value decompositions and the convex-order derivative comparison detailed in `RESULT.md`. The near-critical theorem uses exact multiplicity counts and controlled expansions. The boundary assertion uses unitary Gaussian convolution and its Fourier multiplier.

Proof hypotheses: \(t,\alpha,\beta>0\) and \(\delta=\beta(2t-\alpha)-t^2>0\) throughout the Schatten statements; \(2t>\alpha\) and \(\beta\downarrow t^2/(2t-\alpha)\) for the critical statements. No independent audit has been performed.
