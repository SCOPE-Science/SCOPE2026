# Four-palette two-homogeneous recolouring of the Heawood graph: 504 seven-vertex trees and 2520 isolated states

## Finding
Let \(H\) be the Heawood graph (the point–line incidence graph of the Fano plane). A named colouring \(c:V(H)\to\{0,1,2,3\}\) is **two-homogeneous** when it is proper and every open neighbourhood has exactly two distinct colours. Let \(\mathcal R\) have all these colourings as vertices, with edges corresponding to a change at exactly one graph vertex that preserves both requirements. Then
\[
\boxed{\mathcal R\cong 2520K_1\;\sqcup\;504T_7,}
\]
where \(T_7\) is the tree obtained by joining the centres of two copies of \(K_{1,2}\) with a path of two edges; equivalently, its degree multiset is \(\{3,3,2,1,1,1,1\}\). There are exactly \(6048\) named valid colourings: \(504\) use three distinct colours and \(5544\) use all four. Every \(T_7\) component contains precisely one three-colour state, and all isolated states use four colours. The complete degree enumerator is
\[
2520+2016t+504t^2+1008t^3.
\]
There are exactly \(3024\) reconfiguration edges, no nontrivial cycles, and \(3024\) connected components.

## Assumptions and scope
Label points \(P_i\) and lines \(L_j\), with \(i,j\in\mathbb Z/7\mathbb Z\), where \(P_i\sim L_j\) precisely if \(i\in\{j,j+1,j+3\}\pmod7\). Every vertex has three neighbours. Colours are **named**; unused colours are allowed; the vertex set of \(\mathcal R\) contains no improper or non-two-homogeneous states. The only allowed move changes a single vertex colour. In particular, this is not the graph of *all* proper four-colourings.

## Proof
**Fano-side rigidity.** Restrict a valid colouring to its seven point vertices. Every Fano line contains precisely two point colours. A bichromatic triple has exactly one equal-coloured pair; every unordered pair of Fano points belongs to exactly one line. If the four point-colour multiplicities are \(a_0,a_1,a_2,a_3\), then
\[
\sum_{i=0}^{3}a_i=7,\qquad \sum_{i=0}^{3}\binom{a_i}{2}=7.
\]
The unique unordered nonnegative integer solution is \(\{4,2,1,0\}\). Write \(P\) for the singleton-colour point and \(Q,R\) for the pair-colour points. The triple \(P,Q,R\) lies on a Fano line: otherwise the line through \(P,Q\) has one point from each of the three used classes, contradicting bichromaticity. The four points outside that line share the third colour. Thus one shore is determined by a Fano incidence flag (\(21\) choices) and an ordered triple of distinct names from the four-colour palette (\(24\) choices). Each of the \(504\) choices satisfies the line-bichromatic condition. The analogous classification holds for the line shore by incidence duality.

**Twelve exact extensions.** Symmetry permits fixing the point-colour vector, in \(P_0,\ldots,P_6\) order, to \((2,1,0,1,0,0,0)\), with the fourth colour \(3\) unused. Every line sees exactly two of the three used point colours, so properness gives exactly two possible colours for that line: the one missing from \(\{0,1,2\}\), or colour \(3\). The seven canonical missing colours, in \(L_0,\ldots,L_6\) order, are \((0,2,2,2,1,2,1)\). Let bit \(j\) in an integer \(m\in[0,127]\) indicate replacing the canonical colour of \(L_j\) by \(3\). The point-neighbourhood conditions hold exactly for the following twelve masks:
\[
\{0,1,17,23,46,57,65,75,80,92,101,114\}.
\]
This is a finite exhaustive identity: for every mask, check at each point \(P_i\) that the three line colours indexed by \(\{j:i\in\{j,j+1,j+3\}\}\) have exactly two distinct values. The twelve masks and the explicit test are reproduced by `verify.py`. The empty mask uniquely produces a three-colour assignment. Therefore the state counts are \(504\cdot12=6048\), with \(504\) three-colour states and \(504\cdot11=5544\) four-colour states.

