# A seven-coordinate threshold for sharp positive-box normalization stability

## Finding
Let \(n\ge2\) be an integer, \(0<a<b<\infty\), \(B=[a,b]^n\), and \(F:B\to\mathbb R^n\) be Euclidean direction normalization, \(F(x)=x/\|x\|_2\). Both perturbation and output magnitudes are measured in the coordinate maximum norm \(\|\cdot\|_\infty\). Define
\[
q_n=\max\left\{1,\frac{\sqrt{8n+1}-3}{4}\right\},\qquad u_n=\min\left\{\frac ba,q_n\right\}.
\]
Then the exact global Lipschitz coefficient is
\[
\boxed{\sup_{x\ne y\in B}\frac{\|F(x)-F(y)\|_\infty}{\|x-y\|_\infty}=\frac{(n-1)(1+u_n)}{a(n-1+u_n^2)^{3/2}}.}
\]
The maximizing differential pattern is approached by vectors with one distinguished coordinate \(a u_n\) and every other coordinate \(a\). Specifically, the extremal Jacobian row is normed by a perturbation with one positive entry and all other entries negative, with arbitrarily close feasible interior perturbations.

There is a sharp dimensional change: \(q_n=1\) for \(2\le n\le6\), making the coefficient exactly \(2(n-1)/(a n^{3/2})\) for every \(b>a\); whereas \(q_n>1\) for every \(n\ge7\). In dimensions seven and above, the worst input becomes a one-outlier positive vector. If \(b/a<q_n\), its distinguished coordinate approaches the upper bound \(b\); if \(b/a\ge q_n\), it approaches the interior level \(a q_n\). The scalar threshold \(q_n\) is therefore a sharp contrast-saturation frontier.

For each fixed contrast \(r=b/a>1\), the dimensional law is
\[
\lim_{n\to\infty}\sqrt n\,aL_n(a,ar)=1+r.
\]
For contrasts \(r_n\) satisfying \(r_n/\sqrt n\to\kappa\in(0,\infty]\), put \(v=\min\{\kappa,1/\sqrt2\}\), with \(v=1/\sqrt2\) if \(\kappa=\infty\). Then
\[
\lim_{n\to\infty}a L_n(a,a r_n)=\frac{v}{(1+v^2)^{3/2}},
\]
which saturates at \(2/(3\sqrt3)\). The formula concerns the raw unit Euclidean direction; multiplying the output by \(\sqrt n\), as in the zero-offset root-mean-square normalization convention, multiplies every coefficient by \(\sqrt n\).

## Assumptions and scope
All coordinates are real and positive. The domain is the **full closed convex box** \([a,b]^n\) with common strictly positive lower bound \(a\), strictly larger upper bound \(b\), and no constraints on coordinate sums. The quantity is the supremum over all *distinct* vectors in this box, rather than an average derivative, a spectral norm, or relative perturbation ratio. The boundary maximum of the Jacobian need not be attained by any distinct pair of inputs; it is attained as a limit of feasible interior finite differences. When \(n=1\), the map is constant and its sharp coefficient is zero; when \(a=b\), the domain is a singleton and there are no distinct inputs, so the natural minimal Lipschitz coefficient is zero. The stated formula applies only when \(n\ge2\) and \(a<b\).

## Proof
**1. Exact coordinatewise differential norm.** For \(x\in(0,\infty)^n\), put \(S=\sum_{j=1}^n x_j^2\). The elementary derivative is
\[
DF(x)=S^{-1/2}\left(I-\frac{xx^{\mathsf T}}S\right).
\]
Its diagonal entries are nonnegative, and each off-diagonal entry is strictly negative. Therefore the induced \(\ell_\infty\to\ell_\infty\) norm is the largest absolute row sum. Writing \(T_i=\sum_{j\ne i}x_j^2\) and \(H_i=\sum_{j\ne i}x_j\), the exact \(i\)-th row sum is
\[
J_i(x)=\frac{T_i+x_iH_i}{(x_i^2+T_i)^{3/2}}.
\]

