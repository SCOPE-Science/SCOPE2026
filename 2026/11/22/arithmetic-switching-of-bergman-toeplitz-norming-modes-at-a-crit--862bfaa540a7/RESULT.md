# Arithmetic switching of Bergman Toeplitz norming modes at a critical degree ratio

## Finding

Let \(\rho=1.609778956757873\ldots\) be the unique real zero larger than one of
\[
6r^3-13r^2+6r-1=0.
\]
For each sufficiently large integer \(n\), set \(m=\lfloor\rho n\rfloor\), \(d=m-n\), and let \(H_{m,n}=[T_{m,n}^*,T_{m,n}]\), where \(T_{m,n}\) is the analytic Bergman Toeplitz operator with symbol \(z^m\overline z^{\,n}\). Define
\[
G=-\frac{(\rho-1)^2(13\rho^2-1)}{2\rho^3(2\rho-1)^3}<0,
\qquad
L=-\frac{(\rho-1)(18\rho^2-26\rho+6)}{\rho^2(2\rho-1)^3}<0,
\qquad
\vartheta_*=G/L=0.573738632835250\ldots.
\]
The **only possible norm-attaining monomial degrees** are \(d-1\) and \(d\). Writing \(\theta_n=\{\rho n\}\), the exact eigenvalue separation satisfies
\[
 n^2\big(\lambda_d-\lambda_{d-1}\big)
 =G+|L|\theta_n+O(n^{-1}).
\]
For every fixed \(\epsilon>0\), the unique maximizing degree is \(d-1\) whenever \(\theta_n\le\vartheta_*-\epsilon\), and it is \(d\) whenever \(\theta_n\ge\vartheta_*+\epsilon\), provided \(n\) is sufficiently large. **Both cases occur infinitely often.** In addition,
\[
\|H_{m,n}\|=\frac{2d^2}{(2m-n)^2}
+\frac{1}{n^2}\max\{0,G+|L|\theta_n\}+O(n^{-3}).
\]
The \(O\)-constants are absolute for this floor sequence.

More generally, if \(m=m_n\) and \(b_n=m_n-\rho n\) remains bounded, put \(d_n=m_n-n\). Then every norm-attaining degree is \(d_n-1+\ell\) with \(\ell\ge0\) uniformly bounded; for each fixed \(\ell\), uniformly on bounded \(b_n\),
\[
 n^2(\lambda_{d_n-1+\ell}-\lambda_{d_n-1})
 =G\ell^2+Lb_n\ell+O(n^{-1}),
\]
and
\[
\|H_{m_n,n}\|
=\frac{2d_n^2}{(2m_n-n)^2}
+\frac1{n^2}\max_{\ell\in\mathbb Z_{\ge0}}(G\ell^2+Lb_n\ell)+O(n^{-3}).
\]
The nonnegative-integer maximum is finite and is the complete critical-window lattice correction.

## Assumptions and scope

Work on the classical analytic Bergman space \(A^2(\mathbb D)\) with normalized area measure. Let \(P\) be its orthogonal Bergman projection and \(e_k(z)=\sqrt{k+1}z^k\), \(k\ge0\), its standard orthonormal basis. For integers \(m>n\ge1\), write
\[
T_{m,n}f=P(z^m\overline z^{\,n}f),\quad d=m-n,\quad H_{m,n}=T_{m,n}^*T_{m,n}-T_{m,n}T_{m,n}^*.
\]
The norm refers to the operator norm on \(A^2(\mathbb D)\). All asymptotic claims concern \(n\to\infty\) through positive integers and positive integer \(m_n\). The letter \(\lambda_k\) denotes the eigenvalue of \(H_{m,n}\) on \(e_k\), not a reordered singular value.

## Proof

**1. Exact diagonalization.** The Toeplitz operator is a unilateral weighted shift of step \(d\),
\[
T_{m,n}e_k=w_ke_{k+d},\qquad
w_k^2=\frac{(k+1)(k+d+1)}{(k+m+1)^2}.
\]
Consequently \(H_{m,n}\) is diagonal, and for \(0\le k<d\), \(\lambda_k=w_k^2\); for \(k\ge d\), direct subtraction yields
\[
\lambda_k=\frac{(k+1)d\{k(m+n)+m^2+m+n^2+n\}}{(k+m+1)^2(k+n+1)^2}.
\]
All entries are nonnegative. The first branch is strictly increasing in \(k\), and its top value is
\[
\lambda_{d-1}=\frac{2d^2}{(2m-n)^2}.
\]
The displayed rational second branch remains algebraically valid at \(k=d-1\), since its formally subtracted shift weight vanishes there. Moreover \(\lambda_k\to0\) as \(k\to\infty\), so the operator norm is attained among its eigenvalues.

**2. Exact derivative and localization.** Extend the rational second branch to a smooth function \(F_{m,n}(x)\) of real \(x\ge d-1\), and put \(x=d+y\). Differentiation shows that the derivative has the sign opposite to the cubic \(A_0+A_1y+A_2y^2+A_3y^3\), where
\[
\begin{aligned}
A_0={}&6m^4-13m^3n+13m^3+6m^2n^2-13m^2n+9m^2\\
 &-mn^3-mn^2+2m+n^3-3n^2+2n,\\
A_1={}&13m^3-13m^2n+18m^2-mn^2+6m+n^3-6n^2+6n,\\
A_2={}&3(3m^2+2m-n^2+2n),\qquad A_3=2(m+n).
\end{aligned}
\]
The derivative denominator and the omitted prefactor \(m-n\) are positive. For \(m=\rho n+b\), with \(|b|\le B\), the defining cubic of \(\rho\) gives \(A_0=O_B(n^3)\), whereas
\[
 A_1=(\rho-1)(13\rho^2-1)n^3+O_B(n^2)>c n^3,
\]
with \(c>0\); also \(A_2,A_3>0\) for large \(n\). Thus the cubic is strictly increasing on \(y\ge0\). If \(A_0\ge0\), \(F_{m,n}\) decreases there; otherwise it has exactly one positive critical point, at most \(O_B(1)\) from zero. Together with monotonicity for \(k<d\), all maximizing indices belong to \(\{d-1,d,\ldots,d+C_B\}\), for some finite constant \(C_B\), independently of \(n\).

