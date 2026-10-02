# Independent scientific audit — SCOPE-20260919-75866f4b972e

Audited at: 2026-10-01T15:09:23.525185Z

Disposition: **failed**

## Correctness — PASS

The cut-set converse and block-Markov pipeline give the exact capacity \(D+\min\{C_1,C_2\}\). For the proposed expressions, decode-forward is at most \(C_1\); the common compress-forward relaxation plus the conditioned post-processing SDPI gives \(D+\eta C_2\). The BSC specialization and numerical gap values agree with the inspected verifier and independent arithmetic checks.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_bsc_family.py
- published SCOPE relay-family result

### Correctness risks

- The finite BSC grid is only a sanity check; the all-channel statement rests on the analytic SDPI argument.

## Originality — FAIL

A published SCOPE record dated 2026-09-18 already proves the same post-SDPI relay-family mechanism, exact orthogonal-channel capacity, proposed-rate upper bound, full BSC wedge \(0<\delta_1\le\delta_2<1/2\), identical gap formula, and the same \(1/8\) numerical witness. The assigned record extends the noiseless direct coordinate from one bit to \(D=\log_2 M\) and allows general finite input alphabets, but the proof is the same capacity/SDPI calculation with the constant \(1\) replaced by \(D\).

### Equivalent formulations

The assigned theorem is the same orthogonal relay construction with a \(D\)-bit noiseless direct coordinate; replacing \(1\) by \(D\) is a parameter extension, not a new implication.

### Broader coverage

The assigned general-alphabet version is broader syntactically but does not introduce a new proof mechanism or new BSC counterexample region.

### Exact database or table

This is theorem coverage rather than a tabulated invariant; the earlier theorem is decisive.

### Claim versus prior implication

The final claim is mechanically implied by the earlier template plus the obvious entropy-capacity replacement for a noiseless \(M\)-ary coordinate.

### Sources inspected

- A post-SDPI family of orthogonal relay-channel counterexamples — published SCOPE record 2026/09/18/post-sdpi-relay-counterexample-family--40cc30383546. COVERING: It contains the same SDPI obstruction, same BSC wedge, same gap, and same \(p=q=1/8\) witness.
- Counterexample to a Proposed Capacity Characterization of the Relay Channel — https://arxiv.org/abs/2609.18727. BACKGROUND: This source is the fixed BSC counterexample being generalized; it is not needed for the decisive originality failure because the broader 2026-09-18 SCOPE theorem already covers the family mechanism.

### Checked sources

- published SCOPE 2026/09/18/post-sdpi-relay-counterexample-family--40cc30383546
- https://arxiv.org/abs/2609.18727
- https://arxiv.org/abs/2609.15709

### Residual risks

- No residual comparison can restore originality against the explicit earlier published SCOPE family theorem.

## Value — FAIL

The general-\(D\) rewrite is mathematically correct and may be expository, but it is a routine parameter generalization of an already-published structural theorem. Under the stated value bar, a mechanically implied extension with the same counterexample family and same proof does not qualify as a distinct validated finding.

### Value sources

- published SCOPE 2026/09/18/post-sdpi-relay-counterexample-family--40cc30383546

### Value risks

- This is a scientific-value judgment, not a statement that the formulas are unhelpful.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The theorem addresses only the specific proposed DF/C-CF/U-CF characterization on the stated product relay architecture.
