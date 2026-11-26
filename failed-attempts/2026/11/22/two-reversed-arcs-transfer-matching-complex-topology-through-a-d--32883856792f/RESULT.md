# Two reversed arcs transfer matching-complex topology through a directed four-cycle

## Finding
Let \(B=(U\sqcup W,E)\) be any finite simple bipartite graph and let \(e_1=u_1w_1\) and \(e_2=u_2w_2\) be vertex-disjoint edges. Form a digraph \(D(B;e_1,e_2)\) by directing every edge from \(U\) to \(W\), except for \(e_1\) and \(e_2\), which are directed \(w_1\to u_1\) and \(w_2\to u_2\). Write \(X(D)\) for the *multipath complex*: its vertices are directed arcs and its faces are collections of vertex-disjoint directed paths (including isolated vertices). Let \(H=B-\{u_1,u_2,w_1,w_2\}\) be the induced subgraph on the remaining vertices, and \(\mathcal M(H)\) its ordinary matching complex. Then

\[
|X(D(B;e_1,e_2))|\simeq
\begin{cases}
|\mathcal M(H)*S^0*S^0*S^0|,&u_1w_2,u_2w_1\in E,\\
\{*\},&\text{otherwise}.
\end{cases}
\]

The displayed \(S^0\) factors are the two-vertex discrete simplicial complex, and the join is simplicial. In the special case that \(H\) has no edges, \(\mathcal M(H)=\{\varnothing\}\) in the **augmented** simplicial convention, so the threefold join is \(S^2\). Thus even the four-cycle instance is a two-sphere. In every cross-complete case, the result provides natural shifted reduced integral homology groups:

\[
\widetilde H_k(X(D);\mathbb Z)\cong
\widetilde H_{k-3}(\mathcal M(H);\mathbb Z),
\]

with the augmented degree \(-1\) convention for the empty matching complex. All these statements are full homotopy equivalences, not deductions from field Betti numbers.

In particular, for \(B=K_{7,7}\), with any two disjoint edges reversed, \(H=K_{5,5}\); Jonsson's established \(\widetilde H_2(\mathcal M(K_{5,5});\mathbb Z)\cong\mathbb Z/3\mathbb Z\) implies
\[
\widetilde H_5(X(D);\mathbb Z)\cong\mathbb Z/3\mathbb Z.
\]
This supplies integral three-torsion in a very sparse two-arc modification of an acyclic orientation.

## Assumptions and scope
All graphs are finite and simple. There are no loops, parallel edges, or doubled antiparallel arcs. The two reversed edges have four distinct endpoints. For a subset of arcs to be a multipath it is necessary and sufficient that all selected indegrees and outdegrees be at most one and there be no selected directed cycles. An edge of \(H\) corresponds to an independent forward arc of \(D\). No regularity, completeness or connectedness assumption is made on \(B\) or \(H\). For the empty graph the matching complex retains its empty face; this augmented convention is essential to the four-vertex boundary case.

## Proof
Set \(r_1=(w_1\to u_1)\), \(r_2=(w_2\to u_2)\), and let \(F=B-\{e_1,e_2\}\). Write \(L=\mathcal M(F)\) for the complex of forward arcs. Because all forward arcs go from \(U\) to \(W\), the indegree/outdegree conditions for a forward-only arc subset say exactly that the chosen undirected edges form a matching. Such subsets cannot contain directed cycles.

Every choice of one reversed arc together with a forward matching is a multipath. Indeed, a directed cycle containing \(r_i\) would require a forward directed path from \(u_i\) to \(w_i\); such a path can only be an edge \(e_i\), which is no longer forward. The remaining degree conditions are automatic: a reversed arc contributes indegree only at a vertex of \(U\) and outdegree only at a vertex of \(W\), unlike all forward arcs.

