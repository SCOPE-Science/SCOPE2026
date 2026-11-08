# Sharp Euclidean inball phases of complete-bipartite spanning-tree polytopes

## Finding

For integers \(2\le p\le q\), let \(G=K_{p,q}\), let \(m=pq\), and let \(t=p+q-1\). In the affine hyperplane \(H=\{x\in\mathbb R^{E(G)}:\sum_e x_e=t\}\), consider the spanning-tree polytope
\[
P_{p,q}=\operatorname{conv}\{\mathbf1_{E(T)}:T\text{ is a spanning tree of }G\}.
\]
All metric quantities use the Euclidean metric induced on \(H\). Define
\[
d_0=\frac{t}{\sqrt{m(m-1)}},\qquad
 d_1=\frac{p-1}{\sqrt{m(q-1)}}.
\]
Then its Euclidean inradius is
\[
\boxed{r(P_{p,q})=\begin{cases}1/\sqrt{12},&(p,q)=(2,2),\\\min\{d_0,d_1\},&\text{otherwise}.\end{cases}}
\]
There is a largest inscribed ball centered at the uniform edge vector \(\mu=(t/m)\mathbf1\). For \((p,q)\ne(2,2)\), exactly two competing obstruction families determine the radius: coordinate nonnegativity and the degree-at-least-one constraints at the vertices in the larger bipartition class. The competing values are \(d_0\) and \(d_1\). The only additional support-plane coincidences in the subset-rank family are the symmetric degree constraints when \(p=q\), and single-edge upper constraints when \(p=q=3\).

The complete affine dimension of the locus \(\mathcal C_{p,q}\) of centers of maximum-radius balls is
\[
\boxed{\dim\mathcal C_{p,q}=\begin{cases}
0,&(p,q)\in\{(2,2),(3,3)\}\text{ or }d_0\le d_1,\\
q(p-1),&d_1<d_0\text{ and }p<q,\\
(p-1)(q-1),&d_1<d_0\text{ and }p=q\ge4.
\end{cases}}
\]
In particular, nonunique optimal centers occur on the degree-controlled side even though the graph itself is edge-transitive. The unique Euclidean circumcenter is \(\mu\), and the circumradius is
\[
\boxed{R(P_{p,q})=\sqrt{t\left(1-\frac{t}{m}\right)}.}
\]
For \(p\to\infty\) with \(q/p^{3/2}\to c\in(0,\infty)\), the ratio \(d_1/d_0\to1/c\). Thus the dominant inball obstruction changes sharply across the scale \(q\asymp p^{3/2}\): for \(c<1\) coordinates control eventually, while for \(c>1\) degree facets control eventually. No eventual statement at \(c=1\) is asserted.

## Assumptions and scope

Every graph is a finite simple undirected complete bipartite graph, with both part sizes at least two; we order the part sizes only to select the larger class for notation. The spanning-tree polytope has dimension \(m-1\) inside \(H\). The coordinate-edge labels and the ambient scalar product are fixed; the result does not concern rescaled coordinates, other matroids, or alternative gauges. The statement concerns balls *within* \(H\), not balls of positive radius in all of \(\mathbb R^m\).

## Proof

**1. Complete inequalities and symmetry.** Edmonds' forest-polytope inequalities, restricted to the spanning-tree rank hyperplane, give an exact description by \(x_e\ge0\) and
\[
 x(E(U))\le |U|-1\qquad(\varnothing\ne U\subsetneq V(G)),
\]
where \(E(U)\) consists of graph edges with both ends in \(U\). For subsets meeting just one part, this inequality is vacuous; if \(U\) meets \(r\) vertices on the first side and \(s\) on the second, its support-plane normal has \(rs\) unit coordinates. The automorphism group acts transitively on the edges, so averaging any optimal center over the group shows that \(\mu=(t/m)\mathbf1\) is also optimal: the inscribed-ball radius of a center is the minimum of finitely many affine, normalized facet slacks and is concave.

