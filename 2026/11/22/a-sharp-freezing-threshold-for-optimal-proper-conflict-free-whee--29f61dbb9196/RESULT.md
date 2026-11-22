# A sharp freezing threshold for optimal proper conflict-free wheel recolouring

## Finding
For every integer \(n\ge3\), let \(W_{n+1}=K_1\vee C_n\), with distinguished hub \(h\) and rim vertices \(v_0,\ldots,v_{n-1}\) in cyclic order. A proper conflict-free (PCF) colouring assigns different colours to adjacent vertices and gives each vertex an open-neighbourhood colour that occurs exactly once. Fix a palette of four **named** colours. Form the reconfiguration graph \(\mathcal R_n\) whose vertices are all PCF four-palette colourings, with adjacency exactly when one vertex changes colour and the new colouring remains PCF.

The PCF chromatic number of every wheel is \(\chi_{\rm pcf}(W_{n+1})=4\). More significantly, the **entire optimal recolouring graph** is
\[
\boxed{\mathcal R_n\cong
\begin{cases}
24K_1,&n=3,\\
48K_1,&n=4,\\
8C_{15},&n=5,\\
24C_6,&n=6,\\
24nK_1,&n\ge7.
\end{cases}}
\]
The notation \(rH\) means a disjoint union of \(r\) copies of \(H\). In particular, there is a **sharp freezing threshold at seven rim vertices**: all optimal colourings are isolated for every \(n\ge7\), whereas every optimum is mobile for \(n=5,6\). The exact numbers of labelled optimal assignments are \(24,48,120,144\) at \(n=3,4,5,6\), respectively, and \(24n\) for \(n\ge7\). There are no recolouring edges except at \(n=5,6\), where their numbers are \(120\) and \(144\).

## Assumptions and scope
Graphs are finite, simple and labelled. For \(n=3\), the wheel is \(K_4\). A four-palette colouring may in principle leave a colour unused, but the proved optimum forces all four colours to appear. The conflict-free condition uses **open** neighbourhoods. Every reconfiguration edge changes exactly one vertex colour, never two simultaneously; global permutations of colour names are not permitted as a single move. The graph \(\mathcal R_n\) is not the ordinary proper-colouring reconfiguration graph: an intermediate assignment must retain its conflict-free witness at every vertex.

## Proof
**1. The hub reduces PCF to a singleton rim colour.** In every proper colouring, the hub colour is absent from the rim. Hence every rim vertex has the uniquely coloured hub as a neighbour and automatically satisfies its own conflict-free condition. The hub satisfies its conflict-free condition if and only if some rim colour occurs on exactly one vertex. This criterion is for all proper colourings, regardless of palette size. With only three total colours available, an even rim must alternate two colours, each appearing \(n/2\ge2\) times. An odd rim cannot be properly coloured with two colours. Thus three colours never suffice on a wheel. Four suffice: choose any hub colour, colour one rim vertex with a second colour, and alternate the remaining two colours along the path obtained by deleting that vertex. This proves \(\chi_{\rm pcf}=4\).

For \(n\ge5\), every PCF four-colouring has exactly three rim colours and **exactly one singleton rim colour**. Indeed, it has at least one; if there were two, all remaining \(n-2\) rim vertices would have to carry the third colour. But the independence number of \(C_n\) is \(\lfloor n/2\rfloor<n-2\) for \(n\ge5\). Once the singleton vertex \(v_p\) and its colour \(s\) are specified, the remaining two named rim colours must alternate along the path \(v_{p+1},\ldots,v_{p+n-1}\). There are exactly two possible orders. Consequently there are \(n\cdot3\cdot2=6n\) PCF assignments for each fixed hub colour, or \(24n\) across the four hub choices.

At \(n=3\), the rim is a triangle, so its six assignments use all three rim colours. At \(n=4\), the valid rim assignments have colour multiplicities \((2,1,1)\): choose which of three colours is repeated (three choices), one of the two opposite rim-vertex pairs (two choices), and the order of the two singleton colours (two choices). Thus there are twelve assignments per hub colour. This gives the stated vertex counts for all \(n\).

