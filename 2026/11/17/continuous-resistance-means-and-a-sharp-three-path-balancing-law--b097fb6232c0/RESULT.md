# Continuous resistance means and a sharp three-path balancing law

## Finding
Let \(G_m(\ell_1,\ldots,\ell_m)\) be the compact metric graph obtained by joining the two endpoints of each of \(m\ge2\) distinct intervals at common vertices \(A,B\). All edge lengths \(\ell_i\) are positive, and each unit of arclength has unit electrical resistance. Choose \(X,Y\) independently from normalized arclength on the entire graph, **not** uniformly among edge labels. Denote their effective electrical resistance by \(R(X,Y)\), the total length by \(L=\sum_i\ell_i\), and the hub-to-hub resistance by \(\rho=(\sum_i\ell_i^{-1})^{-1}\).

The exact **continuous average resistance** of every such parallel-path network is
\[
\boxed{\mathbb E R(X,Y)=\frac16\left(\rho+\frac2L\sum_i\ell_i^2-\frac1{L^2}\sum_i\ell_i^3\right).}\tag{1}
\]
For two paths it is identically \(L/6\), independent of their subdivision. For every \(m\ge3\) it is strictly less than \(L/6\); that bound is a sharp but unattained supremum at fixed \(L\), approached as one path absorbs all the length.

For **exactly three paths**, there is also a sharp global lower bound:
\[
\boxed{\frac L9\le \mathbb E R(X,Y)<\frac L6,}\tag{2}
\]
with equality on the left if and only if all three path lengths are \(L/3\). All positive unequal triples satisfy strict inequalities at both ends. Thus, unlike the two-path circle, the three-path network has a unique most resistance-efficient length allocation under uniform arclength sampling, while its worst mean can be approached only through degeneration.

## Assumptions and scope
The points \(X,Y\) are independent and uniformly sampled from the one-dimensional arclength measure of total mass \(L\). Effective electrical resistance is the voltage difference under unit current between the two sampled points; it is **not** the shortest-path (geodesic) distance. Path lengths are arbitrary positive real numbers and may coincide. The graph contains all continuum points on its edges, not just the two hubs; endpoints of edges have arclength measure zero. The sharpness of the upper endpoint means a supremum along positive lengths, not an attained maximum.

## Proof
**1. Edge-pair resistance kernels.** Orient each edge from \(A\) to \(B\). When \(x\) and \(y\) are on the same edge \(i\) of length \(a=\ell_i\), let \(z=|x-y|\). The segment of resistance \(z\) is parallel to the complementary segment of resistance \(a-z\) plus the remaining network between \(A,B\). Removing edge \(i\) leaves resistance \(\sigma_i=(\sum_{j\ne i}\ell_j^{-1})^{-1}\). Series-parallel reduction and \(\rho=a\sigma_i/(a+\sigma_i)\) yield
\[
R_{ii}(x,y)=\frac{z(a-z+\sigma_i)}{a+\sigma_i}
=z-\frac{a-\rho}{a^2}z^2.\tag{3}
\]

For distinct edges \(i\ne j\) of lengths \(a,b\), one can ground \(A\) and decompose the electrical Gaussian potential field into a common hub voltage with variance \(\rho\) and independent zero-endpoint Brownian bridges of durations \(a,b\). On edge \(i\) its value at \(x\) is \((x/a)Z+B_i(x)\), where \(\operatorname{Var}Z=\rho\) and \(\operatorname{Var}B_i(x)=x(a-x)/a\). The variance of a difference equals effective resistance (this follows directly by inversion of the grounded conductance Laplacian, or from the Dirichlet energy characterization). Consequently,
\[
R_{ij}(x,y)=\frac{x(a-x)}a+\frac{y(b-y)}b+
\rho\left(\frac xa-\frac yb\right)^2.\tag{4}
\]
Equivalently, (4) follows by a four-terminal Kirchhoff circuit solve; no probabilistic randomness in the network is assumed. The Gaussian field is only a device for computing a deterministic resistance kernel.

**2. Integrals over edge pairs.** The elementary integrals \(\int_{[0,a]^2}|x-y|\,dx\,dy=a^3/3\) and \(\int_{[0,a]^2}|x-y|^2\,dx\,dy=a^4/6\) imply
\[
\int_{[0,a]^2}R_{ii}(x,y)\,dx\,dy=\frac{a^3+\rho a^2}{6}.\tag{5}
\]
For \(i\ne j\), independently uniform fractions \(x/a,y/b\) satisfy \(\mathbb E(x/a-y/b)^2=1/6\). Therefore
\[
\int_0^a\!\int_0^b R_{ij}(x,y)\,dy\,dx
=\frac{ab(a+b+\rho)}6.\tag{6}
\]
Sum (5) over all edges and (6) over both orders of each distinct-edge pair, then divide by \(L^2\). The identities \(\sum_i a_i^2=L^2-2\sum_{i<j}a_ia_j\) and
\[
\sum_i\ell_i^3+2\sum_{i<j}\ell_i\ell_j(\ell_i+\ell_j)
=2L\sum_i\ell_i^2-\sum_i\ell_i^3
\]
give (1) exactly.

