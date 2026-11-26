# Two mobile phases and one frozen orbit in the optimal edge colorings of \(\operatorname{KG}(5,2)\)

## Finding
Let \(P\) be the Petersen graph with vertices the two-subsets of \(\{0,1,2,3,4\}\); disjoint pairs are adjacent. Fix four named edge colors \(0,1,2,3\). The graph \(\mathcal R\) consists of all proper edge colorings of \(P\), adjacent exactly when the color on a *single edge* changes and propriety is preserved. Then
\[
|V(\mathcal R)|=49{,}920,\qquad |E(\mathcal R)|=109{,}440,
\]
and the complete connected-component profile, shown as (number of vertices, number of edges, multiplicity), is
\[
(24{,}480,54{,}720,2),\qquad(1,0,960).
\]
The \(960\) frozen colorings (those with no permissible one-edge recoloring) are a single orbit under the natural \(S_5\times S_4\) action on the five underlying symbols and the four named colors. Every frozen coloring has color-class sizes \(3,4,4,4\). Every palette permutation preserves each of the two large components, while any permutation of the underlying five symbols preserves the large components exactly when it is even and exchanges them when it is odd.

The number \(49{,}920\) of edge colorings is **not new**: it appears as the four-color value of OEIS A159233 [2]. The new assertion is the exact adjacency/component and symmetry classification.

## Assumptions and scope
All graphs are finite and simple. Edge colorings are functions, so distinct assignments of the four color names count as distinct states. A one-edge recoloring must affect exactly one edge; Kempe changes along an alternating path or cycle are **not** allowed as single steps. Vertices of \(P\) are ordered lexicographically as two-element subsets of the five-symbol set; edges of \(P\) are ordered lexicographically as pairs of disjoint vertices. These conventions fix a reproducible encoding of every coloring as a length-\(15\) word over four symbols. The result concerns only \(P\) and this rule, not arbitrary snarks or higher numbers of colors.

There are exactly six perfect matchings of \(P\), and deleting any one leaves two disjoint five-cycles. Thus no proper three-edge-coloring exists: removing any one color class from such a coloring would leave a union of even alternating cycles, contradicting the two odd cycles. The exhaustive construction below produces proper four-edge-colorings, hence four colors are optimal.

## Proof
**Complete state enumeration.** The attached program `verification.py` builds the ten vertices as two-subsets and the fifteen edges as disjoint pairs. Algorithm A assigns one of four colors to each edge in lexicographic order, recursively rejecting any color already present on an adjacent edge. Every proper assignment has a unique branch and every terminal branch is proper; this exhaustively produces \(49{,}920\) labeled assignments. As a second enumeration with a different search space, Algorithm B enumerates the nonempty matchings among the \(2^{15}-1\) subsets of edges. It recursively selects the color class containing the least yet-uncovered edge and partitions the remaining edges into exactly four nonempty matching classes. Every unordered four-class matching partition has a unique such recursive decomposition. It produces exactly \(2{,}080\) partitions, identical to the canonical representatives of Algorithm A when color names are assigned in order of first use. Each partition has \(4!=24\) named realizations, independently recovering \(49{,}920\).

**Exact local adjacency.** For an edge \(e=uv\), let \(F_e(c)\) be the colors appearing on other edges incident with \(u\) or \(v\). A replacement color \(t\) is legal exactly when \(t\ne c(e)\) and \(t\notin F_e(c)\). This equivalence follows directly from the definition of proper edge coloring. The checker computes the forbidden sets both by adjacent-edge lookup and by unions of incident-color sets at the two endpoints; the two tests agree on every state-edge pair. Every generated neighboring assignment belongs to the complete enumerated state set, and all adjacency pairs are checked to be reciprocal. The resulting degree sum is \(218{,}880\), so the handshaking lemma gives exactly \(109{,}440\) undirected edges.

**Connected components and frozen states.** Exact flood-fill of the generated adjacency lists produces two components with \(24{,}480\) vertices and \(54{,}720\) edges each, plus \(960\) singleton components. An independently maintained disjoint-set union for all enumerated edges yields the identical components. In addition, an edge \(e\) is frozen in a state precisely when its three other incident colors collectively exhaust the three alternatives to \(c(e)\), i.e. \(|F_e(c)|=3\). Applying this test to every edge of every assignment identifies exactly the \(960\) singleton states, with the stated color-class size profile. No sampling is involved.

**Symmetry.** Every permutation of the five ground symbols acts on the ten vertices and fifteen edges, and every permutation of the palette acts on assignments; both actions preserve one-edge recoloring. For each of the two large components, the program checks all \(120\) symbol permutations on one representative. Even permutations map the representative into its original component and odd permutations into the other component. Because the action preserves adjacency, the check on one representative extends to the entire connected component. All \(24\) palette permutations similarly fix both large components. Finally the orbit of one frozen state under the \(120\times24\) product actions contains exactly \(960\) distinct assignments, and an equality check against the complete frozen-state set proves transitivity.

## Verification
Run `python verification.py` with Python \(\ge3.9\) and its standard library. Its deterministic summary appears in `verification_output.txt`. It verifies both enumeration methods, edge-by-edge legality, independent component algorithms, all prescribed symmetry actions and the elementary perfect-matching obstruction to three colors. All assertions must succeed and its final printed line must be `VERIFY_OK`. The exhaustive proof depends on faithful execution of this short finite checker; there is no extrapolation from a finite experiment to a larger graph family.

## Relationship to prior work
The four-coloring count is tabulated in OEIS A159233 [2], so reproducing that count is a consistency check, not an originality claim. McDonald, Mohar and Scheide [1, Theorem 3] prove that all four-edge-colorings of every subcubic graph are **Kempe equivalent**. A Kempe change exchanges two colors along an entire connected alternating path or cycle, and need not be achievable by individually legal recolorings. Thus [1] does not imply connectivity or component sizes for the more restrictive graph here. The CoRe 2019 open-problems record [3, p. 5] gives a **five**-edge-coloring of the Petersen graph that is frozen under a single-edge rule; it does not classify the four-color state space, nor the two large components. Davtyan [4] studies extremal interval spectra among edge colorings of the same graph, a distinct invariant; only its abstract was accessible during comparison.

## Limitations
The exact results are confined to the Petersen graph, four named colors and one-edge recolorings. Connectivity under Kempe changes is established prior work and is not reproved as a new theorem. Existence of a five-color frozen Petersen coloring is likewise known. Unindexed earlier computations and the inaccessible full text of [4] leave a residual originality risk. The result has not received independent external validation.

## References
[1] J. McDonald, B. Mohar, D. Scheide, *Kempe equivalence of edge-colourings in subcubic and subquartic graphs*, arXiv:1005.2248, submitted 2010-05-13, Theorem 3. Full text: https://arxiv.org/html/1005.2248v2.

[2] OEIS A159233, *Number of edge colorings of the Petersen graph*, first author entry dated 2009-04-06; four-color value 49920. https://oeis.org/A159233.

[3] A. Joffard, P. Ouvrard (compilers), *CoRe 2019 Open Problems*, entry by Marc Heinrich, printed page 5, illustrating a frozen five-color Petersen edge coloring. https://hoanganhduc.github.io/events/CoRe2019/CoRe_2019_Open_Problems.pdf.

[4] N. N. Davtyan, *On the \(\mu\)-parameters of the Petersen graph*, arXiv:1307.2348, first submitted 2013-07-09. https://arxiv.org/abs/1307.2348.
