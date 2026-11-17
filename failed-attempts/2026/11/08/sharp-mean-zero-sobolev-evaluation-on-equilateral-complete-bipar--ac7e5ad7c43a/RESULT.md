# Sharp mean-zero Sobolev evaluation on equilateral complete bipartite metric graphs

## Finding

Let \(m,n\ge3\) be integers. Regard every edge of the complete bipartite graph \(K_{m,n}\) as a closed interval of length \(1\), and give the resulting connected metric graph \(G_{m,n}\) its unnormalized arclength measure \(ds\). On the real Hilbert space
\[
\mathcal H_{m,n}=\left\{f\in C(G_{m,n}):f|_e\in H^1(e)\ \text{for every edge }e,\quad \int_{G_{m,n}}f\,ds=0\right\},
\qquad \|f\|_{\mathcal H}^2=\int_{G_{m,n}}|f'|^2\,ds,
\]
the **exact squared optimal embedding norm** is
\[
\boxed{\sup_{f\ne0}\frac{\|f\|_\infty^2}{\int_{G_{m,n}}|f'|^2\,ds}
=K_{m,n}:=\frac{3m^2n^2-20mn+8m+8n}{12mn(mn-m-n)}.}
\]

Orient each of the \(mn\) edges from the part with \(m\) vertices toward the part with \(n\) vertices. On **every edge** exactly one interior point maximizes the squared norm of point evaluation, at the same coordinate
\[
\boxed{t_{m,n}=\frac{m(n-2)}{2(mn-m-n)}=\frac12+\frac{n-m}{2(mn-m-n)}.}
\]
There are precisely \(mn\) distinct maximizing points. If the two part sizes differ, each is displaced from the edge midpoint toward the endpoint of smaller graph-theoretic degree. No original vertex is maximizing. Every nonzero function attaining the sharp embedding norm is a scalar multiple of the mean-zero Kirchhoff Green representer of one of these maximizing evaluations.

In fact, for a point \(x_t\) at coordinate \(t\in[0,1]\) on any oriented edge, its *squared point-evaluation norm* satisfies the exact localization/deficit identity
\[
\boxed{\|\delta_{x_t}\|_{\mathcal H^*}^{2}=K_{m,n}-\frac{mn-m-n}{mn}(t-t_{m,n})^2.}
\]
Thus a squared evaluation norm within \(\varepsilon\) of optimal forces \(|t-t_{m,n}|\le\sqrt{\varepsilon mn/(mn-m-n)}\); conversely this condition is sharp.

For example \(K_{3,3}=37/108\), with the nine edge midpoints as the only maximizing evaluation points. At \((m,n)=(3,5)\), \(t_{3,5}=9/14\) and \(K_{3,5}=439/1260\). In the two high-connectivity regimes,
\[
\lim_{n\to\infty} K_{m,n}=\frac{m}{4(m-1)}\quad(m\ge3\text{ fixed}),\qquad
\lim_{\min(m,n)\to\infty}K_{m,n}=\frac14.
\]

## Assumptions and scope

An edge is a physical line segment, *not* just a pair of discrete endpoints. Its derivative energy is integrated with respect to length. Each of the \(mn\) edges has length \(1\), hence total length \(L=mn\). Graph functions are continuous at all vertices and have real \(H^1\) restrictions on each edge. The mean constraint is with respect to unnormalized arclength; using normalized arclength only in the mean constraint gives the same space, but the energy in the displayed norm is unnormalized. No vertex atoms or prescribed Dirichlet boundary conditions are present. Integers \(m,n\ge3\) are required for the all-interior maximizer classification.

## Proof

**Step 1: Point evaluation and the Green representer.** Since the graph is compact, connected, and consists of finitely many intervals, derivative energy is a Hilbert norm on continuous edgewise \(H^1\) functions of integral zero. For each point \(x\), the unique centered Kirchhoff Green function \(g_x\) satisfies
\[
- g_x''=\delta_x-\frac{1}{L}\,ds,
\qquad \int_Gg_x\,ds=0,
\]
where the equation is interpreted distributionally with outgoing-derivative Kirchhoff conditions at all original vertices. Integration by parts gives \(\int_Gf'g_x'\,ds=f(x)\) for all \(f\in\mathcal H\); thus \(\|\delta_x\|^2=\int_G|g_x'|^2\,ds=g_x(x)\). Taking a maximum over \(x\) yields the squared embedding norm. Equality in Cauchy–Schwarz says that a nonzero extremizing function must be proportional to one such \(g_x\) at a maximizing point.

**Step 2: A direct graph Green calculation.** Distinguish an edge with endpoints \(a\) in the \(m\)-vertex part and \(b\) in the \(n\)-vertex part. Write \(t\) for its coordinate from \(a\) to \(b\), and \(s\in[0,1]\) for the coordinate on another arbitrary edge \(e=(p,q)\). Put \(L=mn\), and let \(w_v\) be vertex potentials, up to an additive constant. The function
\[
g_{x_t}|_e(s)=(1-s)w_p+s w_q-\frac{s(1-s)}{2L}
+\mathbf1_{e=(a,b)}\min(s,t)[1-\max(s,t)]+\eta
\]
solves the required differential equation along each edge. Here \(\eta\) is a global constant chosen for integral zero. Taking outward derivatives at vertices shows that the discrete unit-conductance graph Laplacian \(\mathsf L\) must obey
\[
(\mathsf Lw)_v=(1-t)\mathbf1_{v=a}+t\mathbf1_{v=b}-\frac{\deg(v)}{2L}.
\]
This equation can be checked without an inverse matrix using the following explicit potentials:
\[
\begin{aligned}
w_a&=\frac{1-t}{n},& w_{a'}&=0\quad(a'\ne a),\\
w_b&=\frac{1/2-t}{mn}+\frac{t}{m},&w_{b'}&=\frac{1/2-t}{mn}\quad(b'\ne b).
\end{aligned}
\]
Indeed, the sum of the \(n\) potentials on the second part is exactly \(1/(2m)\), and the sum of the \(m\) on the first is \((1-t)/n\); substitution checks every distinguished and undistinguished vertex equation. Further,
\[
\sum_v\deg(v)w_v=\frac32-t,\quad
\int_0^1\frac{s(1-s)}{2L}\,ds=\frac{1}{12L},\quad
\int_0^1\min(s,t)[1-\max(s,t)]\,ds=\frac{t(1-t)}2.
\]
Integrating over all edges therefore gives the unique centering shift
\[
\eta=\frac{t^2-4/3}{2mn}.
\]
At the source point \(s=t\) on its distinguished edge, direct substitution yields the exact quadratic
\[
\boxed{g_{x_t}(x_t)=\frac{3m-2}{3mn}+\frac{n-2}{n}t-\frac{mn-m-n}{mn}t^2.}\tag{1}
\]
Continuity extends (1) to \(t=0,1\). Thus it covers all physical graph points, since every point lies on at least one edge and all oriented edges are equivalent.

**Step 3: Sharp maximization and equality.** Let \(D=mn-m-n\). For \(m,n\ge3\), \(D>0\); moreover \(m(n-2)>0\) and \(2D-m(n-2)=n(m-2)>0\). Consequently the strict concave quadratic (1) has its unique maximizer at \(0<t_{m,n}=m(n-2)/(2D)<1\). Completing the square gives
\[
\begin{split}
g_{x_t}(x_t)&=K_{m,n}-\frac{D}{mn}(t-t_{m,n})^2,\\
K_{m,n}&=\frac{3m-2}{3mn}+\frac{m(n-2)^2}{4nD}
=\frac{3m^2n^2-20mn+8m+8n}{12mnD}.
\end{split}
\]
The strict deficit shows that exactly one point per edge is maximizing and no endpoint is. Distinct edges have disjoint interiors, so there are exactly \(mn\) such points. The equality classification follows from Step 1. Taking limits in the displayed rational expression gives the two asymptotics.

## Verification

The accompanying standalone Python/SymPy checker (`verify.py`) symbolically verifies the Green-potential identities, the quadratic completion, the strict displacement formula, the symmetric sharp constant, the \(K_{2,n}\) boundary consistency check, and the asymptotic limits. An **independent** rational calculation subdivides a source edge at each evaluation point, builds the full Kirchhoff Laplacian with the source as a new vertex, solves the mean-zero Poisson equation, and separately checks equality of its diagonal Green value with its exact derivative energy. The checker passed \(87\) exact subdivision instances over \(2\le m,n\le6\) and several rational coordinates. These finite checks are corroboration; the universal claims follow from the derivation and algebra above.

Run with Python 3 and SymPy installed: `python verify.py`.

## Relationship to prior work

Solomyak [1] establishes general Sobolev approximation and embedding estimates on compact metric graphs, without the explicit complete-bipartite sharp evaluation profile. Baker–Faber [2] explains the metric-graph Laplacian and its discrete Kirchhoff representation. Baker–Rumely [3] establishes general metrized-graph Green functions and tabulates eigenvalue examples including \(K_{3,3}\), but the inspected sections and example do not provide formula (1), its global maximum, or the complete maximizer classification. Gervacio [4] treats resistance distances **between original graph vertices** of complete multipartite graphs; its accessible abstract does not address the continuum edge-interior Sobolev point evaluations. The complete Gervacio text was unavailable for comparison, so implicit broader coverage cannot be fully excluded.

The boundary \(m=2\) is a theta graph with \(n\) parallel paths of length \(2\) and already fits the known parallel-path theory; **no novelty is asserted for that boundary**. Our theorem addresses \(m,n\ge3\), where the graph has many vertices of degree at least three and is not a two-terminal parallel-path graph. Generic Green theory is used as an analytical framework, not claimed as new. Published mathematical-record searches did not identify an equivalent sharp complete-bipartite interior localization theorem; this absence is not a uniqueness or priority certificate.

## Limitations

The result assumes real-valued functions, strictly positive equal unit edge lengths, continuous metric edges, arclength mean zero, and quadratic derivative energy. It does not treat general multipartite graphs, unequal edge lengths, higher Sobolev orders, vertex-weighted means, discrete-only energies, or arbitrary nonlinear embedding exponents. The priority comparison is qualified by inaccessible full text of [4] and possible unindexed equivalent formulations. No independent mathematical audit has been performed.

## References

[1] M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235 (public preprint 23 June 2002), introduction and Theorems 1.1–1.2. https://arxiv.org/abs/math/0206235

[2] M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428 (first posted 25 July 2004), especially Sections 4–5. https://arxiv.org/abs/math/0407428

[3] M. Baker and R. Rumely, *Harmonic analysis on metrized graphs*, arXiv:math/0407427 (first posted 25 July 2004), Sections 1.5–1.6 and the \(K_{3,3}\) example. https://arxiv.org/abs/math/0407427

[4] S. V. Gervacio, *Resistance distance in complete n-partite graphs*, *Discrete Applied Mathematics* **203** (2016), 53–61. DOI:10.1016/j.dam.2015.09.017. Abstract and metadata examined, full text unavailable.
