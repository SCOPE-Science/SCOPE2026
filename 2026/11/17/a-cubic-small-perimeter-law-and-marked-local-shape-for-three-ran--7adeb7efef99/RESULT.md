# A cubic small-perimeter law and marked local shape for three random great circles

## Finding

Let \(G_1,G_2,G_3\) be independent isotropically distributed unoriented great circles on the unit sphere \(S^2\). Fix a pole \(e\), and let \(Z\) denote the unique spherical cell containing \(e\). Its geodesic perimeter is \(P\). The event that this cell is a tiny triangle has a sharp cubic probability law:
\[
\Pr(P\le\varepsilon)=K\varepsilon^3+o(\varepsilon^3),\qquad
K=\frac{I}{12\pi^2}=0.0003096989395717\ldots,
\]
where the convergent and strictly positive integral is
\[
I=\int_0^\pi\!\int_0^{\pi-a}w(a,b,\pi-a-b)\,db\,da,
\qquad
w(\alpha)=\prod_{i=1}^3\frac{\sin^2(\alpha_i/2)}{\cos(\alpha_i/2)}.
\]
The conditional distribution admits a complete geometric limit, not merely a tail coefficient. Set each plane normal to point into the hemisphere containing \(e\), let \(t_i\in(0,1)\) be its scalar product with \(e\), and let \(\alpha\) denote the cyclic planar interior-angle triple formed by the projected normals. Conditional on \(P\le\varepsilon\), the joint distribution of \((\alpha_1,\alpha_2,t_1/\varepsilon,t_2/\varepsilon,t_3/\varepsilon)\) converges in total variation (using the consistent cyclic normal indexing) to the density
\[
\frac{1}{K}\cdot\frac{1}{2\pi^2}\,\mathbf1\!\left\{\alpha_i>0,\sum_i\alpha_i=\pi,\ s_i\ge0,\ \sum_i c_i(\alpha)s_i\le1\right\},
\quad c_i(\alpha)=\cot\frac{\alpha_j}{2}+\cot\frac{\alpha_k}{2}.
\]
Equivalently and more conveniently, \(\alpha\) has density \(w(\alpha)/I\) on the angle simplex. Independently choose \(R\sim\operatorname{Beta}(3,1)\) and \(Y\sim\operatorname{Dirichlet}(1,1,1)\), and set \(S_i=RY_i/c_i(\alpha)\). This describes the limiting joint law of the scaled offsets. Further, \(P/\varepsilon\Rightarrow R\), so, for each \(q>0\),
\[
\lim_{\varepsilon\downarrow0}\mathbb E[(P/\varepsilon)^q\mid P\le\varepsilon]=\frac3{q+3}.
\]
The starting azimuthal phase and clockwise order of the original labels are independent uniform discrete/continuous marks.

## Assumptions and scope

The unit sphere carries its intrinsic geodesic metric and surface measure. Isotropic unoriented great circles mean planes orthogonal to independent uniform unit vectors with the sign forgotten. The pole \(e\) is fixed and not on any input circle almost surely. The angular coordinates are defined cyclically, beginning with the normal of labelled first circle and following counterclockwise. If the other two appear in the opposite label order, the label-order bit records that fact. A set of three planar projected normals is **spanning** when it is not contained in a closed semicircle. On the spanning event their cyclic gaps are \(g_1,g_2,g_3\in(0,\pi)\), summing to \(2\pi\), and \(\alpha_1=\pi-g_2,\ \alpha_2=\pi-g_3,\ \alpha_3=\pi-g_1\), so each angle is in \((0,\pi)\) and \(\sum\alpha_i=\pi\). The coefficient \(c_i\) corresponds exactly to normal \(i\) opposite interior angle \(\alpha_i\). No quantitative error bound beyond the stated little-oh tail is claimed.

## Proof

