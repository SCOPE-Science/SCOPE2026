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

The proof uses an exact first-step recursion for the first and second moments and strict discrete-convexity optimizations over integer subtree sizes. Finite independent checks are provided by `verify.py`: exact rational absorbing-chain moments on all rooted forms of nonisomorphic trees of orders 2–8, comparison with the fringe-subtree identity, sharp optimization, equality cases up to rooted isomorphism, and the asymptotic witness parameterization through the indicated finite range. The program is reproducible with Python 3, SymPy, and NetworkX. It does not certify the infinitely quantified theorem: the induction and integer-transfer argument do that. Neither external referee validation nor independent assessment has been performed.