**3. Critical lattice expansion.** For an integer \(\ell\ge0\), substitute \(m=\rho n+b\), \(k=d-1+\ell\) in the exact rational formula. Expansion as \(n^{-1}\to0\) gives, uniformly when \(\ell\) and \(b\) are bounded,
\[
\lambda_{d-1+\ell}-\lambda_{d-1}
 =\frac{-\ell(\rho-1)(6\rho^3-13\rho^2+6\rho-1)}{\rho^2(2\rho-1)^3 n}
 +\frac{G\ell^2+Lb\ell}{n^2}+O_{B,\ell}(n^{-3}).
\]
The first-order coefficient vanishes by the definition of \(\rho\). The quadratic coefficient follows either by direct expansion or by differentiation of the limiting rational profile; algebraic reduction modulo \(6\rho^3-13\rho^2+6\rho-1\) gives the displayed closed forms for \(G\) and \(L\). Since the exact maximizer is localized to finitely many \(\ell\) by Step 2, the expansion is uniform over all candidate maximizers and proves the general maximum formula, including its \(O_B(n^{-3})\) remainder.

**4. Floor sequence and infinitely many switches.** Taking \(m=\lfloor\rho n\rfloor\) gives \(b=-\theta_n\in(-1,0)\). The quadratic \(q_\theta(\ell)=G\ell^2+|L|\theta\ell\) satisfies
\[
\sup_{0\le\theta\le1,\,\ell\ge2}q_\theta(\ell)
 =4G+2|L|=-0.0684930728738\ldots<0.
\]
The root is isolated by the exact rational test \(1.609778<\rho<1.609780\). Monotone rational bounds in that interval give \(0.133229<|G|<0.133233\) and \(0.232213<|L|<0.232218\); hence \(2|G|>|L|\), rigorously certifying the displayed negative gap. The same strict gap holds uniformly for all localized exact eigenvalues when \(n\) is large, so only \(\ell=0,1\) can maximize. Their difference is \(n^{-2}(G+|L|\theta_n)+O(n^{-3})\), yielding the two possible degrees, the norm formula, and the asserted threshold away from the narrow indeterminate neighborhood. The cubic defining \(\rho\) has no rational root, hence \(\rho\) is irrational. The fractional parts \(\{\rho n\}\) are dense in \((0,1)\); each fixed interval strictly below and strictly above \(\vartheta_*\) is visited infinitely often. Both norming modes therefore occur infinitely often.

## Verification

The standalone file `verify.py` recomputes the exact commutator diagonal and the critical expansion with symbolic algebra, reduces the coefficients modulo the defining cubic, checks signs of the constants, and checks norming indices against exact rational eigenvalues for sample finite degrees. These computations test the formulas but do not substitute for the global localization and irrational-rotation arguments above.

## Relationship to prior work

Fleeman and Liaw established the monomial Toeplitz hyponormality setting and exact coefficient tests in their 2017 preprint (2019 publication). Revilla and Simanek (2022), especially their analysis of the monomial commutator and their explicit open Problem 6.2, identify the relevant macroscopic degree-ratio transition and ask for the norm-attaining degrees. Those antecedents already supply the framework and qualitative ratio transition. The point proved here is the previously unstated **second-order integer-lattice law in the critical degree window**, including its fractional-part switching phenomenon. Kim and Lee (2023) study combinations of nonharmonic symbols and provide related, but not quantitatively dominant, conditions. Related published work on harmonic Bergman monomial commutators concerns different Hilbert spaces or different operator products, and does not imply this analytic-Bergman critical-window statement.

## Limitations

The result does **not** solve the full finite-parameter norm-maximizing index classification for arbitrary \(m,n\) asked by Revilla–Simanek. At fractional parts approaching \(\vartheta_*\) on the scale \(O(n^{-1})\), the two-term expansion does not resolve which of the two candidate degrees wins. The proof is for the normalized **unweighted analytic Bergman** space, not general weighted or harmonic Bergman spaces. The claim is a new critical-window refinement using the published exact eigenvalue framework, subject to possible historical priority from unindexed specialized asymptotic work.

## References

1. M. Fleeman and C. Liaw, *Hyponormal Toeplitz operators with non-harmonic symbol acting on the Bergman space*, preprint posted 30 July 2017, arXiv:1707.09677, https://arxiv.org/abs/1707.09677; *Operators and Matrices* 13 (2019), no. 1, 61–77, https://files.ele-math.com/articles/oam-13-04.pdf.
2. N. Revilla and B. Simanek, *Hyponormal Toeplitz Operators on the Bergman Space of the Disk*, preprint posted 1 November 2022, arXiv:2211.00760, https://arxiv.org/abs/2211.00760, especially Section 5 and Problem 6.2.
3. S. Kim and J. Lee, *Remarks on hyponormal Toeplitz operators with nonharmonic symbols*, *Open Mathematics* 21 (2023), 20230114, https://doi.org/10.1515/math-2023-0114.
