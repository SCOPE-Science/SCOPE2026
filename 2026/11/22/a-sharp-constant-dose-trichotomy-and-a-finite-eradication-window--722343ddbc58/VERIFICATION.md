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

# Reproduction of the calculation

Run `python3 verify_calculations.py` with Python 3 and no third-party modules. It verifies the exact rational example and the closed stationary equations using integer/rational arithmetic, then probes the eigenvalue-derivative signs, optimality transitions, and singular scaling over representative numerical grids.

The executable does **not** prove that every admissible parameter tuple has at most one stationary point, nor that an asymptotic remainder holds uniformly. Those are analytic arguments supplied in RESULT.md using monotone one-way crossings and a local series inversion. The code contains no stochastic clinical efficacy estimates and the theorem does not extend to finite noisy measurements.
