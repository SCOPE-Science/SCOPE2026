# Scientific review: period-doubling palindrome-pair lengths

**Correctness: PASS.** The complete characterization uses the independently reconstructed parity factor-count recurrence, Fici--Shallit--Simpson's published exact count of palindromic periodicities, and two elementary substitution arguments. The first establishes every factor at all lengths in the three positive families as a palindrome pair; the second propagates a genuine non-palindrome-pair length-seven factor through all binary substitution iterates. Finite checks through length 192 agree, but are not being treated as an all-length proof.

**Originality: PASS, with priority risk.** Borchert--Rampersad's 2015 property-PP study does not give this period-doubling characterization. The 2024/2025 Fici--Shallit--Simpson enumeration counts *palindromic periodicities*, a strictly larger class, and alone allows the extra family \(7\cdot2^j\). The necessary substitution-based sufficiency and obstruction make the exact palindrome-pair result not a restatement or mere numerical specialization. The precise implication comparison has been made against those primary papers, the period-doubling complexity literature, and relevant indexed findings; an unindexed result is a remaining risk.

**Value: PASS.** This solves the natural complete length-set question for a classical non-Sturmian automatic word, sharpening the wider palindromic-periodicity condition and identifying an infinite exceptional length family. It closes a structural question, rather than adding an arbitrary finite threshold or a routine code rewrite.

**Limits.** The proof relies on the published all-length palindromic-periodicity count, whose original Walnut certificate was not independently reimplemented here. It does not concern arbitrary automatic words or more than two concatenated palindromes.

Self-review: passed. Independent audit: not yet performed.
