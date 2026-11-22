# All-cardinality token-slide geometry of independent dominating sets on open ladders

## Finding
Let \(L_n=P_n\square K_2\) be the open ladder with \(n\ge2\) labelled rungs. For an integer \(k\), let \(\mathcal R_{n,k}\) be the graph whose vertices are **independent dominating vertex sets of cardinality \(k\)** in \(L_n\), where adjacent configurations differ by sliding one selected vertex along an edge of \(L_n\), preserving both independence and domination. Put \(z=n-k\) and \(p=k-1\). Then \(\mathcal R_{n,k}\) is empty unless
\[
\left\lceil\frac{n+1}{2}\right\rceil\le k\le n.
\]
For every integer \(k\) in that range, there is a labelled, explicit graph isomorphism
\[
\boxed{\mathcal R_{n,k}\cong T_z(P_p)\;\sqcup\;T_z(P_p),}
\]
where \(T_z(P_p)\) is the \(z\)-token exclusion graph on a path with vertex positions \(1,\ldots,p\): its vertices are the \(z\)-subsets of these positions, adjacent precisely when an occupied and a vacant consecutive position are interchanged. Both copies are connected, including the singleton cases.

Consequently, \(\mathcal R_{n,k}\) has precisely two connected components of \(\binom{k-1}{n-k}\) vertices each, and
\[
\begin{aligned}
|V(\mathcal R_{n,k})|&=2\binom{k-1}{n-k},\\
|E(\mathcal R_{n,k})|&=\begin{cases}
2(k-2)\binom{k-3}{n-k-1},&1\le n-k\le k-2,\\
0,&\text{otherwise}.
\end{cases}
\end{aligned}
\]
Every connected component is a **median graph**. If \(A=\{a_1<\cdots<a_z\}\) and \(B=\{b_1<\cdots<b_z\}\) are the gap-position encodings of configurations in the same component, then their *exact* reconfiguration distance is
\[
\boxed{d(A,B)=\sum_{i=1}^{z}|a_i-b_i|,}
\]
and each component has diameter
\[
\boxed{z(p-z)=(n-k)(2k-n-1).}
\]
There is no reconfiguration sequence between different components without leaving the specified class of configurations.

The size-refined enumerator and size-refined edge enumerator over all positive orders are, respectively,
\[
\sum_{n\ge2}\sum_k|V(\mathcal R_{n,k})|y^kt^n
=\frac{2y^2t^2(1+t)}{1-yt-yt^2},
\qquad
\sum_{n\ge2}\sum_k|E(\mathcal R_{n,k})|y^kt^n
=\frac{2y^3t^4}{(1-yt-yt^2)^2}.
\]
Summing the first formula over sizes gives \(2F_n\) independent dominating sets for an \(n\)-rung ladder, **a previously established count**, not a new claim. Here \(F_1=F_2=1\).

For minimum-cardinality configurations, \(i(L_n)=\lceil(n+1)/2\rceil\). Thus their reconfiguration graph is \(2K_1\) for odd \(n\), and \(2P_{n/2}\) for even \(n\); at \(n=2\) this is \(2K_1\).

## Assumptions and scope
All graphs are simple, undirected, finite, and labelled. Ladder rungs are ordered from \(1\) to \(n\), each with a top and a bottom vertex. Independence forbids selecting both ends of an edge. Domination means every vertex either belongs to the set or has a selected neighbor. Independent dominating sets are precisely inclusion-maximal independent sets; they are not required to have the minimum possible size unless specifically stated. The reconfiguration rule is **token sliding**, not arbitrary recoloring or a move temporarily violating domination. The \(z\)-token path graph allows \(z=0\) and \(z=p\); each such graph has a single vertex. The component distance statement applies only inside a component.

