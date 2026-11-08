# Frozen, cyclic, and four-regular maximum-packing reconfiguration on squares of cycles

## Finding

Let \(G_N=C_N^2\) be the square of the cycle of order \(N\ge6\): the vertices are \(\mathbb Z/N\mathbb Z\), and two distinct vertices are adjacent when their shortest cyclic separation is one or two. Let \(\mathcal R_N\) be the simple graph whose vertices are maximum independent sets of \(G_N\) and where two sets are adjacent when one is obtained from the other by moving a selected vertex along an edge of \(G_N\), preserving independence. Write \(N=3m+s\), with \(m=\lfloor N/3\rfloor\) and \(s\in\{0,1,2\}\).

**Theorem.** The independence number is \(m\). The entire maximum-set token-sliding graph has the following properties:

* For \(s=0\), \(\mathcal R_N\cong3K_1\): three isolated states and no edges.
* For \(s=1\), \(\mathcal R_N\cong C_N\): one cycle on \(N\) states, with \(N\) edges and no triangles.
* For \(s=2\), \(\mathcal R_N\) is connected and four-regular, has \(N(m+1)/2\) states, \(N(m+1)\) edges, and exactly \(N\) triangles.

When \(s=2\) and \(m\ge3\), the numbers of states lying in precisely two, one, and zero triangles are respectively \(N\), \(N\), and \(N(m-3)/2\). In particular, these connected four-regular graphs are not vertex-transitive. When \(N=8\) (so \(m=2\)), each of the twelve states belongs to two triangles.

The three cases describe a sharp transition in the mobility of densest distance-three packings on a ring: zero spare positions freezes all packings, one spare position gives a single cycle, and two spare positions produce a connected four-regular triangle-bearing graph.

## Assumptions and scope

All graphs are finite, simple and undirected. Index calculations are modulo \(N\). A token-slide moves one token from vertex \(u\) to a different vertex \(v\) with circular separation one or two, and is legal only when the new \(m\)-set is independent. Tokens are indistinguishable. A triangle means an unordered three-vertex clique of \(\mathcal R_N\). The conclusions apply to every integer \(N\ge6\); in particular, the exceptional order \(N=8\) is included.

## Proof

**1. Cyclic gap parametrization and state count.** An independent subset of \(C_N^2\) has cyclic gaps between successive selected vertices at least three. Thus if it contains \(k\) vertices, then \(N\ge3k\). Taking vertices in cyclic steps of three shows \(\alpha(G_N)=m\). In a maximum set, write the \(m\) gaps in cyclic order as \(d_i=3+e_i\), with nonnegative integers \(e_i\) summing to \(s=N-3m\). Conversely any such cyclic list and a starting occupied vertex \(a\) gives an independent maximum set. A state is therefore represented by \((a,e_1,\ldots,e_m)\), modulo changing which of its \(m\) occupied vertices is designated first: \((a,e_1,\ldots,e_m)\sim(a+3+e_1,e_2,\ldots,e_m,e_1)\). This is an equivalence of representations, not a quotient of the underlying labelled graph: the actual vertices remain labelled by \(\mathbb Z/N\mathbb Z\). Counting the \(N\binom{m+s-1}{s}\) rooted representations and dividing by the exactly \(m\) choices of distinguished occupied vertex per state gives
\[
|V(\mathcal R_N)|=\frac Nm\binom{m+s-1}{s}.
\]
Consequently the three state counts are \(3\), \(N\), and \(N(m+1)/2\).

**2. Legal moves as transfers of slack.** Moving a selected vertex clockwise by \(t\in\{1,2\}\) decreases the following gap by \(t\) and increases the preceding gap by \(t\). It is legal if and only if the following gap has at least \(t\) units of slack. The reverse move transfers the same amount in the opposite direction. Thus the complete transition rule is the transfer of one or two slack units between two adjacent gaps. There are no other legal slides. This also proves that the representation is an exact combinatorial model of the full reconfiguration graph.

**3. Zero or one slack unit.** If \(s=0\), every gap is three and no transfer is possible. If \(s=1\), a state has a unique gap four and all other gaps three. Exactly the two endpoint vertices of that gap can slide inward by one step; the resulting state again has a unique gap four. Label a state by the starting vertex \(a\in\mathbb Z/N\mathbb Z\) of its unique long gap. Its two neighbors are labelled \(a-3\) and \(a+3\). Because \(N=3m+1\), the integer three is invertible modulo \(N\); hence these adjacencies form precisely one cycle of length \(N\).

**4. Two slack units: degrees and connectivity.** When \(s=2\), either one gap has length five or two distinct gaps have length four. In the first case, either endpoint of the length-five gap can slide inward by one or two vertices, giving four distinct neighbors. In the second, either endpoint transfer at each of the two length-four gaps provides one slide; these are again four distinct neighbors, including for \(m=2\). Thus \(\mathcal R_N\) is four-regular, and the handshaking lemma gives \(N(m+1)\) edges.

It remains to prove connectivity. Any pattern with two length-four gaps can move one of its unit slack defects around the cyclic list of gaps, transferring it one step at a time, until the two units occupy the same gap. Hence every state reaches a state with a unique length-five gap. Label the latter state \(H_a\) by the starting vertex \(a\) of that gap. A slide of the appropriate endpoint through two cyclic positions moves \(H_a\) to \(H_{a+3}\), and the reverse slide moves it to \(H_{a-3}\). Since \(\gcd(N,3)=1\) when \(N=3m+2\), all \(H_a\) lie in one component. Therefore the entire reconfiguration graph is connected.

