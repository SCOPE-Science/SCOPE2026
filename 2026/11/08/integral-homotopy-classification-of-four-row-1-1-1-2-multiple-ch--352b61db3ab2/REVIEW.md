# Independent mathematical audit

## correctness

PASS

PASS. For capacity (1,1,1,2) and at most one cell in each of m columns, both direct column-choice and disjoint row-subset enumerations yield the same complete faces. Independently replayed pivot matchings and full Hasse acyclicity for m=4 (286 faces; 138 pairs; one 0, nine 2 critical cells), m=5 (840; 409; one 0, 21 three-cells), m=6 (2139;1042; one 0, 53 three-cells, one 4-cell), m=7 (4816;2350; one 0, 23 three-cells, 92 four-cells). Independently reconstructed exact signed algebraic Morse projection: m=6 has zero integral 53x1 boundary, giving wedge53 S3 vee S4; m=7 23x92 boundary rank2, with unit determinant -1 minor rows (1,3), columns (11,33), every column integer-span of these; Smith factors (1,1) and 2-connectivity give wedge21 S3 vee wedge90 S4. m4,5 single positive critical dimension give asserted wedges. m1,m2,m3 have elementary/sourced classifications. For all m>=8 the published shellability criterion (sum capacities=5, rows=4 => m>=8) plus symbolic f-vector/Euler formula yields wedge b(m) S4; finite sampled polynomial values alone would not prove the universal case. Independent source check /mnt/data/scope03_independent_check_20261108.py and signed Morse check /mnt/data/scope03_chess_morse_check.py.

## originality

PASS

PASS best-of-knowledge for m=4,5,6 ONLY. Limonchenko–Yu 2026 explicitly gives m2, m3 and other four-row torsion configurations; 2014 Jojić–Vrećica–Živaljević shellability covers m>=8; 2026 Column Law top homology + connectivity/Euler/wedge lemma implies m7 and is expressly not claimed new. Material full text of Oct27 2026 Limonchenko–Yu was not accessible (arXiv/OA failed and Oxford authorized downloader reported VPN disconnected), so that potentially relevant four-row-family theorem remains a specific priority risk. No accessible theorem was found implying the new m4..6 mixed homotopy types; inaccessible plausible source alone is not a scientific FAIL. Residual issue must be reviewed by authorized reader when access restored.

## value

PASS

PASS. The (1,1,1,2) pattern is the first simple nonuniform four-row multiple chessboard family in a natural allocation/collision constraint setting. The exact m4,m5,m6 homotopy cases close the gap between known low-column examples and the theorem-implied m>=7 regime; in particular m6 has a mixed-dimensional integral wedge not forced by the previously known top homology. The result is a coherent natural finite classification within an all-m statement, not an arbitrary slice; prior m7 and m>=8 cases are clearly credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
