# Cubic boundary commutator law and the sharp Schatten threshold in polyanalytic Bergman spaces

## Finding

For integer \(n\ge2\) and \(\alpha>-1\), the commutator of two bounded real radial Toeplitz operators on the weighted \(n\)-analytic Bergman space has a universal cubic spectral boundary law determined by the first two boundary derivatives of their scalar symbols. In contrast, for \(n=1\), all radial Toeplitz operators commute.

Write \(T_h=P_{n,\alpha}M_{h(|z|^2)}|_{\mathcal A^2_{n,\alpha}}\) and \(C=[T_h,T_k]\). Suppose \(h,k\) are real, bounded on \([0,1)\), and \(C^2\) on a neighborhood of \(1\). Set

\[
\Delta=h''(1)k'(1)-h'(1)k''(1),\qquad
c=\frac{|\Delta|}{2}n(n+\alpha)\sqrt{(n-1)(n-1+\alpha)}.
\]

**Theorem.** If \(\Delta\ne0\), then the singular values of \(C\), in decreasing order and repeated with multiplicity, obey

\[
\boxed{\lim_{m\to\infty}m^3s_m(C)=8c.}
\]

Consequently, for every \(p>0\),

\[
\boxed{C\in\mathcal S_p\quad\Longleftrightarrow\quad p>\frac13.}
\]

The asymptotic is caused by exactly two leading singular directions on each high positive angular-frequency block. On the remaining \(n-2\) directions the singular values are \(o(\xi^{-3})\).

The polynomial pair \(h(t)=t\), \(k(t)=t^2\) admits an exact stronger identity: every \(\xi\ge1\) positive-frequency block is a rank-two skew-symmetric matrix of operator norm \(b_{n,\xi}^2b_{n-1,\xi}\), where

\[
b_{j,\xi}=\frac{\sqrt{j(j+\alpha)(j+\xi)(j+\alpha+\xi)}}{(2j+\alpha+\xi)\sqrt{(2j+\alpha+\xi)^2-1}},\qquad j\ge1.
\]

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and endow it with the probability measure

\[
d\mu_\alpha(z)=\frac{\alpha+1}{\pi}(1-|z|^2)^\alpha\,dA(z),\qquad \alpha>-1.
\]

