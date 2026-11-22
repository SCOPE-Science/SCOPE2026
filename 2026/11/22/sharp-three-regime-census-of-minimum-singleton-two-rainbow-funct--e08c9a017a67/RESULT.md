# Sharp three-regime census of minimum singleton two-rainbow functions on wheels

## Finding
For each integer \(n\ge9\), let \(W_{n+1}=K_1\vee C_n\) be the labelled wheel with a distinguished hub and cyclically indexed rim. A *singleton two-rainbow dominating function* is a map \(f:V(W_{n+1})\to\{0,1,2\}\) such that each vertex with label \(0\) has both a label-\(1\) neighbor and a label-\(2\) neighbor. Its weight is the number of vertices with nonzero label. The two positive colors and the rim vertices are individually distinguished.

**Theorem.** For every \(n\ge9\), the minimum weight is
\[
\widetilde\gamma_2(W_{n+1})=1+\left\lceil\frac n3\right\rceil.
\]
Every minimum function colors the hub with one positive color. Let \(N_n\) be the number of minimum functions with two named colors (without identifying rotations, reflections or color exchange). Then
\[
N_n=\begin{cases}
6,&n\equiv0\pmod3,\\
\dfrac{n(n+11)}3,&n\equiv1\pmod3,\\
2n,&n\equiv2\pmod3.
\end{cases}
\]
Thus the optimal-configuration multiplicity has sharply different bounded, quadratic and linear growth along the three residue classes. More precisely, fix the hub color \(1\) and put \(k=\lceil n/3\rceil\). Every optimal rim coloring has exactly \(k\) positive vertices, and either (a) all are color \(2\), their positions form a minimum dominating set of \(C_n\), or (b) \(n=3q+1\), exactly \(q\) rim vertices are color \(2\), exactly one is color \(1\), and the remaining \(2q\) are color \(0\). Case (b) consists of exactly \(n\) assignments: one long gap of pattern \(2,0,1,0,2\) and otherwise successive gaps of pattern \(2,0,0,2\), with overlapping displayed boundary vertices identified. Exchanging the two named colors gives the other half.

## Assumptions and scope
The graph is finite, simple, undirected and vertex-labelled, and the cycle has \(n\ge9\) vertices. The hub is the unique universal vertex. Each chosen vertex carries exactly one color, unlike standard set-valued rainbow domination. Every vertex labelled \(0\), including the hub if it is zero, must see both colors. A positive-labeled vertex has no further condition. The cyclic positions are fixed and color labels are distinct, so the enumeration is not divided by any automorphism factor. Counts concern only *minimum-weight* assignments; there is no claim about the whole polynomial or a general cone formula.

## Proof
Let \(h\) be the hub and let \(S\) be the set of positively labelled rim vertices. If \(f(h)=i\in\{1,2\}\), each rim vertex labelled \(0\) must have a rim neighbor of the *other* positive color. Consequently \(S\) is an ordinary dominating set of the cycle \(C_n\). The elementary disjoint-coverage bound for a cycle gives \(|S|\ge\lceil n/3\rceil\), since each vertex in \(S\) dominates at most three rim positions. Equality is attained: take any minimum dominating set of the cycle, label all its vertices with the color opposite to \(f(h)\), and label every other rim position \(0\). Thus among functions with a colored hub the minimum weight is \(1+\lceil n/3\rceil\).

Suppose instead that \(f(h)=0\). Every rim zero must have its two rim neighbors colored \(1\) and \(2\), respectively. In particular the rim zeros form an independent set, hence \(|S|\ge\lceil n/2\rceil\). For \(n=9\) and all \(n\ge11\), \(\lceil n/2\rceil>1+\lceil n/3\rceil\). The remaining case is \(n=10\): attaining weight \(5\) would require five alternating rim zeros and five alternating rim positive vertices. The five positive vertices would then have to alternate between colors \(1\) and \(2\) around an odd five-cycle of zero-mediated inequalities, an impossibility. Therefore no minimum function with \(n\ge9\) has a zero hub, proving both the optimum and hub rigidity.

Fix henceforth \(f(h)=1\) and \(k=\lceil n/3\rceil\). An optimum has exactly \(k\) colored rim vertices. Write \(p\) for the number of rim vertices colored \(2\). All \(n-k\) rim zeros must neighbor a color-\(2\) rim vertex. Because a color-\(2\) vertex has at most two zero neighbors, \(n-k\le2p\le2k\). Writing \(n=3q+r\), \(r\in\{0,1,2\}\), this forces \(p=k\) for \(r=0,2\), and forces \(p\in\{q,q+1\}\) for \(r=1\). Thus every optimal rim assignment has only color \(2\), except possibly one color-\(1\) rim vertex in residue class \(1\).

