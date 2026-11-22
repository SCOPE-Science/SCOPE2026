# Two-vertex fault tolerance of antipodal hypercube geodesic rerouting

## Finding
Let \(n\ge4\) and let \(F\) be any set of at most two internal vertices of the Boolean hypercube \(Q_n\). Among all length-\(n\) paths from \(0^n\) to \(1^n\) avoiding \(F\), join two paths if they differ at exactly one internal vertex. **The resulting reconfiguration graph is nonempty and connected.**

The dimension threshold is sharp: in \(Q_3\), forbidding the vertex with support \(\{0\}\) and the vertex with support \(\{1,2\}\) leaves exactly two length-three antipodal geodesics, and neither can be rerouted to the other by changing only one intermediate vertex.

Equivalently, for \(n\ge4\), deleting at most two arbitrary nonempty proper subsets from the Boolean lattice leaves its maximal chains connected under diamond exchanges. Equivalently again, the induced adjacent-transposition graph on permutations whose proper initial segments avoid both forbidden subsets is connected.

## Assumptions and scope
The vertices of \(Q_n\) are the subsets of \([n]=\{0,\ldots,n-1\}\), with adjacent subsets having symmetric difference of size one. The endpoints are the empty set and all of \([n]\), and faults must exclude these endpoints. A shortest antipodal path has exactly \(n\) edges and corresponds bijectively to a permutation \(\pi=(\pi_1,\ldots,\pi_n)\), whose internal vertices are the prefix sets \(\{\pi_1,\ldots,\pi_j\}\) for \(1\le j<n\). Two such paths differ at one internal vertex if and only if the permutations differ by swapping one adjacent pair. No claim is made about arbitrary pairs of non-antipodal endpoints, more than two faults, or shortest-path diameter after faults.

## Proof
**Step 1: the four-dimensional base.** Relabeling coordinates sends an unordered pair of distinct internal forbidden subsets \((A,B)\) to a unique type indexed by \((k,l,t)=(|A|,|B|,|A\cap B|)\), with \(k\le l\). All ten realizable types for \(n=4\) are listed below. The number of valid permutations, the number of legal adjacent swaps, and the number of connected components follow by exhaustive, reproducible enumeration of all 24 permutations, their three neighbors, and the prefix-avoidance predicate; the permutation verifier checks all numerical entries, while an independent direct-path verifier confirms connectivity for every labelled fault pair.

| \((k,l,t)\) | Valid paths | Legal exchanges | Components |
|---|---:|---:|---:|
| \((1,1,0)\) | 12 | 14 | 1 |
| \((1,2,0)\) | 14 | 16 | 1 |
| \((1,2,1)\) | 16 | 21 | 1 |
| \((1,3,0)\) | 12 | 12 | 1 |
| \((1,3,1)\) | 14 | 17 | 1 |
| \((2,2,0)\) | 16 | 20 | 1 |
| \((2,2,1)\) | 16 | 21 | 1 |
| \((2,3,1)\) | 14 | 16 | 1 |
| \((2,3,2)\) | 16 | 21 | 1 |
| \((3,3,2)\) | 12 | 14 | 1 |

The same direct finite check establishes connectedness for zero or one forbidden internal vertex in \(Q_4\). This settles the induction base for all fault sets with cardinality at most two.

**Step 2: connected first-letter fibers.** Suppose the claim is established in dimension \(n-1\), with \(n\ge5\), and fix \(F\) with \(|F|\le2\). Partition permitted permutations by their first coordinate \(s\). A fiber is impossible precisely when the singleton \(\{s\}\) is forbidden. Otherwise a forbidden subset \(U\) containing \(s\) becomes the forbidden set \(U\setminus\{s\}\) of the remaining \(n-1\) coordinates, which is nonempty and proper; a forbidden subset not containing \(s\) can never occur after the initial \(s\). Thus each allowable first-letter fiber is isomorphic to a fault-avoiding shortest-path graph in \(Q_{n-1}\) with at most two internal faults. By induction it is nonempty and connected.

