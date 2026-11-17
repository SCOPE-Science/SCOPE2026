# Eulerian sign law for centered geodesic-angle products on round spheres

## Finding

Let \(d\ge2\) be an integer, \(G=(V,E)\) a finite loopless simple graph, and let \((U_v)_{v\in V}\) be independent surface-uniform points on the unit sphere \(S^{d-1}\subset\mathbb R^d\). Write \(m=|E|\) and define the centered intrinsic geodesic length of an edge by
\[
H_{uv}=\arccos\langle U_u,U_v\rangle-\frac\pi2
       =-\arcsin\langle U_u,U_v\rangle.
\]
The joint centered graph moment is \(M_G(d)=\mathbb E\prod_{uv\in E}H_{uv}\); an empty product has value one.

**All-graph parity and strict-sign theorem.** If some vertex has odd degree, then \(M_G(d)=0\). If every vertex has even degree and \(m>0\), then
\[
(-1)^mM_G(d)>\mathbb E\prod_{uv\in E}\langle U_u,U_v\rangle
=\frac{Z_G(d)}{D_G(d)}>0.
\]
Here \(D_G(d)=\prod_{v\in V}\prod_{j=0}^{\deg(v)/2-1}(d+2j)\) and the **circuit-partition polynomial** \(Z_G(z)\) is the sum of \(z^{c(\pi)}\) over all pairings \(\pi\) of the incident edge ends at every vertex. Upon joining those pairings along the original edges, \(c(\pi)\) is the number of resulting closed circuits. Every coefficient of \(Z_G(z)\) is a nonnegative integer, and \(Z_G(d)>0\) when all degrees are even and \(m>0\).

More precisely, put \(a_k=\binom{2k}{k}/[4^k(2k+1)]\), for integers \(k\ge0\). For each \(\mathbf k=(k_e:e\in E)\), replace edge \(e\) by \(2k_e+1\) separately labelled parallel strands, obtaining an even-degree multigraph \(G_{\mathbf k}\). With the same definitions of \(D\) and \(Z\) for these labelled strands, one has the **absolutely convergent, termwise positive expansion**
\[
(-1)^m M_G(d)=\sum_{\mathbf k\in\mathbb N_0^E}
\left(\prod_{e\in E}a_{k_e}\right)
\frac{Z_{G_{\mathbf k}}(d)}{D_{G_{\mathbf k}}(d)}.
\]
The strict comparison is the contribution of the zero multiindex versus all positive additional terms.

Two explicit non-triangular examples are:
\[
Z_{K_{2,4}}(d)=3d^2+6d,\qquad
\mathbb E\prod_{e\in E(K_{2,4})}\!H_e
>\frac{3}{d^5(d+2)};
\]
\[
Z_{K_5}(d)=15d^3+96d^2+132d,\qquad
\mathbb E\prod_{e\in E(K_5)}\!H_e
>\frac{15d^3+96d^2+132d}{d^5(d+2)^5}.
\]
Both graphs have even degrees, and the first has no triangles. A useful corollary is that geodesic edge lengths indexed by a finite simple graph are jointly independent **if and only if** the graph is a forest, even though any two distinct edge lengths are independent.

## Assumptions and scope

The sphere has radius one and its distance is the shorter-arc intrinsic distance, including endpoints at distance \(\pi\), which occur with probability zero. Graphs are finite and loopless, with no repeated edges for the main theorem; auxiliary multigraphs have distinguishable strands. Isolated vertices are allowed. The probability is the product of normalized rotation-invariant surface measures. Dimension \(d\ge2\) is fixed but arbitrary. The sign theorem concerns a simultaneous product of once-centered **geodesic distances**, not a product of thresholded adjacency indicators, squared distances, or independent noise.

## Proof

