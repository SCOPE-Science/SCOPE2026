# Independent scientific audit — SCOPE-20260919-dc7870b56a90

Audited at: 2026-10-01T17:15:19.026518Z

Disposition: **failed**

## Correctness — PASS

The balanced \(q\)-adic construction has the required two-sided \(r^\alpha\) boundary-neighborhood law and, on odd scales, matching continuum and lattice symmetric-difference lower bounds. For \(\gamma<\eta\), one fixed nonzero Fourier coefficient of a spectral interval and the exact trace-defect identity give the \(R^{d-\gamma}\) lower bound. For \(\gamma>\eta\), Parseval's translation identity and the interval-lattice formula convert the spectral translation lower bound into \(R^{d-\eta}\). Tensoring in the remaining coordinates supplies \(R^{d-1}\). The claim is only along explicit lacunary scales, as stated.

### Correctness sources

- assigned RESULT.md
- Mayeli arXiv:2609.12226 full text
- published SCOPE all-regime trace-defect theorem

### Correctness risks

- The construction proves lower bounds along the stated scale sequence, not all-scale asymptotics.

## Originality — FAIL

A separate published SCOPE record at the audited snapshot proves a strictly stronger theorem for the same trace defect: it constructs explicit alternating-gap Cantor colorings with matching lower bounds in both off-critical regimes and on the whole critical line, and obtains the bounds for all sufficiently large integer scales. The assigned theorem is therefore contained as a weaker special case. Mayeli's primary paper itself supplies only the upper bounds and endpoint box sharpness, so the originality failure is due to the stronger published SCOPE coverage rather than the source paper.

### Equivalent formulations

The stronger record contains both assigned off-critical conclusions and uses a more uniform all-scale construction.

### Broader coverage

The assigned result is strictly dominated by the later/current broader theorem at the audited snapshot.

### Exact database or table

Exact same-object theorem coverage is decisive; this is not merely failure to find a database entry.

### Claim versus prior implication

The assigned final claim is a direct special case of the stronger published theorem.

### Sources inspected

- Trace-defect bounds for discrete Fourier concentration operators — https://arxiv.org/abs/2609.12226. BACKGROUND_NOT_COVERING: Theorem 2.2 gives the off-critical upper powers; the source's stated sharpness result is the classical endpoint box.
- Sharpness of all fractional trace-defect regimes for discrete Fourier concentration — published SCOPE record 2026/09/19/sharp-fractional-discrete-fourier-trace-defects--bbf7e58277be. COVERING: The record proves both assigned powers and additionally proves the entire fractional critical logarithmic line.

### Checked sources

- https://arxiv.org/abs/2609.12226
- published SCOPE 2026/09/19/sharp-fractional-discrete-fourier-trace-defects--bbf7e58277be
- Resultary semantic search

### Residual risks

- The two SCOPE records have date-only publication metadata, so intra-day chronology is not recoverable from those fields; at the audited snapshot, however, the stronger theorem is published coverage and the assigned claim cannot be validated as a distinct original result.

## Value — FAIL

The off-critical construction is mathematically useful, but as a standalone current finding it is redundant with a stronger published same-object theorem that covers both off-critical regimes and the critical line with stronger scale control.

### Value sources

- published SCOPE all-fractional trace-defect theorem

### Value risks

- This rejection is about distinct scientific contribution, not correctness of the assigned proof.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The claim only asserts lacunary-scale lower bounds and does not give plunge-count lower bounds.
- The complete original package is to be preserved in the assigned failed-attempt archive.
