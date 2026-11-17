# Scientific review: quartic Savitzky–Golay variation gain

## Correctness — PASS
The exact convolution kernel is reconstructed from the even least-squares Gram inverse and satisfies polynomial reproduction. Discrete differentiation commutes with convolution, and a step input has a single-impulse derivative, making the \(\ell^1\) kernel norm exactly sharp for total variation. The finite-range global comparison covers each integer window radius \(2\le m\le1999\) with strict integer cross products, aside from exact equality at \(m=6\). The infinite tail \(m\ge2000\) has an independent uniform-polynomial approximation estimate and a rational upper bound separated strictly from \(3763/2431\). No floating-point comparison is required for the theorem.

## Originality — PASS, qualified
The closest fully inspected prior result proves the corresponding **quadratic/cubic** seven-point maximum and explicitly leaves higher degrees outside scope. The classical 1964 source introduced the coefficients rather than the new quartic all-window sharp optimization; the 2022 full-text signal-processing study addresses ringing, stopband response and practical smoothing design rather than exact variation gain. Searches under alternate names including kernel \(\ell^1\) norm, negative coefficient mass, positivity defect, total variation, fourth-degree least-squares smoothing and thirteen-point extremizers revealed no theorem covering the unique quartic all-window maximum. Unindexed equivalent work remains a residual risk; the 1964 publisher-restricted full paper was not fully inspected.

## Mathematical value — PASS
The all-window problem is motivated by deterministic stability of a long-used polynomial smoother, not by a freely chosen numerical example. Higher-order quartic coefficients have two sign crossings, distinct from the previously solved quadratic case. A large finite sharp peak at thirteen points and a strictly smaller asymptotic plateau explain why increasing window length is not monotone for worst-case variation robustness. The complete integer-radius classification is usable directly for filter-window choice.

## Closest literature and limits
Savitzky–Golay (1964) supplies the basic smoother. Schmid–Rath–Diebold (2022) documents shortcomings and alternatives. The previously published quadratic sharp-positivity theorem concerns a different, strictly lower polynomial degree. The result does not extend to finite-boundary implementation, irregular nodes, weighted windows or probabilistic mean-squared performance. Historical all-window uniqueness has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
