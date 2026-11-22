# Exact two-hop token reconfiguration metrics on thin spiders

## Finding
Let \(r\ge2\), and form the thin spider \(H_r\) from a clique with labelled vertices \(c_1,\ldots,c_r\) by attaching one private leaf \(u_i\) to each \(c_i\). Fix \(1\le k\le r\). Let \(\mathcal R_{r,k}\) be the graph whose vertices are the independent \(k\)-sets of \(H_r\), with an edge when a single token is relocated between two vertices at graph distance at most two and the resulting set is independent.

Every state is either \(P_S=\{u_i:i\in S\}\), for \(S\subseteq[r]\), \(|S|=k\), or \(M_{j,T}=\{c_j\}\cup\{u_i:i\in T\}\), for \(j\notin T\subseteq[r]\), \(|T|=k-1\). The complete adjacency classification is:

- \(P_S\) is adjacent to \(M_{j,T}\) if and only if \(T\subset S\) (and, as required by the state definition, \(j\notin T\));
- \(M_{j,T}\) and \(M_{h,U}\) are adjacent if and only if \(T=U\) and \(j\ne h\);
- no two pure states \(P_S\) are adjacent.

For any states, the exact unweighted shortest-path distance is
\[
\begin{aligned}
d(P_S,P_U)&=2(k-|S\cap U|),\\
d(P_S,M_{j,T})&=2(k-1-|S\cap T|)+1,\\
d(M_{j,T},M_{h,U})&=
\begin{cases}
\mathbf1_{j\ne h},&T=U,\\
2(k-1-|T\cap U|),&T\ne U.
\end{cases}
\end{aligned}
\]
In particular, \(\mathcal R_{r,k}\) is connected and
\[
\boxed{\operatorname{diam}(\mathcal R_{r,k})=\min\{2k,\,2(r-k+1),\,r\}.}
\]
It has \((k+1)\binom rk\) states. Every pure state has degree \(k(r-k+1)\); every mixed state has degree \(2(r-k)+1\). Its number of edges is
\[
k(r-k+1)\binom rk+\binom r{k-1}\binom{r-k+1}{2}.
\]

## Assumptions and scope
All graphs are finite, undirected, simple, and labelled. A step relocates **exactly one** token and uses distance in the **underlying thin spider**, not distance in the reconfiguration graph. The independence constraint holds after every step, and token number \(k\) is fixed throughout. The range \(r\ge2\), \(1\le k\le r\), includes maximum independent sets. No theorem about arbitrary split graphs or other jump radii is asserted.

## Proof
**1. Classification and legal edges.** The clique admits at most one selected vertex; if it is \(c_j\), its private leaf \(u_j\) must be unselected. This gives exactly the two state types above. For different indices \(a\ne b\), underlying distances are \(d_{H_r}(u_a,u_b)=3\), \(d_{H_r}(c_a,c_b)=1\), and \(d_{H_r}(u_a,c_b)=2\) (where the last distance is one if \(a=b\)). Consequently a legal two-hop step cannot exchange two different leaves. Exchanging a leaf with an admissible clique vertex gives precisely a pure–mixed edge as stated; exchanging two admissible clique vertices leaves the selected leaf set fixed and gives precisely a mixed–mixed edge.

**2. Lower bounds on distances.** At a pure state exactly \(k\) leaves are occupied; at a mixed state exactly \(k-1\) leaves are occupied. A pure–mixed move adds or removes exactly one leaf, while a mixed–mixed move changes no leaves. Since pure–pure moves are forbidden, replacing one leaf label by a different leaf label needs at least two moves, with a mixed state between them. A path from \(P_S\) to \(P_U\) must replace \(k-|S\cap U|\) labels and hence uses at least \(2(k-|S\cap U|)\) moves. A path from \(M_{j,T}\) to \(M_{h,U}\), when \(T\ne U\), must replace \((k-1)-|T\cap U|\) labels and hence uses at least twice this many moves. From \(P_S\) to \(M_{j,T}\), exactly \(k-1-|S\cap T|\) new leaf labels must be introduced, and the path must finish mixed; it therefore needs at least \(2(k-1-|S\cap T|)+1\) steps. Finally, when \(T=U\), a changed clique vertex requires at least one move.

