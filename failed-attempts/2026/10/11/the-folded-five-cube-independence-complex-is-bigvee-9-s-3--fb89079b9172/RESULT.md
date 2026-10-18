# The folded five-cube independence complex is \(\bigvee^{9}S^3\)

## Finding
Let \(G\) be the sixteen-vertex folded five-cube, also called the degree-five Clebsch or Greenwood–Gleason graph. Then its ordinary independence complex satisfies
\[
\operatorname{Ind}(G)\simeq\bigvee^{9}S^3.
\]
In particular \(\widetilde H_3(\operatorname{Ind}(G);\mathbb Z)\cong\mathbb Z^9\), with all other reduced integral homology groups zero. The complex is four-dimensional and nonpure: it has exactly forty maximal tetrahedra and sixteen maximal four-simplices.

## Assumptions and scope
The graph is the simple undirected graph with vertex set
\[
V=\{x\in\{0,1\}^5:\textstyle\sum_{j=0}^4x_j\equiv0\pmod2\},
\]
where distinct vertices \(x,y\) are adjacent exactly when they differ in four of the five coordinates. Equivalently, this realizes the quotient of the five-cube by the antipodal involution, using the even-parity representative of each antipodal pair. The object \(\operatorname{Ind}(G)\) is the ordinary abstract simplicial complex of independent vertex subsets. No field coefficients or asymptotic extrapolation are assumed in the homotopy assertion.

The construction has sixteen vertices, forty edges, and strongly regular parameters \((16,5,0,2)\). Distinguish this degree-five graph from its degree-ten complement, which is also called the Clebsch graph in some references. The asserted independence complex is equivalently the clique complex of that degree-ten complement.

## Proof
Represent each vertex as an even-parity five-bit integer and label the sixteen such integers in increasing order. Two distinct labels are adjacent exactly when their bitwise xor has four set bits. The standalone exhaustive verifier examines each of the \(2^{16}-1\) nonempty vertex subsets, accepting it if and only if no pair of its vertices is adjacent. It obtains the face vector
\[
(f_0,f_1,f_2,f_3,f_4)=(16,80,160,120,16)
\]
and no faces of larger dimension. Testing all extensions shows that the maximal faces consist of forty dimension-three faces and sixteen dimension-four faces.

Define a partial matching on the nonempty-face poset deterministically as follows. Initially all 392 simplices are unmatched. Visit the sixteen vertex labels in increasing order. At label \(v\), visit each still-unmatched simplex \(\sigma\) not containing \(v\), in increasing bit-mask order, and match \(\sigma\) with \(\sigma\cup\{v\}\) whenever both are still unmatched. Remove both from the unmatched set before continuing. Every chosen pair differs by one vertex and is therefore a cover relation.

The enumerated matching has 191 disjoint pairs. Its ten critical faces consist of exactly one vertex and nine tetrahedra (dimension-three simplices). For acyclicity, orient every codimension-one inclusion between nonempty faces upwards except matched inclusions, which are oriented downwards. The verifier constructs all 1,200 such directed incidences, then exhaustively removes vertices of indegree zero. All 392 faces are removed, so the oriented Hasse diagram contains no directed cycle. This proves the matching acyclic; no inference is made from sampling or a timeout.

Forman's discrete Morse theorem gives a CW complex homotopy equivalent to \(\operatorname{Ind}(G)\), with precisely one zero-cell, nine three-cells, and no cells of any other positive dimension. Every three-cell attaches to the unique zero-cell, since there are no one- or two-cells. The resulting CW space is the one-point union of nine three-spheres. This proves the claimed integral homotopy equivalence.

## Verification
Running `python3 verify_clebsch.py` with Python 3 reconstructs the graph from five-bit vectors, checks degree five and every common-neighbor count (zero for adjacent vertices, two for nonadjacent vertices), verifies the full face vector and facet dimensions, reconstructs the matching, and checks all 1,200 oriented Hasse incidences by topological sorting. It asserts the exact critical-cell profile before reporting success.

Independently, `python3 verify_homology.py` constructs independent sets by recursive extension, rather than scanning bit masks and reusing the matching. It computes the mod-two simplicial boundary ranks \((15,65,95,16)\), giving reduced mod-two Betti numbers \((0,0,0,9,0)\). This independently corroborates the face enumeration and expected Betti ranks, but does not by itself prove integral homotopy or torsion-freeness. Those stronger conclusions come from the verified acyclic matching and the absence of intermediate critical cells.

The ordinary Euler characteristic is \(-8\), matching the nine odd-dimensional spheres: \(1-9=-8\).

## Relationship to prior work
Barmak's theorem for triangle-free graphs shows that their independence complexes are suspensions; it does not determine an exact sphere multiplicity or rule out higher attaching phenomena for this graph. The folded five-cube is triangle-free, so that theorem is consistent with the calculation but does not imply it.

Cioabă and Mim analyze first clique homology of strongly regular graphs. Their Proposition 7.7 treats the degree-ten Clebsch graph—precisely the complement whose clique complex equals the independence complex here—and establishes vanishing of first homology over fields. First-homology vanishing does not determine the rank-nine third integral homology or the homotopy type. Their manuscript does not state the present wedge decomposition.

Existing calculations for other named graph independence complexes, including the Heawood and dodecahedral graphs, do not cover the present sixteen-vertex graph, even though the complexes use the same functor.

## Limitations
This establishes a single exact finite graph case, not an all-dimension formula for folded cubes or a classification of strongly regular graph independence complexes. Both checking programs are finite computations and not external independent certification. The topological conclusion requires the correctness of the executable enumeration and the standard discrete-Morse homotopy theorem. An equivalent result in unindexed literature cannot be excluded by finite searches; independent audit has not been performed.

## References
1. J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1, first publicly submitted 2010-07-02, especially Theorem 3.4. https://arxiv.org/abs/1007.0418
2. S. M. Cioabă and M. Mim, *On the homology groups of clique complexes of strongly regular graphs*, arXiv:2606.27328v1, 2026, especially Proposition 7.7. https://arxiv.org/abs/2606.27328
3. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145. https://doi.org/10.1006/aima.1997.1650
