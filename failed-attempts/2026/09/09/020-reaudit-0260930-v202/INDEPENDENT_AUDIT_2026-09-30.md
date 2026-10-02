---
audit_date: 2026-09-30
status: failed
---

# Independent mathematical audit

## Final claim

For the 51 groups of order 32, the package gives exact distributions of nilpotency class, derived subgroup order, center order, Frattini rank, gamma3 size and class-2-quotient derived order, identifies three maximal-class groups with the listed invariants, and notes that every nonabelian group has class-2-quotient derived order at least 2, attained by 35 groups.

## Correctness — UNRESOLVED

The actual table.json blob was parsed afresh and its aggregate counts exactly match the headline distributions: class 1/2/3/4 counts 7/26/15/3, derived orders 1/2/4/8 counts 7/17/24/3, center orders 32/8/4/2 counts 7/15/19/10, Frattini ranks 1/2/3/4/5 counts 1/19/24/6/1, gamma3 sizes 1/2/4 counts 33/15/3, and quotient-derived orders 1/2/4 counts 7/35/9. The three class-4 rows also match the reported extremal tuple. However, the binary representative bundle could not be independently replayed in this audit, and the inspected verifier recomputes class/derived/center/Frattini invariants but does not independently recompute every gamma3, quotient-derived, and conjugacy-class field. Thus the table arithmetic is verified but the complete from-presentations certificate chain is not.

## Originality — FAIL

The scientific content is a recomputation of standard small-group catalogue invariants. The existence of exactly 51 groups of order 32 is established in the SmallGroups ecosystem and public group tables enumerate the groups. The three maximal-class groups are the classical dihedral, semidihedral, and generalized quaternion groups of order 32; their maximal-class status and basic invariants are standard. The lower bound on the class-2-quotient derived subgroup is a direct consequence of nilpotency: for a nonabelian finite 2-group, gamma2/gamma3 cannot be trivial, because gamma2=gamma3 would make the lower central series stabilize above 1. Hence the headline extremals are either catalogue aggregation or textbook deductions.

### Equivalent formulations

Searches: groups of order 32 nilpotency class SmallGroup; order 32 maximal class dihedral semidihedral quaternion

Evidence: FiniteGroupDatabase lists all 51 groups of order 32; GroupNames identifies the standard maximal-class families.

Reasoning: The package's lane-local representatives are alternative labels for a classical finite catalogue.

### Broader coverage

Searches: maximal class 2-groups dihedral semidihedral generalized quaternion

Evidence: Standard classification of maximal-class 2-groups gives exactly these three families at order 32.

Reasoning: This broader structural theorem already determines the 'three class-4 groups' part.

### Exact database or table

Searches: groups order 32 database 51 SmallGroups

Evidence: https://finitegroupdatabase.com/o/32 and the GAP SmallGroups library context enumerate the 51 isomorphism types.

Reasoning: The aggregate invariant distributions are mechanically obtainable from an established complete catalogue rather than a newly motivated classification problem.

### Claim versus prior implication

Searches: nonabelian p-group gamma2 gamma3 quotient

Evidence: Lower-central-series definition for nilpotent groups.

Reasoning: If gamma2/gamma3 were trivial, then gamma2=gamma3; in a nilpotent group this forces gamma2=1, contradicting nonabelianity. Thus every nonabelian finite 2-group has nontrivial derived subgroup in the class-2 quotient without an order-32 census.

## Value — FAIL

The aggregate table is reproducible and potentially convenient, but it is primarily a known-catalogue recomputation, while the highlighted quotient lower bound is a short general deduction. Under the stated value bar, correctness and reproducibility do not turn this into a worthwhile new mathematical gap.

## Sources inspected

- artifacts/table.json blob 9650316bfaf3b2f31581d79333d2a02714c011eb
- artifacts/build_table.py blob dcc4deab6f920262b13268b6a6541fe51d89afb4
- artifacts/toolkit.py blob c6a32c89f51c5cd05044915efc0b67bacc945ba8
- https://finitegroupdatabase.com/o/32
- https://people.maths.bris.ac.uk/~matyd/GroupNames/
- https://www2.math.uni-wuppertal.de/~schuster/research/pdf/ord32.pdf
- Resultary semantic search

## Residual risk

Correctness of every per-group derived field remains unresolved because the full binary representative bundle was not independently replayed; this does not affect the scientific rejection, which already follows from originality and value.

## Disposition

FAILED. Acceptance requires PASS on correctness, originality, and value.