**2. Distances from the symmetric center.** The projection of a coordinate basis vector to the tangent space \(\mathbf1^\perp\) has length \(\sqrt{1-1/m}\); hence \(x_e\ge0\) has distance \(d_0\) from \(\mu\). For a subset with \(r,s\ge1\) and \(z=rs<m\), the projected rank-inequality normal has squared norm \(z(1-z/m)\). Its positive slack at \(\mu\) is \(r+s-1-tz/m\), so its squared distance equals
\[
 D(r,s)^2=\frac{\left(r+s-1-\frac{t}{m}rs\right)^2}{rs\left(1-\frac{rs}{m}\right)}.
\]
For \(r=p\) and \(1\le s<q\), this reduces to
\[
 D(p,s)^2=\frac{(p-1)^2(q-s)}{pqs},
\]
which is strictly decreasing in \(s\) and has unique minimum \(d_1^2\) at \(s=q-1\). This rank inequality is equivalent, using \(\sum_e x_e=t\), to degree at least one at a specific vertex on the side of size \(q\).

**3. Sharp domination of all other subset ranks.** First take \(r=1\). With \(a=t/m\),
\[
 D(1,s)^2=\frac{(1-a)^2s}{1-s/m},
\]
which increases with \(s\). Its minimum is attained at \(s=1\), with
\[
 \frac{D(1,1)^2}{d_1^2}=\frac{(q-1)^3}{pq-1}.
\]
For \(q\ge3\) and \(p\le q\), this ratio is at least one because \((q-1)^3\ge q^2-1\ge pq-1\), and equality occurs only at \(p=q=3\). For \(p=q=2\), however, \(D(1,1)^2=1/12<d_1^2=1/4\): this is the stated exceptional simplex.

Now suppose \(2\le r<p\), and set \(z=rs/m\), \(A=r-1>0\), and \(B=(p-r)(q-r)/r>0\). The rank slack becomes \(A(1-z)+Bz\), so
\[
 D(r,s)^2=\frac{(A(1-z)+Bz)^2}{m z(1-z)}.
\]
The continuous minimum of this function occurs at \(z_*=A/(A+B)\). If \(2r\ge q+1\), then \(z_*\ge r/p\), the maximum feasible \(z\); the expression decreases throughout the allowed interval. Consequently
\[
 D(r,s)^2\ge D(r,q)^2=\frac{(q-1)^2(p-r)}{pqr}\ge d_1^2.
\]
The last inequality uses \(r\le p-1\) and \(q\ge p\), and equality can occur only when \(r=p-1\) and \(p=q\).

If \(2r<q+1\), then \(q\ge2r\), and the arithmetic–geometric mean inequality gives
\[
 D(r,s)^2\ge \frac{4AB}{m}=\frac{4(r-1)(p-r)(q-r)}{pqr}.
\]
This exceeds \(d_1^2\) because
\[
4(r-1)(p-r)(q-r)(q-1)>r(p-1)^2.
\]
Indeed, if \(p\ge2r\), the left side is at least \((r-1)p^2(p-1)>r(p-1)^2\). If \(p<2r\), it is at least \(4(r-1)r(2r-1)>r(2r-2)^2\ge r(p-1)^2\). This proves the rank-orbit minimum and all its equality cases, whence the inradius formula by Step 2.

**4. Full center-locus dimensions.** At a controlling nonnegativity constraint, every coordinate of an admissible inball center is at least its corresponding coordinate of \(\mu\). Since the sum of the coordinates is fixed, all are equal: the center is unique. For \((p,q)=(2,2)\), the four sharp one-edge upper bounds \(x_e\le1\) similarly force uniqueness; for \((3,3)\), all nine one-edge upper bounds are tied with the degree constraints and also force uniqueness.