**1. Antipodal selection rule.** The identity \(H(-x,y)=-H(x,y)\) holds for unit vectors, because the distance to an antipode is the complementary angle. Flipping one uniformly distributed \(U_v\) multiplies the integrand defining \(M_G(d)\) by \((-1)^{\deg(v)}\). If the degree is odd, invariance under that flip forces the expectation to vanish. This also covers degree-one vertices and disconnected graphs.

**2. Positive tensor monomials.** For any finite loopless multigraph \(F\), expand
\[
\prod_{e=uv\in E(F)}\langle U_u,U_v\rangle
=\sum_{\chi:E(F)\to\{1,\ldots,d\}}
  \prod_{v\in V(F)}\prod_{e\ni v}U_{v,\chi(e)}.
\]
Independence across vertices reduces each summand's expectation to products of coordinate moments of one uniform sphere point. Every odd coordinate exponent gives zero by coordinate-reflection symmetry. When all coordinate exponents are even, the expectation is strictly positive. Therefore every summand has nonnegative expectation. If all vertex degrees in \(F\) are even, the coloring assigning coordinate \(1\) to every edge contributes strictly positively. Consequently the dot-product expectation is strictly positive for every nonempty even-degree multigraph. This argument never assumes independence among edges sharing vertices.

**3. Exact pairing evaluation.** For \(X\) uniform on \(S^{d-1}\) and coordinate indices \(i_1,\ldots,i_{2r}\), the normalized sphere moment is
\[
\mathbb E\prod_{s=1}^{2r}X_{i_s}=
\frac{\displaystyle\sum_{\pi\in\mathcal P_2(2r)}
       \prod_{\{a,b\}\in\pi}\delta_{i_a,i_b}}
     {d(d+2)\cdots(d+2r-2)}.
\]
For \(r=0\), numerator and denominator are one. This follows by writing a standard Gaussian vector as the product of an independent radial factor and a uniform direction, applying the Gaussian pairing identity, and using \(\mathbb E\|N(0,I_d)\|^{2r}=d(d+2)\cdots(d+2r-2)\). Applying this formula at each graph vertex identifies the free coordinate-index loops precisely with circuits formed by pairing incident strands. Summing over their labels yields \(Z_F(d)/D_F(d)\), establishing the claimed finite graph polynomial formula.

**4. Passing from chords to angles.** The exact power series
\[
\arcsin t=\sum_{k=0}^{\infty}a_k t^{2k+1},
\quad a_k=\frac{\binom{2k}{k}}{4^k(2k+1)}>0,
\quad \sum_{k\ge0}a_k=\frac\pi2
\]
converges absolutely and uniformly on \([-1,1]\). Its finite product over the edges has absolutely integrable coefficient sum bounded by \((\pi/2)^m\), justifying termwise expectation. Each term corresponds to one even-degree parallel-strand multigraph, so Step 2 makes each expectation strictly positive whenever the original graph is nonempty and even-degree. The zero-index term equals the dot-product moment from Step 3. At least one nonzero multiindex exists and contributes strictly positively, which proves the strict inequality and the complete convergent series. When there is an odd-degree vertex, Step 1 already establishes the complementary zero case.

**5. Explicit graph polynomials.** In \(K_{2,4}\), the two degree-four vertices each have three possible local pairings and the other four vertices have unique pairings. Three of the nine choices create two circuits; six create one, giving \(3d^2+6d\) and denominator \(d^6(d+2)^2\). In \(K_5\), each of its five degree-four vertices has three pairings. Among the \(3^5=243\) choices, exactly \(132\), \(96\), and \(15\) give respectively one, two, and three circuits. Thus \(Z_{K_5}(d)=132d+96d^2+15d^3\), with denominator \([d(d+2)]^5\). Both counts are independently reproducible by the checker through a direct sum over coordinate colors.

**6. Forest independence corollary.** An edge of a finite forest incident to a leaf has a conditional length distribution independent of the position of its other endpoint, by rotation invariance. Integrating leaves successively proves joint independence of all forest edge lengths. Conversely, every graph with a cycle contains a simple cycle. On that cycle, the product of its centered edge lengths has nonzero expectation by the even-degree part of the theorem, whereas it would have expectation zero under mutual independence. Therefore no graph containing a cycle has mutually independent edge lengths. This corollary does not assert that distinct cycles are independent.

