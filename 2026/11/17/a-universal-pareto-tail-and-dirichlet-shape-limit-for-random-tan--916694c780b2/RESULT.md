# A universal Pareto tail and Dirichlet shape limit for random tangent polygons

## Finding
Fix an integer \(n\geq 3\) and a real concentration parameter \(\alpha>0\). Sample a vector \((Y_1,\ldots,Y_n)\) with the symmetric \(\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\) distribution, and a uniform angular offset independent of it. Place tangency normals at the cumulative angles \(2\pi Y_i\) around the unit circle. Let \(B\) denote the event that the supporting tangent halfplanes form a bounded polygon, and let \(A\) denote that polygon's area on \(B\).

Write \(I_z(a,b)\) for the regularized incomplete beta function and \(\mathrm B(a,b)\) for Euler's beta function. Then
\[
 p_{n,\alpha}:=\Pr(B)=1-n\bigl[1-I_{1/2}(\alpha,(n-1)\alpha)\bigr]>0.
\]
For every fixed \(n\geq3\) and \(\alpha>0\),
\[
 \boxed{\lim_{x\to\infty}x\Pr(A>x\mid B)
 =C_{n,\alpha}:=\frac{n\,2^{2-n\alpha}}{\pi\,\mathrm B(\alpha,(n-1)\alpha)\,p_{n,\alpha}}.}
\]
In particular, for \(\alpha=1\) (independent uniform tangency points),
\[
 p_{n,1}=1-\frac{n}{2^{n-1}},\qquad
 C_{n,1}=\frac{n(n-1)}{\pi\,2^{n-2}(1-n/2^{n-1})}.
\]
For each \(q>0\), \(\mathbb E[A^q\mid B]<\infty\) if and only if \(q<1\). Although \(A\) is finite almost surely on \(B\), its conditional mean is infinite for every finite \(n\ge3\) and \(\alpha>0\).

There is a joint geometric limit. On \(\{A>x\}\cap B\), let \(J\) be the index of the largest angular gap (unique almost surely), \(G_{\max}=2\pi Y_J\), and let \(Z\) be the \(n-1\) remaining gaps, in cyclic order, divided by their sum. Then, conditionally on \(A>x,B\),
\[
 \left(J,\frac{x(\pi-G_{\max})}{2},Z,\frac{A}{x}\right)
 \Longrightarrow\left(J_\infty,U,Z_\infty,U^{-1}\right),
\]
where \(J_\infty\) is uniform on \(\{1,\ldots,n\}\), \(U\) is uniform on \((0,1)\), and \(Z_\infty\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\) in dimension \(n-1\); all three are independent. The independent global rotation remains Haar-uniform. Thus the conditional excess-area ratio converges to the Pareto law \(\Pr(U^{-1}>t)=1/t\) for \(t\ge1\).

## Assumptions and scope
The tangency polygon is the intersection of the closed supporting halfplanes \(\{z\in\mathbb R^2:z\cdot(\cos\theta_i,\sin\theta_i)\le1\}\), with normals ordered cyclically. Its interior contains the unit disk. Strict positivity of Dirichlet coordinates is almost sure. The polygon is bounded exactly when every cyclic normal gap \(G_i=2\pi Y_i\) is strictly less than \(\pi\). All asymptotics keep \(n\) and \(\alpha\) fixed while the area threshold \(x\to\infty\); there is no uniformity claim in either parameter. Equality at a semicircle boundary is a probability-zero event.

## Proof
**Geometry and the conditioning event.** Consecutive supporting tangents meeting at angular separation \(G_i<\pi\) contribute \(2\tan(G_i/2)\) to total perimeter: each adjacent edge has tangent-segment length \(\tan(G_i/2)\) from its point of tangency to the intersection. Therefore, using inradius one and the area-perimeter identity,
\[
 A=\sum_{i=1}^n T_i,\qquad T_i=\tan(\pi Y_i)>0\quad\text{on }B.
\]
A convex polygon containing the unit disk is bounded if and only if its outward normal directions have no covering open semicircle, equivalently \(\max_iY_i<1/2\). Because \(\sum_iY_i=1\), events \(\{Y_i>1/2\}\) are disjoint. The marginal law is \(Y_i\sim\operatorname{Beta}(\alpha,(n-1)\alpha)\), which gives the stated exact \(p_{n,\alpha}\). A neighborhood of equal gaps has positive probability, so this probability is positive.

**One nearly semicircular gap.** Put \(\beta=(n-1)\alpha\). A particular \(Y_i\) has beta density
\[
 f(y)=\frac{y^{\alpha-1}(1-y)^{\beta-1}}{\mathrm B(\alpha,\beta)},\quad 0<y<1,
 \qquad f(1/2)=\frac{2^{2-n\alpha}}{\mathrm B(\alpha,\beta)}.
\]
The event \(\{T_i>x\}\) on \(B\) means \(\arctan(x)/\pi<Y_i<1/2\), an interval of length \(1/(\pi x)+O(x^{-3})\). Conditional on \(Y_i=y\), the vector of remaining \(n-1\) normalized coordinates is exactly symmetric Dirichlet with parameter \(\alpha\), independent of \(y\). As \(y\uparrow1/2\), the probability that each remaining coordinate is below \(1/2\) tends to one: their total tends to \(1/2\), and a Dirichlet vector has no unit coordinate. Bounded convergence thus yields
\[
 \Pr(T_i>x,B)=\frac{f(1/2)}{\pi x}+o(x^{-1}).
\]

