# The eight-parameter cube threshold for odd torsion in Henson type compatibility

## Finding
Let \(\mathcal H_4\) be the countable homogeneous universal graph omitting \(K_4\). For any finite *triangle-free* induced subgraph \(G\), individually name all its vertices. Index the integral matrix \(M_G\) by all complete nonalgebraic one-point types over \(G\), and put \((M_G)_{S,T}=1\) exactly when the types \(S,T\) have distinct *adjacent* realizations in \(\mathcal H_4\).

**Sharp first-occurrence and uniqueness theorem.** If \(|V(G)|\le7\), the torsion subgroup of \(\operatorname{coker}_{\mathbb Z}(M_G)\) is a \(2\)-group. If \(|V(G)|=8\), nontrivial odd-primary torsion occurs **if and only if** \(G\cong Q_3\), the three-dimensional cube graph. For this sole eight-vertex exception, the matrix has size \(256\times256\), and
\[
\operatorname{SNF}_{\mathbb Z}(M_{Q_3})
=\operatorname{diag}(I_{106},2I_{11},6,0_{138}),
\quad
\operatorname{inertia}_{\mathbb R}(M_{Q_3})=(60,58,138).
\]
In particular its rational rank is \(118\), its ranks in characteristics \(2\) and \(3\) are respectively \(106\) and \(117\), and in every other prime characteristic its rank is \(118\). Its integral cokernel is \(\mathbb Z^{138}\oplus (\mathbb Z/2\mathbb Z)^{11}\oplus\mathbb Z/6\mathbb Z\).

## Assumptions and scope
An old parameter graph is a finite, simple, loopless, undirected, triangle-free graph \(G=(V,E)\), included as an *induced*, individually named subgraph of \(\mathcal H_4\). Because every subset of a triangle-free graph is triangle-free, the nonalgebraic one-point types are precisely the \(2^{|V|}\) sets \(S\subseteq V\) recording the named neighbors of the new vertex. The compatibility relation is existence of two distinct *adjacent* realizations, not a prescribed simultaneous arrangement of three or more new vertices. For an induced vertex set \(U\), write \(I_{G[U]}(t)=\sum_{J\subseteq U\,\mathrm{independent}}t^{|J|}\), including the empty set. The result gives an exact finite first-occurrence threshold, not a bound on possible torsion at arbitrary larger orders.

## Proof
**1. Finite type and compatibility lemma.** In the homogeneous \(K_4\)-free graph, the free one-point extension property allows any proposed neighbor set that induces no triangle. Since \(G\) itself is triangle-free, every \(S\subseteq V\) occurs. For types \(S,T\), add distinct vertices \(x,y\), give them old neighbors \(S,T\), and require \(xy\) to be an edge. The resulting graph is \(K_4\)-free if and only if \(G[S\cap T]\) has no edge: a forbidden quadruple must consist of \(x,y\) together with an adjacent pair in their common old neighborhood. The extension property realizes each allowed finite graph. Thus
\[
(M_G)_{S,T}={\bf1}_{\{S\cap T\ \mathrm{independent}\}}.
\]

**2. Integral reduction.** Order subsets by cardinality, refine arbitrarily, and set \(Z_{S,U}={\bf1}_{\{U\subseteq S\}}\). This integral Boolean-zeta matrix is lower unitriangular and has determinant \(1\). Boolean Möbius inversion of \(f(W)={\bf1}_{\{W\text{ independent}\}}\) gives \(h(U)=\sum_{W\subseteq U}(-1)^{|U|-|W|}f(W)=(-1)^{|U|}I_{G[U]}(-1)\). Entrywise,
\[
M_G=Z\,\operatorname{diag}\bigl(h(U):U\subseteq V\bigr)\,Z^{\mathsf T}.
\]
Both outside matrices are unimodular. Consequently the integral cokernel and the elementary prime-primary torsion are determined by all nonzero induced independence sums. In particular, odd-primary torsion appears exactly when some nonzero \(I_{G[U]}(-1)\) has an odd prime divisor. The signs of the \(h(U)\) determine real inertia. This general factorization is established machinery and is not a novelty claim.

**3. Finite minimality and uniqueness certificate.** The attached reproducible program `verify_cube_threshold.py` exhaustively constructs all triangle-free graphs of orders \(1,\ldots,8\) *up to isomorphism*. Begin with the empty graph. For every representative on \(n\) vertices, adjoin one new vertex whose neighbor set is independent; all triangle-free graphs on \(n+1\) vertices arise this way by deleting an arbitrary vertex. Group candidates by graph invariants only for speed; within each group, the program tests full adjacency-preserving graph isomorphism by exhaustive injective backtracking. It retains one representative per actual isomorphism class. Thus collisions in the preliminary invariants cannot cause missing classes. The generated class counts are exactly
\[
(1,2,3,7,14,38,107,410)
\]
for orders \(1,\ldots,8\), independently agreeing with the standard published triangle-free graph counts. The verified ranges of \(I_G(-1)\) through seven vertices are contained in \(\{-1,0,1,2\}\); for order eight the complete distribution over the \(410\) isomorphism classes is
\[
\begin{array}{c|rrrrrr}
I_G(-1)&-2&-1&0&1&2&3\\\hline
\#\text{ classes}&1&35&253&111&9&1.
\end{array}
\]
There is no class with value \(-3\) or magnitude greater than \(3\). The unique class with value \(3\) is graph-isomorphic (by the full tester) to the Hamming cube \(Q_3\) on three-bit strings, with edges at Hamming distance one. The program independently checks every order-eight class's alternating independent-subset sum by exhaustive subset enumeration, separate from its deletion recurrence. Every induced graph of a graph with at most seven vertices is covered; for an eight-vertex graph, all its proper induced subgraphs are covered. Therefore \(Q_3\) uniquely first produces odd torsion, using the equivalence in Step 2.

