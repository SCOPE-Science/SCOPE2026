# A three-boundary two-sphere trichotomy for nine-vertex grid matching complexes

## Finding
Let \(P_3\) be the three-vertex path and \(C_3\) the three-cycle. For a finite simple graph \(G\), its *ordinary matching complex* \(\mathcal M(G)\) has one simplicial vertex for each graph edge and one simplex for each set of pairwise vertex-disjoint graph edges. There are three natural boundary conditions on the smallest three-by-three square grid:

\[
\begin{aligned}
\mathcal M(P_3\square P_3)&\simeq\bigvee^{5}S^2,\\
\mathcal M(P_3\square C_3)&\simeq\bigvee^{16}S^2,\\
\mathcal M(C_3\square C_3)&\simeq\bigvee^{26}S^2.
\end{aligned}
\]

All equivalences are ordinary integral homotopy equivalences. The rectangular first case is a known comparator, not presented as a new discovery; the cylindrical and fully periodic cases are the new exact boundary values. In particular, the middle and last complexes have free integral second homology of ranks \(16\) and \(26\), are simply connected, and have no other reduced homology.

## Assumptions and scope
The vertex set is \(\{0,1,2\}^2\), and two grid vertices are adjacent when exactly one coordinate changes along an edge of the corresponding factor. The factors are simple graphs: \(C_3=K_3\), while \(P_3\) has edges \(01\) and \(12\). Consequently the open, cylindrical and toroidal graphs have respectively \(12,15,18\) edges, and the largest possible matching has four edges. No multigraph edges or extra diagonal edges are admitted.

A face of cardinality \(k\) corresponds to a simplicial cell of dimension \(k-1\). The empty face is included in enumerations but not treated as a geometric vertex. The result concerns these three specific nine-vertex graphs; no assertion is made for arbitrary strip widths.

## Proof
**Step 1: complete finite face sets.** Number the nine graph vertices lexicographically by their coordinates. Number all graph edges lexicographically by their ordered endpoint indices. Iterate through every list of pairwise vertex-disjoint edges, inserting the empty list. An independent enumeration of all edge-index combinations agrees. For faces of cardinalities \(0,1,2,3,4\), the counts are

\[
\begin{array}{c|rrrrr}
 &0&1&2&3&4\\\hline
P_3\square P_3&1&12&44&56&18\\
P_3\square C_3&1&15&69&107&36\\
C_3\square C_3&1&18&99&180&72
\end{array}
\]

Both enumerations are implemented independently in `verify_torus.py`. This table is an exact enumeration of finite matchings, not sampling.

**Step 2: elementary collapses.** The file `CERTIFICATE.json` lists complete sequences of \(25,43,80\) elementary simplicial collapse pairs for the three complexes. A listed pair \((\sigma,\tau)\) is accepted only if \(\tau\) contains \(\sigma\), \(\dim\tau=\dim\sigma+1\), and \(\tau\) is the *unique* immediate coface of \(\sigma\) among all faces still present. Uniqueness of the immediate coface also rules out larger cofaces, so removing the pair is a valid elementary collapse. `verify_torus.py` reconstructs each original face set and checks this condition afresh at every step. The resulting complexes have no cells above dimension two; their numbers of vertices, edges and triangles are respectively

\[
(12,37,31),\quad(15,62,64),\quad(18,91,100).
\]

**Step 3: fundamental groups.** For each surviving two-dimensional simplicial complex, `CERTIFICATE.json` supplies a spanning tree of its entire one-skeleton, with respectively \(11,14,17\) edges. The graph is connected, as verified from those tree edges. After setting spanning-tree edges to identity, each non-tree edge is a generator of the standard triangular presentation of the fundamental group. There are respectively \(26,48,74\) such generators. The certificate then lists a triangle and a generator for every elimination: the triangle is an actual remaining two-simplex, and among its three boundary edges exactly the named generator has not yet been eliminated or declared a spanning-tree edge. Its triangular boundary relation therefore forces the named generator to be trivial. Each step is checked directly, and in all three cases no generator remains. Thus every original matching complex is simply connected.

**Step 4: integral homotopy.** Elementary collapses preserve homotopy type. For a connected simply connected two-dimensional finite CW complex, the only possible nonzero reduced homology group is the second, which is a subgroup of a finitely generated free cellular chain group and hence free abelian. The Euler characteristics of the three collapsed complexes are \(6,17,27\), so these ranks are respectively \(5,16,26\). By the degree-two Hurewicz theorem, each integral basis class is represented by a map of a two-sphere. Wedge these representing maps: the resulting map from a wedge of the stated number of two-spheres induces an isomorphism on all integral homology groups. Since both spaces are simply connected CW complexes, the homological Whitehead theorem makes that map a homotopy equivalence. This proves all three formulas integrally.

## Verification
All of the evidence required for the finite proof is embedded alongside this document. Run `python verify_torus.py` from the directory containing `CERTIFICATE.json`; only the Python standard library is required. This re-enumerates all faces in two independent ways, checks \(148\) elementary collapse pairs and \(148\) triangular generator eliminations, verifies spanning trees and Euler characteristics, and independently computes mod-two simplicial boundary ranks. `CHECK_OUTPUT.txt` records the output of a successful full execution. The mod-two calculation corroborates the formulas but is not substituted for the integral homotopy proof.

## Relationship to prior work
The rectangular \(P_3\square P_n\) matching complexes are studied in P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs* (first public preprint 2026-09-23). A 2021 work by S. Goyal, S. Shukla and A. Singh explicitly defines the graph by Manhattan adjacency in an interval rectangle; that article was subsequently retracted, and its claimed homotopy recursion is **not** used here. Their graph definitions distinguish open boundaries from periodic ones. The present calculation treats the added wrap-around edges as changes in the matching complex, not as consequences of those rectangular results. Published calculations for other cylinders, including \(P_3\square C_5\), likewise do not determine the distinct three-column case. A search for the same periodic graph via its aliases \(K_3\square K_3\) and the nine-vertex rook graph produced no equivalent topological classification; such non-detection does not establish absolute novelty.

## Limitations
The statement treats exactly the three products on nine vertices and does not extrapolate to longer or higher-dimensional grids. Only nonequivariant integral homotopy is claimed; no symmetry action, persistent map or torsion statement for other graph sizes is inferred. The latest 2026 motivating manuscript was checked at the public abstract level only because full text could not be accessed, which leaves a bibliographic overlap risk. Independent external validation has not been performed.

## References
1. P. Chauhan, A. Sharma, S. Shukla, *Homology of matching complexes of \(3\times n\) grid graphs*, arXiv:2609.27366v1 (first submitted 2026-09-23), https://arxiv.org/abs/2609.27366.
2. S. Goyal, S. Shukla, A. Singh, *Matching complexes of \(3\times n\) grid graphs*, Electronic Journal of Combinatorics 28(4), P4.16 (2021), https://doi.org/10.37236/10496. Retracted; cited only for its explicit rectangular graph definition and historical context.
3. *Mixed-dimensional matching-complex homotopy on the pentagonal three-row cylinder \(P_3\square C_5\)*, indexed public mathematical record (2026-11-08); distinct graph parameter.
