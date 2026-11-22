# Total-domination spectra of two-token complete bipartite graphs

## Finding

For integers \(2\le r\le t\), let \(H_{r,t}=F_2(K_{r,t})\) be the graph of unordered pairs of distinct vertices of \(K_{r,t}\), with two pairs adjacent if a single token may move along a host edge. Define
\[
T_{r,t}(z)=\sum_{D\subseteq V(H_{r,t})\atop D\text{ totally dominating}}z^{|D|},\qquad
M_{r,t}(z)=\sum_{D\subseteq V(H_{r,t})\atop D\text{ inclusion-minimal totally dominating}}z^{|D|}.
\]
Thus every vertex, including a selected one, must have a neighbour in \(D\); inclusion-minimal means no proper subset remains totally dominating. The following formulas determine *both polynomials* for all \(r,t\).

Define the no-empty-row-or-column polynomial
\[
U_{a,b}(z)=\sum_{i=0}^{a}\sum_{j=0}^{b}(-1)^{i+j}\binom ai\binom bj(1+z)^{(a-i)(b-j)},
\]
and the complete-graph edge-cover polynomial
\[
E_s(z)=\sum_{i=0}^{s}(-1)^i\binom si(1+z)^{\binom{s-i}{2}}.
\]
Put
\[
\begin{aligned}
X_{r,t}(z)&=\sum_{a=r-1}^{r}\sum_{b=t-1}^{t}\binom ra\binom tb U_{a,b}(z),\\
Y_{r,t}(z)&=E_r(z)(1+z)^{\binom t2}+E_t(z)(1+z)^{\binom r2}-E_r(z)E_t(z).
\end{aligned}
\]
Then **the complete total-domination polynomial factors** as
\[
\boxed{T_{r,t}(z)=X_{r,t}(z)Y_{r,t}(z).}
\]

Let \(\left\{\!\begin{smallmatrix}a\\b\end{smallmatrix}\!\right\}\) denote a Stirling number of the second kind, taken as zero when \(b>a\). Define two formal power-series coefficient polynomials
\[
\begin{aligned}
J_s(z)&=s![x^s]\exp\left(\frac{zx^2}{2}+\sum_{j\ge3}\frac{x^jz^{j-1}}{(j-1)!}\right),\\
\Phi_{p,q}(z)&=p!q![u^pv^q]\exp\left(u(e^{zv}-1)+v(e^{zu}-1-zu)\right).
\end{aligned}
\]
All coefficients are finite at the prescribed degree; the second expression counts spanning bipartite star forests on labelled shores of sizes \(p,q\), including single-edge components once. The **complete inclusion-minimal polynomial** is
\[
\boxed{
M_{r,t}(z)=\left(rt\Phi_{r-1,t-1}(z)+t\,r!\left\{\!\begin{smallmatrix}t-1\\r\end{smallmatrix}\!\right\}z^{t-1}\right)\left(J_r(z)+J_t(z)\right).
}
\]

In particular, the minimum total-domination number and maximum cardinality of an inclusion-minimal total dominating set (upper total-domination number) are
\[
\boxed{\gamma_t(H_{r,t})=t-1+\left\lceil\frac r2\right\rceil},\qquad
\boxed{\Gamma_t(H_{r,t})=\begin{cases}2t-2,&r\in\{2,3\},\\r+2t-5,&r\ge4.\end{cases}}
\]
The exact number of minimum total dominating sets is
\[
\boxed{
t\,r!\left(\left\{\!\begin{smallmatrix}t-1\\r-1\end{smallmatrix}\!\right\}+\left\{\!\begin{smallmatrix}t-1\\r\end{smallmatrix}\!\right\}\right)
\left(e_r+\mathbf1_{\{\lceil t/2\rceil=\lceil r/2\rceil\}}e_t\right),
}
\]
where
\[
e_s=\begin{cases}\dfrac{s!}{2^{s/2}(s/2)!},&s\text{ even},\\[5pt]
s\binom{s-1}{2}\dfrac{(s-3)!}{2^{(s-3)/2}((s-3)/2)!},&s\text{ odd}.\end{cases}
\]
For example,
\[
M_{3,3}(z)=108z^4,\quad
M_{3,4}(z)=576z^5+384z^6,\quad
M_{4,4}(z)=576z^5+1632z^6+1152z^7.
\]

## Assumptions and scope

The host is the finite, labelled, simple, undirected complete bipartite graph \(K_{r,t}\), with both shore sizes at least two and \(r\le t\). Tokens are indistinguishable, cannot occupy the same host vertex, and move along one host edge at a time. The set variable \(z\) marks selected vertices of the token graph, not edges of the host. Formulae count labelled configurations: neither shore permutations nor graph automorphisms identify different vertex subsets. The two statistics concern total domination (open-neighbourhood coverage), not ordinary domination. All identities are exact for all indicated integers.

## Proof

