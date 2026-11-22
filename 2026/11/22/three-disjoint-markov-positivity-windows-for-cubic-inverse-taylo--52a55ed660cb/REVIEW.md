# Scientific review

## Correctness — PASS

The exact coefficient-generating function of the transient rational inverse was derived from the Markov generator, rather than merely fitted to a numerical sample. The nine low-order sign expressions were reduced to nonnegative-coefficient rational functions, while the remaining three were reduced to explicit \(P\), \(U\), and \(V\) polynomials. Exact Sturm variation counts at zero and infinity are \((5,3)\), \((5,5)\), and \((7,5)\); their isolating rational brackets establish all possible changes in sign. The provided independent rational matrix inversions confirm the coefficient-to-entry reduction and conservation of mass. No computational timeout, finite root grid, or numerical simulation is used as proof of an infinite claim.

## Originality — PASS, with residual historical risk

The closest same-rational-map published statement treats unweighted undirected heat graphs, not the directed birth cascade or its entire positivity set. The complete positivity result for unshifted reciprocal cubic Padé coefficients is logically weaker for this purpose: shifted coefficients are actually negative within a nonempty timestep interval. Published inverse-Taylor order-two and Radau IIA cascade results have different stability functions. The relevant full texts that were available were inspected; a 2010 inverse-heat Padé article remains only partially accessible. The actual comparisons are recorded in `AUDIT.json`. Priority is not externally certified.

## Value — PASS

Markov-chain integrators must preserve the probability simplex to be usable as transition updates. The seven-state homogeneous cascade gives the first all-step failure in a natural dimension ladder for this classical third-order rational method, and the complete set of three disconnected safe intervals demonstrates that a single CFL-type positivity threshold can be misleading. Identifying two distinct active matrix entries and a narrow intermediate recovery provides a meaningful analytical benchmark for positivity tests and integrator selection, rather than an arbitrary numerical slice. The theorem is confined to the specified generator family.

Self-review: passed. Independent audit: not yet performed.
