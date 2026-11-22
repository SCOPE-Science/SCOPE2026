# Scientific review

## Correctness — PASS

The claimed domain and boundary cases were reconstructed for the exact published count law. The tail-sum identity \(m_u=\sum_{k\ge1}S(x+k)/S(x)\) follows from conditioning on \(Y\ge u\), and \(S(x)\asymp x^{-p}\) proves the finite-mean cutoff exactly. Summable Taylor remainders and a four-term Euler–Maclaurin formula prove the two-power expansion, including explicit dependence on \(\kappa\), and show the complete fixed-parameter sign classification. At \(p=2\) the second carrier term and next Bernoulli correction prove the cubic coefficient; its equality substitution is strictly negative whenever the cancelling parameter is admissible. High-precision independent evaluations of the exact Hurwitz-zeta expression, after extraction from the package, agree with the signs and coefficients. Numerical checks alone do not prove an infinite theorem; the analytic remainder proof supplies that step.

## Originality — PASS (qualified)

The defining DEGPD/ZIDEGPD probability laws, classical mean-excess diagnostic, GPD threshold closure, half-step continuity correction and continuous EGPD penultimate expansions are previous results, not rediscoveries. The inspected full 2022 origin, 2024 extension, 2017 discrete-extremes, 2011 extended-GPD and 2023 discrete-tail-inference papers do not state or imply the combined power-DEGPD conditional-mean expansion or the scale-dependent unique cancellation curve. Closest discovered other results concern unrelated lifetime models, extreme-value estimators or moment existence. Lack of a covering search hit is not proof of priority; unindexed/disconnected literature remains a residual risk.

## Value — PASS

Mean residual life plots are explicitly used in discrete extreme-value threshold selection. The theorem gives the order and sign of the otherwise hidden deterministic curvature bias after the universal half-unit correction, distinguishes finite-variance and infinite-variance finite-mean regimes at \(\xi=1/2\), and identifies a nontrivial admissible carrier curve on which apparent linearity is unusually accurate but not exact. These are natural model-specific questions and explain why a visually linear mean-excess plot may misrepresent carrier effects. The precise \(u^{-3}\) residual distinguishes true cancellation from a rounding coincidence.

## Limits and closest literature

The fixed-parameter result does not give empirical confidence intervals, uniform-in-shape rates or independent certification. Primary antecedents: Ahmad–Gaetan–Naveau (2022), Ahmad–Arshad (2024), Hitz–Davis–Samorodnitsky (2017), Papastathopoulos–Tawn (2011), and Daouia–Stupfler–Usseglio-Carleve (2023). The link between their particular statements and this theorem is explained in RESULT.md and AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
