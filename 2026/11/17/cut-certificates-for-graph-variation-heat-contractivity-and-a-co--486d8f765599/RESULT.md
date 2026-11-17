# Cut certificates for graph-variation heat contractivity and a complete unicyclic classification

## Finding

**Theorem A (finite-cut criterion).** Let \(G=(V,E)\) be any finite connected, simple, undirected, unweighted graph with at least two vertices. Let \(L=D-A\) be its combinatorial Laplacian and \(H_t=\exp(-tL)\). Define
\[
\operatorname{TV}_G(f)=\sum_{\{u,v\}\in E}|f(u)-f(v)|.
\]
For every nonempty proper set \(S\subset V\), let \(c_S(v)\) be the number of neighbours of \(v\) on the opposite side of \(S\), and set
\[
K_G(S)=-\sum_{v\in V}c_S(v)^2
+\sum_{\substack{\{u,v\}\in E\\\mathbf1_S(u)=\mathbf1_S(v)}}|c_S(u)-c_S(v)|.
\]
Writing \(\|H_t\|_{\mathrm{TV}}\) for the operator norm on functions modulo constants,
\[
\lim_{t\downarrow0}\frac{\|H_t\|_{\mathrm{TV}}-1}{t}
=\max_{\varnothing\ne S\subsetneq V}\frac{K_G(S)}{|\partial S|}.
\]
In particular,
\[
\operatorname{TV}_G(H_tf)\le\operatorname{TV}_G(f)
\quad\text{for every real }f\text{ and every }t\ge0
\quad\Longleftrightarrow\quad K_G(S)\le0
\text{ for every nontrivial }S.
\]
If a cut has \(K_G(S)>0\), its indicator is an explicit input with strictly increasing variation for all sufficiently small positive times.

**Theorem B (all finite unicyclic graphs).** Suppose additionally that \(G\) is connected and unicyclic, and let \(k\ge3\) be the length of its unique cycle. The heat flow is contractive in graph total variation at **all** times precisely for the following graphs:

1. A bare cycle of any length \(k\ge3\).
2. A triangle or square to whose cycle vertices arbitrary *distinct* pendant leaves have been attached, with no more than one pendant leaf per cycle vertex.
3. A pentagon with at most two pendant leaves, attached to distinct cycle vertices.

Every other connected unicyclic graph has a cut whose variation increases immediately under heat flow. In particular, adding a single leaf to a cycle creates amplification exactly when \(k\ge6\), whereas the pure cycle remains contractive for every length.

**Separation from Lipschitz heat contractivity.** On a pentagon with leaves attached at adjacent cycle vertices \(0\) and \(1\), graph total variation contracts for all times, but the edge Lipschitz seminorm expands for some inputs at arbitrarily small times. Indeed, label the cycle \(0,1,2,3,4\) and the new leaves \(5,6\) at \(0,1\). The function with values \((1,0,0,1,2,2,-1)\) has Lipschitz seminorm \(1\), realizes difference \(f(0)-f(1)=1\), and the derivative of \((H_tf)(0)-(H_tf)(1)\) at time zero equals \(1>0\).

## Assumptions and scope

All graphs are finite, simple, undirected, connected, and unweighted; all vertex signals are real valued. The heat generator is the *unnormalized* counting-measure Laplacian \(L=D-A\). Edges are counted once in \(\operatorname{TV}_G\). For connected \(G\), total variation vanishes precisely on constant functions, so the induced operator norm on the quotient is unambiguous. The unicyclic classification allows arbitrary trees attached to cycle vertices before imposing the necessary contractivity conditions.

## Proof

**1. Coarea reduction to indicator cuts.** Let \(T\) be linear and preserve constants. For an arbitrary real function, write its distinct ordered levels as \(a_1<\dots<a_s\). The pointwise identity
\[
f=a_1\mathbf1_V+\sum_{j=1}^{s-1}(a_{j+1}-a_j)\mathbf1_{\{f\ge a_{j+1}\}}
\]
is exact. The edge coarea identity gives
\[
\operatorname{TV}_G(f)=\sum_{j=1}^{s-1}(a_{j+1}-a_j)|\partial\{f\ge a_{j+1}\}|.
\]
By the triangle inequality, the sharp operator bound for \(T\) is therefore attained in the supremum over nontrivial indicators:
\[
\|T\|_{\mathrm{TV}}=\max_{\varnothing\ne S\subsetneq V}
\frac{\operatorname{TV}_G(T\mathbf1_S)}{|\partial S|}.
\]
The equality is not merely an upper bound: every indicator is an admissible test function.

