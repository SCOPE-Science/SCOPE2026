# Exact tree-variation sensitivity of isotonic projection and unbounded cubic-branch amplification

## Finding

Let \(T=(V,E)\) be an undirected finite tree with at least two vertices. Orient each edge in an arbitrary direction and let \(K_T\subset\mathbb R^V\) be its (unweighted) isotonic cone: \(x_v\ge x_u\) for every directed edge \(u\to v\). Let \(\Pi_T\) be Euclidean nearest-point projection onto \(K_T\). On real vertex signals define
\[
 \operatorname{TV}_T(h)=\sum_{\{u,v\}\in E}|h_u-h_v|,
 \qquad
 L_T=\sup_{\operatorname{TV}_T(f-g)>0}
 \frac{\operatorname{TV}_T(\Pi_T f-\Pi_T g)}{\operatorname{TV}_T(f-g)}.
\]
The sharp constant \(L_T\) is independent of the chosen edge orientation and has the following **finite exact combinatorial formula**. For every connected vertex set \(S\) containing an edge \(e\), remove \(e\) from the induced subtree on \(S\); call the resulting sets \(A,B\), put \(a=|A|\), \(b=|B|\), and let \(p\) (respectively \(q\)) be the number of original edges of \(T\) with one endpoint in \(A\) (respectively \(B\)) and the other outside \(S\). Then
\[
\boxed{L_T=\max\left\{1,\max_{S\subseteq V\text{ connected}}\max_{e\in E(S)}
\frac{bp+aq}{a+b}\right\}.}\tag{1}
\]
The second maximum skips singleton sets. Every value contributing to (1) is realized as the exact **local** variation gain of \(\Pi_T\) at an explicit input, in a cut-step direction. A maximizer of (1) therefore gives arbitrarily close, and in the exhibited local affine region exactly equal, two-input ratios.

A polynomial-time tree-knapsack algorithm computes the rational number in (1) from the tree alone. Three sharp consequences identify the role of branching:

* For every path tree, \(L_T=1\), regardless of the orientation.
* For a star with \(m\ge1\) leaves,
  \[\boxed{L_T=\max\{1,(m-1)/2\}.}\tag{2}\]
  Thus the first expansive star has four leaves and sharp constant \(3/2\).
* Let \(C_k\), \(k\ge2\), have a spine of \(k\) vertices forming a path, with one additional pendant leaf attached to each spine vertex. Then \(C_k\) has maximum degree at most three and \(2k\) vertices, yet
  \[\boxed{L_{C_k}=k/2.}\tag{3}\]
  Hence these nonlinear projections have arbitrarily large variation sensitivity even at uniformly bounded vertex degree.

## Assumptions and scope

All signals and coordinates are real. The Euclidean fitting objective is the ordinary *unweighted* sum of squared vertex residuals. The graph variation \(\operatorname{TV}_T\) is a seminorm, vanishing precisely on constant signals; because \(\Pi_T(f+c\mathbf1)=\Pi_T(f)+c\mathbf1\), the quotient defining \(L_T\) is well-defined on signals modulo constants. No assumption that the orientation points away from a root is necessary: every orientation of a tree is acyclic. An edge crossing the two sides of \(S\) is counted as boundary only when its other endpoint is outside \(S\). Formula (1) includes an explicit \(1\) because the projection acts identically on strictly order-preserving inputs.

## Proof

**1. All local linear branches are connected-block averages.** Let \(y\in\mathbb R^V\) and \(x=\Pi_Ty\). Retain precisely the edges whose fitted endpoint values are equal, and let \(\mathcal P\) denote the connected components of that active-edge forest. Across different blocks all defining inequalities are strict. A sufficiently small common translation of an individual block, with other fitted values fixed, remains feasible in both directions. First-order optimality therefore gives, for every block \(B\in\mathcal P\),
\[
 x_v=|B|^{-1}\sum_{w\in B}y_w\quad(v\in B).
\]
Thus \(\Pi_T(y)=Q_{\mathcal P}y\), where \(Q_{\mathcal P}\) is the orthogonal block-averaging projection. There are finitely many connected partitions. The Euclidean metric projection is continuous and piecewise affine on the finitely many active-set regions. Along any line segment its variation-Lipschitz constant is consequently bounded by the largest induced \(\operatorname{TV}_T\)-norm among all \(Q_{\mathcal P}\). This implication can alternatively be proved by the continuous finite-selection lemma applied to the finite family of linear maps \(Q_{\mathcal P}\).

**2. Every connected partition actually occurs on an open linearity region.** Fix any partition \(\mathcal P\) of \(V\) into connected blocks. Contract its blocks. Because \(T\) is a tree, the oriented quotient is an oriented tree and hence has a strictly order-preserving block-constant vector \(x\); all uncontracted edge inequalities are strict. For an oriented edge \(u\to v\), define its row \(D_e=\mathbf e_v-\mathbf e_u\). Put \(F\) equal to the active edges internal to blocks and choose positive multipliers \(\lambda_e=1\) for \(e\in F\). Set
\[
 y=x-D_F^{\mathsf T}\lambda.
\]
The KKT system for minimizing \(\|z-y\|_2^2/2\) subject to \(Dz\ge0\) holds at \(z=x\): the active constraints vanish, the remaining constraints are strict, and all active multipliers are positive. The incidence rows \(D_F\) are independent, since \(F\) is a forest. Consequently, in a sufficiently small neighborhood of \(y\), the solution remains on exactly the same face and equals \(Q_{\mathcal P}z\), with positive multipliers depending continuously on \(z\). Every connected partition therefore contributes its genuine local operator norm, not merely an unattainable formal bound. This argument also shows why the orientation disappears from the final constant.

