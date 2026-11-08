# Electrical antichain widths determine inballs of acyclic unit-flow polytopes

## Finding

**Theorem (weighted electrical-antichain inball formula).** Let \(G=(V,E)\) be a finite connected directed acyclic graph with distinguished source \(s\) and sink \(t\), with every edge belonging to a directed \(s\)-to-\(t\) path, and with at least two distinct such paths. Give each edge a positive length-squared weight \(q_e>0\). Set \(Q=\operatorname{diag}(q_e)\), let \(B\) be the signed vertex–edge incidence matrix with column \(b_e=\mathbf e_{\mathrm{tail}(e)}-\mathbf e_{\mathrm{head}(e)}\), and let \(L=BQ^{-1}B^{\mathsf T}\). Let \(R_e=b_e^{\mathsf T}L^+b_e\) denote the effective resistance of the corresponding undirected weighted network, with edge resistance \(q_e\). Define

\[
\alpha_e=\sqrt{q_e^{-1}-q_e^{-2}R_e}\,,
\qquad W(G,Q)=\max_{A\in\mathscr A(G)}\sum_{e\in A}\alpha_e,
\]

where \(\mathscr A(G)\) consists of antichains in the *edge reachability poset*: \(e\prec f\) exactly when a directed path (possibly of length zero) runs from the head of \(e\) to the tail of \(f\). On the affine flow space \(Bx=\mathbf e_s-\mathbf e_t\), use the intrinsic norm \(\|u\|_Q=\sqrt{u^{\mathsf T}Qu}\). Then the largest radius of a \(Q\)-metric ball contained in the unit-flow polytope

\[
F_G=\{x\in\mathbb R^E:x\geq0,\ Bx=\mathbf e_s-\mathbf e_t\}
\]

is **exactly**

\[
\boxed{r(F_G,Q)=\frac1{W(G,Q)}.}
\]

Moreover the *entire* incenter locus is

\[
\boxed{\mathcal C(G,Q)=\{x\in F_G:x_e\geq\alpha_e/W(G,Q)\text{ for every }e\in E\}.}
\]

For every maximizing antichain \(A\) and every \(x\in\mathcal C(G,Q)\), all coordinate constraints on \(A\) with \(\alpha_e>0\) are tangent to the maximal ball: \(x_e=\alpha_e/W(G,Q)\). The formula allows zero \(\alpha_e\), for example when an edge belongs to every source–sink route.

**Consequences.** With the ordinary inherited Euclidean metric, \(q_e=1\), the width is a maximum-weight antichain with weights \(\sqrt{1-R_e}\). For \(k\geq2\) internally vertex-disjoint directed source–sink paths of lengths \(\ell_1,\ldots,\ell_k\), put \(H=\sum_{j=1}^k\ell_j^{-1}\); then

\[
\boxed{r=\left[\sum_{i=1}^k\sqrt{\ell_i^{-1}-\ell_i^{-2}/H}\right]^{-1}.}
\]

For exactly two paths this simplifies to \(r=\sqrt{\ell_1+\ell_2}/2\). These are metric statements, not invariant under arbitrary integral or affine equivalences of flow polytopes.

## Assumptions and scope

The graph can have several arcs with identical endpoints, provided they are treated as distinct edges. Its underlying undirected multigraph is connected, and all vertices and edges participate in source–sink routes. Each \(q_e\) is an arbitrary positive real number. The positive cycle-space dimension \(|E|-|V|+1\) follows from the existence of at least two routes. This theorem concerns unit netflow \(\mathbf e_s-\mathbf e_t\), not general prescribed netflow or constrained-capacity network flows. The Laplacian pseudoinverse \(L^+\) is the Moore–Penrose pseudoinverse and depends on the edge conductances \(q_e^{-1}\). The inradius is *intrinsic* to the affine hull with the declared diagonal metric; no ambient full-dimensional ball is intended.

## Proof

**1. Every point is a mixture of routes.** Conservation and acyclicity allow successively extracting a directed source–sink route carrying the minimum positive flow along its edges, then subtracting that route flow. This terminates after finitely many extractions, proving \(F_G=\operatorname{conv}\{\chi_P:P\text{ is an }s\text{-}t\text{ route}\}\). Consequently each edge-reachability chain lies on some route: concatenate the intervening directed paths with the edges of the chain, and extend from \(s\) and to \(t\) because all edges lie on routes. Conversely no route contains two incomparable edges. Thus the route-incidence vectors are the indicator vectors of maximal chains of the edge poset, up to harmless route extension.

**2. Norms of coordinate restrictions.** The tangent linear space to the affine flow space is \(K=\ker B\). Its orthogonal projection in the weighted inner product \(\langle u,v\rangle_Q=u^{\mathsf T}Qv\) is

\[
\Pi_K^{(Q)}=I-Q^{-1}B^{\mathsf T}(BQ^{-1}B^{\mathsf T})^+B.
\]

The squared operator norm of the coordinate functional \(u\mapsto u_e\) restricted to \(K\), with the \(Q\)-metric, is

\[
\|u\mapsto u_e\|_{K,Q}^{2}
=\bigl[Q^{-1}-Q^{-1}B^{\mathsf T}L^+BQ^{-1}\bigr]_{ee}
=q_e^{-1}-q_e^{-2}R_e=\alpha_e^2.
\]

This identity is a direct quadratic orthogonal-projection computation; no independence or asymptotic assumption is used. By duality, for a center \(x\in F_G\), the intrinsic ball of radius \(r\) is contained in every halfspace \(y_e\geq0\) precisely if \(x_e\geq r\alpha_e\). If \(\alpha_e=0\), the coordinate is constant on the affine hull and imposes no positive-radius restriction. Hence a ball of radius \(r\) is contained in \(F_G\) if and only if there is a unit flow \(x\) with \(x\geq r\alpha\).

