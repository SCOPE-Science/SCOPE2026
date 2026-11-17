# Isometric token sliding for cyclic \(k\)-path vertex covers

## Finding

**Theorem (exact cycle-cover slide metric).** Let \(n,k,t\) be integers with \(n\ge 3\), \(2\le k<n\), and \(\lceil n/k\rceil\le t<n\). Give the cycle \(C_n\) vertices \(0,1,\ldots,n-1\), cyclically. A \(k\)-path vertex cover is a subset meeting every simple path on \(k\) vertices, and a token slide moves a selected vertex one cycle edge to a currently unselected vertex while retaining the cover condition. Write \(\mathcal R_{n,k,t}\) for the graph of these covers of cardinality \(t\), joined by single token slides.

If \(kt=n\), the graph \(\mathcal R_{n,k,t}\) consists of precisely \(k\) isolated vertices (the equally spaced configurations). Otherwise, it is connected and is **isometric** in the unrestricted \(t\)-token graph of \(C_n\). More explicitly, for any two covers \(S,T\), set
\[
 p_i=\sum_{j=0}^{i}\bigl(\mathbf 1_S(j)-\mathbf 1_T(j)\bigr),\qquad 0\le i<n.
\]
If \(kt>n\), their exact shortest legal token-slide distance is
\[
 \boxed{d_{\mathcal R_{n,k,t}}(S,T)=\min_{c\in\mathbb Z}\sum_{i=0}^{n-1}|p_i+c|
 =\sum_{i=0}^{n-1}|p_i-m|},
\]
where \(m\) is any median of the \(n\) integers \(p_0,\ldots,p_{n-1}\). A shortest reconfiguration sequence exists and can be constructed without any moves beyond the unrestricted optimum. The distance can be evaluated in linear time in \(n\) by accumulating the \(p_i\) and choosing a median (for example using a counting array on \([-n,n]\)).

In particular, this settles the shortest-token-slide problem on cycles for **every admissible number of tokens**, not just minimum covers, and for every permissible path order. The fully occupied case \(t=n\), excluded above, consists of a single state and has distance zero.

## Assumptions and scope

All paths considered are simple paths in the ordinary undirected simple cycle, with \(2\le k<n\). Thus every \(k\)-vertex path is a consecutive cyclic window. Covers are labelled vertex subsets; rotations and reflections are **not** identified. Each move changes one occupied position by one along a cycle edge and preserves both cardinality and the \(k\)-path cover property. Distances are minimum counts of moves, not Hamming distance or token-jumping distance. The theorem concerns precisely \(\lceil n/k\rceil\le t\le n\); smaller sets do not cover the cycle.

For a cover with occupied positions in clockwise order, write \(x_i\), with periodic extension \(x_{i+t}=x_i+n\). The cover condition is equivalent to every consecutive gap satisfying \(1\le x_{i+1}-x_i\le k\). Summing gives \(t\le n\le kt\), and \(t\ge\lceil n/k\rceil\) is necessary and sufficient for covers to exist.

## Proof

**1. Frozen boundary.** If \(kt=n\), every one of the \(t\) positive gaps is at most \(k\) and has total \(tk\), hence every gap equals \(k\). Exactly \(k\) phase translates exist, corresponding to occupied congruence classes modulo \(k\). Since \(t\ge2\) and increasing one gap by one necessarily produces a forbidden gap \(k+1\), no token can slide. The theorem's remaining case satisfies \(t<n<kt\).

**2. Universal circular-flow lower bound.** Orient the cycle edges clockwise, edge \(i\) from \(i\) to \(i+1\) modulo \(n\). For any token-slide sequence from \(S\) to \(T\), let \(f_i\) be the net number of clockwise minus anticlockwise traversals of edge \(i\). Conservation at vertex \(i\) gives
\[
 f_i-f_{i-1}=\mathbf 1_S(i)-\mathbf 1_T(i),
\]
so necessarily \(f_i=p_i+c\) for some integer \(c\). Each edge contributes at least \(|f_i|\) actual slides. Every sequence, even one ignoring the cover condition, consequently has length at least \(\min_c\sum_i|p_i+c|\). The minimizing \(c\) is minus any integer median \(m\) of the \(p_i\).

