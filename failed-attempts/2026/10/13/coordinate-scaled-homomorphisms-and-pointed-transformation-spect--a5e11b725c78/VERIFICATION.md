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

Dietzel–Menchón–Vendramin Thm. 5.9 uses the coordinatewise ordered direct sum of integer chains; sign reversal and deletion of inactive coordinates give the asserted finite downsets, including the singleton. A coordinate h of a homomorphism satisfies h(0)=0, and for distinct active indices e_i•e_j=e_j makes h(e_i) and h(e_j) unable to be simultaneously positive. If a_i>0, the two ordered differences between a and a-e_i force h(a)-h(a-e_i)=h(e_i), so telescoping proves the normal form. Each such coordinate map preserves the operation, is monotone, and lands in the target exactly when all maximal source images do. For a full box target the choices are independent, with floor(t_j/r_i) nonzero scales for source i; active unit vectors distinguish the choices. For equal positive side length r, all nonzero scales equal 1. Writing coordinate-copy maps by a pointed function τ gives reversed composition; bijections are exactly coordinate permutations. With k nonzero selected inputs, independent values give image cardinality (r+1)^k. Pointed fibers partition m+1 labels into k+1 blocks with the zero block distinguished. Choosing k nonzero input labels and assigning them to the other blocks gives the stated unrestricted count. An idempotent fixes exactly its used indices, hence choose k fixed nonzero labels and map each remaining index to one of those or zero. Its embedded image sees only the partition: the zero block is forced to zero and other blocks have independent values. Every partition arises by choosing a fixed representative per nonzero block; distinct partitions give distinct sets since r≥1. The three formulas reproduce 64, 23 and 15 at m=3.

## originality

FAIL

There is affirmative broader coverage: Rump's The Category of L-Algebras (2023), Prop. 2.4 and §3 before Thm. 3.3, give preservation of partial multiplication and the self-similar reflector; Thm. 3.3 identifies its value on a monoid-generating subalgebra. Specializing to the Dietzel–Menchón–Vendramin diagrams makes every map a restriction of a cone morphism preserving additive monoid multiplication. The one-sparse coordinate rows are then forced by a relation on pairs of basis vectors. The remaining assertions are the coordinatewise admissibility test and ordinary pointed-function/fiber counts under that specialization. This is direct implication, not an inference from a similar title, and does not depend on access to Rump's earlier 2008 paper.

## value

FAIL

The explicit coordinate description can be useful exposition. As an independent finding, however, after applying the known theorem on L-algebra morphisms to the known representation, the additional checks and formulas are separate coordinate bounds and standard pointed-set partition counts. The record identifies no nonroutine restriction, counting problem for nonrectangular targets, or additional structural inference that would give the remaining exact counts independent research value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
