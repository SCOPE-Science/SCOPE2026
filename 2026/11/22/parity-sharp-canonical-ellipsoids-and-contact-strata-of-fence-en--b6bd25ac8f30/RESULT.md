# Parity-sharp canonical ellipsoids and contact strata of fence enriched chain polytopes

## Finding
For every integer \(n\ge3\), let \(F_n\) be the height-two fence poset on \(\{1,\ldots,n\}\), with each odd-indexed element below each of its even-indexed neighbors and no other nontrivial comparisons. Its comparability graph is the path on \(n\) vertices. In the standard orthonormal coordinate realization, let
\[
K_n=\operatorname{conv}\{x\in\{-1,0,1\}^n:\operatorname{supp}(x)\text{ is an antichain of }F_n\}.
\]
Then the unique John ellipsoid \(J_n\) and Löwner ellipsoid \(L_n\) are **homothetic with the sharp universal factor**
\[
\boxed{L_n=\sqrt n\,J_n.}\tag{1}
\]
More explicitly, defining \(b_i\) by
\[
b_i=\begin{cases}
\tfrac12,&n\text{ even},\\[2pt]
\tfrac{n+1}{2n},&n\text{ odd and }i\text{ odd},\\[2pt]
\tfrac{n-1}{2n},&n\text{ odd and }i\text{ even},
\end{cases}
\]
the two ellipsoids are
\[
\boxed{J_n=\left\{x:\sum_{i=1}^n\frac{x_i^2}{b_i}\le1\right\},\qquad
L_n=\left\{x:\sum_{i=1}^n\frac{x_i^2}{n b_i}\le1\right\}.}\tag{2}
\]
Both are Euclidean balls exactly when \(n\) is even. Every one of the \(4(n-1)\) facets of \(K_n\) touches \(J_n\). The complete set of \(L_n\)-contact vertices consists of signed characteristic vectors of the following supports:

- If \(n=2m\), **all** \(m+1\) independent sets of size \(m\); there are \((m+1)2^m\) contact vertices.
- If \(n=2m+1\), **only** the all-odd and all-even independent sets; there are \(2^{m+1}+2^m=3\cdot2^m\) contact vertices.

Let \(B_{\mathrm{in}}\) and \(B_{\mathrm{out}}\) be the largest contained and smallest containing Euclidean balls. For even \(n\), \(J_n=B_{\mathrm{in}}\) and \(L_n=B_{\mathrm{out}}\). For odd \(n=2m+1\),
\[
\frac{\operatorname{vol}(J_n)}{\operatorname{vol}(B_{\mathrm{in}})}
=\left(\frac{2(m+1)}{2m+1}\right)^{(m+1)/2}
\left(\frac{2m}{2m+1}\right)^{m/2}\longrightarrow1,
\tag{3}
\]
while
\[
\boxed{\frac{\operatorname{vol}(L_n)}{\operatorname{vol}(B_{\mathrm{out}})}
=\left(\frac m{m+1}\right)^{m/2}\longrightarrow e^{-1/2}.}\tag{4}
\]
Thus the odd-dimensional Löwner ellipsoid retains a nonvanishing proportional volume advantage over the enclosing ball even though its principal-axis ratio approaches one. The odd-dimensional John ellipsoid attains the general height–width entropy lower bound beyond the layered-poset equality examples.

## Assumptions and scope
All ellipsoids and volumes use the **native standard Euclidean metric** on \(\mathbb R^n\), not a freely selected affine metric. John means the unique maximum-volume inscribed ellipsoid and Löwner means the unique minimum-volume circumscribed ellipsoid. Scalar multiplication of a centered ellipsoid is taken about the origin. The fence orientation is chosen so that odd vertices are minimal, even vertices are maximal, and comparisons exist exactly along the path edges. The result includes \(n=3\), but the non-layered odd cases start at \(n=5\). The cited enriched chain polytope is an unconditional signed-antichain polytope, not the enriched order polytope.

A signed indicator supported on an independent set that is not inclusion-maximal is not a vertex: adding a possible new coordinate with signs \(+1\) and \(-1\) expresses it as their midpoint. Conversely, signed indicators on inclusion-maximal independent sets are vertices, since fixing their coordinates at their signed unit bounds uniquely determines the point. Therefore this gives the complete vertex description needed for contact counting.

