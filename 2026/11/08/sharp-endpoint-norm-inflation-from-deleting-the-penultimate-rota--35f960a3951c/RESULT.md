# Sharp endpoint-norm inflation from deleting the penultimate rotation-group Fourier block

## Finding
Let \(\Pi_j\) denote the Peter–Weyl projection onto **all matrix coefficients** of the irreducible spin-\(j\) representation of \(SO(3)\), of representation dimension \(2j+1\). For every integer \(L\geq2\), set
\[
S_L=\sum_{j=0}^{L}\Pi_j,\qquad T_L=S_L-\Pi_{L-1}.
\]
With Haar probability measure on \(SO(3)\), their sharp endpoint operator norms have the asymptotics
\[
\|S_L\|_{L^1\to L^1}=\|S_L\|_{L^\infty\to L^\infty}
=\frac4\pi(L+1)+O(\log(L+2)),
\]
\[
\|T_L\|_{L^1\to L^1}=\|T_L\|_{L^\infty\to L^\infty}
=\left(\frac4{3\pi}+\frac{8\sqrt3}{\pi^2}\right)(L+1)
+O(\log(L+2)).
\]
In particular, deleting a **single penultimate irreducible block** increases the sharp Fourier-projection norm by a linear amount:
\[
\lim_{L\to\infty}\frac{\|T_L\|}{\|S_L\|}=
\frac13+\frac{2\sqrt3}{\pi}>1,
\qquad
\lim_{L\to\infty}\frac{\|T_L\|-\|S_L\|}{L+1}
=\frac{8\sqrt3}{\pi^2}-\frac8{3\pi}>0.
\]
The ratio is approximately \(1.436\); the result is not a claim that the norm increases at every finite cutoff.

## Assumptions and scope
The group is \(SO(3)\), equivalently the center-invariant part of \(SU(2)\), with normalized Haar measure. For each nonnegative integer \(j\), \(\Pi_j\) projects onto the entire matrix-coefficient block of the unique \((2j+1)\)-dimensional irreducible representation, rather than onto its one-dimensional character span. The cutoff retains spins \(0,1,\ldots,L\) except spin \(L-1\). These are convolution operators on the full \(L^1\) or \(L^\infty\) space, not just on class functions. Every error bound is for integer \(L\to\infty\), with constants independent of \(L\).

## Proof
**1. Exact endpoint norms as central kernel integrals.** Parameterize conjugacy classes in \(SU(2)\) by \(0\le\theta\le\pi\), writing the spin-\(j\) character as
\[
\chi_j(\theta)=\frac{\sin((2j+1)\theta)}{\sin\theta}.
\]
Each \(\chi_j\) is invariant under the center, so this calculation descends to \(SO(3)\). Schur orthogonality gives the convolution kernels \(\sum_j(2j+1)\chi_j\) for the stated projections. For continuous central functions the normalized Weyl integration formula is
\[
\int_{SO(3)}F(g)\,dg=\frac2\pi\int_0^\pi
F(\theta)\sin^2\theta\,d\theta.
\]
The \(L^1\to L^1\) norm of convolution by an integrable kernel is precisely the kernel's \(L^1\)-mass: the upper bound is Young's inequality, while a nonnegative approximate identity gives the reverse bound. Duality gives the same \(L^\infty\to L^\infty\) norm. Thus for either projection it suffices to integrate the absolute value of its kernel with weight \(2\sin^2\theta/\pi\).

**2. Unpunctured trigonometric identity.** Let \(N=L+1\). Differentiating the finite sum
\[
\sum_{j=0}^L\cos((2j+1)\theta)=\frac{\sin(2N\theta)}{2\sin\theta}
\]
gives the *exact*, nonsingularly extendible identity, for \(0<\theta<\pi\),
\[
B_L(\theta):=\sin\theta\sum_{j=0}^L(2j+1)\sin((2j+1)\theta)
=-N\cos(2N\theta)+\frac12\cot\theta\sin(2N\theta).
\]
Since the convolution kernel times \(\sin^2\theta\) equals \(B_L(\theta)\),
\[
\|S_L\|=\frac2\pi\int_0^\pi|B_L(\theta)|\,d\theta.
\]
For every integer \(N\ge1\),
\[
\int_0^\pi|\cos(2N\theta)|\,d\theta=2.
\]
The error term satisfies
\[
\int_0^\pi|\cot\theta\sin(2N\theta)|\,d\theta
=O(\log(N+1)).
\]
Indeed, with \(d(\theta)=\min(\theta,\pi-\theta)\), use \(|\cot\theta|\le C/d(\theta)\) and \(|\sin(2N\theta)|\le\min(1,2Nd(\theta))\), and integrate separately over distances below and above \(N^{-1}\). The reverse triangle inequality establishes the first asymptotic.

**3. Exact penultimate-deletion identity.** Removing spin \(L-1\) changes the weighted kernel to
\[
\widetilde B_L(\theta)=B_L(\theta)
-(2L-1)\sin\theta\sin((2L-1)\theta).
\]
Use \(2\sin\theta\sin((2L-1)\theta)=\cos((2L-2)\theta)-\cos(2L\theta)\), then pair the frequencies \(2L+2\) and \(2L-2\). Rearrangement yields
\[
\boxed{\widetilde B_L(\theta)=
-N(2\cos2\theta-1)\cos(2L\theta)
+\frac12\cot\theta\sin(2N\theta)
+3\sin\theta\sin((2L-1)\theta).}
\]
The middle term has \(L^1(0,\pi)\) norm \(O(\log N)\) by Step 2; the final term has uniformly bounded \(L^1\) norm. Consequently,
\[
\|T_L\|=\frac{2N}{\pi}
\int_0^\pi |2\cos2\theta-1|\,|\cos(2L\theta)|\,d\theta
+O(\log N).
\]

