# Exact three-term covering-radius tail of the four-dimensional root-lattice quantizer

## Finding
Let \(X\) be uniformly distributed in the origin Voronoi cell of the four-dimensional root lattice \(D_4\) as defined below, with covering radius one. Its rare near-covering-radius events obey the explicit three-term expansion
\[
\mathbb P(\|X\|_2>1-\varepsilon)
 =24\varepsilon^4+48\varepsilon^5+\frac{772}{5}\varepsilon^6+O(\varepsilon^7),\qquad \varepsilon\downarrow0.
\]
In fact, an exact three-variable integral holds for all sufficiently small positive \(\varepsilon\) and gives a convergent power series with rational coefficients to any order. For independent uniform \(X_1,\ldots,X_N\),
\[
\lim_{N\to\infty}\mathbb P\big((24N)^{1/4}(1-\max_{1\le j\le N}\|X_j\|_2)>t\big)=e^{-t^4},\quad t\ge0.
\]
At the same covering radius, the four-dimensional cube has coefficient \(32/3\) instead of \(24\), hence the ratio of leading endpoint tails is \(9/4\). The latter comparison does **not** hold at equal covolume.

## Assumptions and scope
Define
\[
D_4=\{z\in\mathbb Z^4:\;z_1+z_2+z_3+z_4\in2\mathbb Z\},\quad
V=\{x:\ |x_i|+|x_j|\le1\ \text{for every }1\le i<j\le4\}.
\]
The root vectors \(\pm e_i\pm e_j\) supply these Voronoi inequalities; these are the full Voronoi inequalities for \(D_4\), a classical identification. The region \(V\) is a regular 24-cell with the 24 vertices
\[
\{\pm e_i:1\le i\le4\}\ \cup\ \{(\pm\tfrac12,\pm\tfrac12,\pm\tfrac12,\pm\tfrac12)\}.
\]
Its volume is \(2\), the index of \(D_4\) in \(\mathbb Z^4\), and each vertex has norm one. Uniformity refers to four-dimensional Lebesgue measure divided by \(2\). The statements are about the distribution of Euclidean distance to the nearest lattice point, not the second moment alone. All asymptotics refer to real positive \(\varepsilon\to0\).

## Proof
**1. Endpoint localization.** The squared Euclidean norm is strictly convex. Its maximum on the compact convex 24-cell equals one, and only vertices attain that value. Indeed, a nonvertex is a nontrivial convex combination of distinct vertices, each of norm one, so its norm is strictly smaller than one. It follows by compactness that, for small enough positive \(\varepsilon\), the set \(\{x\in V:\|x\|>1-\varepsilon\}\) is a disjoint union of 24 vertex neighborhoods. Signed coordinate permutations together with an orthogonal half-Hadamard symmetry act transitively on the 24 vertices, so all pieces have equal volume. These symmetries preserve \(V\).

**2. Exact cap geometry.** Consider the vertex \(v=e_1\). Close to it write \(x=(1-s,su_1,su_2,su_3)\), where \(s\ge0\) and \(u\in[-1,1]^3\). In a sufficiently small neighborhood this is exactly the part of \(V\) with \(x_1=1-s\): the three constraints \(|x_1|+|x_j|\le1\) give \(|u_j|\le1\), and the remaining pair constraints hold automatically when \(s<1/2\). Let \(U=\sum_{j=1}^3 u_j^2\). Then
\[
\|x\|^2=(1-s)^2+s^2U=1-2s+(1+U)s^2.
\]
For sufficiently small \(\varepsilon\), the cap intersects each such ray in precisely \(0\le s<t(\varepsilon,U)\), where the smaller quadratic root is
\[
t(\varepsilon,U)=\frac{2\varepsilon-\varepsilon^2}{1+\sqrt{1-(1+U)(2\varepsilon-\varepsilon^2)}}.
\]
The Jacobian is \(s^3\). Taking 24 equal caps and dividing by \(\operatorname{vol}(V)=2\) therefore gives the **exact** small-\(\varepsilon\) identity
\[
\mathbb P(\|X\|>1-\varepsilon)=\frac{24}{2}\int_{[-1,1]^3}\int_0^{t(\varepsilon,U)}s^3\,ds\,du
=3\int_{[-1,1]^3}t(\varepsilon,U)^4\,du.
\]

