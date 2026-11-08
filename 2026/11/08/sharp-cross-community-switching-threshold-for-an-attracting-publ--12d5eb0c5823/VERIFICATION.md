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

## Reproduction

Run `python CHECK.py` with SymPy installed, from the directory containing the files. It proves the payoff-advantage identity by symbolic simplification; verifies the proposed two-block affine switching equations and the algebraic equivalence of the switching inequality to the stated cutoff; reconstructs the exact four-player period-two trajectory, its strict switching margins and the eigenvalues of its two-step opinion Jacobian using rational arithmetic; and checks 360 reproducibly seeded rational parameter triples for the cutoff equivalence and affine identities.

The executable passed in the assembled working directory before inclusion. The general theorem follows from the written analytic proof and is not inferred from finite testing. No independent review is claimed. No global attractor census, stochastic simulation, or field validation was performed.
