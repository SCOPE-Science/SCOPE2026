# Critical-mass single-pass chip-firing waves on complete bipartite graphs

## Finding

For the parallel chip-firing map on the labelled complete bipartite graph \(K_{m,n}\), with \(m,n\ge1\), exactly \(mn\) chips, and an initially periodic state in which **every vertex fires once during the least period**, all firing rounds alternate between the two shores. For \(1\le k\le\min(m,n)\), the number of such labelled states having least period \(2k\) is

\[
C_{m,n}(2k)=2(k!)^2\left\{\begin{matrix}m\\k\end{matrix}\right\}\left\{\begin{matrix}n\\k\end{matrix}\right\}.
\]

Here the bracketed quantities are Stirling numbers of the second kind (partitions of a labelled set into \(k\) nonempty, unordered blocks). The number of distinct temporal cycles of period \(2k\) is

\[
O_{m,n}(2k)=k!(k-1)!\left\{\begin{matrix}m\\k\end{matrix}\right\}\left\{\begin{matrix}n\\k\end{matrix}\right\}.
\]

All other least periods are impossible **in this explicitly defined single-pass, critical-mass sector**. In particular, on \(K_{3,3}\) there are exactly 72 period-six configurations, forming 12 distinct period-six orbits. For \(K_{r,r}\), the maximum single-pass period \(2r\) occurs on exactly \(2(r!)^2\) configurations. The result does not classify every state of mass \(mn\).

## Assumptions and scope

Write the labelled shores as \(L=\{u_1,\ldots,u_m\}\) and \(R=\{v_1,\ldots,v_n\}\). Vertices in \(L\) have degree \(n\); those in \(R\) have degree \(m\). A configuration is a function \(x:L\cup R\to\mathbb Z_{\ge0}\), with conserved total chip mass \(\sum_v x(v)\). At every synchronous step, all vertices with \(x(v)\ge\deg(v)\) send one chip to every neighbor, while others send none. We require \(\sum_v x(v)=mn\), initial periodicity \(U^p x=x\) with least positive \(p\), and exactly one firing of every vertex in the \(p\) rounds. These are necessary restrictions of the theorem, not conclusions about unrestricted chip-firing systems. A fixed point is not a single-pass state.

## Proof

**1. The energy equality forces no edge to fire simultaneously.** Fix a state of least period \(p\) satisfying the hypotheses. For every vertex \(v\), let \(t_v\in\{0,\ldots,p-1\}\) be its unique firing round. Before its firing, \(v\) has sent no chips and has received one chip from each neighbor firing at an earlier round. Hence

\[
x(v)+\#\{w\sim v:t_w<t_v\}\ge\deg(v).
\]

Summing over vertices, each edge contributes exactly once to the total of earlier-firing-neighbor counts when its endpoints fire in different rounds, and zero otherwise. Let \(e_=\) be the number of edges whose endpoints fire in the same round. Since \(K_{m,n}\) has \(mn\) edges, summation yields

\[
mn=\sum_vx(v)\ge 2mn-(mn-e_=)=mn+e_=.
\]

Thus \(e_=0\), and equality holds in every individual vertex inequality. Consequently adjacent vertices never fire in the same round, and

\[
x(v)=\#\{w\sim v:t_w>t_v\}.
\]

**2. The nonempty firing rounds must alternate shores.** There cannot be an empty firing round on a nonfixed periodic orbit: then the entire configuration is unchanged, forcing least period one. Because each firing round contains no edge, and every vertex of \(L\) is adjacent to every vertex of \(R\), each nonempty firing set belongs entirely to one shore. Suppose consecutive firing rounds, including the cyclic pair of rounds \(p-1\) and \(0\), came from the same shore. Each vertex scheduled for the later round has neither fired nor received any chips during the earlier round, because all earlier-round firers are on its own shore. Its chip count would therefore be unchanged, so it would already have been eligible in the earlier round, contradicting its unique scheduled firing. Consequently firing shores alternate cyclically, the period is \(p=2k\), and each shore is partitioned into \(k\) nonempty firing blocks. Hence \(1\le k\le\min(m,n)\).

**3. Every alternating pair of ordered partitions produces a distinct state.** Choose ordered partitions \((A_1,\ldots,A_k)\) of \(L\) and \((B_1,\ldots,B_k)\) of \(R\), with all blocks nonempty. Choose the starting shore, say \(L\), and prescribe the successive firing sets

\[
A_1,B_1,A_2,B_2,\ldots,A_k,B_k.
\]

For \(u\in A_i\) and \(v\in B_i\) define

