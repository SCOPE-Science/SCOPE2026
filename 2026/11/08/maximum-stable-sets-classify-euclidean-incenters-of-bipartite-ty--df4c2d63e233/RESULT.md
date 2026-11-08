# Maximum stable sets classify Euclidean incenters of bipartite type-B graph-root polytopes

## Finding

For every finite connected simple bipartite graph \(G=(V,E)\) with \(n=|V|\ge2\), form the type-B graph-root polytope
\[
P_G=\operatorname{conv}\bigl(\{0\}\cup\{\pm e_i:i\in V\}\cup\{\pm e_i\pm e_j:ij\in E\}\bigr)\subset\mathbb R^n.
\]
Let \(\mathcal M(G)\) be the family of inclusion-maximal independent vertex sets, \(\alpha(G)\) the maximum size of an independent set, and \(U(G)\) the union of the maximum-cardinality independent sets. In the standard Euclidean metric, the maximum inscribed-ball radius and **all** maximizing centers are respectively
\[
\boxed{r_G=\frac1{\sqrt{\alpha(G)}}},\qquad
\boxed{\mathcal C_G=\Bigl\{c\in\mathbb R^V:\ \sum_{i\in I}|c_i|\le1-\sqrt{\frac{|I|}{\alpha(G)}}\quad(I\in\mathcal M(G))\Bigr\}}.
\]
In particular,
\[
\boxed{\operatorname{affdim}\mathcal C_G=n-|U(G)|},
\]
and the incenter is unique precisely when every vertex belongs to at least one maximum independent set.

For the path with \(n=2k\) vertices, the incenter is unique. For the path with \(n=2k+1\) vertices (\(k\ge1\)) the full incenter locus is the explicit \(k\)-dimensional crosspolytope
\[
\boxed{c_{2j-1}=0\ (1\le j\le k+1),\qquad \sum_{j=1}^k |c_{2j}|\le 1-\sqrt{\frac{k}{k+1}}}.
\]
Among all trees on \(n\ge2\) vertices, the largest possible affine dimension of the incenter locus is exactly
\[
\boxed{\left\lfloor\frac{n-1}{2}\right\rfloor}.
\]
Explicit trees attain the bound for every order; the odd paths attain it for odd order.

## Assumptions and scope

Graphs are finite, simple, **connected**, bipartite and have at least one edge; coordinates are in the fixed canonical root-system realization in \(\mathbb R^n\). The Euclidean ball is \(B_2^n=\{z:\|z\|_2\le1\}\). An incenter is any \(c\) satisfying \(c+r_G B_2^n\subseteq P_G\). A maximal independent set means maximal **under inclusion** and may be smaller than a maximum independent set. A path is ordered along its consecutive edges. No claim about nonbipartite graphs is made: the polar there need not be an integral signed stable-set polytope.

## Proof

**Step 1 (polar and its vertices).** Since the graph has no isolated vertices, the inequalities imposed by the coordinate roots \(\pm e_i\) follow from those imposed by the edge roots \(\pm e_i\pm e_j\). Thus
\[
P_G^\circ=Q_G=\{y\in\mathbb R^n: |y_i|+|y_j|\le1\text{ for every }ij\in E\}.
\]
Fix an orthant with signs \(\sigma_i\). Substituting \(y_i=\sigma_i t_i\) identifies its section with \(t\ge0\) and \(t_i+t_j\le1\) for each edge. The edge--vertex incidence matrix of a bipartite graph is totally unimodular: multiplying columns of one color class by \(-1\) turns it into an oriented incidence matrix. Together with the identity for nonnegativity, this proves every vertex of each orthant section is a \(0/1\) vector (the right-hand side is integral). Such a vector is the incidence vector of an independent set.

Every full-polytope vertex is also a vertex of an orthant section containing it, hence is a signed independent-set incidence vector. If the independent set is not inclusion-maximal, it can be enlarged by a vertex \(j\), and both signs in coordinate \(j\) give two distinct feasible points with the original as midpoint. Conversely, if \(I\) is maximal, any point of \(Q_G\) with the prescribed \(\pm1\) values on \(I\) must vanish on all other vertices, because every vertex outside \(I\) has a neighbor in \(I\). The signed incidence vector is therefore an exposed point (maximize the sum of its signed coordinates on \(I\)) and a vertex. Hence the complete vertex set of \(Q_G\) consists of all signings of the inclusion-maximal independent sets.

**Step 2 (radius and the full center set).** For a centrally symmetric full-dimensional polytope \(P=Q^\circ\), the containment \(c+rB_2^n\subseteq P\) is equivalent, by support functions, to
\[
\langle q,c\rangle+r\|q\|_2\le1\qquad\text{for every vertex }q\text{ of }Q.
\]
At \(c=0\) this allows \(r=1/\max_{q\in Q}\|q\|_2\). Central symmetry also proves no larger radius is possible: averaging the inequalities for \(q\) and \(-q\) gives \(r\|q\|_2\le1\). In the vertex description above the squared norm is \(|I|\), so the largest norm is \(\sqrt{\alpha(G)}\). Applying all independent sign choices at the optimal radius yields precisely the displayed \(\ell_1\)-inequality for each inclusion-maximal independent set. This proves both formulas, including their necessity and sufficiency.

