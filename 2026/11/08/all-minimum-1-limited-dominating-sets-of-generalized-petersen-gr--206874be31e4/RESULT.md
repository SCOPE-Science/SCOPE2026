# All minimum \(1\)-limited dominating sets of generalized Petersen graphs \(GP(n,2)\)

## Finding
For each integer \(n\ge5\), the generalized Petersen graph \(GP(n,2)\) has \(2n\) vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\), and three types of edges: \(u_i u_{i+1}\), \(v_i v_{i+2}\), and \(u_i v_i\). Its minimum \(1\)-limited domination number is
\[
\gamma_1^{\mathrm L}(GP(n,2))=n.
\]
The complete family of minimum sets has cardinality
\[
N_n=2+10\mathbf 1_{5\mid n}.
\]
There are always two constant-column minimum sets: all outer vertices and all inner vertices. If and only if \(5\mid n\), the remaining ten are the five cyclic shifts of each of two periodic column-mask words:
\[
(0,3,1,3,0),\qquad(0,3,3,0,2).
\]
Mask \(0\) means neither vertex of a column is chosen; \(1\) means only the outer vertex; \(2\) only the inner vertex; \(3\) both. Each word is repeated \(n/5\) times. The equivalent enumeration of **unordered** vertex bipartitions with a perfect matching as the entire cut is \(1+5\mathbf1_{5\mid n}\).

## Assumptions and scope
All graphs here are finite, undirected, simple, and have **labelled** columns \(i\in\mathbb Z/n\mathbb Z\). We require \(n\ge5\), so each vertex has degree three and the two step-two inner neighbours are distinct. A vertex set \(D\) is **\(1\)-limited dominating** when each vertex outside \(D\) has a neighbour in \(D\) and each vertex in \(D\) has at most one neighbour outside \(D\). Vertex sets, rather than equivalence classes under graph automorphisms, are counted. The indicator \(\mathbf1_{5\mid n}\) equals one when \(5\mid n\), and zero otherwise.

## Proof
**Cardinality and the equality condition.** Let \(D\) be any \(1\)-limited dominating set. Counting edges from \(D\) to its complement gives
\[
2n-|D|\le |E(D,V\setminus D)|\le |D|.
\]
The lower bound holds because each vertex outside \(D\) is dominated, and the upper bound holds because each vertex of \(D\) has at most one crossing edge. Thus \(|D|\ge n\). Both complete shores attain \(n\): every vertex has exactly one crossing neighbour, through its spoke. At equality \(|D|=n\), every vertex on **both** sides has exactly one crossing edge. Therefore the cut edges form a perfect matching; conversely, a vertex bipartition whose cut edges form a perfect matching gives two size-\(n\), \(1\)-limited dominating sets.

**Column-state constraints.** Encode the selection of \(u_i,v_i\) by a mask \(c_i\in\{0,1,2,3\}\). Put \(b_j(c)\in\{0,1\}\) for bit \(j\) of mask \(c\), where bit zero is the outer vertex. Write \([P]\) for one when proposition \(P\) is true and zero otherwise. Exactly one crossing neighbour at each vertex is equivalent, for all \(i\) modulo \(n\), to
\[
[b_0(c_{i-1})\ne b_0(c_i)]+[b_0(c_{i+1})\ne b_0(c_i)]+[b_1(c_i)\ne b_0(c_i)]=1,
\]
\[
[b_1(c_{i-2})\ne b_1(c_i)]+[b_1(c_{i+2})\ne b_1(c_i)]+[b_0(c_i)\ne b_1(c_i)]=1.
\]
These constraints involve five consecutive columns, so no local state outside the next paragraph can affect feasibility.

**A finite universal transition certificate.** Form a directed graph with all \(4^4=256\) vertices \((a,b,c,d)\in\{0,1,2,3\}^4\). There is an arrow \((a,b,c,d)\to(b,c,d,e)\), for \(e\in\{0,1,2,3\}\), if the preceding two constraints hold at the central column \(c\) for the five-tuple \((a,b,c,d,e)\). A complete strongly connected component enumeration, with all \(256\) states included, finds exactly four components containing a directed cycle:

- The loop at \((1,1,1,1)\).
- The loop at \((2,2,2,2)\).
- The directed five-cycle on \((0,3,1,3),(3,1,3,0),(1,3,0,0),(3,0,0,3),(0,0,3,1)\).
- The directed five-cycle on \((0,3,3,0),(3,3,0,2),(3,0,2,0),(0,2,0,3),(2,0,3,3)\).

