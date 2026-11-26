---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For q>=3, n>=1 and 3<=t<=q, diagonal translates over the cyclic alphabet partition the words into q^(n-1) full cliques, each meeting a K_t-free set in at most t-1 vertices. The one-coordinate cylinders attain the bound. At equality every full transversal is saturated: relabel symbols independently in each coordinate to make that transversal a member of a diagonal partition, then apply equality in the sum of the per-clique bounds. For n>=2, the two tuples (a,u),(b,v) with coordinatewise-different u,v, and their swap (b,u),(a,v), can be completed by the identical remaining q-2 tuples by filling each column with its unused symbols. Subtracting the two saturation equalities gives the same coordinate increment at u and v. The disagreement graph on the remaining coordinates is connected by a common neighbor chosen coordinatewise outside the two given symbols. Increments therefore do not depend on context. Telescoping from a base tuple proves additivity. If two coordinate functions were nonconstant, choosing a low and high input in each gives a strictly increasing chain of three values by changing the two coordinates successively, impossible for a Boolean function. The nontrivial cardinality forces exactly one relevant coordinate and t-1 selected symbols. The descriptions are distinct for different coordinates since varying one while fixing the other changes membership in only one cylinder. For n=1 the complete graph gives the same classification directly. The frozen proof handles all parameters including t=q and requires no field; the supporting verify.py and recorded small checks were inspected but not executed and do not prove the universal result.

## originality

FAIL

The rigidity is a direct consequence of the known full dimension of the axial multi-index assignment polytope (Appa–Magos–Mourtos, 2006, Theorem 9, as specifically identified and described with scope in Lee §4.3) and the standard Boolean degree-one classification on product domains (Filmus–Ihringer Theorem 7.1). The equivalence is exact: a full transversal clique is a strength-one index-one orthogonal array, i.e. an axial assignment. The per-coordinate marginal equations give the full affine hull by the axial dimension theorem. Consequently, any real weight with constant sum on every full transversal is a linear combination of coordinate marginals, which is stronger than the target's additivity step for Boolean weights. Uniform averaging over transversals gives the elementary bound and forces these constant sums at equality. Applying the Boolean theorem and counting selected symbols gives exactly the target's rigidity and count. This is not an inference from the same numeric maximum in a distance-one graph or from the date of Lee's exposition. The original 2006 full text could not be retrieved, but the exact all-order theorem is described in an accessible mathematical source, and the implication is exhibited below.

## value

FAIL

The graph endpoint and extremizer question are natural. The numerical bound is a one-line averaging or partition argument; the rigidity and count follow immediately once the known axial-affine-hull and Boolean degree-one results are translated. The swap proof is a valid self-contained presentation of the needed additivity fact, but this record establishes no stronger result beyond those known ingredients and their routine application. No distinct new exact or structural contribution remains to preserve in a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
