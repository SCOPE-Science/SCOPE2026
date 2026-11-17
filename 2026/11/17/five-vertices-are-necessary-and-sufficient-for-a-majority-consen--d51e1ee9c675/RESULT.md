# Five vertices are necessary and sufficient for a majority-consensus gain–loss paradox

## Finding

Let \(G=(V,E)\) be a finite connected simple graph, with a binary state at each vertex. At each synchronous update, a vertex adopts the strict majority of its **open neighbors** and retains its current state when tied. Let \(\mathcal B(G)\) be the set of all labelled initial states whose trajectories eventually reach either unanimous state. For an edge \(e\) with \(G-e\) still connected, call the deletion **gain–loss** if
\[
|\mathcal B(G-e)|>|\mathcal B(G)|\quad\text{and}\quad
\mathcal B(G)\not\subseteq\mathcal B(G-e).
\]
The smallest order of a graph admitting a gain–loss deletion is **five**. At that order there are exactly two marked-edge graph types, up to vertex relabelling. With vertices \(0,1,2,3,4\), representatives are:

* **Diamond with a leaf:** \(E=\{01,02,03,04,12,13\}\), with edge \(12\) deleted. The consensus basin increases from \(26\) to \(30\), although precisely two old consensus-attracted states leave the basin; six states enter.
* **House:** \(E=\{01,03,04,12,23,34\}\), with edge \(04\) deleted. The consensus basin increases from \(22\) to \(24\), although precisely two old consensus-attracted states leave; four states enter.

Here each two-digit edge \(ij\) means \(\{i,j\}\). Exactly \(240\) labelled pairs \((G,e)\) of order five have this property: \(120\) in each class. **Aggregate attraction and pointwise preservation are different:** one edge can enlarge the consensus basin while preventing consensus from some initial states that previously reached it.

## Assumptions and scope

The graph is connected both before and after deleting exactly one edge (so a bridge is never deleted). All graphs are loopless, undirected and unweighted. Every vertex updates simultaneously; a tie retains the vertex's current bit. Both unanimous states are absorbing on every such graph. The consensus basin includes initial unanimous configurations. A labelled state on \(n\) vertices is encoded by \(s=\sum_{v=0}^{n-1}s_v2^v\). The theorem is a minimum-order and complete minimum-order classification; it makes no claim that all larger graphs have gain–loss edges.

## Proof

**1. Exact finite dynamical test.** For a graph with adjacency sets \(N(v)\), define
\[
T_G(s)_v=\begin{cases}
1,&2\sum_{u\in N(v)}s_u>|N(v)|,\\
0,&2\sum_{u\in N(v)}s_u<|N(v)|,\\
s_v,&2\sum_{u\in N(v)}s_u=|N(v)|.
\end{cases}
\]
Make the functional directed graph \(s\to T_G(s)\) on all \(2^n\) binary words. Its consensus basin is **exactly** the reverse-reachable set from the two absorbing unanimous states. This follows because reaching either unanimous state is equivalent to having a forward path to one of them. The algorithm `verify_all_labelled.cpp` constructs this reverse-reachable set with a queue and integer bit masks, without any assumption about other periodic orbits.

**2. Exhaustion of all smaller orders.** For each integer \(2\le n\le5\), encode all simple labelled graphs by the \(\binom n2\) possible edge bits, enumerate all \(2^{\binom n2}\) masks, keep only connected graphs, and test every present edge whose deletion preserves connectivity. For each test, construct both exact consensus basins and evaluate the two gain–loss inequalities. At orders \(2,3,4,5\), the numbers of connected labelled graphs are respectively \(1,4,38,728\); the numbers of eligible labelled marked-edge deletions are \(0,3,84,3140\); and the numbers satisfying gain–loss are \(0,0,0,240\). At order one there are no edges.

For a compact hand-checkable boundary, the **entire list of nonbridge edge types through order four** is:

| Graph and deleted edge type | Old basin | New basin | States lost | States gained |
| --- | ---: | ---: | ---: | ---: |
| Triangle, any edge | 8 | 6 | 2 | 0 |
| Four-cycle, any edge | 10 | 12 | 0 | 2 |
| Triangle plus a leaf, triangle edge incident to leaf's neighbor | 16 | 12 | 4 | 0 |
| Triangle plus a leaf, opposite triangle edge | 16 | 8 | 8 | 0 |
| Diamond (two triangles sharing edge), shared edge | 10 | 10 | 0 | 0 |
| Diamond, nonshared triangle edge | 10 | 16 | 0 | 6 |
| Four-clique, any edge | 10 | 10 | 0 | 0 |

