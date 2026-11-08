# Scientific review

## Correctness — PASS

The universal part is proved without finite search: in a three-agent cyclic allocation of no more than \(6\) goods, any agent's initial turn precedes every other agent's second turn. Thus, whenever a rival obtains two goods, an agent can deviate on her first turn to secure that rival's later good and guarantee at least its singleton value by monotonicity. Equilibrium makes the actual utility at least that value, verifying EF1. The argument covers every ordered agent pair, all boundaries with at most one recipient good, and nonnegative monotone (not merely additive) valuations.

For the seven-good upper bound, the displayed integer matrix, exact subset recursion, tie-breaking and on-path allocation form a complete reconstructible pure SPNE certificate. `CHECKER.py` confirms all \(128\) states and \(448\) candidate actions, plus a separate history-recursion check of \(13{,}700\) game-tree nodes against `DP_CERTIFICATE.json` and verifies the strict envy gap \(1286-1120=166\). The additive sunk-value property makes each state's remaining-set continuation valid after every possible history. All singleton utilities are positive and the subset-value uniqueness follows from the low-bit perturbation argument. The computation establishes one explicit SPNE, **not** that every SPNE is non-EF1.

## Originality — PASS, qualified

The directly closest prior theorem is Goldberg–Hollender–Tyrovolas (arXiv:2609.18309, 2026-09-16), Section 4 and Table 3: it gives an online three-agent, **nine-good** example where every SPNE violates EF1, and a two-agent EF1 guarantee. Neither the existence of a nine-good non-EF1 example nor the two-agent positive result implies the sharp **seven-good** existential boundary for three agents. Its stronger *every-equilibrium* property is not claimed here. Amanatidis et al. (arXiv:2610.23686, 2026-10-16), Section 2 and Proposition 1, analyze **offline simultaneous ranking reports** and an **eight-good** PNE EF1 failure; those strategy spaces are different and do not imply the online cutoff. Supporting antecedent Kalinowski et al. (2013) studies sequential strategic allocation, without the stated cutoff. Multiple semantic research-index searches for online SPNE, seven goods, EF1, and equivalent characterizations returned no implicating record, and accessible earlier claims of this research series concern other sequential/resource-allocation properties.

There remains risk of an unindexed equivalent seven-good construction or another paper giving the cutoff. Searching is not proof of priority, and the novelty verdict is qualified until external review.

## Mathematical value — PASS

The number of goods required for **strategic EF1 failure** is a natural, finite exact invariant of the online cyclic mechanism; determining its sharp minimum addresses a meaningful boundary of a recently established failure phenomenon, not an arbitrary parameter slice. The result reduces the previously explicit online nine-good witness to seven goods while proving six goods universally safe, and it separates on-path contingent SPNE from the strategically different offline ranking-report PNE problem. A minimal, generic-valuations counterexample has direct use in benchmark construction and mechanism-design testing.

## Sources and limitations

- Goldberg, Hollender, Tyrovolas, *Equilibria of Round-Robin: Computational Hardness and Fairness for Few Subadditive Agents*, https://arxiv.org/abs/2609.18309 (Sections 2–4, especially Table 3).
- Amanatidis et al., *Revisiting the Fairness of Pure Nash Equilibria of Round-Robin*, https://arxiv.org/abs/2610.23686 (Sections 2–4).
- Kalinowski, Narodytska, Walsh, Xia, *Strategic Behavior when Allocating Indivisible Goods Sequentially*, https://cgi.cse.unsw.edu.au/~tw/knwxaaai13.pdf (2013; supporting precedent).

The finding is existential at seven goods, analytically universal only up to six goods, and specific to three agents with full-information cyclic online picking. The integer certificate verifies the constructive case but cannot establish novelty against inaccessible literature.

Self-review: passed. Independent audit: not yet performed.