**3. Exact coefficients and all orders.** The smaller root solves
\[
s-\frac{1+U}{2}s^2=\varepsilon-\frac{\varepsilon^2}{2}.
\]
Uniformly for \(0\le U\le3\), its analytic expansion begins
\[
t=\varepsilon+\frac U2\varepsilon^2+\frac{U+U^2}{2}\varepsilon^3+O(\varepsilon^4).
\]
Consequently,
\[
t^4=\varepsilon^4\left(1+2U\varepsilon+\left(2U+\frac72 U^2\right)\varepsilon^2+O(\varepsilon^3)\right).
\]
For independent uniform \(u_j\in[-1,1]\), the exact moments are \(\mathbb E U=1\) and \(\mathbb E U^2=19/15\). Since the integration domain has volume \(8\), the three coefficients equal
\[
24,\qquad 24(2)=48,\qquad24\left(2+\frac72\frac{19}{15}\right)=\frac{772}{5}.
\]
Uniform analyticity on the compact parameter set proves the stated \(O(\varepsilon^7)\). Higher coefficients can be determined recursively: writing \(t=\sum_{k\ge1}c_k(U)\varepsilon^k\), one has \(c_1=1\) and, for \(k\ge2\),
\[
c_k(U)=\frac{1+U}{2}\sum_{j=1}^{k-1}c_j(U)c_{k-j}-\frac12\mathbf1_{k=2}.
\]
Thus each \(c_k\) is a rational polynomial in \(U\), and every integrated coefficient is rational by the explicit cube moments. This provides an effective all-order expansion.

**4. Independent-sample extreme tail.** With \(\delta=t/(24N)^{1/4}\), the preceding result yields \(N\mathbb P(\|X\|>1-\delta)\to t^4\). Independence gives the limit \((1-t^4/N+o(N^{-1}))^N\to e^{-t^4}\) for the maximum-deficit survival probability.

**5. Cubical comparison.** For the four-cube \(C=[-1/2,1/2]^4\), the circumradius is also one and the volume is one. Near any corner \(v=(\pm1/2)^4\), inward displacements \(y_i\ge0\) satisfy \(\|v-y\|^2=1-\sum_i y_i+\sum_i y_i^2\). The leading cap is the four-simplex \(\sum_i y_i<2\varepsilon\), whose volume is \((2\varepsilon)^4/4!=\frac23\varepsilon^4\); multiplying by 16 corners gives \(\frac{32}{3}\varepsilon^4+O(\varepsilon^5)\). The endpoint coefficient ratio is \(24/(32/3)=9/4\).

## Verification
The accompanying pure-standard-library script `verify_tail.py` checks the 24 exact candidate vertices and tangent-cube combinatorics, calculates the cube moments using rational arithmetic, and obtains \(24,48,772/5\) by two independent algebraic coefficient calculations. Deterministic quadrature checks are supplementary and are not used as a proof of the asymptotic formula. Run `python3 verify_tail.py` from the extraction directory.

## Relationship to prior work
Liu (2026) proves the global four-dimensional lattice *second-moment* optimum and describes the root Voronoi cell; that result establishes the importance of the \(D_4\) quantizer but does not imply the near-covering-radius radial probabilities. Conway and Sloane provide classical lattice Voronoi geometry and second moments. Hamprecht and Agrell (2003), §13.5.3 and Fig. 13.8, explicitly study and plot the **same radial distribution** for \(D_4\), a substantive antecedent that is credited. Their inspected section gives qualitative curves and covering/quantization interpretation but not the three exact endpoint coefficients, all-order recurrence or extreme-value normalization. Ordentlich (2025) develops spherical CDF bounds for lattice settings, particularly random ensembles, not this explicit deterministic root-cell endpoint expansion. Thus the originality claim is *only* the exact endpoint formula and its consequences, not introduction of the radial statistic or the \(D_4\) cell.

## Limitations
The displayed integral and power series are proved only for a sufficiently small, not explicitly optimized, neighborhood of the covering radius. They are not a closed formula for the full radial CDF. The cubic comparison holds at identical Euclidean covering radius but different cell volumes; it does not assert a globally superior distortion distribution at equal point density. Priority against all obscure tables or unpublished computations is not certified. No independent audit has been performed.

## References
- Tianle Liu, *Optimality of the D4 Lattice Quantizer*, arXiv:2611.00100, version first publicly posted 2026-10-26. https://arxiv.org/abs/2611.00100
- F. A. Hamprecht and E. Agrell, *Exploring a space of materials: Spatial sampling design and subset selection*, 2003, §13.5.3, Fig. 13.8. https://research.chalmers.se/publication/14989/file/14989_Fulltext.pdf
- J. H. Conway and N. J. A. Sloane, *Voronoi regions of lattices, second moments of polytopes, and quantization*, IEEE Trans. Inform. Theory 28 (1982). https://doi.org/10.1109/TIT.1982.1056483
- O. Ordentlich, *The Voronoi Spherical CDF for Lattices and Linear Codes: New Bounds for Quantization and Coding*, arXiv:2506.19791 (2025). https://arxiv.org/abs/2506.19791
