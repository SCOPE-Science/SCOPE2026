# The open-neighborhood complex of the thirteen-vertex Paley graph is a wedge of twenty-five two-spheres

## Finding
Let \(P_{13}\) be the simple quadratic-residue Paley graph on \(\mathbb Z/13\mathbb Z\), and let \(\mathcal N(P_{13})\) be its ordinary **open** Lovász common-neighbor simplicial complex. Then
\[
\boxed{\mathcal N(P_{13})\simeq\bigvee^{25}S^2.}
\]
More concretely, its nonempty face poset admits an acyclic discrete-Morse matching with exactly one critical vertex and twenty-five critical triangles, and no other critical cells. The matching is perfect over the integers: the only nonzero reduced integral homology group is \(\widetilde H_2\cong\mathbb Z^{25}\). In particular, the fundamental group is trivial.

## Assumptions and scope
All graphs are finite, simple, undirected, and loopless, and homotopy refers to geometric realization. Write
\[
Q=\{1,3,4,9,10,12\}\subset\mathbb Z/13\mathbb Z
\]
for the nonzero quadratic residues. The vertices are \(0,1,\ldots,12\), with distinct vertices \(u\) and \(v\) adjacent if and only if \(v-u\pmod{13}\in Q\). The open neighborhood of \(u\) is \(N(u)=u+Q\), **excluding** \(u\). A nonempty subset \(F\) is a face of \(\mathcal N(P_{13})\) precisely when \(F\subseteq N(u)\) for some \(u\). The thirteen six-vertex neighborhoods are the facets. This is not the clique complex, closed-neighborhood complex, independence complex, or a Vietoris–Rips complex.

Encode a vertex subset \(F\) by the integer \(\sum_{i\in F}2^i\); this last expression is a coding convention, not an assertion about the topology. Orient simplices by increasing vertex labels. A face of cardinality \(k+1\) has dimension \(k\).

## Proof
**1. Finite face model.** For each \(u=0,\ldots,12\), form the bit mask of \(N(u)\). List every nonempty submask and take the union. Independently, a nonempty bit mask \(F\) belongs to the complex precisely when the intersection \(\bigcap_{i\in F}N(i)\) is nonempty. Both descriptions produce the same \(598\) nonempty faces, with
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(13,78,221,195,78,13).
\]
The ordinary Euler characteristic is \(26\), so the reduced Euler characteristic is \(25\). The executable certificate checks all \(8191\) nonempty vertex subsets and independently verifies the strongly regular intersection counts \((13,6,2,3)\), guarding against an incorrect graph or neighborhood convention.

**2. An exact matching.** Start with the set of all nonempty faces, and visit the vertices in the fixed order \(0,1,\ldots,12\). At stage \(v\), visit the still-unmatched faces in increasing bit-mask order. If \(v\notin F\) and \(F\cup\{v\}\) is also still unmatched, pair the two and remove both from subsequent stages. The resulting list in `paley13_certificate.json` has exactly \(286\) matching pairs. The unmatched cells are the singleton \(\{0\}\) and precisely twenty-five two-simplices, with bit masks
\[
\begin{gathered}
44,88,98,134,140,176,262,280,322,518,522,560,644,\\
1036,1042,1096,1282,2058,2072,2082,2192,4114,4130,4144,4354.
\end{gathered}
\]
These numerical masks are sufficient to identify all critical cells; the standalone artifact contains all pairs, not merely the critical-cell counts.

**3. Acyclicity certificate.** Every codimension-one incidence between nonempty faces is directed from the higher-dimensional face to the lower-dimensional face, except that a matched incidence is reversed. There are exactly \(2067\) such incidences. The artifact contains a permutation of all \(598\) face masks; the verifier checks that every directed incidence increases strictly in this permutation. Therefore no directed cycle exists. This verifies Forman's acyclicity condition without assuming acyclicity merely from the choice of pivot order. Each pair is checked to differ in exactly one vertex, so it is a legal face-poset matching.

