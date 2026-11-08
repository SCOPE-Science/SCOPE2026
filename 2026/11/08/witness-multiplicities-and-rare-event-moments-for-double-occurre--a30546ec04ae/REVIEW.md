# Self-review

## Correctness — PASS

The claim is normalized to a fixed labeled alphabet with exactly two occurrences of each symbol and unordered position bipartitions. A forbidden nested pair is incompatible with equal subsequence order, while order agreement yields the canonical witness. Every interlaced pair enforces equality of first-occurrence colors, giving exactly two assignments per crossing-graph component and a quotient by global color swap. The FIFO property makes those components precisely the primitive Dyck excursions. Catalan convolution gives the exact histogram; the geometric excursion generating function gives all moments. At second-moment weight four the unique dominant pole at \(3/16\) supplies the stated exponential factor. Direct enumeration and the extracted standalone script confirm every candidate through five symbols and 64 exact coefficient identities. Finite tests are not used as infinite proof.

## Originality — PASS, with explicit risks

The 2023 *Variations on shuffle squares*, Proposition 3, proves the double-occurrence no-nesting existence criterion and Catalan number of qualifying words. Those are expressly credited. The present claim determines the **number of distinct witnesses for each qualifying word**, gives a full histogram, and proves a limiting distribution whose bounded typical scale differs sharply from the mean and second moment. The inspected 2021 *Shuffle Squares and Reverse Shuffle Squares* counts word languages via nonnesting matchings, not per-word two-subsequence witness multiplicities. The 2025 *Shuffle squares and ordered nest-free graphs* establishes canonical ordered-graph representations and binary word characterizations, without the present Catalan-return witness law. The 2011 *Shuffling and Unshuffling* develops self-shuffles at the language level. Published-record searches under aliases (twofold words, interlacement graph, nonnesting perfect matching, Catalan returns and decomposition multiplicity) did not uncover an explicit equivalent. Residual risk: a Dyck-path-refined version of the known nonnesting description may exist under different terminology. Search absence is not uniqueness proof.

## Value — PASS

A recognition result merely decides whether a word is a shuffle square; this theorem resolves the distinct decomposition *ambiguity* of every word in a canonical infinite family. The classification gives all attainable multiplicities and their exact counts, identifies uniquely decomposable words, and reveals that bounded-in-probability witness counts coexist with linear mean and exponentially large second moment. This is a natural structural and probabilistic refinement relevant to unshuffling certificates, not an arbitrary finite enumeration. It requires a crossing-component analysis not contained in the unrefined Catalan word count.

## Limits of the review

Proof and searches are checked within this study, not independently audited. The finite verifier tests length at most ten and formula coefficients through order 32; higher lengths rely on the written proof. Strongest relevant inspected sources: arXiv:2308.13882, arXiv:2109.12455, arXiv:2503.22043, and arXiv:1106.5767.

Self-review: passed. Independent audit: not yet performed.
