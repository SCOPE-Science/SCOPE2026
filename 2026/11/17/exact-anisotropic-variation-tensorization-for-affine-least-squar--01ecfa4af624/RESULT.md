# Exact anisotropic-variation tensorization for affine least squares on product grids

## Finding
Let \(d\ge1\), let each factor \(X_j=\{1,\ldots,n_j\}\) have \(n_j\ge2\), and let the strictly increasing real sample locations be \(t_{j,1}<\cdots<t_{j,n_j}\). Give factor \(j\) strictly positive probability masses \(\mu_{j,i}\) summing to one. For every factor choose strictly positive edge weights \(w_{j,k}\), \(1\le k<n_j\), and a positive axis multiplier \(\alpha_j\). Write \(X=\prod_jX_j\) and \(\mu=\bigotimes_j\mu_j\). Define the weighted anisotropic graph variation
\[
V(f)=\sum_{j=1}^{d}\alpha_j\sum_{x_{-j}\in X_{-j}}\mu_{-j}(x_{-j})
\sum_{k=1}^{n_j-1}w_{j,k}|f(x_{-j},k+1)-f(x_{-j},k)|.
\]
Here \(\mu_{-j}\) is the product probability on all coordinates except \(j\). Let \(P\) be the \(L^2(\mu)\)-orthogonal projector onto the **globally additive affine** subspace
\[
\mathcal A=\left\{c+\sum_{j=1}^d a_j t_{j,i_j}:c,a_1,\ldots,a_d\in\mathbb R\right\}.
\]
This is not projection onto the full tensor-product, separately affine/multilinear polynomial space. Put
\[
\begin{aligned}
 m_j&=\sum_i\mu_{j,i}t_{j,i},
 &s_j^2&=\sum_i\mu_{j,i}(t_{j,i}-m_j)^2,\\
 B_j&=\sum_{k=1}^{n_j-1}w_{j,k}(t_{j,k+1}-t_{j,k}),
 &U_{j,k}&=-\sum_{i=1}^k\mu_{j,i}(t_{j,i}-m_j)>0.
\end{aligned}
\]
Then the exact, **attained**, two-input operator seminorm is
\[
\boxed{\sup_{V(f-g)>0}\frac{V(Pf-Pg)}{V(f-g)}
=\max_{1\le j\le d}\max_{1\le k<n_j}
\frac{B_jU_{j,k}}{s_j^2w_{j,k}}.}
\]
Every entry in this finite maximum has a witness: the function \(f(i_1,\ldots,i_d)=\mathbf1_{\{i_j>k\}}\), with \(g=0\). In particular the sharp coefficient does **not depend on the number of other factors or the positive axis multipliers** \(\alpha_j\). Its computation uses only \(O(\sum_j n_j)\) arithmetic operations once factor data are supplied, despite \(|X|=\prod_jn_j\) observations.

For the equally spaced, equally weighted case \(t_{j,i}=i-1\), \(\mu_{j,i}=1/n_j\), \(w_{j,k}=1\), the exact coefficient becomes
\[
\boxed{C_{\boldsymbol n}=\max_j \frac{3\lfloor n_j/2\rfloor}{2\lfloor n_j/2\rfloor+1}.}
\]
Consequently \(P\) is graph-variation nonexpansive **if and only if** every axis has length at most three. The first possible amplification is \(6/5\) at an axis of length four; the coefficients display the exact plateau \(C_{2m}=C_{2m+1}=3m/(2m+1)\) in one dimension. Every finite product has coefficient strictly below \(3/2\), while the sharp supremum over all factor sizes and dimensions equals \(3/2\). A Boolean product grid can be graph-variation nonexpansive even though its affine projector is not positive: on the two-by-two cube, the indicator of one corner projects to \(-1/4\) at the opposite corner.

## Assumptions and scope
All functions are real-valued and defined on the entire finite Cartesian product. The masses and weights are strictly positive, and each one-dimensional variance \(s_j^2\) is positive because sample sites are strictly ordered. The seminorm vanishes precisely on constant functions since the Cartesian product graph is connected. The quotient by constants therefore carries a norm, and \(P\) preserves constants, so the displayed induced coefficient is well-defined. Factor masses are normalized probabilities; \(\alpha_j\) multiplies every edge of one coordinate direction, while \(w_{j,k}\) is constant along the fibers in that direction. Without these product assumptions the equality is not claimed.

## Proof
**Orthogonal decomposition.** Independence of product coordinates makes the \(d\) centered coordinate functions \(t_{j,i_j}-m_j\) mutually orthogonal, and orthogonal to the constant function. Hence
\[
(Pf)(i_1,\ldots,i_d)=\mathbb E_\mu f+
\sum_{j=1}^d a_j(t_{j,i_j}-m_j),\qquad
 a_j=\frac{1}{s_j^2}\mathbb E_\mu[(t_{j,I_j}-m_j)f(I)].
\]
The edge difference of \(Pf\) along axis \(j\) is \(a_j(t_{j,k+1}-t_{j,k})\); summing it gives
\[
V(Pf)=\sum_{j=1}^d\alpha_j B_j|a_j|.
\]

