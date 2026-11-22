# Scientific assessment: finite-height tetration critical crossover

## Correctness

**PASS.** The exact two-step conjugacy uses \(g_t(z)=te^{-z}\) and its fixed point \(W(t)\). The cubic Taylor coefficients are derived from that exact identity, rather than estimated from a finite orbit. At the neutral point \(T_1(-v)>-v\) follows strictly from \(-\log(1-v)>e^v-1\) for \(0<v<1\); this gives parameter-uniform entry into the Taylor neighborhood. The reciprocal-square recursion has drift \(1/3\) and multiplier \(1-2a/k\), and its remainder has vanishing averaged size once \(r_j=O(k)\) is established. This proves a positive, locally uniform Riemann-sum limit for \(r_k/k\). The equilibrium two-cycle is checked independently through Euler's exact \(q=s/\sinh s\) parametrization, with \(\log(t/e)=s^2/6+O(s^4)\). The boundary cases \(a<0\), \(a=0\), and \(a>0\) are separately accounted for; no finite diagnostics are presented as an infinite proof. The `verify.py` script passed 279 finite diagnostics when executed from its package directory.

## Originality

**PASS on checked evidence, with historical-priority risk.** The source arXiv:2611.03895v1 (Sections 2, 4.1 and 4.2) defines and proves convergence of the odd-height distribution, and gives only the qualitative algebraic critical approach and a numerical equilibrium cusp coefficient, not the explicit joint finite-height \(1/k\)-detuning profile. Corless–Jeffrey–Joby (2023), including its appendix and Karamata expansions, treats static real/complex two-cycles; the present crossover depends on a finite number \(k\) of iterations and a parameter moving with \(k\). Toledo (2022) studies fixed-base convergence and initial conditions, not such a joint limit. Related cubic-flip finite-time crossovers in different dynamical models explain why the form is plausible but do not imply the tetration CDF formula without computing and controlling its actual normalization and initial orbit. The new conclusion does not claim the known fixed-parameter square-root cusp alone.

## Mathematical value

**PASS.** The result quantifies the singular finite-size behavior of an explicitly motivated new distribution family exactly where its previously established uniform convergence loses geometric speed. It provides a nonconstant whole-family crossover for the CDF, an exact \(\sqrt3/e\) critical finite-height rate, a one-sided infinite-height contrast, and an attainable local probability-mass profile for every bounded detuning interval. It distinguishes the shrinking finite-height layer from a mere equilibrium bifurcation coefficient. The precise limiting function is useful for resolving small-probability masses and finite-height approximation near \(e^{-e}\). No global distance estimate, density derivative limit, or finite-height mode law is asserted.

## Closest sources and limits

- M. A. Thornton (2026), arXiv:2611.03895v1, https://arxiv.org/html/2611.03895v1 : CDF definition, fixed-parameter limit, known threshold and numerical cusp coefficient; finite-height critical-window formula not supplied.
- R. M. Corless, D. J. Jeffrey and J. Joby (2023), https://rcorless.github.io/Two-cycles.html : two-cycle parametrization and cusp expansions, not joint finite-iteration/parameter asymptotics.
- F. J. Toledo (2022), https://doi.org/10.1007/s13398-022-01213-9 : domains of convergence for generalized power towers with initial data, not a scaling law for a distributional moving parameter.
- There remains a risk of an unlocated equivalent theorem in general near-flip scaling literature. Search coverage does not constitute mathematical uniqueness or historical priority.

Self-review: passed. Independent audit: not yet performed.
