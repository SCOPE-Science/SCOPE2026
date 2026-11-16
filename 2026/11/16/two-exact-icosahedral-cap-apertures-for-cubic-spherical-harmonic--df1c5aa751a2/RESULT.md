# Two exact icosahedral cap apertures for cubic spherical-harmonic Parseval sampling

## Finding
Let \(\sigma\) be normalized surface-area probability on \(S^2\). For the twelve vertices \(I\) of a regular icosahedron, let \(\sigma_{u,c}\) be normalized area probability on the cap \(C(u,c)=\{x\in S^2:u\cdot x\ge c\}\), where \(0<c<1\). Define the **mixture**, not the set-theoretic union,
\[
\mu_c=\frac1{12}\sum_{u\in I}\sigma_{u,c},\qquad
\frac{d\mu_c}{d\sigma}(x)=\frac1{6(1-c)}\sum_{u\in I}{\mathbf{1}}_{C(u,c)}(x).
\]
Let \(\mathcal H_3\) be the seven-dimensional complex space of pure degree-three spherical harmonics, with inner product \(\langle q,r\rangle_\sigma=\int q\overline r\,d\sigma\). Define \(G_c\) by \(\langle G_cq,r\rangle_\sigma=\int q\overline r\,d\mu_c\). Set
\[
a(c)=\frac{c(1+c)(429c^4-390c^2+65)}{208}.
\]
**Theorem.** For every \(0<c<1\), the complete spectrum of \(G_c\) is
\[
\operatorname{spec}(G_c)=\{1-a(c)\text{ (multiplicity 4)},\quad 1+\tfrac43a(c)\text{ (multiplicity 3)}\}.
\]
Its two eigenspaces are independent of \(c\). The first consists of cubics vanishing at every vertex of \(I\). The second is its \(L^2(\sigma)\)-orthogonal complement. Thus \(G_c=\mathrm{Id}\) exactly at the two **positive** thresholds
\[
 c_\pm=\sqrt{\frac{195\pm26\sqrt{15}}{429}},\quad
 c_-\approx0.468848793470714,\qquad c_+\approx0.830223896278567.
\]
The two sharp frame bounds are \(A(c)=\min\{1-a(c),1+4a(c)/3\}\) and \(B(c)=\max\{1-a(c),1+4a(c)/3\}\). In the successive intervals \((0,c_-),(c_-,c_+),(c_+,1)\), the least-observed eigenspaces have dimensions \(4,3,4\), respectively. At either equality aperture the whole seven-dimensional space is the equality eigenspace. As \(c\uparrow1\),
\[
 A(c)\sim\frac{21}{2}(1-c),\quad B(c)\to\frac73,\quad
 \kappa(c)=\frac{B(c)}{A(c)}\sim\frac{2}{9(1-c)}.
\]

## Assumptions and scope
A standard concrete icosahedron has antipodal vertices \(I=\{\pm v_1,\dots,\pm v_6\}\), where, writing \(\varphi=(1+\sqrt5)/2\) and \(s=\sqrt{1+\varphi^2}\),
\[
 (v_1,\dots,v_6)=s^{-1}\big((0,1,\varphi),(0,1,-\varphi),(1,\varphi,0),(1,-\varphi,0),(\varphi,0,1),(\varphi,0,-1)\big).
\]
The caps at the two Parseval thresholds overlap. Repeated coverage is weighted in \(\mu_c\); the theorem does **not** identify \(\mu_c\) with uniform area measure on the union. Sampling on \(\mathcal H_3\) is exact in the sense \(\|q\|^2_{L^2(\mu_c)}=\|q\|^2_{L^2(\sigma)}\) for every cubic at precisely the two thresholds.

## Proof
**1. The icosahedral five-design.** For any fixed vertex, the other eleven consist of one antipode and five each with dot product \(\pm1/\sqrt5\). By the spherical-harmonic addition theorem, the squared norm of the mean of all degree-\(\ell\) harmonics vanishes if the average of \(P_\ell(u\cdot v)\) over ordered vertex pairs vanishes. For odd \(\ell\) this follows from antipodality. For \(\ell=2,4\) the average is \([1+5P_\ell(1/\sqrt5)]/6=0\), since both Legendre values equal \(-1/5\). Thus \(I\) is a spherical five-design.

**2. The point-sampling spectrum.** The reproducing kernel of \(\mathcal H_3\), for normalized area measure, is \(K_3(u,v)=7P_3(u\cdot v)\), with \(P_3(t)=(5t^3-3t)/2\). Since cubic harmonics are odd, the nonzero eigenvalues of the twelve-point sampling Gram operator \(G_{\mathrm{pt}}\) are the nonzero eigenvalues of the six-by-six matrix
\[
 M=\frac76\left(I_6+\frac{S}{\sqrt5}\right),\qquad
 S_{ij}=\begin{cases}0&i=j,\\\sqrt5P_3(v_i\cdot v_j)&i\ne j.\end{cases}
\]
For the displayed representatives, all off-diagonal entries of \(S\) equal \(\pm1\), and direct multiplication gives \(S^2=5I_6\), \(\operatorname{tr}S=0\). Hence its eigenvalues are \(\sqrt5\) and \(-\sqrt5\), each of multiplicity three. It follows that \(G_{\mathrm{pt}}\) on the seven-dimensional harmonic space has eigenvalues \(0\) (multiplicity four) and \(7/3\) (multiplicity three). The four-dimensional vanishing subspace is also described in Hitchin's 2007 Proposition 1; its existence is not asserted as new.

