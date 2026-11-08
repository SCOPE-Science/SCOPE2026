# Exact open-neighborhood shattering polynomials of rectangular rook graphs

## Finding
Let \(m,n\ge1\) be integers and let \(R_{m,n}=K_m\square K_n\) be the graph on \([m]\times[n]\), with distinct cells adjacent exactly when they share a row or a column. Let \(\mathcal N_{m,n}=\{N_{R_{m,n}}(v):v\in[m]\times[n]\}\) consist of **open** neighborhoods, and write \(\Phi_{m,n}(z)=\sum_{j\ge0}s_j(m,n)z^j\), where \(s_j\) counts the \(j\)-element subsets shattered by \(\mathcal N_{m,n}\). Put \(\binom ab=0\) if \(a<b\). Then
\[
\begin{aligned}
s_0(m,n)&=1,\\
s_1(m,n)&=mn\,\mathbf 1_{\{mn\ge2\}},\\
s_2(m,n)&=\mathbf1_{\{m\ge2,n\ge3\}}m\binom n2
+\mathbf1_{\{n\ge2,m\ge3\}}n\binom m2\\
&\quad+\mathbf1_{\{m,n\ge2,\max(m,n)\ge3\}}2\binom m2\binom n2,\\
s_3(m,n)&=\mathbf1_{\{m\ge2,n\ge4\}}\left[m\binom n3+m(m-1)\binom n2(n-2)\right]\\
&\quad+\mathbf1_{\{n\ge2,m\ge4\}}\left[n\binom m3+n(n-1)\binom m2(m-2)\right],\\
s_j(m,n)&=0\qquad(j\ge4).
\end{aligned}
\]
In particular, the VC dimension equals zero on \(1\times1\), equals one on every nontrivial one-row or one-column graph and on \(2\times2\), equals two for \(m,n\ge2\) with \(\max(m,n)=3\), and equals three for \(m,n\ge2\) with \(\max(m,n)\ge4\). Thus the smallest board realizing dimension three is \(2\times4\), up to transposition. Its polynomial is \(1+8z+24z^2+32z^3\).

**Exact structural classification.** Regard a nonempty support \(S\) as edges of the bipartite graph on row vertices and column vertices, deleting isolated vertices. A pair is shattered precisely when it has one of these forms: a two-edge row star, with \(m\ge2,n\ge3\); a two-edge column star, with \(n\ge2,m\ge3\); or two independent edges, with \(m,n\ge2\) and \(\max(m,n)\ge3\). A triple is shattered precisely when it has one of four forms: a three-edge row star, with \(m\ge2,n\ge4\); a three-edge column star, with \(n\ge2,m\ge4\); a two-edge row star together with a disjoint edge, with \(m\ge2,n\ge4\); or the transposed two-edge column star together with a disjoint edge, with \(n\ge2,m\ge4\). No other nonempty supports are shattered beyond singletons when \(mn\ge2\).

## Assumptions and scope
All graphs are finite simple undirected graphs. The graph has \(mn\) distinct vertices, and a center is excluded from its own open neighborhood. A support \(S\) is shattered if each of its \(2^{|S|}\) subsets is the trace \(N(v)\cap S\) of **some vertex center of this same graph**. There are no empty/full hypotheses added beyond the actual open neighborhoods. We count labeled (coordinate-position) support subsets, not isomorphism classes. The convention \(\binom ab=0\) for \(a<b\) only concerns nonnegative integral top arguments, and all parameter ranges are explicit above.

## Proof
**Cut-incidence reduction.** Regard \(S\subseteq[m]\times[n]\) as an edge subset \(F\subseteq E(K_{m,n})\), where cell \((i,j)\) represents edge \(r_i c_j\). A query center \((a,b)\) gives the Boolean trace
\[
\{r_i c_j\in F:(i=a)\mathbin{\mathrm{xor}}(j=b)\}=\delta_F(\{r_a,c_b\}),
\]
the cut of \(F\) induced by the two-element root set \(\{r_a,c_b\}\). This identity accounts for the exclusion of the center itself; the two incidence stars overlap at their shared cell and cancel there. It also supplies a direct proof-replay criterion.

**One- and two-point supports.** Every cell in a board of size at least two has a neighbor, while its own center gives the empty trace; hence the singleton count. For two cells in one row, a center in that row but in a third column realizes both, centers in a distinct row using one of the two columns realize singletons, and a distinct row with a third column realizes the empty trace. These witnesses exist exactly when \(m\ge2,n\ge3\). There are \(m\binom n2\) such pairs. Interchanging coordinates gives the column contribution. For cells in distinct rows and columns, centers at the opposite corners realize both; a center in a selected cell gives empty; to realize the two separate singletons requires at least one unused row or column, hence \(m,n\ge2\) with \(\max(m,n)\ge3\). There are \(2\binom m2\binom n2\) such diagonally separated pairs. This exhausts all pair patterns and proves the formula for \(s_2\).