**3. Cut indicators compute the operator norm exactly.** Fix a root of \(T\) only for notation. For each edge \(e\), let \(h_e\) be the indicator of the component of \(T\setminus\{e\}\) not containing the root. Every signal has a unique expansion modulo constants,
\[
 h=h(r)\mathbf1+\sum_{e\in E}\delta_eh\,h_e,
 \qquad \operatorname{TV}_T(h)=\sum_e|\delta_eh|,
\]
where \(\delta_eh\) is the root-outward difference across \(e\). Since block averaging preserves constants, the triangle inequality, followed by testing each \(h_e\), gives
\[
 \|Q_{\mathcal P}\|_{\operatorname{TV}_T\to\operatorname{TV}_T}
 =\max_{e\in E}\operatorname{TV}_T(Q_{\mathcal P}h_e).
\]
If the endpoints of \(e\) belong to different blocks, every block lies wholly on one side of the cut, so \(Q_{\mathcal P}h_e=h_e\), with variation \(1\). Otherwise \(e\) lies in a unique connected block \(S\). Removing \(e\) from \(S\) leaves parts \(A,B\) of sizes \(a,b\). Taking \(h_e\) to be zero on the \(A\)-side and one on the \(B\)-side, the average on \(S\) is \(b/(a+b)\), while every other block remains identically zero or one. The only output jumps are along boundary edges of \(S\): each of the \(p\) edges on the \(A\)-side has jump \(b/(a+b)\), and each of the \(q\) edges on the \(B\)-side has jump \(a/(a+b)\). Hence the variation is exactly \((bp+aq)/(a+b)\). Combining steps 1 and 2 proves (1) with all sharpness quantifiers.

**4. Polynomial-time evaluation.** For each original edge \(e=uv\), remove \(e\). On the side containing \(u\), let \(B_{u|v}(a)\) be the largest number of edges going from a connected size-\(a\) set containing \(u\) to its complement *on that side*; define \(B_{v|u}(b)\) analogously. The two sides may be optimized independently, yielding the equivalent formula
\[
 L_T=\max\left\{1,\max_{uv\in E}\max_{a,b}
 \frac{bB_{u|v}(a)+aB_{v|u}(b)}{a+b}\right\}.\tag{4}
\]
Each side profile is obtained by a rooted-tree knapsack. Start at a vertex with connected set consisting only of that vertex; each child branch not selected contributes one boundary edge. When a child rooted subtree of size \(s\) and boundary value \(c\) is included, replace the one boundary edge to that child by its \(c\) outward edges, increasing set size by \(s\) and boundary count by \(c-1\). Keep the maximum for each total size. Naively recomputing profiles for every edge uses at most \(O(|V|^4)\) arithmetic operations and polynomial memory, giving an exact algorithm without numerical optimization.

**5. Paths and stars.** For a path, every connected set is an interval. Each side of an internal cut has at most one outward boundary edge, so \((bp+aq)/(a+b)\le1\); equality of the global constant follows from the identity region. On a star, any connected nonsingleton set is its center together with \(s\) leaves. Cutting an internal leaf edge gives \(a=1,b=s,p=0,q=m-s\) up to swapping sides, hence gain \((m-s)/(s+1)\). Maximizing over \(1\le s\le m\) and adjoining the baseline \(1\) proves (2).

**6. Exact cubic caterpillar law.** For \(C_k\), a cut edge incident to a pendant leaf yields \(a=1,p=0\), hence gain \(q/|S|\le1\). Indeed, every vertex has degree at most three and the included pendant endpoint has degree one, so any connected \(S\) containing that edge has at most \(|S|\) outward edges.

It remains to consider a spine edge. Any connected set \(S\) containing it consists of an interval of \(m\) spine vertices, plus some selected pendant leaves. Write \(a,b\ge1\) for the numbers of spine vertices on the two sides of the cut, and \(\delta_A,\delta_B\in\{0,1\}\) for the possible outward spine edges at the two ends of the interval. For the spine-only interval, the variation ratio is
\[
 F_0=\frac{2ab+b\delta_A+a\delta_B}{a+b}
 =\frac{m+\delta_A+\delta_B}{2}
 -\frac{(a-b)(a-b+\delta_A-\delta_B)}{2m}.
\]
The final product is nonnegative because \(a-b\) is an integer and \(\delta_A-\delta_B\in\{-1,0,1\}\). Also \(m+\delta_A+\delta_B\le k\); therefore \(F_0\le k/2\). If \(l\) pendant leaves from the first side and \(r\) from the second side are included in \(S\), its numerator becomes
\[
 (a+b)F_0+r\delta_A+l\delta_B-2lr
 \le (a+b)F_0+l+r,
\]
while its denominator becomes \(a+b+l+r\). Its ratio is therefore at most \(\max\{F_0,1\}\le k/2\). This proves the upper bound for all connected \(S\).

