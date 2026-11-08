# Cusp-pair tails for random distances in ideal hyperbolic polygons

## Finding

Let \(P\) be a fixed convex ideal \(n\)-gon, \(n\geq 3\), in the complete hyperbolic plane of curvature \(-1\). Let \(X,Y\) be independent and uniform for hyperbolic area on \(P\), and set \(D=d_{\mathbb H^2}(X,Y)\). There is a positive, explicitly computable, isometry-invariant quantity \(C(P)\) such that

\[
\boxed{\Pr(D>R)=C(P)R e^{-R}+O_P(e^{-R})\qquad(R\to\infty).}
\]

Normalize by a hyperbolic isometry so the ideal vertices are \(a_1<\cdots<a_m<\infty\), followed cyclically by \(\infty\), where \(m=n-1\). Define \(w_\infty=a_m-a_1\) and

\[
\begin{split}
w_1&=(a_2-a_1)^{-1},\\
w_m&=(a_m-a_{m-1})^{-1},\\
w_i&=(a_i-a_{i-1})^{-1}+(a_{i+1}-a_i)^{-1}\quad(1<i<m).
\end{split}
\]

Then

\[
\boxed{C(P)=\frac{2}{(n-2)^2\pi^2}\left[w_\infty\sum_{i=1}^m w_i+\sum_{1\le i<j\le m}w_iw_j(a_j-a_i)^2\right].}
\]

For an ideal triangle, \(C(P)=6/\pi^2\). An ideal quadrilateral can be normalized to vertices \(0,1,t,\infty\) with \(t>1\), and its coefficient is

\[
\boxed{C(P)=\frac{2t^2}{\pi^2(t-1)}\ge\frac{8}{\pi^2}.}
\]

Equality holds exactly for the regular ideal quadrilateral, up to hyperbolic isometry. The asymptotic error is for each **fixed** polygon; no uniformity is asserted as polygonal vertices coalesce.

## Assumptions and scope

The polygon is the closed convex hull of \(n\) distinct cyclically ordered points on the circle at infinity, with interior carrying area measure. All geodesic distances are ambient curvature-\(-1\) hyperbolic distances (equivalently, intrinsic distances because \(P\) is geodesically convex). Gauss--Bonnet gives \(A=\operatorname{area}(P)=(n-2)\pi<\infty\), so independent area-uniform points are well defined. The limiting variable \(R\) is a geodesic distance, not a Euclidean distance or a boundary-clearance distance. For each fixed \(P\), constants in \(O_P(\cdot)\) may depend on its shape.

## Proof

**1. Exact cusp charts and their area densities.** Work in the upper half-plane with metric \(ds^2=(dx^2+dy^2)/y^2\). For the vertex at infinity, the two adjacent sides are vertical lines, and for sufficiently large \(H_\infty\) its cusp is exactly

\[
\{x+iy:a_1<x<a_m,\ y>H_\infty\}.
\]

For a finite vertex \(a_i\), apply the hyperbolic isometry \(\gamma_i(z)=-1/(z-a_i)\). The two sides adjacent to this vertex become vertical lines. Their separation is \(w_i\): the images of the neighboring vertices are the reciprocal differences displayed in the definition above, with an image of zero for an infinite neighbor. For a sufficiently large \(H_i\), the corresponding cusp is exactly a vertical strip of Euclidean width \(w_i\) above \(H_i\), in the \(\gamma_i\) chart. Choose all \(H_i\) so the cusps are disjoint. Their complement in \(P\) is compact.

Write \(y=H_i e^u\), \(u\ge0\), and let the transverse coordinate \(\xi\) range over the strip of width \(w_i\). Exactly, not just asymptotically,

\[
 dA=\frac{w_i}{H_i}e^{-u}\,du\,\frac{d\xi}{w_i}.
\]

Thus the unnormalized area of a cusp-depth slice is \((w_i/H_i)e^{-u}du\). Here \(w_\infty\) is interpreted in the same way.

**2. Pairwise cusp distance.** Fix distinct cusps \(i,j\). For finite indices, a point at depth \(u\) has representation

\[
 z_i=a_i-\frac{1}{\xi_i+iH_i e^u}.
\]

Its imaginary part is \((H_i e^u)^{-1}(1+O_P(e^{-2u}))\), and its real part is \(a_i+O_P(e^{-2u})\), uniformly in the bounded transverse coordinate. The upper-half-plane distance formula

\[
\cosh d(z,w)=1+\frac{|z-w|^2}{2\operatorname{Im}(z)\operatorname{Im}(w)}
\]

gives, for two distinct finite cusps,

\[
 d(z_i,z_j)=u+v+\log\bigl((a_i-a_j)^2H_iH_j\bigr)
 +O_P(e^{-u}+e^{-v}).
\]

For one point in the cusp at infinity and one in the finite cusp \(i\), the same calculation gives

\[
 d(z_\infty,z_i)=u+v+\log(H_\infty H_i)
 +O_P(e^{-u}+e^{-v}).
\]

Both estimates are uniform in transverse coordinates, for all \(u,v\ge0\) once the fixed cutoff heights are sufficiently large. Let \(g_{ij}=(a_i-a_j)^2\) for finite indices and \(g_{i\infty}=1\). In either case write the main term as \(u+v+\kappa_{ij}\), where \(\kappa_{ij}=\log(g_{ij}H_iH_j)\).

**3. Quantified convolution tail.** Independent exponential depths obey the exact identity

\[
 \int_{u,v\ge0}e^{-(u+v)}\mathbf1_{\{u+v>s\}}\,du\,dv
 =(s+1)e^{-s}\qquad(s\ge0).
\]

