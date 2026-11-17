# A one-leaf bidirected-cycle fault response through the four initial residue classes

## Finding
For an integer \(n\ge3\), let \(L_n\) be the loopless bidirected graph with vertex set \(\{0,1,\ldots,n\}\) and arcs in both directions between \(i\) and \(i+1\pmod n\) for every \(0\le i<n\), together with the two arcs \(0\to n\) and \(n\to0\). Thus \(L_n\) is a bidirected \(n\)-cycle with exactly one bidirected pendant leaf. Write \(X(L_n)\) for the simplicial multipath complex, with one simplicial vertex per directed arc, in which a set of arcs is a face exactly when it forms a disjoint union of directed paths and isolated vertices.

The complete integral homotopy classification for the first representative of each of the four residue classes of \(n\) modulo four is
\[
\begin{aligned}
X(L_3)&\simeq\bigvee^{3}S^1,\\
X(L_4)&\simeq S^1\vee\bigvee^{2}S^2,\\
X(L_5)&\simeq\bigvee^{3}S^2\vee\bigvee^{2}S^3,\\
X(L_6)&\simeq S^3\vee\bigvee^{2}S^4.
\end{aligned}
\]
Every equivalence is integral and concerns the full homotopy type, not merely homology with field coefficients. No formula for larger cycles is asserted.

## Assumptions and scope
All graphs are finite, loopless, with distinguishable oppositely oriented arcs. The cycle has exactly \(n\) distinct vertices and \(2n\) arcs; the leaf is a new vertex and contributes exactly two arcs. The four values are \(n\in\{3,4,5,6\}\). A face of \(X(L_n)\) has at most one incoming arc and at most one outgoing arc at each graph vertex, and no directed cycle, including a two-cycle. This is equivalent to a disjoint union of consistently oriented directed paths.

We use the standard convention that a simplicial \(k\)-face has \(k+1\) vertices (directed arcs of the graph). A zero-cell of the Morse CW model is a point. The statement is nonequivariant; no claim is made concerning the automorphism action on homology.

## Proof
**Exact simplicial model.** Index the directed arcs by integers \(0,\ldots,2n+1\). For \(0\le i<n\), index \(2i\) is \(i\to(i+1\bmod n)\) and index \(2i+1\) is its reversal. Index \(2n\) is \(n\to0\), and index \(2n+1\) is \(0\to n\). A subset is a face precisely when the in/out-degree bounds and acyclicity condition in the preceding section hold. The standalone verifier constructs all such subsets twice: first by enumerating masks and tracing successor arrows from each vertex, and then by recursively adjoining arcs and independently reconstructing disjoint directed paths from their indegree-zero starts. The two constructions agree exactly.

**Acyclic discrete Morse matchings.** Let \(F_n\) be the set of nonempty faces represented as bit masks. For an ordered list \(p_1,\ldots,p_{2n+2}\) of arc indices, start with all of \(F_n\) unmatched. At each step \(p\), for each currently unmatched face \(a\) lacking bit \(p\), match \(a\) with \(a\cup\{p\}\) whenever both faces remain unmatched. Remove both from further consideration. The four fully specified pivot orders in `CERTIFICATE.json` give matchings with the following critical cells (dimension followed by multiplicity):

| \(n\) | Nonempty faces | Matching pairs | Critical cells |
|---:|---:|---:|---|
| 3 | 26 | 11 | one 0-cell; three 1-cells |
| 4 | 66 | 31 | one 0-cell; one 1-cell; two 2-cells |
| 5 | 162 | 78 | one 0-cell; three 2-cells; two 3-cells |
| 6 | 394 | 195 | one 0-cell; one 3-cell; two 4-cells |

The checker constructs the full Hasse diagram of nonempty faces. It orients unmatched cover relations from coface to face and matched cover relations from face to coface; topological sorting succeeds in every case. Thus each complete matching is acyclic in Forman's sense, without assuming that a mere partial matching supplies a homotopy reduction. The discrete Morse theorem supplies a CW complex with exactly the displayed cells.

**Integral Morse attaching degrees.** Orient each simplex using increasing arc indices. For an oriented \(d\)-simplex \(b\), the signed incidence coefficient of the face \(a=b\setminus\{j\}\) is \((-1)^t\), where \(t\) is the number of selected indices of \(b\) less than \(j\). If a \((d-1)\)-face \(a\) is paired upward with \(b\), its projection to Morse chains is computed by replacing \(a\) with the opposite signed sum of the other facets of \(b\), divided by its incidence \(\pm1\). Repeating recursively terminates because the matching is acyclic. Faces paired downward project to zero, and critical faces project to themselves. This standard integral algebraic Morse reduction yields **zero for every differential between critical cells in all four cases**, not just zero modulo a prime. `verify.py` recomputes all coefficients directly from the raw simplicial boundaries and checks the result.

**From critical cells to homotopy.** For \(n=3\), one 0-cell and three 1-cells give three circles. For \(n=4\), the 1-skeleton is a circle, and the vanishing integer 2-to-1 Morse boundary says both 2-cell attaching maps have winding number zero and are nullhomotopic. For \(n=5\), the 2-skeleton is a wedge of three 2-spheres, and the integral Hurewicz isomorphism identifies its second homotopy group with \(\mathbb Z^3\); zero integral 3-to-2 boundary means both 3-cell attaching maps are nullhomotopic. For \(n=6\), the 3-skeleton is a 3-sphere, so \(\pi_3(S^3)\cong\mathbb Z\), and zero 4-to-3 boundary makes the two attaching maps nullhomotopic. These four CW complexes are exactly the displayed wedges of spheres. \(\square\)

## Verification
Run `python3 verify.py` from the directory containing `CERTIFICATE.json`; it requires only the Python standard library. The command independently constructs the complete face sets, verifies every selected matching pair, recomputes the full reversed-Hasse acyclicity test, and calculates all signed integer Morse differentials. Its recorded deterministic output is `VERIFY_OUTPUT.json`. The source code and the complete pivot-order certificates are included with this result. The successful recorded status is `PASS`.

The certificates are finite proofs for exactly the stated four graph orders. They do not establish a periodic infinite-family classification, and the displayed critical cell counts alone are not used as a substitute for checking the integral attaching degrees.

## Relationship to prior work
Caputi, Collari, and Smith (arXiv:2601.05670, first publicly posted January 9, 2026) analyze multipath complexes of bidirected paths and unmodified bidirected polygons, including homological and connectivity results, and investigate a specified T-operation that produces suspensions. Their bidirected polygons have no attached pendant vertex, and the T-operation requires a different local construction; it does not add a single bidirected leaf to a vertex of a bidirected cycle. Caputi, Collari, Di Trani, and Smith (arXiv:2208.04656) give the basic multipath framework and results on directed polygons, linear graphs, other graph families, and dynamical-module decompositions, but no complete classification for these particular bidirected one-leaf cycles. The present result is a direct finite classification of the new local graph perturbation. Related computations for bare bidirected polygons, one-arc-punctured polygons and different orientations of sunlets concern distinct arc sets and do not imply these four statements.

## Limitations
The classification is restricted to \(3\le n\le6\). The four cases motivate, but do not prove, a possible periodic pattern for larger cycles. No equivariant homotopy claim, arbitrary pendant-path extension, or result for several attached leaves is asserted. An equivalent unindexed or unpublished prior finite calculation remains a bibliographic risk.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (public January 9, 2026), https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656 (public August 9, 2022), https://arxiv.org/abs/2208.04656.
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145.
4. A. Björner, *Topological methods*, in *Handbook of Combinatorics*, 1995.