**Step 3: bridges between first-letter fibers.** Let \(s,t\) be distinct allowable first coordinates. We construct a legal edge between the fibers whenever \(\{s,t\}\notin F\). Seek a permutation starting \((s,t)\) such that its remaining order \(R\) avoids all forbidden prefix sets, and swap the first two letters to obtain \((t,s,R)\). The first singleton prefixes are allowed by choice; the two-element prefix is common and allowed by assumption. A forbidden subset \(U\) can obstruct the suffix only if \(\{s,t\}\subsetneq U\subsetneq[n]\). For such a set of size \(q\), exactly a fraction
\[
\binom{n-2}{q-2}^{-1}\le\frac1{n-2}
\]
of the \((n-2)!\) orders \(R\) encounter it as a prefix after \(s,t\). Since there are at most two forbidden sets, the union bound excludes a fraction at most \(2/(n-2)<1\) for \(n\ge5\). Thus some suffix is valid for both paths, yielding the required reconfiguration edge.

**Step 4: first-letter connectivity.** Remove from the complete graph on the \(n\) first-letter labels the vertices \(s\) for which \(\{s\}\in F\), and remove edges \(\{s,t\}\) for which that two-element set lies in \(F\). If \(r\) singleton faults occur, the remaining graph has \(n-r\) vertices and at most \(2-r\) edges removed. It is connected for \(n\ge5\): when \(r=0\), deleting at most two edges from \(K_n\) cannot disconnect it; when \(r=1\), deleting at most one edge from \(K_{n-1}\) cannot disconnect it; and when \(r=2\), the graph is \(K_{n-2}\). Each vertex represents one connected nonempty fiber by Step 2, and each surviving edge has a bridge by Step 3. Their union is connected. The induction is complete.

**Sharpness.** For \(n=3\), take \(A=\{0\}\) and \(B=\{1,2\}\). The only surviving permutations are \((1,0,2)\) and \((2,0,1)\); these differ at both internal vertices, so no one-vertex rerouting step joins them. The remaining permutation graph has two isolated vertices.

## Verification
Execute `python3 verify_permutations.py` to enumerate every distinct unordered two-fault pattern up to coordinate relabeling in dimensions three through eight and assert the complete ten-type base table. Execute `python3 verify_cube_paths.py` to generate the hypercube geodesics directly, construct adjacency by counting changed internal vertices, and test every zero-, one-, and two-fault subset in dimensions two through six. Both programs are standalone Python standard-library computations. Their outputs and run limits are recorded in `VERIFICATION.md`. The finite computations certify the dimension-four base and provide consistency checks above it. They do **not** substitute for the induction proving the infinitely many larger dimensions.

## Relationship to prior work
The permutation–geodesic correspondence and adjacent-transposition move model are established in Proposition 27 of Asplund–Edoh–Haas–Hristova–Novick–Werner (2017) and Observation 2 / Theorem 5 of Gajjar–Jha–Kumar–Lahiri (first public 2021). The latter gives an optimal sorting algorithm in the fault-free hypercube. These results do not by themselves establish that *all* valid shortest paths remain mutually reachable after two arbitrary internal-vertex failures; the new theorem proves that additional fault-resilience property by a first-letter induction. Existing one-fault conclusions are strictly weaker, because connectivity after removing one fault does not logically imply connectivity under two simultaneous faults.

## Limitations
The guarantee concerns existence of an optimum-length antipodal route and connectedness under single-intermediate-vertex rerouting, not a sharp bound on the number of rerouting moves. The exact base table is computationally exhaustive, with source code supplied; the induction argument is the all-dimensional component. The literature comparison cannot rule out an equivalent theorem in an unindexed or inaccessible source. No independent external mathematical audit has been performed.

## References
1. K. Gajjar, A. V. Jha, M. Kumar, A. Lahiri, *Reconfiguring Shortest Paths in Graphs*, arXiv:2112.07499, first posted 2021-12-14; open-access journal version, *Algorithmica* 86 (2024), 3309–3338. https://arxiv.org/abs/2112.07499 ; https://doi.org/10.1007/s00453-024-01263-y
2. J. Asplund, K. Edoh, R. Haas, Y. Hristova, B. Novick, B. Werner, *Reconfiguration graphs of shortest paths*, arXiv:1705.09385 (2017), Proposition 27. https://arxiv.org/abs/1705.09385
3. P. Bonsma, *The complexity of rerouting shortest paths*, *Theoretical Computer Science* 510 (2013), 1–12. https://doi.org/10.1016/j.tcs.2013.09.012
