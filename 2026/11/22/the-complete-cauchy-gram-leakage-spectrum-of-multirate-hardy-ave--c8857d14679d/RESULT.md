# The complete Cauchy–Gram leakage spectrum of multirate Hardy averages

## Finding

Let \(\beta>-1\), let \(m\geq 2\), and let \(\alpha_1,\ldots,\alpha_m\) be pairwise distinct **real** numbers satisfying
\[
\frac{\beta-1}{2}<\alpha_j<\beta.
\]
For nonzero complex coefficients \(\lambda_1,\ldots,\lambda_m\), define \(T=\sum_{j=1}^{m}\lambda_jH_{\alpha_j}\) on \(\mathcal H_\beta=L^2((0,1),x^\beta\,dx)\), where
\[
(H_\alpha f)(x)=x^{-\alpha-1}\int_0^x t^\alpha f(t)\,dt.
\]
Write \(P_n\) for orthogonal projection onto ordinary polynomials of degree at most \(n\), \(c_j=2\alpha_j-\beta+1>0\), \(\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_m)\), and
\[
C=(C_{ij})_{i,j=1}^m,\qquad C_{ij}=\frac1{c_i+c_j}.
\]
Then, for every \(1\leq k\leq m\), the nonzero singular values of the finite-rank Galerkin leakage satisfy
\[
\boxed{\lim_{n\to\infty}s_k([P_n,T])=s_k(2C^{1/2}\Lambda C^{1/2})>0.}
\]
For all \(n\), \(\operatorname{rank}[P_n,T]\leq m\), and equality holds for all sufficiently large \(n\). The commutators converge strongly to zero but do not converge to zero in operator norm. In particular, for \(\beta=3\), \((\alpha_1,\alpha_2)=(2,5/2)\), and \((\lambda_1,\lambda_2)=(1,-1)\), the two limiting singular values are precisely \(1/5\) and \(1/30\).

## Assumptions and scope

All Hilbert spaces are complex. The measure \(x^\beta dx\) is not probability-normalized: the projection and the operator use the same weighted inner product \(\langle f,g\rangle=\int_0^1 f(x)\overline{g(x)}x^\beta\,dx\). Singular values are ordered decreasingly with multiplicity. The conditions \(\beta>-1\) and \(\alpha>(\beta-1)/2\) ensure boundedness of each weighted averaging operator; the strict bound \(\alpha<\beta\) ensures an integrable boundary singularity in the adjoint formula. The distinctness and nonzero coefficients make the limiting matrix invertible. No assertion is made for complex rates, repeated rates, the excluded endpoints, or other polynomial weights.

## Proof

**Step 1: boundedness, invariance, and adjoints.** Put \(c=2\alpha-\beta+1\) and \(\delta=\beta-\alpha\). For \(c>0\), the change of variables \(x=e^{-s}\), followed by multiplication by \(e^{-(\beta+1)s/2}\), turns \(H_\alpha\) into convolution on the positive half-line by the integrable kernel \(e^{-cs/2}\mathbf 1_{s\ge0}\) (with a possible reversal of the convolution coordinate). Hence \(H_\alpha\) is bounded, with norm at most \(2/c\). Alternatively the weighted Hardy inequality gives this bound. Its monomial action is
\[
H_\alpha x^r=\frac{x^r}{r+\alpha+1}\quad(r=0,1,2,\ldots).
\]
Thus \(H_\alpha\operatorname{ran}P_n\subseteq\operatorname{ran}P_n\), and the commutator equals \([P_n,H_\alpha]=P_nH_\alpha(I-P_n)\). A Fubini calculation gives
\[
(H_\alpha^*g)(x)=x^{-\delta}\int_x^1t^{\delta-1}g(t)\,dt.
\]
For any polynomial \(p\), \(H_\alpha^*p\) equals a scalar multiple of \(x^{-\delta}\) plus a polynomial of degree at most \(\deg p\), because \(\delta>0\). The singular term belongs to \(\mathcal H_\beta\), because \(c=\beta-2\delta+1>0\).

