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

# Scientific verification

Extract the embedded `verify.py` and `requirements.txt`, install the listed SymPy dependency and run `python verify.py`. The checker was run successfully against the exact files in this record and reported `PASS`. It derives the equilibrium, Jacobian, homogeneous characteristic polynomial, each spatial quartic coefficient, both Routh–Hurwitz polynomial identities, the derivative of the modal threshold, and the three exact leading Neumann thresholds. This is an exact symbolic calculation, not approximate spectral sampling.

The all-mode comparison is analytic: one positive critical point of the rational threshold function, together with exact comparisons of lattice modes 3, 4 and 5. Exponential growth is a **linear** spectral result only. No numerical PDE simulation or nonlinear bifurcation analysis is claimed.

Historical priority remains literature-bounded because the related 2025 thesis was available as an indexed repository entry but its complete file was not accessible. No independent audit has occurred.
