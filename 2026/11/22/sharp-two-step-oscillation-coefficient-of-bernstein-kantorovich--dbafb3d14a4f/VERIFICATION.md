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

# Computational verification and scope

The exact-rational standalone program `verify_kantorovich.py` was run with a standard Python interpreter, testing degrees 1 through 14. It separately integrates the Bernstein basis over the averaging cells with rational polynomial antiderivatives, checks transition stochasticity and endpoint symmetry, computes the endpoint overlap, and compares every endpoint norm against values on a grid of 11 rational evaluation sites. It also checks the parity formulas and prints exact fractions.

Expected final output is `EXACT_ALL_TRANSITION_AND_TV_CHECKS_PASS`. Re-running the program is independent of any inaccessible package, network request or compiled dependency. The finite test grid does not prove the continuum maximum and the finite degree range does not prove the all-degree theorem or asymptotic; these follow from the separate analytical argument.

Scientific limitations: the operator is one-dimensional, unweighted, degree \(n\ge1\), with exactly two applications; no independent mathematical audit is claimed.
