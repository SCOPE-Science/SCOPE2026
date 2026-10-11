# Nontrivial pointwise saturation is impossible for the generalized-concurrence QFI speed bound
## Finding
For the generalized concurrence \(C_N\) and quantum Fisher information \(F_Q\) defined in arXiv:2609.31853v1, there is no nontrivial pointwise saturation of the bound
\[
\left|\frac{{dC_N}}{{dg}}\right|\le \sqrt{{F_Q}}
\]
when the ordinary two-sided derivative exists. More precisely, at every differentiability point with \(F_Q>0\),
\[
\left|\frac{{dC_N}}{{dg}}\right|<\sqrt{{F_Q}}.
\]
Equality is possible only in the trivial case \(F_Q=0\), where both sides vanish. Consequently, the source paper's statements that the general bound is "touched exactly" at product-state instants must be read as a limiting or one-sided saturation statement, not as equality of the ordinary derivative appearing in the theorem.

## Assumptions and scope
The state is a differentiable pure \(N\)-partite state path in the sense used by arXiv:2609.31853v1. For each inequivalent bipartition \(i\),
\[
C_i=\sqrt{{2\left(1-\operatorname{{Tr}}\rho_i^2\right)}}
\]
and
\[
C_N=\sqrt{{\frac1M\sum_i C_i^2}},\qquad M=2^{{N-1}}-1.
\]
The claim concerns ordinary two-sided differentiability of \(C_N\) at the parameter value under discussion. It does not deny the source paper's inequality itself, nor its rank-two tightened inequality. It corrects the interpretation of equality/saturation for the general bound.

## Proof
At a point with \(C_i>0\), the source paper derives
\[
\left|\frac{{dC_i}}{{dg}}\right|\le \frac{{2\Delta A_i}}{{C_i}}\sqrt{{F_Q}},
\]
where, for the eigenvalues \(\{{\lambda_k}\}\) of the reduced state,
\[
(\Delta A_i)^2=\sum_{{k<\ell}}\lambda_k\lambda_\ell(\lambda_k-\lambda_\ell)^2.
\]
For every contributing pair one has \(\lambda_k\lambda_\ell>0\). Hence \(|\lambda_k-\lambda_\ell|<1\), so whenever \(C_i>0\),
\[
(\Delta A_i)^2<\sum_{{k<\ell}}\lambda_k\lambda_\ell=\frac{{C_i^2}}4.
\]
Therefore, if \(F_Q>0\), every positive-concurrence cut obeys the strict bound
\[
\left|\frac{{dC_i}}{{dg}}\right|<\sqrt{{F_Q}}.
\]

Now suppose \(C_N>0\). At least one \(C_i\) is positive, and differentiation of the root-mean-square definition gives
\[
\left|\frac{{dC_N}}{{dg}}\right|
\le \frac{{1}}{{MC_N}}\sum_i C_i\left|\frac{{dC_i}}{{dg}}\right|
< \frac{{\sqrt{{F_Q}}}}{{MC_N}}\sum_i C_i
\le \sqrt{{F_Q}},
\]
where the final inequality is the arithmetic-mean/root-mean-square inequality. Thus equality is impossible at every entangled differentiability point with nonzero QFI.

It remains to consider \(C_N=0\). Since \(C_N\ge0\), any parameter value with \(C_N=0\) is a local minimum. If the ordinary derivative exists there, it must be
\[
\frac{{dC_N}}{{dg}}=0.
\]
Hence, if \(F_Q>0\), the inequality is again strict. Equality can occur only if \(F_Q=0\), in which case both sides are zero and there is no nonzero state-space speed.

The source paper's own two-level family illustrates why its displayed curves can visually approach the envelope without pointwise equality. Take
\[
|\psi(\theta)\rangle=\cos\theta\,|0\rangle^{{\otimes N}}+\sin\theta\,|1\rangle^{{\otimes N}}.
\]
Every nontrivial bipartition has the same Schmidt probabilities \(\cos^2\theta\) and \(\sin^2\theta\), so
\[
C_N(\theta)=|\sin 2\theta|.
\]
For this normalized pure-state path,
\[
F_Q=4.
\]
Away from product points,
\[
\left|\frac{{dC_N}}{{d\theta}}\right|=2|\cos2\theta|<2=\sqrt{{F_Q}}.
\]
At \(\theta=k\pi/2\), the ratio tends to one, but \(|\sin2\theta|\) has a cusp and the two-sided derivative does not exist. Thus the boundary behavior is limiting/one-sided saturation, not pointwise saturation of the theorem's derivative.

## Verification
The proof uses only the source paper's exact definitions and its spectral identity for \((\Delta A_i)^2\), plus strictness of \(|\lambda_k-\lambda_\ell|<1\) for positive pairs and the elementary fact that a differentiable nonnegative function has derivative zero at a zero. The included `verify.py` checks the GHZ-family formulas numerically on both sides of a product point and confirms the one-sided slopes \(\pm2\), \(F_Q=4\), and strict interior ratio.

## Relationship to prior work
arXiv:2609.31853v1 proves the valid universal inequality and explicitly observes that its spectral step is never exactly saturated when a bipartition has positive concurrence. It nevertheless describes the general bound as being "touched exactly" at isolated product-state instants, while its figure caption also marks those instants as points where the derivative does not exist. The present finding resolves that internal tension by proving a global no-nontrivial-pointwise-saturation statement: positive-concurrence points are strict, and differentiable zero-concurrence points have zero derivative.

Targeted published-finding corpus searches for the paper identifier, product-boundary saturation, cusp differentiability, and generalized-concurrence/QFI equality found no record stating this correction.

## Limitations
This result does not alter the inequality itself and does not rule out asymptotic saturation, one-sided saturation, or exact saturation of the separate rank-two tightened bound away from the product boundary. It is specifically about equality in the paper's general bound using the ordinary derivative appearing in its theorem. The source was inspected through its full arXiv HTML rendering; no claim is made about later revisions after v1.

## References
1. Z. H. Saleem, D.-W. Luo, A. M. Babu, T. Yu, S. K. Gray, and A. Shaji, "Quantum Fisher Information as the Speed Limit for Multipartite Entanglement," arXiv:2609.31853v1 (2026).
