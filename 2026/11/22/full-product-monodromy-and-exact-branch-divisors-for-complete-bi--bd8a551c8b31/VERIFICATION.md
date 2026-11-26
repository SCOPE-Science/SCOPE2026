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

For distinct b_j the row map E_i ↦ F_i is invertible: evaluating F_i at b_j multiplies E_ij by a unit, and evaluation on degree ≤d is an isomorphism. On the stated open the parameters are therefore the boundary values, independent nonzero leading coefficients and independent monic polynomial coefficients, with P_i(b_j)≠0. Separate unordered generic root sets yield the product invariant field over both Q and its algebraic closure, and the product action is faithful on root tuples. Each universal discriminant has geometrically irreducible support, parameterized by monic polynomials divisible by (T−r)²; a generic point has exactly one double root and avoids all b_j and the other row discriminants. A transverse split of that double root gives an inertia transposition in exactly one factor and d^(m−1) tuple exchanges. The diagonal Jacobian tests étaleness and excludes other branch divisors on this open. The row trace determinant is the squared Vandermonde in the power basis; the tensor-product trace pairing gives the claimed exact determinant including its exponent. This also holds for d=2. The source checker was read, not executed. A separate bounded calculation (/tmp/opencode/review02_cubic_check.py) agreed with both listed cubic numerators, found both irreducible modulo 13, and reproduced discriminants 688908 and 94800 via Sylvester determinants. The nonsquare discriminants with distinct square classes suffice for the example, since any nontrivial common quotient of the two S₃ fields has a quadratic quotient. The generic proof does not depend on that example.

## originality

PASS

The equation and product upper bound are prior, as is attainment in K₂,₃. The reviewed increment is simultaneous attainment for all m,n with independent energies and the exact branch, trace-discriminant and inertia description on B, not a new theorem about generic polynomials in isolation.

## value

PASS

This settles whether a known graph-specific monodromy bound is attained uniformly, and obtains all codimension-one branching and its exact tensor trace multiplicities on the natural parameter open. These invariants distinguish the behavior of the graph cover from a bare degree count or isolated specialization. The useful step is identifying this genuinely unconstrained universal coefficient model despite the common boundary variables, not re-proving a textbook generic-polynomial theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
