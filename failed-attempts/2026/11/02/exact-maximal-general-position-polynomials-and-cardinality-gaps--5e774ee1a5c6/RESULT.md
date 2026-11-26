# Exact maximal general-position polynomials and cardinality gaps in rectangular rook graphs

## Finding
For all integers \(m,n\ge2\), let \(R_{m,n}=K_m\square K_n\) be the rook graph. A vertex set is in *general position* if no geodesic contains three of its vertices; it is *inclusion-maximal* if adding any unselected vertex destroys this condition. Define the full counting polynomial
\[
M_{m,n}(z)=\sum_{S\text{ inclusion-maximal general-position}}z^{|S|}.
\]
Set \(T(N,k)=N![u^N](e^u-1-u)^k\) for nonnegative integers \(N,k\), and let \(T(0,0)=1\). This counts functions from \(N\) labelled points to \(k\) labelled targets in which every target receives at least two preimages. The complete exact polynomial is
\[
\boxed{M_{m,n}(z)=m!n![x^m y^n]\exp\!\left(xyz+x(e^{zy}-1-zy)+y(e^{zx}-1-zx)\right)+z^n\sum_{a=1}^{m-1}\binom ma T(n,a)+z^m\sum_{b=1}^{n-1}\binom nb T(m,b).}
\]
Here all coefficient extraction is in formal power series, so no convergence hypotheses are needed. In particular, for every \(2\le m\le n\), the cardinalities attained by inclusion-maximal general-position sets are exactly
\[
\boxed{\{m\}\cup\{n,n+1,\ldots,m+n-2\}.}
\]
For \(n\ge m+2\), exactly \(n-m-1\) intermediate sizes are missing. The previously established minimum and maximum are \(m\) and \(m+n-2\); the new assertion is the entire gap-free upper interval, the missing-size gap, and the full multiplicity polynomial.

## Assumptions and scope
All graphs are finite, simple, undirected; \(m,n\ge2\). Cells \((i,j)\) correspond to edges \(ij\) of the complete bipartite graph with \(m\) row-vertices and \(n\) column-vertices. A star component includes a single isolated edge \(K_{1,1}\); unused row and column vertices are allowed in the incidence graph. "Maximal" always means inclusion-maximal, not maximum cardinality. The theorem counts labelled configurations (each board cell distinguished).

## Proof
**1. General-position equivalence.** Any two nonadjacent cells in a rook graph have distance two. For distinct cells \((i,j'),(i,j),(i',j)\), the middle cell lies on a shortest path joining the other two. Conversely a geodesic triple must have precisely this pattern, perhaps with rows and columns exchanged, since the graph has diameter two. Thus a set of cells violates general position precisely when one of its incidence edges has two endpoints each of selected degree at least two. A finite bipartite graph in which every edge has a degree-one endpoint is a disjoint union of stars and isolated vertices: every nontrivial connected component has all its edges incident with one common center. Hence general-position sets correspond bijectively to star forests in the complete bipartite incidence graph.

