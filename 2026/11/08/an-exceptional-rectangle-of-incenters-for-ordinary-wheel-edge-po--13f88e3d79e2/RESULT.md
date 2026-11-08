# An exceptional rectangle of incenters for ordinary wheel edge polytopes

## Finding

Let \(W_m=K_1*C_m\) be the wheel with a hub and \(m\ge3\) rim vertices. Its **ordinary graph edge polytope**, rather than its symmetric edge-root polytope, is
\[
E_m=\operatorname{conv}\{e_a+e_b:\{a,b\}\in E(W_m)\}
\subset\{x\in\mathbb R^{m+1}:\sum_{i=0}^{m}x_i=2\}.
\]
Use the Euclidean distance induced from \(\mathbb R^{m+1}\) on this \(m\)-dimensional affine space. Set
\[
k=\lfloor m/2\rfloor,\qquad
u=\sqrt{\frac{m}{m+1}},\qquad
v=\sqrt{\frac{k(m+1-k)}{m+1}}.
\]
For every integer \(m\ge3\), the intrinsic Euclidean inradius is
\[
\boxed{\rho(E_m)=\begin{cases}
\displaystyle\frac{1}{u+2v},&m=4,\\[2mm]
\displaystyle\frac{1}{ku+v},&m=3\text{ or }m\ge5.
\end{cases}}
\]
For \(m\ne4\), the incenter is unique, and its rim coordinates all equal
\[
s_m=\frac{u}{ku+v}.
\]
The hub coordinate is \(2-ms_m\). For \(m=4\), put
\[
s_4=\frac{u+v}{4v+2u},\qquad \ell_4=\frac{u}{u+2v}.
\]
The complete set of maximum-ball centers is the nondegenerate rectangle
\[
\boxed{y_1+y_3=y_2+y_4=2s_4,\quad
 y_i\ge\ell_4\ (1\le i\le4),\quad
 x_0=2-\sum_{i=1}^4y_i.}
\]
Here \(y_i=x_i\) for the rim. At its dihedrally symmetric center, exactly eight facets touch when \(m=3\), exactly three touch when \(m=4\), exactly \(m+2\) touch for even \(m\ge6\), and exactly \(2m\) touch for odd \(m\ge5\).

## Assumptions and scope

All graphs are finite, simple, and undirected. The wheel has rim edges \(i(i+1)\) with indices taken modulo \(m\) and hub spokes \(0i\). Its ordinary edge polytope is the convex hull of the unsigned incidence vectors \(e_a+e_b\), not the centrally symmetric convex hull of \(\pm(e_a-e_b)\). These constructions have different metric geometry. All balls use the original Euclidean metric on the affine hyperplane \(\sum x_i=2\). The result holds for every integer \(m\ge3\), including both parity classes and the exceptional square rim.

## Proof

**1. An exact halfspace model.** Eliminate the hub coordinate by writing \(x_0=2-\sum_i y_i\). The rim-coordinate polytope is
\[
Q_m=\operatorname{conv}\{e_i,e_i+e_{i+1}:i\in\mathbb Z/m\mathbb Z\}\subset\mathbb R^m.
\]
We claim an *exact*, not merely necessary, inequality description:
\[
\tag{H}
y_i\ge0,\qquad 1\le\sum_i y_i\le2,\qquad
\sum_{i\in S}y_i\le1\quad
\text{for every independent set }S\subseteq C_m.
\]
The upper total-sum inequality is redundant for even \(m\) but is retained for a uniform description. Every displayed generating vertex satisfies (H).

Conversely, take \(y\) satisfying (H), and set \(t=\sum_i y_i-1\), so \(0\le t\le1\). We seek nonnegative weights \(b_i\) for the rim-edge vertices with \(\sum_i b_i=t\) and \(b_{i-1}+b_i\le y_i\). It suffices to show that the capacity-packing linear program
\[
\max\bigl\{\sum_i b_i:b_i\ge0,\ b_{i-1}+b_i\le y_i\bigr\}
\]
has optimum at least \(t\). Its dual is the nonnegative fractional vertex-cover problem
\[
\min\bigl\{\sum_i y_i z_i:z_i\ge0,\ z_i+z_{i+1}\ge1\bigr\}.
\]
Every vertex of this dual feasible polyhedron is either the zero-one indicator of a vertex cover, or (only for odd \(m\)) the all-one-half vector. Indeed a coordinate strictly above one can be perturbed in both directions without affecting any tight constraint. For the remaining coordinates, any fractional coordinates bounded strictly between zero and one form path components whose active adjacent edge equalities can be perturbed by alternating signs, unless *all* coordinates are fractional and *all* cycle-edge equalities are tight. The latter system has only the all-one-half solution for odd \(m\), and has a nontrivial alternating direction for even \(m\). Thus these are precisely the possible extreme types; a linear functional with nonnegative coefficients attains its finite minimum at such an extreme point.

