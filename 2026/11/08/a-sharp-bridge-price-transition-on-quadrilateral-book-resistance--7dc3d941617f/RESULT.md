# A sharp bridge-price transition on quadrilateral-book resistance networks

## Finding

Let \(m\ge2\) be an integer. Consider two vertices \(u,v\), together with \(2m\) further vertices \(x_i,y_i\) for \(1\le i\le m\). The allowed edges are \(ux_i,x_iy_i,y_iv\) for each \(i\), together with the direct edge \(uv\). Every path edge has unit price per unit conductance; the direct edge has price \(d>0\). A total budget \(B>0\) can be distributed among the \(3m+1\) allowed edges, each independently and nonnegatively. An allocation with disconnected positive-conductance support has infinite objective. The objective is the Kirchhoff index
\[
\mathcal K(L)=\sum_{s<t}R_{st}=(2m+2)\operatorname{tr}(L^+),
\]
where \(L\) is the weighted combinatorial Laplacian and \(L^+\) its Moore--Penrose pseudoinverse.

Define, for \(r>0\),
\[
 g_m(r)=m-1+\frac1{m+1}+\frac{m-1}{1+2r}
             +\frac{m+1+2r}{2mr}.
\]
There is exactly one \(r_m>0\) satisfying
\[
 g_m(r_m)+(2+r_m)g'_m(r_m)=0,\qquad
 g'_m(r)=-\frac{2(m-1)}{(1+2r)^2}-\frac{m+1}{2mr^2}.
\]
Set
\[
 d_m^*=\frac{(2+r_m)(m+1+4r_m+4r_m^2)}
                {2mr_m^2 g_m(r_m)}.
\]
**Theorem.** The globally optimal allocation is unique, even without any imposed symmetry. Every path-edge outer conductance and every path-edge middle conductance is strictly positive. The direct bridge \(uv\) has zero optimal conductance **if and only if** \(d\ge d_m^*\). At equality the bridge remains zero.

More precisely, all \(2m\) outer edges share conductance \(a>0\), all \(m\) middle edges share conductance \(b>0\), and the bridge has conductance \(q\ge0\). If \(d\ge d_m^*\), the exact optimum is
\[
 a=\frac{B}{m(2+r_m)},\qquad b=r_m a,\qquad q=0.
\]
If \(0<d<d_m^*\), the unique positive pair \((r,t)\) solving the two equations displayed in the proof gives the exact optimum
\[
 a=\frac{B}{m(2+r)+dt},\quad b=ra,\quad q=ta.
\]
The allocation proportions and the critical price are independent of \(B\). In both regimes the minimum Kirchhoff index is obtained by substituting these conductances in the explicit rational spectral formula below.

The threshold has the exact special value and asymptotic law
\[
 d_2^*=\frac{99}{35},\qquad
 r_m=\frac{\sqrt3-1}{2}+O(m^{-1}),\qquad
 d_m^*=\left(3+\frac{3\sqrt3}{2}\right)\frac1m+O(m^{-2}).
\]
Thus a direct shortcut's economically justified unit price is of order \(1/m\) when there are many parallel three-edge routes.

## Assumptions and scope

- The graph is simple and undirected, with precisely \(2m+2\) vertices, the indicated \(3m+1\) permitted edges, and no other edges. In graph terminology it is a book of \(m\) four-cycles sharing the edge \(uv\), also \(K_{1,m}\square K_2\).
- Conductances are nonnegative; the total resource constraint is \(\sum_{i=1}^m(w_{ux_i}+w_{x_iy_i}+w_{y_iv})+d w_{uv}=B\). There are no compulsory lower bounds.
- The objective includes all unordered vertex pairs, including intermediate vertices; eliminating such vertices electrically does **not** preserve the objective.
- The direct edge is permitted to receive zero conductance. No assumption of symmetric conductance choices is made in the optimization problem.
- The result concerns global Kirchhoff-index minimization, not algebraic connectivity, leader selection, or fixed-weight graph augmentation.

## Proof