Suppose \(d_1<d_0\), \(p<q\). The only sharp subset-rank orbits at \(\mu\) are the \(q\) constraints requiring every vertex on the larger side to have edge degree at least one. Every maximum-ball center must have all its column sums equal to those of \(\mu\): each must be at least the symmetric value, and their sum is fixed. These independent equalities leave dimension \(m-q=q(p-1)\). All other inequalities are strict at \(\mu\), so a relative neighborhood in this affine space is admissible at the same radius, proving equality of dimensions. If \(p=q\ge4\) and \(d_1<d_0\), sharp constraints occur at vertices on both sides. They force both row and column sums to match \(\mu\), leaving dimension \((p-1)(q-1)\); again all remaining inequalities are strict. If \(d_0=d_1\), the coordinate constraints already force uniqueness. These cases exhaust the stated center classification.

**5. Circumradius and threshold.** Every vertex has precisely \(t\) unit entries and \(m-t\) zero entries, hence squared distance \(t(1-t/m)\) from \(\mu\). Since the vertex average is \(\mu\), the mean squared distance to any other center \(c\) is \(t(1-t/m)+\|c-\mu\|^2\); the maximum squared distance is no smaller. This proves that \(\mu\) is the unique circumcenter. Finally, if \(q/p^{3/2}\to c>0\), then \(d_0\sim1/p\) and \(d_1\sim\sqrt p/q\), giving \(d_1/d_0\to1/c\) and the asserted strict-phase alternatives.

## Verification

The standalone `verify.py` uses only the Python standard library. It checks the projected-normal squared-distance formula and minimum-rank orbit by exact rational arithmetic on a finite grid of part sizes, including the exceptional simplex and all three possible sources of ties; checks the inradius against coordinate obstructions; and checks the asymptotic sign on representative scaling sequences. A separate linear-programming cross-check used the complete facet system for ten small bipartitions, independently optimizing center and radius in the affine hyperplane; it agreed with the formula to numerical solver precision. The infinite-family statements and full center classification are consequences of the written proof, not of finite enumeration.

To replay the standalone checker, run `python3 verify.py` in the directory containing this document.

## Relationship to prior work

The exact rank-inequality description of graphic matroid base polytopes is due to Edmonds and is used here as an established input. Aprile, Fiorini, Huynh, Joret and Wood (arXiv:2106.11945, first public June 22, 2021) study the extension complexity of spanning-tree and forest polytopes, including these rank inequalities; they do not provide an intrinsic Euclidean inradius classification in the inspected material. Dong and Ge (arXiv:2103.05294, first public March 9, 2021) study enumeration of spanning trees of complete bipartite graphs containing a prescribed forest, rather than minimum Euclidean distances to supporting hyperplanes. The present metric result is not implied by the counting formula alone or by an extended-formulation-size bound. A distinct result on Minkowski asymmetry of complete-bipartite spanning-tree polytopes determines a different, affine-invariant optimization problem and does not supply the Euclidean normalization used here. Literature priority beyond the inspected sources remains provisional.

## Limitations

The formulas are for the unweighted, canonical edge-indicator realization of \(K_{p,q}\) with \(p,q\ge2\). They do not assert an inradius formula for other graphic-matroid polytopes or positive coordinate weights. The asymptotic statement leaves the critical scaling constant \(c=1\) undecided at finite dimensions. The finite checker provides corroboration rather than a proof for unbounded part sizes. Independent mathematical auditing and an exhaustive historical-priority certification have not been performed.

## References

1. J. Edmonds, *Matroids and the greedy algorithm*, Mathematical Programming **1** (1971), 127–136; the original graphic-matroid rank description.
2. M. Aprile, S. Fiorini, T. Huynh, G. Joret and D. R. Wood, *Smaller Extended Formulations for Spanning Tree Polytopes in Minor-closed Classes and Beyond*, arXiv:2106.11945 (v1 June 22, 2021), https://arxiv.org/abs/2106.11945.
3. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294 (v1 March 9, 2021), https://arxiv.org/abs/2103.05294.