**3. An optimal cut and ordered matching.** Choose an index \(h\) with \(p_h=m\). For the optimal flow \(f_i=p_i-m\), edge \(h\) has zero net flow. Cut the cycle at that edge, viewing the remaining vertices as the ordered interval \(h+1,\ldots,h+n\). List the starting and target token positions in this interval as \(x_0<\cdots<x_{t-1}\) and \(y_0<\cdots<y_{t-1}\), respectively. The ordered pairing \(x_i\mapsto y_i\) on a path has total transport length
\[
 L=\sum_{i=0}^{t-1}|x_i-y_i|=\sum_{j\ne h}|f_j|=\sum_{j=0}^{n-1}|p_j-m|.
\]
To see the middle equality, at each uncut edge the difference between the numbers of starting and target tokens in the prefix ending there is exactly \(f_j\). For the ordered matching, all pairs crossing a fixed cut cross in the same direction, and exactly \(|f_j|\) pairs cross; summing over edges counts their total travelled lengths. It remains to prove that this ordered matching can be carried out by legal slides without increasing \(L\).

**4. Bounded-gap lattice lemma.** Let \(a=(a_0,\ldots,a_{t-1})\) and \(b=(b_0,\ldots,b_{t-1})\) be two integer lifts of feasible configurations, both satisfying the periodic rule \(a_{i+t}=a_i+n\), \(b_{i+t}=b_i+n\) and the gap inequalities \(1\le a_{i+1}-a_i\le k\), \(1\le b_{i+1}-b_i\le k\). Their coordinatewise maximum \(z_i=\max(a_i,b_i)\), periodically extended, also satisfies these inequalities: the maximum of two sequences each increasing by at least one and at most \(k\) between successive coordinates obeys the same two bounds. The coordinatewise minimum likewise satisfies them.

Suppose \(a_i\le b_i\) for all \(i\) and \(t<n<kt\). We claim there is a sequence of legal **single-coordinate increases** from \(a\) to \(b\) of length exactly \(\sum_i(b_i-a_i)\). At a current feasible \(a\), let \(U=\{i:a_i<b_i\}\). Increasing coordinate \(i\in U\) by one is blocked only if the next gap is \(1\) (collision) or the preceding gap is \(k\) (gap overflow). If the next gap is \(1\), then \(b_{i+1}\ge b_i+1>a_i+1=a_{i+1}\), so \(i+1\in U\). If the preceding gap is \(k\), then \(b_{i-1}\ge b_i-k>a_i-k=a_{i-1}\), so \(i-1\in U\). Thus every blocked coordinate in \(U\) points to another coordinate in \(U\), along an adjacent cyclic gap that is respectively tight at its lower or upper bound.

If every coordinate of \(U\) were blocked, this finite dependency digraph would contain a directed cycle. Immediate reversals across the same gap would require that gap to equal both \(1\) and \(k\), impossible because \(k\ge2\). Hence a dependency cycle must wind consistently all the way around the token index ring; it would require **every** gap to equal \(1\) or **every** gap to equal \(k\). Their sums would be \(n=t\) or \(n=tk\), contradicting \(t<n<kt\). The same argument covers \(t=2\), treating its two cyclic gaps as distinct. Therefore an allowed increase exists whenever \(U\ne\varnothing\). Repeating proves the claim. Reversing such an increasing sequence gives an equally short sequence of decreases.

**5. Legal optimal path.** Apply the lemma with \(a=x\) and \(b=z=\max(x,y)\), and then reverse its application from \(y\) to \(z\). The result is a legal single-token slide sequence \(x\to z\to y\) of length
\[
 \sum_i(z_i-x_i)+\sum_i(z_i-y_i)=\sum_i|x_i-y_i|=L.
\]
All its coordinates stay between their respective initial and final values and therefore inside the chosen cut interval. The gap inequalities hold at every intermediate step, including the wrap-around gap, so every intermediate configuration is a \(k\)-path vertex cover of the **original cycle**. Thus the cut edge is not crossed and every move is legal. This meets the flow lower bound, proves the formula and the isometric statement, and provides the promised constructive shortest route. \(\square\)

