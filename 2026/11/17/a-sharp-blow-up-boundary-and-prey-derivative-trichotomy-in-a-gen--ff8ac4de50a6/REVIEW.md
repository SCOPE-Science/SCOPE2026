# Scientific review

## Correctness

**PASS.** Logistic comparison bounds prey. For \(E\geq AD\), the function \(h(x)=2\int_0^x g_+(u)/q(u)\,du\) is finite at zero and \(\log y+h(x)\) cannot increase when \(y\) is above a fixed state-independent-in-time threshold; each excursion gives the explicit uniform bound in `RESULT.md`. For \(E<AD\), \(g(x)\geq D-E/A>0\) forces finite-time Riccati blow-up. The reciprocal-predator identity first supplies a positive power upper bound for prey, then a precise predator pole; an integrable error in the prey logarithmic derivative yields a finite strictly positive asymptotic amplitude. The derivative trichotomy follows without finite-experiment extrapolation. Exact algebraic and numerical replay is provided. The isolated finite-time singularity and all parameter boundaries were checked directly.

## Originality

**PASS within inspected evidence, with residual publication-priority uncertainty.** The 2021 original model article gives conditional boundedness and stability results, not this all-positive-data parameter dichotomy. The 2023 follow-on analyzes blow-up and claimed concurrent derivative quenching but does not establish the parameter-wide *converse* global bound or the exponent threshold. The 2024 Patra–Maitra–Kundu article proves the sufficient \(D>E/A\) blow-up side, which is explicitly credited and excluded from the novelty claim. Relevant indexed mathematical results on other Leslie–Gower and quadratic predator systems have different vector fields, invasion thresholds, or extinction regimes. The 2024 journal source was only accessible in material excerpts, so equivalence elsewhere remains a risk.

## Value

**PASS.** The sharp \(D=E/A\) boundary resolves whether the printed mathematical flow can actually explode, a central question raised by the originating papers. The global boundedness statement resolves the full complementary parameter half, not just a local stability neighborhood. On the blowing-up half, the exact exponent \(\nu=M/[C(D-E/A)]\) yields a three-regime classification of the prey derivative and separates exploding derivatives from bounded or vanishing derivatives at predator blow-up. This directly tests the interpretation of reported simultaneous blow-up and quenching, and has concrete parameter-level implications without a special rational slice.

## Closest literature and limitations

- Patra, Kundu and Maitra (arXiv:2104.09166; 2021), original model and conditional boundedness.
- Srivastava, Antwi-Fordjour and Parshad (arXiv:2306.13666; 2023), blow-up and quenching analysis in the same printed ODE.
- Patra, Maitra and Kundu (*Journal of Biological Systems* 2024, DOI:10.1142/S0218339024500165), sufficient blow-up condition \(D>E/A\), not a converse or exact power profile in the inspected section.

Unindexed equivalent results and incompletely accessible 2024 full-text material remain novelty risks. The theorem is restricted to the undelayed ODE, positive coefficients and initial populations, and \(p\geq1\); it does not describe delayed or spatial variants. Numerical tests do not constitute an infinite proof.

Self-review: passed. Independent audit: not yet performed.
