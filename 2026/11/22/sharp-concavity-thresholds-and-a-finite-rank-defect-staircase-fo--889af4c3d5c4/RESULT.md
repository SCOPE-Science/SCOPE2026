# Sharp concavity thresholds and a finite-rank defect staircase for fractional-moment shifts

## Finding

Fix an integer \(m\geq2\), a real shift parameter \(a>0\), and a nonintegral exponent \(m-2<\alpha<m-1\). For every \(\eta>-a\) set
\[
 b_n=(n+a)^\alpha+\eta(n+a)^{\alpha-1},\qquad
 W_\eta e_n=\sqrt{\frac{b_{n+1}}{b_n}}\,e_{n+1}\quad(n\geq0)
\]
on \(\ell^2(\mathbb N_0)\). These are bounded, strictly positively weighted shifts. Define \(\nabla_+^m f(x)=\sum_{j=0}^m(-1)^{m-j}\binom mj f(x+j)\) and the explicitly computable positive thresholds
\[
 \tau_n=-\frac{\nabla_+^m(x^\alpha)|_{x=n+a}}
 {\nabla_+^m(x^{\alpha-1})|_{x=n+a}},\qquad n=0,1,\ldots.
\]
Then the thresholds are strictly increasing with a uniform lower separation,
\[
 \tau_{n+1}-\tau_n>\frac{\alpha}{m-\alpha}>0,
 \qquad
 \tau_n=\frac{\alpha}{m-\alpha}\left(n+a+\frac m2\right)+O_{m,\alpha,a}(n^{-1}).
\]
With the conventional higher-order defect
\[
 \Delta_m(W_\eta)=\sum_{j=0}^m(-1)^{m-j}\binom mj W_\eta^{*j}W_\eta^j,
\]
the following sharp classification holds.

1. \(W_\eta\) is \(m\)-concave, meaning \(\Delta_m(W_\eta)\leq0\), **if and only if** \(-a<\eta\leq\tau_0\). It is never \(m\)-convex or an \(m\)-isometry for any admissible \(\eta\).
2. At \(\eta=\tau_k\), the positive spectral subspace of \(\Delta_m(W_\eta)\) has dimension exactly \(k\), its kernel is exactly \(\mathbb C e_k\), and the negative spectral subspace is infinite-dimensional. If \(\tau_k<\eta<\tau_{k+1}\), those dimensions are \(k+1,0,\infty\), respectively. For \(-a<\eta<\tau_0\), there are no positive or zero eigenvectors.
3. Every defect \(\Delta_m(W_\eta)\) is compact, and, writing its singular values in decreasing order, one has
\[
 \lim_{j\to\infty}j^m s_j(\Delta_m(W_\eta))
 =\left|\alpha(\alpha-1)\cdots(\alpha-m+1)\right|.
\]
Thus, for every real \(p>0\), the defect belongs to the Schatten ideal \(\mathcal S_p\) **if and only if** \(p>1/m\), independently of \(\eta\).
4. The number \(r_+(\eta)\) of positive eigenvalues, counted with multiplicity, satisfies the sharp linear growth law
\[
 r_+(\eta)=\frac{m-\alpha}{\alpha}\eta+O_{m,\alpha,a}(1)
 \qquad(\eta\to+\infty).
\]

## Assumptions and scope

The Hilbert space is complex and separable, with standard basis indexed from zero. All inequalities between bounded self-adjoint operators are in the quadratic-form order. The exponent lies in the **open** interval \((m-2,m-1)\); no endpoint or complex-parameter assertion is made. The only free perturbation parameter is real \(\eta>-a\), which guarantees all moments \(b_n>0\). The operator \(\Delta_m(W_\eta)\) is the defect in the convention where \(m\)-concavity is nonpositivity, as in the cited recent lifting literature. Schatten classes with \(0<p<1\) mean the usual quasi-Schatten ideals.

## Proof

**1. Shift reduction.** The moment sequence is positive because \(b_n=(n+a)^{\alpha-1}(n+a+\eta)>0\). The squared weights tend to one, hence define a bounded shift. Telescoping gives
\[
 W_\eta^{*j}W_\eta^j e_n=\frac{b_{n+j}}{b_n}e_n,
 \qquad
 \Delta_m(W_\eta)e_n=\frac{\nabla_+^m b_n}{b_n}e_n.
\]
Consequently the entire operator sign and spectral multiplicity problem reduces to the signs of two finite differences.

**2. Exact signs and threshold representation.** For a real exponent \(q\) and \(x>0\), repeated application of the fundamental theorem of calculus yields
\[
 \nabla_+^m x^q
 =q(q-1)\cdots(q-m+1)
 \int_{[0,1]^m}(x+u_1+\cdots+u_m)^{q-m}\,d\mathbf u.
\]
Because \(m-2<\alpha<m-1\), the falling factorial for \(q=\alpha\) is negative and the one for \(q=\alpha-1\) is positive. In particular \(\tau_n>0\). Their prefactor ratio simplifies to \(c=\alpha/(m-\alpha)>0\). Put \(U=u_1+\cdots+u_m\) and \(r=\alpha-m-1<0\). Then, for every \(x>0\),
\[
 \tau(x)=c\frac{\int_{[0,1]^m}(x+U)^{r+1}\,d\mathbf u}
 {\int_{[0,1]^m}(x+U)^r\,d\mathbf u},
 \qquad \tau_n=\tau(n+a).
\]
Let \(\mathbb E_x\) mean expectation under the positive probability density proportional to \((x+U)^r\) on the unit cube, and \(Y=x+U\). Differentiating the positive quotient under the integral sign, 
\[
 \tau'(x)=c\left[1+r\{1-\mathbb E_x(Y)\mathbb E_x(Y^{-1})\}\right]>c.
\]
Strictness follows from Cauchy--Schwarz, since \(\mathbb E_x(Y)\mathbb E_x(Y^{-1})>1\) and \(r<0\). Integrating over \(x\in[n+a,n+a+1]\) proves the strict separation. As \(x\to\infty\), uniform expansion of \((x+U)^r\) on the compact cube gives \(\mathbb E_x(Y)=x+m/2+O(x^{-1})\), since the unweighted cube mean of \(U\) is \(m/2\). This establishes the threshold asymptotic.

