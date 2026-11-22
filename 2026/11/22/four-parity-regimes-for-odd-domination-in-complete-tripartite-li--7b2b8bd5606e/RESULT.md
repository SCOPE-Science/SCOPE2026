# Four parity regimes for odd domination in complete-tripartite line graphs

## Finding
Let \(a,b,c\ge1\) be integers. Write \(H=K_{a,b,c}\) for the complete tripartite graph with labelled vertex parts \(A,B,C\) and \(G=L(H)\) for its line graph. An *odd-dominating set* is a subset \(S\subseteq V(G)\) that meets the **closed** neighborhood of every vertex in an odd number of vertices. It is *connected odd dominating* if the graph induced by \(S\) is connected.

The complete classification, including every cardinality, has four parity regimes. The parts may be permuted without changing any conclusion. Write \(W_{a,b,c}(z)=\sum_{S\text{ odd-dominating}}z^{|S|}\).

1. **Three even part sizes:** The only odd-dominating set is all of \(E(H)\), and it is connected. Thus \(W_{a,b,c}(z)=z^{ab+ac+bc}\).
2. **Three odd part sizes:** There are exactly four odd-dominating sets: the full edge set \(E(H)\) and the three complete bipartite edge sets \(E(A,B),E(A,C),E(B,C)\). All four are connected, and
   \[
   W_{a,b,c}(z)=z^{ab+ac+bc}+z^{ab}+z^{ac}+z^{bc}.
   \]
   The minimum connected odd-dominating cardinality is \(\min\{ab,ac,bc\}\).
3. **Two odd parts and one even part:** If \(a,b\) are odd and \(c\) is even, independently choose odd-cardinality subsets \(X\subseteq A\) and \(Y\subseteq B\), and let \(S\) comprise exactly the edges of \(H\) having either both endpoints in \(X\cup Y\) or neither endpoint there. This gives every odd-dominating set uniquely. Exactly one is connected, namely \(S=E(A,B)\), of cardinality \(ab\). With \(x=|X|\) and \(y=|Y|\),
   \[
   W_{a,b,c}(z)=\sum_{\substack{1\le x\le a\\x\text{ odd}}}\sum_{\substack{1\le y\le b\\y\text{ odd}}}\binom ax\binom by
   z^{xy+(a-x)(b-y)+c(a+b-x-y)}.
   \]
   There are exactly \(2^{a+b-2}\) odd-dominating sets.
4. **One odd part and two even parts:** If \(a\) is odd and \(b,c\) are even, independently choose odd-cardinality subsets \(Y\subseteq B\) and \(Z\subseteq C\), and let \(S\) consist exactly of edges of \(H\) whose endpoints both belong to \(Y\cup Z\) or both lie outside it. This gives every odd-dominating set uniquely, and **none is connected**. With \(y=|Y|\), \(\ell=|Z|\),
   \[
   W_{a,b,c}(z)=\sum_{\substack{1\le y\le b\\y\text{ odd}}}\sum_{\substack{1\le \ell\le c\\\ell\text{ odd}}}\binom by\binom c\ell
   z^{a(b+c-y-\ell)+y\ell+(b-y)(c-\ell)}.
   \]
   There are exactly \(2^{b+c-2}\) odd-dominating sets.

In particular, for each \(m\ge1\), the connected claw-free graph \(L(K_{1,2m,2m})\) has \(4m^2+4m\) vertices and minimum degree \(4m\), has exactly \(2^{4m-2}\) odd-dominating sets, and has **no connected odd-dominating set**. Thus connected-odd-domination nonexistence persists in an explicit family with unbounded minimum degree, despite exponentially many feasible ordinary odd-dominating configurations.

## Assumptions and scope
All graphs are finite, simple and undirected. The base graph has three nonempty, distinguished labelled independent parts; each vertex of the line graph represents one base edge. The line-graph adjacency relation means that two distinct base edges share an endpoint. Closed neighborhoods include the vertex itself. Oddness and linear algebra refer to \(\mathbb F_2\). Cardinality polynomials count labelled subsets of line-graph vertices, not orbits or sequences. Connectivity refers to the induced graph on selected vertices.

