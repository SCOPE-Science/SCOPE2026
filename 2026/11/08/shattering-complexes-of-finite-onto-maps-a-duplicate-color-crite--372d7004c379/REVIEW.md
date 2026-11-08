# Review of shattering complexes of finite onto maps

## Correctness

**PASS.** The proof reconstructs necessity from mutually exclusive row labels, the full-row missing-color obstruction, and all-positive color coverage. For each proposed positive subset it proves an explicit Hall condition for missing colors: at least two demanded colors are adjacent to all unassigned rows, and one demanded color has access to an unqueried row. Thus all dichotomies extend to surjections. The Stirling sum and facet count follow by disjoint cases, and the matroid boundary follows from partition-matroid truncation for two colors and a concrete basis-exchange failure for three or more. Complete finite support enumeration (104,272 cases across eight parameter pairs) and 15 exchange-witness checks corroborated the derivation. The unrestricted assertions are proved, not inferred from the finite sample.

## Originality

**PASS within the accessible comparisons.** Leboeuf--LeBlanc--Marchand (arXiv:2210.10781, 2022) considers categorical equality decision-stump partitions, not the binary incidence traces of all globally surjective assignments. Godbole--Pinella--Zhuang (arXiv:1301.6371) treats random word/permutation covering patterns with a different shattering object. Bucic et al. (arXiv:1906.05908) treats intersection statistics of perfect matchings rather than exact support shattering. The bijective boundary is known as a perfect-matching setting and is not separately claimed new. Actual synonym, implications, exact-table and record searches did not surface the all-parameter n>q criterion and matroid boundary. Historical priority under alternative terminology remains uncertain.

## Value

**PASS.** The exact duplicate-color obstruction and full face polynomial describe every allowable binary query support for a natural constrained categorical class. Purity and the matroid-versus-nonmatroid transition sharply distinguish the two-color and higher-color cases, giving structural information not supplied by the VC dimension alone.

## Scope and limitations

For n>q>=2 only; binary equality-incidence supports rather than arbitrary multiclass shattering. Does not establish Littlestone dimensions, homological consequences, or results for prescribed fiber quotas. Finite verification does not prove the all-parameter theorem; the proof does. Historical priority is not independently certified.

Self-review: passed. Independent audit: not yet performed.
