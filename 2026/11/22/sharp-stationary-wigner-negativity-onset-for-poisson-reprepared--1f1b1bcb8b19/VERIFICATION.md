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

The result can be replayed by running `python3 CHECK.py` (Python 3.10+; no third-party packages). The checker's exit status is zero; it prints `PASS 136 numerical assertions` and three example onset coefficients. The complete analytic proof is in `RESULT.md`.

Checks include independently computed odd-Fock parity sums, attenuation-Wigner normalization, positivity on varied samples below and at threshold, strictly negative Wigner value at the origin above threshold, explicit positive quadratic coefficients, the derivative of the reset-age integral and direct numerical integration of Wigner-negative mass for two small supercritical ratios. Simpson quadrature truncation is controlled only numerically and is not a certified error bound. Analytic quantifiers (all positive rates and amplitudes, entire phase space) are justified by integral inequalities, not by the finite checker.

Scientific limits: no rigorous finite-sample tomography guarantee; the shape of the negative set at large supercritical ratios is not classified; source access and statement-level searching do not establish absolute global publication priority. Independent audit has not been performed.
