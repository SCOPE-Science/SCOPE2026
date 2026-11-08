# Exact face-reversal sectors and metric centers of the four-by-four square-ice torus

## Finding

The labelled graph \(C_4\square C_4\), embedded as a periodic square grid, has \(2970\) Eulerian orientations (two arrows into and two arrows out of each vertex). Give two such orientations an edge when one is obtained from the other by reversing the four arrows of **one coherently oriented elementary square**. There are \(8768\) undirected edges in this configuration graph, and its complete component decomposition is

\[
60K_1\;\sqcup\;4H_{140}\;\sqcup\;4H_{340}\;\sqcup\;H_{990},
\]

where the subscript denotes the vertex count of a connected component. The nine nontrivial components are separated exactly by the pair of integer fluxes \((a,b)\in\{1,2,3\}^2\); all sixty boundary-flux states are frozen. Every nontrivial component has radius \(8\). Each \(140\)-vertex component has diameter \(9\), while the \(340\)- and \(990\)-vertex components have diameter \(12\). The entire disconnected graph has no finite global diameter.

Each \(140\)-vertex component has \(320\) edges and eccentricity counts \((8:92,9:48)\); each \(340\)-vertex component has \(960\) edges and eccentricity counts \((8:28,9:168,10:96,11:32,12:16)\). The central \(990\)-vertex component has \(3648\) edges and eccentricity counts

\[
(8:2,9:284,10:416,11:224,12:64).
\]

In the central component the two, and only two, metric centers are the two checkerboard arrow configurations in which all sixteen faces have directed boundaries. Its exact unordered pair-distance distribution, at distances \(1,\dots,12\), is

\[
(3648,14112,35904,66064,92224,102304,95680,58579,16992,3632,352,64).
\]

## Assumptions and scope

Rows and columns are indexed by \(i,j\in\mathbb Z/4\mathbb Z\), with all edges and faces labelled. Let \(h_{ij}=1\) mean that the horizontal edge \((i,j)\to(i,j+1)\) points to the right, and \(v_{ij}=1\) mean that the vertical edge \((i,j)\to(i+1,j)\) points down. Values \(0\) indicate the opposite arrow. The Eulerian constraint at every vertex is precisely

\[
h_{ij}+v_{ij}=h_{i,j-1}+v_{i-1,j}.\]

The allowed move reverses the four boundary edges of the square with upper-left vertex \((i,j)\), and only when they form a coherently directed cycle. Equivalently, the ordered bit tuple

\[
(h_{ij},v_{i,j+1},h_{i+1,j},v_{ij})
\]

must be either \((1,1,0,0)\) or \((0,0,1,1)\); the move complements those four bits. Both senses of a directed cycle are allowed, and no simultaneous multi-face update or winding-cycle reversal is allowed. Define the two fluxes by

\[
a=\sum_{i=0}^3h_{i0},\qquad b=\sum_{j=0}^3v_{0j}.\]

Summing the Eulerian conditions around a row or column proves that these are independent of the chosen cut and preserved by every move.

## Proof

**Exhaustive state space.** A complete row-transfer enumeration uses four-bit words for incoming vertical arrows, a row's horizontal arrows, and outgoing vertical arrows. For each of the \(16^3\) triples of words retain precisely those satisfying the four vertex equations. Chain four admissible transitions, requiring the final outgoing word to equal the initial incoming word. This enumerates all Eulerian arrow assignments, without duplication or omissions, and yields exactly \(2970\) labelled orientations. `verify_transfer.py` implements precisely these equations and loops. A separate construction, `verify_vertex_constraints.cpp`, assigns the 32 edge bits by depth-first branching, propagating the two-out-of-four constraints at all 16 vertices; it independently yields the same 2970 states.

**Complete adjacency and distances.** For every enumerated state, inspect all sixteen elementary squares and complement the four bits exactly for the two directed boundary patterns stated above. Looking up each resulting state produces a symmetric, simple graph with \(8768\) edges. Breadth-first search identifies the \(69\) components and then, independently from every root in each nontrivial component, determines all shortest-path distances and eccentricities. Both supplied implementations perform this enumeration and every all-source breadth-first search independently; assertions check the component-size multiset, flux sectors, eccentricity counts, and the two central metric centers. The result is an exhaustive finite proof because every one of the \(2970\) possible states and every one of the sixteen possible transitions from it is considered.

**Frozen boundary.** If \(a=0\) or \(a=4\), cut conservation forces all horizontal arrows to have one common direction, while the vertical arrows have a freely chosen uniform direction in each of four columns: \(16\) states for either extreme value of \(a\). Similarly either extreme value of \(b\) gives \(16\) configurations, with uniform vertical direction and independent horizontal row directions. These four families have four overlap states in total, leaving \(4\cdot16-4=60\) distinct configurations. No elementary square is directed in any of them. Exhaustive enumeration confirms that these are all isolated states, and that each of the nine interior flux sectors is connected.

**Sharp lower bound for twelve moves.** Encode each horizontal row and vertical row by its four-bit integer. Consider the two central-flux orientations

