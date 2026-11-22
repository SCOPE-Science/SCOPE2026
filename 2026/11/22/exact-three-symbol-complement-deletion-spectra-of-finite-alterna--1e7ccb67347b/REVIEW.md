# Scientific review: exact three-symbol complement-deletion spectra

## Correctness
PASS. The complete epsilon-interleaving automaton proves that each accepted deterministic input is exactly one distinct residual after prescribed triple deletion. The at-most-ten-state adjacency matrices give sixteen sequences, whose fourth differences are identically zero by 148 exact finite arithmetic identities followed by Cayley–Hamilton. Four initial values in each case give the table. The independently implemented positional deletion enumerator agrees in all 176 host-pattern cases for lengths 3–24. The finite census is not substituted for the unrestricted proof.

## Originality
PASS against inspected evidence. The full text of Adamson–Fleischmann–Huch (https://arxiv.org/html/2603.20790v1), first posted 21 March 2026, defines the object and leaves specific counting formulas open. The binomial-tail theorem (https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binomial-tail-law-for-complements-of-alternating-words--d7ef6cdd9c92) handles only even-length alternating deleted patterns; the arbitrary-host run-pair result (https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-run-pair-formula-for-two-letter-complement-scattered-factors--3b99e07a61fe) handles only two-letter deleted patterns. The fixed-composition alternating-host spectrum (https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fixed-composition-deletion-spectra-and-parity-bias-for-alternati--4b7dc91ebfc9) counts the union over prescribed deleted orders and does not yield the distinct numbers for `001`, `010` and `100`. Actual semantic and literal formula searches found no exact prior eight-pattern table. This is not a proof of historical uniqueness; differently indexed shuffle/deletion formulae remain a priority risk.

## Value
PASS. A complete eight-pattern, all-length, both-parity classification resolves the smallest deletion length not covered by the even-length alternating deleted-word theorem. The sharp identity that `010` produces exactly one more distinct residual than `100` in every even-length alternating host is order-sensitive information absent from composition-only counting, while the odd-phase comparison gives a different exact unit gap. The result's mathematical object is natural and fully quantified; it does not assert an improvement for arbitrary-input algorithms.

## Limitations
Only alternating binary host words and length-three prescribed deleted patterns are covered. Proof uses a small exact finite-state certificate and Cayley–Hamilton; its finite regression test extends through length 24. Independent external mathematical audit is not yet performed. Historical priority outside inspected sources remains uncertain.

Self-review: passed. Independent audit: not yet performed.
