# Sharp graph-variation transfer by arithmetic edge-midpoint lifting

## Finding

Let \(G=(V,E)\) be a finite connected simple unweighted graph, with \(n=|V|\ge2\). Its line graph \(L(G)\) has one vertex for each edge of \(G\), with two distinct edges adjacent exactly when they share an endpoint. Define the **midpoint lift** \(M_G:\mathbb R^V\to\mathbb R^E\) by
\[
(M_G f)_{\{u,v\}}=\frac{f_u+f_v}{2}.
\]
For any graph \(H\), put \(\operatorname{TV}_H(h)=\sum_{\{u,v\}\in E(H)}|h_u-h_v|\). The sharp quotient-seminorm coefficient is
\[
\boxed{\ C(G):=\sup_{\operatorname{TV}_G(f)>0}
 \frac{\operatorname{TV}_{L(G)}(M_Gf)}{\operatorname{TV}_G(f)}
 =\max_{\varnothing\ne S\subsetneq V}
 \frac{\sum_{v\in V}s_v(S)[d_v-s_v(S)]}{2|\partial_G S|}\ },
\]
where \(d_v=|N_G(v)|\), \(s_v(S)=|N_G(v)\cap S|\), and \(\partial_G S\) consists of the edges with one endpoint in \(S\). Every maximizing cut produces an **actual** norming input \(f=\mathbf1_S\).

Moreover, for all connected simple graphs,
\[
\boxed{\ C(G)\le\frac{n-2}{2}.\ }
\]
Equality occurs if and only if some nontrivial cut \(S\) has the following property: **every vertex incident to a cut edge is adjacent to every other vertex on its own side of the cut**. In particular,
\[
C(K_n)=C(K_{1,n-1})=\frac{n-2}{2}.
\]
For every tree \(T\) on at least two vertices, the cut maximum simplifies to the exact edge-degree formula
\[
\boxed{\ C(T)=\frac12\max_{\{u,v\}\in E(T)}(d_u+d_v-2).\ }
\]
Consequently, \(C(T)\le1\) if and only if \(T\) is a path or the four-vertex claw \(K_{1,3}\). All connected graphs of order at most four are nonexpansive for this lift; order five is the first possible strict amplification, realized by both \(K_5\) and \(K_{1,4}\), with sharp factor \(3/2\). For cycles, \(C(C_3)=1/2\) and \(C(C_n)=1\) for every \(n\ge4\).

## Assumptions and scope

Only real-valued vertex signals and finite, simple, connected, unweighted, undirected graphs are considered. Each unordered pair of incident original edges is counted exactly once in \(\operatorname{TV}_{L(G)}\); this normalization matters, particularly for triangles and stars. There is no anchoring term. Both seminorms annihilate constant signals, and \(M_G\) maps constants to constants, so the quotient is well defined. At \(n=2\), the line graph has one vertex and no edges and \(C(G)=0\). All stated suprema are maxima on nonconstant binary inputs.

## Proof

**1. Wedge identity.** Each adjacent pair of distinct edges in \(G\) has a unique common vertex \(u\) (because the graph is simple), so corresponds to a unique unordered pair \(\{v,w\}\subset N_G(u)\). Their lifted values differ by exactly \((f_v-f_w)/2\). Thus
\[
\operatorname{TV}_{L(G)}(M_Gf)
 =\frac12\sum_{u\in V}\sum_{\{v,w\}\subset N_G(u)}|f_v-f_w|.
\]
This identity includes every line-graph edge once, including when original triangles are present.

**2. Exact cut formula.** If \(f=\mathbf1_S\), the number of unordered pairs of neighbors of \(u\) on opposite sides is \(s_u(S)[d_u-s_u(S)]\). Hence the displayed cut quotient is exact on indicators. For an arbitrary real \(f\), write \(f=c\mathbf1+\int\mathbf1_{\{f>t\}}\,dt\), integrating between its smallest and largest coordinates. The triangle inequality, linearity of \(M_G\), preservation of constants, and the graph coarea identity give
\[
\operatorname{TV}_{L(G)}(M_Gf)
\le\int \operatorname{TV}_{L(G)}(M_G\mathbf1_{\{f>t\}})\,dt
\le C_{\mathrm{cut}}\int|\partial_G\{f>t\}|\,dt
=C_{\mathrm{cut}}\operatorname{TV}_G(f).
\]
An indicator of a maximizing cut gives equality; thus \(C(G)=C_{\mathrm{cut}}\).

