# Vertex-amalgamation ranks and character degrees for square-cactus Lie algebras

## Finding
Let \(q\) be any prime power, let \(t\geq1\), and let \(G_t\) be the graph obtained by identifying one vertex of each of \(t\) four-cycles, leaving all other vertices distinct. The graph has \(3t+1\) vertices and \(4t\) edges. For each assignment \(\lambda\in\mathbb F_q^{E(G_t)}\), form the alternating weighted adjacency matrix \(B_{G_t}(\lambda)\), with the orientation signs chosen arbitrarily once and for all, and set
\[
R_{G_t,q}(z)=\sum_{\lambda\in\mathbb F_q^{E(G_t)}}z^{\operatorname{rank}(B_{G_t}(\lambda))/2}.
\]
Writing \(a=q(q^2-1)\) and \(b=q^2(q^2-1)\), the complete rank polynomial is
\[
\boxed{R_{G_t,q}(z)=(1-z)(1+az)^t+z(q^2+bz)^t.}
\]
Thus \(N_r(q,t)=[z^r]R_{G_t,q}(z)\) counts **individual labeled** alternating matrix specializations of rank \(2r\); it vanishes unless \(0\le r\le t+1\). With \(\binom{t}{j}=0\) outside \(0\le j\le t\), explicitly
\[
N_r(q,t)=\binom tr a^r-\binom t{r-1}a^{r-1}+\binom t{r-1}q^{2(t-r+1)}b^{r-1}
\]
for \(1\le r\le t+1\), and \(N_0(q,t)=1\). The coefficient formula is interpreted only for positive \(r\), so no negative powers arise at \(r=0\).

