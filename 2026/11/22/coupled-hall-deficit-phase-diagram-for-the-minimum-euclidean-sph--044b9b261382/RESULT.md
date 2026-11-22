# Coupled Hall-deficit phase diagram for the minimum Euclidean sphere of three-step Ferrers root polytopes

## Finding

Let \(U_1,U_2,U_3\) and \(V_1,V_2,V_3\) be six disjoint nonempty blocks, of positive integer sizes \(a_i=|U_i|\) and \(b_j=|V_j|\). Define the three-step Ferrers graph by including every pair \(uv\in U_i\times V_j\) exactly when \(i+j\le4\). It has six allowed block cells:
\[
 (1,1),(1,2),(1,3),(2,1),(2,2),(3,1).
\]
Orient every edge from left to right. The canonical root polytope is
\[
 Q=\operatorname{conv}\{e_u-e_v: uv\in E(G)\}\subset\mathbb R^{A+B},
 \quad A=a_1+a_2+a_3,\quad B=b_1+b_2+b_3.
\]

Set
\[
 \delta=\begin{pmatrix}a_3/A-b_1/B\\
 (a_2+a_3)/A-(b_1+b_2)/B\end{pmatrix},
\]
and the strictly positive definite matrix
\[
 K=\begin{pmatrix}
 \dfrac{a_3(a_1+a_2)}A+\dfrac{b_1(b_2+b_3)}B &
 \dfrac{a_3a_1}A+\dfrac{b_1b_3}B\\[5pt]
 \dfrac{a_3a_1}A+\dfrac{b_1b_3}B &
 \dfrac{(a_2+a_3)a_1}A+\dfrac{(b_1+b_2)b_3}B
 \end{pmatrix}.
\]
Write \(K_{ij}\) for its entries. Define \(\lambda=(\lambda_1,\lambda_2)\) using exactly one of the following four (boundary-consistent) regimes:

1. If \(\delta_1\le0\) and \(\delta_2\le0\), take \(\lambda=(0,0)\).
2. Otherwise, if \(\delta_1>0\) and \(\delta_2\le K_{12}\delta_1/K_{11}\), take \(\lambda=(\delta_1/K_{11},0)\).
3. Otherwise, if \(\delta_2>0\) and \(\delta_1\le K_{12}\delta_2/K_{22}\), take \(\lambda=(0,\delta_2/K_{22})\).
4. Otherwise, take \(\lambda=K^{-1}\delta\); in this regime both components are positive.

These formulas, including the equalities on regime boundaries, yield the unique solution of
\[
 \lambda\ge0,\qquad \delta-K\lambda\le0,\qquad
 \lambda_i(\delta-K\lambda)_i=0\quad(i=1,2).
\]
**The exact squared circumradius** and unique minimum-sphere center are
\[
 \boxed{R^2=2-\frac1A-\frac1B-\lambda^\top K\lambda,}
\]
\[
 \boxed{u_i=\frac1A-\lambda_1\left(\mathbf1_{i=3}-\frac{a_3}{A}\right)
 -\lambda_2\left(\mathbf1_{i\ge2}-\frac{a_2+a_3}{A}\right),}
\]
\[
 \boxed{v_j=\frac1B+\lambda_1\left(\mathbf1_{j=1}-\frac{b_1}{B}\right)
 +\lambda_2\left(\mathbf1_{j\le2}-\frac{b_1+b_2}{B}\right).}
\]
Here \(u_i>0\) and \(v_j>0\) are the per-vertex coordinate magnitudes, so the center in the original root coordinates equals \(u_i\) on \(U_i\) and \(-v_j\) on \(V_j\).

**Every contacting edge is classified.** For an allowed cell \((i,j)\), the square-radius clearance (squared radius minus squared center-to-vertex distance) is
\[
 \boxed{\mathcal C_{ij}=2\left[\lambda_1\mathbf1_{\{j=1,\ i<3\}}+
 \lambda_2\mathbf1_{\{i=1,\ j\le2\}}\right].}
\]
Thus that entire cell is tangent exactly when \(\mathcal C_{ij}=0\). With \(\lambda_1=\lambda_2=0\) all six cells contact; with both strictly positive, only \((1,3),(2,2),(3,1)\) contact, and the three other cells are screened. If only one multiplier is positive, precisely four of six cells contact. The exact number of contacting graph edges is \(\sum_{i+j\le4}a_i b_j\mathbf1_{\{\mathcal C_{ij}=0\}}\).

