# Independent Audit — 2026/09/11/052

- Audit date: 2026-09-28 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `865f8fb34b5933dfc1c990c02a897cc2b2c0c226`
- Disposition: **FAILED**

## Correctness

**PASS** — For beta=3/5, the scaled truncation level is N^{beta-1/2}=N^{1/10}. For any fixed K below that level, a Pareto-3 entry exceeds K sqrt(N) with probability of order N^{-3/2}; among order N^2 off-diagonal entries the expected count is order N^{1/2}, so the maximum scaled off-diagonal entry diverges in probability. The diagonal maximum is o_P(1) under the stated tail, and the two-coordinate Rayleigh quotient yields lambda_max≥max_{i<j}|H_ij|-max_i|H_ii|. Thus lambda_max diverges and a Tracy–Widom limit centered at 2 is impossible at beta=3/5. The variance-renormalization estimates for zero-fill, clipping, and conditioning are also asymptotically correct.

## Originality

**FAIL** — The mechanism is the standard extreme-entry obstruction for heavy-tailed Wigner matrices: with tail exponent alpha=3, order N^2 entries produce extremes on the N^{2/3} unscaled scale, and any truncation left above sqrt(N) permits scaled entries to grow. Lee–Yin's necessity theory and the established alpha<4 heavy-tail literature already identify large entries as the obstruction to Tracy–Widom edge universality. Choosing beta=0.6 and applying a union bound plus a 2x2 Rayleigh quotient is a direct specialization of that mechanism, not an original phase-transition result.

## Scientific value

**FAIL** — The counterexample is a clear correction to the particular proposed beta_c=2/3 diagram, but it is obtained by the most basic single-entry necessary condition and does not identify the actual phase diagram, a new limiting law, or a new universality threshold theorem. Its useful content is primarily diagnostic—showing the proposed statement fails already for beta>1/2—rather than a sufficiently substantive standalone research contribution.

## Limitations

- The result refutes the claimed Tracy–Widom half by one exponent beta=3/5; it does not characterize the entire intermediate regime.
- The audit does not assess the record's untouched beta>2/3 Poisson-persistence claim.
- The numerical simulation is unnecessary to the proof and was not used for the verdict.

## Sources

- A Necessary and Sufficient Condition for Edge Universality of Wigner Matrices — Ji Oon Lee; Jun Yin: https://arxiv.org/abs/1206.2251 — Establishes the tail criterion for Tracy–Widom edge universality and the role of rare large entries.
- Poisson convergence for the largest eigenvalues of heavy tailed random matrices — Antonio Auffinger; Gérard Ben Arous; Sandrine Péché: https://arxiv.org/abs/0710.3132 — Established heavy-tail regime in which extreme entries govern top eigenvalues.

GitHub was read only as evidence. The record's pre-existing `AUDIT.json` was inspected only after an independent assessment and was not treated as authority. No repository mutation was performed by this audit chat.
