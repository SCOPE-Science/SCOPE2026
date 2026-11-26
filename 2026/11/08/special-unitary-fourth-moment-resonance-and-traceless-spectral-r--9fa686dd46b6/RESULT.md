# Sharp fourth-moment bounds and determinant-phase rigidity on the special unitary group

## Finding

Equip \(\mathrm{SU}(n)\) with probability Haar measure, and let \(n\ge3\). For any nonzero complex \(n\times n\) matrix \(A\) define \(f_A(U)=\operatorname{Re}\operatorname{tr}(A^*U)\) and \(K_n(A)=\mathbb E f_A^4/(\mathbb E f_A^2)^2\). The full range of \(K_n\) is
\[
\begin{cases}
[3n/(n+1),3],& n\ne4,\\
[12/5,7/2],& n=4.
\end{cases}
\]
In all dimensions the minimum is attained exactly at rank one. For \(n\ne4\) the maximum is attained exactly by positive multiples of unitary matrices. For \(n=4\) it is attained exactly by positive multiples of **special** unitary matrices. Thus the fourth power of the sharp \(L^2\)-to-\(L^4\) embedding norm on this real coefficient space exceeds the Gaussian ratio \(3\) only in dimension four. The distinction between unitary and special-unitary extremizers is essential even at a fixed singular spectrum.

## Assumptions and normalization

The coefficient space is that of the real parts of the fundamental matrix coefficients, with no trace, Hermitian or normality constraint on \(A\). With \(S=\operatorname{tr}(AA^*)\), \(Q=\operatorname{tr}((AA^*)^2)\), \(r=Q/S^2\) and (in dimension four) \(d=\operatorname{Re}\det A/S^2\), the normalized moment identities are
\[
\mathbb E f_A^2=\frac{S}{2n},\qquad
K_n(A)=\begin{cases}
\dfrac{3n^2}{n^2-1}\left(1-\dfrac rn\right),& n\ne4,\\[3pt]
\dfrac{16}5-\dfrac45r+8d,& n=4.
\end{cases}
\]
These identities are consequences of known group integration formulas; the sharp optimization over all complex coefficients is the subject here.

## Proof

**Moment reduction.** Write \(Z=\operatorname{tr}(A^*U)\). Multiplication by a central \(n\)-th root of unity makes \(\mathbb E Z^p\bar Z^q\) vanish unless \(n\mid(p-q)\). Balanced moments equal their \(\mathrm U(n)\) versions, since multiplication by a scalar preserves the integrands and scalar times special-unitary Haar gives unitary Haar. In particular \(\mathbb E|Z|^2=S/n\). For the fourth balanced moment, \(Z^2\) is the trace coefficient of \(U^{\otimes2}\) with coefficient \((A^*)^{\otimes2}\). On the symmetric and exterior squares (inequivalent irreducible \(\mathrm U(n)\)-representations), the squared Hilbert–Schmidt norms of the restricted coefficients are \((S^2+Q)/2\) and \((S^2-Q)/2\). Indeed, the projections are half the sum and difference of identity and the transposition of tensor factors, and the trace of \((AA^*)^{\otimes2}\) times the transposition is \(Q\). Schur orthogonality divides each squared norm by its dimension, \(n(n+1)/2\) and \(n(n-1)/2\), and removes cross terms. Hence
\[
\mathbb E|Z|^4=\frac{2}{n^2-1}(S^2-Q/n).
\]
At second order there is no unbalanced term for \(n\ge3\). At fourth order the only permitted unbalanced terms are the pure fourth powers for \(n=4\). Haar averaging \(U^{\otimes4}\) in that dimension projects onto the normalized alternating determinant line, so \(\mathbb E Z^4=\overline{\det A}\). Expanding \((Z+\bar Z)^4/16\) gives the stated balanced term \(6\mathbb E|Z|^4/16\) and the additional term \(\operatorname{Re}\det A/8\) in dimension four.