**3. The cycle benchmark and the strict upper bound.** Put \(p_i=\ell_i/L\) and \(h=(\sum_i p_i^{-1})^{-1}=\rho/L\). Formula (1) becomes
\[
6\mathbb E R/L=h+2\sum_i p_i^2-\sum_i p_i^3
=1-\left(\sum_i p_i(1-p_i)^2-h\right).\tag{7}
\]
By Cauchy-Schwarz,
\[
\left(\sum_i p_i(1-p_i)^2\right)\left(\sum_i p_i^{-1}\right)
\ge \left(\sum_i(1-p_i)\right)^2=(m-1)^2.\tag{8}
\]
For \(m\ge3\), the expression in parentheses in (7) is at least \(((m-1)^2-1)h>0\), proving the strict upper bound. When \(m=2\), both paths together form a circle of circumference \(L\) and \(h=p_1p_2=\sum_i p_i(1-p_i)^2\), giving \(L/6\) exactly. For any fixed \(m\ge3\), let \(p_1\to1\) and all other \(p_i\to0\). Then both \(h\) and \(\sum p_i(1-p_i)^2\) tend to zero, so \(\mathbb ER\to L/6\). This proves sharpness without attainment.

**4. Unique three-path minimum.** For \(m=3\), write \(p,q,r>0\) with \(p+q+r=1\), \(u=pq+pr+qr\), and \(v=pqr\). Since \(\sum_i1/p_i=u/v\), we have \(h=v/u\). Newton's identities give \(\sum p_i^2=1-2u\) and \(\sum p_i^3=1-3u+3v\). Thus
\[
\frac{6\mathbb ER}{L}=1-u+v\left(\frac1u-3\right).\tag{9}
\]
The elementary identity \(u=(1-(p^2+q^2+r^2))/2\le1/3\), with equality exactly at \(p=q=r=1/3\), shows \(1/u-3\ge0\). Therefore (9) is at least \(1-u\ge2/3\), proving \(\mathbb ER\ge L/9\). Equality in both inequalities requires \(p=q=r=1/3\), where (9) is exactly \(2/3\). This proves uniqueness and completes (2).

## Verification
The companion standalone `check_resistance.py` reconstructs resistor networks with the sampled continuum points inserted as additional electrical nodes, then solves the grounded Kirchhoff equations. For 400 random point pairs across five networks it compares the direct nodal voltage difference against (3)–(4); independent double integration and tensor Gauss quadrature compare with (1). It also checks the cycle identity and randomly stress-tests the three-edge bounds. The observed completion markers were `DIRECT_CIRCUITS_AND_EXACT_MEAN_OK` and `THREE_PATH_SHARP_BOUNDS_AND_TWO_PATH_INVARIANCE_OK`. The finite computation corroborates the analytic proof; it is not an exhaustive infinite-parameter verification.

## Relationship to prior work
Baker and Faber's 2004 preprint supplies the metrized-graph resistance framework and the edgewise quadratic formula for resistance from a vertex (Theorem 10); those general principles and the underlying series-parallel laws are prior art, not claimed as new. Cinkir (first posted 2009) computes the *tau constant* of arbitrary multi-edge banana graphs, \(\tau=L/12-(m-2)\rho/6\). This depends only on \(L,\rho,m\), whereas (1) depends additionally on two length power sums. Thus the tau-constant result is not the arclength-uniform two-point resistance mean or its three-edge sharp optimization. For example, the triples \((1/5,3/10,1/2)\) and \((1/4,3/8-3\sqrt{57}/152,3/8+3\sqrt{57}/152)\) have the same \(L=1\) and \(\rho=3/31\), but (1) yields different mean resistances.

Previous three-path metric-graph work on *intrinsic mean distance* establishes a distinct sharp geodesic-length inequality with coefficient \(5/27\), which does not imply (2) because resistance and shortest-path distance are different metrics. Previous work on the *terminal resistance eccentricity* of parallel paths maximizes the resistance from a fixed branch vertex to a single point, again a different statistic. The new content assessed here consists of the exact arclength-uniform pair-resistance mean for arbitrary parallel-arm lengths, its cycle benchmark, and the sharp unique three-edge allocation law. Other equivalent treatments might exist outside the inspected material.

## Limitations
This is a continuous-point sampling result for networks of parallel intervals with unit resistance density. It does not assert an optimal length allocation for general \(m\ge4\), arbitrary graph topologies, unequal sampling densities, or discrete vertex-only Kirchhoff indices. The strict upper endpoint in (2) is only a supremum along degenerating positive triples. Historical priority and independent mathematical validation remain provisional.

## References
1. M. Baker and X. Faber, *Metrized graphs, electrical networks, and Fourier analysis*, arXiv:math/0407428, first posted 2004-07-25, §6 and Theorem 10.
2. Z. Cinkir, *The tau constant of a metrized graph and its behavior under graph operations*, arXiv:0901.0407, first posted 2009-01-05, Propositions 8.9–8.10.
3. J. K. Doyle and J. E. Graver, *Mean distance for shapes*, Journal of Graph Theory 6 (1982), 453–471, DOI 10.1002/jgt.3190060410 (intrinsic, not electrical, distance).
4. *Exact intrinsic mean distance and sharp balancing law for three-path theta graphs*, published-finding corpus published finding `c5b63a299170` (intrinsic geodesic statistic).
5. *Resistance-eccentricity tomography of three-path metric networks and its sharp path threshold*, published-finding corpus published finding `4ec9c49f0085` (terminal-to-point extremal statistic).
