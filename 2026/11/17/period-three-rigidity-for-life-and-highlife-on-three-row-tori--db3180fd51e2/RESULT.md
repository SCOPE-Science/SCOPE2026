# Period-three rigidity for Life and HighLife on three-row tori

## Finding
Let \(F_{R,n}\) be the synchronous Moore-neighborhood cellular automaton on the indexed torus \(\mathbb Z_3\times\mathbb Z_n\), with \(n\ge3\), under either Conway Life \(R=\mathrm{B3/S23}\) or HighLife \(R=\mathrm{B36/S23}\). Then
\[
\operatorname{Fix}(F_{R,n}^{3})=\operatorname{Fix}(F_{R,n})\qquad(n\ge3).
\]
Equivalently, neither rule has a configuration of least temporal period three on any such torus. Both rules have the same 57 recurrent *vertices* in the three-layer column-history transfer graph, all of which are constant in time. This does **not** assert that the two rules have identical sets of fixed configurations: the allowable transitions between the recurrent vertices can differ.

## Assumptions and scope
Each site is binary, and each of the eight offsets \((\delta r,\delta c)\in\{-1,0,1\}^2\setminus\{(0,0)\}\) contributes one neighbor to its update. For \(n\ge3\), all eight neighbors are distinct. A living cell survives at exactly two or three living neighbors; a dead cell becomes alive at exactly three, and also at six for HighLife. Spatial positions and temporal phases are labelled; no spatial symmetry quotient is taken. The equality concerns only third iterates and does not classify other temporal periods, transients, or larger heights.

## Proof
For any three-bit column \(b\in\{0,\ldots,7\}\), write \(\mathcal L_R(a,b,c)\in\{0,\ldots,7\}\) for its synchronous successor when the preceding, present and following spatial columns are \(a,b,c\). At row \(r\in\mathbb Z_3\), the neighbor count is
\[
N_r(a,b,c)=\sum_{j=0}^{2}(a_j+c_j)+\sum_{j\ne r}b_j.
\]
The new bit is one if and only if \((b_r=1\wedge N_r\in\{2,3\})\) or \((b_r=0\wedge N_r\in B_R)\), with \(B_{\mathrm{Life}}=\{3\}\) and \(B_{\mathrm{HighLife}}=\{3,6\}\). This determines \(\mathcal L_R\) for all \(8^3=512\) triples, without approximation.

Encode a three-periodic temporal history at one spatial column by \(A=(a^{(0)},a^{(1)},a^{(2)})\in\{0,\ldots,7\}^3\), packed as an integer from zero through 511. Construct the directed graph \(G_R\) whose \(512^2=262144\) vertices are ordered column-history pairs \((A,B)\). Include \((A,B)\to(B,C)\) precisely when, for each \(t\in\mathbb Z_3\),
\[
b^{(t+1)}=\mathcal L_R(a^{(t)},b^{(t)},c^{(t)}).
\]
The superscripts are interpreted modulo three. For every \(n\ge3\), a length-\(n\) closed directed walk in \(G_R\) corresponds bijectively to a configuration \(x\) satisfying \(F_{R,n}^3(x)=x\): the three time slices supply the entire global trajectory, with the closure enforcing spatial periodicity, and the local conditions enforce all three updates. Conversely a third-iterate fixed state supplies such a walk. This is an infinite-family equivalence, not a bounded simulation argument.

**Finite transfer-graph lemma.** The fully enumerated graphs have exactly 294072 edges for Life and 321875 for HighLife. In each graph, exactly two nontrivial strongly connected components exist, of sizes 30 and 27, and no singleton component with a self-loop exists. Their union comprises exactly 57 vertices, identical between the two rules. On every one of those vertices \((A,B)\), each of \(A\) and \(B\) has three identical time slices. The exhaustive construction and iterative strongly-connected-component algorithm are contained in `space_time_graph.cpp`. An independently implemented Python/NetworkX construction (`independent_graph.py`) reproduces these exact counts, component sizes, and absence of time-varying recurrent vertices. Both sources enumerate all 262144 graph vertices, not a sampling of them.

Every closed directed walk is contained entirely in a strongly connected component which contains a cycle. By the finite lemma, every column-history along a closed walk is constant across its three temporal slices. Hence every \(x\in\operatorname{Fix}(F_{R,n}^3)\) is unchanged after the first update. The reverse inclusion holds trivially. This establishes the claimed equality for both rules and every \(n\ge3\).

## Verification
Compile `space_time_graph.cpp` using `c++ -O3 -std=c++17 -o graph space_time_graph.cpp`, then run `./graph`; the exact expected output is `graph_output.txt`. The script checks the two component sizes, edge counts, absence of time-varying cyclic vertices, and equality of the two recurrent vertex sets. Separately run `python independent_graph.py` with NetworkX 3.x; its output is `independent_graph_output.txt` and it uses a different implementation of local neighborhoods and strongly connected components. Finally compile `direct_evolution.cpp` using `c++ -O3 -std=c++17 -o direct direct_evolution.cpp` and run `./direct`; `direct_output.txt` records exhaustive state-by-state evolution for both rules at circumferences 3 through 7. The last test is a finite cross-check, not the reason the theorem holds for all sizes.

## Relationship to prior work
Life and HighLife both possess nontrivial oscillations on the unrestricted plane; for example, Life's classical pulsar has temporal period three. Eppstein's `Growth and Decay in Life-Like Cellular Automata`, arXiv:0911.2890v1 (15 November 2009), explains both rules and planar oscillator behavior, but does not give the all-circumference three-row period-three exclusion. Eppstein's HighLife replicator catalogue discusses large-period oscillators and related dynamics rather than this finite-width constraint. An earlier exact fixed-configuration and primitive-period-two analysis on three-row Life tori and an earlier fixed-configuration comparison between Life and HighLife supply different temporal information; neither implies the third-iterate equality. The present result is a temporal rigidity theorem, not another fixed-state enumeration.

## Limitations
The rigorous infinite-circumference conclusion rests on a reproducible exhaustive calculation on a finite transfer graph, rather than a short human-only case classification. This does not prove an odd-period exclusion beyond three, a minimal spatial width for period-three oscillators, or anything about infinite-plane stability or transients. Public catalogues of Life-like oscillators are extensive; unidentified prior thin-torus investigations remain a historical-priority risk. The cited early HighLife catalogue's underlying Bell ZIP was unavailable in material form during this comparison. No independent external mathematical audit has been performed.

## References
1. D. Eppstein, *Growth and Decay in Life-Like Cellular Automata*, arXiv:0911.2890v1, submitted 2009-11-15, https://arxiv.org/html/0911.2890v1 .
2. D. Eppstein, *Replicators: B36/S23 (HighLife)*, https://ics.uci.edu/~eppstein/ca/replicators/b36s23.html .
3. *Pulsar*, LifeWiki, https://conwaylife.com/wiki/Pulsar (relevant pattern catalogue; full page was not retrievable during inspection).
4. *Small period-3 oscillators*, LifeWiki, https://conwaylife.com/wiki/Small_period-3_oscillators (catalogue search result; full page was not retrievable during inspection).
