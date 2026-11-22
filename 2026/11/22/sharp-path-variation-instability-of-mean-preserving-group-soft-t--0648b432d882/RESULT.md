# Sharp path-variation instability of mean-preserving group soft thresholding

## Finding
For every integer \(n\ge2\) and every threshold \(\lambda>0\), let \(\mathbf1\in\mathbb R^n\) denote the all-ones vector, let \(M=I-\mathbf1\mathbf1^{\mathsf T}/n\), and define the mean-preserving group shrinker
\[
G_\lambda(x)=\bar x\mathbf1+
\left(1-\frac{\lambda}{\|Mx\|_2}\right)_+Mx,
\qquad\bar x=\frac1n\sum_{i=1}^n x_i,
\]
where the second term is zero when \(Mx=0\). For path total variation \(V_n(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|\), its sharp **two-input** Lipschitz coefficient is
\[
\boxed{\quad
K_n=\sup_{V_n(x-y)>0}\frac{V_n(G_\lambda(x)-G_\lambda(y))}{V_n(x-y)}
=\frac{1+\sqrt{(4n-6)\lfloor n^2/4\rfloor/n}}2.\quad}
\]
Thus \(K_2=1\), \(K_3=3/2\), \(K_4=(1+\sqrt{10})/2\), and
\[
K_n=\frac n2+\frac18+O(n^{-1})\qquad(n\to\infty).
\]
The coefficient is independent of the positive threshold and exceeds one exactly for \(n\ge3\). Every individual signal obeys \(V_n(G_\lambda(x))\le V_n(x)\), and the map is Euclidean nonexpansive. The coefficient for \(n\ge3\) is a sharp **supremum**, approached by arbitrarily close two-input examples near the shrinkage sphere, but is not attained by any fixed distinct pair. For \(n=2\), equality is attained. At \(\lambda=0\), the map is the identity and its coefficient is one.

## Assumptions and scope
The signal space is real \(\mathbb R^n\), with consecutive unit-weight path edges and the usual Euclidean norm. The norm \(V_n\) is a seminorm on the full space and a norm on the quotient by constants, identified with the mean-zero hyperplane \(E=\{z:\sum_i z_i=0\}\). All suprema range over pairs with positive input-difference variation; no regularity, monotonicity or sign restrictions are imposed. The threshold is common to the entire centered group, not to individual coordinates. The formula concerns unweighted open-path variation, not cyclic variation or observation-weighted penalties.

The map is the unique Euclidean proximal minimizer of
\[
\min_z\left\{\frac12\|z-x\|_2^2+\lambda\|Mz\|_2\right\}.
\]
Orthogonal decomposition into constants and \(E\), followed by scalar minimization of the centered radius, proves the displayed shrinkage formula.

## Proof
**1. Derivative reduction.** Write \(x=\bar x\mathbf1+v\) with \(v\in E\) and \(r=\|v\|_2\). When \(r>\lambda\), set \(u=v/r\) and \(t=\lambda/r\in(0,1)\). On \(E\), ordinary differentiation gives
\[
DG_\lambda(x)|_E=(1-t)I_E+t uu^{\mathsf T}.
\]
When \(r<\lambda\), this derivative vanishes on \(E\); the constant component never affects variation. Define
\[
S_n=\sup_{\substack{u\in E\\\|u\|_2=1}}\|uu^{\mathsf T}\|_{V_n\to V_n}.
\]
By convexity of the induced operator norm, \(\|(1-t)I_E+t uu^{\mathsf T}\|_{V_n\to V_n}\le(1-t)+tS_n\le\max\{1,S_n\}\). The centered part of any line segment crosses the sphere \(\|v\|_2=\lambda\) in at most two points (unless it lies in a degenerate tangent case). Piecewise integration of its derivative therefore gives the global Lipschitz upper bound \(\max\{1,S_n\}\). Conversely, at the exterior points \((1+\delta)\lambda u\), the directional difference quotient tends, as the perturbation tends to zero and then \(\delta\downarrow0\), to the rank-one derivative \(uu^{\mathsf T}\). Thus the global sharp coefficient is \(\max\{1,S_n\}\).

**2. Exact rank-one variation norm.** Let \(D:\mathbb R^n\to\mathbb R^{n-1}\) be \((Dh)_i=h_{i+1}-h_i\), so \(V_n(h)=\|Dh\|_1\). Let \(b_j=M\mathbf1_{\{1,\ldots,j\}}\), \(1\le j<n\). Every centered input \(h\) is a signed linear combination of these centered steps, with the sum of absolute coefficients equal to \(V_n(h)\). Consequently,
\[
\|uu^{\mathsf T}\|_{V_n\to V_n}=V_n(u)\max_{1\le j<n}|u^{\mathsf T}b_j|.
\]
Using \(V_n(u)=\max_{\sigma\in\{-1,1\}^{n-1}}\sigma^{\mathsf T}Du\), set \(a_\sigma=D^{\mathsf T}\sigma\in E\). Since the sign can be reversed, the order of the finite maxima and the supremum over \(u\) may be interchanged, giving
\[
S_n=\max_{\sigma,j}\max_{\substack{u\in E\\\|u\|_2=1}}
|(a_\sigma^{\mathsf T}u)(b_j^{\mathsf T}u)|.
\]
The elementary symmetric rank-two eigenvalue identity states that for any real vectors \(a,b\),
\[
\max_{\|u\|_2=1}|(a^{\mathsf T}u)(b^{\mathsf T}u)|
=\frac{\|a\|_2\|b\|_2+|a^{\mathsf T}b|}{2}.
\]
Indeed, the two potentially nonzero eigenvalues of \((ab^{\mathsf T}+ba^{\mathsf T})/2\) are \((a^{\mathsf T}b\pm\|a\|_2\|b\|_2)/2\). The maximum absolute Rayleigh quotient is the displayed number. As \(a,b\in E\), restricting \(u\) to \(E\) changes nothing.

**3. Sign and cut maximization.** For any \(\sigma\in\{-1,1\}^{n-1}\), elementary differences give
\[
\|a_\sigma\|_2^2=2+4\#\{i:1\le i<n-1,\ \sigma_i\ne\sigma_{i+1}\}\le4n-6.
\]
Equality holds for alternating signs. For every \(1\le j<n\),
\[
\|b_j\|_2^2=\frac{j(n-j)}n,
\qquad a_\sigma^{\mathsf T}b_j=\sigma^{\mathsf T}Db_j=-\sigma_j,
\]
so the absolute inner product is **exactly one**, independently of the sign pattern. Both factors in the rank-two expression can therefore be maximized simultaneously: take alternating \(\sigma\) and \(j\) closest to the midpoint, for which \(j(n-j)=\lfloor n^2/4\rfloor\). Hence
\[
S_n=\frac{1+\sqrt{(4n-6)\lfloor n^2/4\rfloor/n}}2.
\]
For \(n=2\) this is one, and for \(n\ge3\) it exceeds one, completing the sharp upper bound and the supremum statement.

**4. Explicit sharpness and attainment.** Fix \(j=\lfloor n/2\rfloor\) and choose alternating signs with \(\sigma_j=-1\); then \(a_\sigma^{\mathsf T}b_j=1\). Put
\[
u=\frac{a_\sigma/\|a_\sigma\|_2+b_j/\|b_j\|_2}
{\|a_\sigma/\|a_\sigma\|_2+b_j/\|b_j\|_2\|_2},
\quad h=b_j.
\]
The step \(h\) has \(V_n(h)=1\). The rank-two eigenvector formula and the already-proved global upper bound imply \(V_n(u)|u^{\mathsf T}h|=S_n\). Now take \(x_{\delta}=(1+\delta)\lambda u\) and \(y_{\delta,\varepsilon}=x_\delta+\varepsilon h\). For each \(\delta>0\), first let \(\varepsilon\to0\); then let \(\delta\downarrow0\). The ratio of output to input variation converges to \(S_n\), proving sharpness.

If \(n\ge3\), then \(S_n>1\). Along every segment between distinct inputs modulo constants, at almost every active point \(t=\lambda/r<1\), giving derivative norm strictly smaller than \(S_n\), while inside the threshold sphere the variation derivative is zero. Integrating over the segment yields a strict inequality below \(S_n\) for any fixed nonconstant difference. For \(n=2\), choose two points on the same exterior centered ray; the subtractive radial offset cancels and the variation ratio is exactly one. For \(\lambda=0\), \(G_0=I\).

**5. Asymptotics.** Substituting \(\lfloor n^2/4\rfloor=n^2/4+O(1)\) into the radical and expanding the positive square root yields \(S_n=n/2+1/8+O(n^{-1})\).

## Verification
The included self-contained `verification.py` uses only the Python standard library. It exhaustively enumerates all sign patterns and cuts for each \(2\le n\le9\), checking the exact integer sign norm and rational cut norm against the formula. It constructs near-threshold norming pairs and verifies convergence toward the predicted coefficient. A deterministic additional 2,550 randomly sampled two-input tests over \(2\le n\le18\) check the bound and individual-signal variation diminution, including multiple thresholds. Run `python verification.py`; the final line is `ALL_CENTERED_GROUP_SHRINKAGE_BV_CHECKS_PASS`. These finite checks corroborate, but do not establish, the infinite all-dimensional theorem.

## Relationship to prior work
Yuan and Lin's group-lasso paper, first publicly available online on 2005-12-21, develops grouped Euclidean shrinkage as an estimation tool; its sections on optimization, solution paths and degrees of freedom do not provide a path-variation two-input operator norm. Huang, Breheny and Ma's 2012 review covers grouped shrinkage and statistics without the same seminorm stability question. A published finding on radial retractions provides sharp mixed coordinate \(\ell_1\) and \(\ell_\infty\) norms for \(x/\max(1,\|x\|_p)\); that mapping and its metrics are not the mean-preserving soft-threshold map and path variation here. Other related sharp path-variation results address coordinatewise soft thresholding, isotonic projections and total-variation-ball projections, neither of which has the displayed rank-one derivative family. No inspected result was found implying this closed-form coefficient. The possible existence of older unindexed BV shrinkage estimates remains an originality risk, so priority is qualified rather than independently established.

## Limitations
The theorem is for real finite paths with uniform edge weights and one centered Euclidean group. It does not cover overlapping groups, coordinatewise shrinkage, irregular graph variation, arbitrary penalties, complex inputs, or the exact constants for weighted path edges. The sharp factor for \(n\ge3\) is a nonattained supremum, so it must not be described as an attained maximum. Finite computational tests are not proofs of the all-dimensional statement. Historical completeness of the literature search cannot be guaranteed.

## References
1. M. Yuan and Y. Lin, *Model selection and estimation in regression with grouped variables*, Journal of the Royal Statistical Society B 68 (2006), 49–67, first publicly published online 2005-12-21. DOI: https://doi.org/10.1111/j.1467-9868.2005.00532.x. Accessible article text: https://www.academia.edu/93573215/Model_selection_and_estimation_in_regression_with_grouped_variables
2. J. Huang, P. Breheny and S. Ma, *A Selective Review of Group Selection in High-Dimensional Models*, arXiv:1204.6491, submitted 2012-04-29. https://arxiv.org/abs/1204.6491
3. *Sharp dual cross-norm Lipschitz constants for radial retractions of finite-dimensional \(\ell_p\) balls*, publicly accessible mathematical research result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-dual-cross-norm-lipschitz-constants-for-radial-retractions--36a632bc9802
