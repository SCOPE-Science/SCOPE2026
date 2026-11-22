# The logarithmic interior caustic of random unit-cube projection perimeters

## Finding

Let \(Q=[-1/2,1/2]^3\subset\mathbb R^3\) be the solid unit cube. For Haar-uniform \(N=(n_1,n_2,n_3)\in S^2\), let \(P\) be the Euclidean perimeter of the orthogonal shadow of \(Q\) in \(N^\perp\). Then
\[
P(N)=2\sum_{j=1}^3\sqrt{1-n_j^2},\qquad 4\le P\le 2\sqrt6.
\]
Write \(F(p)=\Pr(P\le p)\) and \(p_*=2+2\sqrt2\). The distribution is absolutely continuous on its open support. At its unique interior singular value, the density satisfies, from either side,
\[
\boxed{f_P(p)=\frac3{\pi\sqrt{2-\sqrt2}}\log\frac1{|p-p_*|}+O(1)\quad(p\to p_*).}
\]
The corresponding sharp endpoint probabilities are
\[
\boxed{F(4+\varepsilon)=\frac38\varepsilon^2+O(\varepsilon^3),\qquad 1-F(2\sqrt6-\varepsilon)=4\sqrt{\frac23}\,\varepsilon+o(\varepsilon).}
\]
The coefficient is dimensionless because the cube side length is normalized to one. For side length \(a>0\), all perimeter thresholds scale by \(a\), and the density coefficient scales by \(1/a\).

## Assumptions and scope

The projection is orthogonal, the cube is solid and Euclidean, and \(N\) is a full-sphere uniform unit normal; signs \(N\mapsto-N\) describe the same plane and are counted consistently. No random point sampling is involved. Perimeter means the outer boundary length of the planar projected convex polygon, not the perimeter of a planar section. Probability statements are for fixed cube side length and \(\varepsilon\downarrow0\).

An exact one-dimensional CDF quadrature is available throughout the support. For \(0\le z\le1\), set
\[
B(z)=\sqrt{1-z^2},\quad L(z)=2[B(z)+z+1],\quad U(z)=2[B(z)+\sqrt{2(1+z^2)}].
\]
For \(z<1\) and \(L(z)<p<U(z)\), define
\[
R(p,z)=\frac{\{[p/2-B(z)]^2-(1+z^2)\}^2-4z^2}{(1-z^2)^2}.
\]
Let \(G(p,z)=0\) for \(p\le L(z)\), \(G(p,z)=1\) for \(p\ge U(z)\), and otherwise let \(G(p,z)=2\arcsin\sqrt{R(p,z)}/\pi\). Assign any value at the zero-measure endpoint \(z=1\) consistent with its limiting conditional law. Then
\[
\boxed{F(p)=\int_0^1G(p,z)\,dz.}
\]
The middle-case radicand lies in \([0,1]\) without numerical clipping; clipping in accompanying code is only for floating-point roundoff.

## Proof

**1. Exact shadow perimeter and range.** The cube is a Minkowski sum of three orthogonal unit line segments. Projecting an axis segment onto \(N^\perp\) leaves length \(\sqrt{1-n_j^2}\). The projected hexagonal zonotope (possibly degenerating) has perimeter twice the sum of these three lengths. Put \(q_j=n_j^2\), so \(q_1+q_2+q_3=1\). Strict concavity of \(\sqrt{1-q}\) on \([0,1)\) shows that the maximum \(2\sqrt6\) occurs precisely at the eight normals with all \(|n_j|=1/\sqrt3\); the minimum \(4\) occurs precisely at the six coordinate-axis normals, by concavity on the simplex and direct evaluation.

**2. Complete CDF.** For a uniform sphere normal, \(z=|n_3|\) is uniform on \([0,1]\), independent of the azimuthal angle \(\beta\), whose folded representative lies uniformly in \([0,\pi/2]\). The three absolute coordinates can be represented as \(z\), \(B(z)\cos\beta\), \(B(z)\sin\beta\). Dividing the perimeter by two gives
\[
\frac P2=B(z)+\sqrt{z^2+(1-z^2)\sin^2\beta}+\sqrt{z^2+(1-z^2)\cos^2\beta}.
\]
For each fixed \(0\le z<1\), this expression increases from its value at \(\beta=0\) to its value at \(\beta=\pi/4\) and decreases symmetrically thereafter. The endpoint perimeters are \(L(z)\) and \(U(z)\). If \(A=p/2-B(z)\), the sum of the last two radicals has squared value
\[
(1+z^2)+2\sqrt{z^2+\frac14(1-z^2)^2\sin^2(2\beta)}.
\]
Solving the threshold equation for \(\sin^2(2\beta)\) gives \(R(p,z)\). In the middle case, \(P\le p\) holds on azimuths of total length \(\arcsin\sqrt R\) in \([0,\pi/2]\); dividing by \(\pi/2\) gives \(G\). Averaging over uniform \(z\) proves the quadrature.