\[
\begin{aligned}
(h_0,h_1,h_2,h_3)&=(0,0,15,15), & (v_0,v_1,v_2,v_3)&=(3,3,3,3),\\
(h'_0,h'_1,h'_2,h'_3)&=(15,15,0,0), & (v'_0,v'_1,v'_2,v'_3)&=(6,6,6,6).
\end{aligned}
\]

Write \(\Delta h=h'-h\) and \(\Delta v=v'-v\) bitwise as integer differences. The integer face-height potential, unique up to an additive constant, satisfies \(\Delta h_{ij}=\phi_{i-1,j}-\phi_{ij}\) and \(\Delta v_{ij}=\phi_{ij}-\phi_{i,j-1}\). For this pair it can be taken to be

\[
\phi=\begin{pmatrix}
0&0&1&1\\
-1&-1&0&0\\
0&0&1&1\\
1&1&2&2
\end{pmatrix}.
\]

Each permitted face reversal changes precisely one coordinate of this height function by one unit. Therefore any path between these endpoints has length at least \(\min_{c\in\mathbb Z}\sum_{i,j}|\phi_{ij}+c|=12\). The following twelve zero-based face coordinates give a legal path attaining the bound:

`(1,1), (0,1), (1,0), (0,0), (1,2), (1,3), (2,1), (1,1), (2,0), (1,0), (3,3), (3,2)`.

Sequential legality and the endpoint are checked directly by the provided code. The all-source computations show that no pair in any mobile sector is farther than twelve moves, completing the sharp diameter proof.

**Centers.** The two central metric centers are given by row-word tuples \(h=(5,10,5,10),v=(10,5,10,5)\) and their complement \(h=(10,5,10,5),v=(5,10,5,10)\). In both configurations every one of the sixteen faces is directed. The all-source enumeration proves that only these two states have eccentricity eight in the central component. Conversely, solving the directed-face pattern equations around adjacent faces forces the alternating checkerboard bits, so these are the only states with sixteen available elementary flips.

## Verification

Run `python3 verify_transfer.py` using Python 3 standard library. Independently compile and execute `g++ -std=c++17 -O2 verify_vertex_constraints.cpp -o check && ./check`. The programs construct the configurations by different algorithms (row transfer and propagating 32 individual arrow bits), independently create the face-move graph, calculate all connected components and all-source distances, and verify the reported numerical classifications. The Python program additionally verifies the explicit twelve-face path and both central metric centers. They are deterministic and require no input datasets. The complete pairwise central distance histogram comprises \(\binom{990}{2}=489555\) unordered pairs. A separate exploratory consistency check compared the height-potential lower bound with every shortest-path distance in every mobile component; this additional check is not needed to establish the enumerated assertions.

## Relationship to prior work

The exact number \(2970\) of four-by-four periodic square-ice states is previously known, including in OEIS A054759; it is **not** a new enumeration. Lieb's 1967 solutions concern equilibrium six-vertex counts and entropy. Felsner's planar alpha-orientation lattice theory studies directed cycle flips and gives a general structural framework, but does not tabulate this toroidal finite metric. Borodin and Bufetov study a toroidal six-vertex Markov process with particle moves that are not confined to reversing a single elementary directed square. Zhang and Qian give general surface-graph homology, facial-flip reachability criteria, and an explicit minimum-count formula for **directional** facial flips, but do not evaluate this finite graph’s undirected one-face radius, eccentricities, or all-pairs distance table. Those works and the general concept of flux are prior knowledge; the present contribution is the fully specified flux-component sizes, radii, sharp diameters, central metric centers, and distance distribution under the strict single-square move.

## Limitations

This theorem concerns a specific finite, labelled toroidal graph and a strict move rule. It does not prove analogous exact diameters at other torus sizes or for other Monte Carlo dynamics, nor does it claim a new general height-function or homology-connectivity theorem. Exact numbers depend on distinguishing the two directions of every graph edge and on keeping labelled positions (no symmetry quotient). A finite exhaustive certificate with two independent implementations establishes the stated values, but independent scholarly review has not been performed. Historical completeness cannot be guaranteed for older or unindexed finite-model computations.

## References

1. E. H. Lieb, “Exact Solution of the Problem of the Entropy of Two-Dimensional Ice,” *Physical Review Letters* **18** (1967), 692–694; DOI: 10.1103/PhysRevLett.18.692 (published 24 April 1967).
2. E. H. Lieb, “Residual Entropy of Square Ice,” *Physical Review* **162** (1967), 162–172; DOI: 10.1103/PhysRev.162.162.
3. S. Felsner, “Lattice Structures from Planar Graphs,” *Electronic Journal of Combinatorics* **11** (2004), R15; DOI: 10.37236/1768.
4. A. Borodin and A. Bufetov, “An irreversible local Markov chain that preserves the six vertex model on a torus,” arXiv:1509.05070 (2015).
5. W. Zhang and J. Qian, “Flips on homologous orientations of surface graphs with prescribed forbidden facial circuits,” arXiv:2011.07481 (2020).
6. OEIS A054759, numbers of square-ice configurations on periodic square grids; the fourth value is 2970.
