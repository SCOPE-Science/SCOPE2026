# Least-coordinate principle for Dirichlet affine-projection norms

## Finding

Let \(m\ge2\), let \(\alpha_1,\ldots,\alpha_m>0\), set \(A=\sum_{i=1}^m\alpha_i\), and equip the closed standard simplex
\[
\Delta_{m-1}=\{x\in[0,1]^m:\sum_i x_i=1\}
\]
with the Dirichlet probability \(\mu_\alpha=\operatorname{Dir}(\alpha_1,\ldots,\alpha_m)\). Let \(P_\alpha\) be the real \(L^2(\mu_\alpha)\)-orthogonal projection onto all affine functions, including constants, viewed as an operator on \(L^\infty(\mu_\alpha)\). Put \(a=\min_i\alpha_i\), \(b=A-a\), and \(t=a/(A+1)\). For the regularized incomplete beta integral
\[
I_t(u,v)=\frac{\int_0^t s^{u-1}(1-s)^{v-1}\,ds}{\int_0^1s^{u-1}(1-s)^{v-1}\,ds},
\]
the exact operator norm is
\[
\boxed{\|P_\alpha\|_{\infty\to\infty}=1+2\left[A I_t(a,b)-(A+1)I_t(a+1,b)\right].}
\]
**Only the vertices \(e_i\) with \(\alpha_i=a\) maximize the continuous evaluation-kernel \(L^1\) norm.** For such a vertex, the extremal unit input is the sign of its reproducing kernel, up to a \(\mu_\alpha\)-null set. The maximal downward excursion among measurable inputs \(0\le f\le1\) is exactly
\[
-\left[A I_t(a,b)-(A+1)I_t(a+1,b)\right],
\]
attained at one of these vertices by \(f(y)=\mathbf1_{\{y_i<t\}}\).

At **fixed total concentration** \(A\) and number of coordinates \(m\), the norm is uniquely minimized by equal parameters \(\alpha_i=A/m\). It increases strictly as the smallest coordinate parameter decreases. Its sharp supremum over positive parameter vectors with that total is \(2A+1\), never attained, approached as a smallest parameter tends to zero. At fixed \(m\), if \(A\to\infty\) and \(\alpha_i/A\to p_i\in(0,1)\) for every coordinate, then
\[
\boxed{\frac{\|P_\alpha\|_{\infty\to\infty}}{\sqrt A}\longrightarrow\sqrt{\frac{2(1-p_*)}{\pi p_*}},\qquad p_*=\min_i p_i.}
\]
Thus all imbalance dependence collapses to the least coordinate parameter and the total, not to the remaining individual parameters.

## Assumptions and scope

The simplex has \(m\) vertices, so dimension \(m-1\). All Dirichlet parameters are strictly positive (arbitrary real values). The operator is the exact \(L^2\) projection on the *whole* affine space, not a discrete least-squares interpolant. The output \(P_\alpha f\) has a unique affine continuous representative on the closed simplex; its \(L^\infty(\mu_\alpha)\) norm equals the maximum of that representative because the Dirichlet measure has full support. Vertex evaluation is accordingly meaningful even though every vertex has probability zero.

The distribution may be transported to any nondegenerate geometric simplex by its barycentric-coordinate affine map; the norms and extremizers remain unchanged. This is a real-valued statement. The claim does not extend to degree-two polynomial projection, arbitrary non-Dirichlet densities, or coupled global finite-element projectors.

## Proof

**1. Projection kernel and vertex reduction.** Let \(Y\sim\mu_\alpha\), \(\mu_i=\alpha_i/A\). Dirichlet moments yield
\[
\mathbb EY_i=\mu_i,\qquad
\operatorname{Cov}(Y_i,Y_j)=\frac{\mu_i\delta_{ij}-\mu_i\mu_j}{A+1}.
\]
Consequently the reproducing kernel for constants and centered affine functions is
\[
K(x,y)=1+(A+1)\sum_{i=1}^m\frac{(x_i-\mu_i)(y_i-\mu_i)}{\mu_i}
=(A+1)A\sum_{i=1}^m\frac{x_i y_i}{\alpha_i}-A.
\]
Indeed, integrating against the constant function gives one; integrating against each \(y_j\) gives \(x_j\), by the covariance identity. Hence \((P_\alpha f)(x)=\int K(x,y)f(y)\,d\mu_\alpha(y)\).

