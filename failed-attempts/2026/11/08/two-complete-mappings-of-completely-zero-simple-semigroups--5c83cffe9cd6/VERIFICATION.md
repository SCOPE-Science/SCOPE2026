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

If f is k-complete on a semigroup with zero, the preimage of zero under f also maps to zero under the product map and hence is zero. Any nonzero y with y^k=0 would produce another preimage of zero, at f^{-1}(y). Each zero sandwich entry in the Rees matrix produces such an element for every k>=2. Conversely, for nonzero p=p_{lambda,i}, the fixed-(i,lambda) multiplication is g*p*h in group coordinates, with identity p^{-1} and inverse p^{-1}g^{-1}p^{-1}; zero is its own one-element group. No subgroup can contain a nonzero element whose square is the absorbing zero. In a completely regular semigroup the maximal subgroups partition the elements, and in each, inversion is an involution with x(x^{-1})^2=x^{-1}. This checks the finite equivalence, necessity for all k>=2, and the infinite completely regular sufficiency, without using enumeration. As a check on the stated k=1 contrast, in B_n one may set f(i,j)=(j,i+j mod n), fixing zero; the product map sends (i,j) to (i,i+j mod n), so both maps are bijective.

## originality

FAIL

A distinct indexed result explicitly establishes a stronger finite-semigroup theorem with the same subgroupwise-inversion construction for k=2. The frozen finite Rees theorem and its higher-power necessary condition follow by identifying complete regularity with full support. This is demonstrated coverage, not a conclusion drawn from a search miss or a claim about the order of public release.

## value

FAIL

A short direct Rees proof is useful exposition, and the k=1 versus k=2 contrast is natural. As a new finding, however, this specialization closes no additional classification gap or supplies a new invariant: the stronger classification gives the same obstruction and specializes to the identical construction, while the coordinate translations are immediate Rees multiplication. No separately substantial new remainder was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
