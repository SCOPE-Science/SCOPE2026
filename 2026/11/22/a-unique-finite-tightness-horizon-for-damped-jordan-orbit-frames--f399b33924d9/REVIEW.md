# Self-review

## Correctness: PASS

For any nonzero generator \(v=(x,y)\), the orbit is \(e^{-at}(x+bty,y)\). Its frame matrix equals a centered second-moment matrix; with \(y\ne0\), it is a scalar multiple of \(\left(\begin{smallmatrix}|z|^2+\rho_T&z\\\bar z&1\end{smallmatrix}\right)\), whose determinant is exactly \(\rho_T\) independent of \(z\). Consequently the condition-number optimizer is uniquely \(z=0\). Direct exponential integration yields \(\rho_T=(b/(2a))^2[1-(aT/\sinh(aT))^2]\). Strict monotonicity of \(s/\sinh s\) yields every horizon classification, including the unique finite tight horizon iff \(b>2a\). The proof handles all positive parameters and all complex directions, plus singular \(y=0\). `verify.py` passes 862 numerical tests, supplementary to the exact proof; the independent symbolic moment calculation gives zero discrepancy.

## Originality: PASS on inspected evidence

The motivating full preprint arXiv:2611.13867v1 supplies half-line semigroup frame existence and general tightness but does not optimize the finite Jordan orbit or its horizon. arXiv:1801.10103 concerns normal operators, and arXiv:1902.04548 discusses the general connection between Gramian conditioning and tightness, not the present exact parameter threshold. Closest complete related results inspected are the published pinned-three-measurement damped-Jordan determinant design, diagonal discrete infinite-horizon two-mode condition design, and damped cyclic permutation actuator majorization; none dominates this exact finite continuous frame claim. The variance and basic Gramian identities are classical and not presented as new. Historical two-regressor experimental-design literature may contain an equivalent result, so priority remains provisional.

## Value: PASS

The finding resolves a natural attainable-tightness and condition-minimizing-vector question for the smallest nonnormal continuous orbit, giving a complete three-regime classification and a concrete counterintuitive boundary: collecting longer than the unique critical horizon strictly degrades the smallest achievable frame condition number. The exact threshold \(b>2a\), unique center-shifted generator, and sharp frame bounds are useful design facts that do not follow from mere frame existence. The scope is intentionally finite and specific; extensions to other generators, time weights, or higher Jordan blocks are unproved.

Self-review: passed. Independent audit: not yet performed.
