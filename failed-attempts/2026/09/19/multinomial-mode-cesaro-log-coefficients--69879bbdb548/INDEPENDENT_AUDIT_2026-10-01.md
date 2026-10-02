# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-69879bbdb548`

## Correctness — PASS

The all-orders formula is correct. Janson's fixed-proportion Jefferson seat-excess law gives bounded modal displacements with convergence of every polynomial moment. Combining the marginal moment-generating function with the Bernoulli-polynomial generating function cancels the source-independent factor and yields \(e^w((e^w-1)/w)^{n-2}\); Stirling-number coefficient extraction produces the stated \(A_m(n)\), and the weighted category sum collapses to \(\sum_i p_i=1\). The verifier was read in full and its first four empirical Cesaro means agree with the closed formula to the reported finite-sample errors.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_modal_cesaro.py and verification.txt
- Janson 2014 Jefferson seat-excess theorem
- Elezović 2026 local multinomial expansion

### Correctness risks

- Only the generic rationally independent regime is proved.
- The numerical check is corroborative, not the proof.

## Originality — FAIL

The theorem is already contained in an earlier 2026-09-18 SCOPE record. That earlier record proves the full polynomial transfer law, the universal Cesaro mean of every logarithmic coefficient, and more: it also computes the first nonuniversal second multiplicative coefficient. The generating function there is algebraically identical to the present Bernoulli–Stirling formula. A later provenance-corrected September 19 record explicitly identifies this assigned record as a later restatement. Current originality therefore fails decisively.

### equivalent_formulations

Searches:
- Resultary search for multinomial modal Cesaro logarithmic coefficients
- direct comparison with `multinomial-mode-cesaro-universality--a66b1067c370`

Evidence:
- The 2026-09-18 theorem already states universality for every \(c_k\) and the same first coefficients.

Reasoning:
Its generating-function coefficient \(b_{m,n}\) equals the present Stirling-number coefficient by the standard expansion used here.

### broader_coverage

Searches:
- earlier polynomial-transfer theorem
- later provenance-corrected multinomial Cesaro record

Evidence:
- The earlier theorem is strictly broader because it also gives joint polynomial averaging and a nonuniversal \(Q_2\) formula.

Reasoning:
The assigned claim is a direct special case/re-expression of the earlier result.

### exact_database_or_table

Searches:
- current Resultary multinomial-mode records

Evidence:
- The later provenance-corrected record explicitly lists this record and the earlier 9/18 theorem as prior occurrences.

Reasoning:
No table issue remains after exact theorem coverage is established.

### claim_vs_prior_implication

Searches:
- formula-level implication comparison

Evidence:
- Both formulas produce identical \(\overline c_1,\overline c_2,\overline c_3\), and the all-order generating functions are the same under elementary algebra.

Reasoning:
This is exact mathematical duplication, not merely similar subject matter.

### source_inspections

- **On-slice Cesàro laws for multinomial modes** — 2026/09/18/SCOPE-multinomial-mode-cesaro-universality--a66b1067c370. Trigger: Earlier exact Resultary match. Material read: Complete RESULT.md. Method: Full theorem and proof comparison. Assessment: DECISIVE COVERAGE. Evidence: It proves all-order universal log-coefficient means and the stronger polynomial transfer law.
- **Universal Cesàro averages of multinomial modal log coefficients — provenance-corrected presentation** — 2026/09/19/SCOPE-universal-cesaro-multinomial-modal-log-coefficients--aa06a9f55cdc. Trigger: Later provenance record found in the same semantic search. Material read: Complete RESULT.md. Method: Chronology and theorem comparison. Assessment: Confirms the theorem was already present earlier and treats this assigned record as an alternate derivation. Evidence: Its status section explicitly names the 2026-09-18 theorem and this assigned record.
- **Assigned modal Cesaro verifier** — artifacts/verify_modal_cesaro.py. Trigger: Numerical formula check. Material read: Complete source and saved output. Method: Line-by-line inspection. Assessment: Correct reproducibility evidence only. Evidence: The first four empirical means converge to the same already-covered constants.

### checked_sources

- earlier 2026-09-18 SCOPE theorem
- later provenance-corrected SCOPE record
- assigned RESULT.md and verifier
- fresh Resultary search

### residual_risks

- No residual originality remains for the stated theorem.

## Scientific value — FAIL

The theorem itself is mathematically useful, but this record adds only an alternate Bernoulli/Stirling derivation and verification of a theorem already proved in a strictly stronger earlier record. Under the required value bar, a duplicate derivation of a covered result is not a separate new scientific finding.

### Value sources

- earlier polynomial-transfer/Cesaro theorem
- assigned alternate derivation

### Value risks

- The failed value judgment is about this record as a new finding, not about the importance of the theorem.

## Limitations

- Correctness passes.
- Originality and value fail because a strictly stronger earlier SCOPE theorem already contains the result.
- The generic arithmetic assumptions remain as in the earlier theorem.

## Disposition

**FAILED**
