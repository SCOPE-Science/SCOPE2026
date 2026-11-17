# The multipath complex of the bidirected triangular prism is a mixed-dimensional sphere wedge

## Finding

Let \(P=C_3\square K_2\) denote the undirected triangular-prism graph. Replace each of its nine undirected edges by the two opposite directed arcs to obtain the digraph \(D=\overleftrightarrow P\). Its ordinary multipath complex \(X(D)\) has one vertex for each of the 18 arcs and a simplex for every arc set that is a vertex-disjoint union of simple directed paths, including singleton paths. Then its **integral homotopy type** is

\[
|X(D)|\simeq \bigvee^{5}S^2\vee\bigvee^{22}S^3\vee\bigvee^{6}S^4.
\]

In particular, the only nonzero reduced integral homology groups are \(\widetilde H_2\cong\mathbb Z^5\), \(\widetilde H_3\cong\mathbb Z^{22}\), and \(\widetilde H_4\cong\mathbb Z^6\), with no torsion. The claim is about the whole homotopy type, not just homology ranks.

## Assumptions and scope

Label the six vertices \(0,1,2,3,4,5\). The nine undirected edges are \(01,12,20,34,45,53,03,14,25\). The 18 directed arcs are sorted lexicographically for the checker. A subset \(A\) of these arcs is a multipath if each graph vertex has at most one incoming and at most one outgoing selected arc and no selected directed circuit occurs. For a finite digraph these two conditions characterize vertex-disjoint unions of directed paths. The empty arc set is the empty simplex.

No planarity embedding, geometric metric, equivariance, or filtration parameter is invoked. The homotopy result is specific to this bidirected triangular prism.

## Proof

**1. Exact face set.** Encode each subset of the 18 ordered arcs by an 18-bit mask. Test both local degree restrictions and directed acyclicity; the latter follows exactly by following each selected successor pointer until termination or repetition. The complete search over all \(2^{18}\) masks produces 687 simplices including the empty face. The nonempty face vector in dimensions zero through four is

\[
(f_0,f_1,f_2,f_3,f_4)=(18,108,260,240,60),
\]

with no higher faces. All face deletions are checked to remain in the complex.

**2. A genuine acyclic Morse matching.** Start with all faces. For each directed-arc index from 0 through 17 in order, match every still-unmatched pair \((\sigma,\sigma\cup\{i\})\) for which both faces remain available, then remove these pairs before the next index. The empty simplex is paired once with a vertex and this pair is removed for the ordinary CW construction. There are then 326 matched nonempty-face pairs, leaving precisely one critical vertex, five critical two-faces, 22 critical three-faces and six critical four-faces. To verify acyclicity rather than infer it from the construction, orient each unmatched codimension-one incidence from the larger face to the smaller, and each matched incidence oppositely. Direct topological sorting visits all 686 nonempty faces in this 2,256-incidence directed Hasse graph. Thus Forman's acyclic matching theorem produces a CW model \(Y\simeq|X(D)|\) with exactly those critical cells.

**3. The integral Morse chain groups have zero differentials.** The exact elimination of a matched face \(\sigma\), with upper mate \(\tau\), uses the signed coefficient \(\langle\partial\tau,\sigma\rangle=\pm1\) to replace \(\sigma\) by its negative signed sum of all the other codimension-one faces of \(\tau\). Recursive substitution is terminating because the matching is acyclic. A critical cell's boundary is reduced by these substitutions and projected to critical faces. The complete, integer-valued calculation yields the zero vector for every critical cell, in every degree. Hence the Morse cellular boundary maps vanish over \(\mathbb Z\), giving the displayed integral homology groups. Independently, the mod-two ranks of the simplicial boundary maps in dimensions 1,2,3,4 are \((17,91,164,54)\). These ranks agree with the Morse calculation; the integer calculation is what rules out torsion.

**4. Vanishing attaching obstructions.** The CW complex \(Y\) has one zero-cell and no one-cells. Its two-skeleton is a wedge of five two-spheres. By the Hurewicz theorem \(\pi_2(\bigvee^5 S^2)\cong H_2(\bigvee^5 S^2;\mathbb Z)\). Because the degree-three Morse differential vanishes, all 22 attaching maps of three-cells represent zero in this \(\pi_2\). Thus the three-skeleton is homotopy equivalent to \(\bigvee^5S^2\vee\bigvee^{22}S^3\).

