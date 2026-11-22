# Scientific review: exact shortest unique factors of dyadic regular-paperfolding prefixes

## Correctness — PASS
The theorem's domain is every integer \(k\ge6\), for contiguous factor occurrences in the explicitly defined regular paperfolding prefix and zero-based start indexing. The proof uses the exact even/odd decimation identity, an explicit short-factor coverage argument, a finite occurrence-frequency certificate, a parity-rigidity lemma, and an induction that **retains the possible loss of one source-suffix occurrence at the right boundary**. The suffix-multiplicity invariant is proved simultaneously to prevent that loss from creating spurious unique factors. Every target-length unique factor corresponds bijectively to a unique factor in the preceding prefix and positions transform by \(i\mapsto2i+1\). The finite base cases and independent longer-prefix checks are reproducible from the two included Python scripts, with recorded output. The proof does not infer an infinite statement from finite tests.

## Originality — PASS against inspected evidence
The closest paper on the *same word* is Allouche (1992), whose Lemma 2 **already establishes the length-seven odd/even factor separation**, which is explicitly credited; the paper's main conclusion is the number of distinct infinite-word factors, not finite-prefix unique occurrence counts or their location. The 2026 algorithmic source treats shortest unique substrings over arbitrary packed inputs, without the uniform paperfolding formula. A 2026 Thue–Morse result gives a different automatic-word classification of minimal unique factors, not an implication for paperfolding. A search of accessible earlier findings identified related period-doubling and Thue–Morse results but no paperfolding analogue. The parity lemma is neither asserted to be new nor counted as the theorem's novel content. The novelty claim pertains solely to the exact global shortest length, count, and positions for all dyadic prefixes.

## Value — PASS
The shortest unique substring is a natural indexing and sequence-identification invariant. Exact location information over an infinite family is materially finer than the known linear factor complexity, and the proof gives a structural explanation for precisely two sharp boundary-anchored signatures. The result supplies a uniform explicit benchmark for paperfolding sequence analysis and demonstrates how to control prefix-edge occurrence loss in dyadic self-similarity arguments, rather than reporting only a finite census or a straightforward algorithm output.

## Closest literature and limitations
- Allouche, *The number of factors in a paperfolding sequence* (1992), particularly Lemma 2 and its complexity theorem, establishes parity separation and infinite-word factor counts, **not** the claimed finite-prefix unique factor spectrum.
- Charalampopoulos et al., *Faster Algorithms for Shortest Unique or Absent Substrings* (first public 2026-05-06), establishes general packed-string algorithms, **not** the formula for this recursive sequence.
- Faro et al., *Smallest String Attractors and Minimal Coverage Certificates of Thue–Morse Words* (2026), uses minimal unique factors of another word.
- Shallit, *Runs in Paperfolding Sequences* (2024), treats runs rather than unique-factor multiplicities.

The theorem does not classify other paperfolding instructions, arbitrary-length prefixes, or all inclusion-minimal unique factors. Historical priority cannot be guaranteed against works outside the inspected indexed corpus. No independent external audit or validation has been performed.

Self-review: passed. Independent audit: not yet performed.
