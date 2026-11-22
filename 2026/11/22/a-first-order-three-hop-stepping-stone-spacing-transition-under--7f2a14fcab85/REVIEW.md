# Scientific review

## Correctness — PASS

The feasible three-gap simplex is compact. At a face with a zero gap, the first variation toward the interior strictly reduces the logarithmic denominator. All interior critical points have either equal gaps or reciprocal gap values; the only possible asymmetric global minimum consists of two equal short gaps and one reciprocal long gap. A tangent Hessian test eliminates the other stationary branch. The derivative of the log-cost difference between equal and stable asymmetric branches is strictly negative on \((2\sqrt2,3)\), with exact opposite signs at the endpoints, proving one and only one global switch. The direct two-gap denominator identity proves the claimed minimality of a three-hop discontinuity. Supplementary reproducibility: 76,359 assertions by `verify.py`. Risk: the transition only concerns a fixed three-hop independent success model, not actual dispersal success measured over many generations.

## Originality — PASS on inspected evidence

Lapin et al. (2024) provide a forest stepping-stone prioritization framework, not this continuous three-gap optimal-spacing theorem. Saura, Bodin and Fortin (2014; available online 2013) already develop maximum-product stepping-stone connectivity ideas; those ideas are credited as existing work, while their inspected mathematical analysis does not classify the present exact reciprocal-gap transition. Chapman et al. (2007; available online 2006) and Skelsey et al. (2013; available online 2012) study dispersal kernels or landscape patterns, with different optimization variables. Direct searches for the reciprocal-gap threshold, related constrained-product inequality, and comparable route designs did not identify a mathematically stronger covering theorem. The special two-hop case is explicitly contrasted rather than recycled. Residual risk: general mathematical inequalities in older literature may yield the same formula; search and inspected evidence do not certify universal first discovery.

## Value — PASS

The result is a complete global classification, with exact ties and a first-order transition despite persistent local stability, of a minimal continuous conservation-connectivity placement model. It clarifies when a uniform-spacing heuristic is globally incorrect and how network movement kernels can favor a widely spaced route segment rather than uniform links; this provides a self-contained analytic benchmark for richer spatial restoration models. Its value is the structural threshold and shortest-chain boundary, not a claim to predict an actual field placement.

## Closest sources and limits

- Lapin et al. (2024), https://doi.org/10.1111/csp2.13161 — full article methods and results inspected; regional multi-indicator conservation prioritization, not exact optimized three-hop spacing.
- Saura, Bodin and Fortin (2014), https://doi.org/10.1111/1365-2664.12179 — full article mathematical connectivity and implications inspected; maximum product of dispersal probabilities is prior work; no corresponding inverse-quadratic gap optimization identified.
- Chapman, Dytham and Oxford (2007), https://doi.org/10.1111/j.1365-2656.2006.01172.x — full article methods inspected; fitted dispersal kernels and emigration probabilities rather than free location optimization.
- Skelsey, With and Garrett (2013), https://doi.org/10.1007/s12080-012-0171-3 — full accessible article text inspected; scale of heterogeneity and other model objectives.
- General abstract-level related source: da Rocha et al. (2021), https://doi.org/10.1007/s10980-021-01310-x; not used for decisive negative coverage.

Self-review: passed. Independent audit: not yet performed.
