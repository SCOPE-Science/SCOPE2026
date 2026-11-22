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

# Finite checks and proof boundary

Run `python3 verify_antiprism.py` with Python 3 (standard library only) to independently check facial sums in twelve cyclic-product abelian groups, each across \(3\le n\le13\), verify exact ordinary/strong counts and permutation orbits, exhaust all nonzero vertex assignments in ten small cases, and check the strong generative \((\mathbb Z/4\mathbb Z)^2\) count.

Expected checked output:

```
ALL_AB_GROUP_TWO_SEED_COUNTS_AND_ORDERS_PASS 132
INDEPENDENT_FULL_VERTEX_EXHAUSTION_PASS 10
FINITE_GROUP_FULL_SYMMETRY_ORBIT_FORMULA_PASS
FOUR_TORSION_AND_GENERATIVE_C4xC4_96_PASS
VERIFY_OK
```

Separately, integer Smith-form computations on facial incidence matrices for \(4\le n\le12\) found \(2n\) unit invariant factors for \(3\nmid n\) and \(2n-2\) unit factors otherwise, without nonunit factors. Small automorphism enumeration for \(4\le n\le7\) obtained \(4n\) automorphisms. These finite checks are supporting evidence, not an infinite proof or external certification; the unrestricted argument is in `RESULT.md`. All checks described here are tests actually performed.
