# Sharp all-dimensional Euclidean chord-perimeter endpoint law for random spherical triangles

## Finding
Let \(d\ge3\) be a fixed integer and let \(X_1,X_2,X_3\) be independent points uniformly distributed with respect to normalized spherical area on \(S^{d-1}\subset\mathbb R^d\). Define the Euclidean **chord** perimeter
\[
P_d=\sum_{1\le i<j\le3}\|X_i-X_j\|_2.
\]
Then its deterministic maximum is \(M=3\sqrt3\), attained exactly when all three pairwise inner products are \(-1/2\), that is, by equilateral triangles on a great circle. Its sharp upper-tail law is
\[
\boxed{\Pr\{P_d>3\sqrt3-\varepsilon\}=C_d\varepsilon^{d/2}+o(\varepsilon^{d/2}),\qquad
C_d=\frac{2^{4-d/2}3^{(3d-10)/4}\Gamma(d/2)}{d\sqrt\pi\,\Gamma((d-1)/2)}.}
\]
In particular, \(C_3=2\sqrt2/(3\,3^{1/4})\) and \(C_4=2\sqrt3/\pi\). The exponent \(d/2\) differs sharply from the previously studied **intrinsic geodesic**-perimeter upper-tail exponent \((d-2)/2\).

There is a marked conditional shape law in **total variation**. By an orthogonal change of frame, put
\[
X_1=e_1,\quad X_2=(u,\sqrt{1-u^2},0,\ldots,0),\quad
X_3=(v,\sqrt{1-v^2}\,s),\quad s\in S^{d-2}.
\]
Near a maximizing configuration, write \(s=(-\sqrt{1-\|\eta\|^2},\eta)\) for \(\eta\in\mathbb R^{d-2}\), and set \(y=(u+1/2,v+1/2,\eta)\in\mathbb R^d\). Define
\[
H_d=\begin{pmatrix}
2\sqrt3/3&\sqrt3/3&0\\
\sqrt3/3&2\sqrt3/3&0\\
0&0&(\sqrt3/4)I_{d-2}
\end{pmatrix},\qquad Z_\varepsilon=(2\varepsilon)^{-1/2}H_d^{1/2}y.
\]
For sufficiently small \(\varepsilon\), the event \(\{P_d>M-\varepsilon\}\) is entirely in this chart, and
\[
\boxed{\mathcal L\bigl(Z_\varepsilon\mid P_d>M-\varepsilon\bigr)
\xrightarrow{\ \mathrm{TV}\ }\operatorname{Unif}(B_d),}
\]
where \(B_d\) is the Euclidean unit ball. The normalized perimeter deficit additionally converges in distribution to \(\operatorname{Beta}(d/2,1)\), jointly with the ball mark, as the square of its radius.

## Assumptions and scope
All \(X_i\) are independent, area-uniform points on the complete unit sphere in a **fixed ambient dimension** \(d\ge3\). The statistic uses straight Euclidean chords, not minimizing spherical arcs, and the cutoff \(\varepsilon\) is an absolute perimeter deficit. The frame is selected measurably from the ordered first two points; degenerate selection events have probability zero. The conditional total-variation assertion concerns the aligned Euclidean coordinate \(Z_\varepsilon\), not a joint total-variation statement involving the deterministic deficit as an additional coordinate. For small enough thresholds, the chart is unambiguous on the conditioning event. No exact finite-threshold CDF, quantitative error rate, or dimension-uniform estimate is asserted.

## Proof
**1. Exact maximum and its equality locus.** Put \(\ell_{ij}=\|X_i-X_j\|_2\). Since the three points lie on the unit sphere,
\[
\sum_{i<j}\ell_{ij}^2=9-\|X_1+X_2+X_3\|_2^2\le9.
\]
Cauchy--Schwarz gives \(P_d^2\le3\sum\ell_{ij}^2\le27\). Equality requires \(X_1+X_2+X_3=0\) and all three chords equal. Equivalently, every pairwise inner product equals \(-1/2\). Such triples are precisely regular equilateral triples on a great circle; they exist for all \(d\ge2\). Fixing \(X_1\) and the direction of \(X_2\) leaves one unique maximum: \(u=v=-1/2\), \(s=(-1,0,\ldots,0)\).

