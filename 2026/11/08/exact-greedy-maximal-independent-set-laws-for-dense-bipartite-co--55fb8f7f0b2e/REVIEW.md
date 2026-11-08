# Self-review

## Correctness — PASS

The domain is an arbitrary finite, simple, \(d\)-regular, four-cycle-free bipartite missing-edge graph \(H\) with both sides of size \(n\), \(2\le d<n\); the greedy scan uses independent continuous uniform priorities. The result states the *full* probability of each of the \(2n+2\) maximal independent sets. The proof first classifies those sets using the absence of a four-cycle. After conditioning on the first vertex, it identifies a mixed outcome with the union of \(d\) priority events. An exact order-statistic integral gives their intersections, and inclusion-exclusion reduces to \(q_{n,d}=dn/[n^2-(d-1)^2]\). The standard earliest-blocker certificate and the common-neighbor counts prove all mixed maximal sets equiprobable. The total-variation and expected-size claims follow algebraically.

Independent recursive calculations of full finite terminal-set laws, explicit enumeration of all maximal independent sets, and exhaustive permutation checks on the smallest examples agree exactly. The Python standard-library checker covers deleted-edge even cycles, a disconnected pair of six-cycles and the Fano incidence graph, plus 853 exact parameter/model identities. Finite examples do not replace the arbitrary-size proof. Boundary \(d=2,n=3\) is handled separately as equal terminal-set sizes.

## Originality — PASS, bounded historical priority

Krivelevich–Mészáros–Michaeli–Shikhelman (arXiv:1907.07216; DOI:10.1002/rsa.21200) establish the greedy priority process and local-limit asymptotics. Their accessible relevant text does not give the exact terminal-set distribution for dense complements of \(C_4\)-free regular bipartite graphs. Fairfax-Ball (arXiv:2610.02276) proves precise greedy-versus-flat statements on trees and records a general order certificate, which are acknowledged; tree results do not imply this two-part regular-family formula. Kryven–Versendaal–de Vries (arXiv:2608.07239) study sufficient regular-independent-set conditions for uniform greedy generation; the two distinct maximal independent-set sizes here rule out those conditions in the nondegenerate family. Dall'Asta–Pin–Ramezanpour (arXiv:0907.3309) compare dynamical and flat ensembles on other graph models, a conceptual predecessor rather than the explicit formula here.

Related published-index summaries describe exact greedy laws for threshold, chain and complete multipartite graphs. None of those stated structural families implies the present missing-edge regular girth-six case. Specific searches by graph construction, the exact rational function, the cycle specialization and uniform-versus-greedy total variation did not surface the claimed result. That failure is not a proof of worldwide priority: some related indexed full texts were unavailable, and their possible unseen generalizations remain a documented residual risk.

## Value — PASS

The theorem obtains a complete, not just expected-size, distributional classification for an infinite family encompassing all eligible regular four-cycle-free missing-edge graphs. The law is surprisingly independent of the graph's global incidence structure: all mixed maximal independent sets have equal probabilities even without vertex-transitivity. For every fixed feasible degree \(d\), greedy sampling produces a maximum independent set with probability tending to one, while flat sampling from maximal independent sets almost surely produces size \(d+1\). Their total-variation distance tends to one. Even the explicit deleted-cycle example exhibits this maximal separation, making the exact law a meaningful caution about replacing a dynamic sampler with a flat ensemble.

## Closest literature and limitations

The priority-order construction, the generic first-arrival recurrence and the distinction between dynamic and flat maximal-set sampling are previously known, not claimed original. The new proof applies only to equal-size parts, regular simple missing-edge graphs without four-cycles, and uniform independent priorities. The result does not address irregular deletions or graphs with four-cycles. Historical priority and scientific acceptance await independent review.

Self-review: passed. Independent audit: not yet performed.
