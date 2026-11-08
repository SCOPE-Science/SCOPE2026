# Voronoi-convolution homotopy law for random shortest-geodesic polygons on flat tori

## Finding
Let \(L\subset\mathbb R^d\) be any full-rank lattice, with \(d\ge1\), covolume \(v\), and closed Dirichlet–Voronoi cell \(V\) at the origin. Set \(f=v^{-1}\mathbf 1_V\) and \(\Sigma=v^{-1}\int_V zz^{\mathsf T}\,dz\). Choose \(m\ge3\) independent normalized-volume-uniform points on \(\mathbb R^d/L\), join successive points by their intrinsic shortest geodesics, and close the polygon. Almost surely every edge is unique. Let \(W_m\in L\) be the oriented deck translation obtained by lifting the complete loop.

**Complete homotopy distribution and exact covariance.** For every \(\lambda\in L\),
\[
\Pr(W_m=\lambda)=v\,f^{*m}(\lambda),\qquad
\mathbb E W_m=0,\qquad
\mathbb E[W_mW_m^{\mathsf T}]=m\Sigma.
\]
For each fixed lattice and dimension, uniformly over \(\lambda\in L\) as \(m\to\infty\),
\[
\Pr(W_m=\lambda)=\frac{v}{(2\pi m)^{d/2}\sqrt{\det\Sigma}}
\exp\!\left(-\frac{\lambda^{\mathsf T}\Sigma^{-1}\lambda}{2m}\right)
+O_L(m^{-d/2-1}).
\]
In particular the contractibility probability is \(v/((2\pi m)^{d/2}\sqrt{\det\Sigma})(1+O_L(m^{-1}))\).

**Exact combinatorics for orthogonal products.** If \(L\) has an orthogonal basis, let \(A(n,s)\) and \(B(n,s)\) respectively denote ordinary type-A and signed type-B Eulerian numbers, counting permutations with exactly \(s\) descents; values outside their usual index ranges are zero. In the coordinate basis of \(L\), the coordinates of \(W_m\) are independent, identically distributed integer variables with
\[
\Pr(W_{m,1}=k)=
\begin{cases}
A(m-1,r+k-1)/(m-1)!,&m=2r,\\
B(m-1,r+k)/(2^{m-1}(m-1)!),&m=2r+1.
\end{cases}
\]
This law is independent of the positive side lengths. In dimension two, the exact null-homotopy probabilities for \(m=3,4,5\) are respectively \(9/16\), \(4/9\), and \((115/192)^2\).

**Shape information survives for nonorthogonal tori.** On a square flat two-torus,
\[
\Pr(W_m=0)=\frac6{\pi m}(1+O(m^{-1})),
\]
whereas on the regular hexagonal flat two-torus,
\[
\Pr(W_m=0)=\frac{18\sqrt3}{5\pi m}(1+O(m^{-1})).
\]
The hexagonal/square ratio therefore tends to \(3\sqrt3/5>1\). No extremal claim over all lattices is made. The three-vertex null-homotopy values \(9/16\) and \(7/12\) on rectangular and hexagonal two-tori, respectively, are previously known; the proposed contribution here is the all-length homotopy-vector convolution and covariance law, including lengths \(m\ge4\), and its lattice-shape-dependent local limit.

## Assumptions and scope
The torus is the smooth, compact, intrinsically flat Riemannian manifold \(\mathbb R^d/L\); sampled vertices are independent with Haar probability. The cell \(V\) is a centrally symmetric convex fundamental polytope with boundary measure zero, and its covariance \(\Sigma\) is strictly positive definite. The deck vector \(W_m\) is measured in the Euclidean universal cover; when coordinates are used, they refer to a chosen lattice basis. A loop with zero deck vector is null-homotopic. Distinct sample points and avoidance of geodesic ties hold almost surely. The covariance identity requires \(m\ge3\): for two vertices the two opposite shortest segments retrace one another, so the deck vector vanishes.

## Proof
**1. Independence of lifted increments.** Fix a lift of the initial vertex. For the first \(m-1\) edges, choose the unique shortest displacement \(Z_j\in V\). The map from the \(m\) independent Haar vertices to the first vertex and the \(m-1\) successive torus differences preserves product Haar measure. Since \(V\) is a fundamental domain, the \(Z_j\) are independent and each uniform on \(V\). Put \(S=\sum_{j=1}^{m-1}Z_j\) and let \(R\in V\) be the unique representative of \(S\pmod L\), ignoring its null boundary exceptional set. The closing shortest edge has displacement \(-R\). Therefore \(W_m=S-R\in L\).

**2. Exact distribution.** For \(\lambda\in L\), the event \(W_m=\lambda\) is \(S\in\lambda+V\). As \(V=-V\), convolution with a further independent uniform cell variable gives
\[
\int_{\lambda+V}f^{*(m-1)}(s)\,ds
=v\int f^{*(m-1)}(s)f(\lambda-s)\,ds
=v f^{*m}(\lambda).
\]
The translates of \(V\) tile the cover, so these masses sum to one.

**3. Exact covariance.** The representative \(R\) is uniform on \(V\). Because \(m-1\ge2\), fixing any one increment \(Z_j\) leaves at least one independent Haar-uniform increment in the sum modulo \(L\). Thus \(R\) is independent of \(Z_j\), and \(\mathbb E[SR^{\mathsf T}]=0\). Central symmetry gives zero means, so
\[
\mathbb E[(S-R)(S-R)^{\mathsf T}]=(m-1)\Sigma+\Sigma=m\Sigma.
\]
This is an identity, not an asymptotic assertion.

