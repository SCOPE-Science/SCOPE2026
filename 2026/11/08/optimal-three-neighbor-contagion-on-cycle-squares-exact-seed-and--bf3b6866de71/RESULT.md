# Optimal three-neighbor contagion on cycle squares: exact seed and completion-time census

## Finding
Let \(C_n^2\) be the square of the simple \(n\)-cycle, with vertex set \(\mathbb Z/n\mathbb Z\) and distinct vertices adjacent when their cyclic distance is one or two. Assume \(n\ge5\). Initially activate a set \(A\); at each synchronous integer round activate every inactive vertex having at least three active neighbors. Write \(T(A)\) for the first round at which all vertices are active, and \(T(A)=\infty\) if that never happens.

**Theorem.** Put \(k=\lfloor n/3\rfloor\). The least cardinality of a contagious set is
\[
\mu(n)=\left\lceil\frac{n+2}{3}\right\rceil.
\]
The complete count \(N_{n,t}\) of labeled contagious sets of cardinality \(\mu(n)\) that first finish at round \(t\) is:

* If \(n=3k\), \(k\ge2\), then \(N_{n,k}=nk\), and all other counts vanish.
* If \(n=3k+1\), \(k\ge2\), then \(N_{n,k}=n\), and all other counts vanish.
* If \(n=3k+2\), \(k\ge1\), then \(N_{n,k}=n(k^2+k+2)/2\). For integer \(\lceil k/2\rceil\le t<k\), \(N_{n,t}=n/2\) when \(2t=k\), and \(N_{n,t}=n\) otherwise. All other counts vanish.

In particular, the number of cardinality-minimum contagious sets is respectively \(nk\), \(n\), and \(n(k+1)^2/2\) in the three residue classes. In the third class the earliest completion round among size-optimal sets is \(\lceil k/2\rceil\), and the latest is \(k\); the other two classes have the unique completion time \(k\).

## Assumptions and scope
The graph is finite, simple, undirected, and labeled by cyclic residues. For \(n=5\), the graph is \(K_5\), so each vertex has exactly four distinct neighbors, as it does for all \(n\ge5\). The activation rule is synchronous and irreversible; the initial configuration is round zero. Counts are of vertex subsets, not equivalence classes under rotation or reflection.

Let \(W=V\setminus A\) denote initially inactive vertices. Because the graph is four-regular and the activation threshold is three, a vertex in the remaining inactive set is activated precisely when it has at most one neighbor still inactive. Thus the successive inactive sets are exactly those obtained by **simultaneous leaf-and-isolate deletion** from the induced subgraph \(G[W]\). The process empties if and only if \(G[W]\) is a forest. For an induced path on \(\ell\) vertices, the last deletion occurs in round \(\lceil\ell/2\rceil\), and disconnected paths are processed in parallel.

## Proof
**1. Cyclic-gap characterization.** Suppose \(|W|=m\ge3\) and enumerate its vertices cyclically as \(w_1,\dots,w_m\). Let \(g_i\) be the positive cyclic distance from \(w_i\) to \(w_{i+1}\), where the indices are cyclic, so \(\sum g_i=n\). A pair of successive selected white vertices is adjacent in \(C_n^2\) exactly when its gap equals one or two. If two successive gaps are both one, their three vertices induce a triangle. If every gap is at most two, the white vertices contain a cycle using the successive edges. Conversely, if no two successive gaps are one and some gap is at least three, all white edges are precisely successive-gap edges and these form disjoint paths. Indeed an edge spanning two or more successive gaps would require a pair of adjacent unit gaps. Therefore \(G[W]\) is a forest exactly when (i) there are no cyclically adjacent unit gaps and (ii) at least one gap is at least three. The case \(m=2\), needed at \(n=5\), has an edgeless graph or single edge and is always a forest, compatible with the two relevant gap words \((1,4)\) and \((2,3)\).

**2. Maximum forest size.** Write \(u\) for the number of unit gaps. Under the conditions above, \(u\le\lfloor m/2\rfloor\). Every other gap is at least two, and at least one such gap is at least three. Hence
\[
n\ge u+2(m-u)+1=2m-u+1\ge2m-\lfloor m/2\rfloor+1.
\]
Consequently \(m\le\lfloor2(n-1)/3\rfloor\). The gap words constructed below attain equality for all \(n\ge5\) (and their exceptional two-vertex case works directly), so \(m_{\max}=\lfloor2(n-1)/3\rfloor\), giving \(\mu(n)=n-m_{\max}=\lceil(n+2)/3\rceil\).

**3. Classification by slack.** Write \(e=\sum_{g_i\ge2}(g_i-2)\). Then \(n=2m-u+e\), with \(e\ge1\). When \(n=3k\), \(m=2k-1\), the inequality in part 2 is tight: \(u=k-1\), \(e=1\). Thus precisely one gap is three, the remaining nonunit gaps are two, and the \(k-1\) unit gaps occupy distinct slots between the \(k\) nonunit gaps. Marking the unique three-gap at its initial labeled vertex gives \(n\) choices; of the \(k\) slots between nonunit gaps, exactly one is empty, giving \(k\) choices. Total \(nk\).

