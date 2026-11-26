# Sharp affine least-squares stability on balanced complete multipartite metric graphs

## Finding

Let \(r\ge 3\) and \(s\ge2\) be integers, and let \(G_{r,s}=K_{s,\ldots,s}\) be the complete \(r\)-partite graph with \(s\) vertices in each part. Realize each edge as a unit interval and equip this compact metric graph with arclength measure. Let \(P_{r,s}\) be the real \(L^2\)-orthogonal projection onto the space of continuous functions affine on each edge, without derivative-matching conditions at vertices. Put \(t=2r-3\). Then

\[
\boxed{\|P_{r,s}\|_{L^\infty\to L^\infty}=2+\frac{t(s-4)+1}{3t(ts+1)}.}
\]

Every graph vertex, and no edge-interior point, has maximal evaluation norm. Each norm is attained on measurable inputs of modulus one, explicitly the sign of the corresponding reproducing-kernel row. The amplification threshold is independent of the number of parts:

\[
\|P_{r,s}\|<2\quad(s=2,3),\qquad
\|P_{r,s}\|>2\quad(s\ge4).
\]

The norm is strictly increasing with \(s\) for fixed \(r\). For fixed \(s\), increasing \(r\) strictly **increases** the norm when \(s=2,3\), but strictly **decreases** it when \(s\ge4\). The exact endpoints of the family are

\[
\boxed{\frac{121}{63}\le\|P_{r,s}\|<\frac{19}{9},\qquad
\inf_{r,s}\|P_{r,s}\|=\frac{121}{63}\ (r,s)=(3,2),\quad
\sup_{r,s}\|P_{r,s}\|=\frac{19}{9}\ \text{(unattained)}.}
\]

More precisely, for fixed \(r\),
\[
\lim_{s\to\infty}\|P_{r,s}\|=2+\frac1{3(2r-3)},
\]
whereas for fixed \(s\), \(\lim_{r\to\infty}\|P_{r,s}\|=2\), approached from below for \(s=2,3\) and from above for \(s\ge4\).

## Assumptions and scope

Every one of the \(\binom r2s^2\) edges has length one and density one; vertices have no atomic mass. The \(L^\infty\) norm is the essential supremum with respect to arclength, and the projection acts from real \(L^\infty(G_{r,s})\) into continuous edgewise-affine functions. At an edge endpoint, the evaluation norm means the norm of the bounded linear functional \(f\mapsto (P_{r,s}f)(v)\). The result concerns the equal-part subfamily, not arbitrary multipartite sizes.

## Proof

**1. Nodal mass matrix.** Denote by \(\phi_v\) the standard vertex hat function, equal to one at \(v\), zero at other vertices, and affine on each edge. Put \(d=(r-1)s\), so every vertex has degree \(d\). Direct integration of the products of hats on a unit edge gives the Gram matrix
\[
M_{vw}=\langle\phi_v,\phi_w\rangle
=\frac16(2d\,\mathbf1_{v=w}+\mathbf1_{v\sim w}),\qquad Q=6M=2dI+A.
\]
Here \(A\) is the adjacency matrix, not a distance matrix. The decomposition of vertex vectors into within-part mean-zero vectors, part-constant vectors of total mean zero, and global constants makes \(Q\) act by the respective positive scalars \(2d\), \(s(2r-3)\), and \(3d\). Consequently \(Q\) is invertible. With \(t=2r-3\) and
\[
\beta=\frac1{6s^2(r-1)t},
\]
its inverse row at any vertex \(v\) has the three exact values
\[
(Q^{-1})_{vw}=\begin{cases}
(3st+1)\beta,&w=v,\\
\beta,&w\ne v\text{ and }w\text{ is in the part of }v,\\
-2\beta,&w\text{ is in a different part}.
\end{cases}
\]
These formulas are checked directly on the three invariant subspaces: the row differences in one part have eigenvalue \((2d)^{-1}\), part contrasts have eigenvalue \((st)^{-1}\), and the constant row sum equals \((3d)^{-1}\).

**2. Exact endpoint kernel and its \(L^1\) norm.** The reproducing kernel for evaluation of \(Pf\) at \(v\), at an edge \(e=\{a,b\}\) parametrized from \(a\) to \(b\) by \(u\in[0,1]\), is
\[
K_v(e,u)=6\big((Q^{-1})_{va}(1-u)+(Q^{-1})_{vb}u\big).
\]
The \(L^\infty\)-norm of the evaluation functional is \(\int_G|K_v(y)|\,dy\). Set \(T=3st+1\). Relative to vertex \(v\), there are precisely \(d\) incident edges with kernel \(6\beta[T(1-u)-2u]\), \((s-1)d\) other edges having an endpoint in the part of \(v\) with kernel \(6\beta[(1-u)-2u]\), and \(\binom{r-1}{2}s^2\) edges between two other parts with constant kernel \(-12\beta\).

