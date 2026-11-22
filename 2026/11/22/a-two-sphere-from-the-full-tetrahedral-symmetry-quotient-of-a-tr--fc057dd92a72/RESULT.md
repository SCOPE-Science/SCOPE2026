# A two-sphere from the full tetrahedral symmetry quotient of a truncated-tetrahedron independence complex

## Finding

Let \(T\) be the twelve-vertex truncated-tetrahedral graph: its vertices are ordered pairs \((i,j)\) of distinct elements of \(\{0,1,2,3\}\), with two vertices adjacent exactly when their first coordinates agree or when they are mutually reversed ordered pairs. Let \(X=\operatorname{Ind}(T)\) be its ordinary simplicial independence complex. The complete automorphism group is \(\operatorname{Aut}(T)\cong S_4\), acting by simultaneous relabeling.

**Theorem.** The ordinary geometric quotient of the independence complex has an explicit sequence of sixty elementary cellular collapses onto a closed combinatorial two-sphere. Consequently,

\[
|\operatorname{Ind}(T)|/\operatorname{Aut}(T)\simeq S^2,
\]

and its simple-homotopy type is that of a two-sphere. In particular its fundamental group is trivial and its integral reduced homology is \(\mathbb Z\) in degree two and zero in all other degrees.

The conclusion determines **integral homotopy**, not merely rational homology of the group quotient.

## Assumptions and scope

The graph is the graph of the Archimedean truncated tetrahedron, equivalently the line graph of the once-subdivided complete graph \(K_4\). Vertices \((i,j)\) and \((i,k)\) with distinct second coordinates lie in one of four three-cycles. The only edges between these three-cycles join \((i,j)\) to \((j,i)\). These are all eighteen edges. The four three-cycles are intrinsically distinguishable as the only triangles. Every graph automorphism permutes these four triangles, and the unique external neighbor of \((i,j)\) lies in triangle \(j\). Therefore every automorphism is uniquely a permutation of the four labels; all twenty-four permutations occur.

A simplex of \(X\) is a nonempty independent set (together with the conventional empty simplex). Equivalently, it is the graph of a partial function on four labels without fixed points and without directed two-cycles. Directed three- and four-cycles are permitted. The quotient is the ordinary orbit space of the **geometric realization**, not a set of simplex-orbits treated as an abstract simplicial complex and not the Borel construction. This theorem concerns exactly this graph, its complete automorphism group, and this ordinary independence complex.

## Proof

**1. Replace the quotient by a regular orbit-cell model.** Let \(P\) be the poset of nonempty independent subsets of the twelve graph vertices. The barycentric subdivision \(\Delta(P)\) has a vertex for each such subset and a simplex for every strict inclusion flag. A group element stabilizing a flag fixes each member, since its members have pairwise distinct cardinalities; it therefore fixes every barycenter vertex of the corresponding simplex. The quotient of the barycentric subdivision consequently has a regular cell structure indexed by orbits of strict flags, with facet incidence obtained by deleting one member from a flag and taking its orbit. No two different facets of one flag are identified: their omitted cardinalities differ.

Number the twelve vertices lexicographically from \((0,1)\) to \((3,2)\). Represent a subset by its twelve-bit integer mask. Exhaustive enumeration of masks yields the complete nonempty face vector \((12,48,72,30)\), hence \(162\) faces, with \(3342\) strict flags (of all nonempty lengths). The action of all twenty-four label permutations yields exactly \(146\) flag-orbit cells in dimensions zero through three, with numbers \((11,42,63,30)\). The finite enumeration is specified and checked in the embedded standard-library program `verify.py`.

**2. Construct and verify sixty elementary collapses.** Order every orbit of strict flags by its canonical tuple: the lexicographically least tuple of image masks under all twenty-four automorphisms. Sort orbit cells first by flag length and then by this tuple, giving indices from zero to \(145\). The complete ordered list of sixty pairs \((f,c)\) is embedded as `collapse_pairs.json`. For every successive pair, the verifier checks that the lower-dimensional cell \(f\) has \(c\) as its *unique* remaining immediate coface, that \(c\) has no higher cofaces, that \(f\) is an actual codimension-one boundary face of \(c\), and that the two dimensions differ by one. It then deletes both cells and updates every incidence. These are elementary collapses of the regular CW complex, so they preserve simple-homotopy type. At the end the remaining subcomplex has precisely six vertices, twelve edges and eight two-cells, and no higher-dimensional cells.