**3. Cap smoothing.** Let \(F_c\) send a function to its average over the cap centered at \(u\). Funk--Hecke gives \(F_cY_\ell=a_\ell(c)Y_\ell\), where \(a_\ell(c)=(1-c)^{-1}\int_c^1P_\ell(t)\,dt\). Products \(q\overline r\), for \(q,r\in\mathcal H_3\), contain only even harmonic degrees \(0,2,4,6\). The icosahedral five-design kills the averaged terms of degrees two and four; the degree-zero term is the global integral. Consequently, for all such \(q,r\),
\[
 \langle G_cq,r\rangle_\sigma=\langle q,r\rangle_\sigma+a_6(c)\big(\langle G_{\mathrm{pt}}q,r\rangle_\sigma-\langle q,r\rangle_\sigma\big),
 \quad G_c=I+a_6(c)(G_{\mathrm{pt}}-I).
\]
Integrating \(P_6(t)=(231t^6-315t^4+105t^2-5)/16\) gives \(a_6(c)=a(c)\) above. Substituting the two point-sampling eigenvalues yields the claimed complete spectrum and fixed eigenspaces.

**4. Parseval thresholds, order, and boundary.** On \((0,1)\), \(a(c)=0\) exactly when \(429c^4-390c^2+65=0\), whose two roots in \(c^2\) are \((195\pm26\sqrt{15})/429\). Their simple sign changes give the \(4,3,4\) least-eigenspace pattern. Both branches are strictly positive for \(0<c<1\) because each \(\mu_c\) has positive density on an open cap and a nonzero analytic harmonic cannot vanish on an open set. Finally, \(P_6'(1)=21\), so \(a_6(c)=1-21(1-c)/2+O((1-c)^2)\), yielding the condition-number law.

## Verification
The standalone `check_icosahedral_cubic.py` checks the exact six-by-six conference identity, Legendre-polynomial factorization, two roots, degree-two and degree-four design moments, and point-sampling eigenvalues in exact symbolic arithmetic. It also independently integrates the complete seven-by-seven cap Gram matrix using rotated Gauss--Legendre and periodic azimuth quadrature at seven distinct thresholds. For this polynomial integrand the employed quadrature is algebraically exact in exact arithmetic; floating-point error in the numerical comparison is below \(5\times10^{-15}\) in the recorded run. Invoke `python check_icosahedral_cubic.py` with NumPy and SymPy installed. These checks corroborate, rather than replace, the general proof.

## Relationship to prior work
Hitchin (2007, Proposition 1) already establishes the four-dimensional space of cubic harmonics vanishing at icosahedral vertices. Xiao and Zhuang (2023) analyze spherical-design quadrature and spherical tight framelets, explicitly using the icosahedron as a five-design. Li and Chen (2024) construct cap subdesign quadrature on a **single** cap by moving design points. The present statement instead concerns the **mixture of twelve area-uniform caps**, its complete degree-three Gram spectrum and the **two exact nonhemispherical apertures**; none of these prior statements, as inspected, asserts that spectral or aperture classification. The classical Funk--Hecke and addition formulas are used as known tools.

## Limitations
The aperture classification is for equal-weight, equal-radius cap mixtures at exactly the twelve icosahedral centers and pure degree-three spherical harmonics. It is not a classification for arbitrary centers, unions without multiplicity, other harmonic degrees, or pointwise sampling with finitely many locations inside each cap. The theorem is analytically proved but has no independent external audit; historical-priority searches are provisional and cannot rule out an equivalent unpublished or differently titled result. In particular, the point-sampling nullspace itself is known.

## References
1. Y. Xiao and X. Zhuang, *Spherical Framelets from Spherical Designs*, arXiv:2303.05365, first posted 2023-03-09; SIAM J. Imaging Sci. 16 (2023), 2072--2104. https://arxiv.org/abs/2303.05365
2. N. Hitchin, *Spherical harmonics and the icosahedron*, arXiv:0706.0088 (2007), especially Proposition 1. https://arxiv.org/abs/0706.0088
3. C. Li and X. Chen, *Spherical Designs for Approximations on Spherical Caps*, SIAM J. Numer. Anal. 62 (2024), 2506--2528, DOI:10.1137/23M1555417. https://doi.org/10.1137/23M1555417
4. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, SIAM Rev. 48 (2006), 504--536; arXiv:math/0408424. https://arxiv.org/abs/math/0408424
