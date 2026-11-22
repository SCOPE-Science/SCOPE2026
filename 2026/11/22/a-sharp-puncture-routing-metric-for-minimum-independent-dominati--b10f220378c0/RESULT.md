# A sharp puncture-routing metric for minimum independent domination on helm graphs

## Finding
For every integer \(n\ge3\), let \(H_n\) be the helm graph obtained from the wheel on a rim cycle \(C_n\) by adjoining one pendant vertex to each of its \(n\) rim vertices. Consider minimum-cardinality independent dominating sets, with a move replacing one chosen vertex by an adjacent unchosen vertex while retaining minimum independent domination. Every optimum has exactly \(n\) vertices, and its reconfiguration graph is the Lucas cube of independent subsets of \(C_n\), with the empty subset deleted.

At \(n=3\) this graph is \(3K_1\); at \(n=4\) it is \(2P_3\). For every \(n\ge5\) it is connected, and every pair \(S,T\) of its vertices, encoded as nonempty independent vertex subsets of \(C_n\), has the exact distance
\[
d(S,T)=|S\mathbin\triangle T|+2\varepsilon(S,T),
\qquad
\varepsilon(S,T)=
\begin{cases}
1,&S\cap T=\varnothing\text{ and every vertex of }S\text{ is adjacent to every vertex of }T,\\
0,&\text{otherwise.}
\end{cases}
\]
Consequently precisely \(2n\) **unordered pairs** lose their shortest Hamming route when the empty state is removed. They are the \(n\) pairs of adjacent singleton sets and the \(n\) pairs \(\{v\},N_{C_n}(v)\). Each loses exactly two moves; all other distances remain Hamming-exact. The network has
\[
|V|=F_{n-1}+F_{n+1}-1,
\qquad |E|=n(F_{n-1}-1),
\]
where \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\).

Its exact radius and diameter are
\[
\operatorname{rad}=\begin{cases}5,&n=5\text{ or }n=7,\\4,&n=6,\\\lfloor n/2\rfloor+1,&n\ge8,\end{cases}
\qquad
\operatorname{diam}=\begin{cases}5,&n=5,\\n,&n\ge6\text{ even},\\n-1,&n\ge7\text{ odd}.\end{cases}
\]
The numbers of unordered diametral pairs are \(n\) for odd \(n\ge5\) and \(1\) for even \(n\ge6\). For even \(n\ge6\), the only diametral pair is the pair of alternating maximum independent sets; for odd \(n\ge7\), diametral pairs arise uniquely by omitting one rim vertex and alternately partitioning the remaining rim path.

## Assumptions and scope
Graphs are finite, undirected, simple and labelled. The rim vertices are \(v_i\), with cyclic indices in \(\mathbb Z/n\mathbb Z\), their leaves are \(u_i\), and the wheel hub is \(h\). An independent dominating set is an independent set whose closed neighborhoods cover every graph vertex. A valid slide replaces one selected vertex with one unselected neighbor, with the resulting set again a minimum independent dominating set. This is a **sequential one-token move** metric, not a parallel-swap or simultaneous-replacement metric. The result concerns the routing of optimal solutions, not the minimum domination number of arbitrary graphs.

## Proof
**1. Optimal configurations.** Every pendant vertex \(u_i\) can be dominated only by \(u_i\) or \(v_i\), so each independent dominating set contains at least one vertex from each of the \(n\) disjoint pairs \(\{u_i,v_i\}\). The set of all \(n\) pendants is independent but fails to dominate the hub. Selecting one rim vertex \(v_i\) and all pendants \(u_j\) with \(j\ne i\) gives an independent dominating set of size \(n\). Hence the optimum is \(n\) and selects exactly one from every pair; in particular the hub is not selected. Write \(S\) for the indices at which rim rather than pendant vertices are selected. Rim independence says \(S\) contains no consecutive cyclic indices, and domination of the hub says \(S\ne\varnothing\). Conversely these conditions guarantee every rim, leaf and the hub is dominated. A slide between optimum sets cannot change two different spoke pairs, and the only edge joining the vertices of the same pair is \(u_iv_i\). It therefore toggles exactly one coordinate of \(S\). This proves the claimed state-graph identification.

