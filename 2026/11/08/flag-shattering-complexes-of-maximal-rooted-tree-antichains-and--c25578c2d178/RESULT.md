# Flag shattering complexes of maximal rooted-tree antichains and an unbounded online gap

## Finding
Let \(T\) be a finite rooted tree with at least two vertices. Its *frontiers* are the inclusion-maximal antichains in the ancestor order: equivalently, the vertex sets meeting each root-to-leaf path exactly once. Regard frontiers as binary concepts on the vertices of \(T\), with membership queries.

Form a graph \(G_T\) on the vertices of \(T\). Join two distinct vertices when they are ancestor-comparable, or when one is a leaf \(\ell\) and the other lies in a different child-subtree of the parent of \(\ell\). Then the exact shattered-support complex of the frontier concept class is the independence complex of \(G_T\):
\[
\operatorname{Sh}(\mathcal F(T))=\operatorname{Ind}(G_T).
\]
Thus every minimal obstruction to shattering consists of two queried vertices, and the entire shattered-support polynomial is
\[
\Phi_T(z)=I_{G_T}(z)=\sum_{S\in\operatorname{Ind}(G_T)}z^{|S|}.
\]
If \(\tau(T)\) is the number of internal vertices having no internal child, then
\[
\operatorname{VCdim}(\mathcal F(T))=\tau(T).
\]
For the rooted binary comb \(B_m\), consisting of a chain of \(m\ge1\) internal vertices, with one side leaf at each nonterminal internal vertex and two leaves at the terminal internal vertex,
\[
\operatorname{VCdim}(\mathcal F(B_m))=1,\qquad
\operatorname{Ldim}(\mathcal F(B_m))=\lfloor\log_2(m+1)\rfloor.
\]
This gives an unbounded static-versus-online dimension gap within maximal-antichain membership concepts.

For the complete rooted \(b\)-ary tree of height \(h\), \(b\ge2\), \(h\ge1\), the entire shattering polynomial has the recursion
\[
\Phi_{b,1}(z)=1+(b+1)z,\qquad
\Phi_{b,h}(z)=z+\Phi_{b,h-1}(z)^b\quad(h\ge2).
\]
Its degree is \(b^{h-1}\), and its highest-degree coefficient is \((b+1)^{b^{h-1}}\).

## Assumptions and scope
All trees are finite, nonempty, and rooted. A leaf has no child. An *internal* vertex has at least one child. A frontier is an antichain meeting every maximal directed root-to-leaf path. For a nontrivial rooted tree the frontiers form a nonempty set system. A vertex set \(S\) is shattered when every map \(S\to\{0,1\}\) is the trace of at least one frontier. The Littlestone dimension is the maximum depth of a complete adaptive binary membership-query tree for the finite concept class. The single-vertex tree is exceptional: it has one frontier and shattering polynomial \(1\), with both dimensions zero.

## Proof
**1. Necessary pair obstructions.** Any frontier is an antichain, so comparable queried vertices cannot both receive label \(1\). If \(\ell\) is a leaf and \(u\) belongs to a different child-subtree of its parent \(p\), a frontier containing \(u\) cannot contain \(p\) or an ancestor of \(p\). To meet the root-to-\(\ell\) path it must then contain \(\ell\). Thus the labeling \(u=1\), \(\ell=0\) is impossible. Shattered supports contain no edge of \(G_T\).

**2. Sufficiency for every labeling.** Let \(S\) be an independent set of \(G_T\). Fix an arbitrary desired labeling, with positive vertices \(P\subseteq S\), and negative vertices \(N=S\setminus P\). Put
\[
Q=P\cup\{p(\ell):\ell\in N\text{ is a leaf}\}.
\]
Every leaf has a parent because \(T\) has at least two vertices. The graph-independence assumption implies that \(Q\) is an antichain: elements of \(P\) are mutually incomparable; for a negative leaf \(\ell\), no other selected vertex can be comparable with its parent (a selected vertex inside a different child-subtree would violate the extra edge condition); and the parents of two distinct negative leaves cannot be equal or ancestor-comparable without violating that condition. It also ensures \(Q\cap N=\varnothing\).

For every leaf whose root-to-leaf path is not already met by \(Q\), add that leaf to \(Q\). These added leaves are not in \(S\): a positive leaf is already in \(Q\), and a negative leaf has its parent in \(Q\). The resulting set is a frontier, contains \(P\), and avoids \(N\). This realizes the chosen labeling. As the labeling was arbitrary, \(S\) is shattered. This proves the independence-complex identity and the polynomial statement for all finite rooted trees of order at least two.

