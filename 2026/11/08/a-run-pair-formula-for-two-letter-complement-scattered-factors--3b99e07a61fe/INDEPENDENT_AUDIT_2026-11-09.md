# Independent mathematical audit

## correctness

PASS

For arbitrary finite source word over any alphabet and distinct prescribed a,b, every scattered ab deletion maps to one eligible ordered (a-run,b-run) pair. Distinct run-pair outputs can coincide only across local a^r b a b^s windows with singleton intermediate runs; comparing first deleted differing positions and iterating proves the collision graph is a disjoint union of paths, one edge per contiguous abab factor. Thus |C(w,ab)|=M_ab(w)-N_abab(w) without missing longer-range identifications. Separating run-start pairs into boundary, adjacent and disjoint positions gives the exact stated q-ary expectation by linearity, without false independence assumptions. Independent brute-force deletions on all 9,841 ternary words of lengths 0..8 agreed with the formula.

## originality

PASS

Best-of-knowledge original exact all-word/all-alphabet count for prescribed deletion pattern ab (a≠b). Adamson–Fleischmann–Huch (2026) develop the exact complement-scattered-factor object and general algorithms but identify even special closed counting formulas as future work; their full available paper does not supply the run-pair/abab collision-fiber identity. Older unrestricted two-deletion descendants and alternating-host formulas are different statistics or narrower hypotheses; possible shuffle/deletion terminology overlap remains a risk.

## value

PASS

Solves a directly motivated exact counting problem for the first nontrivial ordered distinct-letter deletion pattern, over arbitrary alphabets/source words; explains every collision fiber, replaces construction of an output set by a linear scan, and yields an exact random-word expectation. The result has structural content beyond its computational verification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
