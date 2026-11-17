# Review: four-colour bipartite cyclic dynamics

## Correctness — PASS

The proof separates the global labelled configuration into eight initially occupied, permanently homogeneous colour classes and updates their tags using opposite-shore counts clipped at two. Clipping commutes with all nonnegative class mergers and exactly captures the contact threshold. Hence all possible graphs reduce to 6400 realizable initial signatures. The fully enumerated transition code verifies the universal map identity, exact periods, sharp fifth-entry witness, and all twenty period-six basin signatures, including their preperiods. Binomial/multinomial counting reconstructs the precise basin and on-cycle counts. A vertex-level implementation checks the update without using the quotient. The proof's numerical portion is finite and exhaustive, not extrapolation from test sizes.

## Originality — PASS, qualified

The closest conceptual works are Durrett–Griffeath (1993) on threshold cyclic dynamics and Matamala–Goles (1995, 1997) on finite-graph cyclic automata. They establish the model and broad dynamical techniques, so neither is claimed as new. Their accessible abstracts do not provide the present finite-biclique four-colour exact transient/period-six basin law; the 1995 and 1997 full texts were unavailable, so their contents cannot be certified as non-covering. Searches also considered the differently defined binary parity rule and infinite-tree cyclic automata. An earlier three-colour biclique result cannot imply the four-colour six-cycle enumeration: its colour group and possible periods differ. Priority remains a substantive qualified risk, not a proof of uniqueness from search failure.

## Mathematical value — PASS

The theorem resolves a natural exact oscillation-basin question for a complete infinite family of symmetric finite networks. The sharp two-shore size threshold, exceptional six-cycles with no feeders beyond one round, exact labelled-state and orbit counts, and exponentially small balanced-family basin probability are dynamical structure not inferred merely from exhibiting a cycle. Four colours alter the qualitative period spectrum relative to three-colour dynamics, making the comparison mathematically motivated rather than a cosmetic parameter change.

## Remaining limitations

The result is restricted to four colours, threshold two, and complete bipartite topology. Full historical comparison with the 1995 and 1997 finite-graph papers is incomplete because their full texts were inaccessible. The finite-state certificate and proof have only self-review; independent scrutiny remains outstanding.

Self-review: passed. Independent audit: not yet performed.