## Verification

The included `verify_cyclic_pvc.py` independently enumerates all cyclic covers, builds token-slide adjacency, computes all BFS distances, and compares them with the median-prefix formula for every \(3\le n\le10\), every \(2\le k<n\), and every \(\lceil n/k\rceil\le t\le n\). This includes the frozen regime, where distinct states must be unreachable. Its observed output is `PYTHON_EXHAUSTIVE_PASS instances=221 BFS_roots=10427`.

The independent `verify_cyclic_pvc.cpp` enumerates binary masks and their one-edge exchanges using a separate representation, performs all-roots BFS, and compares all distances for \(3\le n\le12\) and the same complete \(k,t\) ranges. Compile with `g++ -O2 -std=c++17 verify_cyclic_pvc.cpp -o verify_cyclic_pvc` and execute `./verify_cyclic_pvc`. Its observed output is `CPP_INDEPENDENT_PASS instances=405 BFS_roots=55994`.

The `verify_geodesic_constructor.py` constructs actual optimal legal routes via the median cut, coordinatewise maxima and greedy lattice updates, and validates every successive cover and the optimal length. With fixed seed it passed \(12{,}488\) instances, including cycles of order \(100\). Run it with `python3 verify_geodesic_constructor.py`. These finite checks corroborate but do not replace the all-order proof.

## Relationship to prior work

Brešar, Kardoš, Katrenič and Semanišin introduced and analyzed \(k\)-path vertex covers (2010 arXiv preprint; journal 2011). Hoang, Suzuki and Yagita (arXiv 1911.03026, first public 2019; journal 2022), in their Section 4.2.2 and Theorem 16, already proved the **reachability** dichotomy on cycles: equally sized covers are mutually reconfigurable except the frozen minimum-size configurations at orders divisible by \(k\). They construct polynomial-time reconfiguration sequences but explicitly note their cycle algorithms do **not** always return shortest sequences; their shortest-sequence theorem is for paths. Neither established the present **exact circular-flow distance** or the **isometric embedding** of each nonfrozen layer. The frozen-state and connectivity cases are cited as prior, not claimed novel. The median transport characterization also resembles standard one-dimensional transportation, but the key additional argument is a monotone legal realization within the upper-bounded cyclic-gap constraints.

## Limitations

The distance formula is **not** asserted between distinct frozen phase classes; their distance is infinite. The result does not cover token jumping, token addition/removal, graphs other than ordinary cycles, or constraints allowing paths of arbitrary order. The claim assumes the labelled, undirected, unweighted cycle and at least two occupied vertices. Independent historical-priority review has not been performed; an equivalent treatment of bounded-gap exclusion dynamics may exist under another terminology. Numerical verification is finite; the infinite conclusion relies on the proof above.

## References

1. B. Brešar, F. Kardoš, J. Katrenič, G. Semanišin, *Minimum k-path vertex cover*, arXiv:1012.2088 (first posted December 9, 2010), Discrete Applied Mathematics 159 (2011), 1189–1195. https://arxiv.org/abs/1012.2088 ; DOI: 10.1016/j.dam.2011.04.008.
2. D. A. Hoang, A. Suzuki, T. Yagita, *Reconfiguring k-Path Vertex Covers*, arXiv:1911.03026 (first posted November 8, 2019), IEICE Transactions on Information and Systems E105-D (2022), 1258–1272. https://arxiv.org/abs/1911.03026 ; DOI: 10.1587/transinf.2021EDP7177. See Section 4.2.2 and Theorem 16.
3. D. A. Hoang, *TS-Reconfiguration of k-Path Vertex Covers in Caterpillars for k >= 4*, arXiv:2203.11667 (2022). https://arxiv.org/abs/2203.11667. This studies a different graph class and provides algorithmic context only.
