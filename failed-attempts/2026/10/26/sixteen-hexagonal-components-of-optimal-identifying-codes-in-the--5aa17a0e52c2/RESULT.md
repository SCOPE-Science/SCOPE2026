# Sixteen hexagonal components of optimal identifying codes in the Shrikhande graph

## Finding
Let \(S\) be the Shrikhande graph on \(V=\mathbb Z_4^2\), with vertices \(x,y\) adjacent precisely when \(y-x\) belongs to \(\{(\pm1,0),(0,\pm1),(1,1),(-1,-1)\}\). An identifying code is a subset \(C\subseteq V\) for which the sixteen intersections \(N[v]\cap C\), as \(v\) ranges over \(V\), are **nonempty and pairwise distinct**. The minimum identifying-code size is five.

Set \(H=2\mathbb Z_4^2\), and for \(x\in V\) put \(B_x=(x+H)\setminus\{x\}\). Every minimum identifying code, **uniquely**, has the form
\[
C=B_x\cup\{a,b\},\quad x\in V,\quad a,b\in N(x),\quad a\sim b.
\]
The six neighbors of each \(x\) induce a six-cycle, so there are exactly six choices of adjacent \(\{a,b\}\) for each of the sixteen choices of \(x\), and precisely \(96\) minimum identifying codes in total.

In the exchange graph, join two minimum codes exactly when their symmetric difference contains two vertices (a single selected vertex is replaced). The exchange graph is isomorphic to the disjoint union \(16C_6\): it has \(96\) vertices, \(96\) edges and sixteen six-vertex components. The unique parameter \(x\) is invariant under every single-vertex optimum-preserving exchange, and all six codes with fixed \(x\) lie in one cycle.

## Assumptions and scope
The vertices are the sixteen ordered pairs of residues modulo four, and the graph is the simple undirected Cayley graph given above. \(N(v)\) denotes the **open** six-vertex neighborhood and \(N[v]=N(v)\cup\{v\}\) its **closed** seven-vertex neighborhood. An identifying code requires both coverage (nonempty trace) and separation (distinct traces), including for vertices not in the code. The exchange move is unrestricted single-token replacement, not a token slide. All counts concern labeled subsets of this fixed sixteen-vertex graph; no claim is made for other strongly regular graphs.

## Proof
**Lower bound.** For a code of size \(k\), the sixteen identifying traces are sixteen distinct nonempty subsets of a set of size \(k\); thus \(2^k-1\ge16\), ruling out \(k\le4\).

**Finite classification with an explicit exhaustive certificate.** A subset \(C\) is identifying if and only if it intersects each of the sixteen sets \(N[v]\), and each of the \(\binom{16}{2}=120\) symmetric differences \(N[u]\mathbin{\triangle}N[v]\) for \(u\ne v\). The first sixteen constraints express coverage; the remaining 120 express trace separation. These are exactly 136 finite hitting constraints. The included `verify_structural.py` implements the constraints as sixteen-bit masks using the displayed Cayley differences, iterates **all** \(\binom{16}{4}=1820\) four-subsets and **all** \(\binom{16}{5}=4368\) five-subsets, and asserts that no four-subset and precisely 96 five-subsets meet them. It independently constructs the specified sixteen families \(B_x\cup\{a,b\}\), verifies every proposed code satisfies every constraint, verifies each family has six distinct codes, and checks that the union of these families is exactly the full set of 96 qualifying five-subsets. Therefore the classification is exhaustive, including uniqueness of the parameter \(x\); it is not a sampled enumeration.

**Exchange structure.** For any fixed \(x\), all six codes share the three-vertex core \(B_x\). Two such codes are one-replacement neighbors exactly when their chosen edges of the six-cycle \(S[N(x)]\) share one endpoint. The line graph of this six-cycle is again \(C_6\). The independently implemented exhaustive exchange check constructs all ordered pairs of the 96 minimum codes with symmetric difference of size two, and verifies that every such pair has the same parameter \(x\). No cross-family edges exist; hence the graph is \(16C_6\). In particular, each of its vertices has degree two and each component has exactly six edges.

For a concrete witness, encoding \((a,b)\) by \(4a+b\), the root \(x=(0,0)\) has core indexed by \(\{2,8,10\}\). The code indexed by \(\{2,4,5,8,10\}\) is identifying; all six codes at this root are listed in the structural verification output. Root translations carry this structure to every \(x\).

**Independent cross-check.** The included `verify_exhaustive.py` takes a separate route: it computes all sixteen traces for every candidate five-set and tests their nonemptiness and distinctness directly, rather than using the symmetric-difference hitting constraints. It then compares the resulting set with the template family and constructs the exchange graph from pairwise symmetric differences. The two implementations produce the same cardinality and component census.

## Verification
With Python 3 and no third-party dependencies, run `python3 verify_exhaustive.py` and `python3 verify_structural.py` in the directory holding the four standalone verification artifacts. Their expected successful markers are `CHECK_EXHAUSTIVE_OK` and `CHECK_STRUCTURAL_OK`, respectively. The corresponding complete stdout files `exhaustive_output.txt` and `structural_output.txt` are embedded alongside this result. The programs assert the counts before printing the markers, verify all sixteen families, and reconstruct the complete exchange adjacency relation. The exhaustive first program also confirms, only as a previously known contrast, that the four-by-four rook graph has minimum identifying-code size six.

## Relationship to prior work
Gravier, Moncel and Semri (2008) determine the identifying-code number of Cartesian products of equal-sized cliques; specializing their theorem gives six for the \(4\times4\) rook graph, which is cospectral with the Shrikhande graph but is a different graph. This previously established rook bound is not claimed as new. Gravier, Parreau, Rottey, Storme and Vandomme (2015) study identifying codes in vertex-transitive and strongly regular graphs, including general bounds; their accessible author manuscript does not state this full Shrikhande minimum-code classification or its single-replacement exchange graph. Previously published mathematical records about Shrikhande independence complexes and minimum resolving sets concern different invariants: independent faces or metric distance signatures are not the nonempty closed-neighborhood signatures in this theorem. The complete six-cycle exchange decomposition is therefore not obtained by changing terminology in those statements.

## Limitations
This is an exhaustive finite classification for one specified graph, not an infinite-family theorem. Its reproducibility depends on the clearly specified finite constraint enumeration and the included runnable source code, not an independently audited formal certificate. Publication-priority uncertainty persists: alternate terminology (locating-dominating variants, minimum identifying sets, sensor-code swaps) may hide a covering earlier result, and one plausibly related online item about the Shrikhande graph was not available as a full text. The self-review is not independent validation.

## References
1. S. Gravier, J. Moncel and A. Semri, *Identifying Codes of Cartesian Product of Two Cliques of the Same Size*, Electronic Journal of Combinatorics **15** (2008), N4; publicly dated 2008-02-11. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v15i1n4 .
2. S. Gravier, A. Parreau, S. Rottey, L. Storme and E. Vandomme, *Identifying Codes in Vertex-Transitive Graphs and Strongly Regular Graphs*, Electronic Journal of Combinatorics **22** (2015), P4.6; open manuscript https://orbi.uliege.be/bitstream/2268/186885/1/identifying_codes_arXiv.pdf .
3. Public mathematical-record index: independence-complex comparison of Shrikhande and the four-by-four rook graph, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187 (different invariant).
