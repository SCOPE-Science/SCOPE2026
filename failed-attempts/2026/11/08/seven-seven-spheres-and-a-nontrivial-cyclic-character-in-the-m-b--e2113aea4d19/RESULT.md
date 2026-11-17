# Seven seven-spheres and a nontrivial cyclic character in the Möbius–Kantor dominance complex

## Finding

Let \(M=\operatorname{GP}(8,3)\), the sixteen-vertex Möbius–Kantor graph, and let \(\mathcal D(M)\) be its dominance complex. Then
\[
\mathcal D(M)\simeq\bigvee^{7}S^7.
\]
In particular \(\widetilde H_7(\mathcal D(M);\mathbb Z)\cong\mathbb Z^7\), and all its other reduced integral homology groups vanish.

For the order-eight graph rotation \(r\) defined below, the induced rational character on \(H_7\) is
\[
\bigl(\operatorname{tr}(r_*^k)\bigr)_{k=0}^{7}=(7,-1,3,-1,7,-1,3,-1).
\]
As a rational representation of the rotation group \(C_8\), this is \(2\mathbf 1\oplus3\varepsilon\oplus W\), where \(\varepsilon(r)=-1\) and \(W\) is the rational two-dimensional representation in which \(r\) acts by a quarter-turn. Thus \(\dim_{\mathbb Q}H_7(\mathcal D(M);\mathbb Q)^{C_8}=2\) and \(r_*^4\) acts identically.

The vertex-cover bound of Matsushita is sharp here:
\[
\operatorname{conn}_{\mathbf F_2}(\mathcal D(M))+2=6+2=8=\tau(M).
\]

## Assumptions and scope

All graphs are finite, simple, undirected graphs. The vertices of \(M\) are \(u_i,v_i\), where \(i\in\mathbb Z/8\mathbb Z\). Its twenty-four edges are \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\), for \(i\in\mathbb Z/8\mathbb Z\). This is the standard generalized Petersen realization of the Möbius–Kantor graph. The graph has degree three, girth six, and is bipartite.

A subset \(D\subseteq V(M)\) dominates if every vertex belongs to \(D\) or is adjacent to an element of \(D\). Write \(N_M[w]\) for the closed neighborhood of \(w\). The dominance complex is precisely the simplicial complex
\[
\mathcal D(M)=\{\sigma\subseteq V(M):N_M[w]\not\subseteq\sigma\text{ for every }w\in V(M)\}.
\]
These are the complements of dominating vertex sets, not the ordinary independence, cut, matching, or open-neighborhood complex. In the verifier, vertices are numbered \(u_0,\ldots,u_7,v_0,\ldots,v_7\) by the integers 0 through 15.

The rotation \(r\) maps \(u_i\mapsto u_{i+1}\) and \(v_i\mapsto v_{i+1}\); it preserves every edge class. Only its cyclic subgroup is analyzed, not the full automorphism group's integral representation.

## Proof

**Finite face model.** Encode each vertex subset as a sixteen-bit integer \(s\), and each closed neighborhood as a four-bit-support integer \(c_w\). A subset is a face if and only if \((s\mathbin{\&}c_w)\neq c_w\) for all sixteen vertices \(w\). Independently, the verifier forms the complement \(d\) and confirms that the union of \(d\) and the open neighborhoods of vertices in \(d\) equals the full vertex set. The two tests agree on all \(2^{16}=65{,}536\) candidate subsets. There are 32,390 nonempty faces and 172 facets. Their face counts by dimension \(0,1,\ldots,11\) are
\[
(16,120,560,1804,4176,6976,8208,6462,3136,832,96,4).
\]

**Explicit discrete-Morse matching.** On the nonempty face poset, process the vertex pivots in increasing order \(0,\ldots,15\). At pivot \(j\), simultaneously pair each still-unmatched face \(a\) not containing \(j\) with \(a\cup\{j\}\) whenever both remain; remove each pair before the next pivot. This specifies every pair without an external certificate. There are 16,191 pairs, leaving exactly one zero-dimensional face and seven seven-dimensional faces unmatched. Repeat the same rule in decreasing pivot order \(15,\ldots,0\): it again produces 16,191 pairs and exactly the same counts of critical dimensions.

