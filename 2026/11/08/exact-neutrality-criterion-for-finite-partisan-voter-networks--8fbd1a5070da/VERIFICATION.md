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

# Reproduction and scope

Run `python3 check.py` with Python 3 and the standard library. It enumerates the state-change generator with exact rational arithmetic on connected paths, cycles, a star and a triangle; tests the local generator identity; compares all possible preference assignments with the proposed proper two-colouring criterion; and solves finite absorbing-chain linear systems for the exactly neutral cases. A contrasting all-positive-preference triangle gives a non-neutral exit probability of \(9/13\).

The full all-graph proof is mathematical and does not rely on finite enumeration. It depends on the positivity of all active copy transitions for \(0<\varepsilon<1\), a finite-state absorption argument, one-step generator identities, and the uniqueness of the stationary measure of the simple random walk on a connected graph. Tests are not a proof for untested graph sizes.

The supplied parameters and file are sufficient to reproduce the arithmetic; no third-party data files or network services are required. Independent scientific audit has not been performed.
