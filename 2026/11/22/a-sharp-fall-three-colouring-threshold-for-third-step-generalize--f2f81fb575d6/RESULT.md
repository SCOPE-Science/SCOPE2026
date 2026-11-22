# A sharp fall-three-colouring threshold for third-step generalized Petersen graphs

## Finding

For every integer \(n\ge 7\), the generalized Petersen graph \(GP(n,3)\) admits a proper fall three-colouring if and only if \(n\ge9\). Equivalently, for exactly these orders there is a vertex three-colouring in which every vertex has a neighbour in each of the other two colour classes. In the terminology of two-homogeneous proper colouring, each vertex sees exactly two different colours in its open neighbourhood.

For even \(n\ge8\), the graph is cubic bipartite; therefore the four-colour bound of Hao, Liu and Romaniello [1] gives the exact two-homogeneous chromatic number: it equals \(4\) at \(n=8\) and equals \(3\) at every even \(n\ge10\). This corollary depends on their published upper bound; the new constructive statement itself treats odd and even \(n\) alike.

## Assumptions and scope

The graph \(GP(n,3)\), for integer \(n\ge7\), has \(2n\) vertices \(u_i,v_i\), with subscripts in \(\mathbb Z/n\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\) and \(v_iv_{i+3}\), taken as undirected edges. A fall three-colouring is a map from vertices into \(\{0,1,2\}\) that is proper and whose open neighbourhood at each vertex contains both other colours. All three colours are necessarily used. The statement concerns three colours, not an enumeration or the existence of larger fall palettes, and does not determine the minimum two-homogeneous palette at odd \(n=7\).

## Proof

Write \(a_i\) for the colour of \(u_i\) and \(b_i\) for that of \(v_i\). The necessary and sufficient local conditions are, for every \(i\) modulo \(n\),

\[
 a_i\ne a_{i+1},\quad a_i\ne b_i,\quad b_i\ne b_{i+3},
\]
\[
 |\{a_{i-1},a_{i+1},b_i\}|=2,\qquad
 |\{b_{i-3},b_{i+3},a_i\}|=2.
\]

The three inequalities express properness of the three kinds of edges, while the two set-cardinality conditions say the two other colours occur among each degree-three vertex's neighbours. Each condition is determined by seven consecutive column pairs \((a_j,b_j)\), centred at \(i\).

**Base words.** The following cyclic words, with the first string giving \(a\) and the second \(b\), satisfy all the displayed conditions. Each character is a colour from \(\{0,1,2\}\); the words are read cyclically.

| \(n\) | Outer word | Inner word |
|---:|---|---|
| 9 | `010120212` | `122211000` |
| 10 | `0102101201` | `2211020112` |
| 11 | `01021021021` | `22110202110` |
| 12 | `010210210212` | `221102021100` |
| 13 | `0102101201212` | `2211020112000` |
| 14 | `01021012010212` | `22110201122000` |
| 15 | `010210120121021` | `221102011200112` |
| 16 | `0102101201012012` | `2211020112221100` |
| 17 | `01021021020210212` | `22110202111022100` |
| 18 | `010210120101201021` | `221102011220012100` |
| 19 | `0101201201202012012` | `1220012120011120201` |

All nine words of orders \(10\) through \(18\) start with the identical six column pairs

\[
 ((0,2),(1,2),(0,1),(2,1),(1,0),(0,2)).
\]

**Splicing lemma.** Regard a legal cyclic column word as a closed walk in the finite directed graph whose states are ordered six-tuples of columns from \(\{0,1,2\}^2\), with a transition from one six-tuple to the next when the resulting seven-column window satisfies the five displayed constraints at its centre. (The central index in the window is the fourth column.) Two legal cyclic words beginning with the same six columns represent closed walks based at the same state. Concatenating their walks is another closed walk and hence gives a legal cyclic word with length equal to the sum of the two original lengths. Since the concatenated column sequence is exactly the two words laid end to end, no additional boundary condition is required. Repeated concatenation works as well.

Every integer from \(20\) through \(28\) is the sum of \(10\) and one of \(10,\ldots,18\), and \(29=11+18\). Every integer \(n\ge30\) reduces to the interval \(20\) through \(29\) by repeated subtraction of \(10\). Thus the shared-start base words furnish legal words at all \(n\ge20\). Together with the separate bases \(9\) and \(19\), this proves existence for every \(n\ge9\).

