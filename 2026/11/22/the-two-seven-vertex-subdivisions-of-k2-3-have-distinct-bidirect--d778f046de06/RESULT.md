# The two seven-vertex subdivisions of \(K_{2,3}\) have distinct bidirected multipath homotopy types

## Finding
For positive integers \(a,b,c\ge 2\), let \(\Theta_{a,b,c}\) be the simple graph consisting of three internally vertex-disjoint paths of lengths \(a,b,c\) between two common terminals. Let \(\overleftrightarrow{\Theta}_{a,b,c}\) replace each undirected edge by both directed arcs, and let \(\mathcal X(D)\) be the simplicial complex of directed arc sets that are unions of vertex-disjoint simple directed paths and isolated vertices, with all directed cycles excluded.

**Theorem.** Up to isomorphism, exactly two simple seven-vertex subdivisions of \(K_{2,3}\) exist (equivalently, simple theta graphs with all three arm lengths at least two). Their multipath complexes have integral homotopy types
\[
\begin{aligned}
|\mathcal X(\overleftrightarrow{\Theta}_{2,2,4})| &\simeq \bigvee^{5}S^{3}\vee\bigvee^{4}S^{4},\\
|\mathcal X(\overleftrightarrow{\Theta}_{2,3,3})| &\simeq \bigvee^{5}S^{3}\vee\bigvee^{6}S^{4}.
\end{aligned}
\]
In particular, graphs with identical vertex number, edge number, degree multiset and cycle rank have multipath complexes distinguished by their fourth integral Betti numbers.

## Assumptions and scope
Each graph is finite, simple and connected before replacing every edge by its two directed arcs. The two terminals have labels \(0\) and \(1\). For each arm, introduce fresh internal vertices in increasing order and connect them in a path from terminal \(0\) to terminal \(1\). There are seven vertices, eight undirected edges and sixteen distinct arcs. A selected arc set is allowed precisely when every selected indegree and outdegree is at most one and there is no directed cycle, including an opposite-arc two-cycle. Indeed, every finite digraph with both degrees at most one has components that are paths or cycles. The term multipath complex refers to all such selected arc sets, not the ordinary undirected matching complex.

Every such subdivision of \(K_{2,3}\) with seven vertices satisfies \(a+b+c-1=7\), hence \(a+b+c=8\); subject to \(2\le a\le b\le c\), the only possibilities are \((2,2,4)\) and \((2,3,3)\). Both underlying graphs have degree multiset \((3,3,2,2,2,2,2)\) and cycle rank \(2\).

## Proof
**Exact finite complexes.** Encode an arc set as a sixteen-bit integer, with arcs indexed in lexicographic order by ordered endpoints. Independently enumerate the faces by (i) increasing masks, using hereditary validity and explicit degree/cycle testing, and (ii) a recursive include-or-exclude search maintaining partial incoming and outgoing incidence maps. The two algorithms agree *on the entire sets of faces*. The face vectors, in dimensions \(0\) through \(5\), are respectively
\[
(16,90,220,238,104,12),\qquad (16,90,220,240,108,12).
\]
These correspond to \(681\) and \(687\) faces respectively when the empty face is included.

**Certified discrete-Morse models.** Working in each complete nonempty face poset, process the following arc-index pivots in the displayed order:
\[
\begin{array}{c|c}
\text{Arm lengths}&\text{Arc-index pivots}\\\hline
(2,2,4)&(15,13,1,7,4,6,10,2)\\
(2,3,3)&(15,13,9,7,11,3)
\end{array}
\]
At each pivot \(j\), pair *every still-unmatched* face \(F\) not containing arc \(j\) with the still-unmatched face \(F\cup\{j\}\), whenever both are present. Each stage forms disjoint codimension-one pairs. The standalone exact checker builds the complete Hasse diagram of the original face poset, directs each unmatched cover downwards and each matched cover upwards, and verifies acyclicity by a full topological sort. This visits all \(680\) or \(686\) nonempty faces; there is no closed gradient path. Respectively \(334\) and \(336\) matched pairs leave critical simplices counted by dimension as
\[
\begin{array}{c|rrrrr}
&0&1&2&3&4\\\hline
(2,2,4)&1&0&1&6&4\\
(2,3,3)&1&0&1&6&6.
\end{array}
\]
In particular, Forman's discrete Morse theorem gives CW complexes with precisely those cells, no positive-dimensional cells above dimension four, and no one-cells. The critical cell counts are complete finite certificates, not inferred from a numerical experiment.

