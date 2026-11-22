# Scientific review

## Correctness
**PASS.** The Butcher coefficients and unique-SSP optimum are explicitly identified in Weng–Yu–Zhu, Theorem 5.2. Triangular stage substitution yields the rational-power stability function already published for negative-real stability. The analyticity and \(\varepsilon\mapsto-\varepsilon\) symmetry make the logarithmic expansion odd; the coefficient \(P(z)\) is obtained by Taylor expansion and checked independently. Substituting weak real damping and taking modulus gives the exact leading function; \(\lvert\sin t\rvert<\lvert t\rvert\) establishes strict positivity. A derivative bounded away from zero supplies a unique local crossing. Exponentiating the logarithmic energy expansion proves the long-horizon limit. The standalone verifier passes 97 finite cross-checks but is not used as an infinite proof.

## Originality
**PASS, qualified.** The arXiv primary source proves optimality and gives coefficients, not this spectral asymptotic. The closest published published-finding corpus result proves a real-axis cutoff and explicitly declines to classify the complex plane; its exact transfer formula is acknowledged and reused. The 2007 original coefficient paper, the 2019 full text with four-stage stability plots, and the 2026 algebraic-stability obstruction do not state or imply the sharp explicit large-stage weak-damping profile, its boundary location, or the accumulated energy law merely as stated results. The calculation is a new asymptotic implication of the already-known rational transfer, not an independently new algorithm. Unindexed analyses of imaginary-axis asymptotics remain a priority risk; no search is treated as proof of novelty.

## Value
**PASS.** Fourier-mode energy stability is a standard desideratum for hyperbolic semidiscretizations. The source family is uniquely optimized for nonlinear SSP radius yet can generate artificial amplification on imaginary modes; an exact damping profile at large stage count is an interpretable quantitative design limitation. The \(s^{-2}\) frontier and accumulated \(s^2\)-step energy law distinguish this effect from ordinary low-frequency truncation error and from the already-understood negative-real scalar cutoff. It is not an arbitrary parameter slice: the quadratic stage-count scaling is the first nonzero defect and the wave frequency is the natural nondimensional spectral variable.

## Closest literature and limitations
Weng–Yu–Zhu (arXiv:2610.37425v1); Ferracina–Spijker (Leiden 2007-11, §3.3); *Exact real-axis stability frontier* (published 2026-11-08, full RESULT.md); Fekete–Horváth (2019, §2.2 and Figure 2); Gottlieb et al. (arXiv:2611.07981v1, §5). The theorem is asymptotic, uses bounded fixed frequencies, and does not settle finite-stage imaginary-axis stability or nonnormal problems.

Self-review: passed. Independent audit: not yet performed.