In every listed component, each state has exactly one successor and exactly one predecessor **within that component**. This enumeration is a finite exhaustive lemma, not a numerical extrapolation; the complete generating and verifying procedure is in `artifacts/verify.py`. It explicitly constructs every state and all its valid transitions, runs Tarjan's strongly connected component algorithm, compares every cyclic component with the four sets above, and checks their internal in/out degrees.

**From finite states to every cycle length.** Every cyclic sequence of \(n\) masks satisfying the two local constraints is a closed walk of length \(n\) in this state graph, and conversely, because overlapping length-four windows determine the same cyclic sequence. Every closed walk is contained in one strongly connected component. The four cyclic components identified above therefore allow only the two constant words or a repetition of one of the two five-letter words. The latter requires \(5\mid n\); each directed five-cycle has five distinct initial states, giving five distinct labelled assignments, even when repeated. The two word orbits are disjoint. This yields exactly \(N_n=2+10\mathbf1_{5\mid n}\) minimum dominating sets. Taking complements pairs minimum sets without fixed points, so dividing by two gives the number of unordered perfect-matching cuts. \(\square\)

## Verification
Execute the self-contained standard-library script as `python3 artifacts/verify.py` after extracting this package. It enumerates **all** \(256\) transition states; checks all four cyclic strongly connected components and their internal degree-one structure; independently enumerates all \(n\)-element vertex subsets for \(5\le n\le10\); and verifies all proposed periodic assignments through \(n=150\). The exact finite-state component enumeration is also the exhaustively checked nonstandard lemma used by the general mathematical proof. Direct vertex-subset tests are finite corroboration, not substitutes for the general closed-walk argument.

## Relationship to prior work
Radić and Tepeh (2026, arXiv:2610.01796v1) establish complexity results for \(1\)-limited domination on cubic graphs and exact values on Goldberg snarks, not the complete minimum-set census for \(GP(n,2)\). Radić, Radić, and Tepeh (2026, arXiv:2610.26259v1) prove structural cut-decomposition results for cubic graphs, including the general equality/perfect-matching correspondence, and examine generalized Blanuša and flower snarks; that general correspondence **is prior knowledge** and is used as a starting point, not claimed new. Tepeh (2026, arXiv:2606.22428v1) treats Cartesian products, not the step-two inner edges here. Beggas et al. (2019, arXiv:1906.11966v1) treat **\([1,2]\)-domination**, a distinct restriction on vertices **outside** the chosen set, rather than \((1,2)\)-domination and \(1\)-limited domination. General perfect-matching-cut complexity research does not supply this exact all-length multiplicity theorem. The specific two-orbit, period-five classification is the new claim; historical priority is provisional.

## Limitations
The result concerns \(GP(n,2)\) with \(n\ge5\), not the general \(GP(n,k)\) family nor nonminimum dominating sets. Counting is of labelled vertex subsets. The exhaustive state computation is finite and fully reproducible, but mathematical independent audit has not been performed; unindexed prior matching-cut literature remains a novelty risk. The claim does not assert an independently certified proof.

## References
1. G. Radić and A. Tepeh, *On 1-limited and (1,2)-domination in cubic graphs*, arXiv:2610.01796v1, submitted 2026-10-01, https://arxiv.org/abs/2610.01796.
2. G. Radić, G. Radić, and A. Tepeh, *Structural aspects of 1-limited domination in cubic graphs*, arXiv:2610.26259v1, submitted 2026-10-19, https://arxiv.org/abs/2610.26259.
3. A. Tepeh, *On k-limited domination: complexity and Cartesian products*, arXiv:2606.22428v1, submitted 2026-06-21, https://arxiv.org/abs/2606.22428.
4. F. Beggas, V. Turau, M. Haddad, and H. Kheddouci, *[1,2]-Domination in Generalized Petersen Graphs*, arXiv:1906.11966v1, submitted 2019-06-27, https://arxiv.org/abs/1906.11966.
5. R. Erveš and A. Tepeh, *Induced cycles vertex number and (1,2)-domination in cubic graphs*, Applied Mathematics and Computation 510 (2026), Article 129700, DOI:10.1016/j.amc.2025.129700.
6. M. Bouquet and C. Picouleau, *The complexity of the perfect matching-cut problem*, Journal of Graph Theory (2024), DOI:10.1002/jgt.23167.
