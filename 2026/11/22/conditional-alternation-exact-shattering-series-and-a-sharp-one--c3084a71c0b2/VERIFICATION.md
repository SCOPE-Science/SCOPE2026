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

# Reproducibility

Execute `python3 verify_conditional_alternation.py` in a directory containing the standalone script, with Python 3.9 or newer. Its checks reconstruct the exact 14-state subset-antichain automaton, evaluate all potential inequalities, compare shattering to independently enumerated hypothesis traces at every length from zero through twelve, and verify 28 polynomial-series coefficients. If the `sympy` package is installed, it additionally performs the exact symbolic rational matrix elimination; this check was performed in the supplied run.

The recorded output is in `verification_output.txt`. The computation takes no external data or network access. Finite exhaustive observations are not themselves proofs for unbounded word lengths; the general proof is the state-space closure, rational transfer identity, potential inequality and explicit accepted paths in `RESULT.md`.
