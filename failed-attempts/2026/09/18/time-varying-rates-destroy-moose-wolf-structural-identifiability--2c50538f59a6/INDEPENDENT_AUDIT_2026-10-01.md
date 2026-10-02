# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-2c50538f59a6`

## Correctness — PASS

The gauge is exact. On any positive trajectory away from the carrying-capacity surface, divide the prey and predator equations by the corresponding state and solve pointwise for the two free time-varying rates after choosing any admissible constant interaction triple. Substitution recovers the original derivatives identically for both the Holling type-II and ratio-dependent denominators. Even without the prey reconstruction, changing the conversion constant can always be absorbed by the free predator-death function. Positivity survives sufficiently small parameter changes at an interior positive representation by continuity. The assigned numerical script is only a roundoff-level illustration of this exact algebra.

### Correctness sources

- assigned RESULT.md
- artifacts/verify_gauge.py
- Martinelli arXiv:2211.13507 on time-varying parameters as unknown inputs
- Singh–Kumari arXiv:2609.20793v1

### Correctness risks

- A fixed finite neural-network architecture defines a different finite-dimensional identifiability problem.
- The full three-constant formula is stated away from the surface where the fourth-power logistic factor vanishes.

## Originality — FAIL

Current published coverage is decisive. Two later September 19 findings state the same source-specific gauge for both Moose–Wolf models, the same conclusion that autonomous identifiability cannot be transferred by pointwise freezing, and the same local persistence under positivity constraints. One of them was inspected in full and gives the identical transformed-rate formulas. Under the required current-coverage rule, the audited final claim is therefore covered. The later date means this audit does not adjudicate historical priority on September 18.

### equivalent_formulations

Searches:
- Resultary semantic search for time-varying Moose–Wolf structural identifiability gauge
- direct comparison with `SCOPE-time-varying-rates-gauge-moose-wolf-parameters--525e2b442818` and `SCOPE-gauge-nonidentifiability-nonautonomous-moose-wolf-models--0adfd4c49c72`

Evidence:
- Both later results match the same two models and the same three-constant compensated-rate family.

Reasoning:
Equivalent formulations through direct reconstruction from a trajectory and through transformations from one representation to another are algebraically identical.

### broader_coverage

Searches:
- later source-specific gauge theorems
- general unknown-input identifiability literature

Evidence:
- The later source-specific theorem fully covers the audited result; general literature additionally explains why free time functions require separate identifiability analysis.

Reasoning:
The exact current source-specific coverage is sufficient; broader general theory is contextual rather than the decisive novelty comparison.

### exact_database_or_table

Searches:
- current Resultary Moose–Wolf identifiability records

Evidence:
- Two exact later theorem-level duplicates were located.

Reasoning:
No finite database/table issue is involved once exact theorem coverage exists.

### claim_vs_prior_implication

Searches:
- formula-by-formula implication comparison

Evidence:
- The later theorem gives the same Holling and ratio-dependent gauge formulas, local positivity argument, and autonomous-freezing critique.

Reasoning:
Every originality-bearing part of the audited final claim is implied by the current published theorem.

### source_inspections

- **Time-varying rates gauge away constant parameters in the Moose–Wolf inverse model** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-time-varying-rates-gauge-moose-wolf-parameters--525e2b442818. Trigger: Exact later semantic match. Material read: Complete published RESULT.md. Method: Full theorem and formula comparison. Assessment: DECISIVE CURRENT COVERAGE. Evidence: It states the same gauges for both response models and the same structural-identifiability consequence.
- **Exact gauge non-identifiability in non-autonomous Moose–Wolf models** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-gauge-nonidentifiability-nonautonomous-moose-wolf-models--0adfd4c49c72. Trigger: Second exact later match. Material read: Complete published RESULT.md. Method: Independent statement comparison. Assessment: DECISIVE CURRENT COVERAGE. Evidence: It repeats the same three-constant indistinguishability family and positivity-locality argument.
- **Identifiability of nonlinear ODE Models with Time-Varying Parameters** — https://arxiv.org/abs/2211.13507. Trigger: General prior framework for time-varying unknowns. Material read: Accessible abstract and scope material. Method: Background framework comparison. Assessment: General prior art, not the source-specific decisive coverage. Evidence: It treats time-varying parameters as unknown inputs requiring dedicated identifiability analysis.

### checked_sources

- two later exact Resultary gauge theorems
- Martinelli arXiv:2211.13507
- assigned RESULT.md and verify_gauge.py
- current Resultary semantic search

### residual_risks

- The exact covering findings postdate the audited record by one day, so current coverage does not settle historical first discovery.

## Scientific value — PASS

The gauge is a worthwhile model-specific correction because it invalidates a structural-identifiability inference used to justify joint recovery of ecological constants and free rate functions, and it identifies what extra information is needed to break the ambiguity. Its value survives even though the result is now covered.

### Value sources

- source-specific inverse problem
- general unknown-input identifiability framework
- later exact gauge theorem

### Value risks

- The theorem says nothing about identifiability of a particular finite neural architecture or about forecasting quality.

## Limitations

- Correctness and scientific value pass; originality fails under current published coverage.
- Later covering records postdate this record, so historical priority is not adjudicated.
- The theorem concerns freely time-varying ODE rates, not a fixed finite neural architecture.

## Disposition

**FAILED**