**5. Exact triangle count.** Consider any triangle formed by three distinct maximum independent sets, pairwise differing by one token. An elementary set-theoretic classification of triangles in the Johnson graph says that such a triple either has a common \((m-1)\)-subset or consists of three distinct \(m\)-subsets of one \((m+1)\)-set. The latter alternative is impossible here: every pair of elements of that \((m+1)\)-set belongs to at least one of the three independent states, so their union would be an independent set larger than \(\alpha(G_N)=m\). Consequently the three states have \(m-1\) fixed tokens and one moving token, occupying three pairwise adjacent vertices of \(G_N\).

For \(N=3m+2\ge8\), every triangle in \(G_N\) consists of three cyclically consecutive vertices \(\{i,i+1,i+2\}\). A fixed token must be at cyclic distance at least three from all three positions, so all fixed tokens must lie in the path interval \(\{i+5,i+6,\ldots,i+N-3\}\), containing exactly \(N-7=3m-5\) vertices. Packing \(m-1\) mutually separated fixed tokens into this interval forces the unique set \(\{i+5,i+8,\ldots,i+N-3\}\). For each \(i\), these fixed tokens together with each of \(i,i+1,i+2\) form three mutually adjacent maximum sets and therefore one triangle in \(\mathcal R_N\). Different \(i\) give different moving triples and hence different triangles. There are exactly \(N\) triangles.

**6. Triangle incidences.** For \(m\ge3\), a state with one gap of length five lies in exactly two of the above triangles, corresponding to its two movable end positions. There are exactly \(N\) such states, one for each starting vertex of the length-five gap. A state with two length-four gaps lies in a triangle exactly when those two gaps are consecutive in cyclic gap order; in that case the triangle is unique. There are exactly \(N\) states of this adjacent-gap kind for \(m\ge3\), obtainable by choosing the middle token; the remaining \(N(m+1)/2-2N=N(m-3)/2\) states lie in no triangles. Since the triangle incidences are not constant, these graphs are not vertex-transitive. At \(m=2\), the two length-four gaps are consecutive in both cyclic directions, so all twelve states instead have triangle incidence two. This proves every asserted formula. \(\square\)

## Verification

Two standalone verifiers implement the state and edge definitions differently. Run `python3 verification/verify_gaps.py` to reconstruct cyclic gap states and all allowed slides for every \(6\le N\le74\), testing state totals, degrees, components, edge counts, triangles, and (for two slack units) per-state triangle incidence. Run `g++ -std=c++17 -O2 verification/verify_direct.cpp -o verify_direct && ./verify_direct` to independently enumerate all independent \(m\)-subsets, generate moves by direct vertex replacements, and test the same global invariants for \(6\le N\le26\). Both programs completed with terminating messages `GAP_RECONSTRUCTION_PASS` and `DIRECT_ENUMERATION_PASS`. The all-order proof above, rather than the finite experiments, establishes the theorem for arbitrarily large \(N\).

## Relationship to prior work

Bonsma, Kamiński and Wrochna introduced major algorithmic results for independent-set reconfiguration in claw-free graphs and proved that token-jumping and token-sliding adjacency coincide for maximum independent sets (Proposition 1 of arXiv:1403.0359). Their reachability algorithm does not enumerate the maximum-set reconfiguration graph of \(C_N^2\) or its triangle-incidence spectrum. Bonamy and Bousquet treated interval and chordal graph reconfiguration in arXiv:1605.00442, without this nonchordal family. Avis and Hoang (arXiv:2203.16861) studied graph structure of token-sliding solution graphs, including underlying paths and cycles; its results on \(C_N\) do not determine the graph for its square \(C_N^2\). Hoang (arXiv:2208.07199) studied distance-\(d\) independent-set reconfiguration; using a distance-three packing of the underlying cycle with one-step slides is not the same move graph as token sliding along both one- and two-step edges of \(C_N^2\). None of these inspected results implies the present full modular classification, degree sequence and triangle counts.

## Limitations

The theorem concerns only *maximum* independent sets, only square powers of ordinary finite cycles, and exactly the stated token-slide rule. It does not classify smaller independent sets or the diameters of the four-regular cases. The listed publications and accessible discovery records do not establish a claim of absolute historical priority: an equivalent unindexed calculation is a residual risk. Independent scholarly audit has not been performed.

## References

1. P. Bonsma, M. Kamiński, M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (first posted 2014-03-03), https://arxiv.org/abs/1403.0359 .
2. M. Bonamy, N. Bousquet, *Token Sliding on Chordal Graphs*, arXiv:1605.00442 (2016), https://arxiv.org/abs/1605.00442 .
3. D. Avis, D. A. Hoang, *On Reconfiguration Graphs of Independent Sets under Token Sliding*, arXiv:2203.16861 (2022), https://arxiv.org/abs/2203.16861 .
4. D. A. Hoang, *On the Complexity of Distance-d Independent Set Reconfiguration*, arXiv:2208.07199 (2022), https://arxiv.org/abs/2208.07199 .
