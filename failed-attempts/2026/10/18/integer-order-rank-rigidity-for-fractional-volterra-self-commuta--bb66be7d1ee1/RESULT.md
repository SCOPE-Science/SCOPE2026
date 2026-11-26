# Integer-order rank rigidity for fractional Volterra self-commutators

## Finding

On the complex Hilbert space \(H=L^2(0,1)\), let \(T_\alpha\) be the left Riemann–Liouville integral of real order \(\alpha>1/2\), and form its self-commutator \(K_\alpha=T_\alpha T_\alpha^*-T_\alpha^*T_\alpha\). Its rank and positive/negative spectral inertia are classified by the following dichotomy:

\[
\begin{array}{c|c|c}
\alpha & \operatorname{rank} K_\alpha & (n_+(K_\alpha),n_-(K_\alpha))\\ \hline
m\in\{1,2,3,\ldots\} & 2m &(m,m)\\
\alpha\notin\mathbb N &\infty &(\infty,\infty).
\end{array}
\]

Here \(n_\pm\) count strictly positive and negative eigenvalues with multiplicity. For every admissible order the compact self-adjoint operator \(K_\alpha\) is trace class, satisfies \(\operatorname{tr}K_\alpha=0\), and has a spectrum symmetric about zero, including multiplicities. Thus an arbitrarily small noninteger change of integration order changes a finite-rank, finite-inertia defect into an infinite-rank defect with infinitely many eigenvalues of each sign.

## Assumptions and scope

For each fixed real \(\alpha>1/2\), set
\[
(T_\alpha f)(x)=\frac{1}{\Gamma(\alpha)}\int_0^x(x-t)^{\alpha-1}f(t)\,dt,
\qquad f\in L^2(0,1).
\]
The adjoint is the right-sided integral
\[
(T_\alpha^*f)(x)=\frac{1}{\Gamma(\alpha)}\int_x^1(t-x)^{\alpha-1}f(t)\,dt.
\]
No endpoint boundary conditions are imposed on \(f\). The order threshold \(\alpha>1/2\) guarantees that these integral operators are Hilbert–Schmidt; no rank classification is asserted here at or below that threshold. Rank means Hilbert-space operator rank, and a positive/negative inertia of \(\infty\) means infinitely many nonzero eigenvalues of that sign counted with multiplicity.

## Proof

**1. Trace class and reflection pairing.** The integral kernel gives
\[
\|T_\alpha\|_{S_2}^2
=\frac{1}{\Gamma(\alpha)^2}\int_0^1\int_0^x(x-t)^{2\alpha-2}\,dt\,dx
=\frac{1}{2\alpha(2\alpha-1)\Gamma(\alpha)^2}.
\]
Therefore both products in \(K_\alpha\) are trace class and have the same trace. Let \((Rf)(x)=f(1-x)\), a unitary involution. Substitution yields \(RT_\alpha R=T_\alpha^*\), hence \(RK_\alpha R=-K_\alpha\). The compact self-adjoint spectral theorem pairs every positive eigenvalue with its negative, with identical multiplicity; trace is zero.

**2. Integer orders have polynomial range.** For \(m\in\mathbb N\), \(T_m=J^m\), where \(Jf(x)=\int_0^x f(t)\,dt\). Put \(A=J^mJ^{*m}\), \(B=J^{*m}J^m\). Their weak derivatives satisfy
\[
D^{2m}Af=(-1)^m f=D^{2m}Bf\quad(f\in H).
\]
Consequently \(D^{2m}K_mf=0\), so \(K_mH\) lies in the \(2m\)-dimensional space \(\mathcal P_{2m-1}\) of polynomials of degree at most \(2m-1\). To show that this upper bound is attained, suppose \(p\in\mathcal P_{2m-1}\) and \(K_mp=0\). Then \(g=Ap=Bp\). As \(g=J^mJ^{*m}p\), its derivatives of orders \(0,\ldots,m-1\) vanish at zero, and its derivatives of orders \(m,\ldots,2m-1\) vanish at one. As \(g=J^{*m}J^mp\), the corresponding derivatives of orders \(0,\ldots,m-1\) vanish at one, and those of orders \(m,\ldots,2m-1\) vanish at zero. Thus all derivatives of orders \(0,\ldots,2m-1\) vanish at both endpoints.

Meanwhile, \(g^{(2m)}=(-1)^mp\), so \(g\) is a polynomial of degree at most \(4m-1\). Vanishing of the first \(2m\) endpoint jets forces divisibility by \(x^{2m}(1-x)^{2m}\), impossible for a nonzero polynomial of degree below \(4m\). Therefore \(g=0\) and \(p=0\). The restriction of \(K_m\) to \(\mathcal P_{2m-1}\) is injective. Since its range is contained in that same finite-dimensional space, \(\operatorname{rank}K_m=2m\). Reflection pairing then gives precisely \(m\) positive and \(m\) negative eigenvalues.

