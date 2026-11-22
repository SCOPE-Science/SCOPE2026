# An antipodal six-axis classification of erasure-robust icosahedral identifying codes

## Finding
Let \(I\) be the regular twelve-vertex icosahedral graph. For an integer \(t\geq1\), call \(S\subseteq V(I)\) a *level-\(t\) identifying code* if removal of any collection of at most \(t-1\) selected detectors leaves a nonempty and pairwise-distinct closed-neighborhood signature for every vertex. Equivalently, each vertex has at least \(t\) detectors in its closed neighborhood, and every two different vertices have at least \(t\) detectors in the symmetric difference of their closed neighborhoods.

The complete sharp hierarchy, with numbers of minimum labeled configurations, is

| Required witness multiplicity \(t\) | Minimum number of detectors | Number of minimum configurations |
|---|---:|---:|
| 1 (ordinary identification) | 5 | 120 |
| 2 (one detector may fail) | 6 | 20 |
| 3 (two detectors may fail) | 11 | 12 |
| 4 (three detectors may fail) | 12 | 1 |

No level-\(t\) code exists for \(t\geq5\). The twenty minimum level-two codes are *exactly* the induced six-vertex 3-suns: a triangular face together with the three outside vertices that each have exactly one neighbor on that face. There is one such code per triangular face. Every one of the 120 minimum ordinary five-detector codes is contained in **exactly one** minimum one-erasure-resilient six-detector code. Increasing tolerance from one lost detector to two forces a sharp rise from six to eleven selected vertices.

## Assumptions and scope
The graph is simple, undirected and has vertex set \(\{0,1,\ldots,11\}\). Vertices \(0\) and \(11\) are poles; the upper cycle is \(1,2,3,4,5\) and the lower cycle is \(6,7,8,9,10\), with cyclic indexing modulo five. For \(0\leq i<5\), its six edge families are
\[
\{0,1+i\},\quad\{11,6+i\},\quad
\{1+i,1+(i+1\bmod5)\},\quad
\{6+i,6+(i+1\bmod5)\},\quad
\{1+i,6+i\},\quad\{1+i,6+(i-1\bmod5)\}.
\]
This gives the ordinary 5-regular icosahedral skeleton with thirty edges. Put \(N[v]=\{v\}\cup\{w:vw\in E(I)\}\). Erasures delete members of \(S\), not graph vertices, and knowledge of an intruder's location must remain distinguishable from no intruder. For \(u\ne v\), write \(\Delta(u,v)=N[u]\triangle N[v]\). No weighted, directed or open-neighborhood convention is used. All configuration counts are for the fixed twelve named vertices, not counts of isomorphism classes.

## Proof
**1. Erasure criterion and six antipodal axes.** For any graph, a detector set survives arbitrary deletion of at most \(t-1\) detectors if and only if
\[
|S\cap N[v]|\ge t\quad(\forall v),\qquad
|S\cap\Delta(u,v)|\ge t\quad(\forall u\ne v).
\]
Indeed a signature vanishes after fewer than \(t\) witnesses are erased; two signatures become identical precisely if every distinguishing detector is erased. These two bad events are excluded by the displayed bounds, and conversely either deficient witness set can be erased.

The six antipodal vertex pairs in the given labeling are
\[
P_0=\{0,11\},\ P_1=\{1,8\},\ P_2=\{2,9\},\ P_3=\{3,10\},\ P_4=\{4,6\},\ P_5=\{5,7\}.
\]
Direct substitution into the explicit thirty-edge model proves three finite neighborhood facts: (a) each \(N[v]\) contains exactly one vertex of each \(P_i\); (b) the thirty adjacent-vertex sets \(\Delta(u,v)\) are exactly the fifteen unions \(P_i\cup P_j\), each occurring twice; and (c) at graph distance two the symmetric difference is a union of four antipodal pairs, while for antipodal vertices it is the entire twelve-vertex set. All these identities are checked independently by the two included verifiers. Set \(m_i=|S\cap P_i|\in\{0,1,2\}\). The adjacent-pair inequalities therefore impose
\[
m_i+m_j\ge t\quad\text{for all }0\le i<j\le5.
\]

