# The toroidal shattering complex of minimum domination in the Shrikhande graph

## Finding

Let \(V=\mathbb Z_4^2\) and let \(G\) be the standard Shrikhande graph with undirected connection set
\[
A=\{\pm(1,0),\pm(0,1),\pm(1,1)\}.
\]
Set
\[
B=\{(1,2),(3,2),(2,1),(2,3),(1,3),(3,1)\},
\quad H=\operatorname{Cay}(V,B).
\]
The complete family \(\mathcal D\) of *minimum-cardinality ordinary dominating sets* of \(G\) consists precisely of the \(32\) vertex-triangles of \(H\), all of size three. The Cayley graph \(H\) is isomorphic to \(G\) but has no common edges with \(G\).

Regard each \(D\in\mathcal D\) as a Boolean concept whose query at vertex \(v\in V\) returns whether \(v\in D\). A support \(Q\subseteq V\) is shattered by these concepts **if and only if** it is a clique of \(H\) (including the empty clique). Consequently
\[
\Phi_{\mathcal D}(z)=1+16z+48z^2+32z^3,
\qquad \operatorname{VCdim}(\mathcal D)=\operatorname{Ldim}(\mathcal D)=3.
\]
The shattering complex is the canonical sixteen-vertex triangulation of the two-dimensional torus, so
\[
\widetilde H_i(\Delta_{\mathcal D};\mathbb Z)\cong
\begin{cases}
\mathbb Z^2,& i=1,\\
\mathbb Z,& i=2,\\
0,&\text{otherwise}.
\end{cases}
\]
This is an integral statement, with no torsion.

## Assumptions and scope

All graphs are finite, simple, undirected and labeled by pairs of residues modulo four. A dominating set \(D\) satisfies \(V=\bigcup_{v\in D}N_G[v]\) with *closed* neighborhoods. An optimizer means a set of minimum **cardinality**, not merely an inclusion-minimal set, and not a total, paired, or locating dominating set. The trace on \(Q\) of \(D\) is \(D\cap Q\); shattering requires every subset of \(Q\) to appear as some trace. The minimum family has no duplicate concepts.

## Proof

**1. Classification of the optimizers.** Every closed neighborhood in \(G\) contains seven vertices, so no one- or two-vertex set dominates \(16\) vertices: at most fourteen vertices could be covered by a pair. By translating a candidate dominating triple, assume it contains \(0=(0,0)\) and another vertex \(u\). The fifteen nonzero differences partition into the six neighbors \(A\), the six differences \(B\), and the three order-two differences \(C=\{(2,0),(0,2),(2,2)\}\).

Direct substitution into the six-element connection set gives the following finite lemma, with the complete calculation implemented independently in both supplied checkers. For each \(u\in A\), the two closed neighborhoods \(N_G[0]\cup N_G[u]\) leave six uncovered vertices and no third closed neighborhood covers all of them. For each \(u\in C\), they leave four uncovered vertices and no third closed neighborhood covers them all. For each \(u\in B\), they leave four uncovered vertices and **exactly two** third vertices that cover all four. The third vertices are, respectively, as follows for the six possible \(u\):

| \(u\) | Permitted third vertices \(w\) |
|---|---|
| \((1,2)\) | \((2,1),(3,1)\) |
| \((1,3)\) | \((2,1),(3,2)\) |
| \((2,1)\) | \((1,2),(1,3)\) |
| \((2,3)\) | \((3,1),(3,2)\) |
| \((3,1)\) | \((1,2),(2,3)\) |
| \((3,2)\) | \((1,3),(2,3)\) |

Every allowed \(w\) also has \(w-u\in B\). Conversely, the same table shows that whenever the three pairwise differences belong to \(B\), their three closed neighborhoods cover \(V\). Thus dominating triples are exactly the triangles of \(H\). Each vertex belongs to six such triangles (twelve ordered pairs of the other two vertices divided by two), and the total is \(16\cdot6/3=32\). Hence \(\gamma(G)=3\), and these are **all** its optimizers.

**2. The derived graph is a second Shrikhande graph.** The matrix
\[
L=\begin{pmatrix}1&1\\2&3\end{pmatrix}
\]
has determinant one modulo four and maps the six differences of \(A\) bijectively to \(B\): the three chosen positive generators map to \((1,2),(1,3),(2,1)\). Consequently it gives a Cayley graph isomorphism \(G\to H\). Also \(A\cap B=\varnothing\), establishing that the two edge sets are disjoint.

**3. Every optimizer triangle is shattered.** Translation by any element of \(V\) preserves \(\mathcal D\). The \(32\) triangles of \(H\) form precisely two translation orbits of size sixteen, represented by
\[
T_1=\{(0,3),(1,1),(2,0)\},\qquad T_2=\{(0,3),(1,2),(2,0)\}.
\]
For each representative, the eight membership patterns have explicit optimizer witnesses below. For the three listed coordinates in increasing order, the rightmost trace bit represents the first coordinate, the middle bit the second, and the leftmost bit the third. The displayed witnesses each dominate \(G\) and belong to \(\mathcal D\) by the first step. They establish all eight traces, and translation proves the same for every optimizer triangle.

| Trace | Witness for \(T_1\) | Witness for \(T_2\) |
|---|---|---|
| 000 | \(\{(0,0),(1,2),(2,1)\}\) | \(\{(0,0),(1,3),(2,1)\}\) |
| 001 | \(\{(0,3),(2,2),(3,0)\}\) | \(\{(0,3),(1,1),(3,0)\}\) |
| 010 | \(\{(0,2),(1,1),(2,3)\}\) | \(\{(0,0),(1,2),(2,1)\}\) |
| 011 | \(\{(0,3),(1,1),(3,0)\}\) | \(\{(0,3),(1,2),(3,1)\}\) |
| 100 | \(\{(0,1),(2,0),(3,2)\}\) | \(\{(0,1),(2,0),(3,2)\}\) |
| 101 | \(\{(0,3),(1,2),(2,0)\}\) | \(\{(0,3),(1,1),(2,0)\}\) |
| 110 | \(\{(1,1),(2,0),(3,2)\}\) | \(\{(1,2),(2,0),(3,3)\}\) |
| 111 | \(T_1\) | \(T_2\) |

