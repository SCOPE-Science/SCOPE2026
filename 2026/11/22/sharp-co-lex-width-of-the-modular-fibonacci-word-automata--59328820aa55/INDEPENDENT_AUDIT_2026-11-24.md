# Independent mathematical audit

## correctness

PASS

The last-symbol/residue transitions recognize exactly the stated language (the empty word starts at Z_0); a sufficiently long zero prefix gives each residue with either final symbol, and 11 reaches the sink. All-zero suffixes distinguish unequal residues among states with the same last symbol. A suffix 10^t chosen to accept from a Z state separates it from any O state, and every nonsink state has an accepting suffix unlike the sink. This gives 2m+1 distinct reachable residuals and 2m nonempty residuals for the trim partial automaton. If Z_r<Z_s, backward propagation along the cyclic zero transitions gives Z_i<Z_{i+(s−r)} for every i; iterating the nonzero residue difference closes a strict cycle. Thus the Z states give a width-m lower bound. Ordering all Z states below all O states with no intra-layer comparisons gives width m and makes backward propagation vacuous on strict pairs. With the sink, both 0 and 1 enter it, so sink<Z_r violates the label axiom. Conversely Z_r<sink propagates via O_{r−1} and the sink's zero-loop to O_{r−1}<sink, again violating the label axiom. The antichain increases to m+1 and the same two-layer order with an isolated sink realizes m+1. This argument treats the start label # as additional and least; the start also has a 0 predecessor. It applies at m=2 and all higher moduli without any empirical extrapolation.

## originality

PASS

Standard residual minimization and the general theory of co-lex ordering are prior machinery. The supported distinct content is the exact pair of widths for the length-modular no-11 minimal automata, especially sharpness of the one-unit sink cost. The closest forbidden-factor and modular-result comparisons inspected do not give that pair; this is not a comprehensive priority claim.

## value

PASS

Length congruence on the basic binary run-limited language yields a concrete family in which a residue cycle forces growing width although the number of symbol layers is fixed. The exact trim-versus-complete comparison is useful for interpreting the same co-lex invariant when implementations implement missing transitions using a dead state. The forced extra antichain member, not the standard product state construction, is the useful exact information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
