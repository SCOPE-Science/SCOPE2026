# Two and only two shortest-consensus edge topologies on eight agents: the cube and Wagner graph

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph with \(V=\{0,\ldots,7\}\). An allowed pairwise averaging contact on \(\{a,b\}\in E\) replaces the two state coordinates by their arithmetic mean and leaves the other coordinates unchanged. A product of exactly 12 such contact matrices equals \(J_8/8=\mathbf 1\mathbf 1^{\mathsf T}/8\) if and only if \(G\) contains a spanning subgraph isomorphic to either the three-dimensional Boolean cube \(Q_3\) or the Wagner graph \(W_8\), the eight-cycle with four opposite chords. Each successful 12-contact product uses 12 distinct edges, and its support is one of these two nonisomorphic 3-regular graphs.

The Wagner graph thus supplies a nonbipartite network with exact finite-time symmetric pairwise consensus. It contains no cube, so it refutes the cube-necessity conjecture of Krapivsky and Plakhov [3, Section VII].

## Assumptions and scope

All contacts are sequential single-edge updates with fixed coefficients \(1/2,1/2\), and the initial state is arbitrary in \(\mathbb R^8\). For initial states whose coordinates are rationally independent, equality of all final opinions also implies the full consensus matrix identity. The classification is about shortest-time success; it does not classify graphs that require more than 12 contacts.

For a Wagner word, label vertices modulo eight and execute each matching in sequence, in any order within each matching:

\[
\begin{aligned}
M_1&=\{\{0,4\},\{1,5\},\{2,6\},\{3,7\}\},\\
M_2&=\{\{0,1\},\{2,3\},\{4,5\},\{6,7\}\},\\
M_3&=\{\{0,7\},\{1,2\},\{3,4\},\{5,6\}\}.
\end{aligned}
\]

The first matching pairs antipodes. After the second matching, rows at \(0,1,4,5\) are uniform on \(\{0,1,4,5\}\), and the other rows are uniform on the complementary set. All third-stage contacts join these complementary supports. The cycle \(0,1,2,3,4,0\) certifies nonbipartiteness. Since the Wagner graph has the same 12 edges as the cube in number, a cube subgraph would have to be the entire graph, which is impossible.

## Proof

**1. Sharp entropy bound.** Let \(p_v\) be row \(v\) of the current product of averaging matrices. It is a probability vector over the eight initial vertices. Write \(H(p)=-\sum_i p_i\log_2p_i\), with \(0\log_2 0=0\). Initially \(\sum_v H(p_v)=0\); at consensus it is \(8\log_2 8=24\). A contact replaces distributions \(p,q\) by two copies of \(r=(p+q)/2\), so the increase is
\[
2H(r)-H(p)-H(q)=2I(B;X)\le2,
\]
where \(B\) is the fair binary selector of the distribution from which \(X\) is drawn. Equality holds exactly when \(B\) is determined by \(X\), i.e., when the supports of \(p,q\) are disjoint. Thus at least 12 contacts are required, and every contact in a successful 12-contact word joins disjoint supports.

**2. Uniform supports and three perfect matchings.** Under a disjoint-support contact, each positive weight already in either participating row is multiplied by \(1/2\), with no label lost. The ratios of those weights are preserved in all later updates of that row. Therefore uniformity at the end implies uniformity at every earlier time. Averaging two rows uniform on disjoint sets yields a uniform output only if those sets have the same size. Each participating row therefore doubles its support at each update, so each vertex must participate once at each input size 1, 2 and 4. The contacts of a given size form a perfect matching. An out-of-order adjacent pair of contacts at distinct sizes cannot share an endpoint, because the sizes in each vertex's own history increase; hence these contacts commute. This sorts the word into three successive matchings without changing its product or support. No edge repeats: once its endpoints contact, their supports share labels that can never be lost. The union is a simple cubic graph with 12 edges.

**3. Exhaustive finite classification.** Relabel the first matching as \(M_1=\{01,23,45,67\}\). The second matching must join distinct first-stage two-element blocks. The union of \(M_1\) and \(M_2\) is either two four-cycles (12 choices of \(M_2\)) or one eight-cycle (48 choices). In the first case the third matching is any bijection between the two four-vertex groups with complementary supports, yielding 24 choices. In the second case there are four distinct support sets, each held by two vertices, with two complementary pairs of support sets. The third matching chooses a bijection between the two two-vertex groups for each complementary pair, yielding four choices.

The standalone `verify.py` generates all 105 perfect matchings by pairing the least remaining vertex with every possible partner and recursing. It applies the disjoint-support test at both later stages and checks each surviving 12-edge union by adjacency-preserving bijections against explicit cube and Wagner graphs. For the fixed \(M_1\) the 480 ordered pairs \((M_2,M_3)\) split into 144 cube supports and 336 Wagner supports, with no other type (these count schedules, not distinct labeled graphs). Both types admit valid schedules; the Wagner word above and the cube's three coordinate matchings give exact averaging. Necessity and sufficiency follow by relabeling.

**4. Stochastic contact graph.** If contacts sample edges independently from a fixed full-support law, the Wagner word has a fixed positive probability in each successive disjoint 12-contact block. Almost surely some block realizes it. Any successful block sends the state to its original global mean because all prior contacts preserve the sum. In particular this applies in the equal-rate graph model of [3], whose successive contact edges are uniform. Time-varying independent edge laws with merely stepwise full support need not give almost-sure occurrence.

## Verification

Run `python3 verify.py` using only the Python 3 standard library. It checks exact integer representations (each row scaled by eight), generates and filters the perfect-matching census, checks graph isomorphisms on eight vertices, and verifies both displayed types of schedule. Expected counts are 12 versus 48 second-stage cases, and 144 versus 336 cube and Wagner schedules with no other type. The enumeration covers the reduced finite classification; entropy saturation and the stage reduction are proved above.

## Relationship to prior work

Shi, Li, M. Johansson and K. H. Johansson [1] prove the sharp 12-contact lower bound for eight agents (24 endpoint updates) and construct the cube schedule. They discuss essential uniqueness for four agents; they do not classify the optimal eight-agent supports. Hendrickx, Shi and K. H. Johansson [2] treat general stochastic matrices with positive diagonals and adjustable weights, rather than fixed equal-weight pairwise averages. Krapivsky and Plakhov [3, Section VII] conjecture cube necessity for their graph-constrained random process. The Wagner word refutes this necessity, independently of the shortest-support classification. A related computation [4] uses the disjoint equal-size support criterion to count shortest words on the complete graph, rather than classifying the graphs used by those words.

## Limitations

No classification is claimed for networks whose shortest successful words are longer than 12 contacts. The result is about exact arithmetic and finite equality, not floating-point stability or mixing time. The literature comparison does not rule out an unindexed equivalent classification.

## References

1. G. Shi, B. Li, M. Johansson and K. H. Johansson, *Finite-time Convergent Gossiping*, arXiv:1206.0992. https://arxiv.org/abs/1206.0992
2. J. M. Hendrickx, G. Shi and K. H. Johansson, *Finite-time consensus using stochastic matrices with positive diagonals*, arXiv:1302.6668. https://arxiv.org/abs/1302.6668
3. P. L. Krapivsky and A. Yu. Plakhov, *Finite-time consensus in a compromise process*, arXiv:2509.01024, Section VII. https://arxiv.org/abs/2509.01024
4. *Exact twelve-contact consensus probability for eight-agent random gossip*, Resultary record `866678dfa960`. https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-twelve-contact-consensus-probability-for-eight-agent-rando--866678dfa960/RESULT.md
