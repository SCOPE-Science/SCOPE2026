# Mathematical audit — 2026-10-01

Record: `SCOPE-20260930-2af8b6e84307`

## Correctness — PASS

Knudstorp's source supplies an effective tile-set-to-formula map with non-tiling equivalent to theoremhood throughout the interval. Non-tiling is recursively enumerable because plane tiling is equivalent to tiling every finite octant, so a failed finite octant is a decidable existential witness. Berger's effective simulation maps a Turing machine to a tile set that fails to tile exactly when the machine halts, making non-tiling recursively-enumerable-hard. Therefore every recursively enumerable target logic in the interval is \(\Sigma^0_1\)-complete under the same computable many-one map, and complementing gives \(\Pi^0_1\)-completeness. Knudstorp explicitly records recursive enumerability of all seven named systems.

### Correctness sources

- Knudstorp, arXiv:2605.29880v1 full HTML
- Berger's effective domino construction as used explicitly by Knudstorp
- assigned RESULT.md

### Correctness risks

- The arbitrary intermediate-set statement requires recursive enumerability as an explicit hypothesis.

## Originality — FAIL

The exact arithmetical-level classification is not printed as a named theorem in Knudstorp's paper, but it is mechanically implied by the proof already given there. The source states that the named logics are recursively enumerable, constructs the effective formula reduction, proves the theoremhood/non-tiling equivalence, and explicitly invokes Berger tile sets with machine halting iff non-tiling. Combining an r.e. upper bound with a displayed halting many-one reduction is the standard textbook criterion for \(\Sigma^0_1\)-completeness. Under the required implication-based standard, this is covered even without the exact phrase '\(\Sigma^0_1\)-complete'.

### equivalent_formulations

Searches:
- Resultary: Knudstorp relevant logic Sigma_1 complete recursively enumerable non-tiling theoremhood
- arXiv:2605.29880v1 full HTML
- searches for named relevant logics plus r.e.-complete/halting-level terminology

Evidence:
- Knudstorp explicitly states recursive enumerability for \(\mathsf S\) and the six other named systems.
- The paper explicitly gives the effective tiling formula and later writes a Turing-machine construction with halting iff non-tiling and theoremhood iff non-tiling.

Reasoning:
The equivalent formulation as r.e.-complete theoremhood is exactly the standard consequence of those two properties.

### broader_coverage

Searches:
- Knudstorp full proof
- classical Berger reduction

Evidence:
- The prior source already contains both the many-one lower bound and r.e. upper bound ingredients.

Reasoning:
No stronger or additional nonstandard reduction is needed for the audited classification.

### exact_database_or_table

Searches:
- current Resultary logic-complexity findings

Evidence:
- Only the audited finding states the classification verbatim, but theorem-level implication from the primary source is decisive.

Reasoning:
Textual absence does not defeat implication-based coverage.

### claim_vs_prior_implication

Searches:
- claim versus Knudstorp Theorem 6.4 and tiling reduction

Evidence:
- The source states the named theorem sets are r.e. and gives a halting-to-non-tiling-to-theoremhood computable map.

Reasoning:
Those facts already prove \(\Sigma^0_1\)-completeness by a standard one-line computability argument.

### source_inspections

- **Undecidability in Relevant Logic** — https://arxiv.org/html/2605.29880v1. Trigger: Primary source containing the reduction and recursive-enumerability facts. Material read: Full relevant Introduction, tiling preliminaries/reduction architecture, and Section 6 results including Theorem 6.4 and the explicit Berger machine example. Method: Primary full-text implication reconstruction. Assessment: DECISIVE IMPLICATION COVERAGE. Evidence: The paper states recursive enumerability and exhibits the effective halting-to-non-tiling/theoremhood mechanism.

### checked_sources

- https://arxiv.org/html/2605.29880v1
- Berger 1966 as cited and used there
- current Resultary exact-complexity search
- assigned RESULT.md

### residual_risks

- No historical-priority claim is made about whether the arithmetical-hierarchy label appeared elsewhere; the failure is mechanical implication from the inspected primary source.

## Scientific value — FAIL

Recording the exact arithmetical-hierarchy label is informative, but the mathematical step from 'recursively enumerable' plus an explicit halting many-one reduction to '\(\Sigma^0_1\)-complete' is a routine textbook deduction. It does not add a new reduction, boundary, invariant, or structural lemma beyond Knudstorp's proof, so it does not meet the required value bar as a separate finding.

### Value sources

- Knudstorp's explicit reduction and r.e. statements
- standard computability-theory completeness criterion

### Value risks

- Failure is not a correctness defect.

## Limitations

- Correctness passes.
- Originality and scientific value fail because the final classification is mechanically implied by the primary source.
- The general interval statement remains conditional on recursive enumerability of the intermediate theorem set.

## Disposition

**FAILED**
