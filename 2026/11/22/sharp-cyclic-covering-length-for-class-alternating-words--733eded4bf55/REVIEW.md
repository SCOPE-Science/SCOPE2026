# Scientific review

## Correctness — PASS
The claim is a minimum over single class-alternating circular words. The proof converts circular windows to a closed walk in the full directed alternating overlap graph. For even window length, the mandatory edge set is already Eulerian. For odd window length, every vertex in the lower-outdegree class has exactly the same positive deficit, so summing deficits gives the rigorous lower bound on additional edge occurrences. The rotation permutation \(v_1\cdots v_{2r}\mapsto v_2\cdots v_{2r}v_1\) matches all deficit vertices bijectively to complementary surplus vertices by existing edges; multiplying those edges by the class-size difference gives a balanced strongly connected graph and an Euler circuit. No asymptotic approximation or unchecked numerical certificate is required. The standalone construction tests pass in 80 small families, plus eight exhaustive small-case sharpness checks. Finite tests are supporting evidence only.

## Originality — PASS, qualified
Champlin–Godbole–Tomlinson (arXiv:1303.3323, 2013, Theorem 4) already identify the odd-length indegree/outdegree imbalance and establish existence of exact-one-factor universal cycles in balanced cases. The new claim explicitly does not appropriate that antecedent. It determines the sharp shortest length and a realizable minimum repeated-window multiset in the unequal-size odd case, which the inspected original theorem does not imply. Kreitzer–Nica–Pereira (arXiv:2306.01498, 2023, Definitions 4–6 and Theorem 3) prove existence of an asymmetric alternating sequence covering only one of the two possible odd-window starting classes; their Example 6 has missing windows of the other class. Even when their sequence length numerically matches this optimum, the previously stated weaker covering property does not entail the stronger simultaneous coverage here. Indexed comparisons with run-limited and different forbidden-factor cyclic-cover results are not directly applicable. Earlier unindexed equivalent Eulerizations remain possible.

## Mathematical value — PASS
An earlier feasibility theorem leaves a natural incomplete quantitative problem precisely in the unbalanced odd regime: how much repetition suffices if a universal exact-once cycle is impossible? The exact minimum surplus \((ab)^r|a-b|\), its parity dependence and an explicit all-parameter optimal construction provide a useful complete solution for class-alternating universal-factor scheduling and constrained-word superstrings. The result goes beyond an isolated numerical value or cosmetic reformulation of a prior existence statement.

## Closest literature and limitations
1. Champlin, Godbole, Tomlinson (2013), *Universal Cycles of Complementary Classes*, Theorem 4, https://arxiv.org/abs/1303.3323 .
2. Kreitzer, Nica, Pereira (2023), *Using alternating de Bruijn sequences to construct de Bruijn tori*, Section 2.3 and Section 3, https://arxiv.org/abs/2306.01498 .

The result does not count optimal covers or analyze linear covering hosts; an older unindexed theorem could have an equivalent shortest-cover formulation. No outside independent mathematical validation is represented by the checks here.

Self-review: passed. Independent audit: not yet performed.
