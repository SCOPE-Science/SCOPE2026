# Independent mathematical audit

## correctness

PASS

First-clock greedy matching stabilizes locally by the factorial probability of a long descending homogeneous run. Cutting the target before its first arrival makes its endpoint vacancies independent. At the end of a homogeneous half-line the vacancy solves f(t)=1−∫₀ᵗ e^(−u) f(u) du by cutting its sole incident bond; replacing that bond density by a e^(−au) and then advancing through ordinary bonds gives the stated Volterra equations after x=1−e^(−t). The four-rate difference of the product of vacancies gives the mixed integral exactly. Under the coupling T_a=E/a with E unit exponential, the first marked bond deposits before a fixed deadline with probability E[f(T_a)·1{T_a≤t}], strictly increasing in a since f is strictly decreasing. Volterra iteration reverses the strict sign each step and gives |δ_j(x)|≤x^(j−1)/(j−1)!. Multiplication and integration give the claimed nonzero sign and bound for non-unit rates, including d=2; a unit marked rate makes the difference zero. Own exact finite residual-graph enumeration and separate Gauss integration passed five cases, including rates below one and opposite-signed anomalies, with maximum absolute finite/infinite discrepancy 4.08e−8 at seven buffer edges. Replay: python3 /workspace/reproductions/frozen_math_checks.py 3; output /workspace/reproductions/record-3.txt. This is bounded corroboration, not a proof or a replay of the frozen twelve-edge experiment.

## originality

FAIL

The prior one-defect paper does more than state a final single-defect probability. Its proof uses the exact independent-half-line acceptance product and derives the full time-dependent one-defect cavity q_j=f+δ_j, with pointwise signs and the same pointwise factorial bound. After cutting the intermediate edge in the frozen claim, each component is precisely one of those established cavities (the right one reflected). Substituting both factors and taking the four-rate difference gives ∫δ_j δ_(d−j) against the unit clock density immediately. The sign and integral bound are direct substitutions of the same prior pointwise statements. The mixed observable is differently phrased and is not stated in the prior Finding, but the asserted theorem is mechanically implied by its published proof. Inaccessible heterogeneous papers do not enter this rejection.

## value

FAIL

The nonlinear edgewise interaction is a natural diagnostic and the sign is a useful way to state it, but the frozen result does not establish new analysis beyond the known exact time-dependent one-defect cavities and their independence at this cut. The identity, sign and screening bound are immediate algebraic consequences of those ingredients, not an independently unresolved invariant. No further distance asymptotic, coupled-cavity regime or covariance claim survives in the frozen statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