The group \(\pi_3\) of this three-skeleton is free abelian on the 22 inclusions of the three-spheres, the five Hopf classes into individual two-spheres, and the ten basic Whitehead products between distinct two-sphere inclusions (Hilton–Milnor in degree three). The first 22 coefficients of any four-cell attaching map are its cellular boundary degrees into the three-cells, already zero by Step 3. The Hopf and Whitehead coefficients are detected by the integral cup-square and mixed cup-product structure of the resulting four-dimensional cell attachment.

To check the latter, compute five integral two-cocycles from the signed Morse projection, then verify that their mod-two reductions form a full basis of \(H^2(X(D);\mathbb F_2)\) modulo the image of degree-one coboundaries (mod-two rank 91). Therefore these cocycles also form a rational basis of \(H^2(X(D);\mathbb Q)\). Evaluate their 25 ordered Alexander–Whitney cup-product cochains on all 60 oriented four-simplices. Exact rational Gaussian elimination establishes that **each of the 25 products belongs to the coboundary image** \(\operatorname{im}(\delta^3:\!C^3\to C^4)\), whose rank is 54. Since \(H^4(X(D);\mathbb Z)\cong\mathbb Z^6\) is torsion-free, these products vanish integrally as well. In particular, every degree-four cup pairing vanishes, so the Hopf and Whitehead coefficients of every four-cell attaching map are zero. All four-cell attaching maps are therefore nullhomotopic. The resulting CW complex is precisely the stated wedge of five two-spheres, 22 three-spheres and six four-spheres.

This last argument is essential: zero cellular differentials alone would establish homology but would not rule out nontrivial Hopf attachments.

## Verification

The accompanying standalone file `verify.py` uses only the Python standard library and exact integer, binary-field and rational operations. Run `python3 verify.py` from the extracted package. The complete expected output is `verification_output.txt`, whose first line is `TRIANGULAR_PRISM_MULTIPATH_EXACT_CHECKS_PASS`. The program exhaustively checks all \(2^{18}\) arc subsets, the 2,256 oriented face incidences, 326 Morse pairs, all integral Morse boundary reductions, four independent mod-two boundary ranks, five two-cocycles, and all 25 ordered rational cup products. It also verifies that some raw cup cochains are nonzero, so their exactness is a substantive check rather than a vacuous zero-cochain computation. This finite exhaustive proof depends on the explicit six-vertex graph and does not claim a uniform theorem for larger prisms.

## Relationship to prior work

Caputi–Collari–Di Trani–Smith, *On the homotopy type of multipath complexes* (arXiv:2208.04656, first public 2022-08-09), establish foundations and classifications for directed linear graphs, polygons, small directed grids, and selected other directed families; their directed-grid objects have prescribed arc orientations and do not imply the fully bidirected triangular-prism result. Caputi–Collari–Smith, *Multipath complexes of bidirectional polygonal digraphs* (arXiv:2601.05670, first public 2026-01-09), treats bidirectional paths and individual polygons and motivates investigating richer directed-cycle networks, but a triangular prism has two triangles joined by three rungs and is not a single polygon. Deshpande–Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality* (arXiv:2602.14936, first public 2026-02-16), considers the same construction under a different name, and proves structural conclusions under special orientations; the fully bidirected multiply cyclic prism is not covered by those hypotheses.

Related calculations for **discrete Morse complexes**, graph-metric Rips complexes and total-cut complexes of prisms concern different simplicial constructions. None supplies this multipath homotopy type as an immediate corollary. No claim of absolute priority is made; a stronger unindexed equivalence might exist.

## Limitations

The result is a finite exact classification for the triangular-prism bidirection alone. It does not classify general prism graphs, nonbidirected orientations, automorphism representations, persistent complexes, or cup products in different degrees. Correctness is supported by an executable complete finite enumeration and a homotopy-theoretic interpretation, not by an independently performed mathematical audit. A search cannot rule out all unindexed literature.

## References

1. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (first public 2022-08-09).
2. L. Caputi, C. Collari, and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (first public 2026-01-09).
3. A. Deshpande and S. Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936 (first public 2026-02-16).
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145 (acyclic matching theorem).
5. P. J. Hilton, *On the homotopy groups of the union of spheres*, Journal of the London Mathematical Society 30 (1955), 154–172 (low-degree decomposition of sphere-wedge homotopy groups).