**3. Critical points and the unique interior caustic.** Apart from the six coordinate-axis endpoints, the perimeter is smooth on \(S^2\). The constrained stationarity equations for the nonzero coordinates are
\[
-\frac{2n_j}{\sqrt{1-n_j^2}}=2\lambda n_j.
\]
Thus every nonzero coordinate has the same absolute value. The only stationary classes are (i) six axis minima; (ii) twelve normals with one zero coordinate and two nonzero coordinates of absolute value \(1/\sqrt2\), all with value \(p_*\); and (iii) eight diagonal maxima. At a saddle, use orthonormal tangent coordinates \(s,t\), with \(s\) rotating the two equal coordinates against each other and \(t\) adding the missing coordinate. Taylor expansion gives
\[
P(s,t)=p_*-\sqrt2\,s^2+(\sqrt2-1)t^2+O((s^2+t^2)^{3/2}).
\]
Hence each saddle has a nondegenerate Hessian with opposite signs. The analytic Morse lemma and smooth spherical area density reduce its local pushforward to the indefinite quadratic \(x^2-y^2\), with leading Jacobian factor \(1/\sqrt{\sqrt2(\sqrt2-1)}=1/\sqrt{2-\sqrt2}\). For a sufficiently small fixed rectangular neighborhood,
\[
\int\!\int\delta(\eta-(x^2-y^2))\,dx\,dy=\log\frac1{|\eta|}+O(1).
\]
This follows directly by integrating over \(y\), obtaining twice an inverse-square-root integral with logarithmic divergence; the cutoff and smooth-Jacobian corrections contribute only bounded terms. The uniform surface probability density is \(1/(4\pi)\) per unit spherical area. Summing the twelve saddle contributions yields \(12/[4\pi\sqrt{2-\sqrt2}]=3/[\pi\sqrt{2-\sqrt2}]\). On compact subsets excluding these critical directions, the coarea density is smooth by the submersion theorem. Thus there is no other interior density singularity.

**4. The endpoint exponents.** At an axis normal, use tangent polar radius \(r\): \(P-4=2r+O(r^2)\). Six disjoint spherical caps of radius \(\varepsilon/2+O(\varepsilon^2)\) have total normalized area \(3\varepsilon^2/8+O(\varepsilon^3)\). At a diagonal maximum, in orthonormal tangent coordinates \((s,t)\),
\[
P=2\sqrt6-\frac{\sqrt6}{4}(s^2+t^2)+O((s^2+t^2)^{3/2}).
\]
The eight ellipsoidal caps contribute \([8/(4\pi)]\cdot[\pi\varepsilon/(\sqrt6/4)]+o(\varepsilon)=4\sqrt{2/3}\,\varepsilon+o(\varepsilon)\).

## Verification

Run `python CHECKER.py` from a Python environment with NumPy and SciPy installed. Its deterministic seed checks the exact one-dimensional CDF against uniform-sphere simulation, compares the Minkowski-sum perimeter with an independent two-dimensional projected-vertex convex hull on 160 normal directions, verifies endpoint scaling, and estimates the interior log coefficient from two symmetric probability windows. On execution, the measured coefficient was approximately \(1.24679962\), compared to the exact \(3/[\pi\sqrt{2-\sqrt2}]\approx1.24767573\). This is numerical corroboration of, not a substitute for, the proof.

## Relationship to prior work

Finch's 2012 *Planar Projections and Second Intrinsic Volume* (arXiv:1203.2464v1, especially §§2.2, 5) already provides the exact cube periwidth formula and its first two moments; those are **not claimed as discoveries here**. Vickers and Brown's 2001 *The distribution of projected area and perimeter of convex, solid particles* (DOI:10.1098/rspa.2000.0667, §§4, especially the cuboid case) evaluates related projection statistics and plots a numerical joint area–perimeter density, smoothing its visualization. Neither inspected account states the cube's sharp logarithmic marginal-perimeter divergence or its exact coefficient. The new claim is the analytical caustic, its unique critical value, and its calibrated endpoint laws, not the pre-existing projection formula. Related studies of central cube **sections**, width distributions, and constant-width-body brightness involve different random variables and do not provide these constants. This is a best-knowledge comparison, not a claim of exhaustive historical priority.

## Limitations

The theorem assumes an exact cube, Haar-uniform orthographic views, and perfect perimeter measurement. Numerical evaluation of the integral near the caustic needs endpoint-aware quadrature; the checker uses adaptive interval splitting and only modest-precision diagnostics. The logarithmic result is a single marginal statistic, not a new joint area–perimeter density or a classification of all cuboids. A historical priority risk remains from earlier numerical joint-distribution literature and inaccessible detailed records of later moment calculations. Independent mathematical review has not been performed.

## References

1. S. R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, public March 12, 2012. https://arxiv.org/abs/1203.2464
2. G. T. Vickers and D. J. Brown, *The distribution of projected area and perimeter of convex, solid particles*, Proc. R. Soc. Lond. A **457** (2001), 283–306. DOI:10.1098/rspa.2000.0667. https://doi.org/10.1098/rspa.2000.0667
3. R. Schneider and W. Weil, *Stochastic and Integral Geometry*, Springer, 2008 (standard integral-geometric context; not a source of the asserted logarithmic coefficient).
