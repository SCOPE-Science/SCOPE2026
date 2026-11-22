# Two and only two shortest-consensus edge topologies on eight agents: the cube and Wagner graph

## Finding

Let \(G=(V,E)\) be any finite simple undirected graph with \(V=\{0,\ldots,7\}\). An allowed pairwise averaging contact on \(\{a,b\}\in E\) replaces the two state coordinates by their arithmetic mean and leaves the other coordinates unchanged. Then a product of exactly 12 such contact matrices equals \(J_8/8=\mathbf 1\mathbf 1^{\mathsf T}/8\) **if and only if** \(G\) contains a spanning subgraph isomorphic to either the three-dimensional Boolean cube \(Q_3\) or the Wagner graph \(W_8\), the eight-cycle with four opposite chords. Each successful 12-contact product uses 12 distinct edges, and the support graph is one of precisely these two nonisomorphic, 3-regular graphs.

In particular, the Wagner graph provides a nonbipartite twelve-edge network with exact finite-time symmetric pairwise consensus. It is not a cube-containing graph. Therefore the graph-topology conjecture in Krapivsky and Plakhov [3, Section VII], which predicts that non-cube-containing eight-vertex graphs cannot reach finite-time consensus, is false.

## Assumptions and scope

Arithmetic averaging has fixed coefficients \(1/2,1/2\), not tuned row-stochastic weights. All 12 contacts are sequential single-edge updates; the initial state is arbitrary in \(\mathbb R^8\). For initial states in generic rationally independent position, exact equal opinions imply the full consensus matrix identity; the displayed schedules in fact work for every state. The classification refers to *shortest-time* (12-contact) success. The finite-time reachability of graphs that need more than 12 contacts is not classified here.

Here is a complete 12-event word on the Wagner graph, with vertices indexed modulo eight. Execute the displayed matchings in the indicated order, and the four edges in each matching in any order:

\[
\begin{aligned}
M_1&=\{\{0,4\},\{1,5\},\{2,6\},\{3,7\}\},\\
M_2&=\{\{0,1\},\{2,3\},\{4,5\},\{6,7\}\},\\
M_3&=\{\{0,7\},\{1,2\},\{3,4\},\{5,6\}\}.
\end{aligned}
\]

The first matching pairs antipodes, and the second and third are alternate matchings of the rim 8-cycle. Each final row is the uniform mean of all eight original values. Moreover \(0,1,2,3,4,0\) is a 5-cycle in the union, so this graph is nonbipartite, unlike \(Q_3\).

## Proof

**1. Sharp entropy bound.** Let \(p_v\) be row \(v\) of the current product of averaging matrices. It is a probability vector over the initial eight vertices. Write \(H(p)=-\sum_i p_i\log_2 p_i\), including the convention \(0\log_2 0=0\). Initially \(\sum_v H(p_v)=0\); at consensus its value is \(8\log_2 8=24\). For one contact replacing distributions \(p,q\) by \(r=(p+q)/2\) twice,

\[
2H(r)-H(p)-H(q)=2\,\mathrm{JS}(p,q)\le 2.
\]

The equality case follows by introducing a uniform binary selector \(B\): \(\mathrm{JS}(p,q)=I(B;X)\le H(B)=1\), and equality holds precisely when \(B\) can be recovered from the drawn label \(X\), i.e. the supports of \(p,q\) are disjoint. Thus at least twelve contacts are required and every contact in a successful 12-contact word combines disjoint supports.

**2. Uniform supports and three perfect matchings.** At every such disjoint-support update, the relative probabilities of all preexisting labels within each participating row stay unchanged. Every final row is uniform on the entire eight-element set. Reading back along any one row's update history therefore forces that row to have been uniform on its support at every intermediate time. When two rows uniform on disjoint supports of respective cardinalities \(a,b\) are averaged, their common output is uniform precisely when \(a=b\). Consequently each contact doubles both support cardinalities. Every vertex begins with a one-element support and ends with an eight-element support, so each vertex participates once in a \(1\to2\) contact, once in a \(2\to4\) contact and once in a \(4\to8\) contact. Contacts at different levels can be reordered by commuting those with disjoint endpoints, so every shortest word is equivalent for the matrix product and edge support to three consecutive perfect matchings \(M_1,M_2,M_3\). Supports are disjoint at their respective contacts. These matchings are pairwise edge-disjoint and their union is a 3-regular simple graph with 12 edges.

