# Sharp parallel stabilization of right-Euclidean closure on finite frames

## Finding
For a nonempty finite set \(X\) of size \(n\), let \(R_0\subseteq X\times X\) and form the simultaneous right-Euclidean consequence sequence
\[
 R_{t+1}=R_t\cup\{(y,z):\exists x\;(x,y)\in R_t\ \land\ (x,z)\in R_t\}.
\]
Let \(\tau(R_0)\) be the smallest \(t\geq0\) such that \(R_t=R_{t+1}\). The sharp maximum over all relations on \(n\) vertices is
\[
 \max_{R_0}\tau(R_0)=\begin{cases}
 0,&n=1,\\1,&n=2,\\2+\lceil\log_2(n-2)\rceil,&n\geq3.
 \end{cases}
\]
In addition, after two rounds all nontrivial dynamics are ordinary graph squaring: on the original set of relation targets, \(R_2\) is reflexive and symmetric, and \(R_{2+s}\) connects exactly those vertices at \(R_2\)-graph distance at most \(2^s\) (including each component separately). Rows belonging to original non-targets never change.

## Assumptions and scope
The carrier is nonempty, finite, and labelled only to write matrices. Self-loops are permitted in the initial relation; the right-Euclidean rule is precisely \(xRy\land xRz\Rightarrow yRz\), with \(y=z\) included. All updates add simultaneously consequences of the preceding full relation, not newly inferred edges within the same round. Graph distance refers to the undirected graph of \(R_2\) restricted to \(T=\{y:\exists x\ xR_0y\}\). Different components have infinite distance. The theorem concerns the least right-Euclidean superrelation of \(R_0\), not transitive closure or asynchronous rule firing.

## Proof
**Target invariant and symmetrization.** An added pair \((y,z)\) requires an incoming edge to \(y\), so its first coordinate lies in \(T\). Also each added target already lies in \(T\), hence rows outside \(T\) are unchanged and no edge can ever point outside \(T\) unless it already did (which contradicts the definition of \(T\)). Every \(y\in T\) gains \((y,y)\) in the first round, using any original incoming edge. If \(yR_1z\) and \(y\in T\), the loop \(yR_1y\) adds \(zR_2y\); pairs added via common targets in round two appear together with their converses. Thus \(R_2|_T\) is reflexive and symmetric. For every \(t\ge2\), \(R_t|_T\) remains reflexive symmetric, so \(R_{t+1}|_T\) is its union with its Boolean square. Induction proves that \(R_{2+s}\) connects precisely the pairs whose distance in the \(R_2\) graph is at most \(2^s\). In particular the eventual restriction to each component is the complete reflexive relation.

**A sharp diameter lemma.** For \(n\ge3\), every connected component of the graph of \(R_2|_T\) has diameter at most \(n-2\). This is immediate if \(|T|<n\), or if all components have at most \(n-1\) vertices. Suppose instead \(T=X\) and a component has diameter \(n-1\). Its graph must be a spanning simple path \(v_1,\ldots,v_n\): a diametral shortest path already occupies all vertices, so any extra edge is a shortening chord.

Every \(R_0\) edge must then be either a loop or an edge between neighboring path vertices. All stages preserve connected components of the undirected graph underlying \(R_0\), because new edges join two vertices that already have a common predecessor and hence an undirected \(R_0\)-walk (inductively). Since \(R_2\) is connected, every path adjacency must occur in at least one orientation in \(R_0\). Moreover each row of \(R_1\) contains its own loop; it cannot contain two distinct off-diagonal targets \(v_{i-1},v_{i+1}\), because the next update would add the forbidden chord \(v_{i-1}R_2v_{i+1}\). Thus every vertex has at most one non-loop outgoing edge even in \(R_1\).