**Step 3 (affine dimension).** If \(|I|=\alpha(G)\), its right side is zero. Consequently every optimal center has \(c_i=0\) for \(i\in U(G)\). All other inclusion-maximal independent sets have cardinality strictly less than \(\alpha(G)\), so their inequalities have positive slack at \(0\). Because there are finitely many, a sufficiently small open neighborhood of \(0\) inside the coordinate subspace \(c_i=0\) for \(i\in U(G)\) satisfies every other inequality. The center locus therefore has affine dimension exactly \(n-|U(G)|\).

**Step 4 (paths and crosspolytope).** For \(P_{2k}\), both alternating color classes have \(k\) vertices and each is a maximum independent set. They cover all \(2k\) coordinates, so the incenter is unique. For \(P_{2k+1}\), the only maximum independent set is the odd-position class, of size \(k+1\). Indeed, if \(k+1\) selected vertices are pairwise nonadjacent, the \(k\) gaps between them must use every unselected vertex, forcing positions \(1,3,\ldots,2k+1\). Thus all odd coordinates of a center vanish. The set of all \(k\) even positions is itself inclusion-maximal and supplies the bound \(\sum_j|c_{2j}|\le1-\sqrt{k/(k+1)}\). Every other maximal independent set has size at most \(k\), hence its right-hand side is at least this bound and its left-hand side on the odd-zero subspace is at most the full even-coordinate sum. No further inequality is active, proving the crosspolytope formula.

**Step 5 (sharp tree bound).** In every bipartite graph the larger of its two color classes gives \(\alpha\ge\lceil n/2\rceil\); moreover \(|U|\ge\alpha\), so the center dimension is at most \(\lfloor n/2\rfloor\). If \(n=2k\) and \(\alpha=k\), both color classes are maximum sets, cover every vertex, and force dimension zero. Otherwise \(\alpha\ge k+1\), giving dimension at most \(k-1\). Hence, for all bipartite graphs, the center dimension is at most \(\lfloor(n-1)/2\rfloor\).

For \(n=2k+1\), the odd path attains dimension \(k\). For \(n=2\) any single-edge tree attains dimension zero. For \(n=2k\) with \(k\ge2\), take the path on \(2k-1\) vertices and attach a new leaf at its second vertex. Its bipartition is \(A\), the odd-position path vertices plus the new leaf, of size \(k+1\), and \(B\), the even-position path vertices, of size \(k-1\). Every vertex in \(B\) has at least two neighbors in \(A\). For every nonempty \(S\subseteq B\), the forest induced on \(S\cup N(S)\) has at least \(2|S|\) edges and at most \(|S|+|N(S)|-1\) edges. Hence \(|N(S)|\ge|S|+1\). Any independent set meeting \(B\) in a nonempty \(S\) can contain at most \(|A|-|N(S)|\) vertices of \(A\), so has size strictly less than \(|A|\). Thus \(A\) is the **unique** maximum independent set and the center dimension is \(2k-(k+1)=k-1\), as required.

## Verification

Run `python check_type_b_incenters.py` with NumPy and SciPy installed. It exhaustively enumerates all \(18{,}248\) labeled trees with \(2\) through \(7\) vertices by Prüfer codes, independently computes all maximal independent sets and the dimension bound, tests the odd-path center polytope by linear programming in orders \(2\) through \(10\), checks the even-order extremal construction through \(16\) vertices, and compares direct primal convex-hull facet distances with the reciprocal square-root independence formula on selected graphs. The successful output ends in `TYPE_B_INCENTER_CHECKS_PASSED trees 18248 convexhull_facets 362 paths 9 extremizers 7`. These finite checks are not substituted for the universal proof above.

## Relationship to prior work

Ohsugi and Tsuchiya introduced the graph-root polytope \(P_G\) and proved reflexivity for bipartite graphs, triangulation and Ehrhart-related properties in 2018. Their later work on matching-generating polynomials treats the type-B family including forests and bipartite cacti. The dual is an unconditional signed stable-set polytope; the integrality of the bipartite stable-set relaxation is a standard total-unimodularity fact and is not claimed as new. The result here adds the complete Euclidean inball **center-locus** classification, its dimension from coverage by maximum independent sets, exact odd-path center crosspolytopes, and sharp extremal freedom among trees. Existing metric work on type-A symmetric edge polytopes, ordinary stable-set polytopes and Hansen polytopes concerns distinct canonical realizations and does not imply the stated type-B center loci by equal notation alone.

## Limitations

Euclidean radii depend on the coordinate realization and are not affine invariants. The identification of all polar vertices uses bipartiteness; no assertion is made for a nonbipartite graph. The tree extremal bound describes the maximum dimension but does not classify every equality-case tree. Computational tests are finite evidence only. The literature search cannot rule out an older equivalent statement under unconditional-stable-set or antiblocking terminology; historical priority remains provisional. No independent mathematical audit has been performed.

## References

1. H. Ohsugi and A. Tsuchiya, *Reflexive polytopes arising from bipartite graphs with \(\gamma\)-positivity associated to interior polynomials*, arXiv:1810.12258, initial public submission 2018-10-29, https://arxiv.org/abs/1810.12258 .
2. H. Ohsugi and A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621, https://arxiv.org/abs/2008.08621 .
3. H. Ohsugi and A. Tsuchiya, *The \(h^*\)-Polynomials of Locally Anti-Blocking Lattice Polytopes and Their \(\gamma\)-Positivity*, open-access journal article, https://doi.org/10.1007/s00454-020-00236-6 .
4. A. Schrijver, *Combinatorial Optimization: Polyhedra and Efficiency*, Springer, 2003; chapters on bipartite incidence matrices, total unimodularity and stable-set polytopes (background only).