Let \(\mathcal A^2_{n,\alpha}\) be the closed subspace of \(L^2(\mu_\alpha)\) of \(n\)-analytic functions: \(\partial_{\bar z}^{n}f=0\). The orthogonal Bergman projection is \(P_{n,\alpha}\). The operators \(T_h\) above are bounded since \(h\in L^\infty\). The derivatives \(h'(1),h''(1)\) and their counterparts for \(k\) are one-sided derivatives with respect to \(t=|z|^2\), not with respect to \(|z|\).

For \(p>0\), \(\mathcal S_p\) consists of compact operators whose singular values are \(p\)-summable. There are only finitely many negative angular frequencies; they never influence the stated large-index asymptotic.

## Proof

**1. Exact angular decomposition.** The normalized disk-polynomial basis and radial Toeplitz matrix representation of Barrera-Castelán–Maximenko–Ramos-Vazquez give, for each \(\xi\ge0\), an \(n\)-dimensional angular block with entries

\[
A_\xi(h)_{jk}=\int_0^1h(t)q_{j,\xi}(t)q_{k,\xi}(t)t^\xi(1-t)^\alpha\,dt,
\qquad 0\le j,k<n,
\]

where \(q_{j,\xi}\) are real orthonormal shifted Jacobi polynomials with positive leading coefficients. The whole Toeplitz operator is the orthogonal direct sum of these blocks and finitely many negative-frequency blocks. In particular, the operator commutator decomposes into \(C_\xi=[A_\xi(h),A_\xi(k)]\).

**2. Jacobi multiplication and an exact boundary leakage identity.** In the full orthonormal polynomial basis indexed by \(j\ge0\), multiplication by \(t\) is a tridiagonal Jacobi matrix \(J_\xi\). Its off-diagonal entry between levels \(j-1\) and \(j\) equals the positive coefficient \(b_{j,\xi}\) displayed in the theorem (the factor \(1/2\) comes from shifting the ordinary Jacobi variable to \([0,1]\)). Let \(P\) project onto levels \(0,\ldots,n-1\), let \(B_\xi=PJ_\xi P\), and put \(E=e_{n-1}e_{n-1}^{*}\). Since tridiagonality permits exactly one excursion outside the compressed polynomial subspace,

\[
A_\xi(t^2)=PJ_\xi^2P=B_\xi^2+b_{n,\xi}^2E.
\]

Consequently,

\[
[A_\xi(t),A_\xi(t^2)]
=b_{n,\xi}^2b_{n-1,\xi}
(e_{n-2}e_{n-1}^{*}-e_{n-1}e_{n-2}^{*}).
\]

This identity proves the exact polynomial assertion, including its rank, both nonzero singular values, and norm. Since \(\xi b_{j,\xi}\to\sqrt{j(j+\alpha)}\) for each fixed \(j\), its norm has the sharp cubic limit

\[
\xi^3\|[A_\xi(t),A_\xi(t^2)]\|
\longrightarrow n(n+\alpha)\sqrt{(n-1)(n-1+\alpha)}.
\]

**3. The universal boundary jet.** Define the finite matrices

\[
M_\xi=\xi A_\xi(1-t),\qquad N_\xi=\xi^2 A_\xi((1-t)^2).
\]

The Jacobi recurrence gives \(M_\xi\to M\), where \(M\) is the Laguerre multiplication matrix on levels \(0,\ldots,n-1\), with diagonal \(M_{jj}=2j+\alpha+1\) and adjacent off-diagonal \(M_{j,j+1}=-\sqrt{(j+1)(j+\alpha+1)}\). The exact leakage formula gives

\[
N_\xi=M_\xi^2+\xi^2b_{n,\xi}^2E
\longrightarrow N=M^2+n(n+\alpha)E.
\]

For each fixed positive integer \(r\), repeated use of the tridiagonal Jacobi recurrence gives \(\|A_\xi((1-t)^r)\|=O(\xi^{-r})\): in any fixed number of recurrence steps near the first \(n\) indices, the entries of \(I-J_\xi\) are \(O(\xi^{-1})\). Its matrix elements for the first \(n\) Jacobi polynomials therefore have moments of every fixed order \(O(\xi^{-r})\). If \(h\) is bounded and \(C^2\) near \(1\), Taylor's formula and these moment bounds imply, in matrix norm,

\[
A_\xi(h)=h(1)I-\frac{h'(1)}{\xi}M_\xi
+\frac{h''(1)}{2\xi^2}N_\xi+o(\xi^{-2}).
\]

Indeed, on a sufficiently short terminal interval the Taylor remainder is at most \(\varepsilon(1-t)^2\), while on the remaining compact interval the third moment controls it by \(O(\xi^{-3})\). The same expansion holds for \(k\). Removing the scalar multiples of the identity before forming the commutator yields

\[
\xi^3 C_\xi\longrightarrow
\frac{\Delta}{2}[M,N]
=\frac{\Delta}{2}n(n+\alpha)[M,E].
\]

The matrix \([M,E]\) is supported on the \((n-2,n-1)\) and \((n-1,n-2)\) entries, with opposite signs and absolute entry \(\sqrt{(n-1)(n-1+\alpha)}\). Thus the limiting matrix has exactly two nonzero singular values, both equal to \(c\). This proves the block norm and rank-two limiting assertion.

**4. Global singular-value count.** Denote by \(N_C(u)\) the number of singular values of \(C\) exceeding \(u>0\). For every \(\varepsilon>0\), beyond some block index the two leading block singular values lie between \((c-\varepsilon)\xi^{-3}\) and \((c+\varepsilon)\xi^{-3}\), while each of the other \(n-2\) block singular values is at most \(\varepsilon\xi^{-3}\). The finitely many remaining blocks contribute \(O(1)\) to the counting function. Therefore, as \(u\downarrow0\),

\[
2(c-\varepsilon)^{1/3}
\le \liminf u^{1/3}N_C(u)
\le \limsup u^{1/3}N_C(u)
\le2(c+\varepsilon)^{1/3}+(n-2)\varepsilon^{1/3}.
\]

Let \(\varepsilon\downarrow0\). This gives \(N_C(u)\sim2c^{1/3}u^{-1/3}\), hence \(s_m(C)\sim8c/m^3\). The \(p\)-series criterion now gives \(C\in\mathcal S_p\) exactly when \(p>1/3\). The case \(n=1\) is diagonal on each angular subspace and thus all radial Toeplitz operators commute.

## Verification

The included `check.py` reconstructs normalized Jacobi polynomial blocks by independent Gaussian quadrature and checks their multiplication recurrence. It verifies the exact rank-two commutator identity for \(h(t)=t\), \(k(t)=t^2\), compares the asymptotic cubic constant at large \(\xi\), and tests a separate higher-degree polynomial pair. Its output is `POLY_BERGMAN_COMMUTATOR_CHECKS_PASS 228` and `POLY_BERGMAN_GENERAL_JETS_PASS 264` when run with Python, NumPy, and SciPy. These finite tests are supporting checks, not a proof of the infinite-frequency asymptotic or the Schatten classification; both follow from the preceding arguments.

## Relationship to prior work

Barrera-Castelán, Maximenko and Ramos-Vazquez (2020) construct the angular-frequency decomposition and exact Jacobi matrix representation; their 2023 continuation proves scalar convergence of high-frequency Toeplitz blocks and characterizes the generated operator algebra. Those results are the starting point here. They do not state the cubic rank-two commutator coefficient or its sharp global Schatten threshold. Rozenblum and Vasilevski (2018) develop the broader polyanalytic Bergman Toeplitz framework, including true-space reductions, without this quantitative radial commutator law. Čučković and Le (2010) study polyanalytic Toeplitz products with harmonic symbols; the nonconstant radial symbols here are not harmonic.

## Limitations

The order \(n\) and the weight \(\alpha\) remain fixed as the angular frequency tends to infinity. Symbols must be bounded and have a twice continuously differentiable boundary germ in the squared-radius variable. When \(\Delta=0\), the theorem establishes no sharp Schatten endpoint. No claim is made about nonsmooth symbols, arbitrary nonradial pairs, or joint limits in \(n\) and angular frequency. Historical priority beyond the inspected literature remains open to further specialist checking.

## References

1. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *C*-algebras generated by radial Toeplitz operators on polyanalytic weighted Bergman spaces* (2023), arXiv:2306.06231, Sections 2–4 and 11, especially formulas (19)–(22) and Proposition 4.2.
2. R. M. Barrera-Castelán, E. A. Maximenko, G. Ramos-Vazquez, *Radial operators on polyanalytic weighted Bergman spaces* (2020), arXiv:2009.14301, Sections 3 and 7.
3. G. Rozenblum, N. Vasilevski, *Toeplitz operators in polyanalytic Bergman type spaces* (2018), arXiv:1807.11216, Sections 2, 4 and 5.
4. Ž. Čučković, T. Le, *Toeplitz operators on Bergman spaces of polyanalytic functions* (2010), arXiv:1012.2816, Section 4.