## Proof
Identify the vertex set of \(G\) with the edge set of \(H\). For an odd-dominating selection, let \(x_{uv}\in\mathbb F_2\) indicate that the edge \(uv\in E(H)\) is selected, and define \(p_v=\sum_{e\ni v}x_e\in\mathbb F_2\), the parity of the selected base degree at \(v\). The closed neighborhood in the line graph of \(uv\) consists of all edges incident to \(u\) or \(v\). Its selected parity is \(p_u+p_v+x_{uv}\), because the center edge appears twice in the sum and must be counted once. Therefore the odd-domination constraint at every edge is equivalent to
\[
  x_{uv}=1+p_u+p_v\qquad(uv\in E(H)).\tag{1}
\]
Consequently a solution selects precisely the base edges whose endpoints carry equal parity labels. More importantly, its labelling \(p\) is recovered uniquely from the selected degrees; arbitrary binary labels are **not** presumed valid.

For a part \(P_i\) of cardinality \(n_i\), set \(r_i=\bigl((a+b+c)-n_i\bigr)\bmod2\), and let \(t_i=\sum_{v\in P_i}p_v\pmod2\). Summing (1) over the edges incident to \(v\in P_i\) and imposing the defining equation for \(p_v\) gives
\[
 (1+r_i)p_v=r_i+\sum_{j\ne i}t_j.\tag{2}
\]
Conversely, if a binary vertex labelling satisfies (2) on each part, (1) defines a selection whose selected-degree parity equals that labelling. Thus (2) is a necessary-and-sufficient finite linear system and the solution-to-labelling map is bijective.

If all three part sizes are even, every \(r_i=0\). Equation (2) makes \(p\) constant on each part, but the part totals \(t_i\) are zero, so every \(p_v=0\). Equation (1) gives the unique full-edge solution.

If all three part sizes are odd, every \(r_i=0\) and each \(p\) is constant on a part, say with values \(u_A,u_B,u_C\). Now \(t_i=u_i\), and (2) is equivalent to \(u_A+u_B+u_C=0\). The four admissible triples are \((0,0,0)\), \((1,1,0)\), \((1,0,1)\), \((0,1,1)\), giving the claimed four edge sets.

Suppose \(a,b\) are odd and \(c\) even. Then \(r_A=r_B=1\), \(r_C=0\). Equation (2) on \(A\) forces \(t_B=1\); on \(B\) it forces \(t_A=1\); on \(C\) it forces \(p_v=t_A+t_B=0\). The vertices carrying label one are precisely an arbitrary odd subset \(X\subseteq A\) and an arbitrary odd subset \(Y\subseteq B\), proving the case classification and the stated weighted enumerator.

Suppose \(a\) odd and \(b,c\) even. Then \(r_A=0\), \(r_B=r_C=1\). Equation (2) forces \(t_B=t_C=1+t_A\), and \(p_v=t_B+t_C=0\) on \(A\), implying \(t_A=0\). Thus \(t_B=t_C=1\), and the label-one vertices are arbitrary odd subsets of \(B\) and \(C\), proving the classification and the second weighted enumerator. Choosing an odd subset of a positive even set always leaves both a selected and an unselected vertex.

It remains to prove all connectivity assertions. Every selected base edge joins two vertices with the same parity label. Therefore the selected edge-induced line graph is the disjoint union of the line graphs of \(H[p^{-1}(0)]\) and \(H[p^{-1}(1)]\), omitting any edgeless pieces. Within either parity class, any nonempty complete multipartite induced subgraph has connected line graph. Hence the entire selection is connected if and only if *at most one* parity class spans a base edge. In the all-even and all-odd cases the explicitly listed selections are respectively the entire connected tripartite line graph and connected complete bipartite line graphs. In the two-odd case, both odd-chosen subsets are nonempty, so the label-one class contains an edge; the label-zero class contains an edge exactly when some vertex of \(A\cup B\) was unchosen (because every vertex of \(C\) is label zero). Thus only \(X=A,Y=B\) yields connectivity. In the one-odd case, odd chosen subsets in both even parts span a label-one edge and leave unchosen vertices in both even parts, spanning a label-zero edge; connectivity is impossible.

