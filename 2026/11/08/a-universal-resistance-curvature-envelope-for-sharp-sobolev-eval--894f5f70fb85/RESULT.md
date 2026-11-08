# A universal resistance-curvature envelope for sharp Sobolev evaluation on metric graphs

## Finding

For **every** finite connected loopless multigraph realized as a metric graph with arbitrary positive real edge lengths, the optimal squared norm of real mean-zero first-order Sobolev evaluation is the largest element of an explicitly computable **finite quadratic envelope**. The envelope depends only on vertex-to-vertex effective resistances, edge lengths, and total arclength. Its edge curvatures satisfy an exact topological conservation law that locates the possibilities for interior norming points.

Put \(T=\sum_{e\in E}\ell_e\), \(r_{ab}=R_G(a,b)\) for vertex effective resistance with edge conductance \(\ell_e^{-1}\), and for each vertex \(v\) define
\[
F_v=\sum_{e=(a,b)}\left[\frac{\ell_e}{2}(r_{va}+r_{vb})+\frac{\ell_e}{6}(\ell_e-r_{ab})\right].
\]
Define the global resistance integral and the vertex squared-evaluation constants by
\[
J=\sum_{e=(a,b)}\ell_e\left[\frac{F_a+F_b}{2}+\frac{T(\ell_e-r_{ab})-\ell_e^2}{6}\right],
\qquad Q_v=\frac{F_v}{T}-\frac{J}{2T^2}.
\]
For every oriented edge \(e=(a,b)\), set \(c_e=\ell_e-r_{ab}-\ell_e^2/T\) and parametrize it by \(x_e(t)\), \(0\le t\le1\). The exact squared evaluation norm at every point is
\[
\boxed{Q(x_e(t))=(1-t)Q_a+tQ_b+c_e t(1-t).}
\]
Thus the sharp squared Sobolev embedding constant is the largest among the finitely many vertex values \(Q_v\) and the edge values
\[
Q_e(t_e^*),\qquad t_e^*=\frac12+\frac{Q_b-Q_a}{2c_e},
\]
for **exactly those** edges with \(c_e>0\) and \(0<t_e^*<1\). A vertex is norming precisely if its value equals this maximum; an interior point is norming precisely when it is such a maximizing stationary point, or lies on a flat edge \(c_e=0\), \(Q_a=Q_b\) whose common value is the maximum. On any norming point \(x\), the real norm-attaining nonzero functions are exactly the nonzero scalar multiples of the centered Green representer \(g_x\).

The curvatures satisfy the **topology identity**
\[
\boxed{\sum_{e\in E}\frac{c_e}{\ell_e}=\beta_1(G)-1},\qquad
\beta_1(G)=|E|-|V|+1.
\]
Every bridge has \(c_e=-\ell_e^2/T<0\); if \(\beta_1(G)\ge2\), at least one edge has positive curvature. These conclusions do not assert that a positive-curvature edge necessarily contains a *global* maximizing point.

## Assumptions and scope

A finite connected metric graph is formed from \(|V|\ge2\) vertices and finitely many edges of positive lengths. Parallel edges are allowed; self-loops are omitted, as every geometric loop can be subdivided by inserting a degree-two vertex without changing the graph or the theorem. Use ordinary unweighted edge arclength \(ds\), and no atoms at vertices. The real Hilbert space is
\[
\mathcal H=\{f\in C(G):f|_e\in H^1(e),\ \int_G f\,ds=0\},\qquad
\|f\|_{\mathcal H}^2=\int_G|f'|^2ds.
\]
The target norm is the pointwise supremum norm on \(C(G)\). The sharp squared constant \(K(G)\) is characterized by \(\|f\|_\infty^2\le K(G)\|f\|_{\mathcal H}^2\) for every \(f\in\mathcal H\). This is a real-valued, first-derivative-energy theorem, not an assertion about arbitrary weighted measures or different Laplacians.

## Proof

**1. Resistance as squared energy distance.** Work in the Hilbert energy quotient of continuous edgewise-\(H^1\) functions by constants. The norm of the difference evaluation \(f\mapsto f(x)-f(y)\) squared equals the effective resistance \(R(x,y)\). This follows from the Dirichlet variational principle: the minimum energy of a unit voltage difference is the network conductance. Let \(\eta_x\) be the corresponding evaluation vector after centering by the arclength probability \(ds/T\). Its squared norm equals the sharp squared point-evaluation constant \(Q(x)\).

**2. Centered distance identity.** Set \(F(x)=\int_G R(x,y)\,dy\), \(J=\int_G F(x)\,dx\). Since \(R(x,y)=\|\eta_x-\eta_y\|^2\) and \(\int_G\eta_y\,dy=0\), integrating once and twice gives exactly
\[
Q(x)=F(x)/T-J/(2T^2).
\]
Polarization gives a particularly convenient explicit representer:
\[
g_x(y)=\frac{F(x)+F(y)}{2T}-\frac{J}{2T^2}-\frac{R(x,y)}2.
\]
It has zero integral in \(y\) and satisfies \(f(x)=\int_G f'(y)g_x'(y)\,dy\) for all \(f\in\mathcal H\).

