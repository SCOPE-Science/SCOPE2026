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

# Verification record

The included `verify.py` is a standalone Python 3 / SymPy script. Its exact symbolic assertions validate the invariant axial solution, the transverse Jacobian, both stationary solution branches, the Riccati coefficient expansion, the second-order scalar reduction, the Wronskian and the critical substitutions. Multiple rational parameter instances are also tested. Execute it from the extracted package with `python verify.py` after installing SymPy.

The long-time slow-mode construction requires scalar Riccati barrier comparison; the fast-mode construction requires an integral reduction of order and an asymptotic Gaussian tail estimate. Neither part is established by a finite run of the checker; the analytic argument is in `RESULT.md`. The local transverse linearization does not establish nonlinear basin geometry, nonlinear asymptotic stability or off-axis forward completeness. Independent mathematical audit has not been performed.