\[
x(u)=n-\sum_{j<i}|B_j|,\qquad x(v)=m-\sum_{j\le i}|A_j|.
\]

These are nonnegative integers. Each edge contributes one chip to the endpoint scheduled to fire first, so \(\sum_vx(v)=mn\). At round zero exactly \(A_1\) has degree-many chips. Inductively, before its prescribed firing round, each vertex has exactly its degree's worth of chips, from its initial count and the preceding firings of its neighbors; at each earlier round its count is **strictly below** its degree because at least one neighboring block, with positive size, is still scheduled before its own firing. Thus precisely the prescribed block fires at each round. After \(2k\) rounds each vertex has fired once and received exactly its degree-many chips, so the state returns. Its least period is exactly \(2k\): if a shorter period divided \(2k\), its repeated copies would cause every vertex to fire at least twice during \(2k\) rounds, a contradiction.

The analogous formula with shores exchanged works when \(R\) fires first. Conversely, Step 1 recovers the initial chip count uniquely from the firing times. From any such initial configuration, its first firing shore is unambiguous and the values of the chips on each shore are strictly decreasing between consecutive firing blocks, because those blocks on the opposite shore are nonempty. Thus different ordered partitions or starting shores cannot produce the same initial state.

There are \(k!\left\{\begin{matrix}m\\k\end{matrix}\right\}\) ordered partitions of \(L\), and independently \(k!\left\{\begin{matrix}n\\k\end{matrix}\right\}\) of \(R\). Multiplication by the two starting shores gives the stated formula. Each cycle contains \(2k\) distinct configurations, giving the orbit count.

## Verification

Two independent Python 3 standard-library checkers accompany this result. Run `python3 enumerate_states.py` and `python3 construct_waves.py`. The first enumerates **all** nonnegative labelled configurations of total mass \(mn\) for nine test graphs (including \(K_{3,5}\) and \(K_{4,4}\)), identifies their actual periodic cycles by direct state iteration, and independently counts the single-pass part. The second constructs every ordered-partition wave for five graphs, directly verifies the prescribed firing sets and first return, and tests distinctness. The two programs agree with the formula on every tested case; their outputs are included. The programs are finite sanity checks, not substitutes for the general proof above.

## Relationship to prior work

T.-Y. Jiang (2010, first public arXiv version) established the complete set of *attainable period lengths* on complete bipartite graphs. In particular, Proposition 3.9 explicitly constructs one state for each period \(k\) and \(2k\). Existence of those periods does not determine the exact number of **all** minimal-mass single-pass states for each period. The present result characterizes this entire sector by alternating ordered partitions and gives a Stirling-number orbit census.

Jiang, Scully and Zhang (2012, initial preprint) characterized allowed periodic individual firing sequences on arbitrary graphs. Their nonclumpiness results constrain patterns but do not count the labelled critical-mass period-six-and-higher states on \(K_{m,n}\). Ji, Li and Wang (2024) investigate different chip-density bands, not the present fixed-mass enumeration.

The smallest periods have independent preceding enumerative coverage: a general cut formula for primitive two-cycles and a mass-generating census of primitive four-cycles on \(K_{2,b}\) imply some \(k=1\) and \(k=2\) special cases. The new enumeration is not claimed as a rediscovery of those cases; its substantive content is the exact infinite-family profile, particularly \(k\ge3\), which the prior cited period-existence and lower-period censuses do not provide.

## Limitations

The theorem treats configurations that are **already periodic**, with exactly \(mn\) chips and one firing per vertex during their least period. It does not establish that all periodic states at mass \(mn\) are single-pass, nor enumerate states with multiple firings per vertex, fixed points, or eventual attraction basins. The priority comparison is subject to an inaccessible related 2000 paper on source reversal and chip firing, for which only bibliographic and abstract material was available; its exact results were not asserted to be excluded. Historical priority is therefore qualified rather than certified.

## References

1. Tian-Yi Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, initial version March 4, 2010. In particular Proposition 3.9 and Theorem 3.10. https://arxiv.org/abs/1003.0943
2. Tian-Yi Jiang, Ziv Scully, and Yan X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786, first version November 29, 2012. In particular Theorem 6.2 and Section 7. https://arxiv.org/abs/1211.6786
3. David Ji, Michael Li, and Daniel Wang, *Non-Stabilizing Parallel Chip-Firing Games*, arXiv:2408.10508, first version August 2024. https://arxiv.org/abs/2408.10508
4. Eric Goles and Erich Prisner, *Source reversal and chip firing on graphs*, Theoretical Computer Science 233 (2000), 287–295. DOI: 10.1016/S0304-3975(99)00122-X. Abstract/bibliography checked; full text was not available.
