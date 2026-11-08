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

# Verification performed

The analytic argument uses (i) the complete biclique polar-facet classification, (ii) the exact dual norm induced by a positive diagonal metric on the zero-sum hyperplane, (iii) a signed-partition minimum, (iv) symmetry of the convex body, and (v) a binary PARTITION reduction with explicit yes-certificates.

The included standalone standard-library Python checker tests the maximal centered facet distance with exact fractions by enumerating connected tight-edge labelings. It successfully covered 42 small weighted biclique profiles and 102 maximizing-facet observations, seven PARTITION examples, and 24 unweighted center-rank profiles.

Command: `python verify.py`

Observed marker: `DIAGONAL_BICLIQUE_INBALL_CHECKS_PASSED`.

The finite enumeration covers only the stated finite profiles, not all positive real metric weights. The proof provides the universal quantification. Historical novelty remains subject to discovery of equivalent results under weighted Lipschitz/variance terminology. Independent audit has not been performed.
