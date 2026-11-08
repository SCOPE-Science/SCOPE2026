# Integral multipath homology and affine four-point symmetry of a doubled directed triangle

## Finding
Let \(D\) be the complete cyclic tripartite digraph with six vertices and twelve arcs specified below. Its multipath complex \(X=X(D)\) satisfies the **complete integral homology classification**
\[
\widetilde H_k(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z, & k=2,\\
\mathbb Z^4, & k\in\{3,4\},\\
0, & \text{otherwise}.
\end{cases}
\]
In particular all groups are torsion-free. The nonempty face vector is \((12,54,104,84,24)\); the complex has 24 tetrahedral and 24 four-simplex maximal faces and is not pure.

Let \(G=(C_2)^3\rtimes C_3\) act by independently interchanging the two vertices of each part and rotating the three parts. With \(\Omega=(\mathbb F_2)^3/\langle(1,1,1)\rangle\), a four-element set, and \(\varepsilon(g)=(-1)^{\text{number of twin interchanges}}\), its rational homology representations are
\[
\widetilde H_2(X;\mathbb Q)\cong\mathbb Q,\qquad
\widetilde H_3(X;\mathbb Q)\cong\mathbb Q[\Omega],\qquad
\widetilde H_4(X;\mathbb Q)\cong\mathbb Q[\Omega]\otimes\varepsilon.
\]
In particular the dimensions of the fixed subspaces for the full group, in degrees 2, 3 and 4, are respectively \(1,1,0\).

## Assumptions and scope
The vertices of \(D\) are \(A_i=\{(i,0),(i,1)\}\) for \(i\in\mathbb Z/3\mathbb Z\). For each \(i\) and \(a,b\in\{0,1\}\), include exactly the arc \((i,a)\to(i+1,b)\). There are no arcs within a part and no backwards arcs. A multipath means a subset of arcs in which every vertex has indegree and outdegree at most one and there is **no directed cycle**; equivalently it is a vertex-disjoint union of directed simple paths and isolated vertices. Empty face included. The orientation and no-cycle condition distinguish this complex from the 24-arc bidirected octahedral multipath complex and from standard directed path homology.

For symmetry coordinates, an element \((s,f)\) consists of a layer rotation \(s\in\mathbb Z/3\) and three bits \(f=(f_0,f_1,f_2)\in(\mathbb F_2)^3\), acting on vertices by \((i,a)\mapsto(i+s,a+f_i)\). The three-bit diagonal subgroup \(\langle(1,1,1)\rangle\) acts trivially on \(\Omega\); a layer rotation cyclically permutes the bit coordinates.

## Proof
**Simplices and boundaries.** Index arcs lexicographically by source, then target, as in the included verifier. All \(2^{12}=4096\) arc subsets are checked using two distinct exact predicates: one follows directed successors and rules out repeated vertices; the other maintains indegrees, outdegrees, and an undirected union-find forest (which is equivalent to a directed-path forest when indegrees/outdegrees are at most one). The predicates coincide on every subset. Enumeration yields exactly 278 nonempty faces and the five entries of the face vector shown above. For every face with ordered arc indices \(e_0<\cdots<e_k\), define the oriented boundary by
\[
\partial[e_0,\ldots,e_k]=\sum_{j=0}^k(-1)^j[e_0,\ldots,\widehat e_j,\ldots,e_k].
\]
The verifier constructs every integer boundary column and checks \(\partial_{k-1}\partial_k=0\) coefficientwise.

**Integral cancellation certificate.** Suppose an integer boundary matrix \(B_k\) has unit entry \(u=B_k(a,b)\in\{1,-1\}\). An integral change of bases and cancellation of this unit pair produces the smaller differential with Schur-complement entries
\[
B'_k(r,c)=B_k(r,c)-B_k(r,b)u^{-1}B_k(a,c),\qquad r\ne a,\ c\ne b.
\]
The corresponding row and column of adjacent differentials are removed, as dictated by \(\partial^2=0\). This is a chain-homotopy equivalence over \(\mathbb Z\), not a finite-field rank approximation. The exact algorithm checks all residual entries, not only diagonal pivots. It works descending from degree four to degree one. With both lexicographically first and last available unit pivots it cancels respectively \((11,43,60,20)\) pairs at degrees \(1,2,3,4\), leaving **one basis vector in chain degree zero, none in one, one in two, four in three and four in four**. Every residual integer differential is identically zero. Hence the displayed reduced integral homology groups follow, without torsion.

**Geometric meaning of the two-dimensional class.** Let \(Y\) be the larger arc-selection complex retaining the indegree/outdegree restrictions but allowing directed cycles. Because all arcs run consecutively between the three layers, \(Y\) is the join of the three matching complexes of \(K_{2,2}\). Each matching complex is two disjoint edges and thus retracts to \(S^0\); hence \(Y\simeq S^2\). In each of the three matching-complex factors, choose one arc from each connected component. These six arc vertices span an octahedral \(S^2\) contained in \(X\) (a selection with at most one arc per layer cannot contain a directed cycle). This sphere represents a primitive generator of \(H_2(Y;\mathbb Z)\). Since the computed \(H_2(X;\mathbb Z)\) has rank one, the inclusion \(X\hookrightarrow Y\) induces an isomorphism in degree two. The four higher-rank groups in degrees three and four are therefore a genuine topological effect of excluding directed cycles, rather than an artifact of the degree restrictions alone.

**Symmetry character and representation.** All 24 transformations act simplicially and preserve the ordered-face chain complex up to exact permutation signs. For each \((s,f)\), the verifier computes the trace on \(C_k(X;\mathbb F_{1009})\) and independently on the image of \(\partial_k\) from an invertible maximal-rank minor. The integral unit-pivot certificate proves these ranks agree over \(\mathbb Q\) and \(\mathbb F_{1009}\). Because homology dimensions are at most four, every integral rational character trace is uniquely determined by its residue modulo 1009. The exact sequence of cycles and boundaries gives
\[
\operatorname{tr}(g\mid H_k)=\operatorname{tr}(g\mid C_k)-\operatorname{tr}(g\mid\operatorname{im}\partial_k)-\operatorname{tr}(g\mid\operatorname{im}\partial_{k+1}).
\]
The output is \(\operatorname{tr}(g\mid H_2)=1\), \(\operatorname{tr}(g\mid H_3)=q(s,f)\), \(\operatorname{tr}(g\mid H_4)=(-1)^{f_0+f_1+f_2}q(s,f)\), where
\[
q(s,f)=\begin{cases}
4,&s=0\text{ and } f=(0,0,0)\text{ or }(1,1,1),\\
0,&s=0\text{ and }f\text{ is not constant},\\
1,&s=1\text{ or }s=2.
\end{cases}
\]
This \(q\) counts fixed points of the four-point \(G\)-set \(\Omega\). Equality of rational characters for every group element proves the three representation isomorphisms; averaging the characters gives fixed-space dimensions \(1,1,0\).

## Verification
Run `python3 verify.py` using only Python's standard library; the enclosed `verify_output.txt` is the output of execution from the packaged verifier. The program exhausts all 4096 candidate arc subsets, cross-checks two independent admissibility tests, constructs all boundary columns and composition checks, performs two independent integral cancellation orders, verifies the embedded octahedral sphere, checks all 24 simplicial automorphisms and their signed rational homology characters. Every claimed integer homology group is supported by unit pivots and an all-zero residual integer chain differential.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith established the multipath-complex construction and classified linear graphs, polygons, small grids and transitive tournaments, but not this nontransitive cyclic three-layer digraph. The comparison theorem of Caputi, Collari and Ramos giving joins of matching complexes assumes that a digraph is acyclic; our \(D\) contains directed triangles. The cycle-free ambient \(Y\) construction in the proof is therefore not an application of that theorem to \(D\). The 2026 bidirectional-polygonal results concern bidirected paths and cycles, not a three-layer complete oriented tripartite digraph. An available calculation of the multipath complex of the bidirected octahedral graph uses 24 arcs, whereas \(D\) has 12; its homology does not imply ours. Likewise, standard path homology of cycle blow-ups and multipath-complex homology are different invariants. Searches for alternative descriptions and broader covering results found no covering theorem among accessible records; search absence is not itself proof of priority.

## Limitations
This is one natural six-vertex digraph, not a classification of all cyclic blow-ups or any arbitrary family. The method proves integral homology and rational linear representations, **not** that \(X\) is homotopy equivalent to a wedge of spheres, and not an integral equivariant decomposition. An equivalent unpublished or unindexed result remains possible. Computer-assisted proof assumes correct execution of the included short standard-library verifier; the combinatorial definitions, full finite ranges, integer operations and exact group actions are available for independent reproduction.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the Homotopy Type of Multipath Complexes*, arXiv:2208.04656v1, first posted 2022-08-09; Sections 1–5.
2. L. Caputi, C. Collari and E. Ramos, *The Weak Categorical Quiver Minor Theorem and Its Applications: Matchings, Multipaths, and Magnitude Cohomology*, arXiv:2401.01248v1, first posted 2024-01-02; especially Theorem 4.20 and the acyclicity hypothesis.
3. L. Caputi, C. Collari and J. P. Smith, *Multipath Complexes of Bidirectional Polygonal Digraphs*, arXiv:2601.05670v1, first posted 2026-01-09; introduction and main theorems.
