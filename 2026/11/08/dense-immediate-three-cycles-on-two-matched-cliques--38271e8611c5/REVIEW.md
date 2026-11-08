# Scientific review

## Correctness — PASS

For a connected graph, a nonfixed configuration with three-step return must have every vertex cycling through all phases; otherwise a permanently resting vertex adjacent to a rotating vertex would be forced to excite. The successor-neighbor criterion is both necessary and sufficient. The two-clique support classification exhausts all possibilities, including the forbidden configurations with two colors on each clique. The factor \(6\) in the mixed-support case comes from choosing which clique is two-colored and which of three colors it omits. Exact inclusion–exclusion gives \(9^n-6\cdot6^n+15\cdot4^n-12\cdot3^n+3\). Boundary cases \(n=1,2\) give zero. Code independently checks all \(597861\) states for \(2\le n\le6\) and an independent mask-transfer for \(1\le n\le60\); finite computations are corroboration, not the infinite proof.

## Originality — PASS (best-knowledge, qualified)

The materially inspected primary work of Gravner–Lyu–Sivakoff, arXiv:1610.07320v1, defines the same Greenberg–Hastings rule and gives broad synchronization/activity criteria on arbitrary connected graphs (particularly its Theorem 3), but not the immediately primitive-three count on the one-parameter matched-clique family. The graph \(K_2\square K_n\) also goes by the name the line graph of \(K_{2,n}\). Searches using both graph descriptions and formula-based variants found no covering statement. A 2022 study of graph-dependent synchronization prediction uses different questions and is not a tabulation of the exact initial period-three population. A finite census on another rook-graph size or an activity formula does not, without additional argument, imply this all-size closed formula. Unindexed and implicit equivalent-count literature is a residual novelty risk; lack of a search hit is not treated as proof of uniqueness.

## Mathematical value — PASS

This is the exact naturally defined initial periodic-state population of a connected homogeneous graph family, not an arbitrary graph slice or an ad hoc numerical statistic. The classification shows that both two-color layers are impossible, and supplies an explicit exponential-rate law: almost every initial state starts in a genuine three-cycle when the clique sizes grow. The probability tending to one is a meaningful sharp contrast with sparse finite-range excitation networks. The count also gives all primitive-three orbit numbers without quotienting labels. Neither a paper-sized result nor a downstream theorem is claimed.

## Closest literature and limitations

Gravner, Lyu and Sivakoff (2016; arXiv:1610.07320v1) provide general long-run dynamical criteria, not this exact immediate count. Bassi and collaborators (2022; DOI:10.1038/s41598-022-18953-8) study empirical synchronization prediction rather than this exact enumeration; complete direct inspection of the latter source was obstructed by a site access check and it is used only as context. Potentially equivalent enumerations under cyclically dominated colorings or graph line-graph language remain a priority risk. No claim is made about remaining periods or transient basins. The verification programs use distinct computational approaches, but independent scientific audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
