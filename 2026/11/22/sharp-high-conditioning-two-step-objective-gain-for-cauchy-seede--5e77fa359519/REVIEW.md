# Scientific review: two-step objective gain after curvature feedback

## Correctness — PASS

The claim is limited to two-dimensional positive-definite quadratics with an exact first line search and one subsequent curvature-feedback step. The proof derives both updates from the specified gradients, reduces the gain to one explicit function of the spectral ratio, bounds it by a polynomial with positive coefficients, and constructs the sharp asymptotic family. An exact rational witness gives an initial-to-final objective increase. Symbolic identities, rational arithmetic and independent direct-update comparisons ran successfully (`artifacts/verify_two_step.py`, `artifacts/verification.txt`). Numerical sampling does not establish the universal inequality; the displayed algebraic certificate does.

## Originality — PASS, qualified

The one-step geometric-mean spectral update is classical and explicitly credited to earlier work. The motivating contemporary algorithm introduces running extrema but reduces to that classical step at its first feedback update. Its published result concerns stepsize convergence, not the sharp initial-to-final two-step objective gain. The most pertinent accessible mathematical record proves a sharp local one-step bound for every BB-interval selector, but that bound gives only an order-quadratic estimate for the complete two-step gain when combined with standard Cauchy descent; it neither states nor implies the sharp linear leading coefficient without additional analysis. A separate two-mode result treats a different adaptive optimizer. The accessible 2018 spectral-gradient manuscript was inspected in its method and convergence sections; its results concern update identities and convergence rates rather than the stated finite-horizon extremum. The complete 2015 positive-BB chapter was unavailable and is the main priority risk.

## Value — PASS

The exact numerical objective can exceed its starting level after a *best-possible first step*; the loss growth is not merely a relative spike from an already tiny intermediate iterate. The sharp order-\(\kappa\) finite-budget amplification and exact witness give a motivated stability benchmark for spectral feedback used before estimators have stabilized. The statement is narrow and does not suggest a new algorithm, general-dimensional result, or eventual divergence.

## Limits and literature

The theorem is for two spectral modes and two updates only, with no assertion of an exact finite-\(\kappa\) optimizer. Closest published references are [1]--[6] in `RESULT.md`; the complete 2015 analysis was not inspected, and independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
