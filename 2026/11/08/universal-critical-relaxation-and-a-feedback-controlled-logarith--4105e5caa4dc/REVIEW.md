# Self-review

## Correctness — PASS

The critical identity \(\dot I=-\beta I[I+R+(1-\sigma)C]\) gives global extinction at the nonhyperbolic threshold for every nonnegative simplex initial state; positive infection persists for finite time. Stable forced linear equations first show \(R,C\to0\), then \(R,C=O(I)\), then \(R/I\to a\) and \(C/I\to c\). The argument derives the leading \(I\sim1/(Kt)\) rather than assuming it. Exponentially weighted convolutions give the second-order slaving coefficients \(b,d\), and substitution gives the cubic \(\dot I=-KI^2-LI^3+O(I^4)\). Because \(I-(Kt)^{-1}\) is integrable, the reciprocal has an actual finite constant term after the logarithm, not merely a formal expansion. The included checker confirms six universal algebraic coefficient identities, 576 exact rational residual assertions for both feedback choices, and the sign-change family. Finite checks are corroboration only. There is no unproved extension beyond the exact threshold.

## Originality — PASS within inspected literature

The originating arXiv paper [1] was read in HTML, including the model equations, disease-free linearization, threshold statements, equilibrium results, and relevant appendices. It records nonhyperbolicity at \(\mathcal R_0=1\) but develops the strict threshold and endemic regime, not the global critical relaxation or either feedback-dependent logarithmic coefficient. The published published-finding corpus theorem [3] for exactly these equations was inspected in its complete RESULT document; it proves steady-state uniqueness and feedback monotonicity and explicitly disclaims stability, so it cannot imply the trajectory-wise conclusion. Other critical disease-decay findings were compared by model equations and claimed observables; the coincidence of \(t^{-1}\) exponents is not a statement-level implication. The classic no-feedback SIRC article [2] was accessible as a bibliographic abstract only and could contain uninspected special-case critical analysis, an acknowledged historical risk. The two-feedback cubic coincidence and sign reversal are not consequences of that zero-feedback restriction. Standard center-manifold and reciprocal-ODE asymptotics are acknowledged; no general methodological novelty is claimed.

## Value — PASS

The source leaves an exact nonhyperbolic population-threshold case outside its local stability classification. Global extinction is useful because a linearization with a zero eigenvalue cannot decide attraction. The universal \(1/t\) constant and the signed logarithmic coefficient distinguish first-order threshold behavior from the first feedback-sensitive term, for both original feedback constructions. A nonarbitrary integer-rate example proves the correction changes sign at a finite, exact feedback strength, so this is a structural boundary rather than a numerical fit or routine parameter substitution.

## Scope and unresolved priorities

The result does not address supercritical periodic orbits, time-dependent transmission, or empirical inference. Its \(O(\cdot)\) constants depend on parameters and initial state. Full-text historical comparison to the 2006 zero-feedback paper was not possible; this is not evidence of uniqueness in all literature. Independent validation is outstanding.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Ramírez-Gutiérrez et al., arXiv:2610.01111v1, 2026-10-01. https://arxiv.org/html/2610.01111v1

[2] Casagrandi et al., *The SIRC model and influenza A*, Math. Biosci. 200 (2006), DOI:10.1016/j.mbs.2005.12.029.

[3] *All-feedback endemic uniqueness and separate monotonicity in the prevalence-driven SIRCm system*, published published-finding corpus record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-all-feedback-endemic-uniqueness-and-separate-monotonicity-in-the--c54c540be342.