**2. The exact probability element.** Fix \(X_1=e_1\) by rotational invariance, and rotate the perpendicular direction of \(X_2\) to the positive \(e_2\) direction. Conditional on \(u\) and \(v\), the residual vector \(s\) is independent and uniform on \(S^{d-2}\). Moreover \(u\) and \(v\) are independent with common density
\[
f_d(t)=\frac{\Gamma(d/2)}{\sqrt\pi\,\Gamma((d-1)/2)}(1-t^2)^{(d-3)/2},\qquad-1<t<1.
\]
The area \(\omega_{d-2}\) of \(S^{d-2}\) equals \(2\pi^{(d-1)/2}/\Gamma((d-1)/2)\). In the negative-hemisphere chart \(s=(-\sqrt{1-\|\eta\|^2},\eta)\), spherical surface measure has Jacobian \((1-\|\eta\|^2)^{-1/2}\,d\eta\). Thus the joint density in \((u,v,\eta)\) is
\[
 g_d(u,v,\eta)=\frac{f_d(u)f_d(v)}{\omega_{d-2}\sqrt{1-\|\eta\|^2}},
 \quad g_d(-1/2,-1/2,0)=\rho_d=\frac{\Gamma(d/2)^2}{\pi\Gamma((d-1)/2)^2\,\omega_{d-2}}\left(\frac34\right)^{d-3}.
\]
For \(d\ge3\) the density is smooth and strictly positive near the maximum.

**3. The transverse Hessian.** With \(w=X_2\cdot X_3\), the exact coordinate expression is
\[
 w=uv-\sqrt{(1-u^2)(1-v^2)}\sqrt{1-\|\eta\|^2},\qquad
 P_d=\sqrt{2-2u}+\sqrt{2-2v}+\sqrt{2-2w}.
\]
Taylor expansion at \(y=0\) shows that the first derivative vanishes and
\[
 M-P_d=\frac{\sqrt3}{3}\bigl((u+1/2)^2+(u+1/2)(v+1/2)+(v+1/2)^2\bigr)
 +\frac{\sqrt3}{8}\|\eta\|^2+O(\|y\|^3).
\]
The Hessian is exactly \(H_d\) in the finding. Its first two principal eigenvalues are \(\sqrt3\) and \(\sqrt3/3\), while its remaining \(d-2\) eigenvalues equal \(\sqrt3/4\). In particular
\[
 \det H_d=\left(\frac{\sqrt3}{4}\right)^{d-2}>0.
\]
The gradient calculation and Hessian entries follow by differentiating the preceding explicit square-root expression; no asymptotic numerical fit is used.

**4. Localization and the coefficient.** The product of three compact spheres is compact. By Step 1, all maximizers are equilateral. The frame quotient has the single maximizer described above. Consequently, for any sufficiently small chosen local chart neighborhood, the event \(M-P_d<\varepsilon\) lies wholly in that neighborhood when \(\varepsilon\) is small enough. Positive definiteness gives \(\|y\|=O(\sqrt\varepsilon)\) there. Substituting \(z=H_d^{1/2}y/\sqrt{2\varepsilon}\), bounded support and the quadratic Taylor expansion show that the normalized event indicator tends almost everywhere to \(\mathbf1_{\|z\|<1}\). Continuity of \(g_d\) and dominated convergence give
\[
 \Pr(P_d>M-\varepsilon)\sim\rho_d\frac{(2\varepsilon)^{d/2}}{\sqrt{\det H_d}}\operatorname{vol}(B_d),\qquad
 \operatorname{vol}(B_d)=\frac{\pi^{d/2}}{\Gamma(d/2+1)}.
\]
Substituting the explicit \(\rho_d\) and determinant and simplifying gamma and power factors gives precisely the displayed \(C_d\), including the stated instances \(d=3,4\).