**3. Complete sign classification.** Directly from the definition,
\[
 \nabla_+^m b_n
 =\bigl(\nabla_+^m x^{\alpha-1}|_{x=n+a}\bigr)(\eta-\tau_n),
\]
where the prefactor is strictly positive. Since \(\tau_n\) is strictly increasing to infinity, the sign pattern is negative everywhere precisely when \(\eta<\tau_0\), with the first zero at \(\eta=\tau_0\); for larger parameters, positive signs appear consecutively in positions \(0,1,\ldots\), one position at each successive threshold. There is never a nonnegative tail, proving that \(\Delta_m(W_\eta)\not\geq0\) for every \(\eta\), nor can it vanish identically. The stated positive ranks, kernels, and infinite negative multiplicities now follow from diagonalization. Counting \(n\) with \(\tau_n<\eta\) using the threshold asymptotic gives the linear rank law, including the isolated equality parameters.

**4. Singular-value asymptotics.** With \(X=n+a\), the same cube integral implies
\[
 \nabla_+^m X^\alpha
 =\alpha^{\underline m}X^{\alpha-m}(1+O(X^{-1})),
\]
where \(\alpha^{\underline m}=\alpha(\alpha-1)\cdots(\alpha-m+1)\ne0\). The perturbation term has one lower power of \(X\), while \(b_n=X^\alpha(1+O(X^{-1}))\). Therefore, for fixed \(\eta\),
\[
 \frac{\nabla_+^m b_n}{b_n}
 =\alpha^{\underline m} n^{-m}+O_{m,\alpha,a,\eta}(n^{-m-1}).
\]
This tends to zero, so the diagonal defect is compact. Finite permutations of the initial entries do not affect its decreasing singular-value tail; the above asymptotic gives \(s_j\sim|\alpha^{\underline m}|j^{-m}\), hence the claimed exact membership condition in every (quasi-)Schatten ideal.

## Verification

The accompanying standalone file `verify_fractional_defects.py` requires only Python's standard library. It evaluates forward differences with 85-decimal-digit precision for four integer orders and noninteger exponents, checks signs, strict threshold separations and positivity, verifies predicted finite sign patterns, and checks the asymptotic defect coefficient at larger indices. Its expected output is `FRACTIONAL_DEFECT_DIAGNOSTIC_OK 888`. This finite calculation is a reproducibility diagnostic; the all-index inequalities, classification and infinite-dimensional conclusions are established analytically above, not inferred from finite tests.

## Relationship to prior work

Suciu, *Higher-Order Isometric Liftings of Convex and Concave Operators* (arXiv:2611.20171v1, publicly posted 15 November 2026), proves a general \(m\)-isometric lifting theorem for \(m\)-concave operators, and presents weighted-shift examples with finite-difference defects. That theorem ensures liftings in the newly determined \(m\)-concave parameter region but does not present this fractional two-power family, its sharp parameter boundary, positive-defect rank staircase, or the singular-value asymptotics. The standard diagonal-defect identity and finite-difference integral formula are not claimed as original discoveries.

Chavan and Stochel, *Weakly concave operators* (2023), characterize certain \(m\)-isometric weighted shifts by **polynomial** moment sequences (Proposition 4.3), whereas the present moments have nonintegral powers and never yield an \(m\)-isometry. Benhida, Curto and Exner, *Geometrically regular weighted shifts* (arXiv:2309.05888v2; original 2023), analyze hyperexpansivity and contractivity for weights built from ratios of \(p^n+N\) and \(p^n+D\), with \(p>1\), not the two-term fractional-power moment family studied here. The new classification therefore concerns a distinct precise family and invariant. The proof uses classical tools; an implicit corollary of a broad divided-difference comparison theorem remains possible.

## Limitations

No classification of all weighted shifts, all moment perturbations, or higher-dimensional weighted shifts is claimed. This result establishes a sharp sign/rank/ideal classification only on the stated two-power fractional-moment family. It does not assert a converse to the general lifting theorem or an optimal construction of liftings. Numerical spot checks do not certify infinite-index statements, which rely on the integral proof. No exhaustive mathematical priority claim or independent review is made.

## References

1. L. Suciu, *Higher-Order Isometric Liftings of Convex and Concave Operators*, arXiv:2611.20171v1 (15 November 2026), https://arxiv.org/html/2611.20171v1.
2. S. Chavan and J. Stochel, *Weakly concave operators*, *Proceedings of the Royal Society of Edinburgh Section A: Mathematics*, online 18 January 2023, https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/weakly-concave-operators/EE996E52E333F0B452B5CEEB7F86B471.
3. C. Benhida, R. E. Curto and G. R. Exner, *Geometrically regular weighted shifts*, arXiv:2309.05888 (first version 12 September 2023; HTML of version 2), https://arxiv.org/html/2309.05888v2.
