# Independent mathematical audit

## correctness

PASS

Each singleton must be unbordered; for two words, both directed prefix–suffix overlap tests and Hamming distance at least three are exactly the remaining compatibility constraints. Thus codes are precisely the cliques, and maximal-clique enumeration suffices for the maximum and all its equality cases. The supplied pivot recursion maintains extendible candidates and already-visited extensions. The second checker stops at depth nine, which suffices: a larger clique would contain a nine-clique. Independently I used ternary integer quotient and remainder to form prefix and suffix fingerprints, rebuilt all compatibility edges, and enumerated increasing cliques with a second, unrestricted common-neighbour mask to recognize maximality. For lengths 2–6 this independently gives capacities (1,1,2,4,8), labelled totals (6,18,108,300,528), both stated maximal-clique histograms, and the exact sets in all four TSV files. At length five every pair in each optimal code has Hamming distance three. Recomputing the simultaneous relabeling and reversal action gives size-6/size-12 orbit counts (8,21) and (10,39) at lengths five and six. For length one, two distinct words have distance one, so a singleton is optimal; six is therefore the first length for eight messages. Radius-one balls meet exactly when two centres have distance at most two. The guarantee is aligned correction and uncorrupted non-overlap, not correction of a frame boundary under corruption. For reproduction the frozen Python uses int.bit_count, which requires Python 3.10+ rather than the stated 3.9+; the independent replay used 3.12.

## originality

PASS

The supported distinct result is the joint distance-three non-overlap boundary, especially the complete five-/six-symbol equality census and shortest eight-message length. Earlier exact results on unrestricted non-overlap and on distance-two detection give different feasible families and do not imply that classification. General cross-bifix-free bounds and the standard clique encoding are not claimed as new. The closest partial-overlap distance-constrained article remains an access risk, not proof of noncoverage.

## value

PASS

There is an operational reason to combine the two constraints and target eight messages: the code must mark uncorrupted boundaries and recover a three-bit message after an aligned single substitution. The sharp length bound, and especially all feasible optimal designs modulo the actual symmetries, are useful exact benchmarks. The distance-three rigidity at five symbols is additional structure, not just an optimum number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
