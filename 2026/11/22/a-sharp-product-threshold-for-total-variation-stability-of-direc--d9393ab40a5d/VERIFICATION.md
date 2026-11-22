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

# Reproducible checks

Run `python verify.py` with the Python standard library. The code uses exact fractions for the range affinity \(\rho(t)=1/(1+t^2)\). It verifies the derived edge-transport and exact dissipation identity on 6,000 deterministic test inputs under admissible left/right weights, verifies explicit reversed-edge counterexamples under products above one, and checks equality of total variation for nonconstant monotone step input on 33 finite cases.

The proof of the unrestricted classification is written in `RESULT.md`; the finite tests do not prove quantification over every real signal, every admissible affinity, or unbounded path lengths. Independent assessment has not been performed.
