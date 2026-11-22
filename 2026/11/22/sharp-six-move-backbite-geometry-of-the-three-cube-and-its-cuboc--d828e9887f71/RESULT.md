# Sharp six-move backbite geometry of the three-cube and its cuboctahedral decycling dual

## Finding
Let \(Q_3\) be the binary three-cube, with vertices \(0,\ldots,7\) (three-bit integers) and an edge between vertices differing in exactly one bit. Its line graph \(C=L(Q_3)\) is the cuboctahedral graph. Define a *feedback vertex set* of \(C\) to be a subset \(S\) for which \(C-S\) contains no cycle. The minimum such sets have cardinality five and number 72. With a token slide meaning replacement of one member of \(S\) by an adjacent unselected vertex of \(C\), the reconfiguration graph of minimum feedback sets is a connected, four-regular graph on 72 vertices, with 144 edges and radius and diameter both **six**. Every vertex has eccentricity six, although its local distance histogram depends on which of three 24-element symmetry orbits it belongs to. The associated unrestricted one-token-jump graph adds 120 edges but has the **same 144 diametral pairs**, hence the same diameter six and radius six.

The full ordered distance-shell vectors (distance zero through six) under a slide, one for each 24-element orbit, are
\[
(1,4,11,17,21,13,5),\qquad(1,4,12,18,24,10,3),\qquad(1,4,11,17,16,19,4).
\]
The sorted coordinate-direction multiplicities of the corresponding Hamiltonian paths are respectively \((1,2,4)\), \((2,2,3)\), and \((1,3,3)\). Their endpoint Hamming distances are respectively one, one, and three.

The slide and jump unordered-pair distance distributions are:

| Distance | Slides | Jumps |
| --- | ---: | ---: |
| 1 | 144 | 264 |
| 2 | 408 | 408 |
| 3 | 624 | 576 |
| 4 | 732 | 684 |
| 5 | 504 | 480 |
| 6 | 144 | 144 |

## Assumptions and scope
All graphs are finite, simple, and labelled as stated. Identify the twelve vertices of \(C\) with the twelve unordered edges of \(Q_3\). Adjacency in \(C\) means that the corresponding cube edges have an endpoint in common. A token slide exchanges exactly one deleted cube edge with one undeleted cube edge adjacent in \(C\), preserving both the deletion count and acyclicity of the remaining induced subgraph. A token jump removes the adjacency restriction. Hamiltonian paths are identified with their reversals. Distances refer to shortest legal sequences in the specified reconfiguration graph; no asymptotic or higher-dimensional assertion is made.

## Proof
**Step 1: Optimal feedback sets correspond to Hamiltonian paths.** For any set \(F\) of cube edges, the induced subgraph of \(C\) on \(F\) is a forest if and only if the spanning subgraph \((V(Q_3),F)\) is a disjoint union of paths and isolated vertices. Indeed, any original vertex incident with three selected edges induces a triangle in the line graph. If every degree is at most two, every component of the selected cube-edge subgraph is a path or a cycle; a cycle in the original yields a cycle in the line graph, and a path yields a path. Since a linear forest on eight vertices has at most seven edges, every feedback set deletes at least \(12-7=5\) vertices of \(C\). The explicit cube walk \((0,1,3,2,6,7,5,4)\) uses seven edges, so equality is attained. A seven-edge linear forest on all eight cube vertices must be connected, and is therefore precisely a Hamiltonian path. Thus the correspondence is exact in both directions.

**Step 2: Slides are backbites.** Let \(P=(v_0,\ldots,v_7)\) be a Hamiltonian path. To exchange a path edge for a new cube edge while retaining a Hamiltonian path, the added edge must touch a path endpoint: otherwise the added edge increases the degrees of two internal vertices to three, and deleting only one old edge cannot restore both degrees. If it joins an endpoint to an internal vertex, one old path edge must be removed to break the newly created cycle: this is the endpoint backbite operation. If it joins both endpoints, the added edge closes a Hamiltonian cycle, and deleting a cycle edge incident with an old endpoint yields a backbite; deleting another edge is a token jump but not a slide. Therefore adjacency-restricted exchanges in \(C\) are exactly backbites. At each endpoint of a cube Hamiltonian path, two of its three cube incident edges are unused (the third belongs to the path). This gives two distinct backbites per endpoint, yielding four slide neighbors.