**Two nearly semicircular gaps are negligible.** The joint density of \((Y_i,Y_j)\) for distinct indices is proportional to \(y_i^{\alpha-1}y_j^{\alpha-1}(1-y_i-y_j)^{(n-2)\alpha-1}\) on their simplex. If both \(T_i,T_j>c x\) on \(B\), both coordinates lie within \(O(x^{-1})\) of \(1/2\). Integrating their joint density over this corner gives
\[
 \Pr(T_i>cx,T_j>cx,B)=O\!\left(x^{-1-(n-2)\alpha}\right)=o(x^{-1})
\]
for each fixed \(c>0\). Inclusion-exclusion therefore gives \(\Pr(\max_iT_i>x,B)\sim n f(1/2)/(\pi x)\). To pass from the maximum to the sum, fix \(0<\eta<1\). If \(\sum_iT_i>x\) but \(\max_iT_i\le (1-\eta)x\), then one \(T_i\ge x/n\) and a second \(T_j\ge\eta x/(n-1)\). This event is \(o(x^{-1})\). Consequently
\[
 \Pr(\max_iT_i>x,B)\le\Pr(A>x,B)
 \le\Pr(\max_iT_i>(1-\eta)x,B)+o(x^{-1}).
\]
Letting \(x\to\infty\) and then \(\eta\downarrow0\) proves the tail constant after dividing by \(p_{n,\alpha}\). The same squeeze implies that \(\{A>x,B\}\) and \(\{\max_iT_i>x,B\}\) differ by probability \(o(x^{-1})\).

**Conditional shape.** Condition on the unique index \(i\) with \(T_i>x\). On this event \(Y_i\) lies in a shrinking interval immediately below \(1/2\), whose rescaled coordinate \(\pi x(1/2-Y_i)=x(\pi-G_i)/2\) converges to a uniform \((0,1)\) variable by continuity and positivity of the beta density. The independent normalized remainder is Dirichlet, and the conditioning \(B\) changes its distribution by a vanishing amount. Exchangeability makes \(i\) asymptotically uniform. Since \(\tan(\pi Y_i)/x\to U^{-1}\) and every other tangent contribution divided by \(x\) tends to zero in probability, the displayed joint limit follows. The area-ratio Pareto law and the global-rotation assertion are immediate.

**Moments.** For any nonnegative random variable, \(\mathbb E[A^q\mid B]=q\int_0^\infty t^{q-1}\Pr(A>t\mid B)\,dt\). The established strictly positive tail constant makes this integral finite for \(0<q<1\) and divergent for \(q\ge1\).

## Verification
An independently implemented sampler draws gamma variates, normalizes to Dirichlet gaps, rejects \(\max Y_i\ge 1/2\), and evaluates the exact geometric area. Four parameter combinations, \((n,\alpha)=(3,1/2),(3,1),(4,1),(4,2)\), each use 1,800,000 samples. The sample boundedness frequencies agree with the beta formula, and \(x\Pr(A>x\mid B)/C_{n,\alpha}\) lies within 0.05 of one for thresholds 120, 240 and 480 in these trials. These are finite-sample sanity checks, not the proof of the limiting theorem. Run `python check_tail.py`; NumPy and SciPy are required.

## Relationship to prior work
Schlemm (2014) analyzed the largest uniform circular spacing through the Dirichlet distribution, providing an exact-dated archival spacing anchor. Xu (2015) introduced random circumscribing polygons and observed the boundedness pathology and unbounded possible areas. Wang and Xu (2018) extended the random cyclic polygon model to symmetric Dirichlet gaps, analyzing large-\(n\) convergence. Wang, Li, and Xu (2023) give full-text formulas for these inscribed/circumscribed polygons and large-\(n\) Gaussian/extrapolation results. None of the available inspected material states the fixed-\(n\) exact Pareto-tail constant or the conditional extreme-gap shape limit; in particular, an \(n\to\infty\) central limit theorem does not imply a fixed-\(n\) infinite-mean statement. The 2015 and 2018 article full texts were unavailable for inspection, so historical priority of the precise fixed-\(n\) result remains provisional.

## Limitations
The formulas concern the unit circle and Haar-rotated symmetric Dirichlet normal gaps, conditional on geometric boundedness. They do not give a joint \(n\to\infty\), \(x\to\infty\) limit, nor numerical estimation guarantees from finite samples. No claim of independent validation or exhaustive historical uniqueness is made. An inaccessible earlier full article with the same underlying model remains an originality risk.

## References
1. E. Schlemm, *Limiting distribution of the maximal distance between random points on a circle: A moments approach*, arXiv:1405.6114, first posted 2014-05-23. https://arxiv.org/abs/1405.6114
2. W.-Q. Xu, *Random circumscribing polygons and approximations of π*, Statistics & Probability Letters 106 (2015), 52–57. https://doi.org/10.1016/j.spl.2015.06.026
3. S. Wang and W.-Q. Xu, *Random cyclic polygons from Dirichlet distributions and approximations of π*, Statistics & Probability Letters 140 (2018), 84–90. https://doi.org/10.1016/j.spl.2018.05.007
4. S. Wang, Z. Li and W.-Q. Xu, *Nonlinear random extrapolation estimates of π under Dirichlet distributions*, J. Numer. Anal. Approx. Theory 52 (2023), 273–294, full text examined. https://ictp.acad.ro/jnaat/journal/article/view/1360/1463