Set \(F(x)=\int|K(x,y)|\,d\mu_\alpha(y)\). Because \(K\) is affine in its first variable and \(x=\sum_i x_i e_i\),
\[
F(x)\le\sum_i x_iF(e_i)\le\max_iF(e_i).
\]
The first inequality is strict whenever at least two coordinates of \(x\) are positive: for any two such indices \(i\ne j\), at \(y=e_i\) the kernel \(K(e_i,e_i)=(A+1)A/\alpha_i-A\) is positive while \(K(e_j,e_i)=-A\) is negative. This sign disagreement persists on a nonempty relatively open neighborhood inside the simplex, which has positive Dirichlet measure. Thus **only vertices** can maximize \(F\).

**2. Exact vertex norm.** At \(x=e_i\) one has
\[
K(e_i,Y)=A\left(\frac{(A+1)Y_i}{\alpha_i}-1\right),\qquad
Y_i\sim\operatorname{Beta}(\alpha_i,A-\alpha_i).
\]
Let \(a_i=\alpha_i\), \(b_i=A-a_i\), and \(t_i=a_i/(A+1)\). Since \(\mathbb EK(e_i,Y)=1\),
\[
F(e_i)=1+2C_A(a_i),\qquad C_A(a_i)=A\,\mathbb E\left(1-\frac{(A+1)Y_i}{a_i}\right)_+.
\]
The truncated-beta identities
\[
\Pr(Y_i\le t_i)=I_{t_i}(a_i,b_i),\qquad
\mathbb E[Y_i\mathbf1_{\{Y_i\le t_i\}}]=\frac{a_i}{A}I_{t_i}(a_i+1,b_i)
\]
prove
\[
C_A(a_i)=A I_{t_i}(a_i,b_i)-(A+1)I_{t_i}(a_i+1,b_i).
\]
The sign of \(K(e_i,y)\) changes only on \(y_i=t_i\), a null set. Its sign therefore gives the unique (up to null sets) unit-norm input extremizing this evaluation. Choosing the negative region indicator instead gives the sharp nonnegative-input descent \(-C_A(a_i)\).

**3. Strict least-coordinate ordering.** Fix \(A>0\) and \(0<a<c<A\). Couple
\[
(U,V,W)\sim\operatorname{Dir}(a,c-a,A-c).
\]
Then \(U\sim\operatorname{Beta}(a,A-a)\), \(S=U+V\sim\operatorname{Beta}(c,A-c)\), and
\[
\mathbb E\left[\frac Ua\,\middle|\,S\right]=\frac Sc.
\]
The function \(\phi(z)=(1-(A+1)z)_+\) is convex, so conditional Jensen gives
\[
\mathbb E\phi(U/a)\ge\mathbb E\phi(S/c).
\]
This inequality is **strict**. Conditional on every \(S=s>a/(A+1)\), the law of \(U\) has positive density throughout \((0,s)\), hence \(U/a\) takes values on both sides of the kink \(1/(A+1)\). Such \(s\) have positive probability. Thus \(C_A(a)>C_A(c)\). The largest vertex norm is therefore attained exactly at the vertices with smallest \(\alpha_i\), establishing the formula and complete norming-location classification.

**4. Optimal balancing and the sharp boundary.** Every positive parameter vector of total \(A\) satisfies \(a\le A/m\), with equality only when every parameter is \(A/m\). Strict monotonicity makes the equally weighted Dirichlet law the unique minimizer.

For \(0<a<A\), the kernel at the corresponding vertex is bounded below by \(-A\) and has a positive region of positive measure. Therefore \(0<C_A(a)<A\), so \(1<\|P_\alpha\|<2A+1\). As \(a\downarrow0\) with \(A\) fixed, the normalized beta variable \(Y_a/a\) converges to zero in probability. For example, for every \(q\in(0,1)\),
\[
\mathbb E(Y_a/a)^q
=a^{-q}\frac{\Gamma(a+q)\Gamma(A)}{\Gamma(a)\Gamma(A+q)}=O(a^{1-q})\longrightarrow0.
\]
Since \(0\le(1-(A+1)Y_a/a)_+\le1\), dominated convergence in probability yields \(C_A(a)\to A\). This proves sharpness of the unattained supremum \(2A+1\).