All other connected graphs through four vertices are trees and have no eligible edge deletion. In none of these seven cases is there both a strict basin gain and a loss of an old member.

**3. Complete order-five classification.** The exact enumeration returns \(240\) labelled marked pairs. For each such pair, apply all \(5!\) vertex permutations simultaneously to the graph and its marked deleted edge and choose the lexicographically least encoded pair. Exactly two canonical pairs result. Both have \(120\) labelled realizations and are isomorphic to the two representatives stated above. The second checker, `verify_independent.py`, independently traces trajectories from **all** initial configurations for each graph, then uses this permutation minimization; it reproduces the same two canonical pairs, counts and basin values. Thus both minimum order and exclusivity of the two types follow by exhaustive finite proofs.

**4. Explicit witnesses for both directions.** For the diamond-with-leaf representative, initial state \(10\) follows \(10\to8\to0\) in the original graph but is fixed at \(10\) after deletion. Conversely state \(3\) belongs to the original two-cycle \(3\leftrightarrow28\), but in the modified graph follows \(3\to30\to11\to31\). For the house representative, state \(3\) follows \(3\to2\to0\) before deletion but becomes fixed at \(3\) afterward; state \(7\) belongs to the original two-cycle \(7\leftrightarrow14\) but follows \(7\to15\to31\) afterward. Here \(0\) and \(31\) are unanimous states. These trajectories explicitly demonstrate strict inclusion failures and nonempty basin gains, separately from the complete count certificates.

## Verification

From the directory containing the supplied files, run `g++ -std=c++17 -O2 verify_all_labelled.cpp -o verify_all_labelled && ./verify_all_labelled` and `python3 verify_independent.py`. The recorded successful outputs are supplied as `labelled_output.txt` and `independent_output.txt`. The C++ checker enumerates all labelled graphs and obtains consensus basins by reverse breadth-first search. The Python checker independently iterates each state until it reaches unanimity or repeats and uses all vertex permutations to classify marked graph pairs. The programs do not invoke a graph-atlas database or random sampling. Both were executed and their outputs compared with the present claims.

## Relationship to prior work

Mustafa and Pekeč (BRICS RS-00-8, May 2000) studied synchronous local majority and proved that the global property of correctly computing the **initial majority** is nonmonotone under edge addition or deletion. Their property is not the setwise attraction to **either** consensus, and their result does not yield the stronger combination of an increased total basin with the loss of particular previously attracted states or its sharp five-vertex classification. Their observation about nonmonotonicity is fully credited.

Benjamini, Chan, O'Donnell, Tamuz and Tan (arXiv:1405.2486, 2014) discuss majority consensus and the classical eventual period-at-most-two property for finite graphs; their main results concern infinite unimodular and random graphs, not edge-perturbed finite basin comparisons. Fountoulakis, Kang and Makai (2020) prove rapid consensus for dense random graphs rather than exact tiny-graph perturbations. A published complete-bipartite one-edge defect census supplies formulas only for \(K_{a,b}\) with one cross edge deleted; neither five-vertex exceptional graph is bipartite. The present result therefore does not follow from that family. The previously documented Heawood two-edge consensus-attraction loss also does not imply the sharp one-edge minimum across all connected graphs.

## Limitations

The claim is an exact classification **only at minimum order**, not an asymptotic frequency theorem or a classification of higher-order graphs. Connectivity after deletion is essential to the stated minimum-order question. All counts pertain to synchronous tie-retaining open-neighbor majority; asynchronous updates and random ties are different models. No independent external audit has been conducted. Although relevant primary works and mathematical records were compared, an unindexed historical enumeration could still overlap the result.

## References

1. N. H. Mustafa and A. Pekeč, *Democratic Consensus and the Local Majority Rule*, BRICS Report Series RS-00-8 (May 2000). Full-text public rendering: https://paperzz.com/doc/7886945/democratic-consensus-and-the-local-majority-rule .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, Unanimity and Disagreement in Majority Dynamics on Unimodular Graphs and Random Graphs*, arXiv:1405.2486v1, first publicly posted 2014-05-11: https://arxiv.org/pdf/1405.2486 .
3. N. Fountoulakis, M. Kang and T. Makai, *Resolution of a conjecture on majority dynamics: Rapid stabilization in dense random graphs*, *Random Structures & Algorithms* (2020), DOI:10.1002/rsa.20970, first published 2020-10-13.
4. *A one-edge majority defect has three exact basin responses*, public mathematical record `4c37e2b972d1` (2026), complete-bipartite family: https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-a-one-edge-majority-defect-has-three-exact-basin-responses--4c37e2b972d1/RESULT.md .