**3. Edge interpolation, including the same-edge correction.** On an edge \(e=(a,b)\) of length \(\ell\), an evaluation at fraction \(t\) decomposes orthogonally into the linear interpolation of endpoint evaluations and an independent Dirichlet-bridge evaluation. The bridge covariance is \(\ell(\min(s,t)-st)\) for fractions \(s,t\in[0,1]\). Consequently, for \(y\) outside the open edge,
\[
R(x_e(t),y)=(1-t)R(a,y)+tR(b,y)+(\ell-r_{ab})t(1-t).
\]
For \(y=x_e(s)\) on the same edge, subtract \(2\ell(\min(s,t)-st)\). Integrating this correction across the edge yields exactly \(-\ell^2t(1-t)\). Therefore
\[
F(x_e(t))=(1-t)F_a+tF_b+[T(\ell-r_{ab})-\ell^2]t(1-t).
\]
Integrating this identity over each edge with \(t\in[0,1]\) establishes the displayed formulas for \(F_v\) and \(J\). Indeed \(F_v\) follows by integrating the outside-edge formula with \(x=v\), and the \(J\) formula then follows from integrating \(F(x_e(t))\). Division by \(T\) establishes the quadratic profile for \(Q\).

**4. Finite optimization, exhaustive equality cases.** For \(c_e>0\), the quadratic \(Q_e\) is strictly concave and its unique stationary point is \(t_e^*\); if it lies inside the edge it is the unique maximum on that edge. For \(c_e<0\), the quadratic is strictly convex and its edge maximum lies at endpoints. For \(c_e=0\), it is affine and has interior maximizers only when constant with its value equal to the global maximum. This enumerates every possibility without an infinite search. The Riesz representation theorem and equality in Cauchy–Schwarz establish the stated scalar-multiple characterization of norm-attaining functions.

**5. Conservation of curvature.** Foster's identity for a finite connected conductance network gives \(\sum_{e=(a,b)}r_{ab}/\ell_e=|V|-1\). Thus
\[
\sum_e c_e/\ell_e=|E|-(|V|-1)-\sum_e\ell_e/T=|E|-|V|=\beta_1(G)-1.
\]
On a bridge, \(r_{ab}=\ell_e\), giving strictly negative curvature. If the graph has at least two independent cycles, the curvature sum is positive and at least one summand is positive.

## Verification

A standalone standard-library Python program (`verify.py`) independently recomputes the edgewise evaluation constants from exact rational Kirchhoff–Poisson equations. It inserts a vertex at each sampled interior position, solves the grounded vertex Laplacian for a unit point source minus uniform arclength, restores the quadratic within-edge solution, and subtracts its exact arclength mean. This route does **not** evaluate the resistance interpolation formulas to compute the expected evaluation value. Ten networks (including trees, weighted cycles, cactus networks, complete and bipartite networks, a non-cactus diamond, and parallel edges) and six exact fractional positions per edge give \(294\) exact matches. All ten curvature sums and global-envelope dominance tests also agree. Run `python3 verify.py`; no nonstandard packages are required. The tests are finite corroboration, not the proof of the universal statement.

## Relationship to prior work

Solomyak (2002) develops metric-graph Sobolev embeddings and sharp approximation-number bounds, but the inspected approximation theorems do not supply this graph-specific point-evaluation envelope. Baker–Faber (2004) develop the essential effective-resistance quadratic laws and Foster's identity; those fundamental ingredients are explicitly used rather than claimed as new. Baker–Rumely (2004) give the general centered Green kernel and spectral analysis, including interval and circle examples. Their inspected statements do not explicitly optimize the arclength-centered Green diagonal over every edge or state the resulting curvature conservation and complete finite equality classification. The contribution here is the finite arbitrary-topology optimization and its positive/flat/negative edge classification, not the underlying electrical resistance or Green theory. The result includes specialized tree, cactus, complete multipartite, and vertex-transitive graph evaluations as cases but they do not imply the arbitrary-topology formula.

## Limitations

The theorem is specific to finite connected graphs, strictly positive lengths, real functions, standard Kirchhoff continuity and edgewise derivative energy, and uniform arclength mean. It neither evaluates unrelated spectral invariants nor supplies simplified graph-family closed forms. The finite envelope requires effective-resistance calculations on the input graph; it can be computationally large, but is finite. Literature priority remains qualified: a general older Green-kernel identity could be combined with elementary optimization to recover the envelope even when this exact packaging is not indexed; a complete priority claim is not established.

## References

1. M. Solomyak, *On approximation of functions from Sobolev spaces on metric graphs*, arXiv:math/0206235, first public version 23 June 2002. https://arxiv.org/abs/math/0206235
2. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first public version 25 July 2004, particularly the resistance quadratic and Foster sections. https://arxiv.org/abs/math/0407428
3. M. Baker and R. Rumely, *Harmonic analysis on metrized graphs*, arXiv:math/0407427, first public version 25 July 2004, particularly Sections 1, 7 and 14 on Green kernels. https://arxiv.org/abs/math/0407427
