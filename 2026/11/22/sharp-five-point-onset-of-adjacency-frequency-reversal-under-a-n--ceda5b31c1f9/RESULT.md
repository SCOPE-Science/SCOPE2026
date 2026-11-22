# Sharp five-point onset of adjacency-frequency reversal under a named edge in the homogeneous triangle-free graph

## Finding
Let \(\mathcal H_3\) be the countable homogeneous universal triangle-free graph. The base \(G\) is any finite triangle-free induced subgraph, with all its vertices named separately. A complete ordered injective two-type means a complete type of an ordered pair of distinct new points over those constants; the uniform distribution is on the finite set of such types, **not** on vertices of \(\mathcal H_3\).

Put \(I(G)=|\{A\subseteq V(G):A\text{ is independent}\}|\), counting \(\varnothing\), and \(B(G)=|\{(A,B):A,B\subseteq V(G)\text{ independent},\ A\cap B=\varnothing\}|\). Then the adjacency-type probability is
\[
p(G)=\frac{B(G)}{I(G)^2+B(G)}.
\]
For each absent base edge \(e\) for which \(G+e\) is still triangle-free, the response \(p(G+e)-p(G)\) is **strictly positive** whenever \(|G|\le4\). At \(|G|=5\), there are exactly two edge-marked isomorphism classes with negative response:

| Before insertion | After insertion | \((I,B)\) before | \((I,B)\) after |
|---|---|---|---|
| \(K_{1,3}\sqcup K_1\) | \(K_{1,4}\) | \((18,129)\) | \((17,113)\) |
| \(P_3\sqcup K_2\) | \(S(1,1,2)\) | \((15,119)\) | \((14,103)\) |

Here the second insertion joins an endpoint of the edge component to the central vertex of the three-vertex path, creating the tree with arms of lengths \(1,1,2\). In the first case the odds \(B/I^2\) go from \(43/108\) to \(113/289\); in the second they go from \(119/225\) to \(103/196\). In the labelled census there are exactly \(20\) and \(60\) decreasing additions of these types, respectively, and no zero changes.

This reversal persists: for every integer \(m\ge4\), insertion of the center-to-isolate edge \(K_{1,m-1}\sqcup K_1\to K_{1,m}\) strictly decreases \(p\). Both signs occur at every finite parameter order \(n\ge5\); in fact, adjoining any number of isolated parameters to any fixed eligible insertion leaves its sign unchanged.

## Assumptions and scope
The only graph relation is adjacency; loops are absent. Both parameter graphs before and after insertion are finite and triangle-free. The base vertices are pointwise named, so automorphisms of the base do **not** quotient the counted types. The insertion has two distinct previously nonadjacent endpoints, and no existing edge is deleted. All finite computations and exact inequalities concern the unweighted count of complete, nonalgebraic types of two *distinct* new vertices. The conclusion is about a fraction of types rather than the absolute number of types.

## Proof
**Type-counting identity.** The extension property defining the homogeneous triangle-free graph realizes a new vertex whose neighbors in the base are precisely any independent subset. Two distinct new vertices not adjacent to one another therefore permit all \(I(G)^2\) ordered neighborhood pairs. If the new points are adjacent, their neighborhoods must additionally be disjoint, because a shared old neighbor would make a triangle. Conversely the resulting finite graph is triangle-free, hence embeds by homogeneity. This gives exactly \(B(G)\) adjacent types and proves the probability formula. Since the map \(x\mapsto x/(1+x)\) is strictly increasing for nonnegative \(x\), comparing \(p\) is equivalent to comparing the odds \(R(G)=B(G)/I(G)^2\).

**Exhaustive sharp cutoff and the two edge-marked classes.** For each \(1\le n\le5\), enumerate every bitmask of the \(\binom n2\) potential edges of a simple labelled graph on \(\{0,\ldots,n-1\}\). Retain those with no triple spanning all three of its edges. For each absent edge, retain the insertion when the augmented graph remains triangle-free. For every retained graph, independently enumerate all \(2^n\) vertex subsets, reject nonindependent subsets, and count every ordered disjoint pair. The sign is the exact integer sign of
\[
B(G+e)I(G)^2-B(G)I(G+e)^2.
\]
The number of eligible labelled insertions at orders \(1,2,3,4,5\) is respectively \(0,1,9,96,1410\). The decreasing counts are \(0,0,0,0,80\), and every other eligible change is strictly positive. At five vertices all \(80\) negative transitions are canonically grouped under all \(5!\) simultaneous relabellings of the old graph and designated added edge, yielding exactly two classes of labelled multiplicities \(20\) and \(60\), with the stated graph descriptions and integer pairs. The complete deterministic checker is included as `checker.py`; its nested loops and `canonical_aug` procedure cover every labelled graph and every possible vertex relabelling, so this is an exhaustive finite proof, not a sample of the class.