## Proof
**1. Structure of every independent dominating set.** Each rung has at most one selected vertex by independence. An endpoint rung must be occupied: if the first rung were empty, each of its two vertices could only be dominated from the second rung, which cannot contain two selected vertices. Likewise the last rung must be occupied. No two consecutive rungs can be empty, since the first of two consecutive empty rungs would have only one adjacent occupied rung to cover its two vertices. Moreover, if two occupied rungs have no vacancy between them, their selected top/bottom positions must differ by independence. If they have exactly one vacant rung between them, those selected positions must differ so that both vertices of the vacant rung are dominated. Therefore, reading occupied rungs left to right, the selected layers alternate strictly. Conversely, an assignment with occupied endpoints, no consecutive vacant rungs and alternating layers across occupied rungs is independent and dominates every vertex.

**2. Unique gap coordinates and cardinalities.** With \(k\) occupied rungs, there are \(p=k-1\) gaps between successive occupied rungs. Each gap has length zero or one vacancy. Write \(b_j=1\) when the \(j\)-th gap contains one vacancy; otherwise \(b_j=0\). Then \(\sum_jb_j=z=n-k\). The side of the first selected vertex is an independent binary choice \(\sigma\in\{0,1\}\); once fixed, every subsequent selected layer is forced by alternation. These data reconstruct the entire labelled vertex set uniquely. Such a word exists if and only if \(0\le z\le p\), equivalent to the stated size range. Thus \(|V|=2\binom{p}{z}\), with two naturally distinguished classes of size \(\binom pz\).

**3. Exactly which slides are legal.** A vertical move from one layer to the other in an occupied rung leaves all other occupied rungs unchanged. Since \(k\ge2\) and the two neighboring occupied vertices in the occupied-rung order must have opposite layer labels, a change of that single layer cannot preserve the characterization in step 1. A horizontal move into a vacant neighboring rung is possible only if the new vacancy remains isolated and the occupied endpoint rungs remain occupied. In gap coordinates, it moves one vacancy across a selected rung, exactly interchanging an adjacent pair \(01\leftrightarrow10\) in the length-\(p\) gap word. Conversely any such interchange defines a legal horizontal slide, since it preserves the total gap count, endpoint occupancy and alternating occupied layers. It leaves the first selected layer \(\sigma\) unchanged. Thus the entire graph is exactly the two asserted copies of \(T_z(P_p)\). Each copy is connected, since successive adjacent swaps move all occupied gap positions to the leftmost \(z\) locations.

**4. Exact edges and generating functions.** Fix a consecutive gap-position pair among the \(p-1\) pairs. Exactly \(2\binom{p-2}{z-1}\) gap words have opposite bits at this pair, so the total degree sum within one copy is \(2(p-1)\binom{p-2}{z-1}\). Dividing by two and doubling for the two copies gives \(2(p-1)\binom{p-2}{z-1}\) edges, with zero edges at the saturated endpoints. This is the claimed formula. Its bivariate series follows by substituting \(n=k+z\), letting \(j=k-3\) and \(h=z-1\), summing \(2(j+1)\binom{j}{h}(yt)^jt^h\), and using \(\sum_{j\ge0}(j+1)v^j=(1-v)^{-2}\). The vertex series similarly follows from \(\sum_{p\ge0}\sum_{z=0}^p\binom pz(yt)^pt^z=(1-yt-yt^2)^{-1}\), with an initial factor \(2yt\), after subtracting the excluded \(n=1\) term \(2yt\). The previously known total count \(2F_n\) is an immediate specialization, not asserted as novel.

**5. Geodesics and medians.** List occupied gap positions in increasing order: \(1\le a_1<\cdots<a_z\le p\). A swap moves one position by one unit without changing the order. Therefore any reconfiguration path from \(A\) to \(B\) uses at least \(\sum_i|a_i-b_i|\) steps. To attain that bound, first move all particles requiring leftward travel leftwards, processing them from left to right; then move all particles requiring rightward travel rightwards, processing them from right to left. At every step the destination is empty by these orders and because the target positions are strictly increasing, so there is no need to reverse a move. This gives exactly the lower bound. The maximum coordinatewise distance is attained between \(A=\{1,\ldots,z\}\) and \(B=\{p-z+1,\ldots,p\}\), and no other two ordered lists can have larger aggregate displacement than \(z(p-z)\).

