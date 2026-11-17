# Graph-independent sharp stability window for stationary logistic checkerboards

## Finding

Let \(G=(V,E)\) be any finite, connected, simple, undirected bipartite graph with at least one edge, with bipartition \(V=V_0\sqcup V_1\). In the degree-normalized coupled logistic map defined below, for every \(3/8<D<1/2\) there exist exactly two nonconstant equilibria which are constant on each bipartition class: one takes \(u\) on \(V_0\) and \(v\) on \(V_1\), and the other interchanges them, where
\[
 s=1+\frac1{4(4D-1)},\qquad h=\sqrt{s(3/2-s)},\qquad u=\frac{s+h}{2},\quad v=\frac{s-h}{2}.
\]
Both equilibria belong to the open population cube \((0,1)^V\) and are hyperbolic sinks **if and only if**
\[
 \boxed{\frac{4+\sqrt6}{16}<D<\frac{19+\sqrt{73}}{64}.}
\]
The interval is independent of the number of vertices, degree distribution, and connectivity pattern beyond connectedness and bipartiteness. For \(0<D\le3/8\) no strictly positive nonconstant two-color equilibrium exists. At either stability boundary an eigenvalue has modulus one, so the claim makes no nonlinear asymptotic-stability assertion there.

## Assumptions and scope

Write \(d_i\) for the positive degree of vertex \(i\), \(P_{ij}=1/d_i\) for adjacent \(i,j\), and zero otherwise. For a parameter \(0<D<1/2\), consider the synchronous map \(\mathcal T_D:[0,1]^V\to[0,1]^V\) with
\[
 (\mathcal T_D(x))_i=(1-2D)f(x_i)+2D\sum_{j\in V}P_{ij}f(x_j),\qquad f(z)=4z(1-z).
\]
The normalized weights are nonnegative and sum to one. On a cycle graph this is precisely the nearest-neighbor logistic map with exchange weight \(D\) per neighboring site. “Two-color” means constant on each shore \(V_0,V_1\), not that the graph has only two vertices. “Hyperbolic sink” means every eigenvalue of the full \(|V|\)-dimensional derivative has modulus strictly less than one; it implies local exponential attraction. We make no claim of global attraction, unique attractors, or stability of equilibria of other forms.

## Proof

**1. Two-color fixed points.** Every vertex has all its neighbors in the opposite shore, so the two-color subspace is invariant, with map
\[
 (u,v)\longmapsto ((1-2D)f(u)+2Df(v),\,(1-2D)f(v)+2Df(u)).
\]
Suppose \(u\ne v\). Put \(s=u+v\), \(h=u-v\). Subtracting the two equations gives \(1=4(1-4D)(1-s)\), hence \(s=1+1/[4(4D-1)]\). Adding and using \(u^2+v^2=(s^2+h^2)/2\) gives \(h^2=s(3/2-s)\). For \(1/4<D<1/2\), the condition \(h^2>0\) is equivalent to \(D>3/8\), and the resulting \(u,v\) lie strictly between zero and one. For \(0<D<1/4\), the same formal equations either yield nonpositive \(s\), or \(0<s<3/4\) and \(|h|>s\), so one coordinate is nonpositive. At \(D=1/4\), the difference equation is impossible for \(u\ne v\). This proves existence and exclusivity among nonconstant two-color states.

**2. Full graph modes.** Let \(a=1-2D\), \(b=2D\), and \(g_0=f'(u)\), \(g_1=f'(v)\). The full derivative is \(J=(aI+bP)\operatorname{diag}(g_i)\). Since the graph is undirected, conjugating by the diagonal matrix of square roots of degrees makes \(P\) into the symmetric normalized adjacency \(S\), while leaving the shore-constant diagonal of slopes unchanged. In bipartite order, \(S=\begin{psmallmatrix}0&B\\B^\top&0\end{psmallmatrix}\), with singular values \(0\le\sigma\le1\) of \(B\). On each singular-vector pair the derivative is represented by
\[
 J_\sigma=\begin{pmatrix}ag_0&b\sigma g_1\\b\sigma g_0&ag_1\end{pmatrix},\qquad
 \chi_\sigma(z)=z^2-tz+d(\sigma^2),
\]
where
\[
 t=a(g_0+g_1)=\frac{2(2D-1)}{4D-1},\quad Q=g_0g_1=-\frac{8(16D^2-9D+1)}{(4D-1)^2},\quad d(q)=Q(a^2-b^2q).
\]
Unpaired singular zero modes, possible when the shore sizes differ, have eigenvalues \(ag_0\) or \(ag_1\), which are exactly the \(q=0\) roots. Because the graph is connected, its normalized adjacency has eigenvalues \(+1\) and \(-1\); thus \(q=1\) is always present. All other mode parameters satisfy \(q\in[0,1]\).

