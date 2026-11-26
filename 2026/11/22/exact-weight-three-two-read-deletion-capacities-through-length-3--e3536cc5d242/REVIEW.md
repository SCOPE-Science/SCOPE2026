# Independent mathematical audit

## correctness

PASS

A pair of distinct reads identifies at most one source precisely when no two codewords share an unordered pair of distinct deletion outputs. I independently reconstructed every length-n word in lexicographic triple order, formed deduplicated decks by literal string slicing at all positions, and checked the frozen JSON data without running either supplied program. All 30 lengths passed: 40,920 candidate words, 18,686 code entries, 310,340 unordered read-pair entries with no duplicate within a code, and 25,972 vertex pairs checked within nonempty, disjoint cliques exhaustively covering each vertex set. Each clique pair shared at least two reads. Thus each code gives the lower bound and its equal-size clique partition the matching upper bound. The table and both polynomials were checked at every stated integer using exact rational arithmetic, including the singleton n=3; nothing is proved for n>32.

## originality

PASS

The closest indexed result concerns the identical fixed-composition graph, but computes different invariants. Exact results on adjacent word layers or for one read do not imply the stated optima. No equivalent sequence or covering theorem was established by the statement-level comparisons below; this is not a proof of priority.

## value

PASS

This settles the natural next fixed-weight layer after the weight-two classification, where a read conflict can arise from moving an alternating block with up to three ones. Certified equal optima and clique-partition bounds over a consecutive range, reaching 4,960 candidates at n=32, provide exact benchmarks for constructions and upper bounds. The finite polynomial agreement is useful as a target for an all-length theorem, not itself such a theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