For three ordered lists \(A,B,C\), define their median list by taking the median of the three entries at each coordinate. This is again strictly increasing: if each of three numbers in coordinate \(i\) is strictly smaller than its counterpart in coordinate \(i+1\), their order statistics have the same property. The distance formula shows that this list lies on a geodesic between each pair. Any list lying on all three pairwise geodesics must at every coordinate lie simultaneously in the three intervals with endpoints \((a_i,b_i)\), \((b_i,c_i)\) and \((a_i,c_i)\); their intersection is the singleton coordinate median. Thus the median is unique. Each component is a median graph.

**6. Smallest-size classification.** For odd \(n=2r+1\), minimum \(k=r+1\) means \(p=z=r\), so both components are singletons. For even \(n=2r\), minimum \(k=r+1\) means \(p=r,z=r-1\), and \(T_{r-1}(P_r)\cong P_r\), since a configuration is determined by the position of its single empty gap and slides move it one step. This gives the claimed two-path structure, including the single-edge ladder case \(n=2\).

## Verification
Three distinct reproducible verification programs and their complete recorded outputs accompany this result. `verify_direct.cpp` constructs the original \(2n\)-vertex ladder from edges and enumerates every vertex subset for \(2\le n\le10\), testing independence and domination directly, then builds actual slide edges and checks each fixed-size component, count, edge total and diameter. `verify_word.py` independently enumerates ternary rung words through \(n=18\), checks the domination conditions and compares every admissible slide with its alleged adjacent-bit interchange. `verify_median.py` enumerates all gap-token graphs of path order at most eight, checking shortest distances, edge counts, diameters and unique medians for all small configurations. The final output markers are respectively `DIRECT_EXHAUSTIVE_PASS`, `WORD_BIJECTION_AND_MOVES_PASS`, and `MEDIAN_AND_DISTANCE_PASS`. These finite experiments corroborate the proof but do not replace its universal arguments.

## Relationship to prior work
Stevanović (2001) proved the **unweighted** maximal-independent-set count \(2F_n\) for an \(n\)-rung open ladder (equivalently its \((n-1)\)-square convention). That formula is credited as known. Brewster, Mynhardt and Teshima (2023) developed independent-domination reconfiguration graphs and classified those of paths and cycles, but their inspected papers do not classify independent dominating sets of open ladders for every size. A published 2026 calculation for minimum independent domination on *circular ladders* \(C_n\square K_2\) uses cyclic binary gap words but determines neither the open-boundary graph families nor their complete all-cardinality distance and median geometry. Hoang (2026) studied when **ladder graphs are targets** of token-sliding realizability, not when the ladder itself is the seed under independent-domination constraints. These differences concern statements and hypotheses, not merely terminology. An unindexed treatment of the same path-particle encoding could still predate the present result.

## Limitations
The graph is the two-row **open** ladder, not a circular or twisted prism. Reconfiguration must preserve independent domination and the fixed cardinality throughout. The theorem does not describe the token-sliding graph of all independent sets without domination, token addition/removal, or distances between distinct connected components. The total unweighted Fibonacci count is previously known. The priority assessment is based on accessible comparisons, rather than exhaustive indexing of unpublished material; independent scientific review has not been performed.

## References
- D. Stevanović, *On the Number of Maximal Independent Sets of Vertices in Star-Like Ladders*, Fibonacci Quarterly **39** (2001), 211–213. Full text: https://www.fq.math.ca/Scanned/39-3/stevanovic.pdf.
- R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *Reconfiguration of Minimum Independent Dominating Sets in Graphs*, arXiv:2303.06299, first public 2023-03-11. https://arxiv.org/abs/2303.06299.
- R. C. Brewster, C. M. Mynhardt, L. E. Teshima, *The \(i\)-Graphs of Paths and Cycles*, arXiv:2303.08190, first public 2023-03-14. https://arxiv.org/abs/2303.08190.
- D. A. Hoang, *Token-sliding realizability for complements, Cartesian-products, and grid graph families*, arXiv:2606.03765, first public 2026-06-02. https://arxiv.org/abs/2606.03765.
- *Minimum independent-domination reconfiguration on circular ladders*, published 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-minimum-independent-domination-reconfiguration-on-circular-ladde--5713d863fdac.
