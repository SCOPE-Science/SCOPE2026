# Independent mathematical audit

## correctness

PASS

Each Wolfram rule r has a four-state de Bruijn graph with vertices 2-bit words ab and arcs ab→bc labeled rule(abc); cyclic inputs are exactly labeled closed walks, including n=1,2 repeated neighbors. A target word belongs to the one-step image iff the Boolean matrix product has a nonzero diagonal. The deterministic automaton of 4x4 Boolean relations has at most 2^16 states and accepts all word lengths. Exhaustive direct enumeration through length 8 partitions the 256 rules into 100 short-signature classes with profile 8 singletons,75 doubles,10 quadruples,3 sextuples,4 tenfold. Complete synchronized relation-automata BFS for all 156 representative-to-member pairs shows no longer distinguishing word: maximum visited product 2375 states for rules 22,104. Every unlike short-signature pair already differs by n<=8. Independently reconstructed all 256 direct image sets and the complete finite-product BFS; confirmed prefix counts (3,8,40,72,75,92,99,100), sharp pair 57,99 with target 00010011 from predecessor 11100101, and compact class table SHA256 8046dbeaba56d5cdec15119e6407b9c712af515a19d6c70adc31613f9a841cee. Finite-state exhaustion, not extrapolation from n<=8, certifies equality for all n.

## originality

PASS

The exact 100 classes of indexed cyclic one-step image languages and sharp eight-cell deciding cutoff are not the usual 88 symmetry classes, preimage multiplicity results or selected finite-size Garden-of-Eden counts. A prior exhaustive equality table might exist in an unindexed source, but no identical implication in the inspected primary automata literature or indexed results was found.

## value

PASS

A complete optimal finite cutoff for equality of an infinite family of cyclic image languages is an intrinsically useful invariant/classification of the natural complete 256-rule elementary automaton space. The sharp length-eight witness and compact canonical 100-class table are nontrivial computational mathematics under a transparent finite-automaton exhaustion proof, not merely listing a few small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
