# The marked antipodal four-cycle law and the first geometric correction to random spherical diameters

## Finding
Let \(n\geq4\) be fixed and let \(X_1,\ldots,X_n\) be independent area-uniform points on the unit sphere \(S^2\subset\mathbb R^3\). Put \(D_n=\max_{i<j}|X_i-X_j|\) and \(p_\delta=(1-\cos\delta)/2\). As \(\delta\downarrow0\),
\[
\boxed{\begin{aligned}
\Pr\{D_n>2\cos(\delta/2)\}
={}&m p_\delta-\binom m2p_\delta^2\\
&+\left[\binom m3-\binom n3-3\binom n4\left(1-\frac{16}{3\pi^2}\right)\right]p_\delta^3
+o_n(p_\delta^3),\\
m={}&\binom n2.
\end{aligned}}
\]
The cubic coefficient includes two distinct geometric corrections to treating all pair events as independent: impossibility of three-edge odd cycles, and a four-edge dependence with constant \(1-16/(3\pi^2)\). Every collection of selected edges forming a forest remains independent. For four sampled points it gives the cubic coefficient \(13+16/\pi^2\).

There is also an explicit **marked configuration limit**. Condition four independent sphere points \(A,B,C,D\) on all four near-antipodal relations \(d_S(A,C),d_S(A,D),d_S(B,C),d_S(B,D)>\pi-\delta\). Rotate the configuration so that \(A=(0,0,1)\), write \(B=(b_1,b_2,b_3)\), \(C=(c_1,c_2,c_3)\), \(D=(d_1,d_2,d_3)\), and define
\[x=(b_1,b_2)/\delta,\qquad y=-(c_1,c_2)/\delta,\qquad z=-(d_1,d_2)/\delta.\]
Then the conditional law of \((x,y,z)\) converges in total variation to the uniform law on the bounded open subset of \(\mathbb R^6\)
\[
\mathcal R=\{(x,y,z): |y|<1,\ |z|<1,\ |y-x|<1,\ |z-x|<1\},
\]
whose six-dimensional volume is exactly \(\pi^3-16\pi/3\). This limit describes the geometry underlying the cubic correction, not merely its frequency.

## Assumptions and scope
All sphere samples are independent with normalized surface measure. Geodesic distances \(d_S\) are measured in radians, and Euclidean lengths in the ambient \(\mathbb R^3\). The sample size \(n\) is any fixed integer at least four; no uniformity in growing \(n\) is asserted. The threshold parameter obeys \(0<\delta\ll1\). The strict versus nonstrict conventions make no difference because the relevant distributions have no threshold atoms. The four-point marked result is conditional on the four specific cross-edge relations between two labelled vertex pairs; it is not a law for four randomly selected graph edges without this conditioning.

## Proof
**1. One-edge probability and forest independence.** Define \(E_{ij}=\{d_S(X_i,X_j)>\pi-\delta\}\). A spherical cap of angular radius \(\delta\) has normalized area \(p_\delta=(1-\cos\delta)/2\), so \(\Pr(E_{ij})=p_\delta\). For every finite forest of such edges, all corresponding events are jointly independent: integrate out any leaf vertex, whose probability of satisfying the single incident condition is \(p_\delta\), regardless of the positions of the other vertices. Iteration proves a forest probability of \(p_\delta^{e}\) for \(e\) edges. A triangle of near-antipodal relations is impossible when \(3\delta<\pi\), by applying the spherical triangle inequality after antipodal reversal. More generally, any odd cycle of \(k\) edges is impossible for \(k\delta<\pi\). All bounds and combinatorial classifications below are for sufficiently small \(\delta\), with \(n\) fixed.

**2. The four-cycle probability.** Let \(q_\delta=\Pr(E_{AC}\cap E_{AD}\cap E_{BC}\cap E_{BD})\). Rotation invariance fixes \(A\) at the north pole. The other point on its side of the bipartition, \(B\), must lie within angular radius \(2\delta\) of \(A\), and \(C,D\) must both lie in the intersection of spherical caps of angular radius \(\delta\) around \(-A\) and \(-B\). With the scaled coordinates in the finding, geodesic constraints converge to the four Euclidean inequalities defining \(\mathcal R\). Normalized surface measure in each of the three local coordinate charts has Jacobian \(\delta^2(1+o(1))/(4\pi)\), uniformly on the bounded relevant coordinate region. Thus
\[
q_\delta=\frac{\delta^6}{(4\pi)^3}\operatorname{Vol}_6(\mathcal R)+o(\delta^6).
\]
The same bounded-coordinate change of variables makes the unnormalized conditional densities converge pointwise almost everywhere to a constant times \(\mathbf1_{\mathcal R}\). Uniform boundedness and compact support give convergence in \(L^1\); after dividing by \(q_\delta\), this proves the claimed total-variation convergence.