**3. The VC dimension.** Every antichain of internal vertices is independent in \(G_T\). Conversely, take an independent set \(S\). Replace each leaf \(\ell\in S\) by its parent \(p(\ell)\). No replacement collides with another vertex or destroys incomparability: such a collision or comparison would already have forbidden the corresponding pair in \(S\). Hence \(|S|\) is no larger than the width of the rooted subtree induced by the internal vertices, and this width is attained by an antichain consisting entirely of internal vertices. The internal vertices themselves form a rooted tree, whose width equals its number of leaves, namely \(\tau(T)\). The claim follows. (The width equality follows by assigning to each member of any antichain a distinct descendant leaf and by taking all leaves.)

**4. The comb separation.** Name the internal spine vertices \(v_0,\dots,v_{m-1}\). Let \(\ell_i\) be the side leaf at \(v_i\) for \(0\le i<m-1\), and let \(\ell_{m-1}\) and \(r\) be the two terminal leaves. There are exactly \(m+1\) frontiers:
\[
F_j=\{\ell_0,\dots,\ell_{j-1},v_j\}\ (0\le j<m),\qquad
F_m=\{\ell_0,\dots,\ell_{m-1},r\}.
\]
The internal vertices form a chain, with one terminal internal vertex, so the VC formula gives dimension one. Membership in \(\ell_i\) holds in \(F_j\) exactly when \(j>i\), giving every threshold cut in the ordered hypothesis list \(F_0,\dots,F_m\). Balanced threshold queries construct a complete binary decision tree of depth \(\lfloor\log_2(m+1)\rfloor\). Conversely, a depth-\(d\) complete mistake tree requires at least \(2^d\) different hypotheses, since a deterministic concept follows only one root-to-leaf answer sequence. There are only \(m+1\) concepts. The two inequalities agree.

**5. Complete regular trees.** When the height is one, the root and any single leaf can each be shattered, but no pair can: root/leaf pairs are comparable and distinct leaves are forced together as a frontier. Hence \(\Phi_{b,1}=1+(b+1)z\). At greater heights the root contributes a singleton shattered support, and any root-free support is independently an admissible support in each of the \(b\) child subtrees, with no cross-subtree conflict edges (the children are not leaves). This gives \(z+\Phi_{b,h-1}^b\). Degrees and leading coefficients follow by induction.

## Verification
The independently programmed finite checker `check_frontiers.py` derives maximal antichains recursively, computes every binary trace directly, and compares shattering with the forbidden-pair graph for every increasing-parent labeled rooted tree on two through eight vertices. Every unlabeled rooted-tree shape of those orders has such a labeling. It additionally checks random larger trees, complete regular trees via independent polynomial expansion, and exact recursive Littlestone dimensions for nine comb sizes. The recorded successful run is:

```
FRONTIER_SHATTERING_PASS rooted_trees 6213 complete_cases 6 comb_online 9
```

Finite tests do not prove the unrestricted theorems; the preceding arguments do.

## Relationship to prior work
Misanantenaina and Wagner, *A polynomial associated with rooted trees and specific posets* (first arXiv version, 2018-03-26, arXiv:1803.09623), already enumerate maximal antichains by leaf content, size and descendants. In particular their Theorem 2.8 and root-branch decomposition are foundational; their polynomial counts frontier concepts and other tree structures, whereas the present polynomial counts **subsets of membership queries whose every label pattern is realized**, a different statistic. The inspected article does not state a forbidden-pair characterization or the comb's Littlestone dimension.

Darnstädt, Ries and Simon, *Hierarchical design of fast Minimum Disagreement algorithms* (Theoretical Computer Science 716, 2018, DOI 10.1016/j.tcs.2017.11.022), use maximal antichains to encode dyadic partitions in an algorithmic setting. That representation is relevant but their available text concerns empirical-risk minimization and partition-size bounds, rather than this all-labelings membership-query classification. Complete comparison of this publisher version is limited by restricted full-text access.

## Limitations
The conflict graph and VC formula concern vertex-membership queries on maximal antichains of a rooted **tree**. They are not claimed for general posets or for samples of leaf labels associated with arbitrary hypotheses on the frontier blocks. Exact Littlestone dimension is only asserted for the explicit comb family, not all rooted trees. Historical priority under another description of complete prefix codes, tree cutsets, or hierarchical frontiers remains a risk; the accessible searches and full-text comparisons do not establish absolute novelty. Independent mathematical assessment has not occurred.

## References
1. V. R. Misanantenaina and S. Wagner, *A polynomial associated with rooted trees and specific posets*, arXiv:1803.09623 (initial public submission 2018-03-26), especially Section 2.2 and Theorem 2.8. https://arxiv.org/html/1803.09623v3
2. M. Darnstädt, C. Ries, and H. U. Simon, *Hierarchical design of fast Minimum Disagreement algorithms*, Theoretical Computer Science 716 (2018), 70–88, DOI: 10.1016/j.tcs.2017.11.022.
3. A. Paszke and M. Pilipczuk, *VC Density of Set Systems Definable in Tree-Like Graphs*, MFCS 2020, DOI: 10.4230/LIPIcs.MFCS.2020.78 (general learning-theoretic context; different definable family).