**3. Antichain upper bound.** If \(A\) is an antichain, a source–sink route contains at most one member of \(A\). For every route-incidence vector \(\chi_P\), \(\sum_{e\in A}(\chi_P)_e\leq1\); by convexity the same holds for every \(x\in F_G\). Therefore \(1\geq\sum_{e\in A}x_e\geq r\sum_{e\in A}\alpha_e\) and \(r\leq1/W(G,Q)\).

**4. Sharpness by weighted Dilworth.** We use the following elementary weighted form of Dilworth's theorem: for any finite poset \(P\) and nonnegative real weights \(a_p\), there is a probability distribution on its maximal chains for which the probability of containing \(p\) is at least \(a_p/W\), where \(W\) is the largest total weight of an antichain. For nonnegative integer weights \(a_p\), replace each element \(p\) by \(a_p\) mutually incomparable copies, ordered relative to copies of other elements as in \(P\). The maximum cardinality of an antichain of the expanded poset equals \(W\): if any copies of \(p\) appear, adding all copies changes no comparability. Ordinary Dilworth partitions the expanded poset into \(W\) chains, each containing at most one copy of a given element. Project each chain to \(P\), extend it to a maximal chain, and choose one of the \(W\) maximal chains uniformly; then the probability of containing \(p\) is at least \(a_p/W\). Rational weights follow by integer scaling; arbitrary real weights follow from rational approximation, continuity of maximum-antichain weight (a maximum of finitely many continuous linear functions), and compactness of the finite simplex of chain distributions. Apply this lemma with \(P\) the edge poset and \(a_e=\alpha_e\). Each maximal chain extends to a source–sink route, so averaging the corresponding path-incidence vectors gives \(x\in F_G\) with \(x_e\geq\alpha_e/W\). Step 2 supplies a ball of radius \(1/W\), matching Step 3. Together with the ball-containment criterion this also gives the claimed *entire* incenter locus. For a maximizing antichain, \(1\geq\sum_{e\in A}x_e\geq\sum_{e\in A}\alpha_e/W=1\); equality forces each nonnegative term \(x_e-\alpha_e/W\) to vanish, proving the tangency claim.

**5. Parallel-path formula.** On \(k\) internally disjoint paths of lengths \(\ell_i\), a tangent flow takes a constant value along each path, so \(K\) is the subspace of vectors constant on each path whose path constants sum to zero. The diagonal coordinate-restriction norm on path \(i\) is \(\alpha_i=\sqrt{\ell_i^{-1}-\ell_i^{-2}/H}\), by projecting a unit coordinate into that \((k-1)\)-dimensional subspace; this is also the electrical expression in Step 2. Selecting one edge from each path forms a maximum-weight antichain, giving \(W=\sum_i\alpha_i\). For two paths the two constants are equal to \(1/\sqrt{\ell_1+\ell_2}\), giving \(W=2/\sqrt{\ell_1+\ell_2}\) and the asserted inradius.

## Verification

The standalone `artifacts/verify.py` uses exact rational grounded-Laplacian inverses and independently solves the path-mixture Chebyshev-center linear program. Its reproducible run returned `DAG_FLOW_INRADIUS_ANTICHAIN_CHECKS_PASSED graph_metric_profiles=96 checked_coordinate_norms=678 parallel_path_profiles=4`. The 96 cases include both unit and nonuniform diagonal metrics, and the checker also tests the tangency conditions for maximizing antichains and four explicit parallel-path configurations. Python dependencies are `sympy>=1.11`, `numpy>=1.24`, `scipy>=1.10`; run `python artifacts/verify.py`. Finite calculations are illustrative checks and not substitutes for the argument in Steps 1–5.

## Relationship to prior work

The source–sink route representation, the class of flow polytopes, and methods for their triangulations and normalized volumes are established in the first three references below. In particular, the source article arXiv:2101.10425 defines the exact unit-flow object and proves combinatorial triangulation and volume results, whereas the present statement gives an intrinsic Euclidean inball for all acyclic unit-flow graphs and arbitrary positive diagonal metrics. The network-effective-resistance identity and Dilworth's theorem are established ingredients, but their combination here yields the metric radius, all possible centers, and antichain tangency certificates. The general flow-polytope triangulation literature investigated does not supply the corresponding inradius statement. Graphical zonotopes, directed edge polytopes, and order polytopes have distinct affine/metric embeddings: their inradius statements do not automatically imply this theorem. An earlier equivalent weighted poset-packing or flow-Chebyshev formula cannot be entirely excluded.

## Limitations

The result requires acyclicity, all edges belonging to some source–sink route, unit netflow, and a positive diagonal edge metric. It does not address arbitrary prescribed netflow, non-diagonal metrics, general cyclic circulation polytopes, or minimum-volume ellipsoids. The maximum-antichain computation is finite and constructive, but no universal closed scalar formula is asserted for arbitrary graph families. Historical priority is provisional.

## References

1. M. von Bell, R. S. González D'León, F. A. Mayorga Cetina, M. Yip, *A unifying framework for the ν-Tamari lattice and principal order ideals in Young's lattice*, arXiv:2101.10425, first publicly submitted 2021-01-25. https://arxiv.org/abs/2101.10425
2. M. von Bell, *A subdivision algebra for a product of two simplices via flow polytopes*, arXiv:2205.09168, first submitted 2022-05-18. https://arxiv.org/abs/2205.09168
3. *Triangulations of Flow Polytopes, Ample Framings, and Gentle Algebras*, arXiv:2203.01896, first submitted 2022-03-03. https://arxiv.org/abs/2203.01896
4. R. P. Dilworth, *A decomposition theorem for partially ordered sets*, Annals of Mathematics 51 (1950), 161–166.