For each matching, form the directed Hasse graph of *all* nonempty faces. Direct each unmatched cover relation from the upper-dimensional face to its codimension-one subface, and each matched relation in the opposite direction. The standalone verifier constructs all 218,672 cover relations and performs a complete topological sort. The sort visits all 32,390 faces in both matchings, so neither directed Hasse graph contains a directed cycle. In particular both are acyclic Morse matchings, not mere cardinality counts.

By discrete Morse theory the complex is homotopy equivalent to a CW complex with one zero-cell and seven seven-cells, and no cells in other positive dimensions. Each seven-cell attaches to the one-point six-skeleton by a constant map. Therefore its homotopy type is \(\bigvee^{7}S^7\), over the integers, rather than a conclusion based on a field-rank computation.

**Character.** The same vertex-labeled face set gives the exact action of each \(r^k\) on oriented simplicial chains: a fixed face contributes the sign of the induced permutation of its ordered vertices. Summing signs with alternating dimension factors computes the unreduced simplicial Lefschetz number \(L(r^k)\). Since the only unreduced rational homology is \(H_0\cong\mathbb Q\) and \(H_7\cong\mathbb Q^7\), the Lefschetz identity gives \(\operatorname{tr}(r_*^k|H_7)=1-L(r^k)\). Exhaustive signed enumeration yields the eight traces displayed above. The identity \(\operatorname{tr}(r_*^k)=2+3(-1)^k+2\cos(\pi k/2)\) for each integer \(k\) identifies the stated rational representation. This character calculation does not assert a full integral-module splitting.

**Bound.** The eight spokes \(\{u_i,v_i\}\) form a perfect matching, so any vertex cover has at least eight vertices. The bipartition supplies a cover with exactly eight vertices. Hence \(\tau(M)=8\). The wedge of seven seven-spheres has mod-two homological connectivity six. Thus Matsushita's bound \(\operatorname{conn}_{\mathbf F_2}(\mathcal D(M))+2\leq\tau(M)\) is attained.

## Verification

Run `python3 mk_dominance_verify.py` with Python 3 and its standard library. The program checks the two independent face predicates, all edges and vertex degrees, bipartiteness and girth, both matchings, all directed Hasse incidences, all eight rotation actions, and the character decomposition. The expected standard output is provided in `mk_dominance_verify_output.txt` and ends with `VERIFY_OK`. This executable verification enumerates the **entire finite** face poset; it does not extrapolate from samples.

The verifier determines the complete acyclicity of the Morse matchings. This is stronger than a numerical homology computation. The mathematical deduction from critical dimensions to the sphere wedge uses Forman's CW theorem. There is no separate independent expert audit.

## Relationship to prior work

Taylan's work establishes matching-tree techniques and classifies dominance complexes for chordal graphs, forests, and related cycles, but does not cover this nonchordal cubic graph. Matsushita's 2020 work provides the general vertex-cover/homological-connectivity inequality, **not** this equality example or its homotopy type. Matsushita and Wakatsuki identify the combinatorial Alexander duality \(\mathcal D(G)^\vee=\mathcal N(\overline G)\) and compute homology for specified path products, but no inspected theorem gives the present Möbius–Kantor classification. The general Alexander-dual identity alone does not specify the homology or homotopy type of the particular graph's complex.

Other studied complexes of the Möbius–Kantor graph include independence (also with its cyclic character), matching, total cut, and Čech complexes. Their simplicial face conditions differ; the homotopy equivalences and equivariant characters obtained for those complexes do not imply this dominance-complex calculation. Previous work on another incidence graph's dominance complex likewise does not imply the present result.

## Limitations

The homotopy equivalence is non-equivariant, and the only symmetry result is the rational character of the specified cyclic group. An integral splitting of its homology representation and the action of the full automorphism group are not established. Novelty is assessed against inspected primary literature and indexed scientific statements; an equivalent result in unindexed literature remains possible. No independent audit is asserted.

## References

1. D. Taylan, *Matching Trees for Simplicial Complexes and Homotopy Type of Devoid Complexes of Graphs*, arXiv:1501.06754 (first posted January 27, 2015), especially the definition and chordal-graph theorem.
2. T. Matsushita, *Dominance Complexes and Vertex Cover Numbers of Graphs*, arXiv:2009.04145 (first posted September 9, 2020), Theorem 1.
3. T. Matsushita and S. Wakatsuki, *Dominance Complexes, Neighborhood Complexes and Combinatorial Alexander Duals*, arXiv:2312.02639 (first posted December 5, 2023), Theorem 1.1 and the path-product computations.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
