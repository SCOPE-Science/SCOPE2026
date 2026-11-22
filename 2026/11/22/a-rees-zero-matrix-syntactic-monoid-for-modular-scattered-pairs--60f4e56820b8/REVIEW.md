# Review of the syntactic-monoid theorem

## Correctness — PASS

The proof gives an explicit monoid morphism for the full language and a separate realization argument for each of the \(4m^3\) nonzero forms. The construction of arbitrary pair-count residues uses two adjacent admissible zero gaps, whose weights differ by one; it requires no prime-modulus assumption. A two-sided-context case analysis separates the absorbing zero, all four boundary patterns, distinct modular triples, and the external identity. The proof thus covers every modulus \(m\ge2\), including composite moduli, and yields the claimed order. The independent finite program checks all transition transformations for six moduli and direct word membership through length twelve; those finite tests are not substituted for the proof.

## Originality — PASS (best-knowledge, with residual risk)

The closest relevant sources were inspected at the level of their motivating definitions and actual statements. Lejeune–Rigo–Rosenfeld's class-two nilpotent correspondence is for integer \(2\)-binomial equivalence on unrestricted words; it neither supplies a Rees sandwich matrix nor proves the two-sided syntactic congruence of the present constrained modular language. Adámek–Milius–Urbat present general syntactic theory without this computed family. Bourne–Ruškuc's Rees analysis concerns contiguous factor counts and abelian underlying groups, not scattered-pair counts and the nonabelian Heisenberg structure. Related indexed exact-state findings cover different languages, observations, or automaton output conventions. Searches of modular subsequences, forbidden adjacent factors, syntactic groups and Rees zero-matrix descriptions did not identify a result covering the stated all-modulus claim; missed equivalent prior work remains possible.

## Value — PASS

This gives a natural, explicit algebraic invariant for a regular language combining a global modular scattered-pair statistic with a local forbidden-factor condition. The nontrivial result identifies not merely a recognition automaton but its *minimal two-sided algebraic recognizer*, including all maximal groups and the precise single-zero sandwich obstruction. The theorem separates algebraic information from routine DFA state counts, and the nonabelian/zero-simple coupling is useful for studying syntactic varieties and star-height questions. No stronger theorem about other patterns or constraints is inferred.

## Limits and source comparison

The proof is self-contained. The full text of the binomial-equivalence paper was inspected in its definition/Parikh-matrix and nilpotent-group sections; the categorical source's introduction and the factor-counting source's Rees-matrix section were inspected. Inaccessible indexed or unindexed papers could still bear on priority. The verification script is a finite cross-check. Exact claims are limited to the specified language and integers \(m\ge2\).

Self-review: passed. Independent audit: not yet performed.
