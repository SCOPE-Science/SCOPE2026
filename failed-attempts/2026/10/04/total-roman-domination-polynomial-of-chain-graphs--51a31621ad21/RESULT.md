# Total Roman domination polynomial of chain graphs
## Finding
Let \(G\) be a finite connected chain graph with canonical nonempty twin classes
\[
A_1,\ldots,A_p,\qquad B_1,\ldots,B_p,
\]
chosen so that every \(a\in A_i\) has
\[
N(a)=B_1\cup\cdots\cup B_i,
\]
and equivalently every \(b\in B_j\) has
\[
N(b)=A_j\cup\cdots\cup A_p.
\]
Write \(\alpha_i=|A_i|\), \(\beta_j=|B_j|\), \(A=\bigcup_iA_i\), \(B=\bigcup_jB_j\), and \(N=|A|+|B|\). A total Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that every \(0\)-vertex has a neighbor labeled \(2\), and the subgraph induced by the positive vertices has no isolated vertex.

The structural criterion is:
\[
f\text{ is total Roman dominating}
\iff
f\text{ is Roman dominating, }f(A_p)>0,\text{ and }f(B_1)>0,
\]
where \(f(X)>0\) means that at least one vertex of \(X\) receives a positive label.

This criterion gives an exact weight enumerator. For \(\epsilon,\tau\in\{0,1\}\), define
\[
F_n^{\epsilon,\tau}(x)=(\epsilon+x+\tau x^2)^n,
\qquad
E_n^{\epsilon,\tau}(x)=F_n^{\epsilon,\tau}(x)-\epsilon,
\qquad
H_n^{\epsilon}(x)=F_n^{\epsilon,1}(x)-F_n^{\epsilon,0}(x).
\]
Thus \(F_n^{\epsilon,\tau}\) is the local weight polynomial when label \(0\) is allowed exactly if \(\epsilon=1\) and label \(2\) is allowed exactly if \(\tau=1\); \(E\) additionally requires a positive label, and \(H\) requires at least one label \(2\).

