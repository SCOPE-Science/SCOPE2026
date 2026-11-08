# Scientific review of the matching-deleted biclique resolving-set enumeration

## Correctness — PASS

The theorem is restricted to \(a,b\ge3\), which ensures that every two distinct vertices in one bipartition class have distance two, that deleted matching endpoints have distance three, and that all other cross-part pairs have distance one. The proof distinguishes the distance behavior of same-side and opposite-side pairs and establishes an exact criterion in terms of omitted deleted-edge pairs and unmatched omitted vertices. It then enumerates the two possible omitted-pair cases without double counting. The inclusion-minimality enumeration checks removability of every possible selected vertex type. The crown-graph limit follows from an exact binomial probability and its Poisson limit. An independent shortest-path implementation exhaustively checked \(15{,}872\) vertex subsets across \(41\) small graphs, including \(979\) inclusion-minimal resolving sets. The finite checks are corroboration, not infinite proof.

## Originality — PASS, with residual priority risk

Saputro et al., arXiv:1101.3624 (2011), prove that the ordinary metric dimension of the matching-deleted balanced complete bipartite graph is \(n-1\). That scalar theorem is recovered as a boundary case and is not claimed as new. Galby et al., arXiv:2206.15424 (2022), establish complexity and parameterization results rather than exact all-set or inclusion-minimal enumerators for matching-deleted bicliques. The inspected 2020 paper by Shahida and Sunitha treats other bipartite/resolvability questions; the 2024 article by Azhar et al. uses a different size notion, measuring induced edges within a resolving set. The general resolving polynomial for connected chain graphs already covers \(t=0\) and \(t=1\), since those boundary graphs are chain graphs; these boundary formulas are not independently claimed as new. For \(t\ge2\), an induced two-edge matching prevents membership in that class, and its result does not cover the remaining three-parameter theorem. Work on edge-metric bases of crown graphs concerns edge distances rather than distances to landmark vertices. A matching-deleted biclique formula in unindexed, inaccessible, or subsequently revised literature remains possible. The finding does not assert certified publication priority.

## Mathematical value — PASS

The parameterized family interpolates between complete bipartite graphs and crown graphs. A single structural criterion determines every resolving-set coefficient and every inclusion-minimal resolving-set coefficient, not merely an extremal parameter. In particular, it isolates the exact and sharp condition \(0<t<\min\{a,b\}\) for an upper-metric-dimension gap, and gives both multiplicities across the transition. Its crown specialization produces an explicit nontrivial probabilistic failure window for random landmarks. These are natural refinements of classical metric dimension questions, rather than a renamed scalar calculation.

## Scope and residual limitations

The theorem requires \(a,b\ge3\); small side sizes are intentionally outside its domain. Exhaustive tests cover only the specified finite range, and no independent human mathematical validation or priority certification has been performed. The arXiv primary sources were read in accessible full-text form; a relevant publisher page about bipartite metric dimension was access-restricted, but available comparisons do not indicate a competing complete enumeration.

Self-review: passed. Independent audit: not yet performed.