Replacing \(u+v+\kappa_{ij}\) by the true distance changes this double integral by \(O_P(e^{-R})\). For completeness, the difference of the two indicator functions is supported on

\[
 |u+v-(R-\kappa_{ij})|\le C_P(e^{-u}+e^{-v}).
\]

Set \(s=u+v\) and \(b=R-\kappa_{ij}\). This support lies in \(|s-b|\le2C_P\). At each fixed \(u\), its possible \(s\)-width is bounded by a constant times \(e^{-u}+e^{-(b-u)}\), with a constant depending only on \(P\). The integral of that bound for \(0\le u\le b+2C_P\) is bounded independently of \(b\); on the support, \(e^{-s}=O_P(e^{-R})\). Hence the indicator replacement costs \(O_P(e^{-R})\).

The contribution from the **ordered** cusp pair \((i,j)\), before division by \(A^2\), is therefore

\[
 \frac{w_iw_j}{H_iH_j}(R-\kappa_{ij}+1)e^{-R+\kappa_{ij}}+O_P(e^{-R})
 =w_iw_jg_{ij}R e^{-R}+O_P(e^{-R}).
\]

Importantly the arbitrary cutoff heights cancel from the leading coefficient.

**4. All remaining pairs are lower-order.** Two points in the same cusp have distance at most \(|u-v|+w_i/H_i\): join their vertical lines along a horizontal horocycle at the larger height. Since \(\int e^{-u-v}\mathbf1_{\{|u-v|>s\}}du\,dv=e^{-s}\), their contribution is \(O_P(e^{-R})\). If one point lies in the compact core, its distance to a point at cusp depth \(u\) is at most \(u+C_P\), so such pairs also contribute \(O_P(e^{-R})\). Both points in the compact core have bounded distance. Summing all ordered distinct-cusp pairs and normalizing by \(A^2=(n-2)^2\pi^2\) proves the displayed formula.

**5. Triangle and sharp quadrilateral case.** With vertices \(0,1,\infty\), all three cusp widths are one, so the three unordered cusp pairs give \(C=2\cdot3/\pi^2\). For vertices \(0,1,t,\infty\), the four widths are

\[
 w_0=1,\quad w_1=\frac{t}{t-1},\quad w_t=\frac1{t-1},\quad w_\infty=t.
\]

Substitution yields \(C=2t^2/[\pi^2(t-1)]\). Finally,

\[
 \frac{t^2}{t-1}-4=\frac{(t-2)^2}{t-1}\ge0,
\]

with equality precisely at \(t=2\). Four cyclically ordered ideal vertices of cross-ratio parameter \(t=2\) form the regular ideal quadrilateral up to isometry. This proves the unique minimizing shape.

## Verification

The accompanying `verify_ideal_polygon_distance_tail.py` independently samples area-uniform points by decomposing the polygon into ideal triangles with one vertex at infinity. For a triangle over a boundary interval \((a,b)\), the area coordinate has \(x=a+(b-a)\sin^2\theta\), where \(\theta\) is uniform on \((0,\pi/2)\), followed by \(y=\sqrt{(x-a)(b-x)}/U\) for independent uniform \(U\in(0,1)\). Each triangle has exact hyperbolic area \(\pi\).

The checker also compares exact cusp-chart distances with the asymptotic \(u+v+\kappa_{ij}\), independently evaluates the finite-vertex coefficient formula, tests the quadrilateral extremum algebra, and reports finite-threshold Monte Carlo survival frequencies for three shapes. Run `python -m pip install -r requirements.txt` and then `python verify_ideal_polygon_distance_tail.py` from the package directory. The fixed-seed test output ends with `IDEAL_HYPERBOLIC_POLYGON_CUSP_PAIR_TAIL_CHECKS_OK`. Simulations corroborate but do not prove the limiting coefficient.

## Relationship to prior work

Castle, Peyerimhoff and Siburg (2011), and Parker, Peyerimhoff and Siburg (arXiv preprint first made public on July 25, 2016), study ideal hyperbolic polygons and extremality of **closed billiard-trajectory lengths**. Their deterministic length comparisons do not give a probability law for the distance of two independent area-uniform points. Martin (2018) studies random ideal quadrilaterals parameterized by boundary-point cross ratios and geometric data of associated punctured tori. That randomization is over **polygon shapes**, unlike the area-uniform sampling of two points in one fixed shape used here. The present coefficient is a different, explicitly computed cross-ratio-sensitive statistic.

## Limitations

The statement applies to convex all-ideal polygons in curvature \(-1\), not to polygons with finite vertices, nonconvex regions, or random boundary-point sampling. Its remainder is not uniform under degeneration of polygon moduli. The result is a self-reviewed mathematical derivation and numerical corroboration, **not** an independently audited proof or a certified historical priority determination. Earlier general hyperbolic pair-distance or cusp-convolution literature could potentially subsume the result and remains a priority risk.

## References

- S. Castle, N. Peyerimhoff and K. F. Siburg, *Billiards in ideal hyperbolic polygons*, Discrete Contin. Dynam. Systems 29 (2011), 893–908, DOI: 10.3934/dcds.2011.29.893. (Publicly accessible author manuscript also available.)
- J. R. Parker, N. Peyerimhoff and K. F. Siburg, *Minimizing length of billiard trajectories in hyperbolic polygons*, arXiv:1607.07383, first submitted July 25, 2016; https://arxiv.org/abs/1607.07383.
- G. J. Martin, *Random Ideal Hyperbolic Quadrilaterals, the Cross Ratio Distribution and Punctured Tori*, arXiv:1807.06202, first submitted July 17, 2018; https://arxiv.org/abs/1807.06202.