For \(1\le s\le p\), put
\[
U_s(x)=
H_{\alpha_s}^{0}(x)
\prod_{i<s}F_{\alpha_i}^{0,1}(x)
\prod_{i>s}F_{\alpha_i}^{0,0}(x)
\;E_{\beta_1}^{1,0}(x)
\prod_{2\le j\le s}F_{\beta_j}^{1,0}(x)
\prod_{j>s}F_{\beta_j}^{0,0}(x).
\]
For \(1\le r\le p\), put
\[
V_r(x)=
H_{\beta_r}^{0}(x)
\prod_{j<r}F_{\beta_j}^{0,0}(x)
\prod_{j>r}F_{\beta_j}^{0,1}(x)
\;E_{\alpha_p}^{1,0}(x)
\prod_{r\le i<p}F_{\alpha_i}^{1,0}(x)
\prod_{i<r}F_{\alpha_i}^{0,0}(x).
\]
For \(1\le r,s\le p\), define
\[
A_{r,s}(x)=
\begin{cases}
1,&s=p,\\
E_{\alpha_p}^{1,0}(x),&s<p,
\end{cases}
\qquad
B_{r,s}(x)=
\begin{cases}
1,&r=1,\\
E_{\beta_1}^{1,0}(x),&r>1,
\end{cases}
\]
and
\[
\begin{aligned}
W_{r,s}(x)={}&
H_{\alpha_s}^{\mathbf 1_{\{s\ge r\}}}(x)
H_{\beta_r}^{\mathbf 1_{\{r\le s\}}}(x)
A_{r,s}(x)B_{r,s}(x)\\
&\times
\prod_{\substack{i\ne s,\ i\ne p}}
F_{\alpha_i}^{\mathbf 1_{\{i\ge r\}},\mathbf 1_{\{i\le s\}}}(x)
\prod_{\substack{j\ne r,\ j\ne1}}
F_{\beta_j}^{\mathbf 1_{\{j\le s\}},\mathbf 1_{\{j\ge r\}}}(x).
\end{aligned}
\]
Then the total Roman domination polynomial, counting every total Roman dominating function by its weight, is
\[
T_G(x)=x^N+\sum_{s=1}^{p}U_s(x)+\sum_{r=1}^{p}V_r(x)+\sum_{r=1}^{p}\sum_{s=1}^{p}W_{r,s}(x).
\]
Consequently,
\[
\gamma_{tR}(G)=\min\{N,\ |A|+2,\ |B|+2,\ 4\}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A connected chain graph means a connected bipartite graph with nested neighborhoods on each side; the displayed twin-class form is canonical up to reversal of the two bipartition sides and equality classes. All \(\alpha_i\) and \(\beta_i\) are positive. The polynomial counts all total Roman dominating functions, not merely minimum ones. The coefficient of \(x^k\) is therefore the exact number of such functions of weight \(k\).

## Proof
First prove the boundary-support criterion. Suppose that a Roman dominating function \(f\) has a positive vertex in both \(A_p\) and \(B_1\). Every positive vertex of any \(A_i\) is adjacent to every vertex of \(B_1\), hence has a positive neighbor. Every positive vertex of any \(B_j\) is adjacent to every vertex of \(A_p\), hence also has a positive neighbor. Thus the positive induced subgraph has no isolated vertex, so \(f\) is total Roman dominating.

Conversely, suppose a Roman dominating function has no positive vertex in \(B_1\). Then every vertex of \(B_1\) is labeled \(0\). A vertex of \(A_1\) has neighborhood exactly \(B_1\); therefore it cannot itself be labeled \(0\), because it would have no neighboring label \(2\). Hence every vertex of \(A_1\) is positive. But every such vertex has only zero-labeled neighbors, so it is isolated in the positive induced subgraph. This contradicts total Roman domination. Therefore every total Roman dominating function has a positive vertex in \(B_1\). By the symmetric argument using that every vertex of \(B_p\) has neighborhood exactly \(A_p\), it must also have a positive vertex in \(A_p\). This proves the criterion.

Now partition total Roman dominating functions by the locations of label \(2\). If no label \(2\) occurs, the Roman condition forbids every label \(0\), so the unique function is the all-ones function, contributing \(x^N\).

Suppose labels \(2\) occur only on the \(A\)-side, and let \(s\) be the largest index for which \(A_s\) contains a label \(2\). Since no \(B\)-vertex has label \(2\), no \(A\)-vertex may have label \(0\). Classes \(A_i\) with \(i<s\) may use labels \(1,2\); \(A_s\) must use at least one \(2\); and classes \(A_i\) with \(i>s\) use only label \(1\). A vertex of \(B_j\) may be labeled \(0\) exactly when \(j\le s\), because then it is adjacent to the mandatory label \(2\) in \(A_s\). The boundary criterion additionally requires \(B_1\) to contain a positive label. These independent class choices give exactly \(U_s(x)\). Summing over \(s\) gives all functions with labels \(2\) only on \(A\). The symmetric argument gives \(V_r(x)\) when labels \(2\) occur only on \(B\), where \(r\) is the smallest index of a \(B\)-class containing a label \(2\).

Finally suppose both sides contain label \(2\). Let \(r\) be the smallest index such that \(B_r\) contains a label \(2\), and let \(s\) be the largest index such that \(A_s\) contains a label \(2\). An \(A_i\)-vertex may receive label \(0\) exactly when \(i\ge r\), because precisely then it sees a \(B\)-side label \(2\); it may receive label \(2\) exactly when \(i\le s\). Dually, a \(B_j\)-vertex may receive label \(0\) exactly when \(j\le s\), and it may receive label \(2\) exactly when \(j\ge r\). The factors \(H_{\alpha_s}\) and \(H_{\beta_r}\) enforce the extremal labels \(2\), while \(A_{r,s}\) and \(B_{r,s}\) enforce the positive boundary classes when those classes are not already extremal \(2\)-classes. Hence the contribution is exactly \(W_{r,s}(x)\). The four cases are disjoint and exhaustive, proving the polynomial formula.

For the minimum weight, the four cases have respective minima \(N\), \(|A|+2\), \(|B|+2\), and \(4\). The latter three bounds are attained by, respectively: labeling one vertex of \(A_p\) by \(2\), one vertex of \(B_1\) by \(1\), every other \(A\)-vertex by \(1\), and all other \(B\)-vertices by \(0\); the symmetric construction; and labeling one vertex of \(A_p\) and one vertex of \(B_1\) by \(2\) and all other vertices by \(0\). This proves the stated formula for \(\gamma_{tR}(G)\).

## Verification
A direct verifier constructs every canonical positive twin-class profile of total order at most \(9\). For each profile it enumerates every labeling in \(\{0,1,2\}^{V(G)}\), checks the total Roman definition directly from adjacency, checks the boundary-support criterion independently, expands the closed polynomial by integer convolution, and compares every coefficient and the minimum weight. Its replay result is:

`VERIFY_OK profiles=255 labelings=3023307 valid_functions=1117507 criterion_checks=3023307 coefficient_checks=3347 gamma_checks=255 max_order=9`

This finite computation is a stress test only; the proof above establishes the theorem for all finite connected chain graphs.

## Relationship to prior work
Liu and Chang introduced the total \((a,b)\)-Roman framework; their publisher record states that total \((a,b)\)-Roman domination is NP-complete already on bipartite graphs. Setting \(a=1\) and \(b=2\) gives the total Roman notion used here. Ahangar, Henning, Samodivkin, and Yero subsequently developed total Roman domination as a named parameter and gave general bounds and extremal results. Their inspected full accepted manuscript states the definition and MSC \(05C69\); searches of that full text found no chain-graph, Ferrers-graph, complete-bipartite, or polynomial treatment matching the theorem above. Poureidi later gave a linear-time algorithm for the minimum total Roman domination number on proper interval graphs, a different structured class and a scalar optimization result rather than an all-function weight enumerator.

The retained contribution is therefore the chain-graph boundary-support equivalence together with the exact all-weight factorization. General NP-completeness on bipartite graphs, general bounds, and minimum-only algorithms do not imply this factorization. Searches using the direct parameter name, the alias “Ferrers graph,” polynomial/enumerator language, and all-function language did not locate a published chain-graph formula. A residual risk remains that an obscure source uses different terminology or contains the same specialization without those searchable terms.

## Limitations
The result concerns connected chain graphs in canonical nested-neighborhood form. It does not claim a formula for arbitrary bipartite graphs, disconnected graphs, signed or double Roman variants, or minimal-under-pointwise-order functions. The exhaustive computation reaches order \(9\) and is not an infinite proof. Originality is supported by the documented searches and source inspections rather than by any claim of exhaustive global bibliographic coverage.

## References
1. C.-H. Liu and G. J. Chang, “Roman domination on strongly chordal graphs,” Journal of Combinatorial Optimization 26 (2013), 608–619. DOI: 10.1007/s10878-012-9482-y. Publisher first-public date: 2012-04-10.
2. H. Abdollahzadeh Ahangar, M. A. Henning, V. Samodivkin, and I. G. Yero, “Total Roman domination in graphs,” Applicable Analysis and Discrete Mathematics 10 (2016), 501–517. DOI: 10.2298/AADM160802017A.
3. A. Poureidi, “Total Roman domination for proper interval graphs,” Electronic Journal of Graph Theory and Applications 8 (2020), 401–413. DOI: 10.5614/ejgta.2020.8.2.16.
