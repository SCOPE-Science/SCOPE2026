# Scientific assessment

## Correctness — PASS

The result follows from Gaussian convolution, symmetry reduction of the three-by-three positive-definite Gram system, and a global monotonicity lemma. The sign of the center coefficient is the sign of \(\eta-H(q)\), while both outer weights are strictly positive. Dividing \(H'(q)\) by \(4q^3\) produces a strictly decreasing expression with opposite endpoint signs, proving a single global maximum without numerical sampling or regularity assumptions on the Gaussian mixing law. A pointwise comparison to \(2q-1-q^4\) and a broad-Gaussian limiting family prove the sharp universal constant. The second derivative at the maximum is strictly negative, giving the square-root fold.

The separately implemented direct system-solving checks in `verify.py` passed for 7,203 finite cases and limiting examples. They are supplementary, not exhaustive proofs. At zero noise the three nodes must remain distinct; nonzero noise does not ensure positivity of realized noisy data.

## Originality — PASS, with qualification

[1] considers Gaussian-kernel weights for Gaussian integration measures and specially scaled Gauss–Hermite nodes; it does not classify the complete sign diagram over all spacings for arbitrary centered Gaussian scale mixtures. [2] proves general sufficient positivity conditions for locally optimized nodes, not a necessary-and-sufficient global nugget threshold for prescribed symmetric nonoptimal nodes. [3] treats asymptotic RBF-quadrature stability and oversampled remedies. [4] gives a different one-crossing diagram for the bounded uniform integration measure, varying the kernel shape with no nugget.

A pre-existing general three-node reduction already yields the exact *pointwise* central-coefficient sign test for symmetric targets; that reduction, and its small-spacing behavior, are not novel claims. The assessed new statement is the strict one-maximum law across all spacings for an entire nonparametric target family, the universal target-independent sharp threshold, the unique forbidden spacing interval, and its fold. Searches for aliases, regularized kernel-weight signs and Gaussian-mixture targets identified no stronger result that asserts those additional global properties. Historical priority remains provisional; general identities can sometimes conceal a published specialty theorem.

## Value — PASS

Positive kernel quadrature weights are relevant to stability, monotonicity on nonnegative sample data and interpretation of the quadrature as a nonnegative discrete measure. A single exact worst-case nugget \(3\,2^{-4/3}-1\) covers all Gaussian scale-mixture target distributions, while each target has its own smaller critical level. The theorem also explains the reentrant sign effect: small but positive regularization makes nearly colliding samples positive, intermediate spacing can still yield a negative center weight, and wide spacing is positive again. This is a qualitative classification of a natural three-sensor architecture for a broad target class, rather than a numerical estimate at one arbitrary parameter. It does not optimize integration accuracy or recommend injecting physical measurement noise to improve the data.

## Closest sources and limitations

[1] Karvonen–Särkkä, *Gaussian kernel quadrature at scaled Gauss–Hermite nodes*, arXiv:1803.09532 (2018-03-26).

[2] Karvonen–Kanagawa–Särkkä, *On the positivity and magnitudes of Bayesian quadrature weights*, arXiv:1812.08509 (2018-12-20).

[3] Glaubitz–Reeger, *Towards stability results for global radial basis function based quadrature formulas*, arXiv:2301.12998 (2023-01-30).

[4] *A one-crossing positivity diagram for symmetric three-node Gaussian kernel quadrature*, public mathematical record (2026-11-02), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-a-one-crossing-positivity-diagram-for-symmetric-three-node-gauss--bf59562e8e52/RESULT.md

The scope requires a squared-exponential kernel, one symmetric three-node rule, common diagonal nugget and a centered Gaussian scale-mixture target. It does not include arbitrary distributions, extra nodes or asymmetric design optimization. Positivity of the coefficients does not guarantee the sign of noisy recorded values.

Self-review: passed. Independent audit: not yet performed.
