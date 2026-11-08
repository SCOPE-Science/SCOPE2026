# Scientific review: Near-linear optimal time-conscious delegation on interval hierarchies

## Correctness — PASS
The proof is a full structural induction over the prescribed rooted tree. For each child, all feasible time labels form consecutive integers; the parent compatibility windows include their respective integer indices, so their union has no missing integer. Intersecting one such interval per child with the parent's own uninterrupted availability gives the exact feasible-time interval, even for erratically changing horizons. The Bellman recursion sums independent conditional child optima. A heap sweep of weighted window intervals, combined with difference-array range additions, evaluates the recursion in \(O(S\log(2+S))\) operations and linear space. `verify.py` passed 5,750 brute-force comparisons of global optimal score and validated witnesses, plus the four-voter obstruction. This finite replay supplements but does not replace the universal proof. Risks: integer action times, fixed parent hierarchy and explicit values are essential.

## Originality — PASS (provisional)
The closest full source is Markakis and Papasotiropoulos, arXiv:2307.12898v1, Sections 2-4 and the appendices. It introduces the relevant temporal voting axioms and proves general NP-hardness, as well as different relaxations, but contains no all-score, arbitrary-trust-horizon interval-hierarchy algorithm. Related temporal branching (Bubboloni et al. 2023), constrained reachability (Brunelli and Viennot 2023), and static-tree delegation equilibrium (Escoffier et al. 2019) do not visibly state the same result. General tree-CSP dynamic programming is an acknowledged methodological precursor, not claimed as new. Priority risk: an equivalent specialized weighted-interval tree algorithm could exist in unindexed material; the full Bubboloni text and some related papers were not inspectable here.

## Value — PASS
The source problem asks for time-conscious, confluent, welfare-maximizing delegation. The fixed single-parent hierarchy plus contiguous approval windows is a practicable restriction that preserves both axioms. The exact interval propagation and near-linear welfare optimization handle nonmonotone temporal trust, not just retrospective trust, and the four-person obstruction shows that separate path feasibility is not enough. The result is structural and algorithmic, not a routine small-parameter numerical comparison.

## Boundaries and nearest literature
No claim is made for choosing parent recipients, multiple disjoint approval intervals, multiple independent casting roots or compressed input. The result is not an independent proof of publication priority and is subject to broader-coverage risk from general temporal-tree optimization literature. No independent external examination has occurred.

Self-review: passed. Independent audit: not yet performed.