**3. Matching constructions.** For a pure-to-pure replacement \(a\in S\setminus U\) by \(b\in U\setminus S\), execute \(P_S\to M_{a,S\setminus\{a\}}\to P_{S\setminus\{a\}\cup\{b\}}\). Both moves are legal because every clique vertex is within distance two of every leaf. Repeat for all mismatches. For a mixed-to-mixed replacement \(a\in T\setminus U\) by \(b\in U\setminus T\), execute \(M_{j,T}\to P_{T\cup\{b\}}\to M_{a,T\setminus\{a\}\cup\{b\}}\). Repeat, choosing \(c_h\) on the final second move. The target clique index \(h\) is outside \(U\), so the final move is legal. If \(T=U\), change the clique position in one move, or use zero moves if already identical. For a pure-to-mixed route, choose \(a\in S\setminus T\), first transform \(P_S\) to \(P_{T\cup\{a\}}\) by \(k-1-|S\cap T|\) pure-to-pure replacements, then move \(u_a\) to \(c_j\). These paths match all lower bounds, proving the distance formulas and connectivity.

**4. Extremal metric and counts.** The largest pure–pure distance is \(2\min\{k,r-k\}\). The largest pure–mixed distance is \(2\min\{k-1,r-k\}+1\). For \(k\ge2\), the largest mixed–mixed distance with different leaf sets is \(2\min\{k-1,r-k+1\}\); same-leaf mixed states are at distance at most one. For \(k=1\), the pure–pure maximum is already two. Comparing these maxima in the cases \(k\le r/2\), \(k\ge(r+2)/2\), and the possible central odd case \(2k=r+1\) yields exactly \(\min\{2k,2(r-k+1),r\}\). Every extremal intersection size is realized by subsets of \([r]\), so these are attained maxima.

There are \(\binom rk\) pure states and \(r\binom{r-1}{k-1}=k\binom rk\) mixed states. From a pure state, each of its \(k\) leaves may be replaced by one of \(r-k+1\) permitted clique vertices, giving degree \(k(r-k+1)\). From a mixed state there are \(r-k+1\) pure neighbors and \(r-k\) same-leaf-set mixed neighbors, giving degree \(2(r-k)+1\). Count every pure–mixed edge from its pure endpoint, and count the clique edges among the \(r-k+1\) mixed states over each fixed \((k-1)\)-subset to obtain the edge formula.

## Verification
`CHECK.py` constructs the original labelled thin spider from first principles, independently enumerates all independent sets, recomputes original-graph distances by breadth-first search, builds every legal two-hop move without using the structural theorem, and then compares all-pairs reconfiguration-graph BFS distances with the formulas. It checks all \(35\) pairs of parameters \(2\le r\le8\), \(1\le k\le r\). It also checks state counts, edges, two degree classes, connectivity, and diameters, plus symbolic extrema for all \(2\le r\le200\). Run `python3 CHECK.py` using the standard Python library. This finite verification supports but does not replace the all-parameter proof.

## Relationship to prior work
Hatano, Kitamura, Izumi, Ito and Masuzawa introduced the bounded-hop rule and proved polynomial-time **reachability** under the two-hop rule on general split graphs. Their paper explicitly asks for the complexity of **shortest** two-hop independent-set reconfiguration on split graphs. The present theorem supplies the complete shortest-path metric and full graph structure for the canonical thin-spider subfamily \(K_r\circ K_1\); it does not solve the general question. Earlier split-graph token-sliding results concern moves of original-graph distance one, not the two-hop edges treated here. Existing Johnson-graph distance formulas apply to pure subset labels only after the requisite two-hop reconfiguration structure has been established.

## Limitations
This is a result for the exact family of clique coronas, not a classification of arbitrary split graphs, and it assumes the strict two-hop bound. It does not establish the complexity of general two-hop shortest reconfiguration. Independent external verification and historical-priority adjudication remain outstanding; an equivalent graph construction under other terminology could exist.

## References
1. H. Hatano, N. Kitamura, T. Izumi, T. Ito, T. Masuzawa, *Independent Set Reconfiguration Under Bounded-Hop Token Jumping*, arXiv:2407.11768, first public 2024-07-16, https://arxiv.org/abs/2407.11768 .
2. R. Belmonte, E. J. Kim, M. Lampis, V. Mitsou, Y. Otachi, F. Sikora, *Token Sliding on Split Graphs*, Theory of Computing Systems 65 (2021), 662–686, https://doi.org/10.1007/s00224-020-09967-8 .
3. D. A. Hoang, A. Khorramian, R. Uehara, *Shortest Reconfiguration Sequence for Sliding Tokens on Spiders*, CIAC 2019, https://arxiv.org/abs/1806.08291 (distinct base-graph family and one-hop rule).