**Complete move table.** For the same normalized point assignment, test every one-site recolouring among all four names against properness and the seven point and seven line neighbourhood constraints. The complete degree table for its twelve masks is

| Mask | 0 | 1 | 17 | 23 | 46 | 57 | 65 | 75 | 80 | 92 | 101 | 114 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Degree | 2 | 3 | 1 | 0 | 3 | 0 | 1 | 0 | 0 | 1 | 0 | 1 |

The normalized coloured flag is representative of every point-shore configuration under Fano collineations and palette permutations. Thus the table applies to all \(504\) point assignments. In addition, the local one-vertex tests show that each degree-two vertex is a three-colour state, adjacent to two degree-three vertices; each degree-three vertex has exactly one degree-two neighbour and two degree-one neighbours; each degree-one vertex attaches to a degree-three vertex. There are no other moves. The resulting graph is a disjoint union of seven-vertex trees \(T_7\) and isolated vertices. The degree table gives counts \(504,1008,2016,2520\) at degrees \(2,3,1,0\), respectively. Every tree contains exactly one degree-two vertex, so there are exactly \(504\) trees and \(2520\) isolated states. Each tree has six edges, giving \(3024\) edges. This proves the claimed isomorphism and all enumerations.

## Verification
Run `python3 verify.py` using Python 3's standard library. The script constructs the Fano incidence relation from the seven triples; checks the unique-line axiom; enumerates both seven-vertex shore assignments independently from all \(4^7\) named words; joins them under all \(21\) proper-incidence constraints; verifies the twelve-mask certificate and state counts; builds every one-vertex move; and performs a complete component search with exact degree, edge, component-size, and tree-shape assertions. It terminates with `VERIFY_OK`. The finite enumeration is exhaustive for the specified fourteen-vertex graph, not an extrapolation to a family.

## Relationship to prior work
Hao, Liu and Romaniello (arXiv:2611.16649, first public 12 November 2026) prove that every cubic bipartite graph has a proper two-homogeneous colouring with at most four colours, and construct fall three-colourings on three-connected det-extremal graphs using the Heawood graph. Their existence and extension theorems do not determine this graph's four-palette recolouring components or its counts. The published Fano-flag classification of the \(126\) frozen proper *three*-colourings of the Heawood graph gives the three-colour backbone here after choosing three of four names (\(504\) states), but its ordinary proper-colouring moves and three-colour palette do not cover the newly counted four-colour states or the two-homogeneous four-palette move graph. A separate count of four-tuples of total dominating sets with two memberships per vertex counts set-valued labels rather than this one-colour-per-vertex properness condition and does not imply the component structure. These comparisons distinguish hypotheses, objects, and allowable moves, not merely titles.

## Limitations
The conclusion is specific to the fourteen-vertex Heawood incidence graph, four named palette colours, and single-site moves preserving exact two-colour open neighbourhoods. No claims are made for other cubic graphs, larger palettes, general proper-colouring reconfiguration, or an independently verified publication-priority certificate. The result is a complete finite mathematical classification supported by a reproducible exhaustive test; an independent scholarly audit has not been performed.

## References
1. R.-X. Hao, J. Liu and F. Romaniello, *On 2-Homogeneous Colourings of Cubic Bipartite Graphs*, arXiv:2611.16649v1, 12 November 2026, https://arxiv.org/abs/2611.16649 .
2. *Fano flags and the unique mobile sector of Heawood \(3\)-colourings*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-fano-flags-and-the-unique-mobile-sector-of-heawood-3-colourings--78dac1ccb780 .
3. *Exact four-fold total-domination witnesses of the Heawood graph*, publicly accessible mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-four-fold-total-domination-witnesses-of-the-heawood-graph--0b0ea03f39a5 .
