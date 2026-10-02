# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260919-3eaf705861a0`

## Correctness — PASS

The cancellation algebra is correct. A resonant cubic monomial \(Cz_pz_q\bar z_r\) contributes \(R^2\operatorname{Im}(Ce^{i(\theta_p+\theta_q-\theta_r-\theta_j)})\) to the straight-isochrone phase projection. In particular \(z_k^2\bar z_j\) produces the missing pairwise second harmonic. Projecting the stated controller term by term gives exactly \(-f_j^{(2)}\); because the controller enters at order \(\varepsilon^2\), deformation/cross terms begin only at order \(\varepsilon^3\). The inspected symbolic verifier independently reduces the full residual to zero and enumerates the relevant cubic phase vectors.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_cubic_phase_cancellation.py
- earlier exact-cubic-counterterm SCOPE theorem
- Muolo–Nakao–Bick source

### Correctness risks

- The statement is only through second order in the specific three-oscillator straight-isochrone reduction.

## Originality — FAIL

An earlier published SCOPE record dated 2026-09-18 states the same result for the same Stuart–Landau triad: it gives an explicit globally phase-equivariant cubic counterterm cancelling the entire second-order correction and identifies \(z_j^2\bar z_i\) as the omitted pairwise second-harmonic direction. After using \(R^2=a\) and matching signs, its \(Q_i\) controller is term-for-term equivalent to the audited \(H_i\). Thus every originality-bearing assertion is already covered before this record.

### equivalent_formulations

Searches:
- Resultary semantic search for complete cubic Stuart–Landau phase compensation and the \(z_j^2\bar z_i\) channel
- direct comparison with SCOPE-exact-cubic-counterterm-stuart-landau-phase-reduction--40d4eb3f4497

Evidence:
- The earlier theorem has the same source model, same full \(O(\varepsilon^2)\) cancellation, and same missing monomial.

Reasoning:
The two controller formulas are equivalent after \(R^2=a\) and the sign convention for the counterterm.

### broader_coverage

Searches:
- earlier exact cubic counterterm theorem
- general synchronization-engineering literature

Evidence:
- The earlier SCOPE theorem is exact source-specific coverage; general inverse-design papers are broader background.

Reasoning:
The final claim is a duplicate, not merely an application of broader qualitative design theory.

### exact_database_or_table

Searches:
- current Resultary Stuart–Landau phase-design findings

Evidence:
- The 2026-09-18 exact-cubic-counterterm record is a direct theorem-level match.

Reasoning:
No table lookup is needed once direct coverage is established.

### claim_vs_prior_implication

Searches:
- term-by-term implication comparison

Evidence:
- Both results cancel Eq. (55) completely and use the same cubic second-harmonic channel.

Reasoning:
The audited controller is mechanically obtainable from the earlier displayed counterterm.

### source_inspections

- **Exact cubic counterterm cancels the full second-order phase correction in a Stuart–Landau triad** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-exact-cubic-counterterm-stuart-landau-phase-reduction--40d4eb3f4497. Trigger: Exact earlier Resultary match. Material read: Complete published RESULT.md. Method: Term-by-term theorem and controller comparison. Assessment: DECISIVE PRIOR COVERAGE. Evidence: It gives the same full cancellation and explicitly names the same omitted \(z_j^2\bar z_i\) harmonic.
- **Assigned symbolic phase-cancellation verifier** — artifacts/verify_cubic_phase_cancellation.py. Trigger: Correctness replay. Material read: Complete source and saved output. Method: Line-by-line symbolic inspection. Assessment: Supports correctness but cannot restore originality. Evidence: The full projected residual simplifies identically to zero.
- **Physical and emergent nonpairwise interactions in oscillator networks** — https://arxiv.org/abs/2609.20632. Trigger: Primary source being corrected/refined. Material read: Accessible abstract/scope material and the explicit equation content reproduced in the audited package; full source text was unavailable through the attempted route. Method: Background comparison. Assessment: Not needed for originality failure because earlier exact source-specific coverage is decisive. Evidence: Both SCOPE records target the same explicit second-order phase equation.

### checked_sources

- SCOPE-exact-cubic-counterterm-stuart-landau-phase-reduction--40d4eb3f4497
- assigned RESULT.md and verifier
- arXiv:2609.20632
- Resultary search

### residual_risks

- No residual originality survives the exact earlier theorem.

## Scientific value — FAIL

The underlying cancellation is a useful correction to the source paper, but this record adds no independent mathematical fact beyond the already published exact counterterm theorem. Under the required value bar, a duplicate reformulation of a known source-specific controller is not a new structural lemma or motivated unknown invariant.

### Value sources

- earlier exact cubic-counterterm theorem
- assigned duplicate formulation

### Value risks

- This is a scientific-value failure for the record as a new finding, not a claim that the covered theorem is unimportant.

## Limitations

- Correctness passes.
- Originality and scientific value fail because an earlier published theorem already contains the same source-specific counterterm and missing harmonic.
- The failed package is preserved in full at the assigned failed path.

## Disposition

**FAILED**