**Step 2: exact rank-one kernel for one rate.** Let
\[
q_k(x)=\sqrt{2k+\beta+1}\,P_k^{(0,\beta)}(2x-1),\qquad k\ge0,
\]
be the orthonormal shifted-Jacobi polynomials (the conventional \(P_k^{(0,\beta)}\) normalization, positive leading coefficient). Rodrigues' identity is
\[
x^\beta P_k^{(0,\beta)}(2x-1)=\frac{(-1)^k}{k!}\frac{d^k}{dx^k}\bigl(x^{k+\beta}(1-x)^k\bigr).
\]
Repeated integration by parts, justified first for positive parameters and then directly by the beta integral for all parameters in the declared range, yields
\[
\begin{aligned}
h_{\alpha,k}&:=\int_0^1x^{\delta-1}q_k(x)\,dx
=(-1)^k\sqrt{2k+\beta+1}\,\frac{\Gamma(\delta)}{\Gamma(\alpha+1)}\frac{\Gamma(k+\alpha+1)}{\Gamma(k+\delta+1)},\\
r_{\alpha,l}&:=\int_0^1x^{\alpha}q_l(x)\,dx
=(-1)^l\sqrt{2l+\beta+1}\,\frac{\Gamma(\alpha+1)}{\Gamma(\delta)}\frac{\Gamma(l+\delta)}{\Gamma(l+\alpha+2)}.
\end{aligned}
\]
For \(k\le n<l\), the polynomial part of \(H_\alpha^*q_k\) is orthogonal to \(q_l\). Consequently
\[
\langle H_\alpha q_l,q_k\rangle=h_{\alpha,k}r_{\alpha,l}.
\]
(The displayed factors are real; all complex conjugations are therefore immaterial.) Thus each single-rate leakage has rank at most one, while the sum has rank at most \(m\).

**Step 3: a common rank-\(m\) factorization and its Gram limits.** Simultaneously remove the signs \((-1)^k\) from both the low-degree and high-degree bases, a unitary operation. Let \(c_j=\alpha_j-\delta_j+1\), and for each \(n\ge1\) set
\[
\begin{aligned}
u_{j,k}^{(n)}&=\sqrt{2k+\beta+1}\,\frac{\Gamma(k+\alpha_j+1)}{\Gamma(k+\delta_j+1)}n^{-c_j},&&0\le k\le n,\\
v_{j,l}^{(n)}&=\sqrt{2l+\beta+1}\,\frac{\Gamma(l+\delta_j)}{\Gamma(l+\alpha_j+2)}n^{c_j},&&l>n.
\end{aligned}
\]
The positive Gamma constants cancel between the two factors. If \(U_n\) and \(V_n\) have these vectors as columns, then \([P_n,T]\), after unitary identification of its nonzero block, equals \(U_n\Lambda V_n^*\). Here \(U_n:\mathbb C^m\to\mathbb C^{n+1}\), while \(V_n:\mathbb C^m\to\ell^2\{n+1,n+2,\ldots\}\).

The Gamma-ratio asymptotics give, for large \(k,l\),
\[
\begin{aligned}
\sqrt{2k+\beta+1}\frac{\Gamma(k+\alpha_j+1)}{\Gamma(k+\delta_j+1)}&\sim\sqrt2\,k^{c_j-1/2},\\
\sqrt{2l+\beta+1}\frac{\Gamma(l+\delta_j)}{\Gamma(l+\alpha_j+2)}&\sim\sqrt2\,l^{-c_j-1/2}.
\end{aligned}
\]
Therefore, for every fixed \(i,j\), the elementary power-sum and tail-integral asymptotics, using \(c_i+c_j>0\), yield
\[
\begin{aligned}
\lim_{n\to\infty}(U_n^*U_n)_{ij}&=\lim_{n\to\infty}\frac{2}{n^{c_i+c_j}}\sum_{k=1}^n k^{c_i+c_j-1}=\frac2{c_i+c_j},\\
\lim_{n\to\infty}(V_n^*V_n)_{ij}&=\lim_{n\to\infty}2n^{c_i+c_j}\sum_{l>n}l^{-c_i-c_j-1}=\frac2{c_i+c_j}.
\end{aligned}
\]
Here equalities containing asymptotic sums express equality of limits, not exact equality of the individual finite sums. The finitely many small indices contribute negligibly to the first limit.

