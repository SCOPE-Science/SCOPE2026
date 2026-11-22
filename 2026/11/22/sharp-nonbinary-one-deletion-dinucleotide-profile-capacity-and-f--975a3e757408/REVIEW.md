# Review of nonbinary dinucleotide-profile deletion capacity

## Correctness — PASS
The all-parameter argument reduces exact profile outcomes to local deletion-change vectors, whose distinct signatures split into \(q\) constant types, \(q(q-1)^2\) proper triples and up to two boundary types. Saturation requires visiting every equal-letter digraph vertex, giving a sharp additional \(2q\) traversed-edge cost when boundary pairs are unequal. A strongly connected balanced proper-triple graph with one modified portal exit has exactly the two Euler-imbalance vertices, yielding a sharp extremizer for every \(q\ge3\). The endpoint calculation and disjoint-block union bound establish the claimed random-word limit. Two independently implemented finite checks pass; they do not substitute for the all-length proof.

## Originality — PASS against inspected sources
The closest exact predecessor is the published binary one-deletion profile-ball classification; its proof uses the same elementary local change identity but does not contain a nonbinary Euler saturation-length theorem. Published global ordered two-multispectrum and unordered ternary composition-profile formulas have different observation spaces or quantifiers and do not imply the local one-deletion claim. The 2026 substring-count hashing paper concerns edit-code asymptotics and motivates the method, but its full text could not be inspected; no whole-document noncoverage claim is made. Searches for q-ary dinucleotide profile balls, Markov-type deletion shadows, saturation lengths and the explicit capacity formula returned no covering exact statement. Unindexed prior work or a hidden subsidiary lemma remains a priority risk.

## Value — PASS
For a fixed alphabet, the number of observable dinucleotide histograms under a single deletion stabilizes at a sharp finite capacity even as word length increases. The exact shortest saturation length and the prevalence of saturation quantify when the full local ambiguity signature becomes possible. On a four-symbol alphabet the result gives 42 possible profile outputs, first realized at length 46, and limiting probability 33/64; the nonbinary saturation threshold depends on a new directed Euler-trail construction.

## Source and scope limits
The proof treats linear words and one exact symbol deletion only; it does not supply the full nonbinary distribution, longer-read statistics or a deletion-code rate improvement. Full text for the recent hashing source could not be obtained, and independent mathematical review is outstanding.

Self-review: passed. Independent audit: not yet performed.
