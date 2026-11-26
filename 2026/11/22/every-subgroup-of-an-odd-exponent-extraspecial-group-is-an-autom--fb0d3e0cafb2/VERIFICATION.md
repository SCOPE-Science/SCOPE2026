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

For an extraspecial group of exponent p, the alternating commutator form gives the stated Heisenberg model. The center has prime order, so its intersection with a subgroup is either the entire center or trivial. In the first case the subgroup is U × F. Splitting U into its nondegenerate part W and its radical R and completing R to a hyperbolic block gives a symplectic map that is the identity on W, a shear fixing exactly R on R ⊕ R*, and minus the identity on the orthogonal complement. Its fixed space is exactly U. In the second case the subgroup is a linear graph over isotropic U. Identity on U, minus identity on U*, and the stated 2-by-2 block B on each remaining plane give a common multiplier −1; det(B−I)=−1, so exactly U is fixed on the quotient. The central equation 2z=2ℓ(u) gives exactly the graph. This includes the smallest prime, the trivial subgroup and all zero-size blocks. A separate bounded replay found all 19 and 39 subgroups at p=3 and p=5 respectively, with an automorphism checked for each by testing multiplication, bijectivity and exact fixed points.

## originality

PASS

The supported contribution is exact realization of each subgroup throughout the odd-prime exponent-p extraspecial family, beyond the previously identified order-27 example. No inspected source states or implies that all-rank, all-subgroups result.

## value

PASS

This resolves the fixed-subgroup-realization question constructively for a natural nonabelian family in every rank. The result shows the entire subgroup lattice is realized, not just subgroup orders or fixed-point-free behavior. The two constructions handle independently the nondegenerate/radical fixed quotient and the central graph condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
