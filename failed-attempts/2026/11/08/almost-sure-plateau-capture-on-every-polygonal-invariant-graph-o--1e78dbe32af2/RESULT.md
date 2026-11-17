# Almost-sure plateau capture on every polygonal invariant graph of the Cima–Gasull–Mañosa–Mañosas map

## Finding
For every real \(a<0\) and \(b\), consider the continuous planar map
\[
F_{a,b}(x,y)=(|x|-y+a,\,x-|y|+b).
\]
Let \(\Gamma_{a,b}\) be the canonical compact forward-invariant polygonal graph constructed in [1] (possibly a singleton). Let \(H_{a,b}\) be the union of the relative interiors of its plateau edges: precisely the edges in the first quadrant with direction \((1,1)\) and the edges in the third quadrant with direction \((1,-1)\). Put \(f=F_{a,b}|_{\Gamma_{a,b}}\), and let \(m=\mathcal H^1|_{\Gamma_{a,b}}\) be Euclidean arclength.

**Theorem (full-measure capture).** For every \(a<0\), \(b\in\mathbb R\),
\[
m\left(\Gamma_{a,b}\setminus\bigcup_{n\ge0}f^{-n}(H_{a,b})\right)=0.
\]
In particular, if \(\Gamma_{a,b}\) has positive length, then an \(m\)-almost-everywhere initial state reaches some plateau in finite time. Its subsequent orbit coincides, after one more iterate, with the orbit of one of finitely many plateau images. Thus the at-most-three \(\omega\)-limits of Theorem C of [1] describe almost every graph orbit (with periodic limits in the rational normalized-parameter cases). Moreover, on any positive-length graph there is **no invariant Borel probability absolutely continuous with respect to arclength**.

This strengthens the open-dense plateau capture of Proposition 23 of [1] to full arclength measure for all parameters, beyond the special regimes previously treated in [2]. The statement says nothing about two-dimensional planar Lebesgue measure; a finite graph has zero such measure.

## Assumptions and scope
The canonical polygonal graph is the one from Theorem B of [1], not an arbitrary invariant subset. Each graph contains finitely many straight edges, meeting at finitely many vertices. Its plateau edges are defined as above, with only relative interiors placed in \(H\); inclusion or exclusion of finitely many endpoints does not affect arclength. When the canonical graph is a singleton, its arclength vanishes, so the measure statement is vacuous and the nonexistence assertion is not made. The parameter restriction \(a<0\) is essential to the chosen graph construction. In the proof normalize \(a=-1\) by the positive spatial scaling \(t=-a\): \(F_{a,b}(tz)=tF_{-1,b/t}(z)\).

## Proof
**1. Uniform expansion outside collapsed edges.** Work at \(a=-1\). The finite graph has tangents in the four directions \((1,0),(0,1),(1,1),(1,-1)\) (Lemma 22(a) of [1]). Directly applying the four quadrant matrices listed in Lemma 21 of [1] shows that an edge of direction \((1,1)\) in quadrant I or \((1,-1)\) in quadrant III is mapped to a point. Every other edge segment is mapped affinely with absolute *Euclidean arclength* slope either \(\sqrt2\) or \(2\), as in Lemma 22(b) of [1]. Consequently, any segment whose first \(N\) orbit positions avoid plateau interiors, and which is subdivided so all intervening images lie in single graph edges, has affine \(N\)-step arclength slope at least \((\sqrt2)^N\). Branch ambiguities occur at finitely many source or preimage vertices for any fixed \(N\), and hence affect no arclength measure.

**2. Finite four-step partition.** Identify each of the finitely many graph edges with a disjoint compact arclength interval, ignoring their shared endpoints of zero measure. Split these intervals at all preimages through time four of vertices, quadrant/edge changes, and the endpoints of the plateau intervals. Discard intervals that enter a plateau at one of their first four positions. The remaining positive-length connected intervals \(B\) are finitely many, with pairwise disjoint interiors. On every such \(B\), the fourth iterate is affine and injective onto a subinterval of a single target edge, with arclength slope \(s_B\ge4\). Because the collection is finite, if nonempty, \(\delta=\min_B m(B)>0\). If no such interval exists, almost-everywhere capture within four steps follows immediately, so assume it is nonempty.

**3. A strict bounded-variation contraction for surviving densities.** Define the killed transfer operator on integrable arclength densities by
\[
(Pg)(y)=\sum_{\substack{x\in f^{-1}(y)\\x\notin H}}\frac{g(x)}{|D_{\mathrm{arc}}f(x)|},
\]
using noncollapsed affine branches only and disregarding finite vertex sets. For \(g\ge0\) its total mass can only decrease: \(\|Pg\|_1\le\|g\|_1\). The adjoint identity says
\[
\int_A P^n1\,dm=m\bigl(\{x:f^j(x)\notin H\ (0\le j<n),\ f^n(x)\in A\}\bigr)
\]
for all measurable \(A\). On the finite disjoint edge intervals write \(\operatorname{Var}(g)\) for the sum of one-dimensional total variations. Each four-step surviving branch contributes \(1_{f^4(B)}g\circ(f^4|_B)^{-1}/s_B\) to \(P^4g\). Extending by zero outside its image increases variation by at most two endpoint jumps, so
\[
\operatorname{Var}(P^4g)
\le\sum_B\frac{\operatorname{Var}_B(g)+2\sup_B|g|}{s_B}.
\]
The elementary BV inequality \(\sup_B|g|\le\operatorname{Var}_B(g)+m(B)^{-1}\int_B|g|\,dm\) and \(s_B\ge4\) imply
\[
\boxed{\operatorname{Var}(P^4g)\le\tfrac34\operatorname{Var}(g)+\tfrac1{2\delta}\|g\|_1.}
\]
Here the terms \(\operatorname{Var}_B(g)\) sum to at most the original total variation, and the intervals are disjoint. All one-, two-, and three-step operators also preserve BV with finite bounds, because each has finitely many affine positive-slope branches. It follows by iteration from \(g_0\equiv1\) that \(g_n=P^n1\) is bounded uniformly in BV and \(L^1\) as \(n\) varies.

