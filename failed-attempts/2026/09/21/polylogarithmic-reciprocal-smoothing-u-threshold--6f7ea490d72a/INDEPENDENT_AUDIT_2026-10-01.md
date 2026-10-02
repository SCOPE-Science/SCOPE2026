# Independent scientific audit — SCOPE-20260921-6f7ea490d72a

Audited at: 2026-10-01T23:13:29.436856Z

Disposition: **failed**

## Correctness — PASS

Bieberbach's \(|b_1|\le2\) bound and the area theorem give the stated Cauchy--Schwarz bound on the reciprocal tail, so the defining root of \(H\) ensures zero-freeness. A second area-theorem estimate controls the \(\mathcal U\) functional uniformly. For every \(\sigma<1\), the starlike power family has reciprocal coefficients with the stated gamma asymptotic and produces a positive radial series whose terms are asymptotic to a divergent power, forcing failure of \(\mathcal U\) unless analyticity has already failed. Thus the bracket is correct.

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_threshold.py
- Ali--Obradović--Ponnusamy 2013

### Correctness risks

- The numerical root bracket is auxiliary; the theorem is intrinsically defined by the series equation.

## Originality — FAIL

A published SCOPE record dated 2026-09-20 already states the identical universal \(\mathcal U\)-tail bracket \(1\le\tau_{\mathcal U}\le s_*=1.41351950\ldots\), with the same defining tail series and the same area-theorem/Bieberbach upper-bound mechanism, together with an explicit starlike family ruling out every exponent below one. The assigned record is therefore an alternate derivation of a theorem already published the previous day.

### Equivalent formulations

The two statements are mathematically identical.

### Broader coverage

No broader surviving implication remains in the assigned record.

### Exact database or table

The exact numerical/root match is direct prior theorem coverage.

### Claim versus prior implication

Every substantive bound in the assigned final claim is already stated and proved in the earlier record.

### Sources inspected

- A quantitative bracket for the polylogarithmic reciprocal-smoothing threshold — published SCOPE 2026/09/20/polylog-reciprocal-u-threshold-bracket--9391b8ab7b89. COVERING: It is the same theorem with an equivalent summation index.
- Necessary and sufficient conditions for univalent functions — https://doi.org/10.1080/17476933.2011.599116. BACKGROUND: The decisive originality failure is the earlier SCOPE theorem, not the source paper.

### Checked sources

- published SCOPE 2026/09/20/polylog-reciprocal-u-threshold-bracket--9391b8ab7b89
- Ali--Obradović--Ponnusamy 2013
- Resultary semantic search

### Residual risks

- No access uncertainty can restore originality against the exact earlier published SCOPE theorem.

## Value — FAIL

The underlying threshold improvement is worthwhile, but this assigned record repeats a theorem already published the previous day with the same mechanisms and constants. Repackaging it does not constitute a distinct motivated mathematical contribution.

### Value sources

- published SCOPE 2026/09/20 threshold-bracket theorem

### Value risks

- The alternate lower family can be pedagogically useful but does not establish separate scientific value.

## Limitations

- Scientific rejection is for originality and value, not correctness.
- The exact universal \(\mathcal U\) threshold remains unknown within the displayed bracket.
- The assigned bracket is already covered by an earlier published record.
