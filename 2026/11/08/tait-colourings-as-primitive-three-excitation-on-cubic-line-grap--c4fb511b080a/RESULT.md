# Tait colourings as primitive-three excitation on cubic line graphs, with a constant-six seam law

## Finding
Let \(H\) be a finite connected simple cubic graph, \(L(H)\) its line graph, and \(U\) the synchronous three-state Greenberg–Hastings update with contact threshold two on \(L(H)\). A resting vertex (state 0) advances to state 1 precisely when at least two of its neighbors have state 1; states 1 and 2 advance unconditionally to 2 and 0, respectively. The vertices of \(L(H)\) are the individually labelled edges of \(H\). Define \(P_3(H)=\#\{x\in\{0,1,2\}^{E(H)}:U^3x=x,\ Ux\ne x\}\).

**General line-graph theorem.** The initially period-three configurations are *exactly* the proper three-edge-colourings of \(H\), with the three edge colours identified with states 0, 1, and 2. In particular, \(\#\operatorname{Fix}(U^3)=1+P_3(H)\), and \(P_3(H)>0\) if and only if \(H\) has chromatic index three. There are \(P_3(H)/3\) distinct primitive-three temporal orbits. This statement concerns periods dividing three, not the full eventual dynamics.

**Twisted-seam exact census.** For \(n\ge3\), denote by \(\Pi_n=C_n\square K_2\) the ordinary cubic prism and by \(\mathcal M_n\) its twisted-seam counterpart (the standard Möbius ladder with \(2n\) vertices). Under the same dynamics on their line graphs,
\[
\begin{aligned}
P_3(\Pi_n)&=2^n+3+5(-1)^n,\\
P_3(\mathcal M_n)&=2^n+3-(-1)^n,\\
P_3(\Pi_n)-P_3(\mathcal M_n)&=6(-1)^n.
\end{aligned}
\]
Thus both populations are asymptotic to \(2^n\), yet switching the closing rail connection changes the number by **exactly six**, with sign alternating by parity. Their primitive orbit counts are the displayed numbers divided by three. For \(n=3,4,5,6\), the prism counts are 6, 24, 30, 72 and the Möbius counts are 12, 18, 36, 66.

## Assumptions and scope
All graphs are finite, simple and undirected. \(H\) is connected and every vertex has degree three; therefore \(L(H)\) is connected and 4-regular, and it has \(|E(H)|\) vertices. The update is synchronous, unweighted and uses open neighborhoods. Colour labels are distinct; graph automorphisms and permutations of the three states are **not** quotiented out. A temporal orbit means the cyclic sequence of states under repeated \(U\). No assumption about initial random colourings, attracting basins or transient lengths is imposed.

To define the two ladder families concretely, use vertices \((i,r)\) with \(0\le i<n\) and \(r\in\{0,1\}\). Include each rung \((i,0)(i,1)\) and, for \(0\le i<n-1\), rail edges \((i,r)(i+1,r)\). The two closing rail edges join \((n-1,r)\) to \((0,r)\) for \(\Pi_n\), but to \((0,1-r)\) for \(\mathcal M_n\). For \(n\ge3\) both are simple cubic graphs; the \(n=3\) twisted ladder is \(K_{3,3}\).

## Proof
**1. Every vertex on a three-periodic trajectory is resting forever or rotates every update.** Suppose \(U^3x=x\). At an individual vertex, states 1 and 2 must move 1-to-2-to-0. To return after three updates, a vertex ever seen in state 1 or 2 must follow one of the cyclic time shifts of \(0,1,2\); a vertex starting in state 0 either remains 0 for all three times or follows \(0,1,2\). This exhausts all three-step words compatible with the deterministic states 1 and 2. Let \(S\) be the set of rotating vertices, and call the others dormant.

**2. Four-regularity excludes dormant vertices in a nonzero three-cycle.** For each rotating vertex \(v\in S\), the time at which it has state 0 must have at least two neighbors in state 1. Every such neighbor is also rotating (a dormant vertex is always 0). For each edge of the subgraph induced by \(S\), at most one endpoint can count the other as its *successor* in the three-phase cycle: endpoints of equal phase contribute neither way, while different phases determine a unique cyclic direction. Therefore
\[
2|S|\le\sum_{v\in S}\#\{w\sim v:w\text{ has successor phase to }v\}\le |E(L(H)[S])|\le2|S|.
\]
All three inequalities are equalities. Equality at the right means every vertex in \(S\) has all four neighbors inside \(S\); connectivity makes either \(S=\varnothing\) or \(S=V(L(H))\). If \(S=\varnothing\), the state is all zero and fixed. Otherwise equality throughout forces every adjacent pair in \(L(H)\) to have *different* initial phases and every vertex to have precisely two neighbors of the successor phase. Hence the initial states give a proper three-vertex-colouring of \(L(H)\), equivalently a proper three-edge-colouring of \(H\).

**3. Every proper three-edge-colouring is a primitive three-cycle.** In a proper three-edge-colouring of cubic \(H\), the three edges meeting at each vertex have one of each colour. Fix an edge \(e=uv\) in colour \(i\). At each of \(u\) and \(v\), precisely one other edge has colour \(i+1\pmod3\), so the corresponding vertex of \(L(H)\) has exactly two neighbors of colour \(i+1\). Thus every resting vertex advances, and \(U\) increments *all* labels modulo three. This is a primitive three-cycle. The only fixed configuration is all zero, because states 1 and 2 cannot be fixed. This proves the bijection and orbit count.

**4. A nine-state seam transfer counts the two ladders.** Label the colour of the top and bottom rail edges crossing the gap between columns \(i\) and \(i+1\) by \((a_i,b_i)\in\{0,1,2\}^2\). At a column, the rung colour must be the unique colour absent from both \(\{a_{i-1},a_i\}\) and \(\{b_{i-1},b_i\}\); the three incident edge colours at each endpoint must be distinct. Hence a transition \((a,b)\to(c,d)\) is allowed exactly when \(a\ne c\), \(b\ne d\), and \(\{a,c\}=\{b,d\}\). For \(a=b\), necessarily \(c=d\ne a\); the three diagonal states are connected like the proper-colouring transition on a triangle of symbols. For \(a\ne b\), the next state must be the swap \((b,a)\); these six off-diagonal states form three 2-cycles. Every allowed transition has one and only one compatible rung colour, so no multiplicities are omitted.

The number of closed walks of length \(n\) within the diagonal states is the number of proper colourings of a labelled \(n\)-cycle with three colours, namely \(2^n+2(-1)^n\). An ordinary seam requires the final state to equal the first, so an off-diagonal walk closes precisely when \(n\) is even, contributing six in that case. A twisted seam instead requires the final state to be the swap of the first, so the off-diagonal walks contribute six precisely when \(n\) is odd; the diagonal contribution is unchanged. Therefore
\[
\begin{aligned}
P_3(\Pi_n)&=2^n+2(-1)^n+6\mathbf1_{2\mid n},\\
P_3(\mathcal M_n)&=2^n+2(-1)^n+6\mathbf1_{2\nmid n},
\end{aligned}
\]
which simplifies to the two stated expressions and their signed constant-six difference. This argument holds for every integer \(n\ge3\), without relying on finite enumeration.

## Verification
Standalone `check_core.py` constructs both graph families, generates their simple line graphs, enumerates exact proper three-edge-colourings independently for \(3\le n\le10\), and directly tests every initial three-state configuration for \(n=3,4\) by applying the synchronous update three times. All comparisons match the formulas. Direct simulations use at most twelve line-graph vertices; no finite test is claimed to establish the all-\(n\) result.

Separately, `check_transfer.py` builds the stated nine-state transfer and the rail-swap matrix from their definitions. It checks the straight and twisted trace formulas for every \(3\le n\le20\) using ordinary integer matrix multiplication. Captured output files give the actual successful runs. Both checks are auxiliary to the self-contained combinatorial proof above.

## Relationship to prior work
The Greenberg–Hastings excitable rule and its use for threshold/contact oscillations originate in classic excitable-media work; Durrett and Griffeath's March 22, 1993 preprint studies threshold-dependent excitable cellular automata. Bello and Sivakoff (arXiv:2108.06404) study higher contact thresholds on **infinite regular trees**, proving almost-sure fluctuation/fixation results; the inspected theorems and discussion do not give a finite cubic-line-graph three-cycle/edge-colouring bijection or seam enumerators. The graph-theoretic notions of Tait three-edge-colourings, cubic class-one graphs and the Möbius/prism ladders are classical, not newly defined here. Lekshmi and West (arXiv:2003.09602) enumerate **perfect matchings** on prisms and Möbius ladders. A perfect-matching count does not itself count proper three-edge-colourings, which additionally require a compatible two-colouring of every complementary 2-factor. The new claim is the exact *dynamical identification* across all connected cubic bases and the exact period-three seam census. Accessible historical claims involving threshold-two excitation on complete bipartite graphs and threshold-one excitation on cubic ladders do not imply this different graph family and update rule.

## Limitations
This theorem classifies only initially fixed or primitive-three states on these line graphs. It says nothing about other possible periodic lengths, transient times, or the number of initial configurations eventually attracted to these cycles. Existing graph-colouring results may furnish alternative derivations of the ladder counts, and unindexed literature might contain an equivalent dynamical correspondence. The complete 1993 historical primary article and the complete 2020 perfect-matching paper were not available for detailed full-text comparison in this investigation; these are priority risks, not proof gaps. The verification computations cover only the stated finite ranges; independent validation has not been performed.

## References
1. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, first preprint March 22, 1993, https://arxiv.org/abs/patt-sol/9303002.
2. J. Bello and D. Sivakoff, *Cyclic Cellular Automata and Greenberg–Hastings Models on Regular Trees*, arXiv:2108.06404, https://arxiv.org/abs/2108.06404.
3. R. S. Lekshmi and D. B. West, *The Number of Perfect Matchings in Möbius Ladders and Prisms*, arXiv:2003.09602, https://arxiv.org/abs/2003.09602.
4. J. Goedgebeur and P. R. J. Östergård, *Switching 3-edge-colorings of cubic graphs*, Discrete Mathematics 345 (2022), accessible bibliographic summary https://biblio.ugent.be/publication/01GR1E0CVVT21B5QYNNX5MHEET.