**4. Compactness and the dense open capture set.** Let \(S_n\) be the graph states avoiding \(H\) at times \(0,\ldots,n-1\); then \(m(S_n)=\int g_n\,dm\) decreases to \(m(K)\), where \(K=\bigcap_n S_n\). Suppose \(m(K)>0\). Compactness of BV bounded sets in \(L^1\) on a finite interval union gives a subsequence \(g_{n_j}\to g\) strongly in \(L^1\), with \(g\ge0\), \(g\in BV\), and \(\int g\,dm=m(K)>0\). For each fixed integer \(r\ge0\), the adjoint identity gives
\[
0\le\int_{f^{-r}(H)}g_n\,dm\le m(S_n)-m(S_{n+r+1})\longrightarrow0.
\]
Consequently \(g=0\) almost everywhere on the open set \(U=\bigcup_{r\ge0}f^{-r}(H)\). Proposition 23 of [1] proves **for every normalized parameter** that \(U\) is dense in the canonical graph, and Theorem C of [1] notes it is open. A nonnegative BV function on finitely many intervals that vanishes almost everywhere on an open dense set must be zero almost everywhere: if its integral were positive, it would have a point of positive value at which it is continuous, hence a subinterval where it stays positive, which must intersect the open dense set in a positive-length open subinterval. This contradicts \(\int g=m(K)>0\). Thus \(m(K)=0\), proving full-measure capture.

**5. Consequences and scaling.** For every captured point the orbit from the instant after reaching \(H\) equals the orbit of a collapsed-edge image, proving the finite list of possible asymptotic behaviors from [1]. If \(\nu\ll m\) were an invariant Borel probability, any plateau \(H\) would have \(\nu(H)=0\): the pushforward of \(\nu|_H\) under \(f\) is supported on finitely many points, whereas \(\nu\) has no atoms. Invariance gives \(\nu(f^{-n}(H))=0\) for every \(n\), contradicting \(\nu(U)=1\) since \(m(\Gamma\setminus U)=0\). Finally the scaling \(z\mapsto tz\) transfers both assertions to every \(a<0\) and \(b\in\mathbb R\).

## Verification
The provided standalone Python program `check_branch_expansion.py` computes the 16 quadrant/direction images exactly using integer and rational arithmetic. It confirms that exactly two combinations collapse, and every noncollapsed squared Euclidean arclength multiplier is \(2\) or \(4\). The BV contraction, finite-branch argument, compactness, and absence of an absolutely continuous stationary probability are proved mathematically above and are not delegated to a finite experiment.

## Relationship to prior work
Cima, Gasull, Mañosa and Mañosas [1] constructed the polygonal invariant graphs, listed the four tangent directions and their affine action (Lemmas 21–22), proved the plateau-preimage set open and dense (Proposition 23), and established the finite list of possible plateau asymptotic behaviors (Theorem C). Their open-dense statement by itself does **not** imply full arclength measure. Their sequel [2], especially Section 5 and Theorem 3, proves full measure only for selected parameter ranges, explicitly treating the general full-measure assertion as open. The present argument adds a uniform finite-step BV contraction to extend that statement to every parameter \(a<0\), without claiming the source graph classification itself as new. Previously described restricted-parameter exact capture results are contained as special cases, not separate novel results.

## Limitations
The statement is relative to canonical polygonal graphs and one-dimensional Hausdorff arclength, not to arbitrary invariant planar sets or absolute continuity relative to planar area. It assumes the prior literature's construction and open-dense Proposition 23, rather than independently reproving their lengthy graph classification. There may be analogous theorems in general expanding graph-map or open dynamical systems literature; the evidence reviewed below supports novelty relative to the identified same-family literature but is not a universal publication-priority guarantee. No independent mathematical audit has been performed.

## References
[1] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant Graphs and Dynamics of a Family of Continuous Piecewise Linear Planar Maps*, arXiv:2410.01052 (first posted 2024-10-01); *Qualitative Theory of Dynamical Systems* 24 (2025), 70; DOI: 10.1007/s12346-025-01221-1. Lemmas 21–22, Proposition 23, Theorem C.

[2] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Further results for a family of continuous piecewise linear planar maps* (later titled *Entropy and omega-limit sets on invariant graphs for a class of planar piecewise linear maps*), arXiv:2503.02411 (first posted 2025-03-04; v4 revised 2026-07-29), Section 5 and Theorem 3; *Communications in Nonlinear Science and Numerical Simulation* 163 (2026), 110602.
