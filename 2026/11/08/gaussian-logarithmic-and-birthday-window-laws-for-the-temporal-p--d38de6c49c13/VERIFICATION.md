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

# Reproduction and verification

Run `python3 check.py` using Python 3 with standard-library modules only. The program exhaustively verifies 848 small temporal approval profiles by evaluating literal PJR, EJR and EJR+ requirements against every candidate-multiplicity vector; it checks 62 finite sparse occupancy factorial-moment identities against direct enumeration. Seeded simulations provide additional sanity checks for the fixed-party and linear-party regimes and the three birthday windows. All limit theorems require the analytic argument in `RESULT.md`, including the exact bin-pair variance and Poisson factorial moment proof. Finite enumeration does not establish asymptotic claims. The independent-audit status in the front matter is unperformed; this is not an independent certification.
