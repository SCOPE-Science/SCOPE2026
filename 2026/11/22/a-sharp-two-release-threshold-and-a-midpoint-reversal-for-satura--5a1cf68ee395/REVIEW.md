# Scientific review: finite-horizon two-release mating-pressure threshold

## Correctness — PASS

For positive initial and second release sizes, constant wild competition, positive mortality, and any positive horizon, the piecewise exponential input integrates exactly to the displayed logarithm. Differentiation reduces global optimality on a compact interval to the sign of a quadratic that is strictly increasing throughout the permissible variable interval. The quadratic has either no interior zero or exactly one with a global increase-then-decrease sign pattern, so it establishes a unique global optimizer rather than only a necessary condition. Implicit differentiation checks monotonicity and the strict derivative bounds. A direct midpoint sign comparison proves the second threshold and its strict equality cases; the infinite-horizon expansion uses a positive root asymptotic. All limits, both endpoints and all positivity assumptions are explicit. Supplementary checker: 187,417 deterministic assertions passed, including independent piecewise quadrature and numerical global scans. The universal proof is analytic, not based on sampled cases.

## Originality — PASS on inspected evidence

The closest application literature is Almeida et al., arXiv:2307.11614 (first public July 21, 2023), later published in 2024. Their pulse design minimizes infected human burden in a coupled dynamic model, and their pulse times and sizes are optimized numerically; it neither states nor implies the exact optimal delay for a pinned-first, fixed-unequal-dose integral saturating-mating proxy. Almeida et al., arXiv:2011.04449 (2020, later 2022), instead optimize population-state control objectives. Ramirez and Gordillo (2016) search over pulse sizes for different control and economic outcomes. Wright et al. (2011) document generic Emax scheduling dependence, which supplies the key cross-domain analogy but not the claimed sharp finite-horizon and midpoint theorems. The explicit noncoverage comparison concerns their actual mathematical objectives, not different titles. Other general impulse-control or pharmacodynamic results may subsume this benchmark and historical priority is not conclusively verified. A related 2021 paper by Huang et al. was available only in synopsis due to access failure; its dynamic population objective differs from the specific proxy, but the residual risk is recorded.

## Value — PASS

The exact boundary between simultaneous and staggered action, and a second threshold at which the optimal delay crosses the often-assumed horizon midpoint, distinguish model regimes that generic "spread pulses" heuristics do not resolve. The result is a fully classified, measurable idealized mechanism for sterile-male competition over a finite window and a benchmark for testing more realistic pest-intervention optimizers. Unequal doses are essential: equal doses cannot produce the second reversal. The contribution is not claimed to predict population extinction or clinical outcomes, and the constant-wild-pool proxy and pinned first pulse are important limitations.

## Closest literature and limitations

- Almeida et al., *Vector-borne disease outbreak control via instant releases*, arXiv:2307.11614, https://doi.org/10.1007/s00285-024-02159-9: impulsive releases, coupled epidemic outcome, numerical pulse optimization.
- Almeida et al., *Optimal control strategies for the sterile mosquitoes technique*, arXiv:2011.04449, https://doi.org/10.1016/j.jde.2021.12.002: state-dependent population control rather than integrated fixed-competition mating pressure.
- Ramirez and Gordillo, https://doi.org/10.1155/2016/8492107: pulsed releases and stochastic cost optimization.
- Wright et al., https://doi.org/10.1111/j.1365-2125.2011.03925.x: nonlinear dose–response schedule dependence, but no exact claimed threshold.
- Huang et al., https://doi.org/10.1080/17513758.2021.1887380: related population release work, abstract-level access only.

Only the stated idealized cumulative competition proxy is optimized. The demonstration is an analytic global theorem plus supplementary finite checks; no field data or independent specialist audit is asserted.

Self-review: passed. Independent audit: not yet performed.