**2. Recolouring possibilities.** No recolouring can change the hub colour: each other named colour occurs on the rim. A non-singleton rim vertex is coloured by one of the two alternating path colours. Its other path-colour is used by an adjacent vertex, so it cannot be recoloured to that colour. It can only be recoloured to the old singleton colour \(s\), and only if it is not adjacent to \(v_p\). Such a move doubles the multiplicity of \(s\) and reduces one alternating colour multiplicity by one. If that latter multiplicity was at least three, **no singleton remains**, and the move is invalid. The singleton rim vertex can be recoloured to an alternating colour only when its two rim neighbours have the same colour, but this eliminates the singleton and produces no new one. (For \(n=3,4\), the small multiplicities are handled directly below.)

If \(n\ge7\), the two alternating colours occur at least three times each: for odd \(n=2m+1\), both occur \(m\ge3\) times; for even \(n=2m\), the counts are \(m\) and \(m-1\ge3\). The preceding argument therefore excludes every one-vertex recolouring. So all \(24n\) vertices are isolated.

For \(n=5\), both alternating colours occur twice. In each such colour class, precisely one vertex is not adjacent to the singleton vertex, so there are exactly two valid recolourings. For \(n=6\), the alternating colour classes have sizes three and two. Exactly the two vertices of the size-two class can be recoloured to the singleton colour, and both are nonadjacent to the singleton vertex. There are again precisely two valid recolourings. Thus the graph induced by a fixed hub colour is two-regular at \(n=5,6\).

For \(n=3\), every rim vertex sees both other rim colours, so no change is proper. At \(n=4\), a repeated-colour vertex sees both singleton colours and cannot change. Either singleton vertex can only be recoloured to the *other* singleton colour; that would leave both rim colours repeated twice, destroying the witness at the hub. Therefore these smaller graphs also have no recolouring edges.

**3. Exactly two fifteen-cycles at \(n=5\), per hub.** Fix a hub colour and name the remaining colours \(A,B,C\). Read rim words in order \(v_0,\ldots,v_4\). The following is a cycle of fifteen distinct allowable single-site recolourings, verified by direct comparison of consecutive words:

`ABABC → ABCBC → ABCAC → ABCAB → CBCAB → CACAB → CABAB → CABCB → CABCA → BABCA → BCBCA → BCACA → BCABA → BCABC → ACABC → ABABC`.

Every word in this display is a proper three-colour cycle word with one singleton, hence a PCF wheel colouring. The displayed cycle occupies fifteen distinct vertices in a two-regular graph. Interchanging the two named colours \(B,C\) sends the first word to `ACACB`, which is absent from the displayed cycle. This automorphism therefore produces a second, disjoint fifteen-cycle. There are exactly thirty PCF rim words, so the two cycles exhaust the fixed-hub graph. Varying the hub colour gives \(8C_{15}\).

**4. Exactly six six-cycles at \(n=6\), per hub.** For each rim word there is exactly one colour occurring three times, and exactly one singleton colour and vertex. Both allowed recolourings change a vertex from the twice-used colour to the singleton colour. Thus they preserve the thrice-used colour and move the singleton's position by \(+2\) or \(-2\) modulo six, preserving its parity. These two invariants have three and two possibilities, respectively. For any fixed thrice-used colour and singleton parity, there are exactly six words: choose the singleton among the three rim positions of that parity, choose the singleton colour among the other two, and the alternating pattern is then uniquely fixed by the requirement that the thrice-used colour occur three times. Both moves preserve this six-state class, and every state has degree two. The clockwise \(+2\) move successively cycles the singleton position through three values and toggles the singleton colour between the other two, so its orbit has length six. Each class is therefore a six-cycle. There are six such classes per fixed hub colour, hence \(24C_6\) across all hub colours.

This completes the complete reconfiguration-graph classification. No finite experimentation is used to extrapolate the infinite freezing regime.

