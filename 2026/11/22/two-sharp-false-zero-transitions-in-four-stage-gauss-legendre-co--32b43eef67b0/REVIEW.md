# Scientific review

## Correctness

**PASS.** The claimed normalized collocation polynomial is reconstructed from its initial value and an exact shifted-Legendre residual. Its endpoint numerator is an explicit sum of positive squares and a positive constant. A degree-six discriminant factor and exact Sturm variation counts certify two and only two positive interior-root collision parameters. Exact root counts at three rational parameter values and the exclusion of triple zeros give the full sign diagram by continuity; algebraic evaluations at the collocation nodes identify the two collision locations. The same standalone verifier checks each critical identity from its packaged source. Computations supplement rather than replace the quantified analytic argument.

## Originality

**PASS, subject to historical-priority uncertainty.** The closest primary source is Falini–Mazzia–Sestini (2023 online/2024 journal), which describes collocation dense output and develops different spline quasi-interpolants; its Gauss Section 5.2 treats two and three stages and does not derive the four-stage scalar-decay positivity or false-event root-count diagram. Ketcheson–Lóczi–Jangabylova–Kusmanov (2016) treats strong-stability-preserving dense output under broader invariant-domain requirements rather than this fixed implicit Gauss polynomial. Published scalar cubic-Hermite event-root and two-stage Gauss Markov internal-stage positivity claims concern different polynomials and imply neither of the two certified four-stage thresholds. The Padé endpoint formula alone does not determine intermediate signs. Accessible public summaries of some related published records did not permit a complete full-text exclusion, and an equivalent derivation outside the inspected corpus cannot be ruled out.

## Value

**PASS.** Event detection and continuous visualization use values *inside* accepted numerical time steps, rather than solely at the endpoints. Two exact spurious-event bifurcations in a standard fourth-order collocation polynomial—one pair appearing, then a second—identify a concrete qualitative failure of endpoint positivity under stiffness. The all-positive-node criterion derived from the integrating-factor residual is a convenient and structural check for scalar decay collocation at any stage count. The result is not framed as a general nonlinear positivity theorem or an incremental rounded constant.

## Closest literature and limitations

- Falini, Mazzia, Sestini (2023 online), DOI: https://doi.org/10.1016/j.apnum.2023.07.023 — Section 5.2 inspected in full public text; different quasi-interpolants and stages.
- Ketcheson, Lóczi, Jangabylova, Kusmanov (2016), https://arxiv.org/abs/1605.02429 — full HTML article inspected; its SSP restrictions do not subsume scalar Gauss collocation.
- Nüßlein, Ranocha, Ketcheson (2020), https://arxiv.org/abs/2005.06268 — abstract/overview inspected; adaptive RK weights and not the natural fixed-polynomial thresholds.

The proof only covers scalar decay, one collocation step and exact polynomial arithmetic. Related full texts restricted to search summaries and incomplete source access leave a finite historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
