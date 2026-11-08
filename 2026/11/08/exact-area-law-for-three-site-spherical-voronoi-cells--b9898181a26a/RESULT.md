# Exact area law for three-site spherical Voronoi cells

## Finding

Choose three points \(X_1,X_2,X_3\) independently from normalized surface area on the unit two-sphere \(S^2\). Let \(C_1\) be the closed intrinsic-geodesic Voronoi cell of \(X_1\), and let \(A\) be its ordinary spherical area (solid angle, not divided by \(4\pi\)). Then \(0<A<2\pi\) almost surely, and its **complete distribution** is
\[
\boxed{\Pr(A\le a)=\frac{a(2+\cos a)-3\sin a}{6\pi}},\qquad 0\le a\le2\pi.
\]
The cumulative distribution is \(0\) below that interval and \(1\) above it. On the open interval it has density
\[
\boxed{f_A(a)=\frac{2}{3\pi}\sin\frac a2\left(\sin\frac a2-\frac a2\cos\frac a2\right)}.
\]
In particular,
\[
\Pr(A\le\pi)=\frac16,\qquad
\mathbb E A=\frac{4\pi}{3},\qquad
\operatorname{Var}(A)=\frac{4\pi^2}{9}-\frac{10}{3}.
\]
Both endpoint behaviors are sharp:
\[
\Pr(A\le a)=\frac{a^5}{360\pi}+O(a^7)\quad(a\downarrow0),
\qquad
\Pr(A>2\pi-\varepsilon)=\frac{\varepsilon^2}{6}+O(\varepsilon^4)\quad(\varepsilon\downarrow0).
\]
All three cell areas have the same marginal distribution; the theorem makes no assertion that they are independent.

## Assumptions and scope

The sphere has radius one and its geodesic metric \(d(x,y)=\arccos(x\cdot y)\). The sites are **exactly three**, independent, and Haar-uniform in surface area. The cell is \(C_1=\{z\in S^2:d(z,X_1)\le d(z,X_j)\text{ for }j=2,3\}\); boundaries have zero area. This is the cell of a uniformly labelled site, not the size-biased cell containing an independently uniform observation point. Coincident or antipodal sites and coincident bisector normals have probability zero. Angular quantities are in radians.

## Proof

**Step 1: geometric reduction.** Rotational invariance permits setting \(X_1=e=(0,0,1)\). Because \(\arccos\) is strictly decreasing,
\[
C_1=\{z\in S^2:b_2\cdot z\ge0,\ b_3\cdot z\ge0\},\qquad
b_j=\frac{e-X_j}{\|e-X_j\|}.
\]
For two nonparallel unit normals with angular separation \(\gamma=\arccos(b_2\cdot b_3)\in(0,\pi)\), the intersection of the corresponding closed hemispheres is a spherical lune of opening \(\pi-\gamma\), hence area \(A=2(\pi-\gamma)\). To see the opening, use coordinates along the line of intersection of the two boundary planes; in its orthogonal plane the two half-plane inequalities define an angular wedge of opening \(\pi-\gamma\), and a unit-sphere lune with wedge angle \(\alpha\) has area \(2\alpha\), obtained by integrating \(\sin\theta\,d\theta\,d\phi\).

**Step 2: the bisector-normal law.** A Haar-uniform \(X\in S^2\) has \(h=e\cdot X\) uniform on \([-1,1]\) and independent uniform azimuth. The unit normal \(b=(e-X)/\|e-X\|\) satisfies
\[
e\cdot b=\sqrt{\frac{1-h}{2}}=:u\in(0,1).
\]
Thus \(u\) has density \(2u\), and its azimuth is uniform. Because spherical area is \(du\,d\varphi\) in these coordinates, the density of \(b\) relative to spherical area is
\[
q_e(b)=\frac{(e\cdot b)_+}{\pi},\qquad (t)_+:=\max(t,0).
\]
The normals \(b_2,b_3\) are independent with this same cosine-weighted hemispherical law.

**Step 3: the exact angular kernel.** Fix any unit vectors \(v,w\) with angle \(\gamma\) and let \(U\) be uniform on \(S^2\). Direct integration gives
\[
K(\gamma):=\mathbb E[(U\cdot v)_+(U\cdot w)_+]
=\frac{\sin\gamma+(\pi-\gamma)\cos\gamma}{6\pi}.
\]
For completeness, take \(G\) standard Gaussian in \(\mathbb R^3\), write \(G=RU\), and use \(\mathbb E R^2=3\). Projection of \(G\) onto \(\operatorname{span}(v,w)\) is an isotropic two-dimensional Gaussian with independent uniform polar angle \(t\) and squared polar radius of mean \(2\). The positive-part product is supported on an angular interval of length \(\pi-\gamma\); its angular integral is
\[
\int_{\gamma-\pi/2}^{\pi/2}\cos t\cos(t-\gamma)\,dt
=\tfrac12\{\sin\gamma+(\pi-\gamma)\cos\gamma\}.
\]
Multiplying by \(2/(2\pi)\) for the planar Gaussian and dividing by \(3\) for the radial Gaussian yields the stated \(K\). This standard cosine-kernel identity is not asserted to be novel.

