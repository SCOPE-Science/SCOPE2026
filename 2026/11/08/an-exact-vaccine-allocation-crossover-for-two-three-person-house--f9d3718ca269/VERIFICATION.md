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

The exact proof is algebraic. The verifier `verification.py` uses independent exhaustive enumeration of all bond and importation configurations on complete graphs with up to three unvaccinated vertices. It uses `fractions.Fraction`, evaluates expected final infected sizes from graph traversal, compares them against the derived formulas, tests the sign classification on a rational grid, and checks rational examples and the equality boundary. It completed 2533 exact-rational assertions. Finite grid assertions do not establish the continuum theorem; the sign analysis in `RESULT.md` does. Independent audit has not been performed. Source priority is provisional, particularly regarding inaccessible older household-vaccination articles.
