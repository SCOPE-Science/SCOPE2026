# Exact singular-value and beta laws for harmonic Bergman polynomial-calculus defects

## Finding

The harmonic Bergman Toeplitz quantization of analytic polynomials is not multiplicative. Its failure is finite-dimensional, has exactly computable rank for every polynomial, and has a universal limiting singular-value distribution along monomials of increasing degree.

Let \(B=T_z\). For any analytic polynomial \(p(z)=\sum_{k=0}^{d}a_kz^k\) with \(d\ge2\) and \(a_d\ne0\), define \(E_p=T_p-p(B)\). Then
\[\operatorname{rank}E_p=d-1,\qquad E_p^2=0.\]
For an integer \(m\ge2\), the entire nonzero singular spectrum of \(E_{z^m}\), counted with multiplicity, is
\[\gamma_{m,n}=\frac{n(m-n)}{(m+1)\sqrt{(n+1)(m-n+1)}},\quad 1\le n\le m-1.\]
Writing \(J_m=\lfloor m^2/4\rfloor\), the sharp operator norm is
\[\|E_{z^m}\|=\frac{J_m}{(m+1)\sqrt{J_m+m+1}},\qquad \lim_{m\to\infty}\|E_{z^m}\|=\tfrac12.\]
The empirical singular-value measures \(\mu_m=m^{-1}\sum_{n=1}^{m-1}\delta_{\gamma_{m,n}}\) converge weakly to the probability law with density
\[\rho(s)=\frac{4s}{\sqrt{1-4s^2}}\,\mathbf1_{(0,1/2)}(s).\]
Equivalently, for every fixed real \(q>0\),
\[\lim_{m\to\infty}\frac1m\sum_{n=1}^{m-1}\gamma_{m,n}^{q}=\operatorname B(1+q/2,1+q/2).\]
In particular, \(\lim_m m^{-1}\|E_{z^m}\|_1=\pi/8\) and \(\lim_m m^{-1/2}\|E_{z^m}\|_2=1/\sqrt6\).

## Assumptions and scope

Use the normalized planar area measure \(dA=\pi^{-1}\,dx\,dy\) on the open unit disk \(\mathbb D\). The Hilbert space \(h^2(\mathbb D)\) is the closed subspace of \(L^2(dA)\) of complex-valued harmonic functions. Denote its orthogonal projection by \(Q\). For bounded \(f\), let \(T_fh=Q(fh)\). The monomials \(e_j=\sqrt{j+1}\,z^j\) for nonnegative integers \(j\), and \(e_{-n}=\sqrt{n+1}\,\overline z^{n}\) for positive integers \(n\), form an orthonormal basis indexed by all integers. Operator powers and polynomials are understood as bounded-operator products; the nonzero singular values are the eigenvalues of \(|E|\) with multiplicity.

## Proof

**Step 1: the Toeplitz monomial shift.** Orthogonality of angular frequencies and the normalized radial moment \(\int_{\mathbb D}|z|^{2k}\,dA=1/(k+1)\) show that \(T_{z^m}e_j=c_{m,j}e_{j+m}\), where
\[c_{m,j}=\begin{cases}\sqrt{(j+1)/(j+m+1)},&j\ge0,\\ \sqrt{(1-j-m)/(1-j)},&j+m\le0,\\ \sqrt{(1-j)(j+m+1)}/(m+1),&j<0<j+m.\end{cases}\]
At the crossing endpoint \(j+m=0\), the second formula applies and agrees with direct projection onto the constant function. These cases exhaust all integer indices.

**Step 2: comparison with iteration.** Multiplying the degree-one coefficients telescopes on each pure analytic or anti-analytic side. In the crossing case \(j=-n\) with \(1\le n<m\), the product of the degree-one coefficients is \(1/\sqrt{(n+1)(m-n+1)}\). The direct monomial coefficient from Step 1 is \(\sqrt{(n+1)(m-n+1)}/(m+1)\). Their difference is
\[\frac{(n+1)(m-n+1)-(m+1)}{(m+1)\sqrt{(n+1)(m-n+1)}}=\frac{n(m-n)}{(m+1)\sqrt{(n+1)(m-n+1)}}.\]
Thus \(E_{z^m}\) vanishes on every basis vector except \(e_{-1},\ldots,e_{-(m-1)}\), which it maps separately to the orthogonal positive-frequency vectors \(e_{m-1},\ldots,e_1\). The displayed coefficients are therefore all its nonzero singular values, proving the exact singular-spectrum formula.