**1. Existence, strict convexity, and symmetry.** Write \(N=2m+2\) and \(J=\mathbf1\mathbf1^\top/N\). For any connected support, \(L+J\) is positive definite and
\[
 \mathcal K=N\bigl(\operatorname{tr}((L+J)^{-1})-1\bigr).
\]
The trace-of-inverse function is strictly convex on positive-definite symmetric matrices: for a nonzero symmetric perturbation \(H\), its second directional derivative is
\[
 2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0.
\]
The map from individual edge conductances to \(L\) is injective, because the off-diagonal \((i,j)\) entry identifies the weight of each allowed simple edge. Hence \(\mathcal K\) is strictly convex in the conductance vector on connected supports. The feasible set is compact, and the objective tends to infinity as the support approaches disconnection (a nonzero Laplacian eigenvalue tends to zero). An optimum exists and is unique. Permuting the \(m\) pages and reflecting \(u\leftrightarrow v\), \(x_i\leftrightarrow y_i\) preserves prices and the objective. Uniqueness forces a common outer weight \(a\), a common middle weight \(b\), and bridge weight \(q\). The budget becomes
\[
 2ma+mb+dq=B.
\]
Necessarily \(a>0\), since \(a=0\) disconnects every page from the two hubs.

**2. Spectral trace identity.** On the \((m-1)\)-dimensional page-difference spaces, the Laplacian has eigenvalues \(a\) and \(a+2b\), each with multiplicity \(m-1\). The reflection-even page-constant subspace has eigenvalues \(0\) and \((m+1)a\). On the two-dimensional reflection-odd subspace, represented by hub values \((U,-U)\) and page values \((X,-X)\), the Laplacian acts by the matrix
\[
 \begin{pmatrix}ma+2q&-ma\\-a&a+2b\end{pmatrix}.
\]
Its trace is \((m+1)a+2b+2q\) and its determinant is \(2mab+2aq+4bq\). Thus, for connected support,
\[
 \boxed{\displaystyle
 \frac{\mathcal K}{N}=
 \frac{m-1}{a}+\frac{m-1}{a+2b}+\frac1{(m+1)a}
 +\frac{(m+1)a+2b+2q}{2mab+2aq+4bq}.}
 \tag{1}
\]
This identity is valid also at \(q=0,b>0\) and at \(b=0,q>0\).

**3. Middle edges cannot be omitted.** If \(b=0\), connectivity requires \(q>0\). Let \(G=\mathcal K/N\) denote the right side of (1). A budget-preserving infinitesimal perturbation increases each middle conductance by \(\varepsilon\) and decreases each outer conductance by \(\varepsilon/2\), leaving the bridge fixed. Direct differentiation at \(b=0\) gives
\[
 \left.\left(\partial_bG-\frac12\partial_aG\right)\right|_{b=0}
 =-\frac{m\bigl((m+1)^2a^2+4(m+1)aq+(2m+3)q^2\bigr)}
 {2a^2q^2(m+1)}<0.
\]
Therefore a feasible allocation with \(b=0\) cannot be optimal. In particular, \(a,b>0\) at the optimum and only the bridge can have zero weight.

**4. Dimensionless two-variable program.** Set \(r=b/a>0\) and \(t=q/a\ge0\). Define
\[
 Z=2mr+2t+4rt,\quad P=m+1+2r+2t,\quad
 G_m(r,t)=m-1+\frac1{m+1}+\frac{m-1}{1+2r}+\frac PZ,
\]
\[
 C(r,t)=m(2+r)+dt,\qquad
 \Phi_m(r,t;d)=C(r,t)G_m(r,t).
\]
The budget gives \(a=B/C\) and (1) becomes
\[
 \mathcal K=\frac{N}{B}\Phi_m(r,t;d).
 \tag{2}
\]
An interior minimizer obeys the explicit pair of rational equations
\[
 mG_m+C\left(-\frac{2(m-1)}{(1+2r)^2}
                       +\frac{2Z-P(2m+4t)}{Z^2}\right)=0,
 \tag{3}
\]
\[
 dG_m+C\frac{2Z-P(2+4r)}{Z^2}=0.
 \tag{4}
\]
Every positive solution of (3)--(4) gives a stationary point for the original strictly convex budget problem, so it is the unique global optimum. Conversely every interior optimum solves them. This is a unique algebraic characterization of the conductance allocation; it does not assert that a short radical expression exists for general \(m,d\).

**5. Sharp bridge exclusion.** On the boundary \(t=0\), \(G_m(r,0)=g_m(r)\). The reduced objective is \(m(2+r)g_m(r)\). It diverges as \(r\downarrow0\) or \(r\to\infty\), and strict convexity of the original two-class allocation makes its minimum unique. Its first-order condition is exactly the defining equation for \(r_m\). The derivative of the dimensionless trace in the bridge direction is
\[
 \partial_tG_m(r,0)=-\frac{m+1+4r+4r^2}{2m^2r^2}.
\]
Consequently
\[
 \partial_t\Phi_m(r_m,0;d)
 =g_m(r_m)\bigl(d-d_m^*\bigr).
 \tag{5}
\]
The only possible inactive variable is \(q\), so the Karush--Kuhn--Tucker necessary and sufficient boundary condition is precisely \(\partial_t\Phi\ge0\). Equation (5), the strict positivity of \(g_m\), and strict convexity prove \(q=0\) exactly for \(d\ge d_m^*\), including equality. When \(d<d_m^*\), the boundary point has a feasible strict descent direction, hence the unique optimum has \(q>0\) and is determined by (3)--(4). The budget scaling in (2) proves independence of \(B\).