**Fiberwise discrete integration by parts.** Set \(c_{j,i}=\mu_{j,i}(t_{j,i}-m_j)\). Since \(\sum_i c_{j,i}=0\), summation by parts on every fixed \(x_{-j}\) yields
\[
\sum_i c_{j,i}f(x_{-j},i)=
\sum_{k=1}^{n_j-1}U_{j,k}
\big(f(x_{-j},k+1)-f(x_{-j},k)\big).
\]
Every \(U_{j,k}>0\): the average of the initial \(k\) ordered sites is strictly below the full weighted mean, while the remaining sites lie strictly above the initial block. Substituting this identity into \(a_j\), taking absolute values, and comparing corresponding terms of the input variation gives
\[
\begin{aligned}
V(Pf)&\le\sum_{j=1}^d\frac{\alpha_jB_j}{s_j^2}
\sum_{x_{-j}}\mu_{-j}(x_{-j})
\sum_{k=1}^{n_j-1}U_{j,k}|\Delta_j f(x_{-j},k)|\\
&\le\left(\max_{j,k}\frac{B_jU_{j,k}}{s_j^2w_{j,k}}\right)V(f).
\end{aligned}
\]
This uses no restriction on the signs of the input and works in any finite dimension.

**Exactness and attainment.** Fix any \((j,k)\) and set \(f(i)=\mathbf1_{\{i_j>k\}}\). The only nonzero input edge differences have direction \(j\) and edge position \(k\), so \(V(f)=\alpha_j w_{j,k}\). The orthogonal coefficient of every coordinate \(\ell\ne j\) vanishes by product independence. The coefficient of coordinate \(j\) equals \(U_{j,k}/s_j^2\). Consequently \(V(Pf)=\alpha_jB_jU_{j,k}/s_j^2\), and its quotient is exactly the corresponding entry of the maximum. Taking an optimizing \((j,k)\) proves the equality and finite attainment.

**Uniform-grid formula.** For \(t_i=i-1\) and equal masses on a factor of length \(n\),
\[
 m=(n-1)/2,\quad s^2=(n^2-1)/12,\quad B=n-1,
 \quad U_k=k(n-k)/(2n).
\]
Thus its factor constant is
\[
\max_{1\le k<n}\frac{6k(n-k)}{n(n+1)}
=\frac{6\lfloor n^2/4\rfloor}{n(n+1)}
=\frac{3\lfloor n/2\rfloor}{2\lfloor n/2\rfloor+1}.
\]
For \(n=2,3\) this is one, and for \(n\ge4\) it exceeds one. It is always strictly smaller than \(3/2\) and tends to \(3/2\) as \(n\to\infty\). Taking the maximum of the factor values yields every stated threshold, plateau, and sharp uniform bound. Finally on \(\{0,1\}^2\) with equal masses, the affine projector kernel is \(K(x,y)=\tfrac14[1+(2x_1-1)(2y_1-1)+(2x_2-1)(2y_2-1)]\). Opposite corners give \(-1/4\), completing the positivity contrast. \(\square\)

## Verification
The standalone `verify.py` computes the weighted projection, edge variation, predicted coefficient and actual maximum over every nonconstant binary cut for seven unweighted product boxes up to twelve sites, plus a nonuniform weighted two-by-three example. All calculations are exact rational arithmetic. The enumeration invokes the finite coarea identity for graph variation as an independent test: the induced variation norm of any linear constant-preserving map is attained on an indicator cut. For the asserted infinite families and arbitrary weights, the proof above, rather than finite enumeration, supplies the argument. Run `python verify.py` with Python 3 and no third-party dependencies.

## Relationship to prior work
Multivariate discrete polynomial least squares on product-like probability models is studied by Zhou, Narayan and Xu (arXiv:1401.0894, first posted 2014-01-05), whose stability results treat the sampling matrix and polynomial approximation errors rather than graph-edge total variation. Nochetto and Salgado (arXiv:1211.1069, first posted 2012-11-05) construct a total-variation-diminishing **local averaged interpolation** operator on Cartesian meshes, rather than the **global orthogonal projector** considered here. The previously published *Sharp dimension-free Lipschitz amplification of affine least-squares projections on cubes* concerns continuous cubes with a maximum-coordinate input metric; its conclusion does not imply stability under the sum of discrete edge differences. The published *Sharp affine least-squares norms on products of two simplices and the balanced-dimension law* concerns the \(L^\infty\) operator norm on continuous product domains; no graph-BV norm is determined there. A sharp result for one-dimensional affine fits under complete-pair Gini variation also concerns a different seminorm and does not give the present formula. None of those statements entails the weighted graph-BV identity under the stated product assumptions.

## Limitations
The exact tensorization requires product observation measures and direction-fiber-factorized edge weights. It does not extend as stated to arbitrary irregular sampled graphs, nonproduct sampling, tensor-product multilinear regression, polynomial degrees at least two, or isotropic Euclidean-gradient total variation. The classification concerns a fixed positive sampling law for each finite product; it makes no inference about statistical accuracy of fitting. A historical equivalent in a differently framed tensorization or regression norm study remains possible. There is no claim of independent validation.

## References
1. T. Zhou, A. Narayan and Z. Xu, *Multivariate discrete least-squares approximations with a new type of collocation grid*, arXiv:1401.0894v1, 2014-01-05, https://arxiv.org/abs/1401.0894 (lead archival source; primary published MSC 41A10).
2. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069v1, 2012-11-05, https://arxiv.org/abs/1211.1069.
3. *Sharp dimension-free Lipschitz amplification of affine least-squares projections on cubes*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-dimension-free-lipschitz-amplification-of-affine-least-squ--55bfd3229687.
4. *Sharp affine least-squares norms on products of two simplices and the balanced-dimension law*, published result, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-sharp-affine-least-squares-norms-on-products-of-two-simplices-an--5ad9b6de5c2f.
5. G. Chavent and K. Kunisch, *Regularization of linear least squares problems by total bounded variation*, ESAIM COCV 2 (1997), 359–376, https://doi.org/10.1051/cocv:1997113 (abstract and metadata comparison only).