**4. Uniform local limit.** Let \(\phi(\xi)=\int e^{i\xi\cdot z}f(z)\,dz\). By symmetry, \(\phi(\xi)=1-\tfrac12\xi^{\mathsf T}\Sigma\xi+O_L(|\xi|^4)\) near zero. Since \(f\in L^1\cap L^2\) has full-dimensional support, \(\phi\in L^2\), it tends to zero at infinity, and \(|\phi(\xi)|<1\) for every nonzero \(\xi\). Fourier inversion for \(f^{*m}\), splitting a small neighborhood of zero from its complement, gives an exponentially small outer contribution bounded by \(q^{m-2}\|\phi\|_2^2\). On the small neighborhood substitute \(\xi=u/\sqrt m\): the Gaussian kernel has an integrable \(O_L(m^{-1}|u|^4)e^{-c|u|^2}\) error. Taking absolute values before the Fourier phase makes the error uniform in \(\lambda\). The Gaussian transform yields the displayed \(O_L(m^{-d/2-1})\) local limit.

**5. Orthogonal products and Eulerian laws.** For a product of circles, the cell is a box and coordinates separate. Each coordinate density is the convolution of \(m\) independent centered unit interval uniforms, evaluated at integer \(k\). The cardinal-spline inclusion–exclusion formula is
\[
 b_m(k)=\frac1{(m-1)!}\sum_{j=0}^m(-1)^j\binom mj
 \left(k+\frac m2-j\right)_+^{m-1}.
\]
For even \(m\) this is the standard type-A Eulerian inclusion–exclusion formula, and for odd \(m\) multiplying the numerator by \(2^{m-1}\) gives the standard type-B formula. Coordinate scaling cancels exactly. Evaluating at \(m=3,4,5\) gives \(3/4,2/3,115/192\) in one dimension, and squaring yields the planar examples.

**6. Square versus regular hexagon.** In a square Voronoi cell of side \(a\), \(v=a^2\) and \(\Sigma=(a^2/12)I_2\). For a regular hexagonal cell of inradius \(\rho\), polar integration over six sectors with angular limits \(-\pi/6\) to \(\pi/6\) gives \(v=2\sqrt3\rho^2\), \(\mathbb E|Z|^2=5\rho^2/9\), and hence \(\Sigma=(5\rho^2/18)I_2\). Substitution into the local limit at \(\lambda=0\) yields the two constants and their strict ratio.

## Verification
The accompanying `verify_voronoi.py` performs exact rational checks of the type-A/type-B inclusion–exclusion formulas, normalization, and \(\mathbb E W_{m,1}^2=m/12\) for integer \(3\le m\le13\), and checks the explicit \(m=3,4,5\) probabilities. Independently, it samples Haar-uniform torus vertices, chooses each shortest edge by enumerating nearby lattice translates, and compares empirical winding covariances and null-class probabilities on square and hexagonal tori for \(690{,}000\) simulated polygons in total. Results agree within stated sampling tolerances. The finite experiments corroborate, rather than establish, the analytic theorem.

## Relationship to prior work
Glorieux and Yarmola (2020) already compute the null-homotopy probability for a random shortest-geodesic **triangle** on an arbitrary flat two-torus: in particular \(9/16\) for rectangular and \(7/12\) for hexagonal tori. Their Dirichlet-domain triple-overlap formula is consistent with the \(m=3\) specialization here; neither the triangular probability nor its known extrema are claimed as original. Wang, Xu, and Xu (2008) supply the classical spline–Eulerian relationship, and Wang and Xu (2010) establish spline Gaussian asymptotics. Those are acknowledged inputs to the orthogonal calculation, not newly proved combinatorial identities. Cantarella, Deguchi, and Shonkwiler (2012) study a different Haar-induced measure on fixed-length Euclidean closed polygons, not independent vertices joined by shortest geodesics on a torus. The new scope asserted is the full lattice-valued \(m\ge4\) homotopy law, its exact covariance and nonorthogonal shape-dependent local limit. Priority is not independently certified.

## Limitations
The theorem assumes a flat torus quotient by a full-rank lattice, Haar-independent vertices, and almost-sure shortest geodesics. It does not apply without further analysis to variable-curvature surfaces, nonuniform vertex laws, minimizing geodesics chosen at positive-probability ties, or arbitrary homology groups. The asymptotic is for fixed lattice and fixed dimension as vertex count grows; the implicit constants are not uniform over degenerating lattices. A leading null-probability constant determines only \(v/\sqrt{\det\Sigma}\), not the complete lattice. The result makes no claim that regular hexagonal lattices extremize the probability for every vertex count. A self-review and computational checks are not independent auditing, and an undiscovered equivalent in specialized geometric probability literature remains possible.

## References
1. O. Glorieux and A. Yarmola, *Random triangles on flat tori*, arXiv:2003.08190, first posted 2020-03-18, Proposition 2.2 and Theorem 1.1; subsequent journal version, Rocky Mountain Journal of Mathematics 52 (2022), 1345–1354.
2. R. Wang, Y. Xu, and Z. Xu, *A spline interpretation of Eulerian numbers*, arXiv:0808.2349, first posted 2008-08-18, equations (1.6) and Theorem 1.1.
3. R. Wang and Y. Xu, *The asymptotic properties of Eulerian numbers and refined Eulerian numbers: A spline perspective*, arXiv:1002.0056, first posted 2010-01-30, Theorems 3.1–3.3.
4. J. Cantarella, T. Deguchi, and C. Shonkwiler, *Probability Theory of Random Polygons from the Quaternionic Viewpoint*, arXiv:1206.3161, first posted 2012-06-14, Sections I–III.
