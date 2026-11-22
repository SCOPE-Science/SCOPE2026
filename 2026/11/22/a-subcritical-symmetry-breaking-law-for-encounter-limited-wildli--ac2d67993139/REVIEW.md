# Scientific review: encounter-limited passage allocations

## Correctness — PASS

For each passage, a zero-event Poisson probability gives the exactly specified throughput \(x_i e^{-cx_i}\). Compactness guarantees a maximizer; a positive first-order perturbation excludes zeros. The derivative \(f_c'\) has at most two preimages and a pair of entries above \(2/c\) violates the second-order maximum condition, reducing the global search to one exceptional passage. For two passages, a hyperbolic-tangent equation has a unique nonzero root exactly when \(c>4\). For \(n\ge3\), a positive cubic tangent direction at \(c=2n\), together with negative-definite Hessian immediately below \(2n\), proves strict coexistence of an inferior balanced local maximum and a superior asymmetric allocation. The strict \(n=3,c=59/10\) witness is certified by exact rational alternating Taylor bounds. A one-large-component upper bound and a matching construction prove the high-load limit and the entire optimizing profile. The bundled standard-library checker passed 21,082 supplementary finite checks. The randomized grid comparisons are not used as infinite proofs.

## Originality — PASS on inspected evidence, with provisional historical priority

The closest ecological sources are Soanes et al. (2024), which reviews empirical crossing effectiveness, Mata et al. (2020), which documents predator–prey encounter associations at wildlife crossings, and Helldin (2022), whose full text develops distributed-versus-concentrated crossing design through ecological arguments, and Karlson et al. (2017), whose abstract and the account in Helldin (2022) describe GIS/circuit-connectivity analyses. Those sources do not themselves state or imply the exact exponential traffic-allocation theorem. Andersson and Ygge (2001) and Wagner and Stone (1974) provide general prior nonconcave-allocation and coverability contexts; their accessible material does not supply the sharp two-versus-at-least-three local/global bifurcation or the limiting one-heavy, many-light optimizer profile. Conceptually adjacent published mathematical results concern exclusion current, logistic/Holling-II predation and a habitat-adjacency eigenvalue, with noninterchangeable objectives. This is a statement-level comparison and not an inference from unmatched titles. The literature search cannot prove uniqueness in all historical optimization theory; uninspected general mathematics and abstract-only generic optimization articles remain a documented risk.

## Value — PASS

The result pinpoints a design-relevant pitfall of equal utilization: with at least three crossings a balanced allocation can be stable against small reallocations yet inferior overall, whereas the two-crossing bifurcation cannot exhibit this local/global coexistence. It also gives a sharp, nonobvious large-encounter-load profile and an exact rational illustrative witness. The objective is explicitly an idealized expected fraction of successful crossing attempts; it is not empirical evidence that concentrating wildlife at one crossing would be beneficial, nor a field-calibrated management rule.

## Closest literature and limitations

- Soanes et al. (2024), DOI: https://doi.org/10.1111/1365-2664.14582 — full open-access review, including methodology and discussion.
- Mata, Herranz and Malo (2020), DOI: https://doi.org/10.3390/d12040166 — full open-access study, including methods and discussion.
- Helldin (2022), DOI: https://doi.org/10.3897/natureconservation.47.67979 — complete open-access paper read, including the modeling discussion and management implications.
- Karlson, Seiler and Mörtberg (2017), DOI: https://doi.org/10.1016/j.ecoleng.2017.04.059 — accessible abstract; spatial circuit-connectivity objective differs from the smooth Poisson-throughput objective.
- Andersson and Ygge (2001), DOI: https://doi.org/10.1023/A:1011263102622 — bibliographic abstract inspected, not a full-text noncoverage judgment.
- Wagner and Stone (1974), DOI: https://doi.org/10.1137/0312029 — abstract inspected; possible general reduction remains a historical-priority risk.

The Poisson-load model excludes animal routing behavior, capacity limits, species heterogeneity and dynamics. Its scale parameter has not been measured. For \(n\ge3\) no exact lowest global phase-transition threshold or global-optimum uniqueness is asserted. Formal independent validation and field testing are absent.

Self-review: passed. Independent audit: not yet performed.