Every subset of a shattered support is shattered. Thus every clique of \(H\) is shattered. Conversely, if a support \(Q\) is shattered, the all-positive trace requires a concept \(D\in\mathcal D\) with \(Q\subseteq D\). Since all \(D\) are triangles of \(H\), \(Q\) is a clique of \(H\). This establishes the exact classification without reliance on extrapolation from finite experiments.

**4. Dimension, face numbers, and topology.** In \(H\), every vertex has six neighbors forming a cycle of length six. Every edge lies in two triangles. The graph has sixteen vertices, forty-eight edges, and thirty-two triangles, so its full clique complex has face numbers \((1,16,48,32)\). The isomorphism \(L^{-1}\) sends this complex to the standard triangulation of the \(4\times4\) periodic square grid with one diagonal per square, i.e. the quotient of the planar triangular tiling by four-step horizontal and vertical translations. The quotient is a triangulation of the orientable torus \(\mathbb R^2/(4\mathbb Z)^2\). Its integral homology is therefore \(\mathbb Z^2\) in degree one and \(\mathbb Z\) in degree two.

The complex has maximum face size three, so its VC dimension is three. A complete online mistake tree of depth four would have a consistent all-positive path containing four **distinct** vertex queries (a repetition would make one of the opposite branches impossible). No three-element concept can answer four distinct queries positively, so the Littlestone dimension is at most three. A shattered triple yields a complete depth-three tree and proves equality.

## Verification

The independently implemented scripts `check.py` (Python 3 standard library only) and `check.cpp` (C++17) enumerate all \(2^{16}=65{,}536\) vertex masks for the fixed graph, determine the complete minimum-dominating family, and check all support traces. The Python program independently enumerates triangles of \(H\), checks the optimizer-family equality, reconstructs two orbit representative witnesses, and computes the triangle-to-edge boundary rank modulo the prime \(1000003\). Both programs output the same exact face numbers. Their recorded output is included as `python_output.txt` and `cpp_output.txt`, but reproducibility rests on the included source and mathematical classification, not on output logs alone. The modular rank is an additional check of Betti numbers, not an integral torsion certificate; the explicit periodic triangulation supplies the integral topological conclusion.

## Relationship to prior work

The standard Cayley description and toroidal embedding of the Shrikhande graph are classical (Sane, 2015), so neither its graph isomorphism type nor its toroidal triangulation is claimed new in isolation. General studies of ordinary domination motivate optimizing over dominating sets (Cyman–Henning–Topp, first public 2017). A 2019 article by VinuPriya–Mageswari–Bibi makes a contradictory ordinary domination-number assertion for the Shrikhande graph; the present result includes a concrete three-set witness and an exhaustive closed-neighborhood coverage check showing that \(\gamma(G)=3\) for the standard Cayley graph. Its separate discussion of total domination does not imply the present assertion.

The previously published studies *Dominance homotopy and symmetry distinguish the Shrikhande–rook twins* (2026) and *Paired-domination distinguishes two graphs with identical total-domination polynomials* (2026) concern, respectively, the complex of complements of arbitrary dominating sets and the number of *paired/total* dominating sets. Neither gives traces of the **minimum ordinary** dominating sets. *A closed-neighborhood shattering-polynomial separation of the Shrikhande and rook graphs* (2026) uses closed-neighborhood *centers* as its Boolean hypotheses; those sixteen seven-vertex concepts are not the thirty-two three-vertex optimizers considered here. Comparing these statements and their mathematical implications does not produce this toroidal optimizer-shattering theorem.

## Limitations

The theorem is exact for one labeled sixteen-vertex graph and its isomorphic Cayley realization; it does not assert corresponding statements for other strongly regular graphs, nor is it a general classification of shattering complexes of minimum dominating sets. The modular boundary calculation alone does not prove torsion-freeness, which comes instead from the explicit torus identification. Literature searches and inspected sources cannot establish priority against every unindexed or inaccessible equivalent result. The proof and code have undergone internal review, not independent mathematical audit.

## References

1. J. Cyman, M. A. Henning, J. Topp, *On accurate domination in graphs*, arXiv:1710.03308, first version 2017-10-09. https://arxiv.org/abs/1710.03308
2. S. Sane, *The Shrikhande graph*, Resonance 20 (2015), 903–918, DOI 10.1007/s12045-015-0255-7. https://doi.org/10.1007/s12045-015-0255-7
3. G. VinuPriya, M. Mageswari, K. Ameenal Bibi, *Total Domination and Inverse Total Domination Number of Some Special Classes of Graphs*, AIJRSTEM 26(1) (2019), 47–57. https://www.academia.edu/39262725/Total_Domination_and_Inverse_Total_Domination_Number_of_Some_Special_Classes_of_Graphs
4. *Dominance homotopy and symmetry distinguish the Shrikhande–rook twins*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-dominance-homotopy-and-symmetry-distinguish-the-shrikhande-rook--288bc37deb9c
5. *Paired-domination distinguishes two graphs with identical total-domination polynomials*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-paired-domination-distinguishes-two-graphs-with-identical-total--0d16d6786052
6. *A closed-neighborhood shattering-polynomial separation of the Shrikhande and rook graphs*, public mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-closed-neighborhood-shattering-polynomial-separation-of-the-sh--670b6697d463
