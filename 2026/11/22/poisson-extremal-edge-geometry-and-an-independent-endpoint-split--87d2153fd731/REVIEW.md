# Scientific review: Poisson extremal-edge geometry

## Correctness — PASS

The component-size forest-inclusion formula is independently derived by contraction and the Matrix–Tree Theorem, with boundary cases included. In any fixed bounded corner region, the number of candidate edges is of order \(n\); candidate edge pairs that share a vertex are lower-order because their total degree-square count is \(O(n^{3/2})\). Exact forest probabilities therefore give the mixed factorial moments of independent Poisson counts of intensity two. The smallest coordinate-sum point is almost surely unique and has density \(2e^{-(x+y)^2}\), whose sum–ratio transform factors into a Rayleigh-type deficit and a uniform endpoint fraction. A standalone exhaustive checker passed 906 exact assertions on Prüfer trees through eight vertices; it checks finite identities, while the asymptotic conclusions rest on the analytic argument.

## Originality — PASS, with specific historical risks

Pitman's forest enumerator and Cameron–Kagan's forest-extension formula are known inputs, not contributions. Kuba and Wagner's *Deterministic Edge Weights in Increasing Tree Families* is the closest identical edge-weight statistic: its Section 6.2 studies maximum numerical-label gap, but only in increasing trees, which are not uniform Cayley trees. Esteban–Ferrer-i-Cancho–Gómez-Rodríguez study total lengths and optimized arrangements; Hackl–Panholzer–Wagner study prefix uncovering; Bóna–Burghart–Wagner study common edges of independent trees. The assessed contribution is the marked planar extreme-edge Poisson process for uniform Cayley trees and the independent split of the longest edge's endpoint deficits. Relevant primary sources and general sparse-edge Poisson and label-bandwidth formulations were searched. An unidentified generic Poisson theorem or equivalent historical label-bandwidth paper remains a priority risk.

## Value — PASS

The fixed-order maximum numerical-label gap is a natural extremal counterpart to total dependency length, and relates to whether a random tree possesses an almost end-to-end connection. The square-root deficit and the endpoint split describe a complete limiting extreme geometry, not just a mean or a routine fixed-parameter substitution. The independent uniform endpoint split is a useful simultaneous mark beyond the one-dimensional maximum.

## Limitations and evidence

No assertion is made about minimum spanning trees, increasing trees, optimized vertex orders, or rates for arbitrary growing sets. The proof establishes convergence, not a full finite-size error bound. The checker's exhaustive finite enumeration is supplemental, not an infinite proof. Sources: Pitman (2001); Cameron–Kagan (2022); Kuba–Wagner (author PDF 2008, online 2009); Esteban and collaborators (2016); Hackl and collaborators (2023); Bóna and collaborators (2025). Their accessible relevant primary text was compared to the claimed domain and conclusion. No independent mathematical audit is claimed.

Self-review: passed. Independent audit: not yet performed.