**Three-point support shapes.** There are exactly four isomorphism types of bipartite three-edge graphs without isolated vertices: a star with three leaves; a path with three edges; a two-edge star plus an independent edge; and three independent edges. (The transposed star placements are counted separately by the side of the bipartition.) A three-edge path cannot give the full trace: cutting all of its edges forces one entire color class of the connected path to be selected, which needs two roots of the same bipartition class, whereas a center selects one row root and one column root. Three independent edges cannot give the full trace either: a center has only two roots. Therefore only stars and a two-edge star plus an independent edge are candidates.

For a row star with selected cells \((r_1,c_1),(r_1,c_2),(r_1,c_3)\), its full trace requires an unused fourth column \(c_4\); its empty and singleton traces require a second row \(r_2\). When these exist, the following centers realize all eight traces: \((r_2,c_4)\) realizes empty; \((r_2,c_i)\) realizes singleton \(i\); \((r_1,c_i)\) realizes the other two selected cells; and \((r_1,c_4)\) realizes all three. Thus exactly \(m\binom n3\) such supports are shattered if \(m\ge2,n\ge4\). The column-star case is the transpose.

For a two-edge row star plus a disjoint edge, name the cells \(e_1=(r_1,c_1)\), \(e_2=(r_1,c_2)\), \(e_3=(r_2,c_3)\), with distinct rows and columns as indicated. The trace \(\{e_1,e_2\}\) needs \((r_1,c_4)\) with \(c_4\notin\{c_1,c_2,c_3\}\); thus a fourth column is necessary. The eight traces are supplied respectively by: \(\emptyset:(r_2,c_3)\); \(\{e_1\}:(r_1,c_2)\); \(\{e_2\}:(r_1,c_1)\); \(\{e_3\}:(r_2,c_4)\); \(\{e_1,e_2\}:(r_1,c_4)\); \(\{e_1,e_3\}:(r_2,c_1)\); \(\{e_2,e_3\}:(r_2,c_2)\); and \(\{e_1,e_2,e_3\}:(r_1,c_3)\). These exist precisely when \(m\ge2,n\ge4\). Choose the repeated row, the other row, the two leaf columns, and the third column: \(m(m-1)\binom n2(n-2)\) choices. Transposition gives the remaining term and proves \(s_3\).

**No four-point support.** The established open-neighborhood VC bound for Hamming graphs, Adler–Benediktsson–Macpherson [1, Theorem 4.6], is \(\operatorname{VCdim}\le3\). The rectangular rook graph is an induced subgraph of the homogeneous two-coordinate Hamming graph \(H(2,q)\), where \(q=\max(m,n)\). For any support in an induced subgraph, every neighborhood trace attained there is also attained in the containing Hamming graph; consequently, shattering of four points in a rook graph would contradict that published theorem. This shows \(s_j=0\) for all \(j\ge4\) and completes the proof. The preceding triple witnesses show sharpness on all boards with two rows and four columns or larger after possible transposition.

## Verification
The standalone standard-library program `VERIFY.py` constructs the rook adjacency relation directly, enumerates every Boolean neighborhood trace for every support of cardinality one through three on all \(36\) boards with \(1\le m\le n\le8\), and compares with the coefficient formulas. It independently checks the four triple support types for all tested boards. It also tests every four-element support on a substantial specified subset of boards, obtaining \(250441\) individual four-point exclusions. The observed output is `ALL_RECTANGULAR_ROOK_OPEN_SHATTERING_CHECKS_PASS`. The exact enumeration covers \(177840\) supports of cardinality one through three. These finite observations are corroboration, not the proof of unbounded parameter claims; the full upper bound relies on the cited universal Hamming theorem and the induced-subgraph implication.

## Relationship to prior work
Adler, Benediktsson and Macpherson [1] explicitly study the open-neighborhood edge relation on Hamming graphs, prove the universal VC bound of three in Theorem 4.6, identify the threshold for homogeneous Hamming graphs in Theorem 4.7, and investigate VC density. Section 1 also describes rook graphs as related local structures. These results give an essential prior upper bound; neither their dimension theorem nor the examples for equal-alphabet Hamming graphs provide the coefficientwise number and classification of all shattered pairs and triples on arbitrary rectangular rook graphs. The specialization to equal sides and all prior VC bounds are not claimed as new. Coudert and collaborators [2] primarily compute graph VC dimension for **closed** neighborhoods and do not furnish the present **open** neighborhood census. The mathematical contribution assessed here is the full bivariate support profile together with the four structural triple patterns, including unequal-side boundary behavior.

## Limitations
This result concerns open neighborhoods of **vertices in the complete rectangular rook graph**; it does not classify arbitrary induced subgraphs, radius-two neighborhoods, closed neighborhoods, adaptive Littlestone dimension, or arbitrary line graphs. The originality comparison rests on accessible full-text primary sources and mathematical-index searches; historical priority under alternative language (edge-incidence trace systems, line-graph neighborhood shattering, lattice-graph traces) may require further specialist verification. Finite exhaustive checks do not independently establish the universal Hamming bound from [1]. The all-parameter correctness proof invokes that published theorem in addition to the self-contained small-support classification.

## References
[1] I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1 (first public version 2020-07-31), especially Section 4, Theorems 4.6–4.8. https://arxiv.org/html/2007.16042

[2] D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1 (first public version 2024-05-13), especially Sections 1–2, 4–6. https://arxiv.org/html/2405.07588
