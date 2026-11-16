# Sharp stagger tolerance and spectral flatness in two-bank Fourier–Hermite interpolation

## Finding

For every positive integer \(m\), consider the complex trigonometric polynomials
\[
f(x)=\sum_{k=-m}^{m-1}c_k e^{2\pi i kx},\qquad x\in\mathbb R/\mathbb Z,
\]
with coefficient norm \(\|c\|_2\). Measure values on the grid \(j/m\) and scaled first derivatives on the uniformly shifted grid \((j+\alpha)/m\), for \(0\le j<m\). Define \(D_m=(2\pi i m)^{-1}d/dx\) and the measurement map
\[
\mathcal H_{m,\alpha,t}c=\frac1{\sqrt m}\bigl( (f(j/m))_{j=0}^{m-1},\ (tD_mf((j+\alpha)/m))_{j=0}^{m-1}\bigr),\quad t>0.
\]
Over all weights \(t>0\) and shifts \(\alpha\in\mathbb R/\mathbb Z\), the sharp smallest possible spectral condition number is
\[
\boxed{\inf_{\alpha,t}\kappa_2(\mathcal H_{m,\alpha,t})=1+\sqrt2.}
\]
The weight of every minimizer is uniquely \(t=\sqrt2\). For \(m\ge2\), the complete set of optimal shifts is exactly
\[
\boxed{\sin^2(\pi\alpha)\le1-\frac1{\sqrt2}.}
\]
For \(m=1\), all shifts are optimal at that weight. Thus a nonzero, grid-size-independent interval of derivative-grid staggering has *no worst-case conditioning penalty*. At either critical shift \(\sin^2(\pi\alpha)=1-1/\sqrt2\), every two-frequency Fourier fiber has the identical least squared singular value \(2-\sqrt2\), giving a frequency-flat lower spectral band.

For \(m\ge2\), set \(u_m=\lfloor m^2/4\rfloor/m^2\), \(q=\sin^2(\pi\alpha)\), and
\[
\tau_m=4(1-u_m),\quad \Delta_m=2(1-4u_mq),\quad L_m=\frac{\tau_m-\sqrt{\tau_m^2-4\Delta_m}}2.
\]
At the optimal weight, the *complete all-shift* condition formula is
\[
\boxed{\kappa_2(\mathcal H_{m,\alpha,\sqrt2})=\sqrt{\frac{2+\sqrt2}{\min\{2-\sqrt2,L_m\}}}.}
\]
All sampling maps with \(t>0\) are invertible except when \(m\) is even and \(\alpha\equiv1/2\pmod1\); then the kernel has dimension exactly one. At the half-grid shift for odd \(m\), the optimal-weight condition number satisfies
\[
\kappa_2(\mathcal H_{m,1/2,\sqrt2})\sim m\sqrt{\frac{3(2+\sqrt2)}2}\qquad(m\to\infty\text{ through odd integers}).
\]

## Assumptions and scope

All frequencies, sample locations, derivative normalizations, and norms are exactly as displayed. The two data banks have equal total sampling weight before the tunable derivative gain \(t\); there are \(2m\) Fourier unknowns and \(2m\) complex measurements. Derivatives are measured at a *common* shift relative to the value grid. Singular values are those of the complex Euclidean linear map, not of the real-part projection. The condition number of a singular matrix is infinite. The formula for \(m=1\) is included separately because there is no nonzero Fourier-residue pair to constrain the shift.

## Proof

**1. Complete Fourier-fiber decomposition.** Apply a unitary \(m\)-point DFT to each measurement bank and permute the coefficient coordinates into the pairs \((k,k-m)\), \(0\le k<m\). This turns the measurement map into the orthogonal direct sum of \(2\times2\) blocks, up to unitary row and column phases,
\[
M_{s,\alpha,t}=\begin{pmatrix}1&1\\ts&t(s-1)e^{-2\pi i\alpha}\end{pmatrix},\qquad s=k/m.
\]
Let \(u=s(1-s)\), \(q=\sin^2(\pi\alpha)\). Direct calculation gives the trace and determinant of the positive Gram matrix:
\[
\operatorname{tr}(M^*M)=2+t^2(1-2u),\qquad\det(M^*M)=t^2(1-4uq).
\]
The two squared singular values are therefore the roots of \(z^2-[2+t^2(1-2u)]z+t^2(1-4uq)=0\). This also proves the complete finite spectrum, not just the extrema.

**2. Universal sharp bound and optimal weight.** Every grid includes \(k=0\), hence \(u=0\). Its trace is \(2+t^2\), determinant \(t^2\), independent of shift. The ratio of its two singular values is minimized uniquely when \(t^2=2\): indeed maximizing \(t^2/(2+t^2)^2\) is equivalent to setting \(t^2=2\). At that weight the squared singular values of the zero-residue block are \(L_0=2-\sqrt2\) and \(U_0=2+\sqrt2\), so the full matrix has condition number at least \(\sqrt{U_0/L_0}=1+\sqrt2\), with equality only possible at \(t=\sqrt2\).