For example, \(a=(1,1,1)\), \(b=(1,2,3)\) gives \(\lambda=(2/23,1/23)\), \(R^2=34/23\), and center magnitudes \(u=(9/23,8/23,6/23)\) and \(v=(6/23,4/23,3/23)\), with exactly the three opposite-diagonal edge cells contacting. The coupled radius correction is \(1/46\), explicitly different from the sum of the two independent single-cut penalties.

## Assumptions and scope

All six group sizes are arbitrary positive integers. All edge-generator vectors are unscaled, and Euclidean distances use the ambient standard inner product. The graph is connected. The affine hull has codimension two; taking its inherited metric does not change enclosing-ball radii or centers. An orthogonal sign reversal on right coordinates identifies this directed-root realization with the convex hull of unsigned \(0/1\) graph edge-incidence vectors. General Ferrers diagrams with four or more distinct neighborhood classes, edge weights, and nonstandard metrics are not covered.

## Proof

**Step 1: Equal-norm sphere principle.** If a finite set \(W\) lies on the centered sphere of squared radius \(L\), its convex hull has a unique minimum-norm point \(c\). For each \(w\in W\), projection optimality gives \(\langle c,w-c\rangle\ge0\), hence \(\|w-c\|^2\le L-\|c\|^2\). Conversely write \(c=\sum_w p_w w\) for nonnegative \(p_w\) summing to one. For any proposed ball center \(z\), the maximum squared distance is at least
\[
\sum_w p_w\|w-z\|^2=L-\|c\|^2+\|z-c\|^2.
\]
It follows that the unique smallest enclosing ball is centered at \(c\), has squared radius \(L-\|c\|^2\), and an extreme vector \(w\) touches exactly when \(\langle c,w\rangle=\|c\|^2\). Here \(L=2\).

**Step 2: Transportation margins and the two independent Hall cuts.** Reflect the right coordinates; every vertex becomes \(e_u+e_v\). By uniqueness, the minimum-norm point is invariant under permutations inside each of the six blocks. Let its total nonnegative mass on the left blocks be \(x_i\) and on the right blocks be \(y_j\). Because it is a convex combination of graph edges, \(\sum_i x_i=\sum_j y_j=1\), and the mass vector satisfies precisely
\[
 x_3\le y_1,\qquad x_2+x_3\le y_1+y_2.
\]
Together with nonnegativity these constraints are sufficient: a nonnegative unit transportation flow with these margins exists by the max-flow/min-cut theorem, since neighborhoods of left blocks are nested and only the two displayed nontrivial Hall inequalities can be restrictive. Its objective is the strictly convex energy
\[
 F(x,y)=\sum_{i=1}^3\frac{x_i^2}{a_i}+\sum_{j=1}^3\frac{y_j^2}{b_j}.
\]
The minimizer is *strictly positive in every coordinate*: suppose a graph vertex has zero mass and choose an adjacent positive-mass vertex along the boundary between zero and positive masses, which exists by connectivity. Some edge at that positive vertex carries positive weight; moving sufficiently small weight from that edge to the edge joining it to the zero vertex strictly lowers the squared coordinate norm (the displaced opposite endpoint has positive mass while the zero endpoint has zero mass). Contradiction. Hence all six block margins are positive and no nonnegativity constraint is active.

**Step 3: Weighted projection onto the Hall halfspaces.** Without the two Hall cuts, the minimum of \(F\) under the two mass sums is \(x_i=a_i/A\), \(y_j=b_j/B\), of value \(1/A+1/B\). The two cut excesses at this point are \(\delta_1,\delta_2\). In the quadratic metric defined by \(F\), the two mean-zero cut-normal vectors have squared inner products exactly \(K_{11},K_{22}\) and mutual inner product \(K_{12}\). Positivity of \(K\) follows because the two independent cut functionals are linearly independent on the affine mass-sum subspace, and \(F\) is strictly positive definite. Applying the first-order Kuhn–Tucker conditions with a factor two in the inequality multipliers gives the center formulas, cut excesses \(\delta-K\lambda\), and complementarity conditions stated above. This quadratic program is strictly convex and has a strict feasible point (put small positive mass on the two extreme left/right blocks), so these conditions are necessary and sufficient. \(K_{11}K_{22}-K_{12}^2>0\) then yields the four explicit multiplier regions by elementary two-by-two inversion.

