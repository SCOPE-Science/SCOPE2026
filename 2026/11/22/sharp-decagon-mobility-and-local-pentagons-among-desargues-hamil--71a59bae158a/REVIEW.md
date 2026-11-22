# Scientific review: Desargues Hamiltonian decagon trades

## Correctness — PASS

The claim concerns twenty-edge undirected Hamiltonian cycles in the explicitly defined twenty-vertex Desargues graph, with an edge in the move graph only when the full symmetric difference is one connected alternating simple cycle of length ten. In a cubic graph, perfect-matching complementation gives a bijection to two-factors; all 60 perfect matchings were enumerated exhaustively, and the 24 Hamiltonian complements were tested against all 276 unordered pairs. The independent direct Hamiltonian DFS in a nonidentical incidence representation reaches the same 24 configurations and 84 trades. Both source programs were executed successfully. Full breadth-first-search assertions from every state verify the uniform distance profile, and explicit neighbourhood checks prove the local five-cycle decomposition. The result is finite, and no extrapolation to untested graph orders is made.

## Originality — PASS, subject to stated historical risk

Compared exact statements and implications, not titles. The previously established Desargues 60-matching, 6/8-flip and edge-Kempe results have different move rules and state spaces; they do not supply a ten-edge Hamiltonian-complement exchange graph. Published ten-edge trade results for the Tutte–Coxeter graph concern a different 30-vertex graph with 144 Hamiltonian cycles. General matching switch-chain and two-edge Hamiltonian-switch papers do not determine the 24-state Desargues metric or its local geometry. Relevant full mathematical records and the primary 2015 switch-chain paper were examined; searchable historical coverage remains incomplete. There is no claim to prove publication priority from search absence.

## Value — PASS

This is a complete optimal-tour mobility classification on a canonical symmetric cubic graph, identifying a sharp minimum simultaneous move length, a self-centered two-step exchange metric, and a nontrivial local five-cycle obstruction with two distinct trade-edge orbits. The combined structural and movement facts go beyond reproducing the known Hamiltonian-cycle count; they provide a natural comparison with other cubic graph Hamiltonian-trade graphs and matching-switch dynamics.

## Scope and residual risks

The theorem is graph-specific and the moves are not ordinary two-edge switches. Related unindexed Hamiltonian-tour switching work could subsume the metric. The finite enumerators are self-contained but independent human audit has not occurred.

Self-review: passed. Independent audit: not yet performed.