**3. Exhaustive, reduced finite classification.** Relabel so that \(M_1=\{01,23,45,67\}\). The second matching must pair vertices from distinct first-stage two-element blocks. There are exactly 60 such second matchings. The 2-regular graph \(M_1\cup M_2\) has either two four-cycle components (12 choices of \(M_2\)) or one eight-cycle (48 choices). For each second matching, form the four-element support of each vertex; the third matching must join vertices with disjoint four-element supports. These are exactly four pairs of complementary supports, so this condition exhausts all admissible third matchings.

The standalone `verify.py` enumerates all 105 perfect matchings (no graph-generator dependency), filters each by the stated support-disjointness predicate, and checks every 12-edge union by an independent adjacency-preserving bijection search against explicit cube and Wagner models. For the fixed \(M_1\), it finds 480 ordered pairs \((M_2,M_3)\): exactly 144 produce \(Q_3\), exactly 336 produce \(W_8\), and zero yield any other isomorphism type. Those finite loops are exhaustive because each recursively generated matching pairs the least remaining vertex with every possible partner. The entire finite classification thus follows; no sampling or heuristic graph enumeration is used. Both isomorphism types admit valid schedules, as confirmed algebraically by the exact averaging words in the verifier. This proves necessity and sufficiency.

**4. Consequence for a fixed stochastic contact graph.** If each allowed edge has positive independent selection probability at each step, the explicit twelve-contact Wagner word occurs with strictly positive probability in any prescribed 12-contact block. Repeating disjoint blocks gives almost-sure occurrence eventually, and a successful block sends every preceding state to the global mean because the contact matrices are doubly stochastic. This shows finite-time consensus almost surely on a graph with no cube subgraph.

## Verification

Run `python3 verify.py` using only the Python 3 standard library. It independently checks exact integer representations (each row scaled by eight), the complete filtered perfect-matching census, eight-vertex graph-isomorphism tests, the stated nonbipartite 5-cycle, and both explicit schedules. Expected printed final counts: 12 versus 48 second-stage cases and 144 versus 336 cubic support types, with zero other types. The finite search proves the reduced finite classification only; the entropy equality and canonical-stage reduction are established analytically above.

## Relationship to prior work

Shi, Li, M. Johansson and K. H. Johansson [1] prove the sharp 12-contact lower bound for eight agents and construct the cube schedule. They explicitly ask whether equally fast symmetric algorithms other than their cube-based algorithm exist, proving only the four-agent uniqueness statement. Their theorem does not classify the eight-agent contact supports. Hendrickx, Shi and K. H. Johansson [2] study general positive-diagonal stochastic matrices with adjustable weights, rather than fixed equal-weight pairwise averages. Krapivsky and Plakhov [3, Section VII] state the much stronger conjecture that all eight-agent networks with finite-time consensus must contain a cube; the Wagner word is a constructive counterexample. The current assertion is a classification of **shortest** edge supports, not of all finite-time feasible graphs.

## Limitations

No full classification is claimed for networks whose shortest successful words are longer than twelve contacts; in particular inclusion-minimality of the Wagner graph among *all* finite-time consensus networks has not been established. This result is about exact arithmetic and pointwise finite-time equality, not floating-point stability or mixing-time optimality. Bibliographic discovery does not rule out all unindexed earlier equivalent classifications. An independent mathematical audit has not been performed.

## References

1. G. Shi, B. Li, M. Johansson and K. H. Johansson, *Finite-time Convergent Gossiping*, arXiv:1206.0992 (first public 2012-06-05). https://arxiv.org/abs/1206.0992
2. J. M. Hendrickx, G. Shi and K. H. Johansson, *Finite-time consensus using stochastic matrices with positive diagonals*, arXiv:1302.6668 (2013). https://arxiv.org/abs/1302.6668
3. P. L. Krapivsky and A. Yu. Plakhov, *Finite-time consensus in a compromise process*, arXiv:2509.01024 (2025), Section VII. https://arxiv.org/abs/2509.01024