**6. Exact small case and large-page behavior.** At \(m=2\), the boundary equation has unique root \(r_2=1\) and the threshold formula gives \(d_2^*=99/35\). For the asymptotic, the polynomial numerator of \(g_m+(2+r)g'_m\), after multiplication by its positive denominator, has leading term \(2m^3r^2(2r^2+2r-1)\), with coefficients of lower order in \(m\). Strict uniqueness and the sign of the first-order condition imply \(r_m\to r_\infty=(\sqrt3-1)/2\); the simple positive root and polynomial perturbation give \(r_m=r_\infty+O(m^{-1})\). Substitution into the exact threshold, using \(g_m(r_m)=m(1+1/(1+2r_\infty))+O(1)\), yields
\[
 \lim_{m\to\infty}m d_m^*
 =\frac{(2+r_\infty)(1+2r_\infty)}{4r_\infty^2(1+r_\infty)}
 =3+\frac{3\sqrt3}{2},
\]
with error \(O(m^{-1})\) in the scaled threshold, as claimed.

## Verification

Run `python verify.py` with Python 3.10 or later; the program has no third-party dependencies. It recomputes the Kirchhoff index by exact rational inversion of \(L+J\) on several graph orders and on all relevant boundary types, compares with (1), checks the middle-edge descent direction, tests threshold identities, and compares an exactly known optimum against non-symmetric feasible allocations. The expected message is `VERIFY_OK 124`.

These finite checks are supplementary. The statements for all \(m\), all positive real prices, and all positive budgets follow from the algebraic and strict-convexity arguments above, not from numerical enumeration. Separate numerical optimization over individually weighted edges was also used to stress-test representative price regimes; it is not a substitute for the proof.

## Relationship to prior work

Ghosh, Boyd, and Saberi developed the convex total-effective-resistance allocation problem, strict uniqueness, Laplacian trace formulations, and analytic reductions for trees, wheels, and barbells. The present argument uses that framework but computes a new exact boundary for a quadrilateral-book family and price-dependent activation of its shared edge. The general formulation alone does not supply equation (5) or the threshold \(d_m^*\).

Liu and Zhang obtained resistance-distance and Kirchhoff-index expressions for the *unweighted quadrilateral graph* formed by replacing each edge with parallel paths of lengths one and three. Their operation is distinct from multiple four-cycles sharing a single edge, and their formulas do not optimize conductances subject to a price budget. Later budget-constrained augmentation work with fixed pre-existing weights and discrete edge-count constraints also differs from simultaneous reallocation of all permitted edges.

Results for direct bridges linking two-edge routes, leader-selection on quadrilateral books, and generic convex optimization are not asserted to be new here. In particular, electrically contracting one internal vertex per route does not preserve the sum of effective resistances over *all* original vertices, and thus does not imply this three-edge-route threshold.

## Limitations

The result applies to symmetric unit prices on all path edges and a separate price on the shared bridge. Heterogeneous page prices, compulsory positive bridge weights, fixed base conductances, and alternative objectives are outside its scope. Equations (3)--(4) may require numerical solution for general parameter values, though their positive solution is unique when applicable. There is no independent mathematical audit. An equivalent theorem may exist in unindexed series--parallel electrical-network literature; the novelty assessment is relative to the inspected sources, not a proof of universal priority. The shorter 2006 conference version of the foundational paper has an earlier month-identified public appearance; the exact calendar day of that appearance was not verified, so the dated 2008 online version supplies the day-resolved bibliographic anchor.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37--66. DOI: 10.1137/050645452. Author-posted full text: https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf . The SIAM page identifies online publication on February 1, 2008 and the authors identify a shorter July 2006 conference version.
2. Q. Liu, Z. Zhang, *The resistance distance and Kirchhoff index on quadrilateral graph and pentagonal graph*, arXiv:1812.02304, December 4, 2018. https://arxiv.org/abs/1812.02304 .
3. O. Bhoite, V. S. Dhuli, S. Werner, K. Kansanen, *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790, September 24, 2026. https://arxiv.org/abs/2609.29790 .