For \(x>0\), an exact one-zero integration gives
\[
\int_0^1|x(1-u)-2u|\,du=\frac{x^2+4}{2(x+2)}.
\]
Thus, since the second integral with \(x=1\) is \(5/6\), the evaluation norm is
\[
6\beta\left[
 d\frac{T^2+4}{2(T+2)}+
 (s-1)d\frac56+
 (r-1)(r-2)s^2
\right].
\]
Substitution of \(d=(r-1)s\), \(T=3st+1\), and \(\beta\) reduces this rational expression exactly to
\[
2+\frac{t(s-4)+1}{3t(ts+1)}.
\]
This value is independent of \(v\), by vertex transitivity. A measurable sign input \(f=\operatorname{sgn} K_v\) attains the value at \(v\); no continuous sign-input requirement is imposed.

**3. Strictly smaller interior evaluations.** At an interior point \(x\) of an edge joining \(v\) to \(w\), the evaluation kernel is a nontrivial convex combination of \(K_v\) and \(K_w\), because every projected function is affine there. The triangle inequality bounds its integral by the common endpoint value. It is strict: choose an edge from \(v\) to a vertex in a third part. On a positive-length interval near \(v\), the row \(K_v\) is strictly positive, while \(K_w\) is strictly negative, as seen from the three entries of \(Q^{-1}\). A third part exists because \(r\ge3\). Hence the absolute-value triangle inequality is strict on a set of positive measure. No interior point is norming.

**4. Threshold, monotonicity and sharp envelope.** Since \(t\ge3\), the sign of the norm minus two is the sign of \(t(s-4)+1\). For \(s=2,3\) it is negative; for every integer \(s\ge4\) it is positive. Treating the rational expression temporarily as a smooth function in positive real \(s\), its derivative is
\[
\frac{\partial}{\partial s}\|P_{r,s}\|=\frac{4t}{3(ts+1)^2}>0.
\]
For the real parameter \(t\), its derivative is
\[
\frac{\partial}{\partial t}\|P_{r,s}\|
=-\frac{t^2s(s-4)+2ts+1}{3t^2(ts+1)^2}.
\]
For \(s\ge4\) the numerator is positive. For \(s=2\) or \(3\) and \(t\ge3\) it is negative: the respective expressions are \(-4t^2+4t+1\) and \(-3t^2+6t+1\). This proves the claimed strict monotonicity in \(r\). The two one-parameter limits follow by dividing the rational expression by its highest relevant power. Increasing in \(s\), the family minimum occurs at \(s=2\); increasing in \(r\) there, it occurs at \(r=3\), where the norm is \(121/63\). Finally, for each \(r\), the strict increasing-in-\(s\) limit equals \(2+1/(3t)\). This is maximal for \(t=3\) and equals \(19/9\); finite \(s\) never achieves it.

## Verification

The included `verify_turan_projector.py` performs independent rational inversion of the nodal mass matrices for ten \((r,s)\) pairs, compares every matrix entry against the three-class inverse, integrates all endpoint reproducing-kernel rows exactly, and checks strict interior evaluation inequalities at three rational positions. In addition, exact rational finite-parameter tests compare the threshold and monotonicity formulas on a large grid. Running `python verify_turan_projector.py` yields `ALL_BALANCED_MULTIPARTITE_P1_CHECKS_OK`. The all-parameter conclusions are proved by the displayed matrix decomposition and algebra, not by finite computation.

## Relationship to prior work

Classical interval-spline theory establishes dimension-free bounds for real \(L^2\) spline projectors; Kayumov's 2004 work studies exponential and trigonometric second-order \(L\)-splines on intervals [1]. Oswald's 2006 study constructs higher-dimensional finite-element triangulations with unbounded \(L^\infty\) projection constants [2]. Hangelbroek, Narcowich, Sun and Ward study uniformly stable least-squares projections generated by localized kernels on manifolds [3]. These results supply context and general methods, but none of the inspected statements has the present arclength metric-graph family, the exact rational norm, or its four-vertices-per-part transition as an implication. Boman's 2006 paper [4] gives weighted finite-element estimates; its full text was not accessible for a decisive all-formulations comparison. The exact claims here are restricted to the explicitly defined complete multipartite graph family; a failed bibliographic search does not prove absolute novelty.

## Limitations

The equal-part assumption is essential to the simple three-entry inverse. Arbitrary unequal part sizes, higher-degree splines, non-unit edges, nonconstant edge densities and atomic vertex mass are not classified. The constant \(19/9\) is the supremum over this family only, not a universal bound over metric graphs. Other unpublished or unindexed equivalent calculations remain possible.

## References

[1] A. Kayumov, *Least-squares approximation by second-order L-splines*, arXiv:math/0408418, first posted August 30, 2004. https://arxiv.org/abs/math/0408418

[2] P. Oswald, *A counterexample concerning the \(L_2\)-projector onto linear spline spaces*, arXiv:math/0611573, first posted November 19, 2006. https://arxiv.org/html/math/0611573v1

[3] T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424, first posted May 13, 2010. https://arxiv.org/abs/1005.2424

[4] M. Boman, *Estimates for the \(L_2\)-projection onto continuous finite element spaces in a weighted \(L_p\)-norm*, BIT Numerical Mathematics 46 (2006), 249–260, DOI 10.1007/s10543-006-0062-3. Full text not inspected.
