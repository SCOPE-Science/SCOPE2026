# Scientific review

## Correctness: PASS

The normalized source mean-field Equations (1)–(3) reduce exactly at the stated tricritical probabilities to the positive two-dimensional system in `RESULT.md` Equation (1). The ratio equation is algebraically exact. A transverse strictly downward crossing of the threshold ratio yields the full one-peak classification. Bounded comparison and stable linear forcing prove global infection clearance and ratio convergence. Successive stable-filter estimates produce the cubic and quartic infection drift; reciprocal-square integration proves both universal coefficients and the stated \(O(t^{-3/2}\log t)\) remainder. The symbolic verifier independently checks the polynomial identities and exact fractions; numerical trajectories support but do not establish infinite-time quantifiers. Risk: all asymptotic statements are pointwise in the initial state and restricted to the exact mean-field model.

## Originality: PASS (inspected sources, subject to publication-priority uncertainty)

Pires et al., arXiv:2306.08135, Sections II.1 and III already obtain the tricritical parameters and the expected exponent \(1/2\), including a numerical estimate \(0.509\pm0.013\). Their accessible complete article does not give a global one-peak classification or an explicit universal second asymptotic coefficient for the infection trajectory. Lübeck's arXiv:cond-mat/0608339, Section 2, Eq. (15), treats a scalar cubic tricritical normal form and gives the established leading exponent, but no coupled vaccination ratio, no nonzero \(t^{-1}\) coefficient for the published vaccination equations, and no infection-peak criterion. The nearest published comparisons found in public research summaries address distinct multiple-exposure and nonlinear SIRS equations, and do not imply this formula or classification. Keyword, alias, analytic-asymptotics and source-ID searches found no decisive equivalent claim. Risk: semantic searches and public summaries cannot guarantee absence of a stronger unindexed work.

## Value: PASS

The initiating study establishes tricritical behavior and estimates a critical decay exponent, but that information leaves finite-time clearance coefficients and infection-trajectory shape undetermined. The sharp \(t^{-1}\) correction quantifies the leading impact of the finite-time susceptible-vaccinated adjustment, is independent of the initial infected share, and differs from the zero \(t^{-1}\) term of the standard scalar cubic normal form. The exact initial ratio cutoff distinguishes transient outbreak growth from monotone decline over the entire biologically admissible simplex. These are motivated model-specific quantitative questions, not merely renamed exponent estimates. No global stochastic, lattice, or noncritical claim is inferred.

## Closest literature and residual limits

1. Pires et al., *Tricritical behavior in epidemic dynamics with vaccination*, https://arxiv.org/abs/2306.08135, first public 2023-06-13. Full source Sections II–IV examined. Owns original equations, tricritical parameters, and known decay exponent.
2. S. Lübeck, *Tricritical directed percolation*, https://arxiv.org/abs/cond-mat/0608339, Section 2, especially Eqs. (1) and (15). Full accessible article examined; scalar comparison, not coupled epidemic system.
3. *Global attraction and two-term critical relaxation at the multiple-exposure disease-free degeneracy*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-global-attraction-and-two-term-critical-relaxation-at-the-multip--45a437e4957f. Published summary examined, full paper not retrievable; dynamics described as Li–Ma multiple-exposure rather than vaccination MVE.
4. *Universal extinction crossover at the pitchfork edge of a nonlinear SIRS model*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-extinction-crossover-at-the-pitchfork-edge-of-a-nonlin--c1921b9ff104. Published summary examined; distinct nonlinear SIRS dynamics.

Self-review: passed. Independent audit: not yet performed.
