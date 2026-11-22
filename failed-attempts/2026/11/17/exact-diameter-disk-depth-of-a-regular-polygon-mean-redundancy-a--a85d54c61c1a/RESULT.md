# Exact diameter-disk depth of a regular polygon: mean redundancy and a quantitative limit law

## Finding
Let \(n\ge3\) and let \(P_n\) be the regular \(n\)-gon with unit circumradius, centered at the origin. For each vertex \(v_j\), let \(D_j\) be the **closed Euclidean disk** having \([0,v_j]\) as diameter. Let \(X_n\) be uniform with respect to planar area in \(P_n\), and define the diameter-disk depth
\[
M_n(x)=\sum_{j=0}^{n-1}\mathbf 1_{D_j}(x).
\]
Then the mean depth is **exactly**
\[
\boxed{\mathbb E M_n(X_n)=\frac{\pi/2-\pi/n}{\sin(2\pi/n)}+\frac12.}
\]
For every \(n\ge3\), this strictly exceeds \(n/4\), and
\[
\mathbb E M_n(X_n)=\frac n4+\frac{\pi^2}{6n}-\frac{\pi^2}{3n^2}+O(n^{-3}).
\]
For every nonzero \(x\in P_n\), the **sharp deterministic estimate**
\[
\boxed{\left|\frac{M_n(x)}n-\frac{\arccos\|x\|}{\pi}\right|\le\frac1n}
\]
holds. The \(1/n\) constant is attained at the midpoint of any side of \(P_n\).

Consequently \(M_n(X_n)/n\) converges in distribution to a random variable \(Q\in[0,1/2]\) with explicit cumulative distribution function
\[
\boxed{F_Q(q)=\begin{cases}0,&q<0,\\\sin^2(\pi q),&0\le q\le1/2,\\1,&q>1/2.\end{cases}}
\]
More quantitatively, for all integers \(n\ge3\),
\[
\boxed{\sup_{q\in\mathbb R}\left|\Pr\left(M_n(X_n)/n\le q\right)-F_Q(q)\right|\le\frac\pi n+1-\frac{n\sin(2\pi/n)}{2\pi}.}
\]
In particular, \(\operatorname{Var}(Q)=1/16-1/(2\pi^2)\), so the limiting depth remains nondegenerate.

## Assumptions and scope
All distances, disks and areas are Euclidean. Vertices are \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\), with \(0\le j<n\), and \(P_n=\operatorname{conv}\{v_j\}\). The random point is area-uniform, not perimeter-uniform. Each disk has radius \(1/2\), contains the origin on its boundary, and is tangent to the unit circumcircle at its associated vertex. Boundary points count as covered; the deterministic estimate excludes \(x=0\), where all \(n\) disks meet. The weak limit and the probabilistic statements are unaffected by this measure-zero exception. The assertions hold for every integer \(n\ge3\), with no parity restriction.

## Proof
**1. One disk, one polygon.** Put \(\beta=\pi/n\) and \(c=\cos\beta\), and focus on \(v_0=(1,0)\). The disk \(D_0\) is \((x-1/2)^2+y^2\le1/4\). The polygon has supporting halfplanes \(u_k\cdot(x,y)\le c\), where the outward unit normals \(u_k\) have arguments \((2k+1)\beta\). The maximum of \(u\cdot x\) on \(D_0\), for a normal making angle \(\alpha\) with \(v_0\), is \((1+\cos\alpha)/2\).

For any nonadjacent side the circular distance of its normal to \(v_0\) is at least \(3\beta\). Since \(1/2\le c<1\),
\[
\frac{1+\cos(3\beta)}2-c
=\frac{(c-1)(4c^2+4c-1)}2<0.
\]
Thus only the two sides adjacent to \(v_0\), with normal angles \(\pm\beta\), can clip \(D_0\). Each such supporting line is at distance \(c/2\) from the disk center and cuts off a circular segment of area
\[
\frac14\bigl(\beta-\sin\beta\cos\beta\bigr).
\]
The two removed caps are disjoint: violation of both inequalities \(c x\pm(\sin\beta)y>c\) would force \(x>1\), while \(D_0\subset\{x\le1\}\). Hence
\[
|D_0\cap P_n|=\frac\pi4-\frac\beta2+\frac{\sin(2\beta)}4.
\]
The polygon area is \(|P_n|=n\sin(2\beta)/2\). Rotational symmetry and linearity of expectation give
\[
\mathbb E M_n(X_n)=\frac{n|D_0\cap P_n|}{|P_n|}
=\frac{\pi/2-\beta}{\sin(2\beta)}+\frac12.
\]
The inequality \(\sin(2\beta)<2\beta\) gives \(\mathbb E M_n>n/4\). Taylor expansion of the exact quotient gives the displayed asymptotic series.

