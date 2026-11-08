# Scientific review

## Correctness — PASS

The signed-crossing rule in the primary source gives weight one to every unvisited child-tree edge and both unused cycle edges, but weight \(e^{-\beta}\) to the reverse of the single incoming parent edge. At the root the latter is absent. Finite cylinder probabilities therefore multiply to the stated exact product, with no independence assumption beyond ordinary conditional probability multiplication. Its positivity criterion follows from two-sided elementary bounds for \(\log(1+x)\). The explicit exponential branching example has a rigorous positive lower bound, and its outward paths have graph distance growing by one per step. The included finite exact checker independently reconstructs adjacency and signed crossing counts; it is a diagnostic rather than a replacement for the infinite proof.

## Originality — PASS, with historical-priority caveat

Erhard–Franco–Reis, *The Directed Edge Reinforced Random Walk: The Ant Mill Phenomenon* (arXiv:1911.07295, Section 2.2), identifies escape via an infinite leaf and proposes—only heuristically—an example with no infinite leaf, rapidly growing branches and growing cycle lengths. Its proved trapping results concern finite non-tree graphs and lattices of dimension at least two; these do not cover the present highly branching infinite cycle-decorated tree. The present claim establishes the contemplated escape, retains constant triangular cycle lengths if desired, and calculates an exact full-event product with an iff branching criterion. Erhard–Reis, *Stochastic Processes with Competing Reinforcements* (arXiv:2105.00880), concerns different multi-particle dynamics. Relevant published mathematical-record searches located no theorem implying this exact claim. Unindexed or independently derived results remain possible.

## Value — PASS

A named open problem asks whether an infinite leaf is actually necessary for positive-probability escape in the Ant RW. This construction answers that concrete possibility, not merely a computed special parameter, and shows that even every vertex being on a finite cycle fails to force certain trapping. The precise summability criterion identifies the branching mechanism behind a natural monotone escaping event, while the independence from all private cycle lengths removes an apparently necessary growth assumption in the proposed example. No general dichotomy or full escape probability is claimed.

## Closest literature and boundaries

The principal comparison is Section 2.2 and Figure 2 of arXiv:1911.07295 and its open-access journal version DOI:10.1007/s10955-022-03031-0. Historical priority is not independently certified. The iff criterion is **only** for the designated monotone event; the walk can make other transitions. The construction is locally finite but of unbounded degree. The general trapping-or-escape Conjecture 2.3 from the motivating paper remains open under this result.

Self-review: passed. Independent audit: not yet performed.
