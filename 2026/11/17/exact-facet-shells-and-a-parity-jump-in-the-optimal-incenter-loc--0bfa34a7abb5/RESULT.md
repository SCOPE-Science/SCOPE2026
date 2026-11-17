# Exact facet shells and a parity jump in the optimal incenter locus of triangular-book symmetric edge polytopes

## Finding

Let \(q\ge 2\) be an integer, let \(B_q=K_2*\overline K_q\) be the graph consisting of \(q\) triangles with the same common edge, and let \(N=q+2\). In the intrinsic Euclidean hyperplane
\[
H_N=\left\{x\in\mathbb R^N:\sum_{i=0}^{N-1}x_i=0\right\},
\]
define the symmetric edge polytope
\[
P_q=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(B_q)\}.
\]
The exact multiset of all facet-supporting hyperplane distances from the origin, together with each facet's number of vertices, is the following union of two indexed families (repeated distances have their multiplicities added):

* **Type A:** For each \(0\le t\le q\), there are \(\binom qt\) facets at distance
  \[
  d_A(t)=\left(q-\frac{(2t-q)^2}{q+2}\right)^{-1/2}.
  \]
  Each has precisely \(2q\) vertices.
* **Type B:** For each \(1\le k\le q+1\), there are \(2\binom q{k-1}\) facets at distance
  \[
  d_B(k)=\left(\frac{k(q+2-k)}{q+2}\right)^{-1/2}.
  \]
  Each has precisely \(q+1\) vertices, so these facets are simplices.

In particular, \(P_q\) has exactly \(3\cdot2^q\) facets, of which \(2^{q+1}\) are simplices. Writing \(\delta=q\bmod 2\), the exact largest inscribed Euclidean ball radius, maximized over **all** centers, is
\[
\boxed{r_q=\left(q-\frac{\delta}{q+2}\right)^{-1/2}.}
\]
Exactly \(\binom q{q/2}\) facets touch the origin-centered optimal ball for even \(q\); for odd \(q\), exactly \(2\binom q{(q-1)/2}\) touch. The set \(\mathcal C_q\) of **all centers of maximal-radius balls** is a nonempty convex set with
\[
\boxed{\dim\operatorname{aff}(\mathcal C_q)=\begin{cases}2,&q\text{ even},\\1,&q\text{ odd}.\end{cases}}
\]

There is a sharp second facet-distance shell. Let \(R_{1,q}^2\) and \(R_{2,q}^2\) be the two largest **distinct** squared lengths of facet polar normals. Then for every \(q\ge2\),
\[
\boxed{R_{1,q}^2=q-\frac{\delta}{q+2},\qquad
R_{2,q}^2=q-\frac{(\delta+2)^2}{q+2},\qquad
R_{1,q}^2-R_{2,q}^2=\frac{4(\delta+1)}{q+2}.}
\]
Thus the exact clearance from the insphere-tangent hyperplanes to the nearest non-tangent facet hyperplanes is
\[
\boxed{R_{2,q}^{-1}-R_{1,q}^{-1}>0.}
\]
The number of facets in this nearest non-tangent shell is \(6\) when \(q=2\), \(14\) when \(q=3\), \(2\binom q{(q-2)/2}\) for even \(q\ge4\), and \(2\binom q{(q-3)/2}\) for odd \(q\ge5\). Only at \(q=2,3\) do simplicial facets share this shell with the type-A facets. For sufficiently large \(q\), the clearance is asymptotic to \(2q^{-5/2}\) along even orders and \(4q^{-5/2}\) along odd orders.

## Assumptions and scope

The common edge has endpoints \(h_0,h_1\); the remaining \(q\) vertices \(v_1,\dots,v_q\) are pairwise nonadjacent and each is adjacent to both endpoints. All edges are simple, unweighted, and undirected. Distances use the metric induced from the **canonical** Euclidean structure of \(\mathbb R^N\), not an arbitrary lattice-equivalent realization. Every facet is counted individually, including antipodal facets. The polytope has dimension \(N-1=q+1\), so every facet has dimension \(q\). The special case \(q=1\) is a triangle: all six facet normals have the same squared length \(2/3\), so there is no second distinct shell; it is not included in the theorem.

## Proof

### 1. Completeness of the polar-vertex classification

