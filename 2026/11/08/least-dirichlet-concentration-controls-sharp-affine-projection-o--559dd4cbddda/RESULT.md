# Least Dirichlet concentration controls sharp affine projection on every simplex

## Finding

Let \(N\ge2\) and let \(\mu\) be the Dirichlet probability measure with **arbitrary strictly positive** concentration parameters \(\alpha_1,\ldots,\alpha_N\) on the barycentric simplex. The exact \(L^\infty\) norm of the real \(L^2(\mu)\)-orthogonal projector onto affine functions depends on the parameter vector only through its total \(T\) and its smallest component \(a_*=\min_i\alpha_i\). More sharply, holding \(T\) fixed, its vertex evaluation norm is strictly decreasing in the corresponding concentration parameter. All maximizing evaluation points, all real norming input functions, and the sharp negative overshoot are identified.

Put \(z=a/(T+1)\), and let \(I_z(p,q)=B_z(p,q)/B(p,q)\) denote the regularized incomplete beta integral. Set
\[
 L_T(a)=1+2\left[T I_{a/(T+1)}(a,T-a)-(T+1)I_{a/(T+1)}(a+1,T-a)\right],\qquad 0<a<T.
\]
Then
\[
 \boxed{\|P\|_{L^\infty(\mu)\to L^\infty(\Delta)}=L_T(a_*),\qquad a_* =\min_{1\le i\le N}\alpha_i.}
\]
The function \(L_T\) is strictly decreasing on \((0,T)\). Exactly the vertices \(e_i\) with \(\alpha_i=a_*\) have point-evaluation norm \(\|P\|\). At a norming vertex, every real norming input \(f\) of essential supremum norm \(1\) equals \(\pm\operatorname{sgn}[(T+1)y_i/\alpha_i-1]\) almost everywhere; conversely these inputs attain the operator norm.

For inputs \(0\le f\le1\) almost everywhere, the globally sharp negative value \(-\sup_{x,f}[-(Pf)(x)]\) is controlled by
\[
 \boxed{\sup_{x\in\Delta,\,0\le f\le1}[-(Pf)(x)]=\tfrac12(L_T(a_*)-1).}
\]
As \(a\downarrow0\) with \(T\) fixed, \(L_T(a)\to1+2T\); as \(a\uparrow T\), \(L_T(a)\to1\). For fixed \(a>0\),
\[
 \boxed{\lim_{T\to\infty}\frac{L_T(a)}{T}=\frac{2a^{a-1}e^{-a}}{\Gamma(a)}.}
\]
In particular, with \(\alpha_i=a\) for each of \(N\) vertices,
\[
 \boxed{\lim_{N\to\infty}\frac{\|P\|}{N}=\frac{2a^{a}e^{-a}}{\Gamma(a)}.}
\]

## Assumptions and scope

The domain \(\Delta=\{x\in\mathbb R^N:x_i\ge0,\sum_i x_i=1\}\) is an \((N-1)\)-simplex in barycentric coordinates, \(N\ge2\). The measure \(\mu\) has strictly positive density proportional to \(\prod_i y_i^{\alpha_i-1}\) on the relative interior. The orthogonal projector is defined using the real inner product of \(L^2(\mu)\), with range the space of real affine functions (dimension \(N\)). Its output has a unique continuous affine representative; the norm at the output is the maximum over the closed simplex, not an essential supremum with a degenerate boundary measure. Because \(\mu\) has full relative-interior support, the essential supremum and continuous supremum of any affine output are equal.

## Proof

**1. Kernel from a finite Gram inverse.** For the barycentric random vector \(Y\sim\mu\), the Dirichlet moment formula is
\[
 G_{ij}=\mathbb E[Y_iY_j]=\frac{\alpha_i(\alpha_j+\mathbf 1_{i=j})}{T(T+1)}.
\]
The matrix is positive definite and direct multiplication, or the rank-one inverse identity, yields
\[
 (G^{-1})_{ij}=\frac{T(T+1)}{\alpha_i}\mathbf1_{i=j}-T.
\]
Since barycentric linear forms span the affine functions, the projection kernel is
\[
 K(x,y)=x^{\mathsf T}G^{-1}y=T(T+1)\sum_i\frac{x_i y_i}{\alpha_i}-T.
\]
Thus \((Pf)(x)=\int K(x,y)f(y)\,d\mu(y)\), and \(\int K(x,y)\,d\mu(y)=1\).

