# Scientific review

## Correctness (C): PASS
The exact object is the sum of length divided by least period over all maximal periodic occurrences, with a separate check for period-one runs. The proof eliminates nonadjacent one-pair periods by two-block parity, derives two position-sensitive upper bounds for the only possible nonunary run periods, and uses an integer two-case optimization with \(m\ge3\). The explicit witness attains equality with four zero runs and two nonunary runs; its period lengths and endpoints are checked directly. Independent exact-rational enumeration of 31,465 inputs and 715 cross-checks of distinct run-enumeration methods corroborates the proof. Risk: the interval and least-period convention must be preserved in any adaptation.

## Originality (O): PASS against the inspected evidence
Czarkowski (CPM 2026) considers the same sum-of-exponents invariant but optimizes over all words, providing only general linear bounds. The closest mathematical record on three-one binary strings classifies the **number** of runs, not their rational exponent sum or its sharp extremum; its full theorem and argument were read and do not logically imply the present numerical extremum without a new interval optimization. The classical Runs Theorem concerns the number, not weighted exponents. Targeted prior-result and literature searches for exact fixed-three-marker exponent sums and aliases found no stronger coverage. The possibility of an earlier unindexed or implicit exact specialization remains.

## Mathematical value (V): PASS
This is a natural, exact sharp extremal variant of a major run statistic at the first sparse composition permitting two distinct nonunary run periods and up to four unary zero runs. The theorem resolves all lengths from thirteen onward, exhibits a nontrivial four-step correction to the linear main term, and distinguishes maximizing exponent sums from maximizing run counts. The finite threshold is sharp, as length twelve does not satisfy the formula. No consequence for unrestricted optimal strings is claimed.

## Literature and limitations
The closest sources are Czarkowski 2026 (DOI 10.4230/LIPIcs.CPM.2026.23) and the 2026-11-08 exact run-count record cited in RESULT.md. General bounds cannot imply the sharp composition result; run counts lack the run-length/period data needed to optimize the exponent total. Independent review is pending, and possible unindexed equivalent derivations are residual risks.

Self-review: passed. Independent audit: not yet performed.
