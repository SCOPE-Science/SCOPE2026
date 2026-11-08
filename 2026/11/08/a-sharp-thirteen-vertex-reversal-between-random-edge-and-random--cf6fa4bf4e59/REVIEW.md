# Scientific review: sharp tree threshold for two greedy matching algorithms

## Correctness — PASS

The two matching algorithms are normalized as uniform edge priority versus uniform job-side priority plus independent uniform free-neighbor selection. Every arm job of the spider has a private leaf, so final matching size has two possible values. Independence of disjoint edge-priority triples gives the random-edge failure probability \(3^{-m}\); last-job conditioning gives the random-vertex failure probability \(1/((m+1)2^m)\). Both calculations are verified against exact rational dynamic programming and independent small-arm enumeration of all priority permutations. For the finite sharp cutoff, the executable certificate constructs all nonisomorphic trees by an exhaustive leaf-extension induction and computes exact expected values from first-step recurrences, considering both bipartition orientations. It reports no reversal through twelve vertices and one at thirteen, with exact gap \(1/6480\). The completeness argument for the generator and the normalization of the recurrences are included in `RESULT.md`.

## Originality — PASS, with historical-priority risk

Arnosti (2021/2022) proves an *edge-set-averaged* random-vertex stochastic dominance theorem and exhibits a smaller *cyclic* counterexample on a fixed graph; neither implies a fixed-tree first-failure classification or the present infinite spider law. Dyer–Frieze (1991) studies random-edge performance without this two-procedure tree comparison; Dyer–Frieze–Pittel (1993) is reported by Arnosti to study averages over random labeled trees, an assertion consistent with isolated exceptions. The 1995 Aronson et al. vertex process permits both sides of a graph to be selected and hence is a different process. Searches of public research records and other literature did not identify the two-point spider formulas or the first thirteen-vertex oriented-tree threshold. Complete older full texts, notably the 1993 article, could not all be inspected; lack of a search hit is not treated as proof of historical priority.

## Value — PASS

A natural finite-graph question left open by stochastic superiority *on average* is whether acyclicity alone prevents a fixed-instance reversal. The exact first counterexample is not a contrived dense graph but a fully symmetric four-arm tree. The two short failure formulas explain the reversal mechanism and yield a full infinite family of strict first-order stochastic dominance reversals, while the exhaustive finite certificate shows the sharp minimal order and uniqueness. This is a structural boundary with direct relevance to choosing between two standard randomized greedy matching algorithms, not merely a decimal comparison.

## Closest literature, limitations and risks

The closest primary source is Arnosti, *Greedy Matching in Bipartite Random Graphs*, https://doi.org/10.1287/stsy.2021.0082 , especially Figure 1 and Theorem 1. Related sources include Dyer–Frieze (1991), Dyer–Frieze–Pittel (1993), Aronson–Dyer–Frieze–Suen (1995), and Tang–Wu–Zhang (2023). The finite threshold relies on a transparent exhaustive exact computation, not a handwritten structural classification. The statements exclude different vertex-selection conventions, edge weights, capacities and non-tree graph families. Historical priority and the mathematical proof have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