## Proof
**1. Facets and symmetry.** The published signed-maximal-chain facet theorem applies to enriched chain polytopes. All maximal chains of \(F_n\) are the \(n-1\) adjacent pairs, so precisely
\[
K_n=\{x:|x_i|+|x_{i+1}|\le1\text{ for }1\le i<n\}.
\tag{5}
\]
Every choice of two signs in every edge inequality gives a genuine facet, hence \(4(n-1)\) facets. This polytope is full-dimensional, centrally symmetric and invariant under **independent** coordinate sign flips. The existence and uniqueness of the John and Löwner ellipsoids imply that each is centered at the origin and has a diagonal shape matrix.

**2. John optimization.** Write a candidate positive diagonal ellipsoid as \(E_b=\{x:\sum x_i^2/b_i\le1\}\), where \(b_i>0\). Cauchy–Schwarz gives
\[
\max_{x\in E_b}(|x_i|+|x_{i+1}|)=\sqrt{b_i+b_{i+1}}.
\]
Thus \(E_b\subseteq K_n\) if and only if \(b_i+b_{i+1}\le1\) for every adjacent pair. Its volume is \(\kappa_n\sqrt{\prod_i b_i}\), so it suffices to maximize the strictly concave objective \(\sum_i\log b_i\) subject to these linear inequalities.

For \(n=2m\), use the disjoint constraints \(b_{2k-1}+b_{2k}\le1\). Arithmetic–geometric mean yields \(b_{2k-1}b_{2k}\le1/4\); equality throughout forces \(b_i=1/2\), which satisfies every overlapping constraint. This is the unique optimizer.

For \(n=2m+1\), set \(b_{2k-1}=(m+1)/n\) and \(b_{2k}=m/n\), so every adjacent constraint is saturated. The following positive multipliers are indexed by edges:
\[
\lambda_{2k-1}=\frac{n(m+1-k)}{m(m+1)},\qquad
\lambda_{2k}=\frac{nk}{m(m+1)},\qquad 1\le k\le m.
\]
With \(\lambda_0=\lambda_n=0\), they satisfy the stationarity identities
\[
\lambda_{i-1}+\lambda_i=\frac1{b_i},\qquad 1\le i\le n.
\]
Feasibility, positivity, complementary slackness and stationarity are the Karush–Kuhn–Tucker conditions of the strictly concave log-product problem. They prove global optimality and uniqueness, without relying on finite-dimensional experiments. All edge inequalities satisfy \(b_i+b_{i+1}=1\); on each facet of signs \((\sigma,\tau)\), the point with coordinates \(x_i=\sigma b_i\), \(x_{i+1}=\tau b_{i+1}\), all others zero, is its tangency point with \(J_n\). This proves complete John facet contact.

**3. Löwner optimization.** Write the diagonal candidate as \(E_c=\{x:\sum_i c_i x_i^2\le1\}\), with \(c_i>0\). It contains \(K_n\) exactly when
\[
\sum_{i\in I}c_i\le1\quad\text{for every independent set }I\subseteq\{1,\ldots,n\}.
\tag{6}
\]
The volume \(\kappa_n/\sqrt{\prod_i c_i}\) is minimized by maximizing \(\sum_i\log c_i\) under (6). In both parities, the two parity classes \(I_{\mathrm{odd}}\) and \(I_{\mathrm{even}}\) are independent sets. Consequently their respective \(c_i\)-sums are at most one. Arithmetic–geometric mean bounds each parity-class product by the reciprocal of the appropriate parity-class size to that power.

When \(n=2m\), this yields \(\prod_i c_i\le m^{-2m}\). Equality requires every \(c_i=1/m\), feasible because any independent set of the even path has at most \(m\) elements.

When \(n=2m+1\), the bound is \(\prod_i c_i\le(m+1)^{-(m+1)}m^{-m}\), with equality only if \(c_i=1/(m+1)\) on odd indices and \(c_i=1/m\) on even indices. It is feasible: the unique independent set of size \(m+1\) is the complete odd class, with weight one; all other independent sets have size at most \(m\), and each coordinate weight is at most \(1/m\). Thus these unique choices solve the exact enclosing-ellipsoid problem.

In both parities, \(c_i=1/(n b_i)\), establishing the homothety (1). Equality in (6) identifies **all** vertex contacts: in even order they are precisely independent sets of size \(m\), which number \(\binom{m+1}{m}=m+1\); in odd order they are precisely the full odd and full even classes. Every sign pattern on each support is allowed, proving the claimed contact counts. Other vertices lie strictly inside \(L_n\).

