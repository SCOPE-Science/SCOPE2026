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

# Reproduction and limits

Run `python verify.py` with SymPy and SciPy. The code verifies the exact four-cycle polynomial identities, product-law identity, the quadratic center-manifold invariance equation, and the symbolic angular integral for the leading quartic energy drift. For positive biases 0.5 and 2, it integrates representative positive interior trajectories and tests agreement with the predicted inverse-time coefficient to the stated finite-horizon tolerance.

Successful observed output:

`VERIFY_OK exact_four_cycle=3 exact_product_law=1 center_manifold=1 quartic_average=1 finite_decay_examples=2`

The computer program does not prove global attraction, LaSalle's invariance conclusion, center-manifold existence, or convergence of the inverse-time limit. Those require the separately written analytic proof in `RESULT.md`. A numerical sample neither establishes an infinite-time limit nor excludes hidden invariant sets. Independent validation has not been performed.
