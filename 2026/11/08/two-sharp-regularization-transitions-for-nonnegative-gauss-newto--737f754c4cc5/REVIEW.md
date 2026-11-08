# Self-review

## Correctness — PASS

The proof starts from the source-defined NGN formula and derives an exact spectral-variance identity for the one-step objective ratio. The elementary endpoint-moment inequality is sharp **for every specified matrix with actual extremal eigenvalues**, because its endpoint eigenspaces are available and can realize every mixture. The derivative of the resulting one-variable rational objective is affine in its spectral-mean parameter, establishing the unique maximizer and both branches. Differentiation in the regularization parameter establishes the unique minimax scale. The AM–GM equality case gives necessity as well as sufficiency of the strict descent frontier. The explicit diagonal witness has exact ratio \(41/31\). The independent arithmetic implementation in `artifacts/verify.py` was run successfully, reporting 37,727 exact-rational/deterministic numerical assertions. Finite tests are supplementary, not an infinite proof.

## Originality — PASS (qualified)

Actual comparisons include the publicly available July 2024 NGN source (arXiv:2407.04358v1, its defining rule and deterministic/stochastic properties), the publicly posted 2026 scaled-Polyak quadratic frontier (full RESULT.md), and Huang–Qi's July 2024 spectral-gradient family (arXiv:2407.04914v1, Section 2). The doubled-Polyak \(3+2\sqrt2\) barrier, the known optimal-gradient factor and the spectral moment inequality are explicitly excluded from novelty. None of the inspected claims asserts the NGN *fixed \(\sigma\)* sharp two-branch objective factor, the mode-switch threshold, the unique finite optimal regularization, or the finite-regularization objective-descent cutoff. Crucially, fixed-scaled Polyak has a constant multiplier while NGN's multiplier depends on the current spectral mean; the former's sharp envelope does not attain the latter's coupled statewise maximum at all spectral means. Primary literature nomenclature is broad, so a historically equivalent finite-regularization result remains a residual risk.

## Value — PASS

Nonnegative Gauss–Newton promises robust optimization behavior with a freely tunable regularization; the exact distinction between safe all-state one-step descent, optimal worst-case contraction, and a transient objective increase is a mathematically motivated calibration question, not a cosmetic variant. The result identifies two distinct structural thresholds, provides sharp extrema in every dimension, and gives a practical exact benchmark for testing parameter choices in quadratic models. No claim of a general downstream convergence theorem is made.

## Limitations and closest literature

All statements concern exact arithmetic, centered positive-definite quadratics, deterministic full gradients and one step only. The 2026 public scaled-Polyak theorem is the closest overlap; it already supplies the shared large-regularization constant and minimax objective-factor value, but not the state-coupled NGN envelope. The 2024 NGN paper supplies the algorithm and general convergence framework. Publication-priority uncertainty about uninspected older adaptive step literature remains.

Self-review: passed. Independent audit: not yet performed.
