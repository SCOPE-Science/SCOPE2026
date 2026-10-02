# Independent mathematical audit — SCOPE-20260912-080

Disposition: **failed**.

## Correctness
**PASS** — The exact constant-force velocity-Verlet identity is correct by direct expansion. I independently reimplemented the stated Cartesian constraints, Newton position projection and tangent momentum projection from the formulas rather than executing repository code. The anchor energy reproduced exactly to displayed precision, and the 10-unit integrations gave dH=-8.04195789037082 at h=0.01 and dH=-5.168375867946267 at h=0.005, agreeing with the archived values to floating-point roundoff. The current public claim correctly withdraws the former continuum-quantified theorem.

## Originality
**PASS** — Targeted Resultary and web searches did not locate the exact archived double-pendulum anchor benchmark or these numerical drift values. The exact constant-force Verlet identity is elementary background, so originality, if any, is confined to the reproducible implementation-specific benchmark rather than the identity.

### Equivalent formulations
The finite claim is a reproducible numerical observation for one implementation and finite sample.

### Broader coverage
General theory does not determine the exact archived floating-point drift numbers.

### Exact database or table search
The archived table is the exact data object; absence elsewhere is not treated as a novelty proof.

### Claim versus prior implication
The benchmark numbers require the implementation and numerical integration.

## Value
**FAIL** — After withdrawal of the uniform all-step/all-neighborhood theorem, the surviving scientific content is an elementary constant-force identity plus two anchor runs and five random perturbations from one floating-point implementation. These finite implementation-specific numbers do not establish a structural boundary, validated error law, sharp cutoff, classification, or motivated exact invariant. Reproducibility and apparent originality of the numbers are insufficient to pass the value bar.

## Source inspections
- **Stored Cartesian double-pendulum benchmark artifacts** (record artifacts/core.py and table_anchor.json at inventory commit): full core implementation, run script, exact archived table and exact-flow comparison script Assessment: The two anchor drifts reproduce to floating-point roundoff; the finite data are correct as observations. Evidence: Independent values: -8.04195789037082 at h=0.01 and -5.168375867946267 at h=0.005.
- **Resultary semantic search** (Resultary local research index): top hits for projected-Verlet double-pendulum projection energy drift Assessment: The exact benchmark record was the only direct hit. Evidence: No stronger SCOPE theorem covering these exact archived observations was returned.
- **General constrained geometric-integration background cited in the record** (standard SHAKE/RATTLE and backward-error literature): record's stated background references and search-result context Assessment: Standard theory motivates projection and near-conservation questions but does not make the specific archived finite drift values scientifically substantial by itself. Evidence: The surviving exact identity is a direct algebraic expansion for constant force.

## Residual risks
- The reproduced drifts remain ordinary double-precision observations, not validated numerical enclosures.
- No universal error law, sign theorem, or open-neighborhood statement survives the corrected record; this is the basis for V=FAIL.
