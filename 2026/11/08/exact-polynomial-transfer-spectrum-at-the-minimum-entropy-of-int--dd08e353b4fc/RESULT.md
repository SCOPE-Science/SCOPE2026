# Exact polynomial transfer spectrum at the minimum entropy of interval transitivity

## Finding
Consider the continuous piecewise-affine interval map
\[
g(x)=\begin{cases}
\frac12+2x,&0\le x\le\frac14,\\
\frac32-2x,&\frac14\le x\le\frac12,\\
1-x,&\frac12\le x\le1.
\end{cases}
\]
This is a canonical two-half interval construction attaining transitive interval entropy \(\frac12\log2\). Its Lebesgue Frobenius--Perron operator \(\mathcal L\) leaves invariant every finite-dimensional space \(\mathcal P_d\) of pairs of polynomials, each of degree at most \(d\), on the halves \([0,\frac12]\) and \([\frac12,1]\). For **every integer \(d\ge0\)**,
\[
\boxed{\det(\lambda I-\mathcal L|_{\mathcal P_d})=\lambda^{2\lceil d/2\rceil}\prod_{k=0}^{\lfloor d/2\rfloor}(\lambda^2-4^{-k}).}
\]
Every nonzero eigenvalue \(\pm2^{-k}\) is simple, and the generalized zero eigenspace is the direct sum of exactly \(\lceil d/2\rceil\) Jordan blocks of size two (none when \(d=0\)). Consequently every polynomial-pair correlation after lag two is a **finite exact linear combination** of \((\pm2^{-k})^n\). In particular, for \(\phi(x)=x-\frac12\) and \(C_n=\int_0^1\phi(x)\phi(g^n(x))\,dx\),
\[
\boxed{C_0=\frac1{12},\quad C_1=-\frac7{96},\quad C_n=\frac{(-1)^n}{16}\quad(n\ge2).}
\]
Thus the smallest-entropy transitive interval construction has a persistent alternating mode despite its positive topological entropy; the polynomial transfer spectrum also has an explicitly determined finite-time nilpotent component.