**3. Universal envelope and equality.** Fix a nontrivial cut \(S\), let \(c_u\) be the number of neighbors of \(u\) across the cut, and \(h_u=d_u-c_u\) its number of neighbors on the same side. Then \(s_u(d_u-s_u)=c_uh_u\), regardless of the side containing \(u\), and
\[
\sum_{u\in V}c_uh_u
=\sum_{\{u,v\}\in\partial_G S}(h_u+h_v).
\]
For each crossing edge, its endpoints lie in opposite parts, and \(h_u\le |S|-1\), \(h_v\le|V\setminus S|-1\) after ordering endpoints appropriately. Therefore \(h_u+h_v\le n-2\), proving \(C(G)\le(n-2)/2\). Equality in a cut quotient holds exactly when **each** crossing edge has \(h_u=|S|-1\) and \(h_v=|V\setminus S|-1\). This is exactly the stated universal-neighbor property of every cut-boundary vertex. The maximum is over finitely many cuts, so this is also necessary and sufficient for equality in the global bound. Every cut in \(K_n\) has this property; a one-leaf cut of \(K_{1,n-1}\) also has it.

**4. Trees.** From the wedge identity and \(|f_v-f_w|\le|f_v-f_u|+|f_u-f_w|\), every original edge \(\{u,v\}\) receives the factor \([d_u-1+d_v-1]/2\), yielding
\[
\operatorname{TV}_{L(T)}(M_Tf)
\le\frac12\max_{\{u,v\}\in E(T)}(d_u+d_v-2)\operatorname{TV}_T(f).
\]
Delete a maximizing edge \(e=\{u,v\}\) and let \(S\) be either resulting component. The sole original cut edge is \(e\); the only two-step wedges separated by this cut are those with center \(u\) or \(v\), numbering \(d_u-1+d_v-1\). Therefore \(f=\mathbf1_S\) attains the upper bound.

If the coefficient is at most one, every edge satisfies \(d_u+d_v\le4\). A vertex of degree at least four violates this immediately; a vertex of degree three must be adjacent only to leaves, making the connected tree \(K_{1,3}\). Otherwise every degree is at most two and the connected tree is a path. Conversely paths and \(K_{1,3}\) satisfy the degree-sum condition. The first-amplification and cycle statements follow from the universal envelope and direct cuts: on a cycle of length at least four, choose two neighboring vertices for \(S\) when \(n=4\), or an interval with at least two vertices on both sides when \(n\ge5\); each crossing-edge endpoint has one same-side neighbor, attaining one. A triangle is a complete graph of order three.

## Verification

The self-contained Python 3 standard-library program `verify.py` independently computes the original line-graph edge-midpoint variation for every indicator cut, its wedge-count expression, the finite cut maximum, and the equality criterion. All **771** connected labeled simple graphs on \(2\le n\le5\), comprising **11,199** representative nontrivial cuts, were checked exactly. The program also checked the tree degree formula for **145** labeled trees and the path, star, cycle, and complete-graph special cases through \(n=12\). The checker uses exact rational arithmetic; no random floating-point tolerance is involved. The unrestricted assertions are proved above; these finite computations are diagnostics and not substitutes for the proof.

Run: `python3 verify.py`.

## Relationship to prior work

Chen, Sandryhaila, Moura, and Kovačević [1] study graph-signal recovery and graph variation, emphasizing graph shifts and quadratic variation for optimization rather than the sharp transfer from vertex absolute-edge variation to line-graph absolute-edge variation. Yanagiya and colleagues [2] study line-graph representations and edge smoothness for graph edge sampling; their edge signals and quadratic smoothness do not provide the coefficient for arithmetic midpoint lifting of vertex signals. Published results on positive vertex-to-edge averaging in the \(\ell_\infty\) setting and on tree descendant averaging use different norms and operations; their norm statements do not imply the cut formula or the tree degree-sum identity here. An unindexed earlier equivalent cannot be excluded.

## Limitations

No claim is made for directed or multigraph inputs, arbitrary original-edge weights, weighted line-graph variation, nonlinear midpoint rules, or optimal interpolation among all possible lifts. For general graphs the exact answer is a cut maximum, not a claimed polynomial-time evaluation algorithm. The structural classification of nonexpansive graphs beyond the tree family is not completed. The reviewed proof and exact checks have not undergone independent mathematical validation.

## References

1. S. Chen, A. Sandryhaila, J. M. F. Moura and J. Kovačević, *Signal Recovery on Graphs: Variation Minimization*, arXiv:1411.7414, first public preprint 2014-11-26, https://arxiv.org/abs/1411.7414.
2. K. Yanagiya, K. Yamada, Y. Katsuhara, T. Takatani and Y. Tanaka, *Edge Sampling of Graphs: Graph Signal Processing Approach With Edge Smoothness*, arXiv:2407.10149, first preprint 2024-07-14, https://arxiv.org/abs/2407.10149.
