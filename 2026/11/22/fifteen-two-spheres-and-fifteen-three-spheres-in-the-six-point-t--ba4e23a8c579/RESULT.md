# Fifteen two-spheres and fifteen three-spheres in the six-point triangular general-position complex

## Finding
Let \(T_6=L(K_6)=J(6,2)\) be the triangular graph with one vertex for each two-element subset of \(\{0,1,2,3,4,5\}\), adjacent when the corresponding subsets intersect. Let \(X=\operatorname{GP}(T_6)\) be the abstract simplicial complex of vertex subsets for which no graph geodesic includes three distinct selected vertices. Then
\[
|X|\simeq\bigvee^{15}S^2\vee\bigvee^{15}S^3.
\]
In particular, \(\pi_1(|X|)=1\), \(\widetilde H_2(X;\mathbb Z)\cong\mathbb Z^{15}\), \(\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{15}\), and every other reduced integral homology group vanishes. This is an integral *homotopy* statement, not only a mod-two rank calculation.

## Assumptions and scope
All graph edges are undirected and have unit length. The graph is precisely the fifteen-vertex line graph of the simple complete graph on six labeled source points, not the two-subset Kneser graph (which is its complement). A face may have any cardinality; it is not required to be a maximal general-position set. By diameter two, a triple fails the geodesic test precisely when it induces a path of two edges in \(T_6\). Therefore \(X\) is *also* the complex of vertex subsets inducing disjoint unions of complete graphs, called the induced cluster complex. This equivalence is proved directly from the distance-two definition and is independently checked by the supplied code.

## Proof
**Step 1 (entire face poset).** Number the source pairs lexicographically. Adjacency is intersection. Every two distinct nonadjacent pairs are disjoint and admit a common neighbor, so \(T_6\) has diameter two. A selected triple is invalid if and only if it has exactly two adjacencies. There are exactly \(180\) such triples. Enumerating all \(2^{15}=32768\) masks and rejecting those containing a forbidden triple yields, in dimensions zero through five, the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(15,105,275,240,66,10).
\]
There are \(711\) nonempty faces. An independent component-is-clique test agrees on every mask. The inclusion-maximal face counts, by cardinality, are \(15,60,6,10\) in sizes \(3,4,5,6\), respectively; this also agrees with the previously published maximal-cluster partition polynomial. All subsequent calculations use the complete face poset rather than only these facet counts.

**Step 2 (genuine simplicial collapses).** For every surviving nonempty face record its immediate cofaces. Process free faces in a deterministic priority queue, preferring larger dimension and then smaller binary mask. Delete a face and its unique immediate coface together and update all incidence degrees. There are exactly \(76\) such elementary collapses: \(10\) of dimensions \((4,5)\), \(56\) of dimensions \((3,4)\), and \(10\) of dimensions \((2,3)\). The surviving complex \(Y\) has face vector
\[
(15,105,265,174)
\]
in dimensions zero through three, with no higher faces. Every deleted lower face has precisely one surviving coface, so each deletion preserves homotopy type. The checker reconstructs and verifies each unique-coface condition; this is not inferred from a Morse log.

**Step 3 (simple connectivity).** The one-skeleton of \(Y\) is the complete graph on the fifteen simplicial vertices. Contract its fourteen-edge star spanning tree to a basepoint, leaving \(91\) oriented edge generators for \(\pi_1\). Every surviving two-simplex supplies a triangular relator. Repeatedly choose the lexicographically first surviving triangle whose boundary has exactly one not-yet-killed generator; that relator identifies the remaining generator (or inverse) with the identity. The checker verifies an ordered sequence of \(91\) such different generator–triangle pairs, after which no generator remains. Each use is a valid van Kampen/Tietze elimination, with both other boundary edges already trivial. Thus \(\pi_1(Y)=1\), without assuming commutativity or confusing first homology with fundamental group.

**Step 4 (integral chain groups and unimodularity).** In the reduced three-dimensional complex, \(C_2(Y;\mathbb Z)\cong\mathbb Z^{265}\) and \(C_3(Y;\mathbb Z)\cong\mathbb Z^{174}\). Orient each simplex by the lexicographic vertex order and form the signed integer third boundary matrix, with every tetrahedron column having four alternating signs. Iterative integer unit-pivot elimination, choosing the pivot with minimum fill and breaking ties lexicographically, finds \(159\) pivots all equal to \(\pm1\); the residual \(106\)-by-\(15\) matrix is exactly zero. Each pivot is eliminated by an integral Schur complement, equivalent to unimodular row and column transformations, and all intermediate nonzero coefficients in this instance remain \(\pm1\). Consequently \(\partial_3\) has rank \(159\), its nonzero Smith invariant factors are all one, and its cokernel is free abelian. Because \(\pi_1(Y)=1\), the edge boundary has rank \(14\) and the image of \(\partial_2\) is all \(\ker\partial_1\), of rank \(105-14=91\). Hence
\[
\operatorname{rank}H_2=265-91-159=15,\qquad
\operatorname{rank}H_3=174-159=15.
\]
The second group injects into the torsion-free cokernel of \(\partial_3\), and the third is a subgroup of a free chain group; both are torsion-free. No homology exists above dimension three, and simple connectivity gives \(H_1=0\).