**2. Equal-tail reduction with no lost extrema.** Write \(m=n-1\). The Cauchy–Schwarz inequality gives \(H_i\le\sqrt{mT_i}\). If we replace the \(m\) coordinates other than \(i\) by the common number \(c=\sqrt{T_i/m}\), then \(a\le c\le b\); their squared sum stays \(T_i\), while their arithmetic sum becomes \(mc=\sqrt{mT_i}\). Thus this replacement does not decrease \(J_i\). Equality is possible, so no upper-bound gap is introduced. Write \(u=x_i/c\in[1/r,r]\), where \(r=b/a>1\). The equal-tail row sum simplifies to
\[
J_i=\frac{m(1+u)}{c(m+u^2)^{3/2}}.
\]
For a fixed feasible ratio \(u\), the smallest permitted common scale is \(c=a\) when \(u\ge1\), and \(c=a/u\) when \(u\le1\), with the corresponding distinguished coordinate feasible in the box. Therefore the maximum reduces *exactly* to maximizing the two scalar functions
\[
\frac{m u(1+u)}{a(m+u^2)^{3/2}}\quad(1/r\le u\le1),\qquad
\frac{m(1+u)}{a(m+u^2)^{3/2}}\quad(1\le u\le r).
\]

**3. Scalar extremization and dimension threshold.** The first function has derivative with the sign of \(m(1+2u)-2u^2-u^3\). On \(0<u\le1\) this is nonnegative because \(m\ge1\) and
\[
m(1+2u)-2u^2-u^3\ge (1-u)(1+3u+u^2)\ge0.
\]
Its maximum is consequently at \(u=1\). The second function has derivative with the sign of \(m-3u-2u^2\). Its unique positive zero is \((\sqrt{8m+9}-3)/4=(\sqrt{8n+1}-3)/4\). It is at or below one precisely when \(m\le5\), or \(n\le6\). On the feasible interval \([1,r]\), the maximizer is thus \(u_n=\min\{r,q_n\}\), where \(q_n\) is defined in the finding. This supplies the claimed exact maximum of every row at every box point, including endpoints.

**4. From a differential maximum to the global two-input constant.** The map is smooth in an open neighborhood of \(B\). For any two distinct points \(x,y\in B\), their segment lies in \(B\); the fundamental theorem of calculus yields
\[
\|F(y)-F(x)\|_\infty\le\left(\sup_{z\in B}\|DF(z)\|_{\infty\to\infty}\right)\|y-x\|_\infty.
\]
Conversely, for a box point \(z\) and an index \(i\) maximizing its row sum, the sign vector \(d\) with \(d_i=1\), \(d_j=-1\) for \(j\ne i\) realizes the absolute row sum of \(DF(z)\). Choose interior points \(z^{(k)}\to z\) and positive \(h_k\to0\) so that \(z^{(k)}\pm h_kd\in B\). The ratios
\[
\frac{\|F(z^{(k)}+h_kd)-F(z^{(k)}-h_kd)\|_\infty}{2h_k}
\]
converge to the row sum by continuity of the derivative. Take \(z=(a u_n,a,\ldots,a)\), with boundary approximations as needed. This proves the matching lower bound and sharpness of the *global* Lipschitz coefficient.

**5. Dimensional laws.** At fixed \(r>1\), the unrestricted optimum \(q_n\sim\sqrt{n/2}\) exceeds \(r\) for all large \(n\), so \(u_n=r\) and the formula gives \(\sqrt n\,aL_n(a,ar)\to1+r\). When \(r_n/\sqrt n\to\kappa>0\), one has \(u_n/\sqrt n\to v=\min\{\kappa,1/\sqrt2\}\); division by suitable powers of \(n\) gives \(aL_n(a,a r_n)\to v/(1+v^2)^{3/2}\). This increasing function on \((0,1/\sqrt2]\) attains \(2/(3\sqrt3)\) at the endpoint. No extrapolation to signed or zero-containing boxes is asserted.