**Step 3: Finite exhaustive classification and metric.** The two included standalone checkers provide independent exhaustive proofs. `verify_line_graph.py` enumerates the \(\binom{12}{5}=792\) candidate five-deletions, certifies acyclicity of their induced complements by disjoint-set union on the 24 line-graph edges, and rejects every potential four-deletion by testing all \(\binom{12}{8}=495\) eight-edge survivors. It builds both legal adjacency lists by direct symmetric-difference-one-edge exchange, and performs breadth-first search from each of the 72 optimal sets. `verify_hamilton_paths.py` independently enumerates all spanning vertex paths by depth-first search in \(Q_3\), identifies reversals, generates backbites from endpoint/path positions, constructs all one-edge exchanges from shared edge sets, and independently performs the 72 breadth-first searches. All reported counts, distance shells and degree classes agree.

For symmetry, the verifier explicitly generates the \(3!2^3=48\) cube automorphisms (coordinate permutations followed by bit translations), and computes three disjoint orbits of size 24. The three coordinate-multiplicity patterns in the Finding section distinguish these orbits. Their exact six-step distance shells listed above prove both connectivity and the sharp upper and lower bound six for *each* configuration. The jump graph has 48 paths whose endpoints are adjacent in the cube and 24 whose endpoints are at Hamming distance three. Only the first type admits five additional one-edge exchanges obtained by closing the Hamiltonian cycle and deleting a non-end edge. Hence the jump graph has \(144+48\cdot5/2=264\) edges, with the stated degree distribution. The second breadth-first calculation gives 144 distance-six unordered pairs in the jump graph, the same as in the slide graph. Since a jump graph contains every slide edge, the set of distance-six pairs in the jump graph is contained in the slide graph's distance-six pairs, and equality of cardinalities forces *the very same 144 pairs*.

An explicit sharpness witness, encoded as vertex orders, is the path pair \((0,1,3,2,6,4,5,7)\) and \((0,2,3,1,5,4,6,7)\). Exhaustive BFS shows their slide distance is six. This is a finite statement: the exhaustive enumeration covers **all** Hamiltonian paths of this eight-vertex graph, not sampled states.

## Verification
Run either source checker using Python 3.10 or later, from a directory containing the unpacked package:

```sh
python3 verify_line_graph.py
python3 verify_hamilton_paths.py
```

The scripts use only the standard library. `VERIFIER_OUTPUT.txt` records the exact outputs of their successful execution; the scripts and independently reconstructed inputs, rather than the output text alone, are the certificate. Check `VERIFICATION.md` for the full scope of these checks.

## Relationship to prior work
The endpoint *backbite* move itself is classical; it is not claimed as a new operation. Oberdorf–Ferguson–Jacobsen–Kondev (arXiv:cond-mat/0508094, first publicly posted 2005-08-03) describe its use to sample compact Hamiltonian lattice walks and give a small **two-dimensional** square-grid transition example, rather than the exact three-cube reconfiguration metric. Kinney–Hickman–Anandakrishnan–Garner (2020) independently enumerate **144 oriented** Hamiltonian paths in the \(2\times2\times2\) cube, corresponding to the 72 unoriented paths here; this path count is **not new**. Their complete article uses these paths as building blocks in large-lattice polymer sampling, without giving the complete 72-state backbite/jump distance graphs. Kazazi (arXiv:2610.05068, 2026) studies backbite connectivity in general graphs; its main sufficient condition of a spanning squared Hamiltonian path cannot apply to the triangle-free \(Q_3\), and it does not compute the metric of this case. The new assertion is the sharp local 72-state metric, orbit-resolved shells, and unchanged 144 diameter pairs despite adding 120 unrestricted exchange edges; the line-graph feedback-set interpretation is an exact reformulation, not a second independent discovery.

## Limitations
This result is only for \(Q_3\) and its line graph, not all hypercubes, grids or polyhedral graphs. The 72-path count and backbite operation are already known. The metric and orbit conclusions are established by independently reproducible finite exhaustion, not a general symbolic formula. There may be unindexed earlier work giving an equivalent transition-graph analysis, particularly in early compact-polymer literature; the original 1982 Mansfield paper was not inspected in full. There has been no independent scholarly audit.

## References
- R. Oberdorf, A. Ferguson, J. L. Jacobsen and J. Kondev, *Secondary Structures in Long Compact Polymers* (2005 preprint; published 2006), https://arxiv.org/abs/cond-mat/0508094 .
- N. Kinney, M. Hickman, R. Anandakrishnan and H. R. Garner, *Crossing complexity of space-filling curves reveals entanglement of S-phase DNA* (2020), https://doi.org/10.1371/journal.pone.0238322 .
- A. Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths* (2026), https://arxiv.org/abs/2610.05068 .
- M. Takaoka, *Complexity of Hamiltonian Cycle Reconfiguration* (2018), https://www.mdpi.com/1999-4893/11/9/140 .