**4. Full eight-vertex matrix invariants.** A direct Hamming-cube independent-set count gives
\[
I_{Q_3}(t)=1+8t+16t^2+8t^3+2t^4,
\qquad I_{Q_3}(-1)=3.
\]
For all \(256\) vertex subsets \(U\) of the cube, the exact induced \(I_{Q_3[U]}(-1)\) value histogram is \(-1:50\), \(0:138\), \(1:55\), \(2:12\), \(3:1\). Thus the diagonal form in Step 2 has \(105\) unit-magnitude entries, \(12\) entries of magnitude \(2\), one entry of magnitude \(3\), and \(138\) zeros. Its nonzero Smith factors follow because \(\mathbb Z/2\oplus\mathbb Z/3\cong\mathbb Z/6\), yielding \(106\) factors \(1\), \(11\) factors \(2\), one factor \(6\), and \(138\) zeros. The diagonal signs \((-1)^{|U|}I_{G[U]}(-1)\) give \(60\) positive and \(58\) negative entries, and hence the displayed real inertia by Sylvester's law.

## Verification
Run `python3 verify_cube_threshold.py` with Python's standard library; no downloaded database or external package is required. `verification_output.txt` is the output from the embedded script. It verifies complete graph-class generation through eight vertices (including the independently tabulated class counts), full isomorphism matching to the cube, two independent evaluations of \(I_G(-1)\) for all \(410\) order-eight classes, all \(256\) cube induced subsets, the exact Boolean-zeta identity for all \(65{,}536\) entries of the cube type matrix, the induced-value histogram, and the signed inertia count. The run ends in `VERIFY_OK`. The complete finite enumeration is the proof of this finite threshold once coupled with Steps 1–2; no inference about larger graphs follows solely from this computation.

## Relationship to prior work
Henson established the homogeneous forbidden-clique extension setting. Levit and Mandrescu (2009) developed bounds on the alternating independence sum at \(-1\), including general bounds by graph cycle structure. Cutler and Kahl (2014) studied which values can occur in classes controlled by decycling number. The cube independence polynomial and the counts of unlabeled triangle-free graphs are individually recorded in existing sequence and graph tables, so neither basic datum is claimed as novel. Boolean meet-matrix diagonalization is classical. Previously reported type-compatibility classifications for chordal and unicyclic bases already use the same integral congruence, and establish unit-only and at-most-two torsion in those restricted families. They cannot imply the present **minimum order and unique multi-cycle extremizer among all triangle-free bases** or the cube's full logical Smith form without additional classification. The present contribution is their sharp first *odd-primary* obstruction across the unrestricted triangle-free finite-base age, with a reproducible complete borderline census. The possibility of an unindexed equivalent cube extremality theorem remains a residual priority risk.

## Limitations
The exhaustiveness statement covers simple triangle-free graphs with at most eight named vertices, not all finite bases at larger orders, not bases containing triangles, and not the analogous logical matrices for larger forbidden cliques or different arities. The complete class-enumeration program's correctness relies on the supplied transparent generator, exact graph-isomorphism backtracking and independent alternating-subset computation; finite computation is used only for the stated finite threshold. The source search does not prove global historical priority. Independent mathematical audit has not been performed.

## References
1. C. W. Henson, *A family of countable homogeneous graphs*, Pacific Journal of Mathematics 38 (1971), 69–83. https://msp.org/pjm/1971/38-1/pjm-v38-n1-p09-s.pdf
2. V. E. Levit and E. Mandrescu, *The independence polynomial of a graph at \(-1\)*, arXiv:0904.4819v1 (first public April 30, 2009). https://arxiv.org/html/0904.4819v1
3. J. Cutler and N. Kahl, *A note on the values of independence polynomials at \(-1\)*, arXiv:1410.7726v1 (first public October 28, 2014). https://arxiv.org/html/1410.7726v1
4. OEIS A354802, cube independence polynomials (coefficient tabulation). https://oeis.org/A354802
5. E. W. Weisstein, *Triangle-Free Graph*, MathWorld (unlabeled graph enumeration). https://mathworld.wolfram.com/Triangle-FreeGraph.html