**2. Classification of inclusion-maximal forests.** If every one of the \(m+n\) bipartite vertices is incident with a chosen edge, an additional edge would have both endpoints of selected degree at least two; the new edge itself violates the star-forest property. Every such *spanning* star forest is therefore inclusion-maximal. If an unused row and unused column coexist, their connecting edge can be added as a new component, so a maximal forest has unused vertices in at most one bipartition class. Suppose some row is unused. Every used column cannot be the center of a nontrivial star: attaching the unused row would be legal. Nor can a used column be an endpoint of an isolated chosen edge: attaching the unused row there would create a two-edge star. Consequently every column is a degree-one leaf of a row-centered star of at least two edges; all columns must be used. Conversely, forests of this form with at least one unused row are maximal: an additional edge either hits an already used row center and used column leaf (making that new edge illegal), or joins an unused row to a used column leaf (making the leaf's previous edge illegal at its center). By exchanging parts, the remaining possibility is a collection of column-centered stars with at least two edges each, covering every row and leaving at least one column unused. The three classes are disjoint and exhaustive.

**3. Exact enumeration.** A spanning forest decomposes into disjoint singleton edges, nontrivial row-centered stars, and nontrivial column-centered stars. Mark each selected edge by \(z\), a row by \(x\), and a column by \(y\). The corresponding labelled-component exponential generating functions are \(xyz\), \(x(e^{zy}-1-zy)\), and \(y(e^{zx}-1-zx)\). The exponential formula then yields the first summand of \(M_{m,n}\). For a nonspanning forest covering all \(n\) columns, choose \(a\) used rows with \(1\le a\le m-1\) and assign all \(n\) labelled columns to these row centers in fibers of at least two: \(\binom ma T(n,a)\) configurations, each with \(n\) selected edges. The transposed class contributes the third summand. This proves the polynomial identity without overcounting.

For an independent finite-sum implementation, the spanning contribution also equals
\[
\sum_{\substack{a,b,c\ge0\\a+c\le m,\ b+c\le n}}\binom ma\binom{m-a}{c}\binom nb\binom{n-b}{c}c!\,T(m-a-c,b)T(n-b-c,a)z^{m+n-a-b-c},
\]
where \(a\) row centers, \(b\) column centers, and \(c\) isolated selected edges are chosen; each \(T\) distributes the remaining leaves among centers. Infeasible terms vanish automatically.

**4. Cardinality spectrum.** Assume \(2\le m\le n\). Each nonspanning maximal forest has exactly \(m\) or \(n\) edges by the preceding classification. A spanning star forest with \(c\) nontrivial components has exactly \(m+n-c\) edges. Because the forest spans both parts and has no isolated vertices, \(2\le c\le m\): a single star cannot cover at least two vertices in both parts, and every star uses at least one row. Hence its cardinality lies in \([n,m+n-2]\). Every integer in this interval occurs. Indeed, fix \(2\le c\le m\), choose \(c-2\) pairwise disjoint isolated selected edges, and on the remaining \(r=m-c+2\ge2\) row-vertices and \(s=n-c+2\ge2\) column-vertices choose one row center joined to \(s-1\) columns and one different column center joined to the remaining \(r-1\) rows; omit the edge between the two centers. This is a spanning two-star forest on the remaining vertices (when \(r=s=2\), these are two isolated edges), hence a spanning \(c\)-component star forest with \(m+n-c\) selected edges. A single full column (all \(m\) cells of that column) is a nonspanning maximal forest of size \(m\) when \(n\ge2\). The asserted spectrum follows.

## Verification
The standalone file `verify.py` constructs each rook graph from its original adjacency rule, obtains graph distances by breadth-first search, flags every forbidden selected triple using the defining geodesic condition, then exhaustively checks both general position and one-cell maximality for every subset. Independently, it computes the theorem's multiplicities from the finite-sum formula using an unrelated labelled-block recurrence for \(T(N,k)\). Run `python3 verify.py`. Tested board dimensions are \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\). The combined exhaustive sweep consists of \(1,152,848\) subsets; all polynomial coefficients matched. In particular, \(M_{2,4}(z)=4z^2+16z^4\), \(M_{3,5}(z)=5z^3+213z^5+15z^6\), and \(M_{4,4}(z)=104z^4+144z^5+16z^6\). Finite checks support, but do not replace, the universal proof.

## Relationship to prior work
Di Stefano, Klavžar, Krishnakumar, Tuite and Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965, Theorem 5.3, prove the lower general-position number of a rook graph is \(\min\{m,n\}\) and explicitly cite the known upper number \(m+n-2\). These endpoints are not asserted to be new here. Klavžar, Neethu and Chandran, *The general position achievement game played on graphs*, arXiv:2111.07425, Theorem 3.6, classify the winner of the corresponding rook-graph achievement game, not the number and lengths of all maximal configurations. Chandran and collaborators, *The general position avoidance game and hardness of general position games*, arXiv:2205.03526, Theorem 4.4, likewise classify game winners without giving this counting polynomial. Iršič and collaborators' *General Position Polynomials* (DOI 10.1007/s00025-024-02133-3) counts ordinary general-position subsets, a different generating function. General spanning-star-forest optimization concerns a related but different graph invariant. The result here is the structural characterization and complete *inclusion-maximal* enumerator on this infinite rook-graph family, including a potentially arbitrarily long forbidden-size gap.

## Limitations
No algorithmic complexity claim is made for arbitrary input graphs, and nothing is asserted for more than two complete-graph Cartesian factors. The count is of all labelled inclusion-maximal sets, not move sequences or winning strategies. The equivalence with star-forest enumeration leaves a residual publication-priority risk from differently named enumerative literature; available targeted searches and inspected papers did not settle that risk absolutely.

## References
1. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965, first publicly available 2023-06-16; see Theorem 5.3. https://arxiv.org/abs/2306.09965
2. S. Klavžar, P. K. Neethu, S. V. Ullas Chandran, *The general position achievement game played on graphs*, arXiv:2111.07425, 2021, Theorem 3.6. https://arxiv.org/abs/2111.07425
3. S. V. Ullas Chandran, S. Klavžar, P. K. Neethu, R. Sampaio, *The general position avoidance game and hardness of general position games*, arXiv:2205.03526, 2022, Theorem 4.4. https://arxiv.org/abs/2205.03526
4. E. K. Welton, S. Khudairi, J. Tuite, *Lower General Position in Cartesian Products*, arXiv:2404.19451, 2024. https://arxiv.org/abs/2404.19451
5. V. Iršič, S. Klavžar, I. G. Rus, J. Tuite, *General Position Polynomials*, 2024, DOI:10.1007/s00025-024-02133-3. https://doi.org/10.1007/s00025-024-02133-3
