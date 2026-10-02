# Independent mathematical audit — Morse-Bott selection for the cell-polarization localization clock

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **failed**.

## Correctness

**PASS** — The Morse–Bott tubular calculation gives the claimed codimension powers and inverse-normal-Hessian density. Curve components dominate isolated points, and insertion into the established localization clock gives the two-thirds threshold exponent and one-third normal-width exponent. The spherical example reproduces the stated cap coefficient.

## Originality

**FAIL** — The final claim is mechanically implied by two broader prior ingredients: the primary paper already characterizes limiting measures by normalized positive-part caps for arbitrary signal geometry, and the earlier published localization-clock theorem gives the general time clock for arbitrary cap function. Standard Morse–Bott tubular asymptotics then give every advertised curve/weight/exponent consequence.

### Equivalent formulations

Searches/sources: Niethammer–Röger–Velázquez Theorems 3.6 and 3.12; 19 September localization-clock theorem.

Evidence: The primary source supplies the normalized-cap characterization. The prior clock theorem supplies the general cap-to-time inversion.

The audited statement is the clean-critical-manifold evaluation of those general formulas.

### Broader coverage

Searches/sources: primary cap theorem for arbitrary signal geometry; general localization clock; classical Morse–Bott tubular asymptotics.

Evidence: The primary and prior clock results are both broader than the Morse–Bott curve specialization.

Their combination dominates the audited claim.

### Exact database or table

Searches/sources: Resultary search for cell polarization Morse-Bott maxima and localization clock; 18 and 19 September published records.

Evidence: The search located the earlier general clock and earlier isolated-Morse results on the same model.

The published-record chain exposes the prior implication.

### Claim versus prior implication

Searches/sources: insert Morse–Bott cap power into the prior clock; normalize the source cap measure in tubular coordinates.

Evidence: The curve exponent follows directly from the three-halves cap power. The inverse-normal-Hessian density and codimension dominance follow from the same standard change of variables.

No additional nonstandard lemma is needed beyond prior general theorems and textbook Morse–Bott geometry.

### Source inspections

- **Localization properties of a free boundary problem for cell polarization** — BROADER_COVERAGE.
  Identifier: https://arxiv.org/abs/2609.20609
  Material read: complete arXiv HTML including Theorems 3.6 and 3.12 and Section 4
  Evidence: The source gives the general normalized-cap characterization.
- **A localization clock and self-similar rates for the cell-polarization slow flow** — BROADER_COVERAGE.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-self-similar-localization-cell-polarization-slow-flow--76b7ab9743ed
  Material read: complete RESULT.md
  Evidence: It proves the general clock and power-law inversion used here.
- **Morse maxima force a t^{-1/4} localization law in the slow cell-polarization limit** — RELATED_PRIOR.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-morse-maxima-t-quarter-cell-polarization-localization--95d03c9c0771
  Material read: complete RESULT.md
  Evidence: It already carries out the analogous Hessian-cap calculation for isolated maxima.

Residual originality risks:
- None identified.

## Scientific value

**FAIL** — After the general cap characterization and localization clock are treated as prior, the remainder is the standard Morse–Bott tubular integral and direct exponent substitution. The formulas are useful but routine under the stated value bar.

## Final assessment

The package is scientifically rejected because the final claim does not pass all three C/O/V axes. Correct calculations are retained as failed evidence.

This is a best-of-knowledge mathematical audit, not formal proof-assistant verification or a guarantee against undiscovered prior art.