## Assumptions and scope
Polynomial pairs are allowed to have a jump at the common half-interval boundary, which is immaterial to the Lebesgue transfer operator. We use \((\mathcal Lf)(y)=\sum_{g(x)=y}f(x)/|g'(x)|\) at almost every \(y\). The map is piecewise affine; all statements concern its canonical action on Lebesgue densities, not an operator spectrum on arbitrary Banach spaces. A correlation is \(C_n(f,h)=\int_0^1 f(x)h(g^n(x))\,dx=\int_0^1 (\mathcal L^nf)(x)h(x)\,dx\), for piecewise polynomials \(f,h\); for centered autocorrelation the mean is zero.

## Proof
Set \(I_L=[0,\frac12]\) and \(I_U=[\frac12,1]\). The left half maps by two branches onto the right half, each with absolute slope \(2\); the right half maps by reflection onto the left half with absolute slope \(1\). Thus for a polynomial pair \(f=(f_L,f_U)\),
\[
(\mathcal Lf)_L(y)=f_U(1-y),\qquad
(\mathcal Lf)_U(y)=\frac12\left[f_L\left(\frac{y-1/2}{2}\right)+f_L\left(\frac{3/2-y}{2}\right)\right].
\]
This proves invariance of \(\mathcal P_d\), and inserting \(f_L=f_U=1\) proves \(\mathcal L1=1\), hence invariance of Lebesgue probability. Write \(\mathcal L=\bigl(\begin{smallmatrix}0&A\\ B&0\end{smallmatrix}\bigr)\). Here \(A\) is the invertible reflection \(Af(y)=f(1-y)\), whereas \(B\) is symmetric-branch averaging. Squaring gives diagonal blocks \(AB\) and \(BA\).

On left-half polynomials the first diagonal block has the especially simple form
\[
(ABf)(y)=\frac12\left[f\left(\frac14-\frac y2\right)+f\left(\frac14+\frac y2\right)\right].
\]
Its image is precisely the span of \(1,y^2,\ldots,y^{2m}\), where \(m=\lfloor d/2\rfloor\). On that image, the monomial-degree filtration is preserved and the triangular diagonal is \(4^{-k}\), for \(k=0,\ldots,m\): the highest term of \((AB)y^{2k}\) is \(4^{-k}y^{2k}\). These values are distinct and nonzero. Since \(A\) is invertible and \(BA=A^{-1}(AB)A\), the two blocks of \(\mathcal L^2\) are similar, each diagonalizable with nonzero spectrum \(\{4^{-k}\}\) and semisimple zero of multiplicity \(d-m\). Consequently \(\mathcal L^2\) has \(4^{-k}\) with multiplicity two and semisimple zero with multiplicity \(2(d-m)\). Moreover, the block-off-diagonal structure makes the characteristic polynomial of \(\mathcal L\) even: its nonzero eigenvalues occur as the simple pairs \(\pm2^{-k}\). The rank of \(\mathcal L\) is \((d+1)+(m+1)\), so its kernel has dimension \(d-m\). The zero generalized eigenspace has dimension \(2(d-m)\) and \(\mathcal L^2=0\) there. Therefore it consists of exactly \(d-m=\lceil d/2\rceil\) Jordan blocks of size two, establishing the characteristic polynomial and complete Jordan statement.

For any \(f,h\in\mathcal P_d\), duality gives \(C_n(f,h)=\langle\mathcal L^nf,h\rangle\). The zero Jordan blocks vanish when \(n\ge2\), while all nonzero blocks are semisimple, yielding the exact exponential expansion.

To obtain the stated coordinate autocorrelation, let \(\phi(y)=y-\frac12\). Directly applying the two transfer branches gives
\[
(\mathcal L\phi)_L(y)=\frac12-y,\qquad (\mathcal L\phi)_U(y)=-\frac14.
\]
A second application gives \((\mathcal L^2\phi)_L=-\frac14\) and \((\mathcal L^2\phi)_U=\frac14\). This piecewise constant changes sign under every further application of \(\mathcal L\); hence \(\mathcal L^n\phi=(-1)^n(-\frac14,\frac14)\) for all \(n\ge2\). Integrating against \(\phi\) yields \(C_n=(-1)^n/16\). Direct integration gives \(C_0=1/12\) and \(C_1=-7/96\).

## Verification
The standalone exact-arithmetic program `artifacts/verify_polynomial_transfer.py` builds \(\mathcal L\) from the three affine branches in rational arithmetic, verifies its characteristic polynomial and kernel dimensions for every \(0\le d\le7\), and independently checks the one- and two-step coordinate correlations. It also checks the branch-exchange identity \(\mathcal L^2\phi=(-1/4,1/4)\). The infinite-dimensional family of polynomial identities is established by the symbolic triangular argument above, not by finite tests.

## Relationship to prior work
Vinod Kumar P B, *The entropy spectra of chaotic maps of an interval*, arXiv:2610.39443v1 (first posted 2026-10-29), establishes that the lower transitive/Devaney entropy \((\log2)/2\) is attainable using square-root constructions. Its construction provides the dynamical setting, but does not state this map's full degree-by-degree polynomial transfer spectrum, exact nilpotent Jordan index, or coordinate correlation sequence. The classical work of Yoshida, Mori, and Shigematsu (1983) treats power spectra and correlations of **a tent-map height family** at band splitting. It is directly relevant to the persistence of alternating statistical modes, so neither oscillatory correlations nor Frobenius--Perron analysis in general are claimed as new. The present result concerns the explicit three-branch reflection/tent square-root map and supplies an all-degree algebraic transfer spectrum; the available abstract of the classical paper does not resolve whether an equivalent formula has appeared in its full text. Priority is therefore provisional.

## Limitations
This is a polynomial-observable result on a specified Lebesgue transfer operator, not a full spectrum theorem for general function spaces. The nondecaying alternating component reflects the exchange of two invariant half-intervals under each iteration, so it does not imply mixing. Other transitive maps of minimal entropy need not have the same transfer spectrum. Comparison with the full 1983 tent-map paper remains incomplete, and independent scientific validation has not been performed.

## References
1. Vinod Kumar P B, *The entropy spectra of chaotic maps of an interval*, arXiv:2610.39443v1, posted 2026-10-29, https://arxiv.org/abs/2610.39443.
2. T. Yoshida, H. Mori, and H. Shigematsu, *Analytic study of chaos of the tent map: Band structures, power spectra, and critical behaviors*, Journal of Statistical Physics 31 (1983), 279--308, doi:10.1007/BF01011583.
