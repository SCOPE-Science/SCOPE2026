# Scientific review

## Correctness
**PASS.** For positive tumbling, resetting and speed, the bounded backward first-hit equations have the unique decaying solution displayed in `RESULT.md`. The reset renewal and geometric adsorption-cycle renewal are algebraically independent steps and yield the exact signed protocol difference. The derivative of the switching function has strictly negative sign, ruling out additional crossings; the alternative rate section follows from a strictly increasing hyperbolic parametrization. Endpoint expansions follow from convergent local Taylor series and explicit large-argument hyperbolic asymptotics. The standalone `verify.py` passed 923 checks, including event-driven simulations; finite tests support but do not replace the proof.

## Originality
**PASS, qualified.** The directly motivating Bressloff–Linn paper [1], section IV and Figure 9, already establishes the two protocol-specific mean-passage formulas and qualitative parameter preferences. Its stated results and contour comparison do not contain the single global switching-curve theorem, uniqueness for every fixed reset/tumble section or endpoint laws. These are nontrivial deductions of a known framework rather than claims to invent the model. The encounter-count work [2] and telegraph resetting background [3] do not cover the same desorption comparison. Topic searches and inspected scientific sources revealed no matching statement; this is not an exhaustive priority guarantee. The main residual risk is an equivalent formula or classification in related supplemental or nonindexed literature.

## Value
**PASS.** The motivating problem is to determine which physically different desorption mechanism yields faster permanent capture. Existing qualitative contours leave unresolved whether the preference can reenter as rates change. The complete necessary-and-sufficient phase boundary rules out reentrance, covers both launch orientations, isolates the exact dimensionless threshold and shows that wall dwell statistics cannot move the switching curve. Exponential high-reset and logarithmic low-crowding endpoints quantify how narrow the favorable regime becomes. This is a natural complete parameter classification, not an arbitrary numerical slice.

## Closest literature and limitations
[1] P. C. Bressloff and S. Linn, *Renewal theory for a run-and-tumble particle with stochastic resetting and a sticky boundary*, arXiv:2602.02446v1 (2026-02-02), https://arxiv.org/html/2602.02446v1, sections III–IV and appendix. [2] P. C. Bressloff, arXiv:2503.01304 (2025-03-03), encounter-based wall absorption. [3] M. R. Evans and S. N. Majumdar, arXiv:1808.06450, classical telegraph resetting.

The proof requires half-line confinement, bulk Poisson resets to the original state, and independent identically distributed finite-mean bound dwell times with the same wall kinetics in both protocols. The source already provides formula-level coverage of mean first passage, so any independent novelty assessment must distinguish the sharpened global classification from straightforward algebraic special cases. No independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