**Sharp exclusions.** For \(n=7,8\), first enumerate every proper three-colour word on the outer cycle, then quotient only by genuine graph symmetries: cyclic rotations, reflection, and simultaneous permutation of three colour names. For each orbit representative, enumerate every inner word respecting spoke properness and the required two-colour outer-neighbourhood condition; finally impose inner-edge properness and the inner-neighbourhood condition. The complete orbit data are:

| \(n\) | Representative | Orbit size | Outer-compatible inner words | Inner-edge-proper | Fully valid |
|---:|---|---:|---:|---:|---:|
| 7 | `0101012` | 42 | 8 | 0 | 0 |
| 7 | `0101202` | 42 | 8 | 4 | 0 |
| 7 | `0102012` | 42 | 32 | 2 | 0 |
| 8 | `01010101` | 6 | 1 | 0 | 0 |
| 8 | `01010102` | 48 | 4 | 0 | 0 |
| 8 | `01010202` | 24 | 4 | 0 | 0 |
| 8 | `01010212` | 48 | 16 | 1 | 0 |
| 8 | `01012012` | 48 | 64 | 0 | 0 |
| 8 | `01012102` | 48 | 16 | 3 | 0 |
| 8 | `01020102` | 12 | 16 | 0 | 0 |
| 8 | `01021012` | 24 | 64 | 0 | 0 |

Their orbit sizes sum to \(126\) and \(258\), respectively, the complete counts of proper named outer-cycle three-colour words. Every compatible inner choice is checked; the final column is identically zero. Thus there is no fall three-colouring for either excluded order. The attached standalone `verify_gp3.py` computes these finite tables directly and exhaustively, using only Python's standard library.

**Even-order corollary.** For even \(n\), parity of the index and the inner step \(3\) give a bipartition of \(GP(n,3)\). The graph is cubic and the proper two-homogeneous definition permits no two-colour solution (a proper two-colouring has only one neighbour colour per vertex). The just-proved three-colour existence/nonexistence together with the general at-most-four theorem of [1] yields the asserted exact values for even \(n\ge8\).

## Verification

Run `python3 verify_gp3.py` using Python 3 and its standard library. The script constructs graph edges and neighbour sets independently of the seven-window formulation, verifies all eleven base words and common six-column prefix, exhaustively derives the exclusion-orbit tables, and checks the explicitly spliced constructions through order \(200\). Its complete run ends with `VERIFY_OK`. The finite tests support the proof; the unbounded existence conclusion follows from the splicing lemma, not extrapolation from tested orders.

## Relationship to prior work

Hao, Liu and Romaniello [1], first public November 12, 2026, establish a four-colour upper bound for every cubic bipartite graph and identify stronger sufficient conditions for three; their result is used for the even-order corollary, not claimed as new. Karami [2] classifies *perfect two-colouring quotient matrices* of the same generalized Petersen family, not proper three-colour fall assignments. General conditional-colouring work [3] studies the problem type, not this exact all-order classification. The new statement supplies the sharp specific order threshold and uniform constructive words in the third-step generalized Petersen family. No general result asserting three colours for all cubic bipartite graphs is assumed.

## Limitations

This theorem does not classify all fall three-colouring assignments or any larger-colour fall spectrum, and does not give the two-homogeneous chromatic number at odd order seven. Historical priority against every unindexed result is not certified; in particular, a related 2012 conditional-chromatic paper was available by abstract but not as an inspectable full text. Exhaustive finite computations are made reproducible as a checkable finite exclusion certificate, not presented as proof of the infinite existence portion by themselves.

## References

1. R.-X. Hao, J. Liu and F. Romaniello, *On 2-Homogeneous Colourings of Cubic Bipartite Graphs*, arXiv:2611.16649v1 (2026-11-12). https://arxiv.org/pdf/2611.16649v1
2. H. Karami, *Perfect 2-colorings of the generalized Petersen graph GP(n,3)*, arXiv:2009.07120v2 (2020). https://arxiv.org/pdf/2009.07120
3. X. Li, X. Yao, W. Zhou and H. Broersma, *Complexity of the conditional colorability of graphs*, arXiv:0711.2843 (2007). https://arxiv.org/abs/0711.2843
4. S. Li, S. Fan and Y. Zhong, *The Best Lower Bound of Conditional Chromatic Number of the Generalized Petersen Graphs* (2012), relevant published title; full text not inspected.