When all \(k\) rim selections have color \(2\), the unselected positions must lie in cyclic gaps of length \(0,1,2\) between successive selected vertices. Marking one selected vertex and writing the lengths of the \(k\) intervening zero gaps gives the exact number
\[
B_n=\frac nk\,[u^{n-k}](1+u+u^2)^k.
\]
Indeed, the marked vertex has \(n\) choices, the ordered cyclic gap tuple is counted by the coefficient, and each unmarked dominating set was counted exactly \(k\) times. In the three residue classes the coefficient evaluates respectively to \(1\), \(k+\binom{k}{2}\), and \(k\). Hence
\[
B_{3q}=3,\qquad B_{3q+1}=\frac{(3q+1)(q+2)}2,\qquad B_{3q+2}=3q+2.
\]

In the remaining case, \(n=3q+1\), there are \(q\) rim vertices colored \(2\), one colored \(1\) and \(2q\) zeros. All \(2q\) incidences from a color-\(2\) position to its two rim neighbors must be used, once each, to cover the \(2q\) zeros. Thus every color-\(2\) position has two zero neighbors and every zero is adjacent to exactly one color-\(2\) position. Between successive color-\(2\) positions there must be two zeros, except in the unique gap containing the single color-\(1\) position, where the pattern must be \(2,0,1,0,2\). The other gaps have pattern \(2,0,0,2\). These forced patterns produce precisely one valid arrangement for each of the \(n\) possible locations of the exceptional color-\(1\) vertex, so there are exactly \(n\) exceptional assignments.

For a fixed hub color, the count is therefore \(B_n+n\mathbf1_{\{n\equiv1\pmod3\}}\). The two possible hub colors contribute equally and without overlap. Doubling yields \(6\), \((3q+1)(q+4)=n(n+11)/3\), and \(2n\), respectively. This proves the full claimed optimizer classification and census.

## Verification
The bundled standalone \(\texttt{verify.py}\) checks the neighborhood condition directly on every one of the \(3^{n+1}\) labelled assignments for \(3\le n\le10\). An independently organized finite-state enumerator then counts all valid cyclic rim words, including the hub condition and both named colors, for every \(3\le n\le50\), comparing exact minima and multiplicities with the displayed all-order formulas. It reports \(\texttt{FINITE_STATE_CHECK_3_TO_50_PASS}\) and \(\texttt{INDEPENDENT_DIRECT_LABELING_CENSUS_3_TO_10_PASS}\). These computations corroborate the proof but do not establish the infinite theorem; the preceding counting argument does.

## Relationship to prior work
Singleton two-rainbow domination is also called dual-server domination. Lange (2026, arXiv:2610.06906v1, Sections 2 and 5) defines this singleton model, establishes scalar minimum values for cycles and selected regular graph families, and discusses service-location motivation. It does not analyze wheel graphs or optimal wheel multiplicities. A published all-weight singleton two-rainbow polynomial for labelled paths and cycles (2026, reference 2) determines the rim-only case; its cycle formulas do not imply the present wheel count because the universal hub adds new configurations, and the exceptional rim vertex contributes an additional \(n\) optimizers in precisely one residue class. A published exact enumeration of singleton three-rainbow minima on two-row cycle prisms (reference 3) exhibits modular multiplicities for a different graph and three-color constraint, not this wheel theorem. The general dual-server-domination paper of Chellali, Haynes and Hedetniemi introduces the same invariant, but accessible descriptions and subsequent citations do not settle whether it contains an earlier wheel-specific multiplicity count. No previously available source identified in the targeted searches implies the stated all-order wheel classification.

## Limitations
Only the minimum-configuration census for \(n\ge9\) is asserted, not the complete weight polynomial or extensions to other cone graphs, larger palettes or set-valued rainbow domination. Smaller rims have different hub behavior and are excluded from the theorem, although independently enumerated in the checker. The primary 2026 dual-server journal article was not available in full text during comparison, and some unindexed earlier results could precede this count; the originality statement is a best-knowledge assessment, not an independent certification. Mathematical independent audit has not been performed.

## References
1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow k-Domination in Regular Graphs*, arXiv:2610.06906v1, publicly posted October 1, 2026, Sections 2, 5 and 6. https://arxiv.org/abs/2610.06906
2. *Complete singleton two-rainbow domination spectra of paths and cycles*, publicly available November 1, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-complete-singleton-two-rainbow-domination-spectra-of-paths-and-c--0518da82b5ef
3. *Exact optimal singleton three-rainbow domination multiplicities of cycle prisms*, publicly available November 2, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-optimal-singleton-three-rainbow-domination-multiplicities--6a2d2531557b
4. M. Chellali, T. W. Haynes and S. T. Hedetniemi, *Dual-server domination in graphs*, Discrete Applied Mathematics 387 (2026), 251–259, DOI:10.1016/j.dam.2026.03.017. https://doi.org/10.1016/j.dam.2026.03.017