In \(H_N\), the polar polytope is
\[
P_q^\circ=\{f\in H_N: |f_u-f_v|\le1\text{ for every }uv\in E(B_q)\}.
\]
The normals of the tight inequalities at \(f\) span \(H_N\) if and only if the graph of tight edges \(uv\) with \(|f_u-f_v|=1\) is connected. Indeed, the edge incidence vectors span the zero-sum hyperplane of each connected component, and hence span all of \(H_N\) exactly for a connected spanning tight-edge graph. Thus a point of the full-dimensional polar is a vertex if and only if its tight-edge graph is connected.

Subtract a common constant from the coordinates of a polar vertex so that the potential \(f_{h_0}=0\). Every tight spanning tree changes potential by \(\pm1\) on each tree edge, so all potential values are integers. The edge \(h_0h_1\) forces \(d=f_{h_1}\in\{-1,0,1\}\).

If \(d=0\), each leaf coordinate belongs to \(\{-1,0,1\}\). A zero leaf has no tight incident edge, so connectivity forces all leaves to have values \(\pm1\). Conversely, when all leaves have values \(\pm1\), each leaf is tightly joined to both hubs; the tight graph is connected. This is type A, with \(2^q\) vertices of the polar.

If \(d=1\), the two hub-to-leaf inequalities force every leaf into \(\{0,1\}\). Each leaf is tightly joined to one hub, and the hub-to-hub edge is itself tight; all \(2^q\) assignments are vertices. The case \(d=-1\) is their antipode, contributing another \(2^q\). These are type B. This proves exact completeness, disjointness and the count \(3\cdot2^q\), with no unenumerated polar vertices.

### 2. Euclidean lengths and facet vertex numbers

For any anchored integral potential word \(w=(w_0,\ldots,w_{N-1})\), its representative in \(H_N\) is \(f=w-\bar w\mathbf1\), where \(\bar w=(\sum_i w_i)/N\). Consequently,
\[
\|f\|_2^2=\sum_iw_i^2-\frac{(\sum_iw_i)^2}{N}.
\]
For type A with \(t\) positive leaves, the sum of coordinates is \(2t-q\) and their sum of squares is \(q\), giving \(\|f\|^2=q-(2t-q)^2/N\) and multiplicity \(\binom qt\). Every leaf is tightly joined to both hubs, and the common hub edge is not tight; there are precisely \(2q\) signed root vertices in the supporting facet.

For type B with \(d=1\), let \(k\) be the number of ones among all \(N\) coordinates. The \(h_1\) coordinate is one and exactly \(k-1\) leaves are one. Thus \(1\le k\le q+1\), \(\|f\|^2=k(N-k)/N\), and the two antipodal choices contribute \(2\binom q{k-1}\). Exactly the hub edge and one hub-to-leaf edge per leaf are tight, giving \(q+1\) affinely independent vertices in the facet. A supporting hyperplane \(\langle f,x\rangle=1\) has distance \(1/\|f\|_2\) from the origin. The two displayed distance spectra follow.

### 3. Maximal insphere and the parity-dependent optimal-center dimension

For type A, \(|2t-q|\) has minimum \(\delta\), with \(\delta=0\) for even \(q\) and \(\delta=1\) for odd \(q\). Hence the maximum type-A squared norm is \(q-\delta/N\), with exactly the stated central-binomial multiplicity. Type B has squared norm at most \(\lfloor N^2/4\rfloor/N\). For even \(q\ge2\), this is \(N/4<q\). For odd \(q\ge3\), the difference is
\[
q-\frac1N-\frac{N^2-1}{4N}=\frac{3q^2+4q-7}{4N}>0.
\]
Thus every maximizing polar normal is type A.

The facet inequalities are \(\langle f,x\rangle\le1\), indexed by polar vertices \(f\). For any ball of radius \(r\) and center \(c\) within \(P_q\), the inequalities for \(f\) and \(-f\) give \(r\|f\|+|\langle f,c\rangle|\le1\). Therefore \(r\le1/\max_f\|f\|\). The origin attains equality, proving the **global** inradius, not merely an origin-restricted radius.

At this radius all maximizing normals must satisfy \(\langle f,c\rangle=0\). Every other polar vertex has strictly smaller length, so its inequality has positive slack at the origin. As the number of facets is finite, a neighborhood of the origin within the orthogonal complement of the maximizing normals consists entirely of optimal centers. Thus the affine dimension of the optimal-center set equals \((N-1)\) minus the rank of the tangent normals.

When \(q\) is even, the maximizing sign words have equally many \(+1\) and \(-1\) leaves and hubs zero. They span exactly the \((q-1)\)-dimensional leaf-zero-sum space: differences of words differing by swapping one plus and one minus give every leaf contrast. The optimal-center dimension is \((q+1)-(q-1)=2\). When \(q\) is odd, maximizing words have leaf sum \(+1\) or \(-1\); differences span the same \((q-1)\)-dimensional contrast space and one maximizing centered word has a nonzero leaf sum. The span has dimension \(q\), yielding a one-dimensional optimal-center locus. These arguments work at the smallest applicable orders, \(q=2\) and \(q=3\).

