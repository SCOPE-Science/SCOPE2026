# Scientific review: single-forbidden-trigram shattering

## Correctness — PASS

The support criteria are necessary and sufficient for all eight cases. In class A, the constant pattern has an immediate all-free-bits-one extension and the alternating pattern has a gap-filling construction. In class B, the first prescribed one gives an explicit extension; any forbidden three-coordinate pattern is impossible. Complement and reversal cover the other factors. The face enumerators follow from a no-triple recurrence and a first-selected-site/independent-suffix count. Avoidance counts follow from complementation, Fibonacci words without adjacent zeros, and the four-state automaton for the alternating factor. The defect generating series has strictly positive coefficients beginning at length four. Two programs exhaustively checked finite ranges with different implementations, not as a substitute for proof. Risk: transcription or conceptual errors remain possible pending an independent reviewer.

## Originality — PASS within checked evidence

Hu–Weinberger–Shayevitz, *On the VC-Dimension of Binary Codes* (arXiv:1703.01586, initially 2017-03-05) studies general asymptotic code rate/dimension questions, not all eight forbidden-trigram coordinate face complexes. Mészáros–Rónyai, *Shattering-Extremal Set Systems of Small VC-Dimension* (2013), establishes general extremality machinery, not these language-specific conditions. The 2020 automata VC paper studies shattering of word samples by automata, a different query universe. Chandgotia–Marcus–Richey–Wu (arXiv:2409.09024) and the classic Guibas–Odlyzko theory calculate word-avoidance counts via autocorrelations but do not determine coordinate-shattered-support families; the counting formulas are not claimed as new. An available result forbidding both monochromatic triples has a concept family strictly contained in the one-trigram class and does not imply its exact supports. Dedicated queries for single forbidden trigrams, equivalent aliases, automata and shattering-extremal families found no decisive coverage. Closest indexed work is recorded in the structured originality assessment. Residual risk: unindexed regular-language literature or a previously unrecognized general theorem may subsume these statements. Absence from search results is not a proof of historical priority.

## Value — PASS

This is a natural complete classification of the eight minimal nontrivial local binary pattern-avoidance constraints. The two exact support predicates and generating functions distinguish linearly different VC-growth slopes, while the extremality refinement proves that a complete face complex does not determine whether its realizing language saturates the shattering inequality. The latter is a sharp structural boundary, not a parameter substitution or isolated count. The theorem also provides constructive extension tests for every assignment on each shattered support.

## Limits

No statement about forbidden factors longer than three, multiple forbidden patterns, other alphabets or Littlestone dimensions is asserted. The published-source comparison is substantial but not exhaustive; independent verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
