# Sharp graph-cut formula for the anchored-variation Lipschitz modulus of scalar superposition

## Finding
For any finite connected undirected simple graph \(G=(V,E)\) with \(|V|\ge2\), and any root \(r\in V\), put
\[
\|h\|_{G,r}=|h_r|+\sum_{\{u,v\}\in E}|h_u-h_v|.
\]
Let \(g:\mathbb R\to\mathbb R\) be globally Lipschitz and define its coordinatewise superposition on real graph signals by \((S_g(x))_v=g(x_v)\). Write \(a=\operatorname*{ess\,inf}_{t\in\mathbb R}g'(t)\), \(b=\operatorname*{ess\,sup}_{t\in\mathbb R}g'(t)\), and \(m=\max\{|a|,|b|\}\). Here \(g'\) exists almost everywhere, \(a\le b\), and all these numbers are finite. Let \(\operatorname{mc}(G)\) be the maximum number of graph edges crossing a bipartition of \(V\). Then the **global sharp two-input Lipschitz modulus** is
\[
\boxed{\operatorname{Lip}_{G,r}(S_g)=m+(b-a)\operatorname{mc}(G).}
\]
It is independent of the anchor vertex. In particular, coordinatewise positive part has coefficient \(1+\operatorname{mc}(G)\), and absolute value has coefficient \(1+2\operatorname{mc}(G)\). If \(g\) is affine, this reduces to its absolute slope. For non-affine globally Lipschitz \(g\), the coefficients on paths of \(n\) vertices grow at least linearly as \(n\to\infty\).

Consequently, positive-part truncation has sharp coefficient \(n\) on a path with \(n\) vertices, \(1+n\) on an even cycle, \(n\) on an odd cycle, and \(1+\lfloor n^2/4\rfloor\) on a complete graph of order \(n\) (the cyclic formulas apply for \(n\ge3\)). On arbitrary graphs, computing this sharp coefficient is NP-hard through its exact maximum-cut identity. The coefficient is attained by distinct finite inputs for positive part and for absolute value, although arbitrary smooth nonlinearities need not attain it.

## Assumptions and scope
All signals and scalar functions are real. The graph is finite, connected, unweighted, simple and has at least two vertices; an edge appears exactly once in the total variation sum. The anchored variation is a norm because the graph is connected. The two-input modulus is the supremum of \(\|S_g(x)-S_g(y)\|_{G,r}/\|x-y\|_{G,r}\) over distinct \(x,y\in\mathbb R^V\). No hypothesis that \(g(0)=0\) is needed. The maximum cut counts crossing **edges**, not vertices, and is independent of the root. Constant-addition of \(g\) does not change the coefficient.

## Proof
**1. Secant slopes and diagonal masks.** A globally Lipschitz real function is absolutely continuous on every bounded interval and differentiable almost everywhere. The fundamental theorem of calculus yields \(a\le(g(s)-g(t))/(s-t)\le b\) whenever \(s\ne t\). For any signals \(x,y\), write \(h=x-y\). At every vertex choose \(s_v\in[a,b]\) so that \(g(x_v)-g(y_v)=s_vh_v\), choosing an arbitrary value when \(h_v=0\). Hence
\[
\|S_g(x)-S_g(y)\|_{G,r}=\|s\odot h\|_{G,r}.
\]
For fixed \(h\), the right side is convex in each \(s_v\), so its maximum over the finite box \([a,b]^V\) is realized at a corner: every slope may be replaced by either \(a\) or \(b\), without decreasing the norm.

**2. Universal graph-cut upper bound.** At a corner, let \(C\subseteq E\) comprise edges whose endpoints receive different slopes. On any edge with equal slopes, \(|s_uh_u-s_vh_v|\le m|h_u-h_v|\). On any edge in \(C\), rewrite
\[
 s_uh_u-s_vh_v=s_u(h_u-h_v)+(s_u-s_v)h_v,
\]
which gives
\[
|s_uh_u-s_vh_v|\le m|h_u-h_v|+(b-a)|h_v|.
\]
Because the graph is connected, a path from \(r\) to \(v\) shows \(|h_v|\le|h_r|+\sum_{e\in E}|\nabla_e h|=\|h\|_{G,r}\). Also \(|s_rh_r|\le m|h_r|\). Summing across edges proves
\[
\|s\odot h\|_{G,r}\le\bigl(m+(b-a)|C|\bigr)\|h\|_{G,r}\le\bigl(m+(b-a)\operatorname{mc}(G)\bigr)\|h\|_{G,r}.
\]
The argument includes \(a=b\), for which the cut correction is zero.

**3. Matching bound with a constant perturbation.** Suppose \(a<b\). Take a maximum graph cut \(V=A\sqcup B\). Choose differentiability points \(t_a,t_b\) of \(g\) whose derivatives approximate \(a,b\), respectively, as closely as desired; these exist by the definitions of essential infimum and supremum. Interchange the sides, if necessary, so the root is assigned a point whose derivative has absolute value arbitrarily close to \(m\). Form a base signal \(x\) taking those two scalar levels on the respective sides and put \(y=x+\varepsilon\mathbf1\), where \(\varepsilon>0\) tends to zero. The denominator is exactly \(\|y-x\|_{G,r}=\varepsilon\), since \(y-x\) is constant. Dividing the output difference by \(\varepsilon\) gives a vector converging coordinatewise to the assigned derivative on each side. Its anchored variation therefore tends to
\[
|g'(t_{\rm root})|+|g'(t_b)-g'(t_a)|\operatorname{mc}(G),
\]
which tends arbitrarily closely to \(m+(b-a)\operatorname{mc}(G)\). This proves sharpness. If \(a=b\), absolute continuity implies \(g(t)=at+c\), so \(\operatorname{Lip}=|a|\) directly.

**4. Specializations and complexity.** For \(g(t)=t_+\) the two possible slopes are \(0,1\); for \(g(t)=|t|\) they are \(-1,1\). Put base levels in their open affine regions and choose a sufficiently small nonzero constant perturbation. The preceding cut witness then gives exact equality for a finite pair, not merely a limit. The path, cycle and complete-graph cut numbers are respectively \(n-1\), \(n\) or \(n-1\) according to cycle parity, and \(\lfloor n^2/4\rfloor\). Finally, a polynomial-time exact evaluator of the positive-part modulus for arbitrary unweighted simple connected graphs would evaluate \(\operatorname{mc}(G)\) by subtracting one, so its determination contains the classical NP-hard maximum-cut problem. For a possibly disconnected instance with \(c\) components, join one selected vertex of each component to the next by \(c-1\) new bridge edges. Each old component can have its cut colors swapped independently, so all new bridges can be cut simultaneously, and the resulting connected graph has maximum-cut size equal to the old maximum-cut size plus \(c-1\). This gives a polynomial reduction to the connected case. No convergence or regularity claim beyond the displayed formula is needed.

## Verification
Run `python verify.py` with Python 3 standard library. It exhaustively tests the **diagonal-mask** formula for every connected labelled graph on two through four vertices, four exact rational slope intervals, and every ternary test increment; it checks exact cut witnesses for paths, cycles and complete graphs through twelve vertices and a smooth hyperbolic-tangent near-extremizer. The expected final line is `ALL_ANCHORED_GRAPH_VARIATION_CHECKS_PASS`. Finite ternary enumeration is only a diagnostic; it does not certify every real input. The proof above supplies the unrestricted upper and lower bounds for every finite connected simple graph and every globally Lipschitz scalar function.

## Relationship to prior work
Classical bounded-variation superposition theory studies mapping conditions and local Lipschitz properties for composition in function spaces, rather than the exact two-input modulus in a finite *graph* variation norm. The 2013 Schramm–Korenblum variation paper and the 2014 bounded \(\kappa\Phi\)-variation paper address those mapping and regularity questions; the relevant theorem statements and proofs do not specify a maximum-cut factor for rooted finite graphs. The maximum-cut problem itself is classical and its complexity is not new. The contribution here is the exact graph-dependent superposition modulus and its immediate complete graph-family consequences. A separate established graph-Sobolev truncation estimate uses a quadratic energy norm, unlike the anchored \(\ell^1\) variation measured here; neither its spectral cut formula nor a generic norm comparison yields the exact coefficient proved above. An unindexed equivalent finite-dimensional result remains possible.

## Limitations
The coefficient concerns real pointwise scalar superposition and anchored \(\ell^1\) graph variation, with **unit edge weights** and a single anchored vertex value. It does not assert the same formula for an unanchored seminorm, weighted graph edge costs, vector-valued nonlinearities, infinite graphs, or Hilbert graph-Sobolev energies. For a non-affine smooth \(g\), equality of the supremum with the formula need not entail attainment by two distinct finite inputs. Exact computation of the arbitrary-graph coefficient is generally NP-hard; simple graph-family formulas require known maximum cuts. Historical priority has not been independently established.

## References
1. M. R. Garey, D. S. Johnson, and L. Stockmeyer, *Some simplified NP-complete problems*, Proceedings of the Sixth Annual ACM Symposium on Theory of Computing, 1974. First publicly dated 1974-04-30. https://doi.org/10.1145/800119.803884 . Used only for classical maximum-cut computational hardness.
2. J. L. Jesús, O. Mejía, N. Merentes, and S. Rivas, *The Composition Operator and the Space of the Functions of Bounded Variation in Schramm-Korenblum's Sense*, 2013. First published 2013-10-28. https://doi.org/10.1155/2013/284389 . Relevant material: composition mapping and Lipschitz regularity in the principal theorem and proof.
3. O. Mejía, N. Merentes Díaz, and K. Rzepka, *Locally Lipschitz Composition Operators in Space of the Functions of Bounded κΦ-Variation*, 2014. First published 2014-09-01. https://doi.org/10.1155/2014/606307 . Relevant material: main characterization, including Theorem 17 and its proof.