### 4. The second facet shell, its multiplicity, and the asymptotic gap

The next-largest type-A squared norm comes from the next possible magnitude \(|2t-q|=\delta+2\), so its value is \(R_{2,q}^2=q-(\delta+2)^2/N\). Comparing this against the largest type-B norm gives, for even \(q\ge2\),
\[
R_{2,q}^2-\max_B\|f\|^2
=\frac{3q^2+4q-20}{4(q+2)},
\]
and, for odd \(q\ge3\),
\[
R_{2,q}^2-\max_B\|f\|^2
=\frac{3q^2+4q-39}{4(q+2)}.
\]
These are zero precisely at the respective boundary values \(q=2\) and \(q=3\), and strictly positive for larger admissible orders. The type-A second-shell multiplicities are the two equal binomial counts at \(|2t-q|=\delta+2\). At \(q=2\), four type-B facets also attain this norm; at \(q=3\), twelve type-B facets do. This yields the stated complete nearest-non-tangent counts and explains why the simplicial/type-A tie disappears exactly at \(q=4\).

Subtracting the two top squared norms gives \(((\delta+2)^2-\delta^2)/N=4(\delta+1)/N\). Applying the mean-value theorem to \(u\mapsto u^{-1/2}\) at \(u\asymp q\) gives the two claimed parity-dependent asymptotic constants. Every assertion follows for all the indicated integers, independently of finite experiments.

## Verification

The standalone program `check_book_facets.py` constructs all integer hub-relative potentials, independently checks tight-edge connectivity, computes Euclidean squared norms by exact rational arithmetic, and compares the resulting facet-distance/face-size multiset to both closed formulas. It also computes the exact rank of tangent-normal matrices, verifies both exceptional second-shell multiplicities, and checks the strict stabilization inequalities. Executing `python3 check_book_facets.py` reports:

`TRIANGULAR_BOOK_FACET_SHELL_CHECKS_PASSED facets=6138 norm_entries=6138 incenter_ranks=9 second_shells=9 integer_inequalities=499`

The enumerations cover \(1\le q\le10\); the integer inequalities are checked for \(2\le q\le500\). Those are finite corroborations of the analytic proof, not substitutes for any of its all-order claims.

## Relationship to prior work

The general tight-edge graph criterion for symmetric-edge-polytope facet normals, and the graph-Lipschitz polar interpretation, are established tools. D'Alì, Delucchi and Michałek study gluing along a common edge, including two odd cycles, with enumerative and Ehrhart emphasis. Chen, Davis and Korchevskaia give the general facet-subgraph characterization; Braun and Bruegge study facet numbers for sparse graphs. Mori, Mori and Ohsugi prove facet-count bounds for graph joins, the ambient setting for \(K_2*\overline K_q\). None of those inspected results gives this family's exact **canonical Euclidean** facet-distance multiset, the optimal-center dimension, or the strict second-shell stabilization threshold. A published fan-graph study gives an analogous metric spectrum for \(K_1*P_m\), which is a different graph family except at the isolated \(q=2\) case. Its formula cannot be specialized to the independent-leaf triangular-book family for \(q\ge3\).

## Limitations

The statement concerns the canonical unweighted realization and intrinsic Euclidean metric only. It does not classify arbitrary weighted book graphs, all face dimensions, entire incenter-set boundaries, or graph-metric models under an arbitrary change of inner product. The previously known general facet criterion and general join-graph results are not claimed as discoveries. Literature priority is provisional: an equivalent metric computation in the language of Lipschitz potentials or graph joins might predate this evaluation. The finite verification does not prove uniqueness in the published literature and does not constitute independent mathematical auditing.

## References

1. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, first submitted 11 October 2019, Section 4.2.
2. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, first submitted 26 July 2021.
3. B. Braun and K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303, first submitted 31 January 2022, Theorem 2.3 and Section 4.
4. A. Mori, K. Mori and H. Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, arXiv:2312.11287, first submitted 18 December 2023, Theorem 1.4 and Section 4.
5. *Exact Euclidean facet-distance spectrum and inball-center parity for fan-graph symmetric edge polytopes*, public mathematical record, 11 October 2026, identifier `50ae21474872`, for an adjacent but distinct graph family.