**5. High-concentration limit.** If \(a_i/A\to p_i\in(0,1)\), the beta central limit theorem gives
\[
\sqrt A\left(Y_i-\frac{a_i}{A}\right)
\ \Longrightarrow\ N(0,p_i(1-p_i)).
\]
Equivalently, \(K(e_i,Y)/\sqrt A\) tends in distribution to a centered normal of variance \((1-p_i)/p_i\). Its second moment is \(\bigl[1+(A+1)(1-a_i/A)/(a_i/A)\bigr]/A\), uniformly bounded as \(A\to\infty\). Uniform integrability therefore gives convergence of the first absolute moment to \(\sqrt{2(1-p_i)/(\pi p_i)}\). Taking the smallest coordinate (the norming one) proves the stated asymptotic.

## Verification

Run `python verify.py` using Python 3 and its standard library. Exact rational arithmetic independently checks beta-CDF formulas against direct polynomial beta-density integration for 275 integer parameter pairs, strict least-parameter ordering for every integer total \(3\le A\le24\), reproduction of constants and each affine coordinate on five heterogeneous Dirichlet laws, and recovery of the known uniform-simplex formula for 12 dimensions. The final marker is `ALL_DIRICHLET_AFFINE_CHECKS_OK`.

These finite checks corroborate the algebra; the continuous-parameter theorem, strictness, and asymptotics are proved by the analytic arguments above rather than by enumeration. No numerical samples are used to certify uniqueness.

## Relationship to prior work

Griffiths and Spanò (arXiv:1003.5131, initially public on 2010-03-26), Section 2.2, give the explicit degree-one Jacobi/Dirichlet reproducing kernel \(Q_1^\alpha\). It is an essential **known input** here. Their work primarily characterizes kernels and canonical-correlation sequences; the present sharp endpoint projection norm, the least-parameter rule, positivity defect, and boundary regimes are distinct norm-optimization statements. The kernel identity alone does not identify the maximizing coordinate among unequal parameters.

An earlier public result, *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (2026-10-04), obtains the uniform-volume case \(\alpha_i=1\), giving the benchmark \(2m(m/(m+1))^{m-1}-1\). The present formula reduces exactly to that benchmark but applies to all strictly positive and **unequal** Dirichlet parameters; the strict ordering and unique optimal balance are additional conclusions. The existing uniform-volume theorem is not represented as novel here.

Białas-Cież, Kenne, Sommariva and Vianello (arXiv:2311.18656) study rigorous numerical evaluation of Lebesgue constants for broad classes of projectors, including weighted least-squares on simplices. Their fully discrete mesh method is not an exact closed formula for the continuous Dirichlet degree-one projector, and it does not entail the least-concentration ordering. Yuan Xu (arXiv:1309.1510) studies Jacobi and related kernels on simplices; only its abstract was available in this comparison, so equivalence hidden in its full text remains a residual literature risk.

## Limitations

The exact result is specific to degree-one projection and Dirichlet density on a simplex. The projection is not positivity preserving: the negative excursion formula quantifies this failure. The norm is a sup over continuous affine output representatives, with input functions only defined almost everywhere; maximizing input signs are unique only up to null sets and overall sign. The large-concentration asymptotic assumes every limiting coordinate proportion is strictly between zero and one, so it is not uniform near the boundary of parameter space. The result does not address higher Jacobi degrees or arbitrary weighted measures. As with any literature comparison, unindexed equivalent results cannot be ruled out by search alone.

## References

1. R. C. Griffiths and D. Spanò, *Orthogonal polynomial kernels and canonical correlations for Dirichlet measures*, arXiv:1003.5131, first public version 2010-03-26; Bernoulli 19 (2013), 548–598, DOI 10.3150/11-BEJ403. Relevant full text: Section 2 and Section 2.2, including the explicit degree-one kernel.
2. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published research result (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 . Relevant full text: result and proof, uniform-volume case.
3. L. Białas-Cież, D. J. Kenne, A. Sommariva and M. Vianello, *Evaluating Lebesgue constants by Chebyshev polynomial meshes on cube, simplex and ball*, arXiv:2311.18656, first public version 2023-11-30. Relevant full text: Sections 1–2 and computational framework.
4. Y. Xu, *Hahn, Jacobi, and Krawtchouck polynomials of several variables*, arXiv:1309.1510, first public version 2013-09-05. Abstract-level comparison only.