**Step 5 (upgrade from homology to homotopy).** A simply connected finite three-dimensional CW complex with torsion-free second and third homology is homotopy equivalent to the wedge of the corresponding two- and three-spheres: its simply connected two-skeleton has the homotopy type of a wedge of two-spheres, and each three-cell attaches by an element of the second homotopy group, identified with the integral second homology. The integral attaching matrix admits Smith basis changes, realized by homotopy equivalences and cell slides. Split off unit attaching pairs and observe that the remaining degree-zero attaching maps are nullhomotopic. Here the two ranks are both fifteen, proving the displayed homotopy equivalence. This step uses simple connectivity and integral Smith information; mod-two homology alone would not suffice.

## Verification
Run `python3 verify.py` using Python 3 without third-party dependencies. It regenerates graph distances, all \(180\) forbidden triples, all \(32768\) subset decisions, and independently checks every decision by testing whether connected components of the induced subgraph are complete. It replays the \(76\) genuine simplicial collapses and \(91\) nonabelian triangular generator eliminations, recomputes the signed third boundary, and verifies \(159\) unimodular pivots with an all-zero residual. As an independent arithmetic check, direct original-chain mod-two reductions give boundary ranks \((14,91,169,56,10)\) in degrees one through five, implying reduced mod-two ranks \((0,0,15,15,0,0)\). The signed integer computation, rather than these mod-two ranks, proves the integral assertion.

## Relationship to prior work
Anand–Chandran–Changat–Klavžar–Thomas (first public version 2018) characterize graph general-position sets and, in diameter-two graphs, identify them with cluster-inducing subsets. Ghorbani–Maimani–Momeni–Rahimi Mahid–Klavžar–Rus (2019, Theorem 4.4) determine the *maximum cardinality* for the entire triangular-graph family, not its homotopy type. Di Stefano–Klavžar–Krishnakumar–Tuite–Yero (2023, Theorem 5.2) determine the *minimum size of maximal faces*. Iršič–Klavžar–Rus–Tuite (2024) introduce general-position polynomials but do not identify this triangular-graph homotopy type. A separately indexed 2026 result, *Maximal cluster subgraphs of triangular graphs: a partition polynomial and the exceptional pure case* (record identifier `68bb3fc9b806`), gives a structural description and the facet-size polynomial, including \(15z^3+60z^4+6z^5+10z^6\) at six source points; it does not state the integral homotopy type or analyze fundamental-group relators and signed attaching matrices. Knowing facet *counts* alone does not determine homotopy, while the structural classification makes this computation naturally motivated. Existing indexed results on the same triangular graph concern different complexes (ordinary clique avoidance, cut complexes, neighborhood complexes, two-independence complexes). No prior source found states or directly implies the two sphere multiplicities through a previously proved topological theorem.

## Limitations
The claim is only for \(T_6\); no statement is made for higher triangular graphs, equivariant homology, cup products, or functorial maps. This is a finite, exhaustively reproducible calculation with explicit theoretical topology steps, not an infinite-family classification. The bibliographic search may miss unindexed equivalent results; the separate public cluster enumeration is acknowledged as a close precursor rather than counted as a new face classification. No independent mathematical audit has been performed.

## References
1. B. S. Anand, S. V. Ullas Chandran, M. Changat, S. Klavžar, E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460 (first public 2018-12-20). https://arxiv.org/abs/1812.08460
2. M. Ghorbani, H. R. Maimani, M. Momeni, F. Rahimi Mahid, S. Klavžar, G. Rus, *The general position problem on Kneser graphs and on some graph operations*, arXiv:1903.04286 (first public 2019-03-11), Theorem 4.4. https://arxiv.org/abs/1903.04286
3. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite, I. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965 (first public 2023-06-16), Theorem 5.2. https://arxiv.org/abs/2306.09965
4. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110, doi:10.1007/s00025-024-02133-3. https://doi.org/10.1007/s00025-024-02133-3
5. *Maximal cluster subgraphs of triangular graphs: a partition polynomial and the exceptional pure case*, published mathematical record `68bb3fc9b806` (2026). https://github.com/published-finding corpus/2026