**Step 3: arbitrary polynomial and exact rank.** By linearity,
\[E_pe_{-n}=\sum_{\ell=1}^{d-n}\frac{a_{n+\ell}\,n\ell}{(n+\ell+1)\sqrt{(n+1)(\ell+1)}}e_\ell\quad (1\le n<d),\]
with \(E_pe_j=0\) for all \(j\ge0\) and all \(j\le-d\). The resulting \((d-1)\)-square matrix is zero beyond the reverse diagonal \(n+\ell=d\); on that diagonal every entry is a nonzero multiple of \(a_d\). Reversing the column order makes the matrix triangular with nonzero diagonal, hence invertible. This proves \(\operatorname{rank}E_p=d-1\). The range lies in positive frequencies, which the operator kills, so \(E_p^2=0\).

**Step 4: sharp norm.** For the monomial, set \(u=n(m-n)\). Because \((n+1)(m-n+1)=u+m+1\), its singular value is \(u/((m+1)\sqrt{u+m+1})\). This expression is strictly increasing for \(u\ge0\). The maximum integer value of \(n(m-n)\) is \(J_m=\lfloor m^2/4\rfloor\), giving the norm formula and its limit.

**Step 5: beta-law.** With \(t=n/m\), rewrite
\[\gamma_{m,n}=\frac{t(1-t)}{(1+1/m)\sqrt{(t+1/m)(1-t+1/m)}}.\]
For \(t\) in any closed subinterval of \((0,1)\) these functions converge uniformly to \(g(t)=\sqrt{t(1-t)}\); everywhere they satisfy \(0\le\gamma_{m,n}\le\sqrt{t(1-t)}\le1/2\). Splitting the Riemann sum into an interior and two arbitrarily short endpoint intervals gives, for every continuous function \(F\) on \([0,1/2]\),
\[\frac1m\sum_{n=1}^{m-1}F(\gamma_{m,n})\longrightarrow\int_0^1F(g(t))\,dt.\]
Thus the weak limit is the pushforward of uniform measure on \([0,1]\) by \(g\). Solving \(s^2=t(1-t)\) for its two inverse branches and differentiating yields \(\rho(s)=4s/\sqrt{1-4s^2}\) for \(0<s<1/2\). Taking \(F(s)=s^q\) gives \(\int_0^1t^{q/2}(1-t)^{q/2}\,dt=\operatorname B(1+q/2,1+q/2)\) for every \(q>0\). The trace and Hilbert–Schmidt asymptotics follow by choosing \(q=1,2\), respectively. No finite numerical test is used as a proof of the limit.

## Verification

The accompanying standard-library Python program `verify.py` independently evaluates the direct monomial Toeplitz coefficients and products of degree-one coefficients at 7,050 finite index/degree pairs; checks 264 complex-polynomial reverse-triangular blocks; and checks 20 exact norm/moment examples, for 7,334 diagnostics in total. It executed with all assertions passing. It does not certify any universally quantified theorem or prove the asymptotic limit; those follow from Steps 1–5.

## Relationship to prior work

The 2026 work of Huang, Wang and Zhao proves a spectral-structure and Weyl-theorem classification for Toeplitz operators with analytic polynomial symbols on the harmonic Bergman space (its Theorem 3.1), not the singular-value distribution of \(T_p-p(T_z)\). The 2014 work of Dong and Zhou studies ranks and canonical forms of **two-factor** quasihomogeneous semicommutators (notably Theorem 5.1 and Corollary 5.7). Such rank/finite-form phenomena are prior input; the exact singular data, degree-dependent norm, and beta-law for iterated monomial functional-calculus defects are the specific additional claims. The 2013 work of Yang, Liu and Lu on pluriharmonic Bergman spaces addresses other operator products and their finite-rank conditions. These comparisons are statements about the inspected literature, not a universal priority guarantee.

## Limitations

This theorem concerns analytic polynomial symbols and harmonic Bergman space with normalized unweighted area. The beta-law applies specifically to the monomial sequence of increasing degree; it is not claimed for arbitrary polynomial coefficient patterns, weighted harmonic Bergman spaces, or nonanalytic symbols. Finite tests are not exhaustive. Existing generalized semicommutator formulas may imply individual finite-rank statements; originality is claimed for the combined explicit singular-value profile and its degree-asymptotic probability law. Broader published but unlocated formulations could affect publication priority.

## References

Huang, M., Wang, J., Zhao, X. (2026). *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space*. arXiv:2610.09638, first posted 2026-10-07. Primary subject 47B35.

Dong, X.-T., Zhou, Z.-H. (2014). *Ranks of Commutators and Generalized Semicommutators of Quasihomogeneous Toeplitz Operators*. arXiv:1411.0213, first posted 2014-11-02.

Yang, J., Liu, L., Lu, Y. (2013). *Algebraic Properties of Toeplitz Operators on the Pluriharmonic Bergman Space*. DOI:10.1155/2013/578436.

Guo, K., Zheng, D. (2002). *Toeplitz algebra and Hankel algebra on the harmonic Bergman space*. J. Math. Anal. Appl. 276, 213–230. Prior general compactness framework; full-text noncoverage not asserted.