For **odd** \(q\), let \(\mathfrak g_t\) be the graph Lie algebra with vertex space \(\mathbb F_q^{3t+1}\), central edge space \(\mathbb F_q^{4t}\), and bracket indexed by edges. Let \(\mathbf G_t(\mathbb F_q)\) be its class-two Baker–Campbell–Hausdorff group. Its complex irreducible character degrees are powers of \(q\), with exact multiplicities
\[
\boxed{\#\{\chi:\chi(1)=q^r\}=q^{3t+1-2r}N_r(q,t).}
\]
In particular, the complete character count is
\[
\boxed{\#\operatorname{Irr}(\mathbf G_t(\mathbb F_q))=(q^2-1)q^{2t-1}(q^2+q-1)^t+q^{3t-1}(2q^2-1)^t.}
\]
The matrix rank formula holds for even fields too; only the ordinary character-degree corollary is restricted to odd \(q\).

More generally, the following rooted vertex-amalgamation identity holds for every finite family of rooted simple graphs over every finite field: if \(H_1,\dots,H_s\) share exactly their root vertex, write the alternating matrix of \(H_i\) in root-first form \(\begin{psmallmatrix}0&b_i\\-b_i^{\mathsf T}&A_i\end{psmallmatrix}\), and define
\[
P_i(z)=\sum_{\lambda_i:\, b_i\in\operatorname{Row}(A_i)}z^{\operatorname{rank}(A_i)/2},\qquad
Q_i(z)=\sum_{\lambda_i}z^{\operatorname{rank}(A_i)/2}.
\]
(The sum is over **all** edge assignments on \(H_i\); \(b_i\) and \(A_i\) depend on that assignment.) Then
\[
\boxed{R_{H_1\vee_*\cdots\vee_*H_s,q}(z)=(1-z)\prod_{i=1}^s P_i(z)+z\prod_{i=1}^sQ_i(z).}
\]
Here \(\vee_*\) denotes identification of only the specified root vertices, **not** graph join or coning.

## Assumptions and scope
All graphs are finite simple graphs, and an edge is assigned one independent scalar from \(\mathbb F_q\). An orientation fixes the signs of off-diagonal matrix entries. Reorienting an edge negates its weight coordinate; therefore the full rank distribution (though not necessarily each fixed-coordinate matrix) is orientation-independent. The square-cactus family has no additional identifications or edges. For the group statement the field has odd characteristic so division by two in the BCH law is defined. Character counts are of inequivalent ordinary complex representations, not modular representations and not isomorphism classes of graph Lie algebras.

## Proof
**1. Alternating rank under rooted gluing.** Let \(A\) be an alternating matrix over a field and let \(b\) be a row vector. Its root extension is \(C=\begin{psmallmatrix}0&b\\-b^{\mathsf T}&A\end{psmallmatrix}\). Choose a congruence that splits \(A\) into a nondegenerate alternating block and its radical. If \(b\) annihilates the radical, equivalently \(b\in\operatorname{Row}(A)\), changing the root by a vector in the nondegenerate block eliminates its coupling; \(\operatorname{rank}(C)=\operatorname{rank}(A)\). Otherwise the root pairs nontrivially with some radical vector, producing one additional hyperbolic plane; \(\operatorname{rank}(C)=\operatorname{rank}(A)+2\). This proof also works in characteristic two because the matrices represent alternating forms.

For a graph obtained by identifying the roots of \(H_1,\ldots,H_s\), deleting the common root produces \(A=\bigoplus_i A_i\) and \(b=(b_1,\ldots,b_s)\). Thus \(b\in\operatorname{Row}(A)\) if and only if all \(b_i\in\operatorname{Row}(A_i)\). Counting independent edge assignments proves the rooted product identity: assignments with every condition satisfied contribute \(\prod_iP_i(z)\), and all others contribute \(z(\prod_i Q_i(z)-\prod_iP_i(z))\).

**2. Single square.** Order the four vertices \(v,a,c,d\) around a cycle, with \(v\) the root; denote the root-edge weights by \(\alpha,\delta\) and the other two edge weights by \(\beta,\gamma\). After deletion of \(v\), the alternating matrix \(A\) is a weighted three-vertex path. If \((\beta,\gamma)=(0,0)\), it has rank zero, and \(b=(\alpha,0,\delta)\) lies in its row space exactly when \(\alpha=\delta=0\). If \((\beta,\gamma)\ne(0,0)\), it has rank two, with one-dimensional radical generated by \((\gamma,0,\beta)\). Then \(b\in\operatorname{Row}(A)\) precisely when \(\gamma\alpha+\beta\delta=0\), a nontrivial single linear constraint on the two root weights, admitting exactly \(q\) solutions. There are \(q^2-1\) choices of nonzero \((\beta,\gamma)\). Consequently \(P(z)=1+q(q^2-1)z\) and \(Q(z)=q^2+q^2(q^2-1)z\). Applying the rooted gluing identity with \(s=t\) identical squares gives the asserted rank polynomial and its coefficients.

**3. Character degrees.** For odd \(q\), choose a nontrivial additive character \(\psi:\mathbb F_q\to\mathbb C^\times\) and form the BCH group \(\mathbf G_t=V\oplus Z\), where \(\dim V=3t+1\) and \(\dim Z=4t\). For a fixed central character \(\psi\circ\lambda\), the quotient of the complex group algebra by the corresponding central-character relations is a twisted group algebra on \(V\). Its commutator pairing is \((x,y)\mapsto\psi(\lambda([x,y]))\), whose radical is the \(\mathbb F_q\)-radical of \(B_{G_t}(\lambda)\). Indeed, a nonzero \(\mathbb F_q\)-linear functional on any vector subspace takes every scalar value, so nontriviality of \(\psi\) detects every nonzero pairing after varying the second argument. If \(\operatorname{rank}B_\lambda=2r\), this twisted algebra has \(q^{\dim V-2r}\) simple blocks of size \(q^r\), by splitting off the central radical and the standard finite Heisenberg matrix algebra of a nondegenerate \(2r\)-space. Therefore there are exactly \(q^{3t+1-2r}\) irreducibles of degree \(q^r\) above each \(\lambda\). Summing over \(N_r(q,t)\) central characters proves the degree formula. Evaluating the rank polynomial at \(z=q^{-2}\) yields the stated total character count.

## Verification
The standalone script `checks/check_square_bouquets.py` exhaustively generates **each** weighted alternating adjacency matrix and computes rank by finite-field Gaussian elimination; it does not use the rooted splitting classification in its direct test. It compares rank histograms against the closed polynomial for \((q,t)=(2,1),(3,1),(5,1),(7,1),(2,2),(3,2),(2,3)\). For each tested odd \(q\), it checks the degree-square sum against the group order \(q^{7t+1}\). It also independently computes the number of conjugacy classes using the vertex-support formula from Rossmann's 2022 theorem and checks equality with the total character count. All checks passed; the exact output is embedded as `checks/direct_output.txt`. For example, at \(q=3,t=2\), the rank counts are \((1,128,1824,4608)\), and the degree counts are \((2187,31104,49248,13824)\) for degrees \(1,3,9,27\), respectively. The mathematical proof, not finite experiments, establishes the formulas for unrestricted \(q,t\).

## Relationship to prior work
The graphical Lie-algebra construction predates this work and is treated in Mainkar's 2010 preprint. Rossmann's 2022 open-access article, especially Section 1.6 and Question 1.10, expresses character-degree populations via alternating weighted-adjacency ranks and asks how they vary with the finite field. Its Theorem A and join formula instead enumerate **conjugacy class sizes**, a different invariant, and are used here only as a cross-check for total numbers of characters. Published formulas for single cycles, trees, and coning of arbitrary graphs are close precedents. They do not directly cover the one-vertex amalgamation of \(t\ge2\) four-cycles: no vertex of this graph is universal, and the graph is neither a tree nor a single cycle. The one-square case \(t=1\) is a previously covered cycle special case, not asserted as independently novel. The contribution assessed here is the rooted vertex-amalgamation rank rule applied to the full square-cactus family and the resulting complete all-parameter character-degree census.

## Limitations
This result does not establish a universal closed character-degree formula for all graphical groups. It determines ordinary characters only when the field has odd characteristic; even-characteristic weighted matrix ranks are nevertheless included. The rooted rank identity is a linear-algebraic transfer principle, not a classification of graph Lie algebras or a new result on single cycles. Independent validation and exhaustive historical-priority certification have not been performed. A more general, presently unidentified graph-rank decomposition theorem may overlap the rooted transfer principle.

## References
- M. G. Mainkar, *A short note on 2-step nilpotent Lie algebras associated with graphs*, arXiv:1010.4005 (first posted 2010-10-19), https://arxiv.org/abs/1010.4005.
- T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bulletin of the London Mathematical Society 54 (2022), 1923–1943, DOI: 10.1112/blms.12665, https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12665 (especially §§1.6, 5).
- T. Rossmann and C. Voll, *Groups, graphs, and hypergraphs: average sizes of kernels of generic matrices with support constraints*, arXiv:1908.09589 (2019), https://arxiv.org/abs/1908.09589.
- *Coning recurrence for character degrees of graphical groups*, publicly indexed research finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-coning-recurrence-for-character-degrees-of-graphical-groups--732adc755a75.
- *Cycle graphical groups have an explicit character-degree enumerator*, publicly indexed research finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-cycle-graphical-groups-have-an-explicit-character-degree-enumera--a874723da77e.
- *Tree graphical groups have matching-support character polynomials*, publicly indexed research finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-tree-graphical-groups-have-matching-support-character-polynomial--fb80c871ed65.
