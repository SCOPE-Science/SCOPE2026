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

Images of the generators lie in the nilpotent maximal ideal. In the graded splitting, an automorphism is specified by an invertible L on V and any Q:V→Sym²V, and its square has linear part L² and quadratic part QL+(Sym²L)Q. In characteristic two L²=I iff (L−I)²=0; its rank-r square-zero part is counted by an image, a containing kernel, and an isomorphism from the quotient onto the image, including r=0. Independently, put L into a basis with r swapped pairs and s=d−2r fixed variables. The induced monomial permutation on Sym²V fixes exactly r+s(s+1)/2 degree-two monomials. The remaining two-orbits give rank (D−r−s(s+1)/2)/2=r(d−r) for Sym²L−I. On a swapped pair the image of one generator freely determines the other, while each fixed generator must map to the (D−r(d−r))-dimensional fixed space. Thus the fiber exponent is rD+s(D−r(d−r)), as claimed. For large d the ratio of each rank-r term to the r=0 term is bounded by c_q^(−2) q^[2r(d−r)−rD−(d−2r)r(d−r)], at most c_q^(−2) q^[−r d(d−3)/2]. Summing the resulting geometric bound verifies the fixed-q concentration. Composition adds Q in the identity-linear subgroup and all its nonzero elements have order two. Removing the identity changes only the order-exactly-two total by one. At d=1 the r=0 term alone gives q; substituting d=2,3 yields the stated three example totals.

## originality

PASS

The distinct claim is the exact cotangent-rank census and its fixed-truncation, growing-dimension concentration for square-one automorphisms of the commutative cubic jet algebra in characteristic two. The normal form, classification of linear involutions, and elementary cyclic-module calculations are ingredients, not claims of new general theory. The most relevant distinct actual Findings change the multiplication, the characteristic, the truncation limit, or the map being counted.

## value

PASS

This is the first commutative jet cutoff with a nontrivial quadratic lift space. Here the cotangent action of a square-one map does not determine its nonlinear possibilities, particularly when the characteristic divides two. The uniform stratum count measures that distinction for every dimension and finite field of characteristic two, and the resulting concentration distinguishes trivial cotangent action from actual triviality of the automorphism. The exact census is useful in its own right as a comparison with tensor-algebra and higher-order jet statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
