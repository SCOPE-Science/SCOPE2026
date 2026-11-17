# Exact boundary-simplex affine projection norm and its surface-volume stability gap

## Finding
Let \(d\ge2\), let \(T\) be a regular \(d\)-simplex, and let \(\mu_\partial\) be normalized \((d-1)\)-dimensional Hausdorff (surface) measure on its boundary. Write \(m=d+1\) and
\[
a_m=m^2-2m+2,\qquad q_m=\frac{a_m}{m(m-1)}.
\]
Let \(P_\partial\) be the real \(L^2(\mu_\partial)\)-orthogonal projector onto restrictions of all affine functions on the ambient affine span of \(T\). Its exact sharp maximum-norm constant is
\[
\boxed{\|P_\partial\|_{L^\infty(\mu_\partial)\to L^\infty(\mu_\partial)}
=\frac{2a_m}{m}q_m^{m-2}-1.}
\]
Exactly the \(m\) vertices of \(T\) are norming evaluation points. For each vertex \(v_i\), the sign of the projection kernel \(K(v_i,\cdot)\) is an extremizing input; the sharp negative output for inputs \(0\le f\le1\) is
\[
-\left(\frac{a_m}{m}q_m^{m-2}-1\right).
\]
For comparison, let \(P_{\mathrm{vol}}\) be the affine orthogonal projector for normalized uniform \(d\)-dimensional volume on the *solid* simplex. Then, in every dimension \(d\ge2\),
\[
\boxed{\|P_\partial\|_{\infty\to\infty}<\|P_{\mathrm{vol}}\|_{\infty\to\infty}=2m\left(\frac{m}{m+1}\right)^{m-1}-1.}
\]
Despite the strict inequality at every finite dimension, both norms have the same leading linear growth, and their exact absolute stability gap has a nonzero limit:
\[
\boxed{\lim_{d\to\infty}\bigl(\|P_{\mathrm{vol}}\|_{\infty\to\infty}-\|P_\partial\|_{\infty\to\infty}\bigr)=\frac2e.}
\]
Here and below the projector norms are taken on their respective measured spaces. The strict comparison is a comparison of two constants, not of the operators on a common domain.

## Assumptions and scope
The simplex is regular, so all facets have equal surface area. Equivalently, the results apply to an arbitrary nondegenerate simplex equipped with the probability measure obtained by selecting one of its \(m\) facets uniformly and then sampling normalized uniform intrinsic volume on that facet; for a nonregular simplex this measure need not equal normalized Hausdorff surface measure. All affine functions are restricted to the boundary, which determines them uniquely. The inputs are real, measurable, and essentially bounded. There are no finite-element continuity constraints or mesh interfaces beyond this single simplex boundary. The parameter \(d\) is an integer at least two.

Write \(\lambda_1,\ldots,\lambda_m\) for barycentric coordinate functions, with \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\) on \(T\). The boundary sampling law chooses a missing index \(J\) uniformly, sets \(\lambda_J=0\), and gives the remaining \(m-1\) coordinates the uniform \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution. Boundaries of the facets overlap only on null sets.

## Proof
**Barycentric second moments and reproducing kernel.** The sampling description and standard simplex integrals give, for distinct \(i,j\),
\[
\mathbb E_\partial[\lambda_i]=\frac1m,\quad
\mathbb E_\partial[\lambda_i^2]=\frac2{m^2},\quad
\mathbb E_\partial[\lambda_i\lambda_j]=\frac{m-2}{m^2(m-1)}.
\]
The covariance matrix of the centered barycentric coordinates has eigenvalue \(1/[m(m-1)]\) on the zero-sum subspace. Consequently the exact affine reproducing kernel, normalized for probability measure, is
\[
K(x,y)=1+m(m-1)\left(\sum_{i=1}^m\lambda_i(x)\lambda_i(y)-\frac1m\right)
=m(m-1)\sum_i\lambda_i(x)\lambda_i(y)-(m-2).
\]
It satisfies \(\int K(x,y)\,d\mu_\partial(y)=1\) and \((P_\partial f)(x)=\int K(x,y)f(y)\,d\mu_\partial(y)\).

**Location and sharpness of the norm.** For a fixed \(x\), the evaluation norm is \(N(x)=\int|K(x,y)|\,d\mu_\partial(y)\). The map \(x\mapsto N(x)\) is convex in barycentric coordinates, and
\[
N(x)\le\sum_i\lambda_i(x)N(v_i)=N(v_1)
\]
by facet symmetry. This inequality is strict whenever at least two barycentric weights of \(x\) are positive: choose distinct \(i,j\) with positive weights. On a positive-measure neighborhood of vertex \(v_i\) along the boundary, \(K(v_i,y)>0\) while \(K(v_j,y)<0\); the triangle inequality in the displayed convex combination is strict on a positive-measure set. Thus the only norming locations are vertices. Although vertices have zero surface measure, every projected output is continuous on the entire boundary and the surface measure has full topological support; hence its essential supremum equals its ordinary supremum over the boundary. The actual operator norm equals \(\sup_x N(x)\) because the input \(f(y)=\operatorname{sgn}K(v_i,y)\) realizes \(N(v_i)\) at \(v_i\), with values arbitrarily close on positive-measure neighborhoods.

