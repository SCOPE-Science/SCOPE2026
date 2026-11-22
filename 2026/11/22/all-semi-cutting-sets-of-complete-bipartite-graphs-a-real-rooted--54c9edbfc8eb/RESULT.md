# All semi-cutting sets of complete bipartite graphs: a real-rooted census and sharp terminal rigidity

## Finding
Let \(G=K_{a,b}\) be a finite, labelled, simple complete bipartite graph, with shores \(A,B\) of sizes \(a,b\ge1\). Fix terminals \(T\subseteq A\cup B\) with \(x=|T\cap A|\), \(y=|T\cap B|\), and \(2\le x+y\le a+b\). An edge set \(F\subseteq E(G)\) is *semi-cutting* for \(T\) when deletion of \(F\) strictly increases the distance between every two distinct terminals, allowing infinity after deletion. Let
\[
P_{a,b;x,y}(z)=\sum_{F\text{ semi-cutting for }T}z^{|F|},
\qquad H_0(z)=1,\quad H_k(z)=z^{k-1}(z+k)\quad(k\ge1).
\]
Then the exact cardinality polynomial is
\[
\boxed{P_{a,b;x,y}(z)=z^{xy}H_x(z)^{b-y}H_y(z)^{a-x}(1+z)^{(a-x)(b-y)}.}
\]
Its zeros are all real and nonpositive. All inclusion-minimal semi-cutting sets have the same cardinality
\[
\boxed{\tau_{a,b}(x,y)=xy+(b-y)\max\{x-1,0\}+(a-x)\max\{y-1,0\},}
\]
and their exact number is \(c_x^{b-y}c_y^{a-x}\), where \(c_0=1\) and \(c_k=k\) for \(k\ge1\). Minimum semi-cutting sets are connected under single-edge exchanges (remove one deleted edge, insert one different edge).

This gives a precise equality classification for the general lower bound \(|F|\ge |T|-1\): **if \(a,b\ge2\), equality is achievable if and only if \(x=y=1\)**. If either shore has size one (a star, including a single edge), equality is achievable for **every** terminal set of size at least two. Thus non-star complete bipartite graphs attain the universal bound only for two terminals on opposite shores.

The coefficient sequence of \(P_{a,b;x,y}\), restricted to its nonzero support, is log-concave and unimodal. For instance, for \(K_{3,4}\) with \(x=2\) and \(y=1\),
\[
P_{3,4;2,1}(z)=z^2\bigl[z(z+2)\bigr]^3(z+1)^4,
\qquad \tau_{3,4}(2,1)=5,
\]
and precisely \(2^3=8\) minimum semi-cutting sets exist.

## Assumptions and scope
Graphs are finite, labelled, undirected, simple, unweighted, and connected. The shores and terminal subset are fixed, and all selected edge sets \(F\) are counted separately; graph automorphism classes are not used. The distance after deletion may be infinite. The semi-cutting property concerns *all* shortest paths between *every* terminal pair, not only globally maximal shortest paths or complete separation. The stated domain is \(a,b\ge1\), \(0\le x\le a\), \(0\le y\le b\), and \(x+y\ge2\). Empty exponents and products have their usual meanings. Single-edge exchange means a symmetric difference of size two between two minimum sets.

## Proof
**1. Exhaustive shortest-terminal-path constraints.** Fix \(T_A=T\cap A\), \(T_B=T\cap B\), \(A_0=A\setminus T\), and \(B_0=B\setminus T\). Every terminal pair across shores is adjacent, so its unique shortest path is its edge. Hence **all \(xy\) edges of \(T_A\times T_B\) are forced into \(F\)**. Every pair of terminals inside \(A\) is at distance two, with one shortest path through each vertex \(v\in B\). It follows that for each \(v\in B\), at most one edge between \(v\) and \(T_A\) may be *undeleted*. The analogous condition holds for each \(u\in A\) and its edges to \(T_B\). Conversely, these conditions hit every shortest terminal-terminal path: the cross-shore length-one paths and all same-shore length-two paths exhaust the possibilities. This equivalence follows directly by considering which shortest paths survive deletion; no assumption about connectivity after deletion is used.

**2. Independent four-block classification.** The edge blocks are \(T_A\times T_B\), \(T_A\times B_0\), \(A_0\times T_B\), and \(A_0\times B_0\). The first block is forced selected. In each column indexed by \(v\in B_0\), at least \(x-1\) of the \(x\) edges to \(T_A\) must be selected when \(x\ge1\): either all \(x\) are selected or exactly one of the \(x\) is unselected. The local polynomial is \(z^x+xz^{x-1}=H_x(z)\). If \(x=0\), there are no such edges and the local polynomial is \(H_0(z)=1\). Symmetrically, each row indexed by \(u\in A_0\) contributes \(H_y(z)\). No edge in \(A_0\times B_0\) lies on any shortest path with terminal endpoints, so those edges can be selected arbitrarily and independently, contributing \((1+z)^{(a-x)(b-y)}\). Multiplication proves the displayed polynomial and is a bijective enumeration of every semi-cutting set.

