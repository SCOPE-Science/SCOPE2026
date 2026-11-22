# Edge-open-packing polynomials separate two cubic line graphs: four optimal Petersen orbits

## Finding

Let \(P=\mathrm{KG}(5,2)\) be the Petersen graph and let \(Q=C_5\square K_2\) be the pentagonal prism. For any finite simple graph \(G\), an **edge-open packing** is a set \(D\subseteq E(G)\) such that, for every two distinct edges \(e,f\in D\), there is no *third* edge \(g\in E(G)\setminus\{e,f\}\) joining an endpoint of \(e\) to an endpoint of \(f\). Define the complete edge-open-packing polynomial, including the empty set, by

\[
\mathcal E_G(z)=\sum_{D\subseteq E(G)\,\text{edge-open packing}}z^{|D|}.
\]

Then the two fifteen-vertex, thirty-edge, four-regular line graphs satisfy

\[
\boxed{\mathcal E_{L(P)}(z)=1+30z+225z^2+530z^3+330z^4},
\]
\[
\boxed{\mathcal E_{L(Q)}(z)=1+30z+235z^2+580z^3+415z^4}.
\]

Thus each has edge-open-packing number four, but the polynomial distinguishes them:

\[
\mathcal E_{L(Q)}(z)-\mathcal E_{L(P)}(z)=10z^2+50z^3+85z^4.
\]

Under the natural action of \(S_5\) on the two-element subsets defining \(P\), the \(330\) maximum edge-open packings of \(L(P)\) form **exactly four orbits of sizes \(30,60,120,120\)**. In the deterministic indexing specified below and implemented in `verify_recurrence.py`, representatives are

\[
\begin{array}{c|c|c}
\text{Orbit cardinality}&\text{Edge indices in }L(P)&\text{Star-forest edge sizes}\\
30&\{0,3,10,11\}&(2,2)\\
60&\{0,5,9,11\}&(2,2)\\
120&\{0,2,10,17\}&(2,1,1)\\
120&\{4,5,9,11\}&(2,2)
\end{array}.
\]

These are *labelled edge subsets*, not colorings or quotients by automorphisms. The final column records the numbers of selected edges in each connected component of the induced-star forest: 210 optima have two two-edge stars, while 120 have a two-edge star plus two isolated edges.

## Assumptions and scope

All graphs are finite, undirected, loopless, and simple. A line graph \(L(H)\) has one vertex for each edge of \(H\), and two vertices are adjacent when the original edges share an endpoint. The Petersen vertices are the ten two-subsets of \(\{0,1,2,3,4\}\), adjacent when disjoint. The pentagonal-prism vertices are \((r,i)\) with \(r\in\{0,1\}\), \(i\in\mathbb Z/5\mathbb Z\); its edges join consecutive positions in a row and corresponding positions between rows.

For the representative indices, first list the ten Petersen vertices in lexicographic order, list the fifteen Petersen edges as increasing pairs of vertex indices in lexicographic order, and finally list the thirty edges of the line graph as increasing pairs of original-edge indices in lexicographic order. An orbit representative \(\{i_1,i_2,i_3,i_4\}\) denotes these four line-graph edges.

The condition for a third joining edge is **not** equivalent to disjoint closed edge neighborhoods, nor to ordinary induced matching; adjacent chosen edges are permitted if no distinct third edge creates the forbidden relation.

## Proof

**1. Exact independent-set reduction.** For a graph \(H\in\{P,Q\}\), construct a simple conflict graph \(C(H)\). Its vertices are the thirty edges of \(L(H)\). Two of its vertices are adjacent precisely when a third edge of \(L(H)\), other than the corresponding pair, joins an endpoint of one to an endpoint of the other. By the definition of edge-open packing, the independent sets of \(C(H)\) are in bijection with the edge-open packings of \(L(H)\), preserving cardinality. Consequently

\[
\mathcal E_{L(H)}(z)=I_{C(H)}(z),
\]

where \(I_C(z)\) is the independent-set polynomial of the finite conflict graph.

**2. Exact finite recurrence.** For every induced conflict subgraph on a vertex set \(S\), define its independence polynomial \(F(S;z)\), with \(F(\varnothing;z)=1\). If \(v\in S\), partition independent sets according to whether they contain \(v\):

\[
F(S;z)=F(S\setminus\{v\};z)
+zF\big(S\setminus(\{v\}\cup N_C(v));z\big).
\]