**4. Balls and limits.** All edge facet normals in (5) have Euclidean length \(\sqrt2\), and central symmetry prohibits an inscribed ball larger than \(1/\sqrt2\). The origin-centered ball of that radius is feasible; hence it is maximal. Every signed antichain point has squared norm equal to its support size, so the smallest enclosing ball is centered at zero with squared radius \(\lceil n/2\rceil\). Taking products of the squared semiaxes in (2) gives (3) and (4). Standard logarithmic limits yield \(\lim_{m\to\infty}(m/(m+1))^{m/2}=e^{-1/2}\), while the logarithm of the John-to-inball ratio is \(O(1/n)\), yielding the other limit.

## Verification
The self-contained program `verify.py` enumerates independent and inclusion-maximal independent sets for every dimension from three through sixteen, checks the exact rational containment constraints, the homothety, all John facet tangencies and all Löwner vertex contact counts, and verifies the explicit positive KKT multiplier equations in odd orders. When SciPy is available it independently optimizes the two log-determinant programs for dimensions three through eleven (eighteen programs) and compares to the exact formulas. Run `python3 verify.py` in the same directory. It prints `FENCE_EXTREMAL_ELLIPSOIDS_PASS`. The infinite-dimensional quantifiers are established by the proof above, not by the finite experiments.

## Relationship to prior work
Ohsugi and Tsuchiya introduced enriched chain polytopes as convex hulls of independently signed antichains. Their paper develops Ehrhart and triangulation properties, not canonical John–Löwner ellipsoids. Their later article on enriched order and Hibi structures gives the signed-chain facet inequalities. Kohl, Olsen and Sanyal study the same bodies as unconditional chain polytopes, including perfect-graph structure but not the particular extremal ellipsoids here.

The publicly recorded general result *A sharp entropy bound for John ellipsoids of enriched chain polytopes* (2026) is particularly close: it proves that a general height–width lower bound for the John volume is attained by specified layered posets, and that roundness is equivalent to the height–width product equalling the number of elements. Its general feasible candidate, applied to the fence's larger parity antichain, coincides with the odd-dimensional John ellipsoid displayed here. **That prior theorem only proves feasibility, not John optimality, for nonlayered fences**; the positive edge-multiplier certificate above establishes the missing sharpness. It also does not give the corresponding Löwner shape, its complete contact supports, or the accumulating odd-dimensional volume gap. The previously published *Height and width are the exact Euclidean radii of enriched chain polytopes* gives the two enclosing/inscribed ball radii, which are used as context, not claimed as new.

The homothety resembles entropy-antiblocker duality for perfect graphs; no universal homothety theorem is claimed here. The contribution is the explicit simultaneous canonical ellipsoids and exact contact transition for the natural nonlayered fence family. Results described only for ordinary nonnegative chain polytopes, signed-order polytopes, or generic reflexive polygons do not directly apply to this unconditional signed-antichain body.

## Limitations
The formulas are not invariant under arbitrary nonorthogonal coordinate changes. The arithmetic equality at even orders and the general inball/circumball values have already been treated in broader work; they are included to state the complete parity classification rather than proposed as independent discoveries. The original 2018 paper and public general 2026 John-volume theorem strongly overlap the background. A differently phrased graph-entropy or extremal-design classification could imply the new fence-specific equalities without using these names; historical priority remains provisional. The numeric checker is finite and not a substitute for the all-dimensional proof. No independent mathematical audit is asserted.

## References
1. H. Ohsugi and A. Tsuchiya, *Enriched chain polytopes*, arXiv:1812.02097, v1 posted 2018-12-05, https://arxiv.org/html/1812.02097v2.
2. H. Ohsugi and A. Tsuchiya, *Enriched order polytopes and enriched Hibi rings*, arXiv:1903.00909, https://link.springer.com/article/10.1007/s40879-020-00403-2 (see Proposition 6.1).
3. F. Kohl, M. Olsen and R. Sanyal, *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry 64 (2020), 427–452, https://link.springer.com/article/10.1007/s00454-020-00199-8.
4. *A sharp entropy bound for John ellipsoids of enriched chain polytopes*, publicly recorded mathematical research finding, 2026-11-08, published-finding corpus identifier `86ee65f9050d`.
5. *Height and width are the exact Euclidean radii of enriched chain polytopes*, publicly recorded mathematical research finding, 2026-10-11, published-finding corpus identifier `db93f92ff100`.