**1. Independent offset and direction coordinates.** Orient each input plane normal \(n_i\) so that \(n_i\cdot e=t_i>0\). In coordinates with \(e=(0,0,1)\), write
\[
n_i=(\sqrt{1-t_i^2}\cos\phi_i,\sqrt{1-t_i^2}\sin\phi_i,t_i).
\]
By spherical rotational invariance, the six scalar coordinates consist of independent \(t_i\sim\operatorname{Uniform}(0,1)\) and \(\phi_i\sim\operatorname{Uniform}(0,2\pi)\). The spherical cell is the intersection of the three closed hemispheres \(n_i\cdot x\ge0\) with \(S^2\).

**2. Spanning is necessary for a tiny cell.** If the planar unit normals \(u_i=(\cos\phi_i,\sin\phi_i)\) lie in a semicircle, there is a planar direction \(v\) such that \(u_i\cdot v\ge0\) for all \(i\). The great-circle arc \(x(\theta)=(\sin\theta\,v,\cos\theta)\), \(0\le\theta\le\pi/2\), lies in \(Z\). Thus the diameter of \(Z\) is at least \(\pi/2\), and its boundary perimeter is at least \(\pi\). Consequently, for \(\varepsilon<\pi\), the event \(P\le\varepsilon\) forces spanning. Under spanning, the intersection is a spherical triangle entirely within the open northern hemisphere: a southern point would violate a strictly positive linear combination of the planar normal inequalities (the positive weights annihilate the planar normals).

**3. Exact local planar model.** Gnomonic coordinates map \(z\in\mathbb R^2\) to \((z,1)/\sqrt{1+|z|^2}\). The three hemispheres become exactly the planar halfplanes
\[
u_i\cdot z\ge-h_i,\qquad h_i=\frac{t_i}{\sqrt{1-t_i^2}}.
\]
On spanning, their intersection is a bounded triangle containing the origin. Moving its three supporting lines independently gives the *exact Euclidean perimeter*, linear in the three offsets:
\[
P_{\rm Euclid}(h,\alpha)=\sum_{i=1}^3c_i(\alpha)h_i,
\qquad c_i=\cot(\alpha_j/2)+\cot(\alpha_k/2).
\]
To verify the coefficient, moving one side outward by a distance \(dh_i\) lengthens the two adjacent sides by \(dh_i\csc\alpha_j\) and \(dh_i\csc\alpha_k\), while the moved side gains \(dh_i(\cot\alpha_j+\cot\alpha_k)\); using \(\csc x+\cot x=\cot(x/2)\) proves the formula. By half-angle addition,
\[
\frac1{c_1c_2c_3}=\prod_{i=1}^3\frac{\sin^2(\alpha_i/2)}{\cos(\alpha_i/2)}=w(\alpha).
\]
For fixed nondegenerate spanning angles, at offsets \(t_i=\varepsilon s_i\) with bounded \(s_i\), the inverse gnomonic metric converges uniformly after scaling to the Euclidean metric; therefore
\[
\varepsilon^{-1}P(\varepsilon s,\alpha)\longrightarrow\sum_i c_i(\alpha)s_i.
\]

