# Scientific review — critical risk-averse opinion and SIS clearance

## Correctness — PASS

The claim is quantified for every initially infected, strictly risk-averse state of the displayed NOD–SIS vector field with \(u_0=1\), \(\bar\beta=\delta\in(0,1)\), \(0<k_p<1\), \(0\le k_x<1/3\), and \(\tau_x>0\). Positivity and the comparison \(\dot p\le-\beta p^2\) first establish extinction of infection. The scalar zero-infection opinion solution is a lower bound on the risk-aversion magnitude, yielding an integrable stretched-exponential upper bound for infection. Uniform negativity of its limiting opinion vector field forces opinion magnitude to zero. The exact cubic and fifth-order tanh coefficients then give the reciprocal-square expansion with a finite remainder: \(1/x(t)^2=(2c/\tau_x)t-(d/c)\log t+K+o(1)\). Because the correction in opinion is integrable against time, the infection logarithmic equation has a finite limiting intercept and a strictly positive stretched-exponential prefactor. The neutral-opinion \(1/t\) comparison is an exact invariant equation. The packaged `verify.py` checked Taylor coefficients and the rational example; its numerical checks are supplementary only.

Limits: global convergence is proved only inside the strict negative-opinion sector, not for positive initial opinion or a networked generalization. No finite simulation substitutes for the infinite-time proof.

## Originality — PASS on the inspected record

The principal initiating source, Ordorica Arango et al., arXiv:2410.12993, equations (2)–(3), was compared at full-text level. Its main results impose \(u_0<1\), identify steady-state and bifurcation regimes, and do not state the joint-critical \(u_0=1\), \(\bar\beta=\delta\) asymptotic law. The pre-existing nonlinear opinion framework by Bizyaeva, Franci and Leonard proves pitchfork behavior but does not address epidemic coupling or stretched-exponential prevalence. The actSIS network study has a distinct feedback system; only an abstract-level comparison was accessible, which is a residual priority risk.

Indexed closest comparisons include a nonlinear SIRS pitchfork-edge result giving *algebraic infection* decay, a multiple-exposure epidemic double-degeneracy result also giving algebraic infection decay, and an epidemic noncompliance threshold giving algebraic behavior but exponentially declining infection. Their stated vector fields and consequences neither imply the present infection law nor cover its model-specific signed logarithmic opinion correction. The originating paper's general risk-aversion mechanism, the scalar pitchfork exponent, and the ordinary SIS critical \(1/t\) law are acknowledged as prior facts, not claimed as discoveries. Search and access are not proofs of novelty; unindexed or inaccessible equivalent works may exist.

## Value — PASS

The exact epidemiological invasion threshold alone predicts an algebraic SIS decay, but the coupled critical opinion feedback instead yields \(\exp(-C\sqrt t)\) prevalence with a positive asymptotic prefactor for the entire strictly risk-averse sector. This is a structurally motivated, measurable change in the extinction class, not a numerical coefficient tweak. The sign reversal of the \(\log t\) correction at \(k_x=2/15\) distinguishes two relaxation patterns within the weak-peer-pressure regime. These quantitative consequences inform analysis of risk perception at a transmission threshold, though they are deterministic asymptotics rather than finite-population extinction predictions.

Self-review: passed. Independent audit: not yet performed.
