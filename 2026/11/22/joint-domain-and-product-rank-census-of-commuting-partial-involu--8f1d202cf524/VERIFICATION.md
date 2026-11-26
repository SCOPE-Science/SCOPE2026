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

Injectivity and s³=s make s² the identity on the domain, and s is an involutive permutation there. For every i,j, s_i commutes with e_j=s_j²; the domains of the two compositions with this partial identity show that a defined s_i preserves both membership and nonmembership in D_j. A point therefore stays in the same membership block whenever any defined map acts. On a block with active set S, the named restrictions are a full (C₂)^S action with no faithfulness condition. Conversely arbitrary disjoint labeled such actions, undefined for inactive coordinates, give the required tuple, including empty blocks. A transitive action has a uniquely determined subgroup H, and by abelianness the equivariant automorphisms of (C₂)^S/H are precisely the translations, of number 2^r for r=codim H. On 2^r labels this gives (2^r)!/2^r actions per H; its EGF term is u^(2^r)/2^r. Ordered names are preserved, so there is no further quotient by coordinate permutations. The product is defined exactly on the all-active block, where it is an involutive permutation; multiplying the corresponding weights across the labeled set of orbits gives the master EGF. The empty carrier contributes 1, and t=1 correctly marks identical individual and product ranks. For t=2 the exponent is 4u+5u²/2+u⁴/4; logarithmic differentiation gives the stated recurrence, including the zero-index conventions, and a_6=45061. The supplied computations/checker.py and verification notes were inspected, not executed; the reported finite checks compare full marked strata and are not the all-parameter proof.

## originality

PASS

Credit is limited to the labeled multivariate census for pairwise commuting partial involutions, with all partial-domain blocks and the product-rank marker. The earlier commutation criterion supplies domain invariance for involutions, and labeled orbit counting for total actions is standard. Neither is claimed as new. The inspected results do not furnish a census encompassing this one. Turning the pairwise local criterion into an arbitrary-arity bijection with a labeled set of colored transitive actions, and identifying how joint partial-product rank behaves on those components, is the additional enumeration argument.

## value

PASS

The domain ranks and the domain rank of composition are natural simultaneous observables of partial permutations. The formula turns a global pairwise-commutation census into a tractable product of local labeled action counts, giving a usable all-size all-arity expression and the exact rank-conditioned coefficients. It applies to inactive and nonfaithful components as well as total actions. The usefulness comes from the full structural and marked classification, not a known group-action count or a list of a few small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