**2. Vertex reduction and strict nonvertex exclusion.** Define \(K_i(y)=K(e_i,y)=T[(T+1)y_i/\alpha_i-1]\). Then \(K(x,y)=\sum_i x_i K_i(y)\) for any \(x\in\Delta\). Therefore
\[
 \int|K(x,y)|\,d\mu(y)\le\sum_i x_i\int|K_i(y)|\,d\mu(y)\le\max_i\int|K_i(y)|\,d\mu(y).
\]
If \(x_i,x_j>0\) for distinct indices, take \(y\) in a small relative-interior neighborhood of \(e_i\). There \(K_i(y)>0\) and \(K_j(y)<0\). This open neighborhood has positive \(\mu\)-measure, so the first triangle inequality is strictly sharp. Hence no nonvertex point maximizes. At a vertex, equality in \(\left|\int K_i f\right|\le\int|K_i|\) for a real \(f\) with \(\|f\|_\infty=1\) forces \(f=\pm\operatorname{sgn}K_i\) almost everywhere; the zero hyperplane of \(K_i\) has \(\mu\)-measure zero.

**3. Exact beta integral.** Fix \(i\) and put \(a=\alpha_i\), \(b=T-a>0\), \(z=a/(T+1)\). The marginal \(Y_i\) is \(\operatorname{Beta}(a,b)\). Since \(\int K_i\,d\mu=1\),
\[
 \int|K_i|\,d\mu=1+2\mathbb E[(-K_i)_+].
\]
Using \(\mathbb E[Y_i\mathbf1_{Y_i<z}]=(a/T)I_z(a+1,b)\) gives
\[
 \mathbb E[(-K_i)_+]=T I_z(a,b)-(T+1)I_z(a+1,b).
\]
This is the displayed \(L_T(a)\). The same mean-one identity shows the sharp negative defect for \(0\le f\le1\) is the largest negative kernel mass, namely \((\|P\|-1)/2\), attained by the indicator of the negative kernel region at a norming vertex.

**4. Strict concentration ordering (the essential structural step).** Fix \(T\) and \(0<a<b<T\). On one probability space choose \((X_1,X_2,X_3)\sim\operatorname{Dirichlet}(a,b-a,T-b)\). Then \(X_1\sim\operatorname{Beta}(a,T-a)\), \(X_1+X_2\sim\operatorname{Beta}(b,T-b)\), and the aggregation property gives
\[
 \mathbb E[X_1/a\mid X_1+X_2]=(X_1+X_2)/b.
\]
Apply conditional Jensen to the convex kink function \(\varphi(v)=T|(T+1)v-1|\):
\[
 L_T(a)=\mathbb E\varphi(X_1/a)\ge\mathbb E\varphi((X_1+X_2)/b)=L_T(b).
\]
For every aggregate value \(s>a/(T+1)\), the conditional distribution of \(X_1/a\), given \(X_1+X_2=s\), has positive density throughout \((0,s/a)\). Its support straddles the unique kink \(1/(T+1)\), so Jensen's inequality is **strict** on that event. This event has positive probability because \(s\) has an interior beta density. Hence \(L_T(a)>L_T(b)\) for all \(0<a<b<T\). This orders all vertices, including ties, and proves the norm and equality classification.

**5. Limits.** As \(a\downarrow0\) at fixed \(T\), the two beta CDFs in the formula tend respectively to \(1\) and \(0\); hence \(L_T(a)\to1+2T\). As \(a\uparrow T\), the beta distribution converges to a point mass at \(1\), while \(a/(T+1)\) stays strictly below \(1\), giving \(L_T(a)\to1\).

