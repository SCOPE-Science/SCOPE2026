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

A standalone Python 3 verifier is supplied as `verify.py`. Run `python3 verify.py` to repeat small exact Prüfer-word enumerations and coefficient/moment consistency tests. The executed checker returned 249 passed assertions and constants approximately \(\rho_2=0.308508322553671\), \(\eta_2=0.215269289248938\), and \(\sigma_2^2=0.195943902805589\).

The full infinite-domain claim rests on the exact multinomial/Prüfer formulas, first-order occupancy expansions with controlled tails, and the conditional characteristic-function proof, not on finite enumerations or truncated numerical series. The package contains neither an independent mathematical audit nor a machine-checked proof of the central limit theorem.