Finally, in \(K_{1,2m,2m}\), an edge joining the two even parts corresponds to a line-graph vertex of degree \((2m+1)+(2m+1)-2=4m\), and every other line-graph vertex has degree \((4m)+(2m+1)-2=6m-1\). The number of base edges is \(4m^2+4m\). By the one-odd case there are \(2^{4m-2}\) feasible solutions and no connected one. Line graphs are claw-free: three pairwise nonadjacent neighbors of a selected edge would require three distinct endpoints of that edge. This proves the stated family properties.

## Verification
`verify_direct.cpp` independently enumerates all subsets of line-graph vertices in eleven labelled small complete-tripartite graphs, explicitly testing every closed-neighborhood parity condition and connectedness, and compares both cardinality profiles and connected counts with an independently generated vertex-parity model. Compile with `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct`.

`verify_linear.py` instead constructs each exact closed-neighborhood matrix over \(\mathbb F_2\), solves the affine system by Gauss–Jordan elimination, enumerates its entire solution space, compares the complete weight histogram to the four displayed expressions, and independently checks connectedness on fourteen test graphs, including sizes with 40 line-graph vertices. Run with `python3 verify_linear.py`; no third-party packages are required. Full stdout for both programs is included as `verify_direct_output.txt` and `verify_linear_output.txt`.

Finite computation verifies the concrete examples and cross-checks the implementations; the formulas for **all** positive \(a,b,c\) are established by equations (1) and (2), not by extrapolation from tests.

## Relationship to prior work
Caro and Klostermeyer (2003) introduced and studied odd domination, including examples on complete multipartite host graphs. Caro, Klostermeyer and Yuster (2005) studied the stronger connected variant and determined several graph-family boundaries. Their statements about the complete multipartite **host graph** are not statements about its **line graph**; the inspected full text of the latter addresses a different object than the three-part line-graph parity classification here. Previously reported exact all-set results for triangular graphs \(L(K_n)\) and rectangular rook graphs \(L(K_{m,n})\) treat complete and complete-bipartite bases rather than three nonempty independent parts. Those known results share the general parity-counting method, which is not claimed as new; neither implies the four-regime tripartite connectivity criterion, weight formulas or the unbounded-minimum-degree nonexistence family. Other work on open-neighborhood or odd *coloring* conditions uses a different predicate.

## Limitations
The result concerns only **closed-neighborhood binary odd domination** on line graphs of complete **tripartite** graphs. It does not classify general complete-multipartite bases with four or more parts, other finite fields or ordinary domination. The complete general linear equations hold for all base graphs, but the four-case parametrization uses the tripartite assumption. The computation is finite verification, not proof of the universal theorem; the universal proof is given above. Historical priority cannot be guaranteed: unindexed or inaccessible earlier work could contain equivalent counts or connectedness statements. Independent scholarly audit has not been performed.

## References
1. Y. Caro and W. F. Klostermeyer, *The odd domination number of a graph*, Journal of Combinatorial Mathematics and Combinatorial Computing **44** (2003), 65–83. Public journal issue dated 2003-02-28. https://combinatorialpress.com/jcmcc-articles/volume-044/the-odd-domination-number-of-a-graph/ .
2. Y. Caro, W. F. Klostermeyer and R. Yuster, *Connected odd dominating sets in graphs*, Discussiones Mathematicae Graph Theory **25** (2005), 225–239. DOI:10.7151/DMGT.1276. https://geodesic.mathdoc.fr/item/DMGT_2005_25_3_a0/ .
3. *Odd-dominating edge cuts and the exact connectivity premium on triangular graphs*, published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-odd-dominating-edge-cuts-and-the-exact-connectivity-premium-on-t--4ceee51a3626 .
4. *Parity-rectangle classification and odd-domination weight enumerator of rectangular rook graphs*, published mathematical research record. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-parity-rectangle-classification-and-odd-domination-weight-enumer--9d5d63966d08 .
