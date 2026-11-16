# Exact optimal taper and quadratic conditioning for a cyclic exponential Gabor basis

## Finding

Let \(m\ge2\) be an integer, \(N=2m\), and let the positive circular exponential window be
\[
g_r(j)=r^{d_N(j)},\qquad d_N(j)=\min\{j,N-j\},\quad 0\le j<N,\quad 0<r<1.
\]
Use the two adjacent cyclic translations and the full index-two modulation subgroup to construct the critical Gabor family
\[
\mathcal G_m(r)=\{M_{2a}T_k g_r:0\le a<m,\ k\in\{0,1\}\}\subset\mathbb C^{2m}.
\]

**Theorem.** This family is a Riesz basis for every \(m\ge2\) and \(0<r<1\). Put
\[
T=(1+r^2)(1+r^{2m-2}),\qquad D=r^{2m-2}(1-r^2)^2.
\]
Its exact sharp lower and upper frame bounds are
\[
\boxed{A_m(r)=\frac m2\bigl(T-\sqrt{T^2-4D}\bigr),\qquad
B_m(r)=\frac m2\bigl(T+\sqrt{T^2-4D}\bigr).}
\]
There is exactly one taper minimizing the **frame-operator** condition number \(\kappa_m(r)=B_m(r)/A_m(r)\) on \((0,1)\). Writing \(r_m=e^{-s_m}\), the minimizer is the unique \(s_m>0\) satisfying
\[
\boxed{(m-1)\tanh((m-1)s_m)\sinh(2s_m)=2.}
\]
If \(z_*>0\) is the unique root of \(z_*\tanh z_*=1\), then
\[
\boxed{(m-1)s_m\longrightarrow z_*,\qquad
\min_{0<r<1}\kappa_m(r)\sim\frac{4}{z_*^2-1}(m-1)^2.}
\]
Here \(z_*=1.1996786402577\ldots\) and \(4/(z_*^2-1)=9.1068701249123\ldots\). In the smallest admissible dimension \(m=2\), the optimizer is \(r_2=\sqrt2-1\), with optimal condition number \((2+\sqrt3)^2\).

## Assumptions and scope

The coordinates of \(\mathbb C^N\) are indexed modulo \(N\). The Hermitian norm is the usual coordinatewise Euclidean norm, without normalizing \(g_r\). Translation and modulation conventions are
\[
(T_k f)(j)=f(j-k\bmod N),\quad
(M_\ell f)(j)=e^{2\pi i\ell j/N}f(j).
\]
There are exactly \(2m=N\) Gabor atoms, and frame bounds mean the best constants in
\[
A\|f\|_2^2\le\sum_{k=0}^1\sum_{a=0}^{m-1}|\langle f,M_{2a}T_k g_r\rangle|^2\le B\|f\|_2^2
\quad(f\in\mathbb C^N).
\]
The ratio \(B/A\) is the condition number of the positive frame operator; the singular-value condition number of the synthesis matrix is its square root. The optimizer and asymptotic claim refer only to this fixed sampling geometry and to the one-parameter positive circular exponential family.

## Proof

**1. Paired-coordinate block reduction.** Write \(S\) for the frame operator. Fourier orthogonality gives
\[
\sum_{a=0}^{m-1}e^{2\pi i(2a)(j-h)/N}
=\begin{cases}m,&j\equiv h\pmod m,\\0,&\text{otherwise}.\end{cases}
\]
Consequently, \(S\) is a direct sum of \(m\) real symmetric \(2\times2\) blocks on \(\operatorname{span}\{e_j,e_{j+m}\}\), \(j=0,\ldots,m-1\). For \(1\le j<m\), the block divided by \(m\) is
\[
Q_j=\begin{pmatrix}
(1+r^2)r^{2j-2}&2r^m\\
2r^m&(1+r^2)r^{2m-2j}
\end{pmatrix}.
\]
The block \(Q_0\) is identical to \(Q_1\). To check the displayed formula directly, the two translation-vectors on the coordinate pair \((j,j+m)\) are \((r^j,r^{m-j})\) and \((r^{j-1},r^{m-j+1})\) for \(1\le j<m\), giving \(Q_j=uu^*+vv^*\). At \(j=0\), they are \((1,r^m)\) and \((r,r^{m-1})\), giving the same block as at \(j=1\).

**2. Sharp bounds and invertibility.** Every block has the same determinant
\[
\det Q_j=r^{2m-2}\bigl((1+r^2)^2-4r^2\bigr)=D>0,
\]
and positive diagonal entries, so every \(Q_j\) is positive definite. The system has exactly \(N\) independent atoms, hence is a Riesz basis. For \(j\ge1\), its trace is
\[
T_j=(1+r^2)\bigl(r^{2j-2}+r^{2m-2j}\bigr).
\]
As a function of real \(j\), the parenthesized expression is strictly convex. Its maximum over integer \(1\le j<m\) must therefore occur at an endpoint. Moreover
\[
\bigl(1+r^{2m-2}\bigr)-\bigl(r^2+r^{2m-4}\bigr)
=(1-r^2)(1-r^{2m-4})\ge0.
\]
Thus the maximal trace is \(T=T_1=T_0\). For a positive \(2\times2\) matrix with fixed determinant \(D\), the larger eigenvalue increases strictly and the smaller decreases strictly with the trace. The extremal eigenvalues of \(Q_1\), multiplied by \(m\), therefore give exactly the asserted \(A_m(r)\) and \(B_m(r)\), with equality realized by their eigenvectors supported on one coordinate pair.