For a face containing **both** reversed arcs, the only possible directed cycle is
\[
 w_1\to u_1\to w_2\to u_2\to w_1,
\]
which occurs if and only if the forward matching contains both cross edges \(x=u_1w_2\) and \(y=u_2w_1\). Let \(L'\subseteq L\) comprise precisely those forward matchings that do not contain both \(x,y\). When a cross edge is absent, simply put \(L'=L\). This proves the *exact simplicial identity*
\[
X(D)=\bigl(\{r_1\}*L\bigr)\cup\bigl(\{r_2\}*L\bigr)
\cup\bigl(\langle r_1,r_2\rangle*L'\bigr),
\]
where \(\langle r_1,r_2\rangle\) is the full edge, and joins include their lower-dimensional faces. If a cross edge is missing, \(L'=L\) and this union is the simplicial cone \(\langle r_1,r_2\rangle*L\), proving contractibility.

Suppose both cross edges exist. The first two pieces together form \(S^0*L\); the third is a contractible simplicial join with an edge, and its intersection with the first two is \(S^0*L'\). All inclusions are cofibrations of finite simplicial complexes. Collapsing the third piece to a point therefore identifies the homotopy type of the union with the cofiber
\[
 (S^0*L)/(S^0*L')\simeq\Sigma(L/L').
\]
Here and below quotient/suspension statements use pointed realizations and respect the augmented empty-face convention.

Since \(x\) and \(y\) are disjoint edges, the forward matchings containing both are exactly \(\{x,y\}\) together with arbitrary matchings of the **induced** graph \(H\): every endpoint of \(x\) or \(y\) belongs to \(\{u_1,u_2,w_1,w_2\}\). Accordingly,
\[
L=L'\cup(\langle x,y\rangle*\mathcal M(H)),\qquad
L'\cap(\langle x,y\rangle*\mathcal M(H))=S^0_{x,y}*\mathcal M(H).
\]
The quotient \(L/L'\) is the cofiber of the inclusion of the boundary of a simplicial edge into the edge, joined with \(\mathcal M(H)\). It is thus the double simplicial suspension of \(\mathcal M(H)\). The preceding suspension gives exactly \(\mathcal M(H)*S^0*S^0*S^0\). The argument also covers \(H\) without edges, where it reduces to the boundary of a tetrahedron and its suspensions. Integral homology suspension gives the displayed degree shift, including all torsion; Jonsson's three-torsion theorem supplies the specific \(K_{7,7}\) corollary. \(\square\)

## Verification
Run `python3 multipath_two_reversal_check.py` using Python 3 with its standard library. The verifier independently enumerates the arc-subset multipath condition by indegree/outdegree and explicit directed-cycle tests, compares every face against the exact three-piece union in the proof, and calculates mod-two reduced boundary ranks on both sides, using augmented degree \(-1\) when needed. All \(1301\) tested instances passed: every bipartite graph containing the two specified disjoint edges in six small board sizes (\(2\times2, 2\times3, 2\times4, 3\times2, 3\times3, 3\times4\)), 45 pseudorandom larger graphs and four complete-bipartite checks. These finite checks corroborate the face identity; **the unrestricted integral homotopy proof is the two-cone/cofiber argument above**, not finite extrapolation. The standalone program does not compute integral homology of the seven-by-seven instance; the three-torsion input is the published theorem of Jonsson.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith (2022, especially Proposition 2.8 and their tournament and bipartite examples) establish the multipath–matching relationship for alternating orientations and analyze other orientation patterns, but do not give the above arbitrary-bipartite two-reversal suspension or its sharp four-cycle obstruction. Caputi, Collari and Di Trani (2021) develop multipath complexes and general path-poset methods, also without this two-fault classification. Caputi, Celoria and Collari (2022) discuss oriented matchings in a different construction and do not identify this cycle-forbidden multipath space. The single source–sink feedback-arc result in the published mathematical record describes top-dimensional Hamiltonian-path sphere retracts after **one added return arc**; it does not imply the full matching-complex homotopy shift after **two reversed arcs**. Jonsson's integral chessboard-complex torsion theorem is **used as an input** for the torsion example, not claimed as new.

## Limitations
The theorem concerns exactly two **disjoint** reversed edges of one original bipartite graph. It does not classify adjacent reversals, three or more reversals, arbitrary digraphs, or the equivariant action on the resulting homology. The Kneser/chessboard torsion example relies on Jonsson's independent, previously known integral homology calculation. The finite verification uses \(\mathbb F_2\); it cannot independently establish integral torsion. Novelty has been compared to the listed accessible primary sources and targeted scientific-record searches, but an unindexed equivalent could remain.

## References
1. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first public 2022-08-09; https://arxiv.org/abs/2208.04656.
2. L. Caputi, C. Collari and S. Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206, first public 2021-10-21; https://arxiv.org/abs/2110.11206.
3. L. Caputi, F. Celoria and C. Collari, *Monotone cohomologies and oriented matchings*, arXiv:2203.03476; https://arxiv.org/abs/2203.03476.
4. J. Jonsson, *On the 3-torsion Part of the Homology of the Chessboard Complex*, arXiv:1203.5644, public 2012-03-26, especially the proof of \(H_2(\mathcal M(K_{5,5});\mathbb Z)\cong\mathbb Z/3\mathbb Z\); https://arxiv.org/abs/1203.5644.
5. L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248; https://arxiv.org/abs/2401.01248.