## Verification
Run `python verification.py` using Python 3 and its standard library. The supplied program checks the scalar derivative root and sharp dimension threshold, scalar bounds on grids, matching near-boundary Jacobian and finite-difference witnesses, random full-box two-input inequalities, exact Jacobian row-sum identities, Cauchy equality mechanisms, dimensional limits, and the degenerate singleton cases. A run of the embedded script printed `VERIFY_OK 124715 deterministic mathematical assertions`. The proof above, not finite testing, establishes the universal formula and the limiting claims.

## Relationship to prior work
Zhang–Sennrich (2019), *Root Mean Square Layer Normalization*, Section 4 and its gradient analysis, give the unsmoothed RMS direction transform and the same classical projected-direction derivative. They do not optimize its sharp absolute-coordinate two-input Lipschitz constant on positive boxes with a fixed dynamic range or state the seven-coordinate extremizer boundary. Singh–Krishnan (2019), *Filter Response Normalization Layer*, Section 3, introduce channelwise normalization by an uncentered second moment. Their implemented normalization includes a stabilizing offset and downstream affine/activation operations, and does not derive a sharp absolute-entrywise positive-box error modulus or a seven-coordinate extremizer transition. Dasoulas–Scaman–Virmaux (2021), *Lipschitz Normalization for Self-Attention Layers*, Sections 4–5, obtain stability controls for attention normalization; their operator, geometry, and matrix norms differ here. Qi–Wang–Zhang (2023), *Understanding Optimization of Deep Learning via Jacobian Matrix and Lipschitz Constant*, discuss normalization Jacobians and RMSNorm's general spectral-norm estimate; the Jacobian is standard and not a novelty claim, while the exact constrained \(\ell_\infty\) optimization, dependence on \(b/a\), and phase threshold are not supplied by that treatment.

For a broader geometric comparison, the published *Sharp dual cross-norm Lipschitz constants for radial retractions of finite-dimensional \(\ell_p\) balls* proves a full-space radial-retraction formula \(R_p(x)=x/\max\{1,\|x\|_p\}\) in weighted coordinate norms. Although its exterior derivative uses the same familiar tangential projection at \(p=2\), its unrestricted full-space extremization neither restricts inputs to a strictly positive box nor determines this sharp contrast-dependent coefficient. The present theorem is a new *restricted-domain* sharp optimization, not a new formula for differentiating the Euclidean norm. These comparisons concern the scientific statements and implications, not merely source-title differences.

## Limitations
The result treats finite-dimensional real positive inputs bounded below away from zero; it is not a uniform result on any box touching zero. It does not apply directly to signed activations, centered normalization, stabilizing offsets, learned gain and bias, or full network robustness. Numerical tests corroborate but do not prove all dimensions. A historically equivalent bounded-dynamic-range calculation may exist outside indexed sources, and there is no independently conducted audit.

## References
1. B. Zhang and R. Sennrich, *Root Mean Square Layer Normalization*, arXiv:1910.07467, first public 2019-10-16, https://arxiv.org/abs/1910.07467.
2. S. Singh and S. Krishnan, *Filter Response Normalization Layer: Eliminating Batch Dependence in the Training of Deep Neural Networks*, arXiv:1911.09737, first public 2019-11-21, https://arxiv.org/abs/1911.09737.
3. G. Dasoulas, K. Scaman and A. Virmaux, *Lipschitz Normalization for Self-Attention Layers with Application to Graph Neural Networks*, arXiv:2103.04886, first public 2021-03-08, https://arxiv.org/abs/2103.04886.
4. X. Qi, J. Wang and L. Zhang, *Understanding Optimization of Deep Learning via Jacobian Matrix and Lipschitz Constant*, arXiv:2306.09338, first public 2023-06-15, https://arxiv.org/abs/2306.09338.
5. *Sharp dual cross-norm Lipschitz constants for radial retractions of finite-dimensional \(\ell_p\) balls*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-dual-cross-norm-lipschitz-constants-for-radial-retractions--36a632bc9802.