**4. Homotopy conclusion.** The discrete-Morse theorem now supplies a CW complex homotopy equivalent to \(\mathcal N(P_{13})\) and having one zero-cell, twenty-five two-cells, and no cells of any other positive dimension. Every attaching map of a two-cell has domain \(S^1\) and target the single zero-cell, hence is constant. The CW complex is therefore exactly a wedge of twenty-five two-spheres. No inference from finite-field homology to integral homotopy is used.

## Verification
Run `python3 verify_paley13.py` next to `paley13_certificate.json` with the Python standard library. The program reconstructs all neighborhoods, tests the complete face set by two independent methods, checks the complete matching and the explicit directed-Hasse topological order, and compares boundary ranks over four finite fields. The reported ranks of simplicial boundaries in degrees one through five are \((12,66,130,65,13)\), and the reduced Betti vector is \((0,0,25,0,0,0)\) over each tested field. These modular computations are cross-checks; the **integral homotopy proof rests on the complete acyclic matching**.

The matching is a finite exact certificate, not an extrapolation to further Paley orders. The verifier's output is stored in `verification_output.txt`, and the required files are embedded alongside this document.

## Relationship to prior work
Kahle's 2005 neighborhood-complex paper studies connectivity and homology of random graphs, not this specified deterministic Cayley graph. Matsushita's 2012 work gives a general description of fundamental groups of neighborhood complexes, and his 2014 paper compares box and neighborhood complexes through Kronecker double coverings; neither yields this exact homotopy type or twenty-five-sphere multiplicity. Garijo–Gitler–Márquez–Revuelta classify locally six-cycle graphs and their embeddings, a natural geometric setting since the induced neighborhood of each Paley vertex is a hexagon; embedding classifications do not calculate the **different** Lovász neighborhood complex.

Shukla's 2018 classification covers graphs of maximum degree at most three and **four-regular** circulants, not the six-regular graph here. An accessible prior calculation for the seventeen-vertex Paley graph gives a different neighborhood complex with \(3\)-torsion; that result is not a universal Paley-family formula and does not imply the present thirteen-vertex calculation. For the thirteen-vertex graph itself, graph-parameter catalogues list the adjacency data and spectrum but no topology of this neighborhood complex. The novelty assessment is about theorem implication rather than exact matching of a title or number.

## Limitations
The theorem concerns only the ordinary open-neighborhood complex of \(P_{13}\). It does not classify all Paley graphs, the group action on the twenty-five-dimensional homology, or other neighborhood conventions. The finite certificate is exhaustive for this graph and does not certify novelty; an unindexed equivalent calculation remains possible.

## References
1. M. Kahle, *The Neighborhood Complex of a Random Graph*, first public arXiv version December 4, 2005, arXiv:math/0512077. https://arxiv.org/html/math/0512077v4
2. D. Garijo, I. Gitler, A. Márquez, and M. P. Revuelta, *Hexagonal Tilings and Locally C6 Graphs*, first public arXiv version December 14, 2005, arXiv:math/0512332. https://arxiv.org/html/math/0512332v1
3. T. Matsushita, *Fundamental groups of neighborhood complexes*, initial public version October 10, 2012, arXiv:1210.2803. https://arxiv.org/html/1210.2803v4
4. T. Matsushita, *Neighborhood complexes and Kronecker double coverings*, initial public version April 6, 2014, arXiv:1404.1549. https://arxiv.org/abs/1404.1549
5. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, initial public version February 13, 2018, arXiv:1802.04526. https://arxiv.org/html/1802.04526v2
6. *Paley graph P13*, DistanceRegular.org, graph parameter reference. https://www.math.mun.ca/distanceregular/graphs/paley13.html
7. *Three-torsion in the neighborhood complex of the Paley graph of order seventeen*, publicly available exact case study. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-neighborhood-complex-of-the-paley-graph-of--3bbd3a54ace8
