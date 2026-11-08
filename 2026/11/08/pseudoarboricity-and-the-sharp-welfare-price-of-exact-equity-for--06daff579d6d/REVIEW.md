# Scientific review

## Correctness — PASS

The object is a normalized binary approval instance with every item approved by one or two agents and every agent approving exactly \(D\) goods, for \(n\ge3,D\ge2\). The maximum exact-EQ level is determined by a capacitated Hall matching: \(t_*=\min_{S\ne\varnothing}\lfloor |N(S)|/|S|\rfloor\). For the double-approval multigraph, \(|N(S)|=D|S|-e_G(S)\), giving \(t_*=D-\lambda(G)\), with \(\lambda(G)\) the ceiling of the maximum edge-per-vertex density. Since \(\lambda(G)\le\lceil D/2\rceil\), each maximum-EQ allocation has utility at least \(\lfloor D/2\rfloor\); its cross-bundle approved value is at most \(D-t_*\le t_*+1\), proving EF1. Every unmatched item can be assigned to a nonapprover because at most two agents like it and at least three agents exist. For \(\lambda\ge1\), a densest witness forces at least \(2\lambda-1\) double-approved goods, making the sharp envelope \((nD-2\lambda+1)/(n(D-\lambda))\); a two-vertex parallel-edge construction attains it. The envelope increases strictly with \(\lambda\), giving the claimed extremum. The standalone checker verified 346 distinct small multiplicity patterns and 51 independent exhaustive complete-allocation searches. Finite tests do not substitute for the all-size analytic proof.

## Originality — PASS (qualified)

The exact graph-density formula invokes a classical pseudoarboricity identity and is credited accordingly, not claimed to reinvent it. Bhaskar et al. (2023) address price of **EQ1** rather than the price of **exact EQ** simultaneously with EF1; their accessible complete text was inspected for the fairness and price definitions, results and related work. Hosseini et al. (2026), first public August 26, 2026, analyze simultaneous EF1+EQ1 for general normalized binary valuations, with an unrestricted positive theorem through seven agents and a distinct laminar domain at arbitrary size. Their accessible abstract and extracted result table do not report this exact-EQ, two-sparse, pseudoarboricity-resolved sharp welfare theorem. The class includes non-laminar cycles with more than seven agents, so the specific reported positive results do not logically imply it. Dedicated semantic and keyword searches did not reveal an exact equivalent. The source paper's complete primary text was inaccessible; appendix coverage and unindexed related results remain meaningful residual risks. These searches cannot establish absolute novelty.

## Value — PASS

The allocation domain models network goods that can benefit either one designated beneficiary or the two endpoints of a shared relationship. In this natural sparse-incidence class, the theorem strengthens a contemporary compatibility problem from approximate equitability to exact equitability while preserving EF1, with an efficient constructive certificate and an explicit Pareto-cost limitation. The exact sharp welfare-price envelope, indexed by the independently meaningful pseudoarboricity, identifies how concentrated shared approvals force welfare loss and gives matching extremal examples for every parameter. This is a classification of an entire non-laminar domain for arbitrary numbers of agents, not a single finite experiment or arbitrary case slice. The result does not provide Pareto efficiency or a guarantee for goods approved by three or more agents.

## Closest literature and limits

- H. Hosseini et al. (2026), *Simultaneous Envy and Equitability Guarantees*, https://arxiv.org/abs/2608.26410; first public August 26, 2026; abstract and extracted result table inspected; full text inaccessible.
- U. Bhaskar et al. (2023), *The Price of Equity with Binary Valuations and Few Agent Types*, https://www.alphaxiv.org/abs/2307.06726; accessible parsed full text inspected (EQ1, not exact EQ).
- M. Blumenstock (2016), *Fast Algorithms for Pseudoarboricity*, https://doi.org/10.1137/1.9781611974317.10; known graph parameter and algorithm, not a claimed invention.

Self-review: passed. Independent audit: not yet performed.
