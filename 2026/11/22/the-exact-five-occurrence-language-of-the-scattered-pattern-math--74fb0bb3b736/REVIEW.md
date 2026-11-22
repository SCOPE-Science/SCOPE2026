# Scientific review

## Correctness: PASS

The occurrence-counter invariant follows by descending-index dynamic programming on all six nonempty pattern prefixes, and saturation at six preserves the exact-five decision. The Thompson token automaton recognizes precisely the claimed two-core regular language. The 126-row, 252-edge certificate checks the reachable product automaton's closure and accepting-predicate equivalence, giving a genuine all-word induction argument. Direct unsaturated enumeration over lengths 6–16 independently tests boundary behavior. The four inert runs and the unique parsing give the binomial count by an ordinary stars-and-bars argument. Reproducing these checks requires the exact `CHECKER.py` and `CERTIFICATE.tsv` files supplied here.

## Originality: PASS against inspected evidence

Bruda's 2026 paper gives the eventual polynomial degree upper bound four for this pattern and highlights the still unresolved tightness criterion; it does not give the present exact multiplicity-five regular language, its two short cores, or its degree-three formula. Menon–Singh give explicit multiplicities only up to four. Tian gives general constructions and counts through primitive words but no closed form for this specialization. A related indexed result gives an exact *different* pattern (`0011`) at frequency five, with one core; neither source language entails the other. The inspected complete claim of that indexed result and its proof were compared. Residual risk: a separate unindexed explicit formula or an unexamined specialized consequence of a general algorithm.

## Value: PASS

The case isolates the first unsolved positive multiplicity beyond the explicit zero-through-four classification for the shortest three-run pattern with all three runs of length two. The sharp degree deficiency is a motivated test of Bruda's open equality criterion, and the entire language structure gives more information than a single coefficient polynomial. This is a small exact classification, not a general theorem for all patterns.

Self-review: passed. Independent audit: not yet performed.
