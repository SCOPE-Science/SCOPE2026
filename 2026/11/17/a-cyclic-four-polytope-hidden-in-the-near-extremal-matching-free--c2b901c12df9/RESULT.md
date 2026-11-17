# A cyclic four-polytope hidden in the near-extremal matching-free complex of a whiskered cycle

## Finding
For every integer \(n\ge5\), the matching-free complex of the fully whiskered \(n\)-cycle at matching threshold \(n-2\) is homotopy equivalent over the integers to a single sphere:
\[
\mathsf{MF}^{n-2}(W(C_n))\simeq S^{2n-6}.
\]
More precisely, its combinatorial Alexander dual simplicially collapses to the boundary of the cyclic four-polytope \(C(n,4)\). This explicit four-dimensional-polytope link is the structural assertion behind the homotopy classification.

## Assumptions and scope
Let \(n\ge5\). The graph \(G=W(C_n)\) has vertices \(x_0,\ldots,x_{n-1},y_0,\ldots,y_{n-1}\), with edges \(x_ix_{i+1}\) (indices modulo \(n\)) and \(x_iy_i\). All graphs are simple. A matching is a set of pairwise vertex-disjoint edges. For positive integer \(q\), define
\[
K_q=\mathsf{MF}^{q}(G)=\{F\subseteq V(G):G[F]\text{ has no matching of size }q\}.
\]
The claim is for \(q=n-2\). Its Alexander dual uses the *full* set \(V(G)\) of \(2n\) vertices:
\[
D=K_{n-2}^{\vee}=\{S\subseteq V(G):V(G)\setminus S\notin K_{n-2}\}.
\]
Thus \(S\in D\) exactly when \(G[V(G)\setminus S]\) contains an \((n-2)\)-matching. We write \(\partial C(n,4)\) for the boundary complex of a four-dimensional cyclic polytope on \(n\) ordered vertices.

## Proof
**1. An elementary collapse from the Alexander dual to the leaves.** A matching of \(n-2\) edges uses \(2n-4\) distinct vertices. Therefore each face of \(D\) contains at most four vertices. Fix \(i\). If \(S\in D\), \(x_i\in S\), and \(y_i\notin S\), the leaf \(y_i\) is isolated in \(G[V(G)\setminus S]\), because its only neighbor was removed. Any witnessing matching avoids \(y_i\), so it also witnesses \(S\cup\{y_i\}\in D\). Consequently the link of the vertex \(x_i\) in the current complex is a cone with apex \(y_i\). Its simplices can be paired with their unions with \(y_i\), in descending dimension, giving a sequence of elementary simplicial collapses deleting \(x_i\). This remains true after previously deleted center vertices. Repeating for all \(n\) centers shows that \(D\) simplicially collapses onto the induced subcomplex \(L\) on the pendant vertices.

**2. Exact description of the leaf subcomplex.** Write \(A\subseteq\{0,\ldots,n-1\}\) for the indices of deleted leaves. A witnessing matching in the graph after removing exactly \(\{y_i:i\in A\}\) may be modified as follows: whenever a cycle edge uses a center \(x_j\) with \(j\notin A\), replace that cycle edge by the pendant edge \(x_jy_j\). This preserves matching cardinality and disjointness because no other matching edge can touch \(y_j\), and it strictly decreases the number of cycle edges having an endpoint outside \(A\). Eventually, all surviving cycle edges are contained in the induced cycle graph \(C_n[A]\). There are at most \(n-|A|\) available pendant edges, so an \((n-2)\)-matching requires at least \(\max(0,|A|-2)\) disjoint cycle edges within \(A\). Conversely, if such cycle edges exist, take them together with sufficiently many of the \(n-|A|\) pendant edges: this produces an \((n-2)\)-matching. Thus for \(|A|\le4\),
\[
\{y_i:i\in A\}\in L\quad\Longleftrightarrow\quad
\nu(C_n[A])\ge\max(0,|A|-2),
\]
where \(\nu\) is matching number; no larger face occurs. In particular every pair is a face; a triple is a face precisely when it contains adjacent cycle indices; and a four-set is a facet precisely when it consists of two vertex-disjoint edges of the underlying \(n\)-cycle. Every face with fewer than four vertices is also contained in such a facet: for a triple containing an edge, the third vertex has a cycle neighbor outside that edge because \(n\ge5\); the case of a pair follows by adding disjoint edges in the cycle (or by the standard two-neighborliness of the complex in the next step).