**Infinite star family.** Let \(m\ge1\), \(G_m=K_{1,m-1}\sqcup K_1\), and \(G_m^+=K_{1,m}\). The old isolate doubles \(I\) and triples \(B\). For a star with \(m\) leaves, an independent set either avoids the center (any leaf subset) or consists solely of that center; hence
\[
I(G_m)=2^m+2,\quad I(G_m^+)=2^m+1.
\]
For an ordered disjoint independent-set pair, give each vertex one of three states: unselected, in the first set, in the second. When the center is unselected its leaves have three choices each; when the center lies in one chosen set, all leaves have two choices. Thus
\[
B(G_m)=3^m+3\cdot2^m,\qquad B(G_m^+)=3^m+2^{m+1}.
\]
The exact cross-multiplied difference factors as
\[
B(G_m^+)I(G_m)^2-B(G_m)I(G_m^+)^2
=2^m\left[2\cdot3^m+3(3/2)^m+2^{m+1}+5-4^m\right].
\]
For \(m=1,2,3\) the bracket is positive; at \(m=4\), the term \(4^m=256\) exceeds the sum of its other terms \(214+3/16\). Writing that positive sum as \(F_m\), each of its four summands grows by a factor at most \(3\) from \(m\) to \(m+1\), whereas \(4^m\) grows by a factor \(4\). Thus \(F_m<4^m\) for every \(m\ge4\), proving strict reversal for all such \(m\).

**Persistence of both signs.** Appending \(k\) isolated named vertices changes \(I\) by \(2^k\) and \(B\) by \(3^k\), hence changes every odds ratio by the positive factor \((3/4)^k\). Consequently the sign of any insertion response is unchanged. The two-isolate-to-single-edge insertion has a strict positive response, and the five-point star insertion has a strict negative response. Padding each with isolates proves persistence to arbitrarily large parameter bases.

## Verification
Run `python3 checker.py` with Python 3 standard libraries only. The checker independently counts adjacent and nonadjacent labelled pair diagrams via a four-state-per-vertex assignment, independently of its subset counting implementation. It exhaustively lists all eligible edge additions through five vertices and uses all vertex permutations to classify five-vertex negative cases. It checks both integer count quadruples and tests the star identities for \(1\le m\le15\). The general star sign beyond the finite checks follows from the elementary geometric growth comparison above. Recorded results appear in `check_output.txt`.

## Relationship to prior work
Henson's construction supplies the homogeneous triangle-free graph. Conant describes its model-theoretic extension setting. Independent-set and all-arity Henson-type counting formulas, including their exact-counting complexity, are established separately; such formulas do not by themselves state the sharp minimal order, the complete edge-marked exception classification, or the persistent sign reversal for the normalized adjacency channel. The mathematical comparison is with the **probability response** \(p(G+e)-p(G)\), not with raw total type counts. A nearby literature on graph-homomorphism partition functions and lattice-gas edge dependence may contain equivalent formulations; historical priority is therefore provisional, and no independent audit is claimed.

## Limitations
The finite minimality/classification statement is exhausted only through order five. For larger bases it establishes explicit infinite positive and negative families, not a classification of all sign changes. Its uniform measure is on complete named-base logical types, not on random elements of the countable graph. The result does not extend automatically to higher tuple arities, other forbidden clique sizes, or base updates that create triangles. The calculation is exact, but priority should be independently checked against graph-homomorphism and statistical-mechanics literature.

## References
- C. W. Henson, *A Family of Countable Homogeneous Graphs*, Pacific Journal of Mathematics 38 (1971), 69–83. DOI: 10.2140/pjm.1971.38.69.
- G. Conant, *Forking and dividing in Henson graphs*, arXiv:1401.1570v1 (public 2014-01-08), https://arxiv.org/abs/1401.1570.
- *Higher-arity Henson type enumeration and exact-counting hardness*, published research record at https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-higher-arity-henson-type-enumeration-and-exact-counting-hardness--141a441755d6. Relevant to the general counting identity; publication-priority comparison to the edge-response theorem remains provisional.
