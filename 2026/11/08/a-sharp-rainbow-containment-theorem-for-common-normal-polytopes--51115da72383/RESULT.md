# A sharp rainbow-containment theorem for common-normal polytopes

## Finding

**Theorem (one rainbow dominates one entire color).** Let \(d\ge1\) and let \(u_1,\ldots,u_m\in\mathbb R^d\) be fixed nonzero vectors, with \(m\ge1\). For \(b\in\mathbb R^m\) put
\[
P(b)=\{x\in\mathbb R^d:\langle u_j,x\rangle\le b_j\text{ for }1\le j\le m\}.
\]
Let \(\mathcal F_1,\ldots,\mathcal F_m\) be arbitrary **nonempty finite families** of these polyhedra, each equipped with a finite defining vector \(b\). Then there exist \(P_i\in\mathcal F_i\) for all \(i\in\{1,\ldots,m\}\) and an index \(r\in\{1,\ldots,m\}\) such that
\[
\boxed{\ \bigcap_{i=1}^m P_i\ \subseteq\ \bigcap_{P\in\mathcal F_r}P.\ }
\]
The selection and winning color are computable by one maximum-weight assignment on an \(m\times m\) real matrix, followed by \(m\) input scans. The same selected rainbow intersection therefore bounds **all** inclusion-monotone set functionals simultaneously, not just one preassigned volume or point-count statistic.

**Sharpness.** Whenever a bounded full-dimensional polytope has a representation by \(m\) irredundant inequalities in these normal directions, \(m-1\) colors do not suffice for the stated universal containment guarantee, even when all color families are identical and all input bodies contain that polytope. In particular, for axis-parallel boxes in \(\mathbb R^d\), the sharp number is \(2d\).

## Assumptions and scope

All families are finite and nonempty; the number of colors equals the number of listed constraint directions. Their members are closed polyhedra sharing the specified normal list but may have different offsets, positions, shapes, and redundant inequalities. The inequalities are part of the input representation; a nonunique representation does not affect the conclusion. Convexity and boundedness of individual members are not required for the inclusion theorem. The sharpness assertion assumes the indicated polytope has all \(m\) inequalities essential; if normal constraints are redundant, a smaller number may suffice. No probability or generic-position assumption is used.

For a box \(\prod_{j=1}^d[\ell_j,r_j]\), use the \(2d\) fixed normals \(e_j,-e_j\) and upper bounds \(r_j,-\ell_j\).

## Proof

**1. Coordinate severity matrix.** For each color \(i\) and constraint index \(j\), define the largest severity
\[
q_{ij}=\max\{-b_j(P):P\in\mathcal F_i\}.
\]
Finiteness ensures every maximum is attained. Taking all constraints in a color gives
\[
J_i:=\bigcap_{P\in\mathcal F_i}P=P(-q_{i1},\ldots,-q_{im}).
\]

**2. A matrix-assignment lemma.** Given any real square matrix \(q=(q_{ij})\), choose a permutation \(\sigma\) of \(\{1,\ldots,m\}\) maximizing
\[
S(\sigma)=\sum_{j=1}^m q_{\sigma(j),j}.
\]
There is a row \(r\) satisfying \(q_{rj}\le q_{\sigma(j),j}\) simultaneously for every column \(j\). To prove this, draw a directed edge from row \(i\) to row \(\sigma(j)\) whenever \(q_{ij}>q_{\sigma(j),j}\). An edge is never a loop. If the directed graph had a cycle, the columns assigned to its successive destination rows could be reassigned cyclically to their respective source rows. They are distinct columns, and every reassigned entry would strictly increase. This would increase \(S\), contradicting its maximum. Hence the graph is acyclic. A finite acyclic digraph has a vertex \(r\) of outdegree zero; precisely the displayed inequalities hold for that row. This proof allows all degeneracies and ties.

**3. Select witness polytopes.** For each column \(j\), choose \(P_{\sigma(j)}\in\mathcal F_{\sigma(j)}\) attaining \(q_{\sigma(j),j}\) in that column. As \(\sigma\) is a permutation, exactly one member is selected from each color. Their intersection \(R\) obeys every inequality
\[
\langle u_j,x\rangle\le-q_{\sigma(j),j}\le-q_{rj}.
\]
Thus every \(x\in R\) belongs to \(J_r\), proving \(R\subseteq J_r\). The argument is valid also when the intersections are empty.