**2. Ordinary codes: sharp five and exactly 120.** For \(t=1\), at most one antipodal pair can have zero occupancy. Consequently a code of four or fewer vertices is impossible. At size five every possible code must omit one entire pair and choose one endpoint from each remaining pair. For any fixed omitted pair there are \(2^5=32\) such choices. The difference between any two distinct closed-neighborhood patterns occupies at least two antipodal coordinates, because the symmetric differences in part 1 have respectively two, four or six coordinate pairs. Hence, after omitting any one antipodal coordinate, the twelve neighborhood patterns remain distinct. Each vertex forbids *exactly one* of the 32 endpoint choices, namely the choice opposite to its closed-neighborhood pattern on all five occupied pairs; the twelve forbidden choices are distinct. Precisely \(32-12=20\) choices remain. Their adjacent-pair separators contain at least one detector and their other separators at least three; they all dominate by construction. Thus there are \(6\cdot20=120\) minimum identifying codes.

**3. One-erasure codes: sharp six and exactly twenty.** For \(t=2\), summing the fifteen pair inequalities gives \(5|S|\ge30\), so \(|S|\ge6\). Equality requires every inequality to be an equality, hence \(m_0=\cdots=m_5=1\). Thus a minimum candidate selects one endpoint from each antipodal pair. It automatically meets all distinction inequalities (two, four or six selected witnesses according to distance); only the twelve domination conditions remain. Encode its six choices as a word \(x\in\{0,1\}^6\), with the first coordinate the pole axis. The twelve closed neighborhoods themselves correspond to \(0^6\), its bitwise complement, and five weight-two words supported on consecutive edges of a 5-cycle together with their complements. Since antipodal neighborhoods are complementary, domination by at least two detectors is equivalent to Hamming distance \(2,3\) or \(4\) from \(x\) to each of the six representative words.

Let \(b\in\{0,1\}\) be the pole bit and \(T\) the selected-one positions among the five cyclic coordinates, with \(r=|T|\). The zero word gives \(2\le b+r\le4\). For each cycle edge \(E\), the weight-two word gives
\[
2\le b+r+2-2|T\cap E|\le4.
\]
Solving these five small inequalities yields exactly the following possibilities:

| Pole bit \(b\) | \(r\) | Permitted cyclic pattern \(T\) | Count |
|---:|---:|---|---:|
| 1 | 1 | Any singleton | 5 |
| 0 | 2 | Any independent pair of the five-cycle | 5 |
| 1 | 3 | Any three-vertex cover of the five-cycle | 5 |
| 0 | 4 | Any four-element subset | 5 |

All other cardinalities or patterns violate one of the inequalities. Thus exactly twenty size-six codes survive one deletion.

Every triangular face \(F\) of the icosahedron has exactly three external vertices with precisely one neighbor in \(F\), one for each member of \(F\); these three outside vertices are mutually nonadjacent. Consequently they extend \(F\) to an induced 3-sun. The graph has twenty triangular faces. By face-transitivity, it suffices to test one such six-set; for example \(\{0,1,2,4,7,10\}\) has minimum domination multiplicity two and minimum distinction multiplicity two. Thus all twenty face-associated 3-suns are feasible, and the exact count already proved shows these are **all** the minimum one-erasure codes.

**4. Unique optimal completion.** Every level-two minimum code remains an ordinary identifying code after deleting any one of its six selected vertices, by definition. Every feasible six-bit word listed in the table has even total Hamming weight (two or four). Hence no two feasible balanced six-vertex codes differ in just one antipodal choice, since changing a single coordinate reverses parity. Therefore no five-set can belong to two different level-two minima. The twenty level-two codes contribute \(20\cdot6=120\) different five-element subcodes; part 2 showed that precisely 120 minimum ordinary codes exist. Every one consequently has exactly one such extension.