**3. Sharp endpoint and all-mode stability.** The real quadratic Schur criterion is \(1-d>0\), \(1+t+d>0\), \(1-t+d>0\). At \(q=1\), exact simplification gives
\[
 \begin{aligned}
 1+t+d(1)&=\frac{128D^2-64D+5}{4D-1},\\
 1-t+d(1)&=\frac{(8D-3)(16D-3)}{4D-1},\\
 1-d(1)&=-\frac{128D^2-76D+9}{4D-1}.
 \end{aligned}
\]
For \(3/8<D<1/2\), these are simultaneously positive precisely when \(D_-<D<D_+\), where \(D_-=(4+\sqrt6)/16\) and \(D_+=(19+\sqrt{73})/64\). Necessity follows already from the \(q=1\) mode.

For sufficiency note \(D_-<D<D_+\) implies \(2/5<D<7/16\). On this wider rational interval, \(|t|\le2/3\), \(|16D^2-9D+1|\le1/8\), \((4D-1)^2\ge9/25\), and \((1-2D)^2\le1/25\). Hence \(|d(0)|\le1/9\). All three strict Schur inequalities hold at \(q=0\), and have already been shown at \(q=1\). Since \(d(q)\) is affine in \(q\), each inequality holds throughout \([0,1]\). Every graph mode is strictly Schur stable. The local exponential-attraction conclusion follows from the finite-dimensional smooth fixed-point theorem.

## Verification

Run `python CHECK.py` in a directory containing the packaged checker. It verifies four symbolic identities exactly using SymPy and the fixed-point residual and eigenvalue stability classifications numerically on a seven-vertex path, six-vertex star, ten-cycle and \(K_{4,3}\), at four parameter choices on both sides of the boundary. Expected output: `BIPARTITE_LOGISTIC_EXACT_OK algebra=4 graph_cases=16`. The finite graph tests do **not** prove the universal quantifier; the block spectral argument does.

## Relationship to prior work

Rusakov, Tikhonov, Nurieva and Medvinsky's 2023 ring study uses the same self-plus-two-neighbors coupling for logistic oscillators and numerically explores regular and irregular spatial dynamics. Biswas and Das (2016), Section 3.4, write the fixed-state two-sublattice equations and determine numerical stability boundaries for an *inhomogeneous* logistic ring; those equations overlap substantially with the two-color part of this result. Atay and Karabacak (2006) identify bipartite-graph-independent stability regions for synchronized equilibria of delayed coupled maps, but their stated result concerns synchronized states and a different delay framework. The present theorem instead gives an exact interval for *heterogeneous stationary states*, including nonregular bipartite graphs with degree-normalized coupling. An indexed analysis of pinned anti-phase checkerboards on regular bipartite graphs treats temporally period-two branches under a different coupling model, and does not imply the stationary two-level theorem here.

## Limitations

The theorem assumes finite connected undirected bipartite graphs, identical local logistic maps at the maximally chaotic parameter, and normalized instantaneous dispersal with no extra forcing. It classifies the two-color branch and its full linear stability only. At the exact endpoints nonlinear center-manifold behavior is unresolved. Other stationary states, periodic attractors and basins are not classified. The earlier ring two-color Jacobian setup and general graph spectral principles are established background; priority of the exact graph-universal heterogeneous-stationary threshold beyond the inspected literature is not certified.

## References

1. A. V. Rusakov, D. A. Tikhonov, N. I. Nurieva and A. B. Medvinsky, *Emergent Spatial–Temporal Patterns in a Ring of Locally Coupled Population Oscillators*, Mathematics **11** (2023), 4970, https://doi.org/10.3390/math11244970. Earlier public preprint: https://www.preprints.org/manuscript/202310.0523/v1.
2. S. Biswas and A. Das, *Patterns, Bifurcations, Multistability and Hysteresis in an Inhomogeneous Coupled Map Lattice*, International Journal of Bifurcation and Chaos **26** (2016), 1630008, https://doi.org/10.1142/S0218127416300081.
3. F. M. Atay and Ö. Karabacak, *Stability of Coupled Map Networks with Delays*, SIAM Journal on Applied Dynamical Systems **5** (2006), https://doi.org/10.1137/060652531.
4. M. Golubitsky and I. Stewart, *Rigid patterns of synchrony for equilibria and periodic cycles in network dynamics*, Chaos **26** (2016), 094803, https://doi.org/10.1063/1.4953664.