**1. The two independent requirements.** Write the host shores as \(A=[r]\) and \(B=[t]\). The vertices of \(H_{r,t}\) form two token-graph bipartition classes: the \(rt\) cross pairs \(\{a,b\}\) with \(a\in A,b\in B\), and the \(\binom r2+\binom t2\) same-shore pairs. Every token-graph edge runs between these two classes. Partition any selected set \(D\) as \(D_X\) (cross pairs) and \(D_Y\) (same-shore pairs). Therefore total domination is equivalent to two independent coverage constraints, one on each selected part.

A same-shore pair \(\{a,a'\}\) is adjacent exactly to cross pairs with first coordinate \(a\) or \(a'\). Thus all same-shore pairs on \(A\) have neighbours in \(D_X\) precisely when at most one row of the \(r\times t\) incidence matrix of \(D_X\) is empty. The analogous condition on \(B\) is at most one empty column. A cross pair \(\{a,b\}\) is adjacent to a selected same-shore pair precisely when \(a\) is covered by the selected edges of \(K_r\), or \(b\) is covered by the selected edges of \(K_t\). Every cross pair is dominated if and only if *at least one* of those two selected edge families covers its entire shore: if both have an uncovered vertex, their cross pair is undominated. No selected cross pair can dominate another cross pair, and no same-shore pair can dominate another same-shore pair; the two requirements are necessary even for selected vertices.

**2. Counting all total dominating sets.** Fixing sets of \(a\) nonempty rows and \(b\) nonempty columns, inclusion-exclusion counts their nonempty \(a\times b\) incidence matrices by \(U_{a,b}(z)\). The coverage rule requires \(a\in\{r-1,r\}\) and \(b\in\{t-1,t\}\), giving \(X_{r,t}(z)\). Inclusion-exclusion over isolated vertices in the chosen edge set of \(K_s\) gives \(E_s(z)\). A chosen same-shore edge family is valid if it covers all of \(A\), all of \(B\), or both. The union formula gives \(Y_{r,t}(z)\), subtracting their intersection once. Independent choices multiply, proving the first boxed identity.

**3. Inclusion-minimal same-shore selections.** If selected edges on \(A\) cover all of \(A\), any edges selected on \(B\) are redundant, and conversely. Hence a minimal valid same-shore selection is *pure*: an inclusion-minimal edge cover of \(K_r\) or an inclusion-minimal edge cover of \(K_t\). In any graph, an edge cover is inclusion-minimal exactly when every selected edge has an endpoint of selected degree one. A graph of minimum selected degree one with that property has each connected component a star: a path of three edges would contain a middle edge whose endpoints both have degree at least two. A two-vertex star has exactly one representation; a star on \(j\ge3\) labelled vertices has \(j\) choices of center. The labelled exponential formula thus gives the degree-marked polynomial \(J_s(z)\), establishing the factor \(J_r(z)+J_t(z)\).

**4. Inclusion-minimal cross selections.** Let the selected cross pairs be a bipartite graph on the \(r+t\) labelled host vertices. Exactly zero or one isolated vertex is allowed on either shore. If neither shore has an isolated vertex, any selected edge can be deleted while preserving at most one isolated vertex on each shore, so such a selection cannot be minimal. If exactly one vertex on each shore is isolated, deleting any selected edge must create a second isolated vertex on some shore. Equivalently, every selected edge has an endpoint of selected degree one; the nonisolated subgraph is precisely a disjoint union of bipartite stars. Choose the isolated vertices in \(rt\) ways, then count the spanning star forests on the remaining \((r-1,t-1)\) vertices by \(\Phi_{r-1,t-1}(z)\). The bipartite-star exponential formula avoids counting single edges twice: all stars with one left vertex are in \(u(e^{zv}-1)\), and stars with a right center and at least two left leaves are in \(v(e^{zu}-1-zu)\).

If the left shore has no isolated vertex and the right has exactly one, removal of a selected edge is critical if and only if its right endpoint has selected degree one. Thus each of the \(t-1\) used right vertices has exactly one edge, and the assignment of its left endpoint is surjective onto all \(r\) left vertices. There are \(t\,r!\left\{\!\begin{smallmatrix}t-1\\r\end{smallmatrix}\!\right\}\) such choices, of size \(t-1\). The opposite asymmetric case would require \(r-1\) used left vertices to cover all \(t\) right vertices, which is impossible because \(r\le t\). These are exhaustive, and multiplying by the independent minimal same-shore selections proves the second boxed identity.

**5. Minimum, multiplicity and upper extreme.** Any valid cross selection has at least \(t-1\) cells, because at least \(t-1\) columns must be occupied. At equality there is exactly one cell in each used column, and its map into the \(r\) rows must use \(r-1\) or \(r\) values. The Stirling count is \(t r!\bigl(\left\{\!\begin{smallmatrix}t-1\\r-1\end{smallmatrix}\!\right\}+\left\{\!\begin{smallmatrix}t-1\\r\end{smallmatrix}\!\right\}\bigr)\). A same-shore selection needs at least \(\lceil r/2\rceil\) edges; this is attained with an edge cover of \(K_r\). A cover of \(K_t\) can tie precisely when \(\lceil t/2\rceil=\lceil r/2\rceil\). The number \(e_s\) of minimum edge covers is the number of perfect matchings when \(s\) is even. When \(s\) is odd, there is exactly one selected-degree-two center, two leaves attached to it, and a perfect matching on the remaining vertices; this yields the stated odd expression. These observations prove the minimum and its multiplicity.

A minimal edge cover of \(K_t\) has at most \(t-1\) edges, attained by a star. For minimal cross choices, the asymmetrical surjections use exactly \(t-1\) edges. A spanning bipartite star forest on shore sizes \((r-1,t-1)\) has \((r-1)+(t-1)-c\) edges, where \(c\) is its number of components. If \(r=2\), the single left vertex forms one star and the maximum is \(t-1\); if \(r=3\), two left vertices require at least two components (because \(t-1\ge2\)), giving maximum \(t-1\). If \(r\ge4\), both remaining shores have at least three vertices, so at least two components are needed, giving maximum \(r+t-4\), attained by two stars whose centers lie on opposite shores. Adding the independent maximum \(t-1\) same-shore contribution proves the upper total-domination number.

## Verification

The standalone Python 3 program `verify.py` calculates the all-set polynomials by inclusion-exclusion, the minimal-set polynomials by a labelled star-forest recurrence, and independently enumerates cross/same-shore selections for \((r,t)\in\{(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)\}\). For \((2,2),(2,3),(2,4),(3,3)\) it additionally generates the entire two-token adjacency graph and exhaustively checks the open-neighbourhood condition for every vertex subset, with no use of the factorization. It verifies the predicted minimum size and multiplicity. The checker prints `VERIFY_OK` only if every assertion passes. In particular, the exact minimal-set polynomials include \(M_{3,3}(z)=108z^4\), \(M_{3,4}(z)=576z^5+384z^6\), and \(M_{4,4}(z)=576z^5+1632z^6+1152z^7\). The general theorem is proved by the preceding structural arguments; the finite replay is corroboration, not an extrapolation.

## Relationship to prior work

Acosta Troncoso, Caldera Caldera and Rivera (arXiv:2610.31557, October 22, 2026) give a complete characterization of **ordinary** dominating sets of \(F_2(K_{r,t})\) and determine the ordinary domination number, including two exceptions. Their bipartite token-state decomposition is acknowledged; it does not give the present open-neighbourhood enumerators, minimal-total-domination star-forest classification or upper total-domination number. Chinman and collaborators (arXiv:2610.28936, October 20, 2026) independently establish ordinary domination numbers; the available abstract does not claim total-domination enumerators. Benítez-Bobadilla and collaborators (arXiv:2611.15124, November 11, 2026) study ordinary domination on the same family and on higher-token graphs; their Section 3.1 does not give total-domination formulas. This distinction matters: the ordinary and total domination numbers differ at the published exceptional parameter pairs. Related work on total domination in Johnson graphs (arXiv:2610.04675) concerns token graphs of complete graphs, not complete bipartite hosts. No universal priority guarantee is asserted.

## Limitations

Only two tokens, complete bipartite host graphs, and shore sizes at least two are covered. The formulas count labelled selected sets, not orbit classes. They concern total dominating sets and inclusionwise minimal total dominating sets, not distances or reconfiguration dynamics. The finite verifier checks only the stated small parameters; all-parameter validity follows from the proof. Although targeted literature and mathematical-record comparisons did not identify a covering exact total-domination census for this host family, earlier unindexed combinatorial enumeration may exist. Independent mathematical validation and historical-priority confirmation have not been performed.

## References

1. E. Acosta Troncoso, I. Caldera Caldera and L. M. Rivera, *The domination number of the 2-token graph of the complete bipartite graph*, arXiv:2610.31557 (first submitted 2026-10-22), https://arxiv.org/abs/2610.31557.
2. N. Chinman, A. Cortijo, B. Pedroni, I. Seong and L. Stenger, *The domination number of the k-token graph of the complete bipartite graph*, arXiv:2610.28936 (first submitted 2026-10-20), https://arxiv.org/abs/2610.28936.
3. G. Benítez-Bobadilla, F. E. Contreras-Mendoza, S. G. Gómez-Galicia and A. Trujillo-Negrete, *Domination in token graphs of graphs with domination number two*, arXiv:2611.15124 (first submitted 2026-11-11), https://arxiv.org/abs/2611.15124.
4. M. G. Cornet, T. Dravec and P. Torres, *Domination and total domination in Johnson graphs*, arXiv:2610.04675 (2026), https://arxiv.org/abs/2610.04675.