**Step 4: angle and cell-area distributions.** If \(v,w\) were independent *uniform* directions on \(S^2\), their mutual-angle density would be \(\tfrac12\sin\gamma\). At fixed separation \(\gamma\), their joint orientation is Haar-uniform. Reweighting their joint uniform density by \((4\pi)^2q_e(v)q_e(w)=16(e\cdot v)_+(e\cdot w)_+\), the actual angle density becomes
\[
f_\gamma(\gamma)=\tfrac12\sin\gamma\,16K(\gamma)
=\frac4{3\pi}\sin\gamma\,[\sin\gamma+(\pi-\gamma)\cos\gamma],
\quad0<\gamma<\pi.
\]
The change of variables \(a=2(\pi-\gamma)\), with Jacobian \(1/2\), gives the asserted \(f_A\). Direct antidifferentiation gives the displayed \(F_A\). It satisfies \(F_A(0)=0\) and \(F_A(2\pi)=1\), so there are no atoms or missing probability mass.

**Step 5: exact moments and tail orders.** Integrating \(a f_A(a)\) and \(a^2f_A(a)\) on \([0,2\pi]\) gives
\[
\mathbb E A=4\pi/3,\qquad \mathbb E A^2=20\pi^2/9-10/3.
\]
Subtracting the square of the mean gives the variance. Finally, Taylor expansion of the *exact* CDF at both endpoints yields
\[
F_A(a)=a^5/(360\pi)-a^7/(7560\pi)+O(a^9),
\]
\[
1-F_A(2\pi-\varepsilon)=\varepsilon^2/6-\varepsilon^4/72+O(\varepsilon^5),
\]
which establishes the sharp leading tail exponents and coefficients. The result follows.

## Verification

The accompanying `verify_voronoi.py` uses two independent forms of evidence. Deterministic numerical quadrature checks normalization and the first two moments, numerical differentiation checks the density, and exact point-sampling from spherical area generates 500,000 three-site configurations and compares empirical CDF values and moments with the formulas. A separate sampling of 125,000 uniform points verifies the spherical-lune area identity for several frozen configurations. The checker was executed and returned `THREE_SITE_SPHERICAL_VORONOI_AREA_LAW_OK 500000 125000`. The proof above, not finite simulation, establishes the general claim. To reproduce, run `python verify_voronoi.py` with Python 3 and NumPy.

## Relationship to prior work

The spherical Voronoi-cell framework and its halfspace characterization are classical. The geometric random-cell motivation is closely related to Devroye, Györfi, Lugosi and Walk (2015), which studies asymptotic cell measures in Euclidean space. Kabluchko and Thäle (2019) study the **face vector** of a typical spherical Voronoi cell, including a corresponding halfspace representation, not this specific random-area law. The two-vector positive-part integral used in Step 3 is the classical first-order arc-cosine kernel of Cho and Saul (2009), and is **not** claimed as new. The resulting spherical three-site area CDF, moments and sharp endpoint tails were not identified in the inspected primary works. Earlier broad spherical-tessellation papers by Miles (1971) and Arbeiter–Zähle (1994) are genuine historical-priority risks; their full texts were not available for substantive comparison. No claim of exhaustive historical originality is made.

## Limitations

The formula concerns ordinary area on the unit two-sphere, three sites, and the cell attached to a labelled randomly chosen site. It is not the distribution of the area-biased cell containing an independent uniform point, nor a general formula for four or more sites, other dimensions, nonuniform sampling, or Euclidean or hyperbolic Voronoi diagrams. Neither independence nor joint distribution of the three areas is established. Relevant inaccessible older literature may contain equivalent statements. Computational experiments only corroborate, not certify, the proof; independent audit has not been performed.

## References

- L. Devroye, L. Györfi, G. Lugosi, H. Walk, *On the measure of Voronoi cells*, arXiv:1512.04267v1 (first posted 2015-12-14), https://arxiv.org/abs/1512.04267.
- Z. Kabluchko, C. Thäle, *The typical cell of a Voronoi tessellation on the sphere*, arXiv:1911.07221 (first posted 2019-11-17), https://arxiv.org/abs/1911.07221.
- Y. Cho, L. K. Saul, *Kernel Methods for Deep Learning*, Advances in Neural Information Processing Systems 22 (2009), https://proceedings.neurips.cc/paper_files/paper/2009/file/5751ec3e9a4feab575962e78e006250d-Paper.pdf.
- R. E. Miles, *Random points, sets and tessellations on the surface of a sphere*, Sankhyā Ser. A 33 (1971), 145–174; https://www.jstor.org/stable/25049720. Full text not inspected.
- E. Arbeiter, M. Zähle, *Geometric measures for random mosaics in spherical spaces*, Stochastics Stochastics Rep. 46 (1994), 63–77, https://doi.org/10.1080/17442509408833870. Full text not inspected.
