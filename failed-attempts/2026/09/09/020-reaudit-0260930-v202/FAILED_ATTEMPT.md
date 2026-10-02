# Failed attempt

Date: 2026-09-30

The published claim did not satisfy the acceptance rule requiring PASS on correctness, originality, and value.

Final claim: For the 51 groups of order 32, the package gives exact distributions of nilpotency class, derived subgroup order, center order, Frattini rank, gamma3 size and class-2-quotient derived order, identifies three maximal-class groups with the listed invariants, and notes that every nonabelian group has class-2-quotient derived order at least 2, attained by 35 groups.

Non-passing axes: correctness, originality, value.

Correctness: UNRESOLVED. The actual table.json blob was parsed afresh and its aggregate counts exactly match the headline distributions: class 1/2/3/4 counts 7/26/15/3, derived orders 1/2/4/8 counts 7/17/24/3, center orders 32/8/4/2 counts 7/15/19/10, Frattini ranks 1/2/3/4/5 counts 1/19/24/6/1, gamma3 sizes 1/2/4 counts 33/15/3, and quotient-derived orders 1/2/4 counts 7/35/9. The three class-4 rows also match the reported extremal tuple. However, the binary representative bundle could not be independently replayed in this audit, and the inspected verifier recomputes class/derived/center/Frattini invariants but does not independently recompute every gamma3, quotient-derived, and conjugacy-class field. Thus the table arithmetic is verified but the complete from-presentations certificate chain is not.

Originality: FAIL. The scientific content is a recomputation of standard small-group catalogue invariants. The existence of exactly 51 groups of order 32 is established in the SmallGroups ecosystem and public group tables enumerate the groups. The three maximal-class groups are the classical dihedral, semidihedral, and generalized quaternion groups of order 32; their maximal-class status and basic invariants are standard. The lower bound on the class-2-quotient derived subgroup is a direct consequence of nilpotency: for a nonabelian finite 2-group, gamma2/gamma3 cannot be trivial, because gamma2=gamma3 would make the lower central series stabilize above 1. Hence the headline extremals are either catalogue aggregation or textbook deductions.

Value: FAIL. The aggregate table is reproducible and potentially convenient, but it is primarily a known-catalogue recomputation, while the highlighted quotient lower bound is a short general deduction. Under the stated value bar, correctness and reproducibility do not turn this into a worthwhile new mathematical gap.

The original scientific files and evidence must be preserved with this failed package. No disclaimer converts a covered, low-value, or unresolved claim into a passing result.