**Unrestricted optimization.** Let \(x_i\) be the squared singular values divided by \(S\). Then \(x_i\ge0\), \(\sum_i x_i=1\), and \(r=\sum_i x_i^2\in[1/n,1]\). Equality on the left means equal singular values, and on the right rank one. This gives both extremal values and classes for \(n\ne4\).

In dimension four, \(|d|\le\sqrt{x_1x_2x_3x_4}\le1/16\). Therefore
\[
\frac72-K_4=\frac45(r-1/4)+8(1/16-d)\ge0.
\]
Both terms vanish exactly when the singular values are equal and \(\det A\) is positive real, which is precisely \(A=cV\) with \(c>0\) and \(V\in\mathrm{SU}(4)\). To bound the minimum for all determinant phases, apply AM–GM to the six pair products:
\[
1-r=2\sum_{i<j}x_ix_j\ge12\sqrt{x_1x_2x_3x_4}.
\]
This gives the exact lower endpoint and the bound
\[
K_4-\frac{12}{5}=\frac45(1-r)+8d\ \ge\ \frac{2}{15}(1-r)\ge0.
\]
Rank one attains equality at \(12/5\), and conversely equality there forces \(r=1\). The normalized coefficient domain \(S=1\) is connected and \(K_n\) is continuous on it, so the extrema bound the entire attained intervals.

## Relationship to prior work

Collins and Śniady give the unitary Weingarten formula; the balanced integrals above are special cases. Borisenko, Voloshyn and Chelnokov give stronger general special-unitary integration identities, including the determinant-charge terms used here. These are not new moment evaluations in the sense of new integration machinery. The optimized sharp range depends on controlling the determinant term together with the singular spectrum and on the exact phase constraint on the upper extremizers. This is a statement about the unrestricted coefficient space, not about only the single coefficient \(A=I\).

The size-four trace-zero Hermitian determinant interval is not claimed as a second optimization result. In fact, for its four eigenvalues regarded as a centered sample, sample kurtosis is \(b_2=4Q/S^2\). The bounds \(1\le b_2\le7/3\) (the upper bound is Dalén's sample-kurtosis bound at sample size four, as reported in Cox, §2.1) and Newton's identity \(\det A/S^2=1/8-Q/(4S^2)\) already give the sharp interval \([-1/48,1/16]\), realized by the one-outlier and balanced two-point samples respectively. Inserting this into the pointwise fourth moment merely produces a restricted example of the moment identities.

## Verification and limitations

The accompanying `su4_fourth_checker.py` is a finite diagnostic: it inverts the order-two unitary integration Gram matrix, checks the alternating contraction and rational profiles and endpoint examples, and compares selected coefficients with QR-based Haar samples on \(\mathrm{SU}(4)\). Some checks concern the attributed restricted example. Run with Python and NumPy and SymPy installed. Numerical agreement is not used to prove the bounds or their equality conditions. The theorem concerns fourth moments for \(n\ge3\) on the fundamental real coefficient space only; it does not assert higher-order or other representation analogues or exhaustive literature priority.

## References

1. B. Collins and P. Śniady, *Integration with respect to the Haar measure on unitary, orthogonal and symplectic group*, arXiv:math-ph/0402073, §2.2, Corollary 2.4. https://arxiv.org/abs/math-ph/0402073
2. O. Borisenko, S. Voloshyn and V. Chelnokov, *SU(N) polynomial integrals and some applications*, arXiv:1812.06069, §§2 and 3.1. https://arxiv.org/html/1812.06069v1
3. J. Dalén, *Algebraic bounds on standardized sample moments*, Scandinavian Journal of Statistics 14 (1987), 155–162.
4. N. J. Cox, *Speaking Stata: The limits of sample skewness and kurtosis*, Stata Journal 10 (2010), 482–495, §2.1, equation (2). https://doi.org/10.1177/1536867X1001000311