**3. Minimality and exact optimum count.** In each local block with \(x\ge1\) and \(v\in B_0\), inclusion-minimality requires selecting exactly \(x-1\) edges, leaving exactly one undeleted: if all \(x\) were selected, removing any one selected edge would preserve the condition. Conversely, removing one more edge when exactly one is already undeleted violates the condition for a same-shore terminal pair when \(x\ge2\); for \(x=1\) no edge is selected at the minimum. Symmetrically for \(A_0\times T_B\). Every edge in \(A_0\times B_0\) must be left undeleted in an inclusion-minimal \(F\). The forced \(xy\) terminal-to-terminal edges remain selected. Hence inclusion-minimal and minimum-cardinality semi-cutting sets coincide, proving \(\tau_{a,b}(x,y)\). Each \(B_0\)-vertex has \(c_x\) choices and each \(A_0\)-vertex has \(c_y\) choices of its single undeleted incident terminal edge, proving the count. These choices form a Cartesian product of complete choice graphs, so the optimum single-edge-exchange graph is connected.

**4. Root and coefficient law.** For \(k\ge1\), \(H_k(z)=z^{k-1}(z+k)\) has zeros only at zero and \(-k\); \(H_0=1\). Every factor in the polynomial therefore has only real nonpositive zeros. Product closure proves real-rootedness. Newton's inequalities (or convolution of nonnegative log-concave binomial sequences) give log-concavity, and the polynomial product gives contiguous nonzero support; therefore the nonzero coefficients are unimodal.

**5. Rigidity of the universal bound.** If \(a,b\ge2\) and \(x,y\ge1\), subtracting \(x+y-1\) from the exact minimum gives
\[
\tau_{a,b}(x,y)-(x+y-1)=(x-1)(y-1)+(b-y)(x-1)+(a-x)(y-1).
\]
Each term is nonnegative. For equality, if \(x>1\) then the first two terms can both vanish only when \(y=1\) and \(b=y=1\), impossible since \(b\ge2\). Thus \(x=1\), and the last term then forces \(y=1\) since \(a-x\ge1\). Conversely \(x=y=1\) gives \(\tau=1=x+y-1\). If \(y=0\) and \(x\ge2\), the minimum is \(b(x-1)\), strictly larger than \(x-1\) for \(b\ge2\); similarly when \(x=0\). If \(a=1\), either \(x=1\) and \(\tau=y=x+y-1\), or \(x=0\) and \(\tau=y-1=x+y-1\); the case \(b=1\) is symmetric. Thus the equality classification holds in all boundaries.

## Verification
`verify_semicut.py` uses graph-wide breadth-first searches to recompute all pairwise terminal distances after every edge-deletion subset, independently of the product derivation. It checks the entire polynomial for 92 parameter profiles with at most ten edges. It additionally checks formula-defined minima and the universal lower bound for 92 larger parameter profiles (including \(K_{4,7}\)). The observed output after `python3 verify_semicut.py` is:
```
INDEPENDENT_TERMINAL_PAIR_BFS_AND_POLYNOMIAL_PASS cases= 92
EXTREMAL_POLYNOMIAL_AND_BOUND_PASS cases= 92
VERIFY_OK
```
The unrestricted proof is the explicit shortest-path and block argument above; finite tests are corroborating, not an infinite certificate.

## Relationship to prior work
Bosek, Serra and Vena, *Structural properties of semi-cutting sets* (arXiv:2611.20287v1, first public 15 November 2026), proved the universal lower bound \(|F|\ge |T|-1\), gave the terminal-geodesic equivalence, and explicitly proposed the equality-case characterization and structure of minimum semi-cutting sets as further directions. Their full paper has no all-set bipartite enumeration or equality-case classification for the natural complete-bipartite family. The present result resolves those two questions for all complete bipartite graphs and all placements of terminals. Earlier general shortest-path disruption and multiterminal-cut problems have distinct constraints: increasing each terminal distance does not require disconnecting terminals. Related published graph invariants dealing with vertex-geodesic transversals and edge-geodesic *covers* do not imply the present edge-deletion enumerator.

## Limitations
This is a classification for complete bipartite graphs, not an equality characterization for general graphs. It counts unweighted simple-graph edge deletion sets and does not establish analogous factorization under arbitrary edge weights or missing biclique edges. Originality was checked against the complete motivating article, targeted indexed research, and accessible previous statements; some indexed related items were available in summary form only, and earlier terminology may hide an equivalent prior classification. Independent mathematical audit has not been performed.

## References
1. B. Bosek, O. Serra and L. Vena, *Structural properties of semi-cutting sets*, arXiv:2611.20287v1, first submitted 15 November 2026, https://arxiv.org/abs/2611.20287 .
2. E. Dahlhaus, D. S. Johnson, C. H. Papadimitriou, P. D. Seymour and M. Yannakakis, *The complexity of multi-terminal cuts*, SIAM Journal on Computing 23 (1994), 864–894 (distinct separation problem; see reference [4] in [1]).
3. *All geodesic transversals of complete multipartite graphs*, indexed published mathematical record, 12 October 2026 (vertex-based shortest-path parameter, not terminal-edge deletion).