**Step 4: full singular spectrum and sharp example.** The Cauchy matrix \(C\) is positive definite: it is the Gram matrix of the distinct functions \(t\mapsto e^{-c_jt}\) in \(L^2(0,\infty)\). Both Gram matrices converge to \(2C\). The nonzero singular values of \(U_n\Lambda V_n^*\) equal those of \((U_n^*U_n)^{1/2}\Lambda(V_n^*V_n)^{1/2}\); continuity of positive square roots and finite-matrix singular values proves the assertion. Since \(C\) and \(\Lambda\) are invertible, all \(m\) limiting values are positive, and both Gram matrices have full rank for sufficiently large \(n\).

For the indicated two-rate example \(c_1=2\), \(c_2=3\),
\[
C=\begin{pmatrix}1/4&1/5\\1/5&1/6\end{pmatrix},\qquad
\operatorname{tr}(2C^{1/2}\Lambda C^{1/2})=\frac16,\qquad
\det(2C^{1/2}\Lambda C^{1/2})=-\frac1{150}.
\]
Its two real eigenvalues are \(1/5\) and \(-1/30\); hence its singular values are \(1/5\) and \(1/30\). Finally, \(P_n\to I\) strongly and the boundedness of \(T\) imply \([P_n,T]=P_nT(I-P_n)\to0\) strongly, whereas its norm converges to the largest strictly positive singular value just computed.

## Verification

The proof is analytic for every allowed real rate and all fixed finite \(m\). The optional standalone script `checker.py` evaluates the two Gram matrices numerically for \(\beta=3\), \(\alpha_1=2\), \(\alpha_2=5/2\), and coefficients \((1,-1)\), checks strict positivity of their two singular values and their convergence toward \((1/5,1/30)\) at several cutoffs. Run `python checker.py` with Python 3 and no external dependencies. This finite test does not certify the all-parameter theorem, which follows from the exact rank-one factorization and the Gamma-ratio limits.

## Relationship to prior work

Agler and McCarthy's 2022 study of Hardy and monomial operators develops monomial eigenvectors, polynomial approximation and a Gram-determinant distance formula; their separate invariant-subspace treatment addresses limits of monomial spans. Chalendar and Partington's 2022 preprint (published in 2023) characterizes boundedness and compactness of monomial operators. These results motivate the family and the choice of polynomial cutoff but do not state the simultaneous limit of **all nonzero** Galerkin commutator singular values for finite linear combinations of distinct weighted Hardy averages. The one-rate factorization alone does not determine how different channels interact: the cross terms in the Cauchy matrix are essential to the full multirate spectrum.

## Limitations

This theorem concerns fixed finite numbers of distinct real rates in the displayed strict parameter range, and the particular ordinary-polynomial projections in the given weighted Hilbert space. It makes no claims about general approximation spaces, nonlinear rate scaling, spectral limits when \(m\to\infty\), or historical novelty beyond the inspected sources. Other unindexed or inaccessible literature might contain the same multirate formula. Supplementary numerical checks are illustrative, not an independent mathematical validation.

## References

1. J. Agler and J. E. McCarthy, *A generalization of Hardy's operator and an asymptotic Müntz–Szász theorem*, arXiv:2205.01856v1, publicly posted 4 May 2022. https://arxiv.org/abs/2205.01856
2. J. Agler and J. E. McCarthy, *Beurling's theorem for the Hardy operator on \(L^2[0,1]\)*, arXiv:2206.03462, first posted June 2022. https://arxiv.org/abs/2206.03462
3. I. Chalendar and J. R. Partington, *Boundedness and compactness of weighted composition operators and monomial operators*, arXiv:2212.02172v1, posted 5 December 2022, subsequently *Archiv der Mathematik* 121 (2023), 707–714. https://arxiv.org/abs/2212.02172
