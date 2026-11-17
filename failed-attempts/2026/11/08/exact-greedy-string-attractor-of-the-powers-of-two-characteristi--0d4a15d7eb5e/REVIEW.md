# Independent mathematical audit

## correctness

PASS

For p(i)=1 iff i=2^j-1, the least failed-prefix greedy attractor initially marks 0,2. After mark h=3a-1 with a=2^k, every trailing word p[3a..j] for 3a<=j<6a-1 has a prior occurrence shifted by 2a, so no new mark is needed. At j=6a-1 the first zero factor of length 2a lies wholly beyond earlier marks, forcing a new mark. Induction establishes marks {0}∪{3*2^k-1}; direct dyadic counting yields g(N)=1 for N=1,2, else 2+floor(log2(N/3)). Independent word/factor tests checked 80 prefixes and exact z-factor phrase-end equality for eight phrases; proof is unrestricted and independent of these finite tests.

## originality

FAIL

FAIL for current independent distinctness, with precise publication-order qualification. A same-day but somewhat LATER posted, broader 2026-11-08 theorem gives the full overlapping shortest-new-factor Ziv-Lempel parsing of radix-power marker words for every base b>=2. Its b=2 phrase starts/lengths (0,1),(1,2),(3*2^(s-1),3*2^(s-1)) have endpoints exactly {0,2,5,11,23,...}, identical to the claimed greedy marks under the previously published 2024 greedy-attractor/novel LZ parsing equivalence. GitHub commit records show submitted special-case package first posted 2026-11-08 20:49:43 UTC and broad same-day SCOPE package at 20:51:33 UTC, so do NOT assert the broader theorem historically preceded this claim. Nonetheless the broad result now contains the entire special case, and no distinct remaining theorem was provided. The originality failure is based on extant exact mathematical coverage, not on an allegation of misattribution or fabricated priority.

## value

FAIL

FAIL for presently nonredundant scientific value: the exact attractor mark set and cost are now direct b=2 phrase-end and count consequences of the complete all-base factorization plus a known equivalence, without a new invariant beyond the covered sequence. The original special-case proof is correct and potentially earlier by about two minutes; chronology is preserved as a material caveat, but this portfolio-level exact claim adds no independent fact not already implied by an extant broader result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