**4. Sharp oscillatory average and constant.** For any fixed bounded-variation weight \(w\), the absolutely convergent cosine expansion of \(|\cos t|\), whose mean is \(2/\pi\) and whose nonconstant coefficients decay quadratically, gives
\[
\int_0^\pi w(\theta)|\cos(2L\theta)|\,d\theta
=\frac2\pi\int_0^\pi w(\theta)\,d\theta+O_w(L^{-1}).
\]
To see the remainder, integrate by parts (or in the Stieltjes sense) each nonconstant oscillatory mode against \(w\); its integral is \(O_w((kL)^{-1})\), summable over \(k\) with the Fourier coefficients. Take \(w(\theta)=|2\cos2\theta-1|\). Its sign changes at exactly \(\theta=\pi/6\) and \(5\pi/6\), and elementary integration gives
\[
\int_0^\pi w(\theta)\,d\theta=\frac\pi3+2\sqrt3.
\]
It follows that
\[
\|T_L\|=\frac{4N}{\pi^2}\left(\frac\pi3+2\sqrt3\right)+O(\log N),
\]
which is the second asymptotic. Dividing by the first asymptotic and subtracting proves both displayed limits. Finally, \(3\sqrt3>\pi\) ensures the limiting ratio exceeds one.

## Verification
The standalone `verify.py` recomputes the weighted convolution kernels directly from all the spin characters and from the two exact closed forms at 100 deterministic parameter points. It checks the elementary integral \(\pi/3+2\sqrt3\) using split quadrature, and independently integrates the absolute kernel for three increasing cutoffs. Run `python verify.py` in a Python environment with `sympy` and `mpmath`. These finite tests do **not** establish the asymptotic; the proof uses only the identities and estimates above.

## Relationship to prior work
Giulini and Travaglini (1986, DOI `10.1016/0022-1236(86)90059-5`) established matching growth **orders** for spherical and polyhedral Dirichlet kernels on compact semisimple Lie groups. Their full-text main theorem and proof discuss undisturbed spectral cutoffs; the paper does not state the present exact norm inflation under deletion of the penultimate spin block. Zhang (first arXiv submission May 23, 2020; `arxiv:2005.11451`) studies sharp \(L^p\) estimates for irreducible characters, Laplacian eigenfunctions, and Fourier restriction on compact Lie groups, rather than the endpoint norm of a one-block-punctured Fourier projection. Cowling, Martini, Müller, and Parcet (`arxiv:1807.04670`) analyze sharp/local Hausdorff–Young inequalities, not the stated spectral-mask endpoint comparison.

A previously published exact \(SU(2)\) all-highest-weight low-pass asymptotic (published-finding corpus `2026/10/11/SCOPE-exact-leading-constant-for-spherical-fourier-partial-sums-on-su--9a49e9fca04c`) gives \(8(L+1)/\pi^2\) for weights \(0\) through \(L\) without holes. Its main theorem and proof were inspected. Its spectral family includes **both parity classes** of \(SU(2)\) representations, whereas the present \(SO(3)\) family includes only even highest weights, and it does not remove an interior block. The numerical ratio \(1/3+2\sqrt3/\pi\) also occurs in a finite cyclic three-character projection result, but that abelian problem involves a different operator and is not an implication of it. Neither result supplies the present nonabelian punctured limit.

## Limitations
The result concerns one moving spectral gap: the penultimate spin block, and only endpoint \(L^1\) and \(L^\infty\) operator norms. It does not prove exact finite-\(L\) values, optimal remainder order, or monotonicity at every finite cutoff; it does not cover all deleted spins or multiple holes. Novelty is subject to a specialist-priority risk: Giacalone and Ricci, *Norms of Harmonic Projection Operators on Compact Lie Groups* (1988), DOI `10.1007/BF01474178`, is relevant by title, but its full text was not available for direct comparison. Its accessible description concerns harmonic projection norms, not an explicit moving-interior-hole asymptotic. No independence or external certification is claimed.

## References
1. S. Giulini and G. Travaglini, *Sharp Estimates for Lebesgue Constants on Compact Lie Groups*, Journal of Functional Analysis **68** (1986), 106–116, DOI `10.1016/0022-1236(86)90059-5`.
2. Y. Zhang, *On Fourier Restriction Type Problems on Compact Lie Groups*, first arXiv version May 23, 2020, `arxiv:2005.11451`, later Indiana University Mathematics Journal.
3. M. Cowling, A. Martini, D. Müller, and J. Parcet, *The Hausdorff–Young Inequality on Lie Groups*, `arxiv:1807.04670` (2018).
4. E. Giacalone and F. Ricci, *Norms of Harmonic Projection Operators on Compact Lie Groups*, Mathematische Annalen **280** (1988), 21–31, DOI `10.1007/BF01474178`.
5. *Exact leading constant for spherical Fourier partial sums on* \(SU(2)\), published research record `2026/10/11/SCOPE-exact-leading-constant-for-spherical-fourier-partial-sums-on-su--9a49e9fca04c`.