For even \(k\), take the entire spine as \(S\) and cut it at the central edge; then \(a=b=k/2\) and the ratio is \(k/2\). For odd \(k\), take the first \(k-1\) spine vertices and cut them into two equal groups; now \(a=b=(k-1)/2\) and exactly one outward spine edge contributes, again yielding \(k/2\). This proves (3).

## Verification

The accompanying standard-library Python program `verify_tree_isotonic_bv.py` computes the exact rational value by three independently constructed mechanisms: connected-set/cut enumeration, exhaustive active-edge partitions and their step-operator norms, and rooted-side boundary knapsack. It checks path, star, asymmetric branching and caterpillar examples. For many specific active sets and cut indicators it also constructs strict KKT inputs with positive active multipliers, solves the exact perturbed multiplier equations over rational numbers, and checks that the predicted local quotient is attained. Run it using `python verify_tree_isotonic_bv.py`. Its diagnostics include `ALL_CONNECTED_SUBTREE_VS_INDEPENDENT_EDGE_PARTITION_CHECKS_PASSED 20`, `EXACT_KKT_ACTIVE_FOREST_AND_LOCAL_RATIO_WITNESSES_PASSED 1504`, and `ALL_ISOTONIC_TREE_VARIATION_DIAGNOSTICS_PASSED`. The code is a finite check, not an exhaustive proof for arbitrary trees; the universal statement rests on the six proof steps above.

## Relationship to prior work

Németh and Németh, *Isotonicity of the projection onto the monotone cone* (first public preprint 23 January 2012), analyze the order-isotonicity of metric projections. Their later *Isotonic regression and isotonic projection* (2015) describes isotonic cones for arbitrary directed graphs and coordinatewise order monotonicity. Those conclusions do not give an operator norm for the edge-variation seminorm on trees. Chen, Li and Su (2023) analyze active-set methods for generalized directed-tree isotonic fitting, including total-variation *penalties* in the optimization objective. Their results concern algorithms and fitted objectives, not the two-input edge-variation operator norm of the unpenalized Euclidean isotonic projection. Yang and Barber's *Contraction and uniform convergence of isotonic regression* (2017) gives a necessary and sufficient neighbor-averaging criterion for contraction of the **linearly ordered** isotonic projection under a given seminorm; in particular that theorem subsumes ordinary one-dimensional total-variation contraction, which is not claimed here as independent novelty. It does not state a branching-tree perturbation envelope or the cubic-caterpillar amplification law. A separate 2026 result on sharp \(\ell_p\) isotonic regression stability for general partial orders concerns input/output vertex-coordinate \(\ell_p\) norms and, except at \(p=2\), a different fitting objective; it does not give the graph-edge \(\ell_1\) variation constant. The new aspect of (1) is the exact topology-sensitive norm of the Euclidean projection *when measured in graph variation*, including sharp local realization and the unbounded-degree-three phenomenon. This comparison does not claim that database nonmatches establish global bibliographic uniqueness.

## Limitations

The underlying graph must be an unweighted finite tree, the fitting objective is Euclidean least squares with uniform vertex weights, and the metric is the unweighted edge-total-variation seminorm. The theorem does not cover graphs with cycles, weighted regression, weighted edges, non-Euclidean \(\ell_p\) fitting or infinite posets. Formula (1) is exact even if some maximizing quotient is realized only locally, but the proof here constructs strictly local pairs rather than a separate global classification of every equality pair. Similar formulas might be implicit in older active-set or polyhedral projection literature; no exhaustive historical priority claim is made.

## References

1. A. B. Németh and S. Z. Németh, *Isotonicity of the projection onto the monotone cone*, arXiv:1201.4677v1, publicly posted 23 January 2012, https://arxiv.org/abs/1201.4677.
2. A. B. Németh and S. Z. Németh, *Isotonic regression and isotonic projection*, arXiv:1503.08458v1 (2015), https://arxiv.org/abs/1503.08458.
3. F. Yang and R. F. Barber, *Contraction and uniform convergence of isotonic regression*, arXiv:1706.01852 (2017), https://arxiv.org/abs/1706.01852.
4. *Sharp \(\ell_p\) isotonic regression stability on every finite partial order*, publicly indexed mathematical research finding (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-ell-p-isotonic-regression-stability-on-every-finite-partia--7bfc7f16ca62 (mathematical claim inspected; different norm/objective).

5. X. Chen, X. Li and Y. Su, *An active-set based recursive approach for solving convex isotonic regression with generalized order restrictions*, arXiv:2304.00244v1 (1 April 2023), https://arxiv.org/abs/2304.00244.
6. V. Kolmogorov, T. Pock and M. Rolinek, *Total Variation on a Tree*, SIAM Journal on Imaging Sciences 9 (2016), 605–636, doi:10.1137/15M1010257 (public abstract only; treats a different tree-TV-penalized minimization objective).
