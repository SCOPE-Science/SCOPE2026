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

# Reproducibility and limits

The supporting-line proof and exact integrals are given in `RESULT.md`. A pure Python 3 checker (`verify_epicycloid_hulls.py`) numerically constructs polygonal convex hulls for seven integer cusp counts, compares their area and perimeter with the closed formulas, and tests contact coordinates and supporting-line maxima. The checker was executed from its exact embedded bytes with the message `EPICYCLOID_CONVEX_HULL_CHECKS_OK 7`. Finite discretization is not a proof for all cusp counts. The 2009 literature full text was not available, so the available abstract cannot rule out historical overlap. No independent mathematical audit has been performed.
