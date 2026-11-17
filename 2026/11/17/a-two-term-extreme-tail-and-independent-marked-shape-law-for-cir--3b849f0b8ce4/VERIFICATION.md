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

# Verification record

The proof's critical identities have the following independent checking paths: (i) global maximum by Jensen's strict concavity applied to the three central gaps; (ii) exact local MST wedge identity from the sine addition formula; (iii) an absolute Jacobian \(3r/2\); (iv) the uniform small-radius expansion of the deficit; (v) two-term integration of the exact cutoff; and (vi) \(L^1\) convergence of the normalized conditional wedge densities. These are mathematical arguments, not inferences from random simulation.

Run `python verify_mst.py` after installing `requirements.txt`. The checker performs a numerical root-quadrature evaluation for five small thresholds, verifies the two-term remainder scale, compares with an independently gridded two-gap simplex, and runs a seeded 2,400,000-triple iid simulation with a five-sigma probability check and loose finite-threshold marked-moment diagnostics.

The checker completed with `CIRCLE_THREE_POINT_MST_TWO_TERM_AND_MARKED_LAW_OK`. Its checks are reproducible but do not certify any limit, establish historical uniqueness, or amount to independent validation. The total-variation assertion concerns marked coordinates only; the coupled perimeter-deficit statement is weak convergence.