When \(n=3k+1\), \(m=2k\), tightness forces \(u=k\), \(e=1\); hence the \(k\) one-gaps alternate with \(k\) nonunit gaps, among which a unique one is three. Mark its starting vertex to obtain exactly \(n\) sets.

When \(n=3k+2\), \(m=2k\), the relation \(e-u=2-k\), together with \(u\le k\) and \(e\ge1\), leaves exactly three mutually disjoint families:

(A) \(u=k\), one gap four, all other nonunit gaps two, with alternating gap types: \(n\) sets.

(B) \(u=k\), two gaps three, all other nonunit gaps two, again alternating: the \(k-1\) possible nonzero separations of the two marked three-gaps, divided by two for interchanging those gaps, produce \(n(k-1)/2\) sets.

(C) \(u=k-1\), one gap three and \(k\) gaps two, with unit gaps in \(k-1\) of the \(k+1\) slots between nonunit gaps: \(n\binom{k+1}{2}=nk(k+1)/2\) sets.

Their total is \(n+n(k-1)/2+nk(k+1)/2=n(k+1)^2/2\). The argument counts labeled sets exactly once by singling out their three-gap/four-gap as appropriate; the two indistinguishable three-gaps in family (B) account for its factor two.

**4. Completion times.** Each gap at least three cuts the successive-white adjacency into paths; part 1 ensures no other edges. The unique long gap in every configuration of the first two congruence classes, and in families (A) and (C), leaves a single induced path with respectively \(2k-1\), \(2k\), or \(2k\) vertices. Its deletion time is \(k\). In (B), the two three-gaps delimit induced paths of even orders \(2r\) and \(2(k-r)\) for some \(1\le r\le k-1\). Its completion time is \(\max(r,k-r)\). For every \(t>k/2\) with \(t<k\), two complementary choices \(r=t\) and \(r=k-t\) contribute together \(n\) labeled sets; if \(k\) is even and \(t=k/2\), the symmetric separation contributes \(n/2\) sets. The number completing at \(k\) is precisely the sum of classes (A) and (C), \(n+nk(k+1)/2=n(k^2+k+2)/2\). This proves every stated count and the optimal-time interval.

The only two-white-vertex boundary \(n=5\) has exactly ten two-vertex complements and all finish after one round, agreeing with the formulas for \(k=1\).

## Verification
Two independent executable checks accompany this statement. `verification/verify_bruteforce.py` exhaustively enumerates all initial subsets and simulates the original synchronous infection rule for every \(5\le n\le18\), comparing the exact optimum and completion-time histogram. `verification/verify_gap_certificate.py` independently enumerates constrained cyclic compositions, tests induced acyclicity by a union-find check, and verifies the claimed count and time spectrum for every \(5\le n\le32\). Recorded outputs are included. Neither finite check is used as a substitute for the infinite-family proof above.

## Relationship to prior work
Guggiola and Semerjian [1, Sec. II.4] describe the threshold-model optimization and its equivalence to feedback vertex sets for degree-minus-one activation; they treat random regular graphs and do not give this exact optimal-state and completion-time census for squares of cycles. Macêdo Filho and collaborators [2] study graph powers of cycles but for biclique-coloring rather than contagious sets or induced forests. General decycling literature [3] and work on Cartesian products of cycles [4] provide related concepts and distinct graph families. Neither the scalar equivalence to decycling nor the underlying bootstrap-percolation dynamics is claimed as new.

## Limitations
The theorem concerns only the fixed four-regular family \(C_n^2\) and threshold exactly three, with simultaneous updating. The classification does not assert a formula for arbitrary cycle powers, nonsynchronous update order, larger thresholds, or random regular graphs. The historical-priority comparison is based on identified accessible literature and mathematical-record searches and does not rule out unindexed or inaccessible older treatments of exactly the same cyclic word enumeration. No independent scholarly audit has been performed.

## References
[1] A. Guggiola and G. Semerjian, *Minimal contagious sets in random regular graphs*, arXiv:1407.7361 (first posted 28 July 2014); full accessible text at https://arxiv.org/html/1407.7361v2 .

[2] H. B. Macêdo Filho, S. Dantas, R. C. S. Machado, and C. M. H. de Figueiredo, *Biclique-colouring verification complexity and biclique-colouring power graphs*, arXiv:1203.2543 (first posted 12 March 2012); full text at https://arxiv.org/html/1203.2543v2 .

[3] L. W. Beineke and R. C. Vandell, *Decycling graphs*, Journal of Graph Theory 25 (1997), 59–77; https://doi.org/10.1002/(SICI)1097-0118(199705)25:1%3C59::AID-JGT4%3E3.0.CO;2-H .

[4] D. A. Pike and Y. Zou, *Decycling Cartesian products of two cycles*, SIAM Journal on Discrete Mathematics 19 (2005); https://doi.org/10.1137/S089548010444016X .
