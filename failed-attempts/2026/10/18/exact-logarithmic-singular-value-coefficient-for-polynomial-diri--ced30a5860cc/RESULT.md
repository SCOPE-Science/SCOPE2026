# Exact logarithmic singular-value coefficient for polynomial Dirichlet Volterra operators

## Finding

For any nonconstant Dirichlet polynomial \(g(s)=b_1+\sum_{m\in M}b_m m^{-s}\), where \(M\) is a finite nonempty set of integers at least \(2\), every \(b_m\ne0\), and the coefficients are complex, the Volterra operator \(T_g:\mathscr H^2\to\mathscr H^2\) obeys the **sharp limit**
\[
\lim_{n\to\infty}(\log n)\,s_n(T_g)
=\max_{z\in\mathbb T^r}\left|\sum_{m\in M}b_m(\log m)z^{\alpha(m)}\right|
=\sup_{\operatorname{Re}s>0}|g'(s)|.
\]
Here the \(r\) variables correspond to the distinct primes dividing the elements of \(M\), the multi-index \(\alpha(m)\) records their valuations, and \(s_n\) denotes the decreasing singular values, with multiplicity. In particular, the limit is strictly positive: \(s_n(T_g)\asymp1/\log n\). No assertion is made about an arbitrary infinite Dirichlet-series symbol.

The dependence on the full torus polynomial, rather than merely the sum of the coefficient moduli, is substantive. For \(g(s)=2^{-s}+4^{-s}-8^{-s}\), the limit equals \((8/\sqrt3)\log2\). The coefficient-modulus sum would instead be \(6\log2\).

## Assumptions and scope

The Hardy Hilbert space \(\mathscr H^2\) of Dirichlet series has orthonormal basis \(e_n(s)=n^{-s}\) for integers \(n\ge1\), hence identifies isometrically with \(\ell^2(\mathbb N)\). Define
\[
T_gf(s)=-\int_s^{+\infty}f(w)g'(w)\,dw
\]
first on Dirichlet polynomials, with the integral taken horizontally to the right and \(\operatorname{Re}s\) sufficiently large. For a finite symbol the bounded extension follows from the proof below. Singular values of a compact Hilbert-space operator are indexed \(s_1\ge s_2\ge\cdots\ge0\). The assertion is for each *fixed* finite, nonconstant complex symbol. The constant term \(b_1\) does not affect \(T_g\).

## Proof

**1. Factorization.** Put \(c_m=b_m\log m\) for \(m\in M\). For each integer \(m\ge2\) define the multiplicative shift \(S_me_k=e_{mk}\) on \(\ell^2(\mathbb N)\). Let \(B=\sum_{m\in M}c_mS_m\). Define the diagonal operator \(D\) by \(De_1=0\) and \(De_k=(\log k)^{-1}e_k\) for \(k\ge2\). Direct multiplication and horizontal integration give, for every finite input \(f=\sum_ka_ke_k\),
\[
(T_gf)_{j}=
\frac{1}{\log j}\sum_{\substack{m\in M,\ k\ge1\\mk=j}}c_ma_k
\quad(j\ge2),\qquad (T_gf)_1=0.
\]
Thus \(T_g=DB\) exactly. Every \(S_m\) is an isometry, so \(B\) is bounded. The diagonal \(D\) is compact and its singular values satisfy \(s_n(D)=1/\log(n+1)\). Consequently \(T_g\) is compact, and the ideal inequality gives
\[
 s_n(T_g)\le\|B\|s_n(D)=\frac{\|B\|}{\log(n+1)}.
\]
This proves \(\limsup_{n\to\infty}(\log n)s_n(T_g)\le\|B\|\).