## Verification
Run `python3 verify.py` with Python 3 and no third-party packages. The script directly constructs the wheel adjacency list, checks properness and the PCF open-neighbourhood multiplicities **without using** the singleton characterization, enumerates all three-colour rim words for each \(3\le n\le11\), and independently constructs their exact one-site reconfiguration graphs. It compares all vertex, degree and component-size counts with the theorem. The script also checks the equivalence between the original PCF condition and the singleton-rim-colour criterion on all properly coloured rim words in this range. Actual replay terminates with `VERIFY_OK`; selected full-palette counts and component decompositions appear below.

| Rim order | Named optimal colourings | Components of the four-palette graph |
|---|---:|---|
| 3 | 24 | 24 isolated vertices |
| 4 | 48 | 48 isolated vertices |
| 5 | 120 | eight fifteen-cycles |
| 6 | 144 | twenty-four six-cycles |
| 7 | 168 | 168 isolated vertices |
| 11 | 264 | 264 isolated vertices |

The proof establishes the classification for all rim orders, whereas these checks cover only the stated finite range.

## Relationship to prior work
Santra, *Proper Conflict-Free Coloring on Structured Graph Classes* (2026), Theorem 22, proves a universal-vertex singleton-colour criterion for optimal proper conflict-free colouring of perfect graph cores. This supplies a related general principle and, when the cycle is even, implies the scalar wheel optimum of four colours; **neither the criterion nor the optimum is claimed as new**. Theorem 22 does not analyse the reconfiguration graph, the exceptional mobile lengths or the seven-rim freezing boundary. Caro, Petruševski and Škrekovski (2022) determine the conflict-free chromatic number of ordinary cycles, a different graph family, but do not derive the optimal wheel recolouring components.

A public 2026 wheel result, *Forced four-colouring polynomial and sharp seed census of wheel graphs*, counts initial partial seedings under the rule that a vertex with three distinctly coloured neighbours is forced; it has a different set of states and moves, and does not imply the present single-vertex recolouring graph of complete proper conflict-free colourings. A 2026 study of optimal PCF colourings of cycle prisms enumerates states on a distinct cubic graph family, without the universal hub or these transitions. Standard proper-colouring reconfiguration results also allow moves that destroy an open-neighbourhood singleton, so they do not imply this restricted optimal-state graph.

## Limitations
The result is limited to a four-colour **named** palette and elementary single-vertex recolouring on wheel graphs. It does not assert connectivity with an extra fifth colour, Kempe-change connectivity, list-colouring analogues, or any result for other cones. The wheel scalar optimum and the universal-vertex singleton principle are previously known or follow easily from prior results; the claimed contribution is the **exact optimal PCF recolouring geometry**. Historical priority remains subject to possible unindexed literature and to independent validation; the present review is not an independent audit.

## References
1. K. Santra, *Proper Conflict-Free Coloring on Structured Graph Classes: Bounds, Exact Algorithms, and Hardness*, arXiv:2611.03906v1 (first posted 2026-11-02), Theorem 22, https://arxiv.org/abs/2611.03906.
2. Y. Caro, M. Petruševski and R. Škrekovski, *Remarks on proper conflict-free colorings of graphs*, arXiv:2203.01088v1 (2022-03-02), https://arxiv.org/html/2203.01088v1.
3. *Forced four-colouring polynomial and sharp seed census of wheel graphs*, publicly indexed mathematical result (2026-11-08), https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-forced-four-colouring-polynomial-and-sharp-seed-census-of-wheel--90f832f169a9/RESULT.md.
4. *Optimal proper conflict-free colouring census for cycle prisms*, publicly indexed mathematical result (2026-11-02), https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-optimal-proper-conflict-free-colouring-census-for-cycle-prisms--373334d2a6e9/RESULT.md.
5. *Recoloring via Modular Decomposition*, Journal of Graph Theory 111 (2026), DOI 10.1002/jgt.70005, https://doi.org/10.1002/jgt.70005 (ordinary proper-colouring reconfiguration, not the extra conflict-free constraint).