**2. Exact shortest paths.** Changing the membership of each element of \(S\triangle T\) is necessary, hence \(d(S,T)\ge|S\triangle T|\). If \(S\cap T\ne\varnothing\), remove the elements of \(S\setminus T\), then insert those of \(T\setminus S\); every state remains nonempty and independent, and exactly the Hamming number of moves occurs. If \(S\cap T=\varnothing\) but some \(a\in S\) and \(b\in T\) are nonadjacent, remove all of \(S\setminus\{a\}\), insert \(b\), remove \(a\), and then insert \(T\setminus\{b\}\). Again the route uses exactly \(|S\triangle T|\) moves.

Now suppose \(S,T\) are disjoint and all cross-pairs are adjacent. Any Hamming geodesic must remove all vertices of \(S\) before inserting any vertex of \(T\), and thus must visit the forbidden empty state. A route in a coordinate-toggle graph has length congruent to \(|S\triangle T|\) modulo two, so the distance is at least \(|S\triangle T|+2\). Because a cycle of length at least five contains no \(K_{2,2}\), every such pair has either \(S\) or \(T\) a singleton. Independence and the two neighbors of a vertex show that (up to swapping the ends) its only possibilities are adjacent singletons \(\{a\},\{b\}\), or \(\{a\},N(a)=\{a-1,a+1\}\). For adjacent singletons choose a rim vertex \(c\) adjacent to neither endpoint (this exists when \(n\ge5\)); then
\[
\{a\}\to\{a,c\}\to\{c\}\to\{b,c\}\to\{b\}
\]
is a legal four-move route. For \(\{a\}\) and \(\{a-1,a+1\}\), put \(c=a+2\) modulo \(n\) and use
\[
\{a\}\to\{a,c\}\to\{c\}\to\{a-1,c\}\to\{a-1\}\to\{a-1,a+1\}.
\]
All intermediate states are nonempty and independent for \(n\ge5\), including \(n=5\). The two lengths are \(2+2\) and \(3+2\), so both meet the lower bound. The exceptional sets listed are all distinct as unordered pairs for \(n\ge5\), proving the \(2n\) count.

**3. Counts.** Independent subsets of a path on \(m\) vertices are counted by \(F_{m+2}\). Conditioning on one vertex of a cycle gives \(F_{n-1}+F_{n+1}\) independent rim subsets, including the empty set. For each coordinate \(i\), the edges of the nonempty-subset flip graph that toggle it correspond to nonempty independent subsets of the residual path on \(n-3\) vertices after excluding \(i\) and its two neighbors. This gives \(F_{n-1}-1\) edges per coordinate and the claimed total.

**4. Eccentricities, radius and diameter.** Fix a nonempty independent set \(S\) with \(k\) elements. List its selected vertices cyclically, and let their positive cyclic spacings be \(g_1,\ldots,g_k\ge2\), with \(\sum_i g_i=n\); for \(k=1\), define \(g_1=n\). The complement \(C_n-S\) is the disjoint union of paths of lengths \(g_i-1\), so the largest independent subset disjoint from \(S\) has \(\sum_i\lfloor g_i/2\rfloor\) vertices. Therefore the maximum Hamming distance from \(S\) to another nonempty state is
\[
B(S)=k+\sum_{i=1}^k\lfloor g_i/2\rfloor.
\]
Only the exceptional pairs in Step 2 can exceed that baseline. Their distances are four for adjacent singletons and five for a singleton opposite its two neighbors. Thus \(\operatorname{ecc}(S)=\max\{B(S),5\}\) if \(S\) is a singleton or the two-neighbor set \(N(v)\), and \(\operatorname{ecc}(S)=B(S)\) for all other sets. This formula gives every eccentricity, not merely the radius. Writing \(o\) for the number of odd spacings gives \(B(S)=(n+2k-o)/2\), where \(o\le k\) and \(o\equiv n\pmod2\). In even lengths \(n\ge8\), this is at least \(n/2+1\) and a singleton attains the bound; the same argument applies in odd lengths \(n\ge9\) with \(\lfloor n/2\rfloor+1\). At \(n=5,6,7\), direct analysis of the allowed gaps and the exceptional singleton penalty gives radii \(5,4,5\), respectively: for \(n=6\), the opposite two-vertex set has eccentricity four.