**4. Rigorous restriction and limit.** For any compact convex spherical triangle its intrinsic diameter does not exceed half its boundary perimeter (each pair of boundary points has two perimeter arcs, at least one of length at most half the perimeter; interior pairs are no farther than the boundary diameter). Thus, on \(P\le\varepsilon\), every plane supporting an edge is at geodesic distance at most \(\varepsilon/2\) from \(e\). This gives \(t_i\le\sin(\varepsilon/2)\le\varepsilon/2\). The rescaled offsets are therefore confined to the fixed cube \([0,1]^3\). Gnomonic convergence from step 3 and a zero-measure limiting boundary imply pointwise almost-everywhere convergence of the small-perimeter indicators. Domination by the cube indicator proves convergence of the rescaled probabilities and convergence in \(L^1\) of their joint conditional densities (equivalently, total variation by Scheffé's lemma).

**5. Angular integration and the coefficient.** For three independent uniform azimuths, the probability of planar spanning is exactly \(1/4\). Given spanning, the cyclic gaps \(g_i\in(0,\pi)\) are uniformly distributed on their two-dimensional simplex; hence the complementary angles \(\alpha_1=\pi-g_2,\ \alpha_2=\pi-g_3,\ \alpha_3=\pi-g_1\) have density \(2/\pi^2\) on \(\alpha_i>0\), \(\sum\alpha_i=\pi\). For fixed \(\alpha\), integration over the offsets gives
\[
\int_{s_i\ge0}\mathbf1\{\sum_i c_i s_i\le1\}\,ds_1ds_2ds_3=\frac1{6c_1c_2c_3}=\frac{w(\alpha)}6.
\]
Therefore the coefficient equals \((1/4)(2/\pi^2)(1/6)\int w=I/(12\pi^2)\), as stated. The integrand vanishes at degenerate angle boundaries, and is continuous and positive in the interior; thus \(I\) is finite and nonzero.

**6. Marked limit and factorization.** The limiting conditional angular density is \(w(\alpha)/I\). For fixed angles put \(y_i=c_i s_i\), \(r=\sum_i y_i\), and \(Y_i=y_i/r\). The three-dimensional Jacobian is \(r^2/\prod_i c_i\). The conditional distribution on \(\{y_i\ge0,\sum_i y_i\le1\}\) is uniform and factors as the product of \(3r^2dr\) on \((0,1)\) and the uniform Dirichlet density on the two-simplex. Thus \(R\) and \(Y\) are independent of the biased angles; the original uniform azimuthal phase and cyclic label-order bit are independent as well. Since \(P/\varepsilon\) differs from \(r\) by a term tending to zero on the conditioning event, its beta limit and the stated conditional moment limits follow by bounded convergence. This completes the proof.

## Verification

An independently executable script `check.py` evaluates the positive two-dimensional coefficient integral, estimates the same coefficient by independently sampling three planar normal directions, checks the exact planar side-shift identity against three vertex intersections, and checks the spherical-perimeter small-event probability by direct spherical geometry under a justified rare-event importance sampling scheme. All numerical tests are finite corroborations; the proof is the analytic argument above. The quadrature yields \(I=0.0366792722041182\ldots\), \(K=0.0003096989395717\ldots\).

## Relationship to prior work

Hug and Schneider, *Random conical tessellations*, arXiv:1508.07768, first published online August 31, 2015, discuss the fixed-ray cell for random great subspheres explicitly in Section 5 and obtain first and second moment identities, including the corresponding spherical typical/zero-cell size-bias relationship. That is the same underlying random object, but its statements do not furnish the cubic small-geodesic-perimeter probability or the joint offset–angle conditioned limit. Huiling Le's 1989 *Random spherical triangles II: Shape densities* derives a shape-space distribution for spherical triangles whose three vertices are uniform in a cap. This is potentially related by polar duality to the hemisphere-normal triangle. It cannot be excluded as a source of an implicit scalar perimeter formula; the present marked small-pole-offset law is finer than the rotation-quotiented triangular shape density. Le's full text was not available for a definitive implication comparison. The earlier spherical tessellation moment work of Miles and Arbeiter–Zähle likewise remains a priority risk where full texts are unavailable.

## Limitations

Only three isotropic great circles on \(S^2\) are treated. The theorem is a small-perimeter asymptotic, not a finite-perimeter distribution or a numerical error rate. The marked convergence uses fixed nondegenerate angle parameters almost everywhere; no uniform estimate over degenerate angular shapes is asserted. The first public date belongs to the motivating source, not a claimed prior appearance of the new result. Historical priority remains provisional, and no independent expert audit was performed.

## References

1. D. Hug and R. Schneider, *Random conical tessellations*, arXiv:1508.07768 (first public submission August 31, 2015), Section 5, https://arxiv.org/abs/1508.07768.
2. H. Le, *Random spherical triangles II: Shape densities*, *Advances in Applied Probability* **21** (1989), 581–594, https://doi.org/10.2307/1427637 (abstract only inspected).
3. M. Arbeiter and M. Zähle, *Geometric measures for random mosaics in spherical spaces*, 1994, https://doi.org/10.1080/17442509408833870 (bibliographic metadata only inspected).
