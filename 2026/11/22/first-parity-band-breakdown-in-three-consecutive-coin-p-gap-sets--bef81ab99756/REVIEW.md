# Mathematical review: First parity-band breakdown in three-consecutive-coin \(p\)-gap sets

## Correctness

PASS: For each q=a+j (0<=j<=5), total coin layers q,q-1,q-2 alone can contribute, because a>=6 excludes a third lower layer. C_m(s)=floor(min(s,2m-s)/2)+1 for 0<=s<=2m yields the exact parity table. Checking q=a through a+5 and using d_a(n+a)>=d_a(n) determines every gap at levels h+1 through h+4, including terminal boundaries. Cardinality, isolated components and sum follow from disjoint intervals and arithmetic progression. A separately packaged exact DP checker passed for 98 even bases, 5,817,672 finite comparisons, 40,376 local formulas and 7,608 directly enumerated triples. Finite checks are corroboration only.

## Originality

PASS best-knowledge after statement and implication comparisons: Komatsu–Ying, Theorem 1 (first public 2022-06-27), treats p<=floor(a/2), not p=h+4. The first-post-boundary baseline covers t=1 but neither t=4 nor its first structural breakdown. The closest published three-phase Frobenius theorem covers the maximum only, explicitly does not give the genus or full gap set. Subwattanachai’s 2023 full article imposes a divisibility condition absent for consecutive pairwise coprime triples. Actual source and exact-parameter published-finding corpus searches found no equivalent. Risk of unindexed stronger work remains; search absence is not itself proof of priority.

The closest published comparators are Komatsu and Ying (arXiv:2206.13052, 2022), Subwattanachai (arXiv:2309.09149, 2023), and *Three exact phases of generalized Frobenius numbers for three consecutive denominations* (2026). The earlier first-post-threshold statement is treated only as baseline. Exact priority beyond these materials is not guaranteed.

## Value

PASS: The problem of how a p-numerical gap set changes immediately beyond the sharp classical p-Apery range is a concrete structural research question. The first three levels remain an interval plus h isolated gaps, while the fourth undergoes a new long-block transition and isolated count drops to h-1 uniformly in the unbounded even base. An exact gap-set classification simultaneously yields an unreported genus and gap sum. This is not a mere tiny numerical increment or a restatement of the known maximum.

## Limits

Only even \(a\ge6\), steps one, and the four specified thresholds are covered. No independent mathematical audit has been carried out. Potential equivalents in unindexed arithmetic-partition literature remain a residual uncertainty.

Self-review: passed. Independent audit: not yet performed.