**3. Unique optimal taper.** Let \(a=m-1\) and \(r=e^{-s}\), \(s>0\). Since \(D>0\), let \(X=T/\sqrt D>2\). Exact algebra gives
\[
X(s)=2\coth s\,\cosh(as).
\]
The condition number is
\[
\kappa_m(s)=\left(\frac{X(s)+\sqrt{X(s)^2-4}}2\right)^2,
\]
a strictly increasing function of \(X>2\). Hence minimizing \(\kappa_m\) is equivalent to minimizing \(\log X\). Differentiation yields
\[
\frac{d}{ds}\log X=a\tanh(as)-\frac{2}{\sinh(2s)}.
\]
The first term is strictly increasing in \(s\) from zero, and the second is strictly decreasing from infinity to zero. Therefore the derivative has exactly one zero, changes sign from negative to positive there, and defines the unique global minimum. Its zero equation is the boxed taper condition. Neither endpoint is optimal, because \(X(s)\to\infty\) both as \(s\downarrow0\) and \(s\to\infty\).

**4. Sharp large-dimension law.** Put \(z_a=as_m\), with \(a=m-1\). The optimizing equation is
\[
a\tanh(z_a)\sinh(2z_a/a)=2.
\]
The function on the left is strictly increasing in \(z_a>0\). Let \(z_*>0\) solve \(z_*\tanh z_*=1\), uniquely, since \(z\tanh z\) rises strictly from zero to infinity. For any fixed \(z>0\),
\[
a\tanh z\,\sinh(2z/a)\longrightarrow2z\tanh z.
\]
Comparison at \(z_*\pm\varepsilon\) and monotonicity imply \(z_a\to z_*\). As \(a\to\infty\), \(X(s_m)/a\to2\cosh z_*/z_*\). Since \(\kappa_m/X^2\to1\) as \(X\to\infty\),
\[
\frac{\kappa_m(r_m)}{a^2}\longrightarrow
\frac{4\cosh^2z_*}{z_*^2}=
\frac4{z_*^2-1},
\]
where the last identity uses \(\tanh z_*=1/z_*\). This proves the sharp constant and completes the proof.

## Verification

The included standalone `CHECK.py` uses the Python standard library. It checks the determinant and maximal-trace certificates exactly with rational arithmetic for \(44\) parameter combinations, separately assembles the complete complex Gabor synthesis matrix for \(44\) further cases and compares every frame-operator entry with the claimed blocks, then checks the stationary equation and minimizing behavior numerically at ten dimensions. It also verifies the \(m=2\) radical special case and convergence of the normalized condition number to the stated constant. Run `python3 CHECK.py` from the extracted package. Finite computation is supplementary: the proof above establishes all infinite claims.

## Relationship to prior work

Asipchuk, De Carli and Rodriguez prove general block-equivalence of finite Gabor frames whenever one index set is a subgroup. Their structural theorem applies here but does not compute the exact bounds for the circular graph-distance exponential window or optimize its taper across all cyclic orders. The present proof uses a direct specialization of that standard block mechanism; novelty is asserted only for the resulting **sharp positive-window design theorem**, not the decomposition itself.

A published finite cyclic phase-alphabet classification treats the same two-translation/even-modulation geometry for flat, phase-only orthonormal windows. The present exponentially decaying positive window is nonflat and cannot be tight; the quantitative unique optimum and sharp quadratic conditioning law address another question. Faulhuber and Shafkulovska study condition-number optimization for continuous two-sided exponentials over integer-oversampled lattices, not the finite graph-distance window at critical cyclic sampling. Their work contains related hyperbolic-function analysis; the elementary equation for the limiting constant is **not itself** claimed as new. The combination of an exact all-size finite spectrum, unique taper, and quadratic limit was not located in the checked sources.

## Limitations

This result is restricted to the two consecutive translations, the index-two modulation subgroup, the circular graph-distance exponential family, and the finite-dimensional standard Hermitian norm. It does not optimize over arbitrary windows, phases, alternate sampling lattices or other localization penalties. A known general polyphase formula could imply the finite block structure; an older equivalent optimized exponential-window calculation might still exist under different terminology. There is no independent audit, and numerical tests alone do not certify the theorem.

## References

1. O. Asipchuk, L. De Carli and L. Rodriguez, *Block-equivalent finite Gabor frames*, arXiv:2605.16139, first public version May 15, 2026; see Theorem 1.1, Corollary 5.1 and Sections 3–5. https://arxiv.org/html/2605.16139v2
2. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (2022), published in *Applied and Computational Harmonic Analysis* 67 (2023); especially Sections 2.4 and 9. https://arxiv.org/abs/2204.02917
3. *A phase-alphabet trichotomy for critical two-translation cyclic Gabor bases*, publicly available manuscript (2026), especially the exact phase-only orthonormality criterion. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-phase-alphabet-trichotomy-for-critical-two-translation-cyclic--740628e0639c