For a zero-one cover with complementary independent set \(S\), its objective is
\(\sum_i y_i-\sum_{i\in S}y_i\ge t\), by (H). For the all-one-half vector its objective is \(\sum_i y_i/2\ge t\), because \(\sum_i y_i\le2\). Strong linear-programming duality therefore produces a packing with sum at least \(t\), which can be scaled down to sum exactly \(t\). Defining \(a_i=y_i-b_{i-1}-b_i\ge0\), we have \(\sum_i a_i=1-t\). Hence
\[
y=\sum_i a_i e_i+\sum_i b_i(e_i+e_{i+1}),\qquad
\sum_i(a_i+b_i)=1.
\]
This proves (H).

**2. Intrinsic facet-distance normalization.** An increment \(dy\) in rim coordinates corresponds in the ambient hyperplane to \((dx_0,dx_1,\ldots,dx_m)=(-\sum_i dy_i,dy)\). Its Gram matrix is \(G=I_m+J_m\), so \(G^{-1}=I_m-J_m/(m+1)\). A linear form \(\sum_{i\in S} y_i\) therefore has intrinsic dual Euclidean norm
\[
\tag{N}\|\mathbf1_S\|_{G^{-1}}
=\sqrt{\frac{|S|(m+1-|S|)}{m+1}}.
\]
In particular, an individual coordinate or the total sum has dual norm \(u\), while a maximum independent set of size \(k\) has dual norm \(v\). For a center to contain an intrinsic closed ball of radius \(r\) in (H), every inequality margin must be at least \(r\) times this dual norm.

**3. Reduction to one dimension and solution.** The dihedral symmetries of the rim fix the hub coordinate, act orthogonally on the intrinsic metric, and preserve \(E_m\). Averaging any optimal center over this group produces an optimal center with every rim coordinate equal to \(s\). For \(1/m\le s\le2/m\), the distances to the coordinate-lower, total-lower, independent-set, and (for odd \(m\)) total-upper hyperplanes are respectively
\[
\frac{s}{u},\quad\frac{ms-1}{u},\quad
\frac{1-js}{\sqrt{j(m+1-j)/(m+1)}}\quad(1\le j\le k),\quad
\frac{2-ms}{u}.
\]
As \(j\) increases from \(1\) to \(k\), the independent-set numerator decreases and its denominator increases. Thus the size-\(k\) independent sets impose the strongest such condition, at distance \((1-ks)/v\).

The crossing of the increasing coordinate-lower distance \(s/u\) and the decreasing maximal-independent-set distance \((1-ks)/v\) gives \(s_*=u/(ku+v)\) and upper bound \(r_*=1/(ku+v)\). The total-lower inequality is satisfied at that point exactly when
\[
\tag{L}\frac vu\le m-1-k.
\]
For odd \(m=2k+1\), the left-hand side is \(\sqrt{k(k+2)/(2k+1)}\le k\) for \(k\ge1\). For even \(m=2k\), it is \(\sqrt{(k+1)/2}\le k-1\) for \(k\ge3\). For odd \(m\), the remaining total-upper inequality holds because \(v\ge u\), with equality only at \(m=3\). Thus for \(m=3\) and all \(m\ge5\), the proposed \(r_*\) is feasible and meets the universal upper bound.

The sole failure of (L) occurs at \(m=4\). In that case the dominant competing bounds are the total-lower distance \((4s-1)/u\) and the size-two independent-set distance \((1-2s)/v\). Their intersection yields
\[
\rho_4=\frac1{u+2v},\qquad
s_4=\frac{u+v}{4v+2u}.
\]
At this point the coordinate-lower constraints are slack and all other inequalities in (H) are satisfied, establishing the exact radius.

**4. All maximizing centers.** For \(m=3\) and \(m\ge5\), any optimal center has \(y_i\ge\rho_*u=s_*\) for every coordinate. Each maximum independent set \(S\) also has \(\sum_{i\in S} y_i\le1-\rho_*v=ks_*\). Every rim vertex belongs to some maximum independent set, so each coordinate must equal \(s_*\). This proves uniqueness.