## Verification

The accompanying `verify_graph_moments.py` uses two independent **finite** computations of the chord-kernel numerator: local half-edge pairings glued into cycles, and direct coordinate-color enumeration with exact integer sphere moments. They agree for triangles, quadrilaterals, two triangles sharing a vertex, and \(K_5\), in dimensions two and three. In particular the two methods confirm the \(K_5\) coefficients \((132,96,15)\) and the double-triangle coefficients \((2,1)\). A separate direct pairing enumeration confirms \(K_{2,4}\) coefficients \((6,3)\).

For a simple cycle of length \(r\), the spherical harmonic decomposition in dimension three independently gives
\[
M_{C_r}(3)=(-1)^r\sum_{k=0}^{\infty}(4k+3)
\left[\frac{\pi}{8(k+1)^2}
\left(\frac{\binom{2k}{k}}{4^k}\right)^2\right]^r.
\]
The checker bounds the truncated series' tail and compares the three- and four-cycle moments with independent numerical sampling on the sphere. Finite sampling is a diagnostic, not an infinite proof. No external proof assistant or independent audit is claimed.

## Relationship to prior work

Finch and Jones, *Random Spherical Triangles* (first posted September 27, 2010), study the joint side-length geometry and perimeter of three independent uniform sphere points; this includes the important older three-edge context. The general three-variable side-length density had already been discussed in earlier spherical random-set literature. Musin, *Multivariate positive definite functions on spheres* (posted January 3, 2007), builds on Schoenberg's characterization of positive definite spherical kernels, which helps contextualize the positive coefficients used here. Berg and Porcu (posted May 21, 2015) develop broader positive-definite function theory for spheres and groups. Bubeck, Ding, Eldan and Rácz (posted November 20, 2014) investigate signed triangle statistics in thresholded geometric random graphs. These contributions and the classical sphere-moment pairing formula are acknowledged inputs or related viewpoints, not claimed as discoveries here.

The specific scope assessed here is the **arbitrary-graph degree-parity classification for products of centered continuous geodesic lengths, its strictly positive chord comparison, and the circuit-partition expansion**, including even-degree triangle-free graphs and \(K_5\). This is not a novel proof of spherical kernel positive definiteness, the three-edge perimeter skewness result, or the fact that tree-edge lengths are independent.

## Limitations

The strict-sign theorem concerns the complete product of once-centered edge lengths; it does not determine their entire joint distribution or the sign of arbitrary mixed nonlinear observables. The combinatorial series is exact and absolutely convergent but can be computationally large for graphs of high degree. The comparison with primary literature establishes no worldwide novelty guarantee: a general prior tensor-network or graphon moment theorem could imply the result despite different terminology. The original 1971 spherical random-set treatment was not completely inspected, and its three-point density remains relevant to historical priority of the triangle subcase. The present analysis does not claim independent mathematical or historical validation.

## References

1. O. R. Musin, *Multivariate positive definite functions on spheres*, arXiv:math/0701083, initial submission January 3, 2007, https://arxiv.org/abs/math/0701083.
2. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329, initial submission September 27, 2010, https://arxiv.org/abs/1009.5329.
3. S. Bubeck, J. Ding, R. Eldan and M. Z. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713, initial submission November 20, 2014, https://arxiv.org/abs/1411.5713.
4. C. Berg and E. Porcu, *From Schoenberg coefficients to Schoenberg functions*, arXiv:1505.05682, initial submission May 21, 2015, https://arxiv.org/abs/1505.05682.
5. I. J. Schoenberg, *Positive definite functions on spheres*, Duke Mathematical Journal 9 (1942), 96–108, DOI: 10.1215/S0012-7094-42-00908-6; year-only historical background, not used as a first-posting date.
