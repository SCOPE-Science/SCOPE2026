# Scientific review

**Claim assessed:** Exact expected-size difference between random-order greedy maximal independent sets on a path and on the graph obtained by closing its first four vertices to a cycle.

## Correctness — PASS

The first-arrival decomposition is exact for every order. The graph remaining after a chosen tail vertex splits into a smaller cycle-tailed component and a path; the five distinguished initial positions have explicitly enumerated residual graphs. This proves recurrence (1). The generating-function identity, alternating increment formula and positive-sign classification follow algebraically, not numerically. The standalone checker executed 516 rational assertions and independent enumeration checks. There is no extrapolation from finite experiments.

## Originality — PASS, with priority qualifications

Krivelevich, Mészáros, Michaeli and Shikhelman, *Greedy maximal independent sets via local limits* (arXiv:1907.07216, DOI:10.1002/rsa.21200), prove that paths minimize expected greedy size among **trees**, give the path formula, and exhibit a different example where deleting a bridge decreases expected greedy size. These statements do not provide the precise comparison for the bipartite unicyclic chorded path. Penrose and Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs* (arXiv:math/0503519), give general blocking-adsorption equations but do not state the evaluated four-cycle-tail sequence in the inspected results. The novelty claim is for the **specific exact family and its all-order sign/limit**, not for the already-known nonmonotonicity phenomenon.

The relevant full primary article sections were inspected, as were the process definitions and principal claims of the earlier adsorption study. Priority remains uncertain against less visible historical finite-graph calculations.

## Value — PASS

A single shortest-even-cycle edge perturbation is the most economical bipartite departure from a path, whose expected greedy occupancy is the extremal baseline among trees. The theorem identifies the exact effect at every order, two exceptional equalities, and a nonzero limiting gain with factorial correction. It gives a structural and quantitative boundary to edge-addition intuitions, beyond simply noting that edge monotonicity sometimes fails.

## Limitations

This is not a theorem about every chord, every unicyclic graph, or arbitrary edge addition. The expected gain is small, and the general nonmonotonicity phenomenon was known. The result has not undergone an independent mathematical audit or a comprehensive historical-priority review.

Self-review: passed. Independent audit: not yet performed.