For fixed \(a>0\), couple independent gamma random variables \(G_a\sim\operatorname{Gamma}(a,1)\) and \(H_{T-a}\sim\operatorname{Gamma}(T-a,1)\), with \(Y=G_a/(G_a+H_{T-a})\). The gamma law of large numbers implies \(TY\Rightarrow G_a\). Uniform integrability follows from the explicit bounded second moment \(\mathbb E[(TY/a)^2]=T(a+1)/(a(T+1))\), so
\[
 \frac{L_T(a)}{T}=\mathbb E\left|\frac{T+1}{a}Y-1\right|\longrightarrow\mathbb E|G_a/a-1|.
\]
Integration at the gamma crossing \(G_a=a\) yields \(\mathbb E|G_a/a-1|=2a^{a-1}e^{-a}/\Gamma(a)\). When there are \(N\) equal Dirichlet parameters \(a\), substitute \(T=Na\) and multiply by \(T/N=a\) to obtain the last displayed limit.

## Verification

The attached `checker.py` performs exact rational Gram-matrix and integer beta-tail checks on 373 parameter tuples, including all parameter combinations with 2–5 vertices and entries 1–3, and exact recovery of the uniform-volume case. It separately checks 24 noninteger beta-integral/quadrature and strict-order cases and 4 large-concentration gamma limits. These tests confirm identities and representative regimes; the universal strict inequality and full equality classification are proved by the analytic steps above, not by finite experiments.

For the asymmetric example \((\alpha_1,\alpha_2,\alpha_3)=(1/2,2,7/2)\), the total concentration is \(T=6\), and the vertex evaluation norms are approximately \(6.1938867065\), \(3.0905575058\), and \(2.0371832716\). Only the first vertex attains the operator norm.

To reproduce the finite checks, run `python checker.py` in a Python environment with SymPy and SciPy installed.

## Relationship to prior work

Waldron's 2007 treatment of Jacobi orthogonal polynomials with arbitrary positive simplex parameters develops the underlying weighted orthogonality, degreewise projections, and their limits as weights become singular. This work uses those established objects, but the sharp \(L^\infty\) norm, the **strict least-concentration selection theorem**, the complete norming evaluation/input classification, and the large-total gamma law are not formulas asserted there. Hangelbroek–Narcowich–Sun–Ward (arXiv:1005.2424) study bounded least-squares projections for kernel spaces over manifolds, not this exact simplex-Dirichlet endpoint constant. The known uniform-volume simplex affine projector formula is recovered at \(\alpha_i=1\), when \(L_N(1)=2N[N/(N+1)]^{N-1}-1\), and **is not claimed as novel**. Unlike vertex-atomic perturbations of uniform volume, continuous asymmetric Dirichlet densities have full interior support and yield the beta-splitting strict order.

## Limitations

Only real affine \(L^2\)-orthogonal projection, strictly positive Dirichlet parameters, and continuous-affine output are covered. The theorem does not claim analogous results for higher polynomial degree, complex coefficients, arbitrary non-Dirichlet densities, or measures with atoms. The kernel/Dirichlet moment identities and beta aggregation are standard; the novelty claim is limited to their sharp endpoint optimization and consequences. Mathematical-record searches and inspected primary sources cannot exclude an unindexed equivalent or an implicit stronger pre-existing theorem. No independent mathematical validation has been performed.

## References

1. S. Waldron, *Multivariate Jacobi polynomials with singular weights*, Technical Report dated 13 February 2007, later *East J. Approx.* **13** (2007), 163–183. Primary accessible preprint: https://www.math.auckland.ac.nz/~waldron/Preprints/Jacobi-singular/jacobi-singular.pdf ; abstract: https://www.math.auckland.ac.nz/~waldron/Preprints/Jacobi-singular/jacobi-singular.html .
2. T. Hangelbroek, F. J. Narcowich, X. Sun, J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424 (initial posting 13 May 2010). https://arxiv.org/abs/1005.2424 .
3. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, publicly indexed 4 October 2026, exact uniform-volume case. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 .
