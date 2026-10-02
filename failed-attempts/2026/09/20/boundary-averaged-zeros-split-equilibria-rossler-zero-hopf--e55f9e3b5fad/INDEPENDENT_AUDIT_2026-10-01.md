# Independent mathematical audit — 2026-10-01

## Final claim assessed

Boundary averaged zeros shadow split equilibria in the classical Rössler zero-Hopf unfolding

## Correctness — PASS

PASS. The exact equilibrium quadratic, source coordinate map, and characteristic polynomial were reconstructed. The split branches have \(u=v=0\) exactly and their scaled \(W\)-coordinates tend to the two zero-radius averaged roots with the opposite branch sign. Fresh algebra also agrees with the first-order spectral drift and with the inspected symbolic artifact. This proves equilibrium shadowing and the first-order spectrum comparison; it does not prove nonexistence of smaller-amplitude cycles.

## Originality — FAIL

FAIL. A published 18 September 2026 finding predates this package and already proves the same central correction: the two zero-radius averaged roots are blown-up limits of the exact split equilibria, the polar/angular chart is singular there, and the cited first-order averaging argument does not certify two extra periodic families. The added first-order spectral matching is a routine linearization of those already-identified branches and does not make the packaged final claim original.

### equivalent_formulations

Searches: Resultary query for Rössler zero-Hopf boundary roots and split equilibria; https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-boundary-polar-zeros-track-rossler-equilibria--6ecaba26fef5

Evidence: The complete 18 September result proves exact split equilibria, exact zero-radius placement, convergence to the boundary roots, and the polar-chart singularity.

Reasoning: The earlier record states the same correction in an equivalent polar-blow-up formulation.

### broader_coverage

Searches: arXiv:2609.17336v1; 18 September published correction

Evidence: The primary source advertises three first-order periodic families; the earlier correction already isolates two roots as equilibrium limits.

Reasoning: The earlier correction dominates the main source-specific conclusion.

### exact_database_or_table

Searches: Published-record semantic search for the exact Rössler correction

Evidence: The 18 September result is the nearest exact prior and predates the audited record.

Reasoning: This is theorem-level prior coverage, not a numerical table question.

### claim_vs_prior_implication

Searches: Complete 18 September RESULT.md; arXiv:2609.17336v1 indexed statement

Evidence: The earlier result directly proves the equilibrium-shadowing obstruction; the later spectral comparison is a straightforward Jacobian expansion.

Reasoning: The final packaged claim is covered under the implication standard.

## Scientific value — PASS

PASS. The correction is scientifically worthwhile because it changes the interpretation of two of the three advertised bifurcating families while leaving the positive-radius family untouched. The rejection is originality, not usefulness.

## Source inspections

- **Boundary polar zeros track equilibria in a Rössler zero-Hopf unfolding** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-boundary-polar-zeros-track-rossler-equilibria--6ecaba26fef5. Material read: Complete published RESULT.md. Assessment: DECISIVE_PRIOR_COVERAGE. Evidence: It proves the same equilibrium-shadowing and polar-chart obstruction two days earlier.
- **Zero-Hopf bifurcation, periodic orbits and C1 non-integrability of the classical Rössler system** — https://arxiv.org/abs/2609.17336v1. Material read: Primary abstract and indexed statement material. Assessment: MOTIVATING_SOURCE. Evidence: It states that first-order averaging produces three distinct periodic-orbit families.

## Limitations and residual risks

The result identifies the two zero-radius averaged roots with split equilibria and limits what first-order polar averaging certifies. It does not exclude smaller-amplitude periodic orbits established by other methods.

- No access risk changes the decisive originality failure.
- The audit does not assert nonexistence of smaller-amplitude periodic orbits.

## Disposition

**failed**
