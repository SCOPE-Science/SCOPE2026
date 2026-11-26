---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The square-zero arrow span J is the Jacobson radical: the eventually constant quotient injects into the product of the coordinate fields and those evaluations have maximal kernels. Primitive quotient idempotents are exactly singleton indicators (every idempotent with larger support splits, including every cofinite one). The bimodule J over R/J is independent of representatives since J²=0, and its nonzero corners recover the directed ray. The unique source and its successive successors therefore fix all vertices. For a lift e_i+w, idempotence forces w to have only the incoming and outgoing coefficients, and e_i'e_{i+1}'=0 makes the two coefficients at a_i negatives. Each arrow image must be a nonzero scaling in its own corner. Conversely these formulas preserve all basis products, even in characteristic two, and every individual basis image has finite support. Composition and the explicit inverse give the unrestricted affine product. A unit is a diagonal with all entries nonzero and an eventually nonzero constant tail, plus finite arrow support. After scalar normalization and writing u=d+s, its inverse is d^{-1}-d^{-1}s d^{-1}; conjugation scales a_i by d_i/d_{i+1} and shears by s_i/d_{i+1}. Exactly the finite-support pairs occur: set d_i to the tail product of the prescribed scalings and s_i=c_i d_{i+1}. Truncating parameters on all arrows incident to a finite list of relevant basis elements gives local innerness; the everywhere-one shear with identity scaling is not inner. Over a finite field (also F_2) the product has continuum cardinality and each finite-support coset is countable, so the quotient has continuum cardinality. Inspected but did not execute the supplied finite-interval diagnostics; neither this proof nor its characteristic or support claims depend on them.

## originality

PASS

The supported distinct result is the simultaneous full, inner, and outer classification for the finite-support unitization of the one-sided square-zero ray, not discovery of the algebra or of the finite-quiver automorphism method. No inspected earlier or distinct indexed statement determines this support-sensitive classification on the same algebra.

## value

PASS

This is a natural structure invariant of a concrete algebra already used to separate homological dimensions. The computation distinguishes all automorphisms from global conjugations and gives an explicit obstruction at infinity: agreement with a conjugation on each finite set does not combine to a single conjugation. Even over F_2 the resulting outer group has continuum cardinality. The support distinction, rather than the routine finite-interval shear calculation, is the scientific payoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
