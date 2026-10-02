# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-87f8866a2ffc`

## Correctness — PASS

The Floquet conclusions are correct. For the stated reverser, the divergence is odd, so an \(S\)-symmetric periodic orbit has zero integrated divergence; Liouville's formula then gives unit monodromy determinant and reciprocal transverse multipliers. The explicit family winds through the thermostat circle and is setwise \(S\)-symmetric. At \(a=0\), the normal system has constant coefficients and directly yields the parity-dependent elliptic/saddle multipliers. Removing the first derivative from the central orbit's normal equation by the stated periodic gauge gives the displayed two-harmonic Hill equation, whose monodromy also has determinant one. For a nonsymmetric periodic orbit, reversibility conjugates its monodromy to the inverse spectrum of its reversed partner.

### Correctness sources

- assigned RESULT.md
- Lamb–Roberts reversible-systems survey
- current published trigonometric Nosé–Hoover Floquet refinements

### Correctness risks

- The result is local Floquet information and does not establish nonlinear stability or existence of the numerically reported attractor.

## Originality — FAIL

The central mechanism is a standard theorem of reversible dynamics: the Floquet spectrum of a reversing-symmetric periodic orbit is reciprocal, which already forbids an asymptotically attracting or repelling symmetric cycle. Applying that theorem to the explicit orbit family is a direct symmetry check. Current published work on the same trigonometric Nosé–Hoover model also explicitly states the same zero-contraction/unit-determinant obstruction and repeats the Hill reduction. The remaining \(a=0\) parity formulas are an elementary constant-coefficient specialization. Therefore the final package does not pass the originality bar as a new mathematical result.

### equivalent_formulations

Searches:
- Resultary: reversible Floquet trigonometric Nose Hoover symmetric family parity a=0
- classical reversible periodic orbit reciprocal Floquet multipliers

Evidence:
- Current model-specific records explicitly contain the symmetric-orbit reciprocal-multiplier obstruction and Hill reduction.
- Classical reversible-systems literature already treats reciprocal Floquet spectra of symmetric periodic solutions.

Reasoning:
Equivalent formulations via unit determinant, reciprocal spectrum and attractor–repeller pairing were compared.

### broader_coverage

Searches:
- Lamb–Roberts 1998 survey
- current cohomological-contraction Floquet result
- current semifinite-gap Floquet result

Evidence:
- The general reversible theorem is broader than the model-specific no-attractor claim; the later model-specific result also contains the same central orbit Hill reduction.

Reasoning:
The audited theorem is a specialization of established general structure, with current exact model-specific overlap as additional confirmation.

### exact_database_or_table

Searches:
- current Resultary trigonometric Nosé–Hoover records

Evidence:
- No finite database is needed: theorem-level coverage exists.

Reasoning:
The database/table check is inapplicable as an originality source because the result is covered structurally.

### claim_vs_prior_implication

Searches:
- implication from reciprocal Floquet theorem to explicit family

Evidence:
- Once setwise reversing symmetry of the displayed orbit is checked, reciprocal transverse multipliers and the no-attractor/no-repeller conclusion follow immediately.

Reasoning:
The \(a=0\) multipliers and Hill gauge are routine computations, not an independent originality-bearing theorem.

### source_inspections
- **Time-reversal symmetry in dynamical systems: a survey** — https://doi.org/10.1016/S0167-2789(97)00199-1. Trigger: Classical general theory of reversible periodic orbits. Material read: Accessible bibliographic/theorem-scope material located in the literature search. Method: General-theorem implication comparison. Assessment: Provides prior structural coverage of reciprocal Floquet behavior for reversing-symmetric periodic dynamics. Evidence: The audited no-attractor conclusion is the standard reciprocal-spectrum consequence.
- **Cohomological contraction and a Floquet edge in the trigonometric Nosé–Hoover flow** — https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19. Trigger: Highly relevant current source-specific result. Material read: Complete published RESULT.md. Method: Full model-specific statement comparison. Assessment: CURRENT COVERAGE of zero integrated contraction for symmetric cycles, unit transverse determinant, and the central Hill reduction. Evidence: It states that an \(S\)-symmetric periodic orbit cannot attract or repel and derives the same Whittaker–Hill normal form.
- **Trigonometric Nosé–Hoover oscillator: chaos, periodic orbits and integrability** — https://arxiv.org/abs/2609.19958. Trigger: Primary source defining the flow and explicit periodic family. Material read: Accessible abstract/metadata; full arXiv/OA text was not obtainable in this run and the authorized route was unavailable. Method: Background-scope comparison only. Assessment: Supplies the model; originality failure already follows from general reversible theory and current exact coverage. Evidence: The audited calculations use the source's explicit family and normal variational equation.

### checked_sources

- https://doi.org/10.1016/S0167-2789(97)00199-1
- https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19
- https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-semifinite-gap-floquet-trigonometric-nose-hoover--87ff381e2668
- https://arxiv.org/abs/2609.19958

### residual_risks

- The source-specific \(a=0\) parity calculation may not have appeared verbatim before, but it is mechanically implied by the displayed constant-coefficient normal system.

## Scientific value — FAIL

The source-specific consequences are useful diagnostics, but the final claim is built from a routine application of the classical reciprocal-Floquet theorem, a direct symmetry check, a constant-coefficient linearization, and a standard first-derivative-removal gauge. Under the required value bar this is a textbook specialization rather than a new structural boundary or independently motivated invariant.

### Value sources

- classical reversible Floquet theory
- source explicit periodic family
- current source-specific Floquet refinement

### Value risks

- This does not diminish its explanatory utility for interpreting the source's numerical windows; it means the mathematical contribution is too routine for acceptance as a new finding.

## Limitations

- The mathematical calculations are correct.
- Originality fails because the main mechanism is classical and currently repeated in model-specific published work.
- Scientific value also fails because the remaining source-specific steps are routine specializations.
- No claim is made about nonlinear/KAM stability or global chaotic bifurcations.

## Disposition

**FAILED**
