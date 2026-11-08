# Sharp minimal-falsifier spectra for inverse functional-dependence disjunctions

## Finding

Let \(P,Q\) be finite nonempty sets of cardinalities \(p,q\), and let \(T\subseteq P\times Q\) be a two-variable team. Under ordinary (lax) dependence-logic splitting, put
\[
\varphi=\operatorname{dep}(x,y)\lor\operatorname{dep}(y,x).
\]
A *minimal falsifier* is a team that fails \(\varphi\) but whose every proper subteam satisfies \(\varphi\). Define \(\mathcal S_{p,q}\) to be the set of their cardinalities and \(m=\min(p,q)\). Then
\[
\boxed{\mathcal S_{p,q}=\begin{cases}
\varnothing,&m=1\text{ or }p=q=2,\\
\{6,7,\ldots,2m+1\},&p=q=m\ge3,\\
\{6,7,\ldots,2m+2\},&p\ne q,\ m\ge2.
\end{cases}}
\]
For an unsatisfying team, the minimum guaranteed upper bound on the size of a *some* unsatisfying subteam is the maximum element of this spectrum. Thus the sharp local-obstruction cutoff is \(2m+1\) for square alphabets of size \(m\ge3\), and \(2m+2\) for unequal alphabets with \(m\ge2\); in the empty-spectrum cases all teams satisfy the formula. The first two coefficients of the minimal-falsifier counting polynomial are
\[
\#\{|T|=6:T\text{ minimal falsifier}\}=\binom p2\binom q3+\binom p3\binom q2,
\]
\[
\#\{|T|=7:T\text{ minimal falsifier}\}=18\binom p3\binom q3.
\]
All binomial coefficients with an insufficient upper argument are zero. In particular, the full obstruction spectrum is an uninterrupted interval beginning at six, with a sharp parity-sensitive boundary in the larger alphabet.

## Assumptions and scope

Teams are **sets** of assignments over two named variables, not bags. The value sets \(P\) and \(Q\) may differ (sorted-domain version); the usual common-domain setting is obtained by \(P=Q\). The functional-dependence atom \(\operatorname{dep}(x,y)\) says equal \(x\)-values force equal \(y\)-values, and the dual atom interchanges variables. The disjunction is satisfied when \(T=T_1\cup T_2\) with \(T_1\models\operatorname{dep}(x,y)\) and \(T_2\models\operatorname{dep}(y,x)\). Because the atoms are downward closed, the cover may be assumed disjoint. The formulas do not require a nonempty team.

For clarity, a *local-obstruction cutoff* \(h\) means that a team fails exactly when it contains some falsifying subteam of at most \(h\) assignments. This is different from literal \(k\)-coherence, which quantifies over **exactly** \(k\)-element subteams and can be vacuous on smaller teams.

## Proof

**1. Convert split witnesses to pseudoforests.** Make a simple bipartite graph \(G_T\) with left vertices \(P\), right vertices \(Q\), and one edge for every pair in \(T\). For a disjoint split, orient each edge from its chosen determinant: an edge assigned to \(T_1\) is oriented out of its left endpoint and one assigned to \(T_2\) out of its right endpoint. Each dependence atom holds exactly when every vertex has outdegree at most one. Conversely, any orientation of outdegree at most one yields a split satisfying both dependence atoms. A finite graph admits such an orientation exactly when every connected component contains at most one cycle: necessity follows because its edges number at most its vertices, while sufficiency follows by directing the edges of each tree toward a root and the edges of each unicyclic component toward its unique cycle, directing that cycle consistently. Thus \(T\models\varphi\) iff \(G_T\) is a pseudoforest. This standard graph reduction is not claimed as new.

**2. Structural constraints on minimal falsifiers.** A minimal non-pseudoforest edge set is one circuit of the bicircular matroid. Directly: if two different components were present, discard one; hence its edge-bearing part is connected. It contains at least two independent cycles, but deleting any edge leaves at most one. In particular, its number \(e\) of edges equals its number \(v\) of incident vertices plus one: take a minimal connected subgraph containing two cycles (a theta or a joined pair of cycles); this is already non-pseudoforest and is equal to the whole edge set by minimality. Every incident vertex has degree at least two, since deleting a leaf edge would leave the two cycles. Let \(a\) and \(b\) be the numbers of incident left and right vertices. Then \(e=a+b+1\), and the bipartite degree sums give \(2a\le e\) and \(2b\le e\), so \(|a-b|\le1\). In particular, \(e\le2m+1\) when \(p=q=m\), whereas \(e\le2m+2\) for unequal alphabets, since the larger part can supply only one extra incident vertex. A bipartite simple graph with at most four incident vertices cannot contain two cycles, and the smallest minimal obstruction is \(K_{2,3}\), with six edges. If \(m=1\), no cycle exists. If \(p=q=2\), there is only a four-cycle and hence no violation.

**3. Realize all permitted even sizes.** The graph \(K_{2,3}\) is a theta: three internally disjoint paths between two degree-three vertices. Replace any edge by a path of length three, thereby adding one vertex to **each** bipartite part and two edges. This *double subdivision* preserves the theta structure, so all its proper edge subsets are pseudoforests. After \(t\) such operations the graph uses \((2+t,3+t)\) bipartite vertices and \(6+2t\) edges. For equal alphabets this fits for \(0\le t\le m-3\); for unequal alphabets place the \(3+t\)-vertex side in the larger alphabet and fit \(0\le t\le m-2\). Thus every even number in the asserted interval occurs.

