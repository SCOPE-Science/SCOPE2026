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

# Verification of dyadic cap-survival asymptotics

The exact inverse identity, spherical surface-area normalization and parameter-domain restrictions were reconstructed directly. The proof proceeds by the exact scalar inverse recurrence, an endpoint expansion of \(\arcsin\), fixed-iteration propagation of the small deficit, and the cap-volume asymptotic \(I_d^{-1}\int_0^r\sin^{d-1}v\,dv\sim r^d/(dI_d)\). The resonance and near-resonance calculations explicitly retain the term proportional to \(z\sqrt{1-t}\), which is necessary for the crossover coefficient.

Running `python checker.py` with `mpmath` installed produced `SPHERICAL_CAP_SURVIVAL_EXACT_AND_CRITICAL_LIMITS_OK`. Tests include the polar inverse for three map parameters, exact spherical integrals in dimensions two and three, and both critical regimes in dimensions two through four, including shifted resonances for \(z=-2,0,2\) and two successive post-collapse iteration counts.

The numerical calculations only corroborate the analytical proof. The statement fixes each finite iteration count and does not provide uniform error bounds for growing iteration counts. The limiting map is undefined at the antipodal point, which has zero surface area. No independent mathematical review, certification or external validation was performed.