The oriented non-loop edges of \(R_0\) cover a path with outdegree at most one, and therefore have an endpoint with no non-loop incoming edge: otherwise starting with the arrow \(v_2\to v_1\) at one endpoint forces the arrows \(v_3\to v_2,\ldots,v_n\to v_{n-1}\), leaving the other endpoint without incoming edges. Reversing the path, take this endpoint to be \(v_1\). Since \(T=X\), \(v_1\) must have an \(R_0\) self-loop. Its path edge must be \(v_1\to v_2\), so round one adds \(v_2\to v_1\). Because \(v_2\) has at most one non-loop successor in \(R_1\), the next edge must be \(v_3\to v_2\) in \(R_0\). Repetition forces \(v_{i+1}\to v_i\) for every \(i\ge2\). Then \(v_n\) has no non-loop predecessor and must have an \(R_0\) self-loop. It follows that \(v_{n-1}\to v_n\) lies in \(R_1\), while \(v_{n-1}\to v_{n-2}\) already lies in \(R_0\) when \(n\ge4\); when \(n=3\), \(v_2\to v_1\) lies in \(R_1\). In either case \(R_1\) has two distinct non-loop successors at one vertex, a contradiction. Therefore diameter \(n-1\) is impossible, proving the lemma.

**Uniform upper bound.** Every finite connected graph of diameter at most \(n-2\) becomes a disjoint union of complete components after at most \(\lceil\log_2(n-2)\rceil\) Boolean squaring rounds. The previous normal form gives the asserted upper bound for \(n\ge3\). For \(n=1\), every possible relation is already Euclidean; direct inspection of the four relations on a two-vertex set gives maximum one round.

**Sharpness.** On vertices \(v_1,\ldots,v_n\), take precisely \(v_iR_0v_{i+1}\) for \(1\le i<n\), with no loops. Here \(T=\{v_2,\ldots,v_n\}\), \(R_1\) adds exactly the loops on \(T\), and \(R_2|_T\) is the reflexive undirected path on its \(n-1\) vertices. Its diameter is exactly \(n-2\); the edge between its endpoints first appears after \(\lceil\log_2(n-2)\rceil\) further rounds. This proves the lower bound for every \(n\ge3\). For \(n=2\), the relation containing only \(v_1R_0v_2\) needs one round to add \(v_2R_1v_2\).

## Verification
The standalone Python 3 program `verify.py` independently implements the rule by a triple loop, checks each of the \(2^{n^2}\) relations for \(1\le n\le4\), tests the exact sharp path construction for \(3\le n\le64\), and checks 1,600 reproducibly seeded random relations of orders five through twelve. For sampled and exhaustive relations, it also checks target invariance, symmetry at round two, and the graph-distance power characterization. The verified output is `VERIFY_OK 67728` (66,066 exhaustive cases, 62 path cases, and 1,600 randomized cases). Exhaustive testing is finite corroboration, not the proof for unbounded \(n\).

## Relationship to prior work
Right-Euclidean relations are standard modal frame conditions. Magnus Boman's September 2026 catalogue studies entailments, independence and relation-algebraic translations for fifteen properties of binary relations, rather than the number of synchronous completion rounds; its available abstract does not settle this particular comparison. The OEIS entry A398718 provides a labelled census and an exponential generating function for *already* right-Euclidean relations; this is a static enumeration problem and does not imply a dynamic round count. Standard references on transitive closure analyze the different inference rule \(xRy\land yRz\Rightarrow xRz\). The sharp right-Euclidean completion-time formula above is a distinct, finite structural question. Exact historical priority is not independently certified.

## Limitations
Only finite nonempty single binary relations and simultaneous right-Euclidean augmentation are covered. Asynchronous update policies may require different step counts. The theorem is not a new decision procedure for modal satisfiability and claims no complexity improvement for arbitrary first-order frame theories. An inaccessible full text of the motivating 2026 catalogue leaves residual priority uncertainty despite comparison to its published abstract and to complete accessible enumeration/closure references.

## References
1. Magnus Boman, *A Catalogue of Properties of Binary Relations: Entailments, Incompatibilities, and Independence Results*, arXiv:2609.13317, first publicly available 2026-09-10, https://arxiv.org/abs/2609.13317.
2. Vladeta Jovovic, *Number of right-Euclidean relations on an n-element labeled set*, OEIS A398718, https://oeis.org/A398718, 2026-09-05.
3. Al Doerr and Kenneth Levasseur, *Applied Discrete Structures*, Section 6.5, “Closure Operations on Relations,” https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Applied_Discrete_Structures_%28Doerr_and_Levasseur%29/06%3A_Relations/6.05%3A_Closure_Operations_on_Relations.