**5. Marked limit.** The preconditioning change of variables has constant Jacobian \((2\varepsilon)^{d/2}/\sqrt{\det H_d}\). After normalization by the event probability, the conditional densities of \(Z_\varepsilon\) converge almost everywhere to \(\mathbf1_{\|z\|<1}/\operatorname{vol}(B_d)\). Their masses are all one, so Scheffé's lemma yields convergence in \(L^1\), hence total variation. The same Taylor expansion gives \((M-P_d)/\varepsilon=\|Z_\varepsilon\|^2+o(1)\) conditionally. Since the squared radius of a uniform point in \(B_d\) is \(\operatorname{Beta}(d/2,1)\), the final distributional assertion follows. The last **joint** convergence is weak convergence, not total variation.

## Verification
The standalone `CHECK.py` verifies the three-variable symbolic Hessian, its two-dimensional and transverse blocks, the exact coefficient formula at \(d=3,4\), and the positive-definite determinant. It independently integrates the exact conditional spherical-chord event probability over the first two inner products using a regularized incomplete-beta distribution for the third direction. For \(d\in\{3,4,5,7\}\), its deterministic finite-threshold ratios tend toward the asymptotic constants, with results printed by the script. Run `python CHECK.py` with dependencies listed in `requirements.txt`. These finite computations corroborate but do not replace Steps 1--5, which establish the limits analytically for every fixed dimension in the stated range.

## Relationship to prior work
Hille (1966) proves classical deterministic extremal facts about equal-distance point configurations; the regular-equilateral maximum here is credited, not claimed new. Koroleva and Nikitin (2013) analyze Euclidean perimeters of random polygons **on a circle** and their U-max statistics, providing the already-known planar \(d=2\) endpoint law. Finch and Jones (2010) study random **intrinsic spherical geodesic** triangle perimeter, whose maximum is \(2\pi\). A later all-dimensional geodesic-boundary treatment also studies that distinct observable, with exponent \((d-2)/2\), rather than the present Euclidean-chord maximum \(3\sqrt3\) and exponent \(d/2\). A separate four-point, six-edge **Euclidean** chord-energy endpoint law concerns the regular tetrahedron, not the three-point maximum treated here. The other investigated archival triangle-shape work of Edelman and Strang uses Gaussian planar vertices, not three surface-uniform sphere vertices. Neither those statements nor their immediate corollaries determine the explicit all-dimensional coefficient and local marked law here.

## Limitations
The result is for fixed \(d\ge3\) and i.i.d. uniform sphere samples. It does not give convergence rates, joint dimension--threshold limits, or extensions to nonuniform spherical densities and nonround surfaces. The \(d=2\) circle analogue is already known and not proposed as a new finding. Original historical priority is provisional: the complete texts of Le (1989) on spherical triangle shape densities and Miles (1971) on isotropic simplices were not available after open-access attempts, and general shape-density formulations might encode some consequences. Proof verification here is not independent mathematical certification.

## References
1. A. Edelman and G. Strang, *Random Triangle Theory with Geometry and Applications*, arXiv:1501.03053 (first public arXiv posting 2015-01-09), *Foundations of Computational Mathematics* **15** (2015), 681--713. https://arxiv.org/abs/1501.03053. The publicly available manuscript lists 52A22 among its primary MSC classifications.
2. E. Hille, *Some geometric extremal problems*, *Journal of the Australian Mathematical Society* **6** (1966), 122--128. https://doi.org/10.1017/S1446788700004067.
3. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (2013). https://arxiv.org/abs/1301.1360.
4. S. R. Finch and A. J. Jones, *Random Spherical Triangles*, arXiv:1009.5329 (first public 2010-09-27). https://arxiv.org/abs/1009.5329.
5. H. Le, *Random spherical triangles II: Shape densities*, *Advances in Applied Probability* **21** (1989), 581--594. https://doi.org/10.2307/1427637. [Abstract available; complete text unavailable for a definitive implication comparison.]
6. R. E. Miles, *Isotropic Random Simplices*, *Advances in Applied Probability* **3** (1971), 353--382. https://doi.org/10.2307/1426176. [Abstract available; complete text unavailable.]
7. A. Akopyan, H. Edelsbrunner, and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-Sphere*, arXiv:2007.07783 (2020), concerning spherical random-polytope expectations and decomposition. https://arxiv.org/abs/2007.07783.