**2. Sharp pointwise discrepancy.** For \(x=r(\cos\theta,\sin\theta)\), \(0<r\le1\), completing the square gives
\[
x\in D_j\quad\Longleftrightarrow\quad\|x\|^2\le x\cdot v_j\quad\Longleftrightarrow\quad\cos(\theta-2\pi j/n)\ge r.
\]
Therefore \(M_n(x)\) counts equally spaced angular sites in the **closed** circular arc of half-angle \(\phi=\arccos r\in[0,\pi/2)\). Counting sites of spacing \(2\pi/n\) in any arc of length \(2\phi\le\pi\) differs from \(n\phi/\pi\) by at most one. This proves the bound. At the midpoint of a polygon side, \(r=\cos(\pi/n)\) and the arc has precisely its two endpoints at consecutive vertex directions, so \(M_n=2\) and \(n\phi/\pi=1\). Thus the discrepancy constant cannot be reduced.

**3. Limit distribution and finite-size error.** Write \(U_n\) for uniform area on \(P_n\) and \(U\) for uniform area on the unit disk. Since \(P_n\) is a subset of that disk, their total variation distance equals
\[
\delta_n=1-\frac{|P_n|}{\pi}=1-\frac{n\sin(2\pi/n)}{2\pi}.
\]
For \(U\), the radius \(R=\|U\|\) has \(\Pr(R\le r)=r^2\) for \(0\le r\le1\). Accordingly \(Q=\arccos R/\pi\) has \(\Pr(Q\le q)=\sin^2(\pi q)\) for \(0\le q\le1/2\). Its density is \(\pi\sin(2\pi q)\), bounded by \(\pi\) on its support; thus its CDF is globally \(\pi\)-Lipschitz. The pointwise bound in Step 2 sandwiches the depth-CDF against the two shifted radial CDFs at displacement \(1/n\). Replacing \(U_n\) by \(U\) changes every event probability by at most \(\delta_n\). The two bounds combine to give the stated \(\pi/n+\delta_n\) Kolmogorov estimate. Finally, integration against this density yields \(\mathbb E Q=1/4\), \(\mathbb E Q^2=1/8-1/(2\pi^2)\), hence the stated variance.

## Verification
The accompanying stand-alone Python 3 program `verify.py` checks the exact intersection area against an independent circular-polygon approximation clipped by all \(n\) supporting lines, compares the resulting mean to the closed formula, tests the angular discrepancy at interior samples and sharp side-midpoint witnesses, and independently samples uniform polygon points. It uses only the Python standard library. The recorded completed run passed ten area comparisons (maximum absolute error below \(8\times10^{-8}\)), 14,400 angular tests, seven Monte Carlo mean tests, and ten finite-size bound checks. These experiments support the proof but do not establish its universal assertions.

Run from the containing directory with `python3 verify.py`.

## Relationship to prior work
Bose, Esteban, Orden, Silveira and Tuttle (2025, §5) investigate diametral disks enclosing large subsets of **finite point sets**, including geodesic analogues, and prove extremal incidence lower bounds. Their result motivates studying quantitative redundancy of diametral-disk incidence, but does not furnish the area-average depth or its distribution for the fixed family of vertex-to-centroid disks. Bose, Esteban and Tuttle (2025/2026, §3.5) give an algorithm for locating a diametral disk containing many input points; that algorithm also does not evaluate these continuous coverage statistics. Earlier existence results of Akiyama et al. (1996) likewise concern optimising a diameter disk over pairs of input points. The present object fixes every diameter at the polygon center and a polygon vertex, then evaluates multiplicity at a uniform continuum point. Neither its mean formula nor its limiting CDF follows from those existential results without a separate geometric integration argument.

## Limitations
The exact finite-\(n\) **full probability mass function** of \(M_n(X_n)\) is not determined here, nor are correlations between incidences for different vertices. The explicit Kolmogorov bound is uniform but not claimed optimal in its coefficient. It does not address arbitrary polygons, geodesic disks, or higher dimensions. Searches of accessible relevant literature and published mathematical results found no covering formula with the same fixed disk family and probability space; this negative search does not independently establish historical priority. A separate simplex diameter-ball result concerns extrema of nested covering regions, not these polygonal area averages or limits. The 1996 original paper was not fully inspected, so possible earlier special-case calculations remain a residual originality risk.

## References
1. P. Bose, G. Esteban, D. Orden, R. Silveira and T. Tuttle, *On geodesic disks enclosing many points*, arXiv:2506.06477 (first publicly submitted 2025-06-06); published in LIPIcs WADS 2025, DOI:10.4230/LIPIcs.WADS.2025.10.
2. P. Bose, G. Esteban and T. Tuttle, *Computational aspects of disks enclosing many points*, arXiv:2601.20036, extended version of a paper from LAGOS 2025; in particular §3.5.
3. J. Akiyama, Y. Ishigami, M. Urabe and J. Urrutia, *On circles containing the maximum number of points*, Discrete Mathematics 151 (1996), 15–18, DOI:10.1016/0012-365X(94)00076-U.
