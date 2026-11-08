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

# Verification

The proof uses a direct mod-one branch calculation, a five-case interval intersection, and exact integration. It does not depend on finite enumeration for any universal quantifier.

The accompanying `verify_orthogonal_tent.py` was executed directly using Python 3. It checked 18,224 exact-rational nonboundary torus-coordinate pairs for agreement between the four branch inequalities and the circular-arc table; it also compared explicit even-step itinerary membership for up to six pairs, and checked all four integrated triangular-area formulas at integers \(m=2,\ldots,29\). It printed:

`ORTHOGONAL_TENTS_EXACT_PAIR_INTERVALS_AND_SURVIVORS_OK grid= 18224`

`ORTHOGONAL_TENTS_EXACT_SURVIVOR_AREA_OK m=2..29 S4= 3/140  S6= 5/396`

An independent direct torus-iteration Monte Carlo spot check at the first several even times gave approximate proportions consistent with the exact rational formula, but no stochastic samples are required as proof. The full-branch initial distribution is distinct from the induced-return distribution in the cited paper. The assertion of almost-sure exit follows from the proven exact tail; no independent audit or external certification is claimed.
