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

# Verification and scope
The mathematical proof is complete in `RESULT.md`. The bounded exact-rational diagnostic `CHECK.py` was run with the packaged source contents and returned `MUTATION_SYMMETRY_EXACT_FRACTION_CHECKS_OK`. Its tests cover the exact sum and pairwise difference identities, the reduced-plane formulas, strict negative Dulac divergence, and algebraic endpoint signs across representative rational inputs. They do not exhaust any continuum of parameters. The step from a three-dimensional omega limit to a singleton equilibrium depends on the standard theorem that omega-limit sets are internally chain transitive and on the planar Poincaré–Bendixson recurrence classification; a reader should review this application explicitly. Independently checking the origin paper's full preprint was possible; a search of all later related literature is inherently non-exhaustive. An independent mathematical audit has not been performed.
