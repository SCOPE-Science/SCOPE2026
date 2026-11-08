# Minimum-degree-three localization for sharp Sobolev evaluation on complete multipartite metric graphs

## Finding

**Theorem.** Fix integers \(p\ge 2\) and \(s_1\ge s_2\ge\cdots\ge s_p\ge1\) with \(N=\sum_i s_i\ge3\). Give the complete multipartite graph \(G=K_{s_1,\ldots,s_p}\) unit-length metric edges and unnormalized arclength \(ds\). Put
\[
 m=\frac{N^2-\sum_i s_i^2}{2},\quad d_i=N-s_i,\quad
 B_i=\frac{N-3}{2}+\frac{s_i}{N}+\frac{(N-1)m}{N d_i},\quad
 C_0=\frac{m-N+1}{6},
\]
\[
 J=\frac12\sum_i s_i d_i B_i+\frac{m(2m-2N+1)}6,
 \qquad
 \alpha_{ij}=m-1-\frac{m(N-1)}N\left(\frac1{d_i}+\frac1{d_j}\right).
\]
For real continuous edgewise-\(H^1\) functions with \(\int_G f\,ds=0\), let
\[
 \mathcal K(G)=\sup_{f\ne0}\frac{\|f\|_\infty^2}{\int_G|f'|^2\,ds}.
\]
Write \(D=N-s_1\), the minimum combinatorial vertex degree.

**Interior regime (\(D\ge3\)).** Let \(\Delta=B_1-B_2\) and \(\alpha=\alpha_{12}\). Then \(0\le\Delta<\alpha\), and
\[
 \boxed{\mathcal K(G)=\frac1m\left[C_0+\frac{B_1+B_2}{2}+\frac\alpha4+\frac{\Delta^2}{4\alpha}\right]-\frac{J}{2m^2}.}
\]
Every norm-maximizing evaluation point lies in the interior of an edge connecting two *distinct parts whose sizes are the two largest part sizes* (allowing ties), and every such edge has exactly one maximizing point. Orient such an edge from a part of size \(s_2\) to a part of size \(s_1\); the coordinate is
\[
 \boxed{t_*=\frac12\left(1+\frac\Delta\alpha\right)\in[1/2,1).}
\]
If \(s_1=s_2\), the maximizing points are midpoints. On every eligible edge, the squared evaluation-norm deficit from the global optimum is exactly \(\alpha(t-t_*)^2/m\).

**Low-degree regime (\(D\le2\)).** The exact constant is
\[
 \boxed{\mathcal K(G)=\frac{B_1+C_0}{m}-\frac{J}{2m^2}.}
\]
The complete classification of maximizing points is as follows. If \(G\) is the triangle \(K_{1,1,1}\) or the square \(K_{2,2}\), *every point* of the metric graph is maximizing. In every other case with \(D\le2\), the maximizing points are precisely the vertices belonging to a part of largest size. The possibilities are stars \(K_{M,1}\) with \(M\ge2\), graphs \(K_{M,2}\) with \(M\ge3\), and graphs \(K_{M,1,1}\) with \(M\ge2\).

In both regimes, every nonzero norm-attaining function is a real scalar multiple of the centered resistance Green function at one of the maximizing points. All the constants are rational for the stated integer part sizes.

## Assumptions and scope

The graph is finite, connected, simple and completely multipartite with at least three vertices; each physical edge is an interval of length one. The energy space consists of real continuous functions whose restrictions to edges belong to \(H^1(0,1)\), with vanishing **arclength mean** and Hilbert norm squared \(\int_G|f'|^2ds\). Vertex masses and additional edge densities are absent. The statement is about the full continuum of points of the metric graph, not merely its original vertices. The embedding norm in the theorem is *squared*.

## Proof

**1. Centered evaluation and resistance.** For a compact connected metric graph of total length \(m\), let \(r(x,y)\) denote electrical effective resistance between arbitrary points. Define
\[
 F(x)=\int_G r(x,y)\,ds_y,\qquad J=\int_G F(x)\,ds_x,
\]
\[
 g_x(y)=\frac{F(x)+F(y)}{2m}-\frac{r(x,y)}2-\frac{J}{2m^2}.
\]
The resistance Laplacian identity \(\Delta_y r(y,x)=2\mu_{\mathrm{can}}-2\delta_x\), where \(\mu_{\mathrm{can}}\) is independent of \(x\), gives \(\Delta_y g_x=\delta_x-ds/m\). Also \(\int_G g_x\,ds=0\), by symmetry and the definition of \(J\). Integration by parts therefore yields \(f(x)=\int_G f'(y)g_x'(y)\,ds_y\) for every mean-zero \(f\) in the stated energy space. Consequently
\[
 \|\delta_x\|^2=g_x(x)=\frac{F(x)}m-\frac{J}{2m^2},
\]
and equality in the energy Cauchy--Schwarz inequality holds precisely for scalar multiples of \(g_x\). Thus it suffices to maximize \(F\) over the *entire metric graph*.

**2. Integrating resistance along edges.** Let \(e=uv\) be a unit edge with endpoint resistance \(q=r(u,v)\), and write \(x_t\in e\) for its point at distance \(t\) from \(u\), \(0\le t\le1\). Elementary series--parallel reduction gives, for \(y\) outside the open edge,
\[
 r(x_t,y)=(1-t)r(u,y)+t r(v,y)+(1-q)t(1-t).
\]
For \(y=x_z\) on the same edge, the exact formula is \(r(x_t,x_z)=|t-z|-(1-q)|t-z|^2\). Integrating the latter over \(z\in[0,1]\) shows that its difference from the linearly interpolated endpoint integrals equals \(-q t(1-t)\). Hence, summing over all \(m\) edges,
\[
 F(x_t)=(1-t)F(u)+tF(v)+[m-1-mq]t(1-t).\tag{1}
\]
Similarly, integrating \(r(v,x_t)\) over one edge gives \((r(v,u)+r(v,w))/2+(1-r(u,w))/6\). Foster's identity \(\sum_{e}r(e)=N-1\) therefore implies, for each original vertex \(v\),
\[
 F(v)=\frac12\sum_{w\in V(G)}\deg(w)r(v,w)+\frac{m-N+1}{6}.\tag{2}
\]
Integrating (1) over all edges, again using Foster's identity, yields
\[
 J=\frac12\sum_{v\in V(G)}\deg(v)\big(F(v)-C_0\big)
   +\frac{m(2m-2N+1)}6.\tag{3}
\]
These are continuum arclength integrals, not approximations based on subdivided vertex samples.

**3. Exact multipartite vertex scores.** Set \(d_i=N-s_i\). The combinatorial Laplacian is multiplication by \(d_i\) on zero-sum fluctuations inside part \(i\), multiplication by \(N\) on partwise-constant vectors orthogonal to constants, and zero on constants. Applying its pseudoinverse gives
\[
 r(v,w)=\frac2{d_i}\quad(v\ne w\text{ in part }i),
\qquad
 r(v,w)=\frac{N-1}{N}\left(\frac1{d_i}+\frac1{d_j}\right)
 \quad(v\in i,\ w\in j,\ i\ne j).
\]
Substitute these into (2), use \(\sum_i s_i d_i=2m\), and simplify to get exactly \(F(v)=B_i+C_0\) for \(v\) in part \(i\). Formula (3) becomes the displayed expression for \(J\). On an edge joining parts \(i,j\), equation (1) now reads
\[
 F(x_t)=C_0+(1-t)B_i+tB_j+\alpha_{ij}t(1-t).\tag{4}
\]

**4. Which pair of parts can maximize?** If \(s_i>s_j\) and \(k\) is a third part, compare an edge from part \(k\) to part \(i\) with one from part \(k\) to part \(j\), parametrized from part \(k\). Formula (4) gives the exact pointwise difference
\[
 \frac{t(s_i-s_j)}N+\frac{t^2m(N-1)}N
 \left(\frac1{N-s_i}-\frac1{N-s_j}\right)>0
 \qquad(0<t\le1).\tag{5}
\]
Thus replacing either endpoint class by a strictly larger available class increases its edge profile at every positive coordinate. It follows by successive replacements that the global maximum is achieved by an edge between two largest classes or at a vertex of a largest class. Further, if the maximizing profile on a largest-pair edge has a strict interior maximum, no vertex and no edge of any smaller pair can tie it. This is a comparison of *full continuum profiles*, not just endpoint resistances.

**5. The sharp degree threshold.** Set \(M=s_1\), \(L=s_2\), \(D=N-M\), \(\Delta=B_1-B_2\), \(\alpha=\alpha_{12}\). Since \(M\ge L\), \(\Delta\ge0\). From the definitions,
\[
 \alpha-\Delta
 =m\left(1-\frac{2(N-1)}{ND}\right)-1-\frac{M-L}{N}.\tag{6}
\]
If there are exactly two parts, then \(m=MD\), \(L=D\), and (6) reduces to \(\alpha-\Delta=M(D-2)\). For \(D\ge3\) it is strictly positive. If there are at least three parts and \(M=1\), the graph is \(K_N\), with \(N\ge4\) when \(D\ge3\); here \(\Delta=0\) and \(\alpha=N(N-3)/2>0\). In the remaining case (at least three parts, \(M\ge2\), \(D\ge3\)), the graph induced by all vertices outside a largest part has at least \(D-1\) edges. Therefore \(m\ge MD+D-1\ge8\), while
\[
 1-\frac{2(N-1)}{ND}>1-\frac2D\ge\frac13,
 \qquad 1+\frac{M-L}N<2.
\]
It follows from (6) that \(\alpha-\Delta>0\). Hence (4) for the largest pair has the unique interior maximum at \(t_*=(1+\Delta/\alpha)/2\), with value \(C_0+(B_1+B_2)/2+\alpha/4+\Delta^2/(4\alpha)\). The exact quadratic deficit on an eligible edge is \(\alpha(t-t_*)^2\), and (5) proves completeness of the maximizing-point classification.

If \(D=2\), the graph is either \(K_{M,2}\) or \(K_{M,1,1}\), and (6) is zero. For \(M>2\) in the bipartite case or \(M>1\) in the tripartite case, \(\Delta=\alpha>0\), so the largest-pair profile increases up to its endpoint in the largest part, and only those vertices maximize (using (5)). The exceptional cases are \(K_{2,2}\) and \(K_{1,1,1}\), where \(\alpha=\Delta=0\); their metric graphs are circles, and every point is maximizing. If \(D=1\), the graph is a star \(K_{M,1}\), \(M\ge2\); its edge profiles have negative quadratic coefficient and their maxima occur exactly at the leaves in the \(M\)-vertex part. Formula (4) yields the constant in each regime. Finally, the Green representation from Step 1 establishes all norm-attaining functions. \(\square\)

## Verification

The accompanying standard-library exact-rational checker `check_multipartite.py` constructs grounded electrical Laplacians from the actual edge lists. It checks the vertex-resistance and score formulas over 63 complete multipartite size profiles (2--5 classes, sizes at most five, total order at most nine), compares edge-orbit extrema exactly, verifies edge-interior arclength integrals on independently subdivided networks, and evaluates double resistance integrals by exact Simpson integration on small graphs. Seven stated rational sharp constants are checked separately.

Execution: `python3 check_multipartite.py`. Successful execution prints `ALL_MULTIPARTITE_H1_CHECKS_PASSED`. These finite checks corroborate, but do not replace, the all-parameter algebraic proof, in particular its pointwise comparison (5) and degree bound (6).

Examples: \(\mathcal K(K_{1,2,3})=2443/7260\), with each relevant edge oriented from its two-vertex part to its three-vertex part attaining at coordinate \(3/5\); \(\mathcal K(K_{1,1,3})=235/588\), attained at its three highest-part vertices; \(\mathcal K(K_{3,3})=37/108\), at all nine edge midpoints. The triangle and square have respective constants \(1/4\) and \(1/3\), constant evaluation norm along their circles.

## Relationship to prior work

The classical resistance-Laplacian framework and Foster identity are from foundational network and metrized-graph analysis, including Baker--Faber. Solomyak treats Sobolev approximation on general metric graphs. The published complete-multipartite *vertex-to-vertex* resistance formulas of Gervacio and of Das--Yang agree with the resistances in Step 3. They do not, in the inspected material, state the continuum arclength-mean-zero sharp embedding norm, the full classification of maximizing evaluation points, or the minimum-degree-three threshold. The particularly symmetric two-part subfamily with both part sizes at least three already admits an exact sharp formula, so that subfamily is not being presented as a new separate calculation. The claim here is the uniform multipartite classification across arbitrary positive part sizes, including its sharp low-degree exceptions, edge ranking, and equality cases.

## Limitations

Only unit-length edges, uniform arclength, real mean-zero first-order energy, and complete multipartite graphs are covered. This does not establish corresponding statements for arbitrary edge lengths, unequal measures, other graph families, or different exponents. The exact rational verifier tests finitely many sizes and subdivided points; the proof is needed for all sizes and all continuum positions. Bibliographic searches cannot exclude uncatalogued or implicit equivalent results; a 2012 multipartite resistance paper's linked full text was not accessible through its current journal endpoint, and that residual source-access uncertainty remains.

## References

- M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235, originally submitted 23 June 2002. https://arxiv.org/abs/math/0206235.
- M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, originally submitted 25 July 2004; especially the resistance and Foster sections. https://arxiv.org/html/math/0407428v2.
- M. Baker and R. Rumely, *Harmonic analysis on metrized graphs*, arXiv:math/0407427, originally submitted 25 July 2004. https://arxiv.org/abs/math/0407427.
- S. V. Gervacio, *Resistance distance in complete n-partite graphs*, *The Mindanawan Journal of Mathematics* 3 (2012), 1--19. https://journals.msuiit.edu.ph/tmjm/article/view/26.
- K. C. Das and Y. Yang, *Eigenvalues of the resistance-distance matrix of complete multipartite graphs*, *Journal of Inequalities and Applications* 2017, article 296, especially Theorem 2.3. https://link.springer.com/article/10.1186/s13660-017-1570-1.
