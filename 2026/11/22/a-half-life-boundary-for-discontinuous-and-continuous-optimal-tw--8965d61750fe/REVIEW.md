# Scientific review: two-bolus threshold-duration optimization

## Correctness — PASS

The result derives the exact exposure factor \(W(a)=\min\{\max\{a,1\},q^{-1}\}\max\{1,d-(1-q)a\}\) from two positive-time regions of a piecewise exponential concentration. The full feasible dose interval is partitioned by the threshold and clipping boundaries. Comparing the strictly concave quadratic branch against the single-bolus endpoints and the declining capped branch establishes the global argmax, uniqueness, and all tie cases for each positive clearance rate, dose total and separation. An exact-rational standalone checker provided 183183 corroborating assertions. It cannot by itself establish an infinite-domain theorem.

## Originality — PASS, provisional historical priority

Corvaisier et al. (1998) use time above MIC under single-compartment IV models and compare indices with bacterial killing. Jacobs (2001) treats PK/PD efficacy indices, and Ibrahim et al. (2004) study a finite set of pulse regimens experimentally. These inspected papers do not give a global analytic optimizer over a fixed-total two-impulse split. Full indexed mathematical results on two oral doses concern either periodic squared-fluctuation phase optimization or the number of peaks from delayed depot absorption, which do not imply the exact clipped-product optimization. The 1999 Plusquellec et al. nonuniform steady-state paper was available only as an abstract and leaves a specific historical-overlap risk. Other older or more general optimization theorems may also subsume this case; finite search is not a uniqueness certificate.

## Value — PASS

A natural exposure measure and dose-budget constraint yield the sharp boundary at one elimination half-life. The character of the optimizer changes there: an unequal second dose becomes optimal by a discontinuous jump for long gaps, while for shorter gaps it emerges continuously. Moreover the open parameter set \(4(1-q)<d<4/(1+q)\) supplies a robust reversal: equal splitting underperforms a single bolus, yet a particular unequal split outperforms it. This is an interpretable structural boundary in a minimal pharmacokinetic model and a counterexample to a generic equal-fractionation assumption. The finding is not a validated medical regimen or a model of bacterial response.

## Closest scientific literature and limitations

The closest applications are Corvaisier et al. (1998), Jacobs (2001) and Ibrahim et al. (2004), alongside the full indexed fluctuation and delayed-Bateman peak theorems discussed in RESULT.md. Broad optimal-dosing computations such as Bachmann et al. (2024) optimize different efficacy and safety functionals and are not a derivation of this model's complete equality cases. The argument requires instantaneous linear dosing, fixed administration times, zero initial residual drug, a single concentration threshold and an infinite postdose observation horizon. It does not establish efficacy, toxicity bounds, optimal patient treatment, robustness to uncertain rate constants or historical priority beyond the inspected materials.

Self-review: passed. Independent audit: not yet performed.