By orthogonality of the correction to the unconstrained energy minimizer,
\[
 \|c\|^2=\frac1A+\frac1B+\lambda^\top K\lambda.
\]
The equal-norm sphere principle proves the radius formula and uniqueness.

**Step 4: Complete contact law.** On an allowed edge cell \((i,j)\), subtract the center inner product from \(\|c\|^2\) using the per-vertex formulas:
\[
 \langle c,e_u+e_v\rangle-\langle c,c\rangle
 =\lambda_1(\mathbf1_{j=1}-\mathbf1_{i=3})
 +\lambda_2(\mathbf1_{j\le2}-\mathbf1_{i\ge2}).
\]
Thus \(\langle c,e_u+e_v\rangle-\|c\|^2\) is the nonnegative sum appearing in \(\mathcal C_{ij}/2\). The difference of the squared radii is twice that inner-product difference, giving the six exact clearances above. Each generator is indeed a vertex: the functional \(z\mapsto z_u+z_v\) strictly exposes the edge \(uv\) among the distinct edge-incidence vectors. Reversing right signs restores the original coordinates. This proves the contact spectrum without an unproved genericity assumption. \(\square\)

## Verification

The accompanying standalone `check_ferrers_three_step.py` uses exact fractions (no floating point) to calculate the four-region solution and independently reconstruct center norms, both Hall complementarity equations, all six distance clearances and tangency classifications. It exhaustively checks all \(4^6=4096\) choices of positive block sizes from one through four, covers all four regimes, and checks the unequal six-block example exactly. Running `python check_ferrers_three_step.py` prints `THREE_STEP_FERRERS_EXACT_PASS 4096 regimes 4`. A separate floating-point stress test also checked \(5^6=15625\) size choices. These finite calculations are safeguards, not proofs for unbounded positive integer block sizes.

## Relationship to prior work

Kálmán and Tóthmérész (arXiv:2203.17127, first public version March 31, 2022) study root polytopes of semi-balanced digraphs, including their spanning-tree dissections and \(h^*\)-polynomials. Lazar (DOI:10.1007/s11139-022-00581-5, published June 7, 2022) develops Ferrers graphs through hyperplane-arrangement bond lattices and enumeration. Neither establishes the present Euclidean center, radius, or contact formulas in the inspected sections.

An earlier exact two-step Ferrers-root-polytope result treats removal of a *single* biclique: its entire radius correction comes from one Hall deficit, and at most one contact-screening transition occurs. That result is directly recovered from the one-cut mechanism but does not imply the two-active-cut phase of a six-block graph. Here the two nonparallel Hall constraints interact through a positive off-diagonal \(K_{12}\), creating a coupled radius correction, a fourth contact regime, and a distinct three-orbit contacting set. The general equal-norm-sphere projection observation and the max-flow/min-cut theorem are established tools, not claimed as new.

## Limitations

Historical priority is provisional: an equivalent formula could appear in broader literature on convex projection onto graph-margin polytopes or quadratic transportation optimization. The result concerns exactly three positive Ferrers row classes and the canonical Euclidean realization, not arbitrary weighted Ferrers graphs or a general polyhedral metric. The checks were performed in the same analysis and have not been independently audited.

## References

1. T. Kálmán and L. Tóthmérész, *\(h^*\)-vectors of graph polytopes using activities of dissecting spanning trees*, arXiv:2203.17127v1, first posted 2022-03-31, https://arxiv.org/abs/2203.17127.
2. A. Lazar, *Ferrers graphs, D-permutations, and surjective staircases*, *The Ramanujan Journal* 60 (2023), 391–426; first online 2022-06-07, https://doi.org/10.1007/s11139-022-00581-5.
3. *Hall-deficit quadratic law for minimum spheres of two-step Ferrers root polytopes*, online mathematical note (2026), https://github.com/published-finding corpus/2026.