**2. Evaluation of the multiplier norm.** Let \(p_1,\ldots,p_r\) be all primes dividing an element of \(M\), and write \(m=\prod_{j=1}^r p_j^{\alpha_j(m)}\). The Bohr transform identifies \(\ell^2(\mathbb N)\) with the analytic Hardy space on the infinite torus and turns \(S_m\) into multiplication by \(z^{\alpha(m)}\). Thus \(B\) becomes multiplication by \(h(z)=\sum_{m\in M}c_mz^{\alpha(m)}\), trivially extended in the other variables. On the analytic Hardy space, its norm is precisely the uniform norm on the distinguished boundary:
\[
\|B\|=\max_{z\in\mathbb T^r}|h(z)|.
\]
The upper bound is the boundary \(L^2\) inequality. For the lower bound, evaluation against normalized reproducing kernels in the finite polydisc shows that the multiplier norm dominates \(|h(w)|\) for every interior \(w\); radial approach to any boundary maximizer proves equality. Finally, unique prime factorization makes \(\log p_1,\ldots,\log p_r\) linearly independent over the rationals. Kronecker density for their rotation flow, together with the limit as \(\operatorname{Re}s\downarrow0\), gives
\[
\max_{z\in\mathbb T^r}|h(z)|=\sup_{\operatorname{Re}s>0}|g'(s)|.
\]
The minus sign in \(g'\) is immaterial for its absolute value.

**3. Uniform-density disjoint translates.** Fix \(\varepsilon>0\). Since finitely supported vectors are dense and \(B\) is bounded, choose a finitely supported unit vector \(x\) satisfying \(\|Bx\|>\|B\|-\varepsilon\). Write \(F=\operatorname{supp}x\), \(G=\operatorname{supp}(Bx)\), \(H=F\cup G\) and \(L=|H|^2+1\). Both sets are finite and \(G\subset\{2,3,\ldots\}\).

For each integer \(R\ge1\) form a conflict graph on \(R\le r\le2R\), joining distinct \(r,r'\) when \(rH\cap r'H\ne\varnothing\). For a fixed \(r\), each collision has the form \(ra=r'b\) for some \(a,b\in H\), and each ordered pair determines at most one \(r'\). Hence the conflict graph has maximum degree no more than \(|H|^2\). Greedy independent-set selection produces \(E_R\subset\{R,\ldots,2R\}\) of cardinality at least \((R+1)/L\) such that the sets \(rH\) are pairwise disjoint for \(r\in E_R\).

Write \(U_re_k=e_{rk}\). The vectors \(U_rx\) are orthonormal since their supports \(rF\) are disjoint. Since multiplicative shifts commute, \(B U_rx=U_r Bx\); the images \(D B U_rx\) have disjoint supports in \(rG\), too. For \(r\in E_R\), each output frequency \(j\) lies between \(2\) and \(2R\max G\), so
\[
\|T_gU_rx\|=\|DU_rBx\|\ge
\frac{\|Bx\|}{\log(2R\max G)}.
\]
By orthogonality, the *same bound* holds uniformly on the unit sphere of the span of \(\{U_rx:r\in E_R\}\). The Hilbert-space min--max characterization of singular values therefore yields
\[
 s_{|E_R|}(T_g)\ge
\frac{\|B\|-\varepsilon}{\log(2R\max G)}.
\]
For each \(n\), choose \(R=Ln\). Then \(|E_R|\ge n\), and decreasing rearrangement gives
\[
 s_n(T_g)\ge\frac{\|B\|-\varepsilon}{\log(2Ln\max G)}.
\]
Multiplying by \(\log n\), sending \(n\to\infty\), and then \(\varepsilon\downarrow0\) establishes \(\liminf_{n\to\infty}(\log n)s_n(T_g)\ge\|B\|\). Combined with Step 1, this proves the stated limit.

**4. Exact example.** With \(g(s)=2^{-s}+4^{-s}-8^{-s}\), its torus multiplier is \(h(z)=(\log2)(z+2z^2-3z^3)\). On \(|z|=1\), put \(t=\operatorname{Re}z\). Then
\[
|z+2z^2-3z^3|^2=20-8t-12t^2
=\frac{64}{3}-12\left(t+\frac13\right)^2.
\]
Therefore the torus maximum is exactly \(8/\sqrt3\), reached when \(\operatorname{Re}z=-1/3\).

## Verification

The standalone \(\texttt{check.py}\) uses exact rational arithmetic for the extremal polynomial identity and finite diagnostics for the multiplicative coefficient formula, translations, support packing, and monomial singular values. It completes 194,050 finite diagnostic assertions. The analytic argument in Steps 1--3 proves the infinite-dimensional theorem; none of the finite checks is used as a surrogate for the limiting min--max argument. The actual checker must be executed from this package, not inferred from a log.

## Relationship to prior work

Chen, Wang, and Yuan (first publicly posted 2026-09-05), in Section 6 of their work on area operators on Hardy spaces of Dirichlet series, establish essential-norm and compactness characterizations for \(T_g\), and recover the compactness for symbols in \(\operatorname{VMOA}\). The present theorem computes the *exact leading singular-value coefficient* for nonconstant Dirichlet polynomials, which is not supplied by those qualitative conclusions.

Brevig, Perfekt, and Seip prove that a Volterra operator with any nonconstant Dirichlet-series symbol belongs to no finite Schatten class (Theorem 7.2), using coefficient lower bounds. This older theorem is expressly not claimed as new. Our sharper statement yields a complete logarithmic singular-value equivalent in the finite-symbol setting, including its potentially phase-sensitive constant. The Bergman-space result of Gómez-Cabello, Lefèvre, and Queffélec involves a different domain space and does not directly imply this Hardy-space singular-value formula.

## Limitations

The coefficient is proved for fixed *finite* symbols on the Hilbert space \(\mathscr H^2\). There is no uniform error term as the number of symbol coefficients or their magnitudes vary, nor an assertion for general \(\mathscr H^p\) with \(p\ne2\) or for a nonpolynomial symbol. The theorem does not determine second-order fluctuations. A general theorem for slowly varying compact diagonal operators could also imply this special-case asymptotic.

## References

1. Jiale Chen, Maofa Wang, and Zixing Yuan, *Area operators on Hardy spaces of Dirichlet series II: counterexamples and compactness criteria*, arXiv:2609.06033 (version 1, 2026-09-05), particularly Section 6 and Theorem 6.2. https://arxiv.org/abs/2609.06033
2. Ole Fredrik Brevig, Karl-Mikael Perfekt, and Kristian Seip, *Volterra operators on Hardy spaces of Dirichlet series*, arXiv:1602.04729 (2016), particularly Section 7 and Theorem 7.2. https://arxiv.org/abs/1602.04729
3. Carlos Gómez-Cabello, Pascal Lefèvre, and Hervé Queffélec, *Volterra operator acting on Bergman spaces of Dirichlet series*, arXiv:2402.12524 (2024), on a distinct Bergman-space setting. https://arxiv.org/abs/2402.12524
