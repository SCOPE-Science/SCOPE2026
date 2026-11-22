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

Run `python verify.py` with Python 3.9+ and its standard library. The program uses exhaustive weak integer compositions for circular gaps at four through seven vertices, independently compares direct point-deletion predicates against the cyclic two-gap rule, checks that more than two pivotal vertices never occur on the grids, evaluates rational probability identities for each integer from 4 through 200, and uses reproducibly seeded auxiliary Dirichlet samples. The geometric comparison grids intentionally have odd total mass so no half-circle tie can occur. All mathematical claims for a continuum of configurations are proved in `RESULT.md`; these finite checks are consistency tests only.

The published Wendel paper was read in full text, and its original scalar identity was compared with the new deletion count; the spindle-convex Wendel variant was read in the available full online article. No independent mathematical audit has been performed. Historical priority against unidentified equivalent coverage results cannot be guaranteed.