**4. Sharpness.** Let \(Q=P(b^*)\) be full-dimensional and bounded, with all \(m\) listed inequalities essential. For every \(k\), choose \(x_k\notin Q\) which violates only its \(k\)-th inequality. Such a point exists immediately outside a relative-interior point of the corresponding facet. Choose \(T>0\) so large that every \(x_k\) obeys \(\langle u_j,x_k\rangle\le b^*_j+T\) for all \(j\). For each \(j\) define \(B_j\) by retaining only the \(j\)-th original bound and relaxing all other bounds by \(T\). Every \(B_j\) contains \(Q\), and \(\bigcap_{j=1}^m B_j=Q\). Give each of \(m-1\) colors the same family \(\{B_1,\ldots,B_m\}\). Any rainbow choice uses at most \(m-1\) distinct indices, so some \(k\) is omitted; the witness \(x_k\) belongs to all selected bodies but not to the common monochromatic intersection \(Q\). Therefore the containment conclusion fails with \(m-1\) colors. The cube \([-1,1]^d\) has \(2d\) essential coordinate facets, proving the stated sharp box threshold.

**5. Universality and construction.** For any inclusion-monotone \(F\), \(F(R)\le F(J_r)\). The same \(R,r\) work for every such \(F\) simultaneously. To construct them, scan all inputs to form \(q\), maximize the assignment (for instance by a standard weighted bipartite matching algorithm), find an outdegree-zero row in the strict-improvement graph, and take a stored extremizing input for each assigned column. A polynomial-time assignment algorithm uses \(O(m^3)\) arithmetic operations after the matrix is formed.

## Verification

The accompanying standalone standard-library script `verify.py` reconstructs maximum-weight assignments independently of the proof and tests the sink-row implication on an exhaustive small integer matrix family and larger deterministic pseudorandom matrices. It separately generates axis-parallel box families, checks coordinate-by-coordinate containment of the selected rainbow in the indicated color intersection, and enumerates all reduced-color choices in explicit irredundant box constructions for dimensions one through three. Its observed output is `PASS: 10323 deterministic checks (including all reduced-color tuples).` The universal theorem follows from the preceding cycle argument; finite checks are not offered as a substitute.

## Relationship to prior work

Ivanov (2026), Theorem 1.1, proves a positive dimension-dependent colorful volume bound for **arbitrary** convex bodies using \(2d\) colors; it does not promise containment of a rainbow intersection in a complete color intersection. Edwards and Soberón (2024), Theorems 1.2, 2.8 and 5.3, prove powerful exact colorful **point-count** statements for boxes and fixed-normal \(H\)-convex bodies; the lossless *volume corollary by itself* is thus not new. Sarkar, Xue and Soberón (2019), Section 2.3, give exact quantitative \(H\)-convex witness results under different hypotheses. The present theorem's distinctive assertion is **one unconditionally selected rainbow intersection contained as a set in one full monochromatic intersection**, with an explicit assignment algorithm, universally valid across increasing functionals, and its sharp color-count example. The shared-normal hypothesis is crucial: arbitrary-oriented convex bodies do not satisfy the same lossless inclusion assertion.

## Limitations

No statement is made for varying facet-normal systems, general convex bodies, fractional colorful hypotheses, infinite families without attained offset minima, or fewer colors than the number of essential normals. The connection to the classical weighted-assignment exchange principle is explicit, so no novelty is claimed for that matrix principle itself or for the already established lossless quantitative colorful box-point theorem. Historical priority of the stronger single-rainbow set-containment formulation has not been independently certified.

## References

1. G. Ivanov, *A colorful quantitative Helly theorem for volume*, arXiv:2609.25671v1, first public 2026-09-22, Theorem 1.1 and introduction. https://arxiv.org/abs/2609.25671
2. T. Edwards and P. Soberón, *Extensions of discrete Helly theorems for boxes*, arXiv:2404.14308v1, first public 2024-04-22, Theorems 1.2, 2.8, 5.3, Sections 2 and 5. https://arxiv.org/html/2404.14308v1
3. S. Sarkar, A. Xue and P. Soberón, *Quantitative combinatorial geometry for concave functions*, arXiv:1908.04438v1, first public 2019-08-12, Section 2.3. https://arxiv.org/abs/1908.04438