**3. Largest singular value and exact shift threshold.** At \(t=\sqrt2\), write \(\tau(u)=4-4u\), \(\Delta(u)=2-8qu\), and \(F_u(z)=z^2-\tau(u)z+\Delta(u)\). Since \(F_0(L_0)=F_0(U_0)=0\),
\[
F_u(L_0)=4u(L_0-2q),\qquad F_u(U_0)=4u(U_0-2q).
\]
For \(0\le u\le1/4\), the greater root of \(F_u\) lies above \(\tau(u)/2\), which is at most \(2\); because \(U_0>2\) and \(F_u(U_0)>0\), the greater root is at most \(U_0\). Thus the *global* largest squared singular value is always \(U_0\), attained in the zero-residue block.

The smaller root lies below \(\tau(u)/2\), while \(\tau(u)/2\ge3/2>L_0\); hence the sign of \(F_u(L_0)\) decides whether that smaller root is at least \(L_0\). If \(m\ge2\), at least one block has \(u>0\), and all lower roots are at least \(L_0\) precisely when \(q\le L_0/2=1-1/\sqrt2\). For \(q=L_0/2\), \(F_u(L_0)=0\) for every fiber, making the lower squared singular-value band exactly flat. This proves the complete optimizer classification.

**4. Full all-shift formula.** When \(q>L_0/2\), the smaller root decreases strictly as \(u\) increases: implicit differentiation gives
\[
\frac{d\lambda_-(u)}{du}=\frac{-4\lambda_-(u)+8q}{2\lambda_-(u)-\tau(u)}<0,
\]
because it starts below \(2q\) and the numerator remains positive while the denominator is negative. When \(q\le L_0/2\), all smaller roots are at least \(L_0\). The largest sampled \(u\) equals \(u_m=\lfloor m^2/4\rfloor/m^2\). Substituting it into the quadratic equation gives exactly the displayed global condition formula.

**5. Singularities and parity asymptotics.** The Gram determinant vanishes precisely if \(q=1\) and \(u=1/4\), since \(0\le q\le1\), \(0\le u\le1/4\). The second condition occurs at exactly one residue \(k=m/2\) when \(m\) is even. Consequently there is exactly one null singular direction in that case, while every odd-grid matrix is nonsingular for every shift. At \(q=1\) for odd \(m\), \(u_m=(m^2-1)/(4m^2)\), so \(\tau_m=3+m^{-2}\), \(\Delta_m=2m^{-2}\), and \(L_m\sim2/(3m^2)\), yielding the stated sharp linear condition-number asymptotic.

## Verification

The accompanying `hermite_shift_check.py` independently constructs each full complex \(2m\times2m\) Fourier–Hermite matrix, without using the fiber construction, for \(1\le m\le32\), a range of shifts and four derivative gains. It compares all full-matrix singular values with the derived fiber spectra and checks the exact optimum, condition formula, parity singularity, and sharp phase boundary. It reports `HERMITE_SHIFT_CHECKS_PASS 1791` under Python with NumPy. These finite comparisons validate implementation and boundary examples; the all-size conclusions are analytical.

## Relationship to prior work

Yu and Townsend (arXiv:2202.04722, initially posted 2022-02-09) analyze stability of **value-only** trigonometric interpolation on perturbed grids, proving discrete Kadec-type bounds. The present data comprise simultaneous value and frequency-normalized derivative banks, with a common relative shift, and the claim is an exact all-dimension optimal-condition plateau and rank classification. Kunis and Nagel (2020) study rectangular Fourier–Vandermonde matrices for *distinct near-colliding value nodes*; their estimates do not specialize to the displayed confluent derivative blocks. Fageot, Aziznejad, Unser, and Uhlmann (2019) study Hermite **spline** approximation and support, rather than finite bandlimited Fourier interpolation or the discrete frequency-flat boundary. Standard DFT aliasing itself is known; the contribution is the exact minimax design and complete sharp phase region in this particular mixed measurement model.

## Limitations

The condition number measures coefficient recovery from Euclidean errors after the displayed derivative normalization. It does not equate physical error variances of value and derivative sensors. The all-shift exact condition formula is proved at the optimal derivative gain; for other gains the explicit fiber spectrum remains valid but no further global closed-form expression is asserted. The model assumes a common rigid shift and a consecutive asymmetric band of \(2m\) frequencies. No claim of priority over uninspected historical results on confluent Fourier matrices or general Hermite frame theory is made.

## References

- A. Yu and A. Townsend, *On the stability of unevenly spaced samples for interpolation and quadrature*, arXiv:2202.04722, v1 posted 2022-02-09, https://arxiv.org/pdf/2202.04722.
- S. Kunis and D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, Numerical Algorithms 87 (2021), 473–496, first published 2020-07-21, https://doi.org/10.1007/s11075-020-00974-x.
- J. Fageot, S. Aziznejad, M. Unser, and V. Uhlmann, *Support and Approximation Properties of Hermite Splines*, arXiv:1902.02565, v1 posted 2019-02-07, https://arxiv.org/abs/1902.02565.
