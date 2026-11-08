# Scientific review: nine-symbol derangement switch distances

## Correctness
PASS. Exact labels, legal moves, orbit-equivariance and exhaustive traversal are all specified in the mathematical argument. A lexicographic C++17 derangement enumerator and a separately implemented recursive Python exact-cover enumerator each generate 133496 states, verify all eight conjugacy-type breadth-first-search profiles, and establish the eccentricity values 8, 9, 10 and the unique inverse antipode for type (3,3,3). The graph has 1835568 edges. The orbit argument transfers the finite representative computations to all labelled states.

## Originality
PASS, qualified. The most directly relevant full-text source is Jain's *Transpositions in Derangements* (2021), which studies the same graph and proves connectivity, degree bounds, vertex-connectivity bounds, and shortest spanning-walk length; it does not state these exact point-to-point distances. Dyer–Jerrum–Müller's earlier switch-chain work defines the same local move on general bipartite perfect matchings, but its diameter bound is restricted to chordal-bipartite graphs and does not imply the present result. OEIS A000166 already supplies the 133496 state count; the count is not novel. The conventional Cayley derangement graph is a distinct object. Exact metric literature searches did not identify covering work. An ambiguous 2026 title has not been checked in full and remains an explicit residual risk.

## Value
PASS. This is the exact geodesic metric of a natural switch sampler state space on the nine-crown graph. Its classification reveals a structurally distinguished collection of 1120 extremal pairs: and only these, inverse triple-three-cycle permutations, require ten operations. Connectivity alone, the known degree bounds, and the known number of states do not answer this reachability-cost question. The result gives a reproducible finite benchmark without claiming an all-order theorem or a mixing-time consequence.

## Limits
No general formula for arbitrary symbol counts is proved. Computation is exhaustive for nine symbols, rather than an infinite symbolic argument. The self-review does not substitute for external priority checking or independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