**2. Exact right derivative.** Put \(x=\mathbf1_S\). For a vertex on the selected side, \((Lx)(v)=c_S(v)\); on the other side \((Lx)(v)=-c_S(v)\). Since \(H_tx=x-tLx+O(t^2)\), each crossing edge \(uv\) contributes the first-order variation \(-c_S(u)-c_S(v)\) to its initial absolute difference \(1\), independently of the edge's orientation. An edge not crossing the cut has zero initial difference and contributes \(|c_S(u)-c_S(v)|\) at first order. The total crossing contribution is
\[
-\sum_{uv\in\partial S}(c_S(u)+c_S(v))=-\sum_{v\in V}c_S(v)^2.
\]
Thus \(\frac{d}{dt}_{\!+}\operatorname{TV}_G(H_t\mathbf1_S)|_{t=0}=K_G(S)\). There are finitely many cuts, so the right derivative of the maximum of their ratios is the maximum of their right derivatives; this proves the slope formula.

**3. Local criterion implies all-time contraction.** Write \(b(t)=\|H_t\|_{\mathrm{TV}}\). If all cut slopes are nonpositive, Step 2 gives \(b(h)\le1+o(h)\) as \(h\downarrow0\). Since \(H_{s+t}=H_sH_t\), the operator norm is submultiplicative. For every \(t>0\),
\[
b(t)\le b(t/N)^N\le(1+o(t/N))^N\longrightarrow1
\]
as the positive integer \(N\to\infty\). Conversely, if any cut slope is positive, its indicator has strictly growing variation near time zero. This proves Theorem A, including both directions without requiring a curvature hypothesis.

**4. Bridge obstruction.** If \(uv\) is a bridge and \(S\) is one connected component after deleting it, then \(c_S(u)=c_S(v)=1\) and all other crossing degrees vanish. Every noncut edge incident to either endpoint contributes \(1\); there are \(\deg(u)+\deg(v)-2\) such edges. Hence
\[
K_G(S)=\deg(u)+\deg(v)-4.
\]
In a unicyclic graph, if an attached tree contains a path beyond the first off-cycle vertex, its first bridge has endpoint degrees at least \(3\) and \(2\), so its cut has positive slope. If two leaves attach to the same cycle vertex, that vertex has degree at least \(4\), and the edge to either leaf has degree sum at least \(5\). Therefore a contractive unicyclic graph can only consist of its cycle plus at most one leaf at each cycle vertex.

**5. Long cycles with attachments.** Suppose \(k\ge6\) and a leaf is attached at cycle vertex \(0\). Select cycle vertices \(1,2,3\) and put each attached leaf on the same side as its parent cycle vertex. On the bare cycle, precisely the four cycle vertices \(0,1,3,4\) have nonzero crossing degrees, all equal to \(1\); both complementary cycle arcs have at least three vertices, so each contributes two internal edges whose crossing-degree difference is \(1\). Thus the bare-cycle cut has \(K=0\). A leaf at vertex \(0\), or indeed at any of these four boundary vertices, contributes an additional \(1\) from its uncut pendant edge and no other change to the cut crossing degrees. Hence \(K\ge1\). This shows that a long cycle is contractive only with no attachments.

**6. A pentagon with at least three leaves.** If at least three distinct cycle vertices carry a leaf, choose an unmarked cycle vertex \(z\), if there is one; otherwise choose any \(z\). Let the selected cycle vertices be the adjacent pair \(z+2,z+3\) modulo five, again keeping every leaf with its parent. The four cycle vertices other than \(z\) are the boundary vertices, each of crossing degree \(1\); the fifth has crossing degree zero. The cycle's own contribution is \(K=-2\). At least three of those four vertices have leaves when \(z\) is unmarked, and all four do when every vertex is marked. Therefore \(K\ge-2+3=1\). These are all remaining necessary obstructions.

**7. Sufficient cases and a finite complete certificate.** A bare cycle is contractive because cyclic edge differences commute with the cyclic heat semigroup, which is positive and has column sums one: the edge \(\ell^1\) norm cannot grow. For a triangle or square with at most one leaf at every cycle vertex, and for a pentagon with at most two such leaves, the remaining cases are a finite complete list. They are verified exhaustively by the standalone exact-integer program `verify_graph_bv_heat.py`: for each allowed attachment subset, it enumerates every nonempty proper vertex cut, computes \(K_G(S)\), and independently reconstructs the first variation directly from \(L\mathbf1_S\). The table records the maximum over all cuts and all attachment choices with the specified leaf count:

| cycle length | pendant-leaf count | largest \(K_G(S)\) |
|---|---|---|
| \(3\) | \(0\) | \(-6\) |
| \(3\) | \(1,2,3\) | \(0\) |
| \(4\) | \(0\) | \(-4\) |
| \(4\) | \(1,2,3,4\) | \(0\) |
| \(5\) | \(0\) | \(-2\) |
| \(5\) | \(1,2\) | \(0\) |