**5. Two and three erasures.** When \(t=3\), no \(m_i\) can be zero and at most one can equal one. Thus \(|S|\ge11\). All twelve eleven-vertex sets (complements of a single vertex) work: every closed neighborhood has six vertices and loses at most one, while every symmetric difference has at least four vertices and loses at most one. Hence the sharp optimum is eleven and has twelve realizations. For \(t=4\), every pair inequality forces every \(m_i=2\); the full vertex set is the unique solution. For \(t\ge5\), the four-vertex symmetric difference for an adjacent pair cannot contain five detectors, even when all vertices are selected.

This completes the complete hierarchy and its structure, including the sharp discontinuity and unique-completion property. All finite graph identities, the 64 binary choices and the full 4096-subset spectrum are independently checked by standalone source programs; the argument above also derives the optimum sizes and counts without assuming their computational outputs.

## Verification
`verify_sets.py` constructs the graph from the six cyclic edge families, tests every subset and all 78 neighborhood/separation requirements using ordinary Python sets, identifies all 20 triangular faces and their attached 3-suns, and verifies unique extension of all 120 five-element minima. `verify_masks.cpp` uses an independent hard-coded thirty-edge list and bit arithmetic to exhaust all \(2^{12}=4096\) subsets; it separately reconstructs graph distances, antipodal coordinates, pair-union separator multiplicities, all twenty 3-suns and the unique extension relation. Run with `python3 -S verify_sets.py`, and compile/run the second with `g++ -O2 -std=c++17 -Wall -Wextra verify_masks.cpp -o verify_masks && ./verify_masks`. Both require no external data or packages. Actual independent executions agreed on the four minimum/count pairs \((5,120),(6,20),(11,12),(12,1)\) and on all additional structure. Exact integer enumeration supports this fixed-graph theorem, not any assertion about arbitrary larger graphs.

## Relationship to prior work
The identifying-code model is due to Karpovsky, Chakrabarty and Levitin (1998). Bousquet and coauthors (first public July 22, 2014) study identifying codes, VC-dimension and approximability in general hereditary graph classes; their original text does not give this icosahedral fault-tolerance classification. Jean and Seo (first public December 3, 2021) give the now-standard one-erasure requirement of twofold domination and pair separation, plus generic complexity and other graph families; that **criterion is not claimed as new** here. An earlier complete study of one-erasure identifying codes on the *dodecahedral* graph concerns the different 20-vertex dual skeleton and does not imply the twelve-vertex icosahedral counts. Published icosahedral metric-basis, zero-forcing and antipodal-polytope volume studies investigate different signatures and objectives; their counts of antipodal endpoint selections do not impose identifying-code domination and separation inequalities. The distinctive contribution is the complete four-level identifying-code resilience spectrum, exact optimizer geometry and unique five-to-six-detector completion.

## Limitations
The result is specific to the ordinary twelve-vertex icosahedral graph and the stated detector-erasure model. It is not a claim about arbitrary planar graphs, polyhedral skeletons, signal-bit errors or multiple intruders. The general one-erasure criterion and the concept of ordinary identifying codes predate this work. Although directly relevant available primary text and mathematical search records were compared, unindexed earlier exact enumerations could affect priority. Independent scholarly validation has not been performed.

## References
1. M. G. Karpovsky, K. Chakrabarty, and L. B. Levitin, *On a new class of codes for identifying vertices in graphs*, IEEE Transactions on Information Theory 44 (1998), 599–611.
2. N. Bousquet, A. Lagoutte, Z. Li, A. Parreau, and S. Thomassé, *Identifying codes in hereditary classes of graphs and VC-dimension*, first public July 22, 2014, arXiv:1407.5833, https://arxiv.org/abs/1407.5833 .
3. D. C. Jean and S. J. Seo, *Fault-tolerant Identifying Codes in Special Classes of Graphs*, first public December 3, 2021, arXiv:2112.01685, https://arxiv.org/abs/2112.01685 .
4. *One-erasure identifying codes of the dodecahedral graph: fifteen isolated optima with a Kneser intersection geometry*, published mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-one-erasure-identifying-codes-of-the-dodecahedral-graph-fifteen--6f3f5679e5c9 .
5. *Exact volume spectrum of antipodal vertex selections in the regular icosahedron*, published mathematical record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-volume-spectrum-of-antipodal-vertex-selections-in-the-regu--bf118805f790 .
