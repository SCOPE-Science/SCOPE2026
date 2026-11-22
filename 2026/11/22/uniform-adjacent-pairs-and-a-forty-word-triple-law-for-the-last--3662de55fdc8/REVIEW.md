# Scientific review

## Correctness — PASS

The factorial recurrence gives a deterministic 64-state transition table. The supplied code exhaustively checks indegree five and the strict positive 4-step transition matrix (minimum four and maximum sixteen labeled paths per ordered state pair); hence the uniform stationary law and quantitative mixing are rigorous. The terminal-digit classification gives the exact 64-cell triple law, and a base-five block decomposition transfers it to natural density with a power-saving bound. Independent direct factorial arithmetic and all finite cases corroborate the derivation. The finite tests alone are not used as an infinite proof.

## Originality — PASS on inspected evidence

Lipka (2018) determines automaticity. Sobolewski (2018) supplies frequencies of a multi-digit *suffix of one factorial*, rather than joint values of three different consecutive factorials. Dresden describes the block recursion. These sources were read in full; neither states the forty-word three-index distribution or the uniform sixteen-pair law. Existing general automaton constructions can enable further computation but do not directly supply the evaluated theorem. Unindexed or other not-yet-inspected equivalent literature is a genuine residual risk.

## Value — PASS

The complete distribution is a motivated invariant of a classical digit sequence: uniformly independent adjacent digits coexist with twenty-four forbidden triples, three precise positive triple frequencies, and power-saving counting discrepancy. This structural transition is not an arbitrary isolated numeric slice, nor merely repetition of the generating recurrence.

## Limitations

Only decimal final nonzero digits at consecutive factorial indices are treated. The matrix-positivity lemma is a reproducible exhaustive finite certificate rather than a handwritten symbolic classification. No statement is made about all larger lags or other bases; bibliographic originality is best knowledge, not proof of uniqueness.

Self-review: passed. Independent audit: not yet performed.