For each row all indicated attachment subsets and all nontrivial cuts are enumerated, not sampled. The largest graph in this finite sufficiency check has eight vertices, so the search is entirely exhaustive. Step 3 upgrades its exact inequalities to all positive times. Combined with Steps 4–6, this proves the complete infinite unicyclic classification.

**8. Lipschitz separation.** For the seven-vertex example, the listed signal satisfies \(|f(u)-f(v)|\le1\) on every edge and \(f(0)-f(1)=1\). Directly evaluating the Laplacian gives \((Lf)(0)=-1\) and \((Lf)(1)=0\), hence
\[
\left.\frac{d}{dt}\big((H_tf)(0)-(H_tf)(1)\big)\right|_{t=0}
=-(Lf)(0)+(Lf)(1)=1.
\]
Thus its Lipschitz seminorm exceeds one for all sufficiently small positive times, although Steps 3 and 7 imply graph-total-variation contraction for every time. This rules out deriving the classification as a mere special case of Lipschitz heat contractivity.

## Verification

Run `python3 verify_graph_bv_heat.py` using Python 3 and no additional packages. The script exhausts 40 allowed small-cycle attachment graphs and checks 3,064 nontrivial cuts, including an independently computed derivative on every one. It also verifies explicit obstructions on long cycles, all three-or-more-leaf pentagons, bridge degree-sum identities, and the separating Lipschitz example. Key successful diagnostics: `ALL_SMALL_CYCLE_ATTACHMENT_PATTERNS_VERIFIED 40`, `EXACT_CUT_SLOPE_VS_INDEPENDENT_FIRST_VARIATION_VERIFIED 3064`, and `ALL_GRAPH_BV_HEAT_CERTIFICATES_PASSED`. Its exact finite case enumeration is a complete proof of only the bounded small-cycle subcases; the universal reduction and the infinite-family obstructions have the separate analytical proofs given above.

## Relationship to prior work

The edge-total-variation functional and coarea principle are standard in graph analysis, and the semigroup/curvature literature provides substantial adjacent theory. Bauer–Horn–Lin–Lippner–Mangoubi–Yau (arXiv:1306.2561, first public 2013-06-11) obtain positive-heat-solution Li–Yau gradient bounds, not an exact edgewise \(\ell^1\)-variation contractivity criterion. Münch–Wojciechowski (arXiv:1712.00875, Theorem 3.8) characterize \(\ell^\infty\) edge-gradient contraction in terms of Ollivier curvature; the seven-vertex example above separates their Lipschitz property from the present one. Münch (arXiv:1907.13514, Theorem 3.1.1) uses *total-variation distance between probability measures*, an \(\ell^1\) vertex-mass metric, not the sum of absolute differences across graph edges. Giga–van Gennip–Okamoto (2022 preprint) treat the **nonlinear total-variation gradient flow**, not the **linear Laplacian heat flow** examined here. The accessible literature inspected did not state the complete cut criterion with the all-unicyclic classification. A historically implicit equivalent in Banach-space semigroup or discrete edge-\(1\)-form literature cannot be excluded.

## Limitations

The theorem is restricted to finite, simple, connected, *unweighted* graphs, the unnormalized counting-measure Laplacian, real-valued vertex signals, and the sum of absolute undirected edge differences. It does not classify all graphs satisfying the cut criterion or determine a closed form for their full time-dependent norms. The cut test is finite and exact but potentially exponential in the number of vertices. External novelty is assessed against the accessible records and inspected literature; no claim of exhaustive publication priority or independent certification is made.

## References

1. F. Bauer, P. Horn, Y. Lin, G. Lippner, D. Mangoubi, S.-T. Yau, *Li-Yau inequality on graphs*, arXiv:1306.2561 (first submitted 2013-06-11), https://arxiv.org/abs/1306.2561.
2. F. Münch, R. K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875 (2017), https://arxiv.org/abs/1712.00875.
3. F. Münch, *Non-negative Ollivier curvature on graphs, reverse Poincaré inequality, Buser inequality, Liouville property, Harnack inequality and eigenvalue estimates*, arXiv:1907.13514 (2019), https://arxiv.org/abs/1907.13514.
4. Y. Giga, Y. van Gennip, J. Okamoto, *Graph gradient flows: From discrete to continuum*, Hokkaido University Preprint Series in Mathematics 1147 (2022), https://hdl.handle.net/2115/86978.
5. Y. van Gennip, J. Budd, *A Prolegomenon to Differential Equations and Variational Methods on Graphs* (2025), https://doi.org/10.1017/9781009346641.
