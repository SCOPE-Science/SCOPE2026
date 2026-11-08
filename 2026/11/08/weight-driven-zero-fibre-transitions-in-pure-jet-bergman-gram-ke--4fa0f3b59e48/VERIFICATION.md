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

# Verification of the weighted pure-jet kernel theorem

## Reproduction
With Python 3, install `requirements.txt` and run `python CHECK.py` beside this file. The standalone checker was executed from the prepared scientific package path and returned `CHECK_OK 383 assertions; sharp scaling constant = 4.828427124746`.

The code checks the terminated hypergeometric/Jacobi transformation at rational weights, directly differentiates weighted Bergman kernels for several orders, compares transformed polynomial roots with an independent numerical root calculation, reconstructs Jacobi matrices from three-term coefficients, counts transition crossings and checks the fixed-order Laguerre contraction numerically. No external code, papers or non-embedded artifacts are needed to run the checker.

## Mathematical validity boundaries
Finite tests do not establish the theorem at arbitrary order or weight. The complete proofs of the exact phase count and both limits are in `RESULT.md`. The strict root movement rests on an explicit positive integral; the large-order limit rests on a Gershgorin/Rayleigh squeeze; the high-weight limit rests on the Jacobi-to-Laguerre polynomial limit. The potentially difficult ownership question is whether a weighted-jet phase characterization was previously published under orthogonal-polynomial terminology. Independent priority and proof audits have not been performed.