For \(m=4\), the total-lower inequality of a ball forces \(\sum_i y_i\ge1+\rho_4u\), while adding the two opposite-pair inequalities gives \(\sum_i y_i\le2-2\rho_4v\). Their bounds coincide by the identity \(\rho_4(u+2v)=1\). Thus both opposite-pair sums equal \(1-\rho_4v=2s_4\). The coordinate constraints say precisely \(y_i\ge\rho_4u=\ell_4\). Conversely any point in this two-parameter rectangle satisfies every ball-offset inequality in (H): a singleton independent set has upper bound \(1-\rho_4u\), and its coordinate is at most \(2s_4-\ell_4\le1-\ell_4\); all remaining constraints follow from the fixed pair sums and positive lower bounds. Since \(2s_4>2\ell_4\), both pair intervals have positive length. Hence the optimal-center locus has affine dimension two, as stated.

**5. Contacts at the symmetric center.** For \(m\ge5\), only the \(m\) coordinate-lower facets and the maximum-independent-set facets attain equality. A cycle has exactly two maximum independent sets when \(m\) is even and exactly \(m\) when it is odd. For \(m=3\), the three coordinate facets, three singleton upper facets, and both total-sum facets touch. For \(m=4\), only the total-lower facet and the two maximum-independent-set facets touch. All indicated supporting hyperplanes define actual facets. The total-lower face consists of the \(m\) affinely independent spoke vectors. On a coordinate-zero face, the remaining induced wheel-minus-one-rim graph is connected and contains a triangle, hence its unsigned incidence vectors span a facet of affine dimension \(m-1\). For a maximum independent set \(S\), the tight graph edges form a connected bipartite graph on all \(m+1\) graph vertices: the spokes link each vertex of \(S\) to the hub, and maximality ensures each other rim vertex is adjacent to \(S\). The unsigned incidence matrix of any connected bipartite graph on \(m+1\) vertices has rank \(m\), so these tight vectors affinely span dimension \(m-1\), exactly a facet. For odd \(m\), the total-upper face consists of all rim-cycle edges, whose unsigned incidence matrix has full rank \(m\) because the cycle is odd. This completes the contact counts.

## Verification

The accompanying `verify_wheel_inball.py` reconstructs (H) by enumerating all independent sets and solves its full intrinsic Euclidean Chebyshev-center linear program using `scipy.optimize.linprog` for every \(3\le m\le16\). It compares the numerical optimum against the exact formulas, checks each symmetric proposed center, counts tight inequalities, and verifies all four corners of the exceptional four-rim incenter rectangle. These are finite corroborations of, not replacements for, the duality and inequality proof. Run with `python verify_wheel_inball.py` in an environment with Python, NumPy and SciPy.

## Relationship to prior work

The standard unsigned edge-polytope construction and general graph-dependent face theory are established in Tran and Ziegler (2014), following Ohsugi and Hibi. Ohsugi and Tsuchiya (arXiv:2103.15045, first posted 2021-03-28) treat PQ-type adjacency polytopes of join graphs including wheels, computing Ehrhart and volume information for a *different* graph-polytope construction. Published calculations on wheel **symmetric edge polytopes** concern centrally symmetric edge-root bodies, not the unsigned incidence polytope addressed here. None of the inspected statements establishes the intrinsic inradius and the isolated two-dimensional incenter locus proved above.

## Limitations

The classification concerns the exact ordinary wheel edge-polytope realization with its inherited Euclidean metric; it is not invariant under arbitrary affine transformations or a statement about symmetric edge polytopes. The literature priority assessment remains provisional: an equivalent result may exist under unsigned-incidence, Chebyshev-center, graph-edge, or fractional-cover terminology. Finite solver tests cover only the stated range; the universal claim relies entirely on the analytic proof.

## References

- Tuan Tran and Günter M. Ziegler, *Extremal edge polytopes*, Electronic Journal of Combinatorics 21(2) (2014), #P2.57, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v21i2p57/pdf/ .
- Hidefumi Ohsugi and Akiyoshi Tsuchiya, *PQ-type adjacency polytopes of join graphs*, arXiv:2103.15045 (first posted March 28, 2021), https://arxiv.org/abs/2103.15045 .
