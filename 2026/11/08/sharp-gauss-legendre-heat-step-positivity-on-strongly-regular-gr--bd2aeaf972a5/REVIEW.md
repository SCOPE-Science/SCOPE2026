# Review: Sharp Gauss–Legendre heat-step positivity on strongly regular graphs

## Correctness — PASS

The complete proof derives the graph's three spectral projectors from the strongly regular adjacency identity, reduces the rational step matrix to explicit diagonal/edge/nonedge entries, and proves the edge-sign polynomial has exactly one positive crossing when \(\Delta>0\). Its denominator is the product of positive scalar Padé denominators. The eigenvalue factor \(((x-3)^2+3)/(x^2+6x+12)\) proves positive diagonal entries for all real steps. The exact rational checker executes 30 matrix identities across six graph families, with signs and row sums; these finite checks are supplementary and not mistaken for a universal proof. No unverified computational lemma is required.

## Originality — PASS, qualified

The pre-existing classical method, standard adjacency algebra, graph Laplacian positivity framework, broad Padé positivity obstructions, an eight-state directed Markov small-step example, and the previously derived five-cycle result are excluded from the novelty claim. Full material was read for the 2012 essentially-negative-news article, the 2021/2022 positivity-preserving graph-Laplacian study, and the two relevant published research notes. Their theorems do not state or logically imply the arbitrary-strongly-regular-graph exact \(\Delta\) classification. Multiple source, alias, implication, and database searches found no equivalence or stronger covering result. A thorough pre-1998 / association-scheme specialist literature comparison remains a publication-priority risk; the available full texts and search evidence do not resolve all possible earlier priority.

## Value — PASS

Strongly regular graphs form a standard structurally natural test class of graph heat semidiscretizations with exactly three spectral values. Here the complete classification gives exact maximum-principle steps for *every* member, not a handpicked numerical counterexample or renamed known-table entry, and it exhibits infinite all-step-positive families alongside finite cutoffs at the same RK order. The explicit Petersen witness shows spectral stability and mass conservation are insufficient for positivity. The graph and timestep parameter are natural; the result is falsifiable with an elementary exact checker and useful for numerical positivity benchmarks.

## Closest work and limitations

Published source arXiv:2102.08242 first posted February 16, 2021, and the 2012 negative-positivity theory supply motivation. Closest method-specific published findings concern directed eight-state Padé failure and periodic five-cycle positivity. The present scope is unit-rate, connected, noncomplete strongly regular graphs, exact arithmetic, and end-step—not internal-stage—positivity. Historical specialist priority and extensions to other graphs remain unresolved.

Self-review: passed. Independent audit: not yet performed.