**Exact integral boundaries.** Orient every simplex by increasing arc index and use the signed simplicial boundary
\[
\partial[v_0,\ldots,v_k]=\sum_{i=0}^{k}(-1)^i[v_0,\ldots,\widehat{v_i},\ldots,v_k].
\]
The checker regenerates every such boundary, checks \(\partial^2=0\), and performs integer elementary row operations at unit pivots, with the complementary column elimination understood, on *each full boundary matrix*. Every nonzero Smith invariant factor is \(1\), and the respective boundary ranks by degree \(1,2,3,4,5\) are
\[
(15,75,145,88,12),\qquad(15,75,145,90,12).
\]
Thus both integral homology groups are torsion-free. Their only nonzero reduced groups are \(\widetilde H_3\cong\mathbb Z^5\) and \(\widetilde H_4\cong\mathbb Z^4\) or \(\mathbb Z^6\), respectively.

**From the Morse model to homotopy.** For either complex the Morse CW structure has one zero-cell, no one-cells, one two-cell, six three-cells and \(r\) four-cells, where \(r=4\) or \(6\). The two-skeleton is \(S^2\). Since integral second homology vanishes, the cellular boundary \(d_3:\mathbb Z^6\to\mathbb Z\) is surjective. Its integer degree vector is primitive. A change of basis in the six three-cell attaching maps, implemented by a homotopy self-equivalence of their source wedge of six two-spheres, sends this vector to \((1,0,0,0,0,0)\). Therefore the three-skeleton is homotopy equivalent to \(\bigvee^5S^3\).

The integral third homology has rank five, equal to the rank of \(\ker d_3\); consequently the cellular four-boundary \(d_4\) is identically zero. Since \(\pi_3(\bigvee^5 S^3)\to H_3(\bigvee^5 S^3;\mathbb Z)\) is an isomorphism by Hurewicz, every four-cell attaching map is nullhomotopic. Each four-cell contributes a freely wedged four-sphere, proving both claimed homotopy equivalences. This argument uses *integral* incidence and does not infer a homotopy wedge merely from Betti ranks.

## Verification
Run `python3 verify.py` next to this file. The script uses only the Python standard library, independently enumerates every face by two procedures, confirms degree and directed-cycle restrictions, checks every matched Hasse edge and full acyclicity, computes every signed boundary and exact integer unit-Smith reduction, verifies \(\partial^2=0\), and checks the resulting homology and critical-cell counts. `verify_output.txt` records a successful replay. All finite assertions are exhaustive for the two specified sixteen-arc graphs. The proof for the claimed homotopy types then follows from the certified CW cell counts and integral boundary ranks, as above.

## Relationship to prior work
Caputi, Collari and Smith's January 2026 study (reference 1) gives connectivity and homology for *single bidirected polygons*, as well as bidirected path formulas. Its Proposition 2.3 concerns T-operations at a vertex of zero indegree or zero outdegree, a hypothesis absent in these bidirected theta graphs. The 2022/2024 study of Caputi, Collari, Di Trani and Smith (reference 2) develops multipath homotopy and decompositions, but its explicit graph-family classifications concern paths, polygons, small grids and tournaments. Its dynamical-module theorem does not reduce the present examples: each directed arc of these strongly connected bidirected theta graphs lies in a directed two-cycle, so no proper decomposition into modules meeting the theorem's cycle condition is produced.

A prior six-vertex calculation (reference 3) establishes the distinct result \(\mathcal X(\overleftrightarrow\Theta_{2,2,3})\simeq\bigvee^5 S^2\vee\bigvee^6 S^3\). It does not include either seven-vertex theta isomorphism class. The present result gives the complete next-vertex classification and shows that the distribution of arm lengths affects an integral homotopy invariant even when basic graph counts agree. Searches for equivalent results remain subject to normal unindexed-publication risk.

## Limitations
Only fully bidirected three-arm theta graphs with seven graph vertices are classified. No claim is made for arbitrary theta arm lengths, other graph orientations, arbitrary graph subdivisions, homology representations under graph automorphisms, persistent homology or attaching-map formulas beyond the two finite cases. The exhaustive finite certificates prove no pattern for larger graphs. Priority against unindexed works is not independently certified, and the result has not received an independent mathematical audit.

## References
1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1, first public January 9, 2026, https://arxiv.org/abs/2601.05670.
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1, August 2022; later published in *Mathematika* 70 (2024), article e12235, https://arxiv.org/abs/2208.04656.
3. *The bidirected uneven-theta multipath complex is a mixed-dimensional sphere wedge*, publicly available November 8, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-bidirected-uneven-theta-multipath-complex-is-a-mixed-dimensi--dcb824ea52f8/RESULT.md.
4. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145.
