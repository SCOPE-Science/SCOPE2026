# Independent mathematical audit

## correctness

PASS

For t6 length64, the exact hitting-set equivalence is correct: for each of 1560 distinct factors, collect all coordinates covered by any occurrence; inclusion-minimal covers number 26. An independent construction regenerated the word and all substring cover masks; exhaustive combinations among C(64,3) give zero size-3 attractors, and among C(64,4) give exactly 32, matching precisely two disjoint independent four-bit boxes {16+e1,24+e2,32+e3,48+e4} and {16+e1,32+e2,40+e3,48+e4}. The pinned verify.py and full certificate.json were inspected; they use two factor-occurrence enumerations and independent recursive transversals. Correctness applies only to t6 and is finite/exhaustive, not a claim of a theorem for all n.

## originality

FAIL

FAIL: independently stronger PUBLISHED coverage is decisive. Banbara–Bannai–Guo–Köppl–Mieno–Okamoto arXiv:2602.16152v3, Theorem 43 and Corollary 45, gives all 32 minimum attractors for EVERY Thue–Morse t_n with n>=6, explicitly including n=6; the October 12 extended text says this was announced at CPM June 2026. Faro–Marino–Pavone arXiv:2610.10950 (Oct 7) Theorem 5.4 independently gives the same all-n>=6 classification. A published Resultary Oct4 RESULT.md already states exactly the two t6 16-element boxes and 32 count plus t4/t5 counts. The assigned claim is the literal n=6 specialization, so its correctness and independent computation do not yield originality.

## value

FAIL

FAIL: Although the canonical length-64 Thue–Morse word is a natural combinatorial object and the exact 32-count is correct, the entire claimed optimizer census and two-family structure already follow immediately from two published general n>=6 theorems and an earlier public exact t6 result. There is no new independently useful exact fact; alternative exhaustive code is reproducibility, not independent scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