**Exact vertex integral.** At \(v_1\),
\[
K(v_1,y)=m(m-1)\lambda_1(y)-(m-2).
\]
Set \(\tau=(m-2)/[m(m-1)]\). Under boundary sampling, \(\lambda_1=0\) with probability \(1/m\), and with probability \((m-1)/m\) it has density \((m-2)(1-t)^{m-3}\) on \(0<t<1\). The negative-kernel mass is therefore
\[
\begin{aligned}
C_\partial&=\int(-K(v_1,y))_+\,d\mu_\partial(y)\\
&=\frac{m-2}{m}+\frac{(m-1)(m-2)}m
\int_0^\tau\bigl((m-2)-m(m-1)t\bigr)(1-t)^{m-3}\,dt\\
&=\frac{a_m}{m}\left(\frac{a_m}{m(m-1)}\right)^{m-2}-1.
\end{aligned}
\]
Since the kernel integrates to one, \(N(v_1)=1+2C_\partial\), establishing the norm formula. Taking \(f=\mathbf1_{\{K(v_1,\cdot)<0\}}\) gives output \(-C_\partial\) at \(v_1\); equivalently \(\operatorname{sgn}K(v_1,\cdot)\) attains the norm.

**Strict comparison with volume.** For normalized uniform volume, the standard barycentric moment computation yields the comparison norm \(2m(m/(m+1))^{m-1}-1\). Put \(\delta=2/[m^2(m-1)]\). Exact algebra gives
\[
\frac{\|P_\partial\|+1}{\|P_{\mathrm{vol}}\|+1}
=\left(1-\frac1m+\frac2{m^3}\right)(1+\delta)^{m-2}.
\]
For \(k=m-2\), one has \(k\delta<1\) and the finite binomial bound \((1+\delta)^k\le1/(1-k\delta)\). Finally,
\[
(1-k\delta)-\left(1-\frac1m+\frac2{m^3}\right)
=\frac{m(m-1)(m-2)+2}{m^3(m-1)}>0.
\]
This proves the universal strict inequality without reliance on sample dimensions.

**Asymptotic stability gap.** Direct Taylor expansion at \(m^{-1}=0\) gives
\[
(m-2)\log q_m=-1+\frac{5}{2m}+O(m^{-2}),\quad
(m-1)\log\frac{m}{m+1}=-1+\frac{3}{2m}+O(m^{-2}).
\]
Together with \(a_m/m=m-2+2/m\), these imply
\[
\|P_\partial\|+1=\frac{2m}{e}+\frac1e+O(m^{-1}),\quad
\|P_{\mathrm{vol}}\|+1=\frac{2m}{e}+\frac3e+O(m^{-1}).
\]
Subtracting establishes the limit \(2/e\).

## Verification
The standalone `verify_boundary_simplex.py` constructs the covariance data directly from the facet mixture, integrates the negative kernel exactly using rational polynomial integration for all integers \(3\le m\le18\), and compares with the closed formula. It also symbolically checks the universal strict-comparison certificate and the asymptotic constant. Reproduce by running `python verify_boundary_simplex.py` with Python 3 and SymPy. The finite tests corroborate, but do not replace, the all-dimensional convexity, binomial-inequality, and Taylor-expansion arguments in the proof.

## Relationship to prior work
Sharp max norms of orthogonal polynomial and spline projectors are a classical stability question. Foucart (2006) studies orthogonal spline projectors on intervals and polynomial comparisons; Crouzeix and Thomée (1987) treat stability of finite-element projections on domains under mesh assumptions. Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, first posted 13 May 2010) establish uniform boundedness for appropriate kernel-generated spaces on smooth manifolds. Their hypotheses and conclusions do not give the present singular equal-facet probability measure or its dimension-explicit exact constant.

The known exact affine projector norm for the *solid*, uniformly sampled simplex is explicitly included as a comparator, not a new assertion. An earlier general formula for interior Dirichlet sampling with all concentration parameters strictly positive does not directly apply: the boundary law is a mixture of singular facet measures and its Gram matrix is that of the mixture, not the individual Dirichlet projectors. Neither the volume formula nor its positive-parameter Dirichlet extension immediately implies the strict surface-volume gap; the new proof computes the singular-mixture kernel and supplies a universal inequality. Algebraically equivalent boundary formulas may still exist in unindexed literature.

## Limitations
Only affine degree-one projection is treated. The surface statement requires a regular simplex or an equal-facet sampling convention; for a nonregular simplex with raw Hausdorff surface measure, facets have unequal weights and the formula can fail. It does not determine projection norms on arbitrary polytope boundaries, for higher polynomial degrees, or for global conforming finite-element spaces. The source comparison cannot eliminate every unpublished or unindexed equivalent formula; independent mathematical audit has not been carried out.

## References
1. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424 (first posted 13 May 2010), https://arxiv.org/abs/1005.2424.
2. S. Foucart, *On the value of the max-norm of the orthogonal projector onto splines with multiple knots*, Journal of Approximation Theory 140 (2006), 154–177, DOI:10.1016/j.jat.2005.12.004; author copy https://foucart.github.io/publi/SplineProj2.pdf.
3. M. Crouzeix and V. Thomée, *The Stability in \(L_p\) and \(W_p^1\) of the \(L_2\)-Projection onto Finite Element Function Spaces*, Mathematics of Computation 48 (1987), 521–532, DOI:10.1090/S0025-5718-1987-0878688-2.
