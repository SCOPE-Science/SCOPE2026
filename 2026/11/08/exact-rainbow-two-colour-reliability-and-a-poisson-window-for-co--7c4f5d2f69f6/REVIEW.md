# Assessment of exact rainbow two-colour reliability for cocktail-party graphs

## Correctness — PASS

The only nonadjacent vertex pairs of \(K_{2m}-M\) are the \(m\) deleted matching edges. Under two colours, a missing pair is rainbow-connected precisely when some common neighbour sees opposite edge colours. In the simultaneous failure of \(k\) pairs, each four-edge block between two matched vertex pairs is either fully monochromatic, split into two independent equal-colour pairs, or unrestricted; these are exhaustive and disjoint cases. The exact block product and inclusion–exclusion prove the full polynomial, and probabilistic weighting proves the reliability expression. The critical window follows from exact fixed-order event intersection probabilities and Bonferroni bounds, without inferring an asymptotic theorem from a finite experiment. Boundary \(m=2\) and \(p\in\{0,1\}\) are included. The standalone original-definition verifier exhausts all colourings for \(m=2,3\) and checks the polynomial for \(m=4\).

## Originality — PASS (provisional historical priority)

Aruna–Jeyakokila (2023, Theorem 2.1, Section 2) proves existence of a rainbow two-colouring on cocktail-party graphs but neither weights nor enumerates all assignments. Gyárfás–Sárközy (2025 preprint, 2026 paper, Theorem 1 and proof) studies monochromatic two-reachable covers of *arbitrary* two-edge-colourings of precisely the same graph, not rainbow connection between every vertex pair or a reliability polynomial. Barát–Boyadzhiyska–Freschi (2026, arXiv:2609.11437v1) studies general Dirac-type existence conditions and probabilistic construction, not the graph-specific all-colouring intersection polynomial or this exact window. The Cartesian product \(K_2\square K_n\) is a different host graph for \(n>2\) (edge count \(n^2\) versus \(2n(n-1)\)), despite the shared four-cycle boundary. Searches under cocktail-party, complete multipartite parts of size two, matching-deleted complete graph, edge-colour reliability, and rainbow two-connection yielded no covering exact count. This is best-knowledge originality, not a proof of priority against every unindexed work.

## Value — PASS

This is a full red-weighted exact enumerator for an infinite, natural dense graph family, not merely a demonstration that its rainbow connection number equals two. The same exact intersection law yields a sharp logarithmic probability transition with an exponential limiting profile under biased random colourings; the joint exact–asymptotic treatment identifies the dependence structure of overlapping failed paths. The coefficient polynomial supports further questions about the distribution of red-edge counts, large deviations, and symmetry-class enumeration. Such information is not determined by the known existence and monochromatic-covering theorems.

## Scope and residual risks

The claims concern two named colours on a fixed labelled graph and the specified independent-edge distribution. No quotient by automorphism or general palette result is claimed. Generic inclusion–exclusion is classical; the graph-specific block intersections, full polynomial and critical law form the claimed combined contribution. The assessment is not an independent external mathematical review.

Self-review: passed. Independent audit: not yet performed.