**4. Realize all permitted odd sizes.** The graph obtained from \(K_{3,3}\) by deleting two disjoint edges is also a theta, with seven edges and three vertices on each side (the two unused endpoints of the deleted edges have degree two, the remaining two degree-three vertices are joined by three internally disjoint paths). Double-subdivide \(t\) edges to obtain a theta with \((3+t,3+t)\) bipartite vertices and \(7+2t\) edges. For \(m\ge3\), take \(0\le t\le m-3\). The odd sizes cover exactly the odd integers permitted by the upper bound. Together with Step 3 this proves the complete spectrum.

**5. First multiplicities and sharpness.** A six-edge minimal falsifier must use exactly two vertices of one color and three of the other, and necessarily be the entire \(K_{2,3}\). This yields \(\binom p2\binom q3+\binom p3\binom q2\). At seven edges the degree bounds force three vertices of each color. Its graph is obtained from \(K_{3,3}\) by removing two edges. The resulting graph is minimally bicyclic precisely when the removed edges are disjoint: if they meet, one vertex is degree one, and deleting its incident edge leaves two cycles. There are \(\binom32^2\cdot 2=18\) ordered disjoint missing-edge pairs (equivalently \(3!\binom32\)), giving \(18\binom p3\binom q3\). Finally, any violating finite team contains an inclusion-minimal violating subteam, so the maximum obstruction size furnishes a universal local cutoff. The theta constructions at that maximum prove no smaller cutoff suffices.

**Literal exact-size coherence consequence.** On a fixed rectangle with violations, the equivalence between team satisfaction and satisfaction of **all** \(k\)-element subteams holds iff all its inclusion-minimal falsifiers have cardinality exactly \(k\): if a minimal falsifier has smaller size than \(k\), the test is vacuous, while if it has larger size, every \(k\)-element subteam passes; the converse follows from downward closure and choosing a minimal falsifier. Hence unequal alphabets with smaller size exactly two are \(6\)-coherent in this restricted sense; every rectangle with smaller side at least three is not \(k\)-coherent for any positive \(k\), since both sizes six and seven occur. Rectangles without violations satisfy the equivalence for all positive \(k\).

## Verification

Run \(\texttt{python verify.py}\) using Python's standard library. The checker independently enumerates disjoint dependence-logic splits and checks the resulting pseudoforest criterion on 4,952 finite teams; then exhaustively enumerates minimal falsifiers in eight small rectangles, including all 65,536 teams on \(4\times4\), and compares both the full size spectrum and the two smallest coefficient formulas. It reports:

```text
direct team-semantics comparisons 4952
1x5: {}
2x2: {}
2x3: {6: 1}
2x4: {6: 4}
2x5: {6: 10}
3x3: {6: 6, 7: 18}
3x4: {6: 18, 7: 72, 8: 54}
4x4: {6: 48, 7: 288, 8: 432, 9: 816}
all checks passed
```

These are finite cross-checks, not a proof for unrestricted alphabet sizes; Steps 1–5 establish the general theorem.

## Relationship to prior work

Fröhlich, Kolaitis and Meier (2025) study the same inverse-dependence disjunction and prove qualitative global incoherence and model-checking results. Barlag and coauthors (2026) give the exact-size coherence definition and general coherence theory. The graph-theoretic pseudoforest characterization and bicircular-matroid circuit types are classical, and Neudauer and Stevens (2003) study **bases** of the bicircular matroid on complete bipartite graphs. These results are not presented as new. The present statement concerns the **complete cardinality spectrum of inclusion-minimal falsifiers at fixed alphabet sizes**, its optimal local test cutoff, and its first two exact counts; it is not a base-enumeration theorem. Primary sources were checked for this precise implication, but an equivalent parameterized circuit-spectrum statement in earlier graph or matroid work remains possible.

## Limitations

The formulas apply to two-variable inverse functional dependencies and binary *sets* of assignments. They do not classify other pairs of dependence atoms or count every minimal falsifier at cardinalities eight and above. The local cutoff refers to detecting failure using subteams **of at most** the specified size; it is not interchangeable with exact-size coherence. The finite experiments cover stated small rectangles only. The mathematical argument and the literature comparison have not undergone independent external review.

## References

1. Nicolas Fröhlich, Phokion G. Kolaitis, Arne Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146v1 (first posted 2025-08-22). https://arxiv.org/html/2508.16146v1
2. Timon Barlag, Nicolas Fröhlich, Miika Hannula, Phokion G. Kolaitis, Juha Kontinen, Arne Meier, Jouko Väänänen, *Aspects of Coherence in Dependence Logic*, arXiv:2605.31269v1 (first posted 2026-05-29). https://arxiv.org/abs/2605.31269
3. Nancy Ann Neudauer and Brett Stevens, *Enumeration of the Bases of the Bicircular Matroid on a Complete Bipartite Graph*, Ars Combinatoria 66 (2003), 165–178. https://combinatorialpress.com/article/ars/Volume%20066/volume-66-paper-14.pdf
4. Santiago Guzmán-Pro and Winfried Hochstättler, *Lattice Path Bicircular Matroids*, Graphs and Combinatorics 40 (2024), article 21, https://doi.org/10.1007/s00373-023-02749-2
