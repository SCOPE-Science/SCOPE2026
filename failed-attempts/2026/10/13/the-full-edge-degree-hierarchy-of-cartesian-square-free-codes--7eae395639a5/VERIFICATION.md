---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The ordered Cartesian factors contain zero and at least one nonzero point each. The m monomials M_i omit exactly one variable; evaluating on points with that variable zero and all others nonzero isolates each M_i, proving independence. Their shadows in Theorem 3.2 are Q⊔Z_i with Q the all-positive exponent box of size P and Z_i the disjoint slice of size P_i=P/(n_i−1). Hence the theorem gives P plus the sum of the r smallest P_i, including ties and r=m. An independent proof works directly with supports: let J be the set of active coefficient coordinates in an r-subspace W of the monomial span, so |J|≥r. On one-zero slice j the support is the full slice iff j∈J; points with two or more zero coordinates are never supported. At all-nonzero points, divide the value by the product of coordinates: evaluation becomes a linear form in the reciprocals of the coordinates. If |J|=r, W is the whole coordinate span on J, so it supports the entire nonzero core. If |J|>r, select any r-subset I⊂J and some j∈J∖I. A single word with coefficient j nonzero determines the j-th reciprocal from the others at any common zero in the core, so at most P_j core points are lost; the gain on the extra slice j offsets that loss. In both cases support is at least P+Σ_(i∈I)P_i, with equality achieved by the optimal monomial span. For projective dimension m≥1 the affine origin has a zero column (degree m); each projective coordinate appears q−1 times up to nonzero scaling on scalar multiples in the punctured affine set. With m+1 affine variables of size q, dividing the affine weight (q−1)^m(q−1+r) by q−1 proves the stated projective formula for the whole rank range. This proof covers the parameters without relying on the frozen finite experiments.

## originality

FAIL

The full formulas are not displayed all at once in the primary source, but are mechanically implied by its exact all-rank shadow theorem and projective replication lemma. At this degree the only shadows are the m omit-one shadows; every intersection of two distinct shadows is the same positive core. The minimum is therefore simply the common-core size plus the r smallest disjoint-slice sizes. The projective step is precisely the prior scaling, not a new weight comparison. This is prior implication, not an allegation of verbatim duplication.

## value

FAIL

Generalized weights and the edge-degree family are natural, and the formula makes a useful example. But its all-rank entries are an immediate disjoint-union count and sort inside a theorem giving the exact minimum over those shadows, with projective scaling already established. The frozen claim does not survive as a nonroutine unknown exact invariant or as a result about a broader class or all optimizers. Correcting the bibliography would not change that scientific conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
