# Quartic edge envelopes for sharp biharmonic Sobolev evaluation on metric graphs

## Finding

Let \(G\) be any finite connected loopless metric multigraph with at least two vertices and with positive edge lengths \(\ell_e\). Give \(G\) arclength measure \(ds\) and write \(T=\sum_e\ell_e\). On the real Kirchhoff Laplacian domain \(D(L)\) with \(L=-d^2/ds^2\), impose \(\int_G f\,ds=0\). The sharp constant in
\[
\|f\|_{L^\infty(G)}^2\le \mathcal K_2(G)\int_G|f''(s)|^2\,ds
\]
is exactly computable from a **quartic polynomial on each edge**, with coefficients given by finite-dimensional vertex linear systems and integrations of quadratic polynomials. In particular, no numerical spectral truncation or continuous optimization is necessary. The full set of maximizing evaluation points consists of the maximizing vertices, all interior real roots of the edge-quartic derivatives that reach the global maximum, and any entire edge whose quartic is identically the global maximum.

Here is the explicit formula. Let \(g(x,y)\) be the symmetric, mean-zero Laplace Green kernel of \(G\), normalized by
\[
L_y g(x,y)=\delta_x-\frac{ds}{T},\qquad \int_Gg(x,y)\,dy=0.
\]
For vertices \(a,b\), define
\[
Q_a=\int_Gg(a,y)^2\,dy,\quad Q_b=\int_Gg(b,y)^2\,dy,\quad C_{ab}=\int_Gg(a,y)g(b,y)\,dy,
\]
and \(A=g(a,a)\), \(B=g(a,b)\), \(D=g(b,b)\). On an edge \(e=(a,b)\) of length \(\ell\), let \(x_t\) be the point at fractional coordinate \(t\in[0,1]\). Then \(Q(x_t):=\int_Gg(x_t,y)^2\,dy\) equals
\[
\begin{aligned}
P_e(t)={}&(1-t)^2Q_a+2t(1-t)C_{ab}+t^2Q_b\\
&+\frac{\ell^2t(1-t)}{12T}\Big[8AT+4BT-\ell^2\\
&\hspace{20mm}+t(-12AT+8BT+4DT-\ell^2)\\
&\hspace{20mm}+t^2(4AT-8BT+4DT+\ell^2)\Big]\\
&+\frac{\ell^3t^2(1-t)^2(4T-3\ell)}{12T}.
\end{aligned}
\]
In particular,
\[
\boxed{\mathcal K_2(G)=\max\Big(\{Q_v:v\in V\}\cup\{P_e(t):e\in E,\ 0<t<1,\ P'_e(t)=0\}\Big).}
\]
If an edge polynomial is constant, its endpoint value is already included; its entire interior is norming exactly when that constant equals \(\mathcal K_2(G)\). Every nonzero extremal function for a norming point \(x\) is a nonzero scalar multiple of \(L^{-1}g(x,\cdot)\), where the inverse is restricted to the mean-zero subspace. Conversely those functions attain equality.

The leading quartic coefficient has a particularly simple electrical interpretation. Let \(r_{ab}\) denote the effective resistance between the endpoints of \(e\), with edge resistance equal to its metric length, and let \(p_e=[t^4]P_e(t)\). Then
\[
\boxed{p_e=\frac{\ell_e^2}{3}\left(\ell_e-r_{ab}-\frac{\ell_e^2}{T}\right),\qquad
\sum_e\frac{3p_e}{\ell_e^3}=\beta_1(G)-1,}
\]
where \(\beta_1(G)=|E|-|V|+1\). Thus every bridge has \(p_e=-\ell_e^4/(3T)<0\), while every graph with at least two independent cycles contains a positive-leading-coefficient edge. The sign alone does not determine which edge contains a global maximizer.

## Assumptions and scope

The graph is finite, compact and connected; parallel edges are allowed, but the chosen presentation has no self-loop edges. Each edge is an interval of strictly positive real length, with ordinary unweighted arclength. Functions in \(D(L)\) are real, continuous at vertices, edgewise \(H^2\), and satisfy the usual Kirchhoff balance of outgoing first derivatives at every vertex. These boundary conditions make \(L\) a nonnegative self-adjoint operator with constants as its kernel. A mean-zero function has \(\|Lf\|_2^2=\int_G|f''|^2\); the mean-zero restriction is essential for finite sharp evaluation constants. Edges may be subdivided without changing the intrinsic metric-graph space or the result; the cubic-stationary-point procedure is therefore presentation-independent at the level of its final maximizing set.

All definitions and claims hold for arbitrary real positive edge lengths. Rational lengths make the finite systems rational, with algebraic stationary-point candidates (real roots of cubic equations). The theorem does not require simplicity, a cactus decomposition, edge transitivity, equal lengths, or restriction to any finite list of graph topologies.

## Proof

**1. Evaluation as a Green-kernel norm.** The mean-zero Kirchhoff operator \(L\) has a bounded inverse on the zero-mean part of \(L^2(G)\). For \(f\in D(L)\) with \(\int f=0\), Green's identity gives
\[
f(x)=\langle Lf,g(x,\cdot)\rangle_{L^2(G)}.
\]
Cauchy–Schwarz yields \(|f(x)|^2\le \|Lf\|_2^2\,\|g(x,\cdot)\|_2^2\). Equality is attained for \(Lf=cg(x,\cdot)\) by setting \(f=cL^{-1}g(x,\cdot)\), which belongs to the mean-zero Kirchhoff domain. Hence the **exact** squared point-evaluation norm is \(Q(x)=\int_Gg(x,y)^2\,dy\), and compactness of \(G\) guarantees a maximum.

**2. A finite vertex Green construction.** To compute \(g(a,\cdot)\) for a vertex source \(a\), let \(z_v=g(a,v)\). The Kirchhoff flux equation at any vertex \(v\) is
\[
\sum_{e=(v,w)}\frac{z_v-z_w}{\ell_e}=
\mathbf1_{\{v=a\}}-\frac{1}{2T}\sum_{e\ni v}\ell_e.
\]
Each incident edge is counted separately, including parallel edges. The unique additive normalization is determined by
\[
\sum_{e=(v,w)}\left\{\frac{\ell_e}{2}(z_v+z_w)-\frac{\ell_e^3}{12T}\right\}=0.
\]
The first system is the weighted discrete graph Laplacian with a zero-sum forcing, and the second removes its one-dimensional constant ambiguity. On the oriented edge \(e=(v,w)\), with fractional coordinate \(u\in[0,1]\), the full Green function for the vertex source is exactly
\[
g(a,y_u)=(1-u)z_v+uz_w-\frac{\ell_e^2}{2T}u(1-u).
\]
Consequently, all \(Q_a\) and \(C_{ab}\) are obtainable by integrating products of explicit edgewise quadratic polynomials. All integrals are elementary and finite.

**3. Green function when the source lies inside an edge.** Fix an oriented edge \(e=(a,b)\) of length \(\ell\). Write \(g_a(y)=g(a,y)\), \(g_b(y)=g(b,y)\), and \(b_t(y)=(1-t)g_a(y)+tg_b(y)\). For \(y\) on the same edge at fractional coordinate \(u\), define the tent kernel \(z_t(y)=\ell\min(t,u)(1-\max(t,u))\); let \(z_t(y)=0\) outside that edge. Put \(c_t=\ell^2t(1-t)/(2T)\). The exact global identity is
\[
\boxed{g(x_t,y)=b_t(y)+z_t(y)-c_t.}
\]
It follows by checking the distributional equation \(L_y g(x_t,y)=\delta_{x_t}-ds/T\), continuity, vertex flux balance and the zero-mean condition. Specifically, \(z_t\) has a unit source at \(x_t\) and compensating endpoint fluxes, while the linear combination of endpoint Green sources cancels those fluxes; furthermore \(\int_Gz_t(y)\,dy=\ell^2t(1-t)/2=Tc_t\), establishing the centering. Uniqueness of the mean-zero Green function proves the identity.

**4. Quartic expansion.** Since \(\int b_t=0\), expansion of the square and cancellation of constant terms give
\[
Q(x_t)=\|b_t\|_2^2+2\int_e b_t(y)z_t(y)\,dy+\int_ez_t(y)^2\,dy-Tc_t^2.
\]
The first term is \((1-t)^2Q_a+2t(1-t)C_{ab}+t^2Q_b\). On the edge, the two endpoint Green kernels have quadratic interpolation given in Step 2, hence the integral in the second term is elementary. Splitting it at \(u=t\) and integrating the two resulting polynomials gives precisely the displayed explicit formula for \(P_e(t)\) in the Finding section, including its last term. This is an identity for **every** real \(t\in[0,1]\), not a sample-based interpolation or an approximation. Each \(P_e\) has degree at most four. A nonconstant polynomial attains its maximum on its closed edge at either an endpoint or a real interior root of its cubic derivative; an identically constant polynomial is handled separately. Taking the finite union over all edges proves the stated sharp constant and the complete norming-point classification.

**5. Quartic coefficient and topology.** Expand only the fourth-degree coefficient of the formula. It reduces to
\[
[t^4]P_e=\frac{\ell_e^2}{3}\left(\ell_e-(g(a,a)-2g(a,b)+g(b,b))-\frac{\ell_e^2}{T}\right).
\]
The electrical identity \(g(a,a)-2g(a,b)+g(b,b)=r_{ab}\) follows by evaluating the zero-mean Green representation of the unit current from \(a\) to \(b\), or by the Kirchhoff energy identity. Therefore the claimed \(p_e\) formula holds. Finally Foster's identity \(\sum_e r_{ab}/\ell_e=|V|-1\), obtained by tracing the weighted incidence Laplacian against its pseudoinverse, implies
\[
\sum_e\frac{3p_e}{\ell_e^3}=\sum_e\left(1-\frac{r_{ab}}{\ell_e}-\frac{\ell_e}{T}\right)=|E|-(|V|-1)-1=\beta_1(G)-1.
\]
A bridge carries all its endpoint-to-endpoint unit current, so \(r_{ab}=\ell_e\), giving the strict negative coefficient. If \(\beta_1(G)\ge2\), the displayed sum is positive, and hence at least one coefficient is positive. This completes the proof.

## Verification

The included standalone `check_biharmonic.py` uses Python 3 and SymPy. Run `python check_biharmonic.py` in the directory containing that file. For each test graph it independently builds the Kirchhoff equation after **subdividing the queried edge** at the selected interior point, obtains the full vertex-source Green function on that new graph, and integrates its square with exact rational arithmetic. It compares those independent values against the edge quartic, independently calculates endpoint resistances and fourth-degree coefficients, and checks an exact Neumann interval formula. The diagnostic output is:

```
TWO_EDGE_METRIC_CIRCLE_CONSTANT_PASSED
FOSTER_CYCLE_RANK_QUARTIC_SUMS_PASSED 10
INDEPENDENT_SUBDIVIDED_GRAPH_GREEN_COMPARISONS_PASSED 140
EXACT_BIHARMONIC_QUARTIC_LEADING_COEFFICIENT_PASSED 35
EXACT_INTERVAL_NEUMANN_BIHARMONIC_EXAMPLE_PASSED
ALL_BIHARMONIC_ENVELOPE_CHECKS_PASSED
```

For a single interval of length \(T\), the formula reduces to \(Q(x_t)=T^3/45-T^3t^2(1-t)^2/3\), so \(\mathcal K_2=T^3/45\) with exactly the two interval endpoints norming. For a metric circle of circumference \(T\), represented by two parallel edges, translation invariance gives \(Q(x)=T^3/720\) at every point. The exact finite calculations corroborate the derivation but cannot replace its universal Green-kernel argument.

## Relationship to prior work

The metric-graph Green operator, resistance identity and spectral expansion are classical ingredients, not new claims. Baker–Rumely study Laplace eigenfunctions and the Green kernel on metrized graphs, including interval and circle examples; their spectral representation implies the abstract squared-Green-diagonal expression for the biharmonic evaluation constant. Baker–Faber develop effective resistance and Fourier analysis on metrized graphs. The new exact statement here is the **explicit arbitrary-edge quartic** for the squared Green diagonal, its finite cubic-root sharp-constant algorithm and exact norming-point classification, and the identification of the fourth-order coefficient with an electrical quantity. The topology identity is an application of the known Foster law, not a new Foster theorem.

Solomyak studies Sobolev approximation on metric graphs rather than the sharp second-derivative Kirchhoff point-evaluation problem. Usman's compact-graph Sobolev inequalities involve first-order variation and Cheeger/coarea methods, not the exact pointwise \(L^{-2}\) evaluation kernel. Borthwick–Jones–Harrell's diagonal heat-kernel and edge-trace theory gives spectral information at graph points but does not supply the finite edgewise quartic formula for the integrated squared Green kernel. Earlier first-derivative sharp evaluation formulas provide a quadratic edge envelope, whereas the present problem uses squared Laplacian energy and has a genuinely different quartic envelope. The equivalence risk from classical biharmonic spline and Green-function literature is real; no assertion of absolute priority or exhaustive literature coverage is made.

## Limitations

The exact operator domain, the mean-zero condition and **unweighted arclength** are part of the theorem. It does not treat vertex masses, nonconstant edge densities, arbitrary self-adjoint vertex conditions, higher powers of the Laplacian, or general Banach-valued maps. The leading quartic coefficient's sign does not by itself locate a global maximizer. Although the finite algorithm is exact, cubic roots need not admit convenient elementary radical expressions for arbitrary edge-length data. Bibliographic priority relative to older spline-kernel formulas is not fully resolved, and independent external validation has not been performed.

## References

1. M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235, first posted 23 June 2002, https://arxiv.org/abs/math/0206235.
2. M. Baker and R. Rumely, *Harmonic Analysis on Metrized Graphs*, arXiv:math/0407427, first posted 25 July 2004, https://arxiv.org/abs/math/0407427.
3. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first posted 25 July 2004, https://arxiv.org/abs/math/0407428.
4. M. Usman, *Sobolev type inequalities for compact metric graphs*, Journal of Inequalities and Applications (2018), https://link.springer.com/article/10.1186/s13660-018-1872-y.
5. D. Borthwick, K. Jones and E. M. Harrell II, *The heat kernel on the diagonal for a compact metric graph*, arXiv:2204.06619, first posted 13 April 2022, https://arxiv.org/abs/2204.06619.
6. R. M. Foster, *The average impedance of an electrical network*, Contributions to Applied Mechanics (1949), classical Foster identity; a standard electrical-network theorem.
