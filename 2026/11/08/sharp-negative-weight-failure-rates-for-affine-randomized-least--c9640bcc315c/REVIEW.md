# Scientific review: affine least-squares quadrature negative-weight probability

## Correctness (PASS)

For the symmetric iid degree-one design the normal equations give \(w_i=(Q-SX_i)/(mQ-S^2)\). The denominator is positive almost surely, and the negative-weight event is equivalent to \(Q<S\max_i X_i\) if \(S>0\), or its reflected analogue if \(S<0\). The endpoint-tilted Cramér upper bound is obtained by Chernoff; a designated near-endpoint sample and a strict large-deviation event on the remaining samples yield the matching lower exponential rate. Continuity of the convex moment-generating minimum gives the limit. The three-node uniform probability follows from an exact one-dimensional integral yielding \((2+\pi)/16\). Both asymptotic and exact finite identities are proved in RESULT.md, without treating numerical checks as infinite proofs. The accompanying standard-library checker passed 4,648 exact rational cases and independent numerical consistency tests.

## Originality (PASS, with priority caveat)

Bělík--Narayan--Turnage, *Constructive Tchakaloff results and well-conditioned quadrature through randomized least squares* (2026, arXiv:2609.09506v1), derives weighted least-squares quadrature and high-probability weight positivity conditions; its examined Sections 2.2, 2.6, 3.3 and 4 do not supply the distribution-dependent sharp negative-weight large-deviation exponent or the exact three-uniform-node failure probability. Migliorati--Nobile, *Stable high-order randomized cubature formulae in arbitrary dimension* (arXiv:1812.07761), studies different sampling and gives sufficient probabilistic positivity. A published deterministic affine \(L^2\)-projection positivity-defect result on simplices concerns a different object; published Newton--Cotes and Savitzky--Golay positivity results also do not cover this random least-squares quadrature event. Literal literature searches did not identify a covering prior formula. Historical-priority uncertainty remains, including possibly related sample-calibration literature, and absence from a database cannot prove uniqueness.

## Mathematical value (PASS)

The source's high-probability weight-positivity result is not an exact probability. The theorem supplies the sharp logarithmic budget scale for rare negative weights for every bounded symmetric nonatomic input law; the three-node case supplies an exact nonasymptotic calibration. Negative weights matter for monotonicity, nonnegative inputs and robustness of quadrature. These quantities do not by themselves give prefactors, rates for all polynomial degrees, or guarantees for postprocessed positive weights.

## Independent-status and limitations

No independent audit or independent validation has been performed. The general asymptotic rate assumes compact symmetric support and identical integration and sampling measures; the finite constant specializes to the continuous uniform distribution. Numerical approximations are only supplemental.

Self-review: passed. Independent audit: not yet performed.