**3. Noninteger orders have infinitely many independent kernel sections.** The continuous integral kernel of \(K_\alpha\), for \(0<x<y<1\), is
\[
\begin{aligned}
k_\alpha(x,y)=\frac1{\Gamma(\alpha)^2}\bigg[&\int_0^x(x-t)^{\alpha-1}(y-t)^{\alpha-1}\,dt\\
&-\int_y^1(t-x)^{\alpha-1}(t-y)^{\alpha-1}\,dt\bigg].
\end{aligned}
\]
For fixed \(y>0\), the second integral is a real-analytic function of \(x\) near zero. The first integral has, for \(0<x<y\), an absolutely convergent expansion
\[
\int_0^x(x-t)^{\alpha-1}(y-t)^{\alpha-1}\,dt
=x^\alpha\sum_{\ell=0}^\infty c_\ell(\alpha)y^{\alpha-1-\ell}x^\ell,
\]
where
\[
c_\ell(\alpha)=(-1)^\ell\binom{\alpha-1}{\ell}B(\ell+1,\alpha).
\]
If \(\alpha>1/2\) is not an integer, every coefficient \(c_\ell(\alpha)\) is nonzero. Suppose that \(y_1,\ldots,y_N\) are distinct interior points and
\(\sum_{j=1}^N a_jk_\alpha(x,y_j)=0\) for all sufficiently small positive \(x\). This equates an ordinary analytic function to \(x^\alpha\) times an ordinary analytic function. Since \(\alpha\notin\mathbb N\), comparison of the first nonvanishing integer and noninteger exponents forces each analytic part to vanish identically. Equating the coefficients of the fractional-power series gives
\[
\sum_{j=1}^N a_j y_j^{\alpha-1-\ell}=0,
\qquad \ell=0,\ldots,N-1.
\]
After factoring \(y_j^{\alpha-1}\) from column \(j\), this is a Vandermonde system in the distinct numbers \(1/y_j\). Thus every \(a_j=0\).

It follows that arbitrarily many distinct kernel sections \(k_\alpha(\cdot,y_j)\) are linearly independent. If a continuous-kernel integral operator had finite rank \(r\), its kernel sections would all lie in the same \(r\)-dimensional subspace of \(L^2(0,1)\): the almost-everywhere finite-rank representation extends to each interior \(y\) by continuity of the section map. Hence \(K_\alpha\) has infinite rank. Reflection pairing from Step 1 then forces infinitely many positive and infinitely many negative eigenvalues, completing the classification.

## Verification

A standalone standard-library program `volterra_selfcommutator_check.py` reproduces \(948\) finite exact-rational identities and numerical coefficient-nonvanishing checks. For integer orders \(m=1,\ldots,6\), it expands the two composite integral kernels independently, verifies equality with the oriented polynomial formula, checks kernel symmetry and reflection antisymmetry on rational grids, and exhibits full-rank \(2m\)-by-\(2m\) rational evaluation matrices. It also verifies nonzero fractional-series coefficients for five noninteger sample orders. These finite checks support the proof but do not substitute for the arbitrary-order analytic argument or the infinite-rank conclusion.

## Relationship to prior work

The established singular-value/boundary-value theory of polynomial Volterra operators [1] concerns \(\varphi(J)^*\varphi(J)\), not the difference of two positive products. The later direct study of self-commutators [2] computes norms for \(J\) and \(J^2\), which are **covered special cases** of the integer-order part here; they are not asserted to be new. The study of real and imaginary parts of integer Volterra powers [3] proves that one of those parts has finite rank at each integer order; by the algebraic commutator identity this already implies the **upper bound** \(\operatorname{rank}K_m\le 2m\). What is added is equality, the complete inertia and, principally, the sharp **finite-rank iff integer** dichotomy throughout the Hilbert–Schmidt Riemann–Liouville semigroup.

The study of the Volterra-generated algebra and its commutation properties [4] is particularly close in terminology but its accessible abstract addresses generated ideals and commutants, rather than a fractional-order rank classification. Its full text was not accessible for comprehensive comparison. Standard fractional-integral operator definitions and compactness properties appear in [5]. Claims of absolute first priority are not made.

## Limitations

The result is restricted to real integration orders strictly above \(1/2\), not general fractional convolution kernels or endpoint orders. It classifies rank and spectral inertia, not the magnitudes, multiplicities beyond sign pairing, or asymptotic decay of individual nonzero eigenvalues. The full text of [4] was not available during comparison, and equivalent results in unindexed sources remain a bibliographic risk. No independent verification has been performed.

## References

[1] Y. Lyubich and D. Tsedenbayar, *The norms and singular numbers of polynomials of the classical Volterra operator in \(L^2(0,1)\)*, Studia Mathematica 199 (2010), 171–184. DOI: 10.4064/sm199-2-3. Open full text: https://www.impan.pl/shop/en/publication/transaction/download/product/90183.

[2] L. Khadkhuu and D. Tsedenbayar, *A note on self-commutators of Volterra operator and its square*, Journal of Applied Science and Engineering A 3 (2022), 11–16. DOI: 10.5564/jasea.v3i1.2455. Open full text: https://www.mongoliajol.info/index.php/JASE-A/article/download/2455/2632.

[3] T. Ransford and D. Tsedenbayar, *On the real and imaginary parts of powers of the Volterra operator* (2024). arXiv:2402.09287. Full text: https://arxiv.org/html/2402.09287v1.

[4] A. F. M. ter Elst, M. Sauter and J. Zemánek, *Generation and commutation properties of the Volterra operator*, Archiv der Mathematik 99 (2012), 467–479. DOI: 10.1007/s00013-012-0444-5 (publicly dated 2012-11-16).

[5] M. A. Lifshits and W. Linde, *Fractional integration operators of variable order: continuity and compactness properties* (2012). arXiv:1211.3826. Full text: https://arxiv.org/abs/1211.3826.
