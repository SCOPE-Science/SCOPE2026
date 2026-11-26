# Independent mathematical audit

## correctness

PASS

For the final result in /workspace/repairs/1/RESULT.md, I checked Definitions 2–3 against the extra explicit all-integer clipping assumption. The zero-predictor branch contributes e^(-t); Poisson thinning in the positive-predictor branch contributes e^(-theta p0 t)−e^(-theta t), with p0=(1−1/(2 theta))/theta in [0,1]. No return to state one is possible, so products are exact and the derivative at zero gives the stated fixed-time limit. The coefficient range [1/2,2−sqrt(2)] follows from AM–GM and endpoint convexity. At the midpoint the perfect square in e^(-t/2) gives the unique minimizer and recovery; without thinning only the zero-predictor branch can survive. The repair corrects the verification description: frozen verify.py lines 16–63 are Poisson-sum and sampled survival checks, not a transition-matrix construction. The script was inspected, not executed; the analytic derivation accounts for all parameters.

## originality

PASS

Pass only the repaired distinct exact finite-step claim: survival law, sharp midpoint floor and recovery, and exact contrast to the baseline. A distinct Resultary theorem covers the first-order inconsistency coefficient and implies the refined-time limit under absorption. The repaired finding retains the limit as a credited consequence, not a separate novelty claim. No priority order follows from the index date.

## value

PASS

An exact, all-step-size survival obstruction at the smallest occupied state shows a concrete failure mode of a correction designed for degenerate propensities. The midpoint retains at least three quarters of initial particles in probability even when true survival is nearly zero, while the unadjusted scheme has exact survival under the same clipping. This is more informative for a low-count diagnostic than reporting only a local error term. No inference about all observables, network behavior or nonnegativity is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