**3. Identify the remaining complex as a surface.** The verifier checks directly from the residual incidence structure that every edge has two distinct endpoints and belongs to exactly two triangles, that every triangle is bounded by three distinct edges meeting at three distinct vertices, and that the link of **every** vertex is a single connected cycle. The link check counts parallel link edges with multiplicity, as required in a regular CW complex. The one-skeleton is connected. Thus the residual subcomplex is a compact connected closed topological surface. Its Euler characteristic is

\[
\chi=6-12+8=2.
\]

By the classification of compact connected surfaces it is homeomorphic to \(S^2\). Since the original quotient collapses to this subcomplex, the theorem follows.

## Verification

The accompanying `verify.py` uses only Python's standard library. Run it in the same directory as `collapse_pairs.json` with `python3 verify.py`. It rebuilds all twenty-four automorphisms and tests edge preservation, constructs all independent subsets in two ways (graph adjacency and partial functions without two-cycles), enumerates the complete flag-orbit cell structure, reads all sixty collapse pairs from the actual certificate, verifies all free-face and maximal-coface conditions, and checks that the final complex is a connected closed surface with Euler characteristic two. The expected successful output is recorded in `verify_output.txt`.

This is an exhaustive finite proof for the specified graph and no extrapolation to a family is claimed. In particular, a numerical homology calculation alone would not prove the surface or collapse assertions; the embedded incidence and local-link checks supply the needed stronger certificate.

## Relationship to prior work

Engström's work on claw-free graph independence complexes establishes general connectivity estimates, not this exact quotient. Barmak's star-cluster methods likewise provide reductions and connectivity bounds rather than the stated full symmetry quotient. A publicly indexed calculation of this *same graph*, equivalently the matching complex of the once-subdivided \(K_4\), proves \(X\simeq\bigvee^5 S^2\), describes the complete rational \(S_4\)-homology character and shows that the full quotient is simply connected with one-dimensional rational degree-two homology. Those statements are compatible with, but do not imply, an **integral** homotopy equivalence to \(S^2\); rational calculations alone do not eliminate quotient torsion or higher-dimensional integral phenomena. Another indexed calculation concerns the two-independence complex of the same truncated tetrahedron, which is a different simplicial complex. Calculations for larger truncated simplices concern the unquotiented complexes on twenty or thirty vertices, not this quotient.

The new content is the complete sixty-step collapse and sphere identification, not the previously computed five-sphere homotopy type or rational representation of the covering complex.

## Limitations

The conclusion is a concrete finite classification and does not assert an analogous collapse for larger truncated simplices, for different subgroups of \(S_4\), or for two-independence or edge-matching complexes of the truncated tetrahedron. The automated certificate is fully reproducible, but its review is not an independent mathematical audit. Publication-priority assessment has residual risk from equivalent unindexed descriptions of this quotient.

## References

1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first posted 17 December 2005, https://arxiv.org/abs/math/0512420.
2. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first posted 2 July 2010, https://arxiv.org/abs/1007.0418.
3. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics **27** (2006), 906–923, https://doi.org/10.1016/j.ejc.2005.04.010.
4. *Homotopy and tetrahedral symmetry of a subdivided-complete-graph matching complex*, public mathematical finding (8 November 2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-homotopy-and-tetrahedral-symmetry-of-a-subdivided-complete-graph--eabf618ad7d5.
5. *Mixed sphere wedges and tetrahedral symmetry in the truncated-tetrahedron two-independence complex*, public mathematical finding (18 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-mixed-sphere-wedges-and-tetrahedral-symmetry-in-the-truncated-te--2b26dff9db46.
