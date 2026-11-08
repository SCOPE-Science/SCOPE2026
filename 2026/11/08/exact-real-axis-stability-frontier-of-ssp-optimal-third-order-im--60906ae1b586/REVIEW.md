# Review of the exact SSP-SDIRK3 scalar stability frontier

## Correctness
**PASS (self-review).** The stated family is exactly the coefficient family of Weng, Yu, and Zhu (Theorem 5.2, equations (5.5)–(5.6)). The triangular stage equations reduce the RK stability function to one Möbius factor raised to the stage count. Its monotone image of the negative real axis is precisely the interval \((-q_s,1]\). Even and odd powers produce separate necessary-and-sufficient absolute-stability tests, including endpoint signs, positivity of all threshold denominators, and the strict instability beyond each endpoint. The large-stage limits follow from \(s\operatorname{artanh}(1/s)\to1\). The attached checker was executed from the prepared files and reported `VERIFY_OK 864`. Finite numerics support but do not replace the analytic universal proof.

## Originality
**PASS (qualified, self-review).** The 2026 source establishes the SSP-optimal tableau and its uniqueness, not its complete real-negative-axis stability frontier. Ferracina–Spijker (2007) conjectured optimality of the same coefficient family; the 2008 Ketcheson–Macdonald–Gottlieb manuscript analyzes generic RK stability and SSP optimization but supplies no equivalent exact all-stage scalar-decay classification in the inspected sections. Fekete–Horváth (2019) displays the four-stage absolute-stability domain numerically, an important partial antecedent, but does not determine an all-stage parity formula or the alternating \(\pm e\) stiff limit. Targeted published-literature and mathematical-record searches found no covering statement. Search failure is not a proof of novelty; unindexed classic stability calculations remain a residual priority risk.

## Value
**PASS (self-review).** The negative-real-axis stability interval is a natural, decision-relevant invariant when an implicit SSP scheme is applied to diffusion and stiff scalar relaxation. This calculation determines a *sharp* admissible spectral step length for every stage count, reveals that it grows as \(4s^2\), and identifies a contrasting large-stiffness amplification whose magnitude approaches \(e\), with sign governed by stage parity. It therefore exposes a genuine SSP-versus-linear-stability trade-off that the SSP-radius optimality theorem alone does not quantify. The result is deliberately limited to scalar/normal negative-real spectra; it does not establish full A-stability, SSP beyond the SSP radius, or nonlinear long-time behavior.

## Sources and residual risks
Primary comparisons: Weng–Yu–Zhu, arXiv:2610.37425v1, §5; Ferracina–Spijker, Leiden report 2007-11, §3.3; Ketcheson–Macdonald–Gottlieb, 2008 postprint, §§2–3; Fekete–Horváth, 2019, §2.2 and Fig. 2. Historical priority is subject to independent verification, especially for analytic stability-functions derived implicitly from classical SDIRK coefficients.

Self-review: passed. Independent audit: not yet performed.