For any two independent sets, at most \(n\) coordinates differ. When \(n\) is even, the two alternating sets differ in all \(n\) coordinates and are the unique complementary independent sets, giving the diameter \(n\). If \(n\) is odd, no two independent sets are complements; their Hamming distance is at most \(n-1\). If equality holds, the sets are disjoint, omit exactly one rim vertex, and are the unique alternating two-color classes of the remaining path, providing exactly \(n\) unordered pairs at distance \(n-1\). For \(n\ge7\), the exceptional pairs have distance at most five and cannot increase this diameter; they also cannot create additional diametral pairs at \(n=7\) because their maximum is five while \(n-1=6\). For \(n=6\), the maximum exceptional distance is five, below six. At \(n=5\), the exceptional singleton-to-two-neighbors pairs have distance five, and there are five of them, while all other pairs have distance at most four. For \(n=3,4\), the independent-set lists are respectively three singletons, and four singletons plus two opposite pairs, establishing the disconnected structures stated above.

## Verification
The standalone pure-Python program `check.py` performs two complementary finite tests. For \(3\le n\le8\) it constructs the original \(2n+1\)-vertex helm graph, enumerates independent dominating sets directly, and checks its optimum-state and actual edge-slide graph against the claimed representation. For \(5\le n\le13\) it builds each connected state graph, computes BFS shortest distances from every source state, and compares all ordered pairs to the explicit distance formula, including eccentricities, radius, diameter and antipodal-pair counts. The program also verifies state/edge counts. Run `python3 check.py` with Python 3.8 or later. These finite checks support, but do not substitute for, the all-size proof.

## Relationship to prior work
The general reconfiguration model of minimum independent dominating sets and the notion of \(i\)-graphs are established in Brewster, Mynhardt and Teshima (2023), *Reconfiguration of Minimum Independent Dominating Sets in Graphs*. Their subsequent *The \(i\)-Graphs of Paths and Cycles* treats original path and cycle graphs, not helm graphs. Munarini, Perelli Cippo and Zagaglia Salvi (2001) studied the **ordinary, unpunctured** Lucas cubes. Castro and Mollard (2012) established full-cube eccentricity distributions, and Azarija and collaborators (2015) established vertex/edge-connectivity for the full families. Those results supply the standard Lucas-cube language, but the present claim concerns the deletion of the all-zero state and the exact induced excess-routing metric, exceptional pairs, and helm-optimum interpretation. In particular, neither the ordinary Lucas cube's Hamming distances nor its diameter alone determines the puncture-induced detours and their \(2n\) exact count.

## Limitations
The metric applies only to optimum independent domination of the defined helm, with one adjacent token replacement per step. The disconnected small cases \(n=3,4\) have no finite all-pairs diameter under the usual disconnected-graph convention. The first-public date refers to the guiding 2023 reconfiguration paper, not a publication date for the present result. Prior-literature searches cannot certify historical uniqueness; an unindexed study of faulty Lucas-cube routing or equivalent cyclic-independent-set flips could cover part or all of the statement. The accompanying program checks only the finite ranges explicitly identified above. No independent mathematical audit has been performed.

## References
- R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *Reconfiguration of Minimum Independent Dominating Sets in Graphs* (2023), arXiv:2303.06299, https://arxiv.org/abs/2303.06299 (first submitted 2023-03-11 UTC).
- R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *The \(i\)-Graphs of Paths and Cycles* (2023), arXiv:2303.08190, https://arxiv.org/abs/2303.08190.
- E. Munarini, C. Perelli Cippo, N. Zagaglia Salvi, *On the Lucas Cubes*, *Fibonacci Quarterly* **39** (2001), 12–21, https://www.fq.math.ca/Scanned/39-1/munarini.pdf.
- A. Castro and M. Mollard, *The eccentricity sequences of Fibonacci and Lucas cubes*, *Discrete Mathematics* **312** (2012), DOI:10.1016/j.disc.2011.11.006, https://doi.org/10.1016/j.disc.2011.11.006.
- J. Azarija, S. Klavžar, J. Lee and Y. Rho, *Connectivity of Fibonacci cubes, Lucas cubes and generalized cubes*, *DMTCS* **17** (2015), https://doi.org/10.46298/dmtcs.2115.
