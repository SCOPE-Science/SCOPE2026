# Independent scientific audit — 2026-10-01

**Disposition: FAILED — not a validated finding.**

## Final claim assessed

For the specified dense two-population QIF/MPR model with fixed total heterogeneity, redistributing heterogeneity toward E produces a unique physical fixed-point branch that crosses a stable gamma limit cycle at rho_c=2.54534 and about 34.58 Hz, with E leading I and a matching finite-spiking gamma state.

## Correctness — FAIL

The central local Hopf computation is reproducible: independently solving the filed fixed-point equations gives the stated branch values at rho=1,2,2.545339,3,4 and the critical eigenvalue approximately +0.217293 i/ms (34.5833 Hz); a fresh RK4 replay at rho=4 reproduces means 60.217/32.497 Hz, amplitudes 39.302/53.901 Hz, frequency 36.6667 Hz and phase -1.2902 rad. However, the final claim is stronger: uniqueness of the physical branch over the full continuum [0.1,10] is supported only by finitely many Newton starts/probed points, and asymptotic stability of the limit cycle is inferred from persistent integration without Floquet or an equivalent basin/stability certificate. Those methods do not prove the stated global uniqueness/stability assertions.

## Originality — PASS

The exact fixed-budget heterogeneity-ratio threshold and parameter tuple were not found in Resultary or the inspected primary MPR literature. The general MPR reduction and QIF bifurcation framework are established, but the stated numeric threshold requires a separate computation. Best-of-knowledge exact-instance originality therefore passes, subject to normal search limitations.

## Scientific value — FAIL

The source tree shows that the final parameter vector was selected after scanning a grid of JEI, JIE, etaE and etaI candidates for the desired baseline/Hopf behavior. The exact rho threshold is therefore a post-selected parameter slice without an independent argument that this tuple, fixed-sum path, or threshold is a natural classification boundary or broadly needed invariant. It is useful exploratory modeling, but not a sufficiently motivated mathematical gap under the shared value standard.

## Originality checks

### equivalent_formulations

The record is a parameter-specific bifurcation computation within the established exact MPR system; no equivalent exact threshold formulation was located.

Evidence: Resultary returned this record itself as the exact threshold match.; Montbrio-Pazo-Roxin arXiv:1506.06581 gives the exact macroscopic QIF equations.

### broader_coverage

The general model is prior; the numeric instance is not mechanically given by the general theorem.

Evidence: MPR provides the broad exact neural-mass framework and supports systematic bifurcation analysis, but does not imply this chosen threshold without computation.

### exact_database_or_table

The exact number is best-of-knowledge new, but exact-instance novelty is insufficient for value.

Evidence: No distinct exact table or database row beyond the record under audit was returned.

### claim_vs_prior_implication

A numerical continuation/eigenvalue solve is required, so the exact threshold is not a direct prior corollary.

Evidence: The primary paper derives the exact low-dimensional equations but does not state the scanned parameter point or rho_c.

## Sources inspected

- Macroscopic description for networks of spiking neurons — https://arxiv.org/abs/1506.06581: general model coverage, not exact parameter threshold
- Assigned package 2026/09/12/053 — https://github.com/SCOPE-Science/SCOPE2026/tree/92c7f26b45ce94be6cda0eafed44298c598d7b47/2026/09/12/053: local Hopf/cycle numerics reproduce, but global uniqueness/stability are under-certified and parameter choice is scan-selected

## Residual risks

- A broader neuroscience search might contain a closely related heterogeneity-ratio scan, but no exact parameter/path threshold was found.
- The finite N=7500 spiking simulation was not rerun; additionally, one-seed finite simulation cannot establish general finite-size robustness.