This is an identity, not a heuristic or a finite-sampling assumption. In `verify_recurrence.py`, each graph is constructed directly from the defining ten-vertex graph, and all thirty conflict neighborhoods are calculated from the third-edge definition. The recurrence is evaluated with exact integer arithmetic and memoization. It visits \(437\) distinct masks for the Petersen conflict graph and \(388\) for the prism conflict graph. Its coefficient vectors are exactly

\[
(1,30,225,530,330)\quad\text{and}\quad(1,30,235,580,415).
\]

In particular no independent set with at least five vertices exists, and therefore both maximum packing numbers equal four. A basic count cross-check is that \(C(P)\) is fourteen-regular on thirty vertices, so its independent pairs number \(\binom{30}{2}-30\cdot14/2=225\); the prism conflict graph has twenty degree-thirteen vertices and ten degree-fourteen vertices, yielding \(\binom{30}{2}-(20\cdot13+10\cdot14)/2=235\).

**3. Symmetry classification.** Every permutation of the five symbols induces an automorphism of the Petersen graph, hence of its line graph and the associated conflict graph. The script constructs all \(120\) such induced permutations and applies them to every four-element independent set of \(C(P)\). Direct orbit enumeration, with exact set comparisons, produces four disjoint orbits of respective sizes \(30,60,120,120\); their union has \(330\) sets, exactly all four-element independent sets. The representative table is obtained by choosing the numerically smallest bit-mask representative in each orbit, and thereby specifies the classes without requiring a drawn embedding.

**4. Independent exhaustive cross-check.** The second implementation, `verify_direct.py`, constructs \(P\) in the *outer pentagon/inner pentagram/spokes* representation, rather than from disjoint two-subsets. For both graphs it tests the third-edge relation directly by scanning the thirty line-graph edges, and checks every \(k\)-subset of the thirty possible line-graph edges for \(0\le k\le5\). The resulting counts are

\[
\begin{array}{c|rrrrrr}
&k=0&1&2&3&4&5\\
L(P)&1&30&225&530&330&0\\
L(Q)&1&30&235&580&415&0
\end{array}.
\]

Since the property is hereditary under taking subsets, the exhaustive exclusion of all five-edge packings independently rules out every larger packing. The two implementations agree coefficientwise and on the conflict-degree diagnostics. Both are standalone Python standard-library programs embedded with the finding.

## Verification

Run `python3 verify_recurrence.py` and `python3 verify_direct.py` from the directory containing the embedded program files. Exact captured outputs are `recurrence_output.txt` and `direct_output.txt`. Both scripts terminate with dedicated success markers after checking the full coefficient identities; the first also checks all orbit memberships and cardinalities. The second enumerates all \(\binom{30}{5}=142506\) five-element candidate subsets for each graph, not a sample. No randomness, external data, proprietary solver, or floating-point tolerance enters the proof.

## Relationship to prior work

Chelladurai, Kalimuthu, and Soundararajan introduced edge-open packing and computed it for standard graphs, including **the Petersen graph itself**, in their 2022 paper. Their result for \(P\) does not determine edge-open packings of its **line graph** \(L(P)\). Brešar and Samadi's March 1, 2024 preprint develops complexity, tree algorithms, extremal bounds, and edge-deletion behavior; its structural induced-star observation motivates counting such configurations but does not provide either polynomial or the orbit census above. Literature on injective edge coloring concerns partition of all edges into packing classes, which does not determine the complete counts of individual classes. Published analyses of edge-open packings of triangular graphs \(L(K_m)\) concern different original graphs; \(P\) is not complete. Searches for `edge open packing line graph Petersen`, `injective edge-coloring of the Petersen line graph`, and `Petersen line graph edge-open packing polynomial` did not identify an implication covering these statements.

## Limitations

This is a finite exact result for two particular line graphs, not a formula for all line graphs of cubic graphs, nor for generalized Petersen families. The assertions about historic priority are necessarily provisional: an unindexed computational catalogue could contain the same counts. The proof has two reproducible independent enumerations, but no independent mathematical audit or human expert certification has been performed.

## References

1. G. Chelladurai, K. Kalimuthu, and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research **56** (2022), 3765–3776. DOI: https://doi.org/10.1051/ro/2022171 ; lawful open-access full text https://www.numdam.org/item/10.1051/ro/2022171.pdf .
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750, first posted **2024-03-01**, https://arxiv.org/abs/2403.00750 .