**3. Exact lens integral.** At a fixed \(x\in\mathbb R^2\), the two admissible \(y\) and \(z\) each lie in the overlap of unit planar disks centered at \(0\) and \(x\). For \(0\le r\le2\), its area is
\[a(r)=2\arccos(r/2)-(r/2)\sqrt{4-r^2}.\]
Fubini and radial integration yield
\[
\begin{aligned}
\operatorname{Vol}_6(\mathcal R)&=2\pi\int_0^2 r\,a(r)^2\,dr\\
&=2\pi\int_0^\pi\sin u\,(u-\sin u)^2\,du\\
&=\pi^3-\frac{16\pi}{3}.
\end{aligned}
\]
The final equality uses \(\int_0^\pi u^2\sin u\,du=\pi^2-4\), \(\int_0^\pi u\sin^2u\,du=\pi^2/4\), and \(\int_0^\pi\sin^3u\,du=4/3\). Since \(p_\delta\sim\delta^2/4\), we obtain
\[q_\delta=\left(1-\frac{16}{3\pi^2}\right)p_\delta^3+o(p_\delta^3).\]

**4. Exhaustion of all edge-event intersections through cubic order.** Inclusion–exclusion for the union of the \(m=\binom n2\) events \(E_{ij}\) has one-edge and two-edge sums \(m p_\delta\) and \(\binom m2p_\delta^2\). Among three distinct selected edges, exactly \(\binom n3\) choices are triangles and hence impossible for small \(\delta\); all remaining \(\binom m3-\binom n3\) choices are forests and contribute \(p_\delta^3\). Among four-edge selections, a bipartite graph with a cycle and at most four edges must be a single four-cycle; the complete labelled graph on four chosen vertices has exactly three such cycles, hence \(3\binom n4\) choices. These contribute \(q_\delta\) and occur with the minus sign in inclusion–exclusion.

It remains to bound other intersections. For any fixed graph of selected near-antipodal edges, choose a spanning forest of its nonisolated components. Assigning the root of each component arbitrarily, every successive vertex is constrained to a cap of normalized area \(p_\delta\) around the antipode of its forest parent, hence the probability of the full intersection is at most \(p_\delta^{v-c}\), where \(v\) is the number of nonisolated vertices and \(c\) their number of components. A graph with at least four edges and rank \(v-c\le3\) can only be a forest with at most three edges or a four-cycle (extra edges would create an odd cycle or raise the rank). Thus all remaining selections of four or more edges contribute \(O_n(p_\delta^4)\). Inserting the evaluated four-cycle term proves the expansion.

## Verification
The standalone `check_antipodal_cycle.py` uses `numpy` and `scipy` as listed in `requirements.txt`. It numerically integrates the planar lens square to verify the exact constant \(1-16/(3\pi^2)\), simulates four-point incidences conditionally on a near-antipodal cluster at three shrinking angular thresholds (800,000 configurations each), and checks the finite-sample diameter expansion against independent uniform-sphere samples (700,000 configurations for each of three distinct sample-size/threshold pairs). It prints `ANTIPODAL_CYCLE_SMALL_CAP_DIAGNOSTIC_OK` on successful execution. The numerical tests are corroboration only; the infinite limiting and inclusion–exclusion arguments above provide the proof.

## Relationship to prior work
Mayer and Molchanov's 2006 analysis treats sample diameters and derives the large-sample extreme-value law for uniform boundary points of balls. Its object is the same maximum interpoint distance, but it does not evaluate the present fixed-sample cubic term or the four-point marked law. Existing spherical-cap graph work, including Bubeck–Ding–Eldan–Rácz (2014) and Bangachev–Bresler (2024), studies dependences between edge indicators and signed cycle statistics; the basic fact that cycles can create dependence is not claimed as new. A published spectral treatment of even spherical-cap cycles also supplies an exact spectral trace for the unmarked four-cycle probability, but does not state the small-cap planar-lens evaluation or the conditional six-dimensional configuration limit. The contribution is the explicit singular small-cap limit, its marked geometry, and the resulting fixed-sample diameter expansion.

## Limitations
The expansion assumes fixed \(n\) and \(\delta\to0\); it is not uniform in growing sample size. The conditional limit treats the particular four labelled cross edges and does not classify every connected component of the rare-event graph. It is a result about uniform sampling on \(S^2\), not arbitrary smooth surfaces or other dimensions. The existence of a general spectral representation for the unmarked four-cycle event raises a residual priority risk for the evaluated coefficient; a comprehensive independent historical audit has not been performed. No numerical experiment replaces the analytic argument.

## References
- M. Mayer and I. Molchanov, *A limit theorem for the maximal interpoint distance of a random sample in the unit ball*, arXiv:math/0605289, first publicly submitted 2006-05-11. https://arxiv.org/abs/math/0605289
- S. Bubeck, J. Ding, R. Eldan and M. Z. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713 (2014). https://arxiv.org/abs/1411.5713
- K. Bangachev and G. Bresler, *On the Fourier Coefficients of High-Dimensional Random Geometric Graphs*, arXiv:2402.12589 (2024); supporting comparison only. https://arxiv.org/abs/2402.12589