**3. A cyclic-polytope boundary.** Gale's evenness criterion for the moment-curve polytope \(C(n,4)\) says exactly that its facets are the four vertices forming two disjoint edges of the cyclic order on \(n\) vertices. Hence \(L\cong\partial C(n,4)\). It follows that \(|D|\simeq|L|\cong S^3\), and the collapses are integral homotopy equivalences, not merely field-dependent homology equivalences.

**4. Recovering the original matching-free complex.** Combinatorial Alexander duality on the full \(2n\) vertices gives
\[
\widetilde H_j(K_{n-2};\mathbb Z)
\cong\widetilde H^{2n-j-3}(D;\mathbb Z).
\]
Since \(D\simeq S^3\), the only nonzero reduced integral homology is \(\widetilde H_{2n-6}(K_{n-2};\mathbb Z)\cong\mathbb Z\). Every minimal nonface of \(K_{n-2}\) must support \(n-2\) disjoint graph edges and hence contains at least \(2n-4\) vertices. Therefore \(K_{n-2}\) contains the entire \((2n-6)\)-skeleton of the simplex on \(2n\) vertices. Such a skeleton is \((2n-7)\)-connected. Set \(d=2n-6\ge4\). The Hurewicz theorem produces a map \(S^d\to|K_{n-2}|\) that induces an isomorphism on the unique nonzero reduced homology group. Both spaces are simply connected CW complexes, so the homological Whitehead theorem makes this map a homotopy equivalence. This proves the claimed sphere homotopy type for every \(n\ge5\).

## Verification
Execute the included standalone program with \(\texttt{python3 verification/check_cyclic_whisker.py}\). It separately enumerates matchings and all candidate dual faces for \(5\le n\le11\), checks the dominated-center elementary collapses including free-face conditions, and compares every leaf face with the downward closure of the two-disjoint-cycle-edge facets. Its recorded output ends with \(\texttt{CYCLIC_WHISKER_DUAL_CHECKS_PASS}\). These are checks for the listed finite \(n\), not an inference that finite tests establish the unrestricted result. Steps 1–4 above are the all-\(n\) proof.

## Relationship to prior work
Ghosh and Selvaraja (first posted March 3, 2026) studied these matching-free complexes on whisker graphs, proving structural purity, shellability and Cohen–Macaulayness criteria and analyzing the neighboring threshold \(n-1\); their statements do not give this \(n-2\) sphere homotopy type or a cyclic-polytope dual collapse. Das, Ghosh and Selvaraja (first posted April 18, 2026) establish the graded-ideal regularity formula for squarefree powers of whiskered cycles, which does not classify the integral homotopy type. Das, Roy and Saha (2024) provide algebraic regularity/depth bounds, likewise without the Alexander-dual cyclic-polytope structure. Gale's evenness criterion supplies the classical identification of the residual complex, not the new matching-complex collapse. These comparisons are about statements and implications rather than the presence or absence of matching terminology alone.

## Limitations
The proof assumes a cycle with one pendant leaf per center and \(n\ge5\); it makes no claim for other graphs, other matching thresholds, or equivariant sphere identifications. It determines a nonequivariant integral homotopy type. An implicit equivalent result in further literature has not been excluded absolutely. The finite verifier is supplementary rather than a replacement for the symbolic argument.

## References
1. R. Ghosh and S. Selvaraja, *Cohen-Macaulayness of squarefree powers of edge ideals of whisker graphs*, arXiv:2603.02824 (first public version March 3, 2026), https://arxiv.org/abs/2603.02824.
2. S. Das, A. Ghosh and S. Selvaraja, *Regularity of Squarefree Powers of Edge Ideals of Whiskered Cycles*, arXiv:2604.17100 (first public version April 18, 2026), https://arxiv.org/abs/2604.17100.
3. K. K. Das, A. Roy and K. Saha, *Square-free powers of Cohen-Macaulay forests, cycles, and whiskered cycles*, arXiv:2409.06021 (2024), https://arxiv.org/abs/2409.06021.
4. G. M. Ziegler, *Lectures on Polytopes*, Graduate Texts in Mathematics 152, Springer (1995), Gale evenness criterion for cyclic polytopes.
