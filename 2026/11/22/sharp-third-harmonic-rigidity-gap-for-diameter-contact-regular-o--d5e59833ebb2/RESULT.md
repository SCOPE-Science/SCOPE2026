# Sharp third-harmonic rigidity gap for diameter-contact regular odd polygons

## Finding
For every odd integer \(n\ge5\), the unweighted first-order response matrix of the \(n\) sides and \(n\) unit-diameter chords of a unit-diameter regular Euclidean \(n\)-gon has precisely three zero singular values, corresponding to planar rigid motions. Its smallest positive singular value \(\sigma_n\) obeys
\[
\lim_{n\to\infty,\ n\text{ odd}} n\sigma_n=\pi\sqrt{25-\sqrt{369}}=7.55984130546\ldots.
\]
For all sufficiently large odd \(n\), its weakest positive directions lie exclusively in the conjugate Fourier modes \(m=3\) and \(m=n-3\). Thus the exact sharp linearized error-to-motion inequality \(\lVert T_nv\rVert_2\ge\sigma_n\operatorname{dist}_2(v,\mathcal R_n)\), where \(\mathcal R_n\) denotes infinitesimal translations and rotation, has constant of order \(1/n\), with the displayed leading coefficient.

## Assumptions and scope
Let \(n\ge5\) be odd, \(k=(n-1)/2\), \(x=\pi/n\), and \(R=1/(2\cos(x/2))\). Define the vertices in cyclic order by \(p_j=R(\cos(2jx),\sin(2jx))\) for \(j\in\mathbb Z/n\mathbb Z\). The \(n\) pairs \(\{j,j+k\}\) are all distinct undirected edges; they are precisely the unit-length diameter contacts. All other vertex distances are strictly less than one. The \(n\) polygon sides have common length \(2R\sin x\).

The linear map \(T_n:(\mathbb R^2)^n\to\mathbb R^{2n}\) sends vertex velocities \(v=(v_0,\ldots,v_{n-1})\) to the directional derivatives of the \(n\) side lengths \(\lVert p_{j+1}-p_j\rVert\), followed by the derivatives of the \(n\) diametral lengths \(\lVert p_{j+k}-p_j\rVert\). Its matrix rows are unit edge directions, with negative and positive copies at the two endpoints. No scaling, quotient-row convention, weighting of chords, or common-side-length variable is used. Both spaces carry their standard Euclidean norms. Define \(\sigma_n>0\) to be the least positive singular value of \(T_n\), including multiplicity. The limit and frequency-selection statement is only for odd orders tending to infinity; it does not assert a finite universal onset index.

## Proof
**1. Local-coordinate Fourier blocks.** Identify the plane with \(\mathbb C\), and express each real velocity as \(v_j=e^{2ijx}(a_j+ib_j)\) with real radial and tangential components \(a_j,b_j\). Orthogonality of the pointwise rotations preserves input norms. For a chord joining vertices \(j\) and \(j+s\), direct scalar projection of the velocity difference onto the unit chord vector gives
\[
\delta\ell_{s,j}=\sin(sx)(a_j+a_{j+s})+\cos(sx)(b_{j+s}-b_j).
\]
Apply the unitary discrete Fourier transform to the two real component sequences and to both output sequences. For a complex Fourier frequency \(m\in\{0,\ldots,n-1\}\), remove the irrelevant phase \(e^{imsx}\) from its output. The resulting complex \(2\times2\) block is unitarily equivalent, by multiplying the tangential input by \(i\), to the real matrix
\[
M_{n,m}=2\begin{pmatrix}
\sin x\cos(mx)&-\cos x\sin(mx)\\
\cos(x/2)\cos(kmx)&-\sin(x/2)\sin(kmx)
\end{pmatrix}.
\]
Consequently the union, counting complex Fourier multiplicities, of the singular spectra of these matrices is exactly the full real singular spectrum of \(T_n\). The conjugate frequencies \(m,n-m\) have equal spectra. Here and below \(k=(n-1)/2\).

**2. Exactly three infinitesimal motions.** Put \(A_{n,m}=M_{n,m}/2\), \(\alpha=mx\), \(\beta=\alpha/2\), \(g=\cos(x/2)\), and \(h=\sin(x/2)\). Trigonometric addition identities give, for \(1\le m\le k\),
\[
|\det A_{n,m}|=\begin{cases}
2g\cos\beta\,(\sin^2\beta-h^2),&m\text{ odd},\\
2g\sin\beta\,(g^2-\sin^2\beta),&m\text{ even}.
\end{cases}
\]
For odd \(m\ge3\), the first expression is positive because \(\beta>x/2\) and both angles lie in \((0,\pi/4]\). For even \(m\ge2\), the second is positive because \(g^2>\sin^2\beta\) when \(n\ge5\) and \(\beta\le\pi/4\). Frequency \(m=1\) has rank one (the determinant vanishes), as does \(m=n-1\); their null directions together are the two translations. Frequency \(m=0\) has rank one and its null vector corresponds to uniform tangential velocity, hence rotation. All other blocks have rank two. Thus \(\ker T_n=\mathcal R_n\) has dimension exactly three.

**3. Fixed-frequency asymptotics.** When a fixed odd \(m\ge3\) is kept while odd \(n\to\infty\), a possible sign change of the second row gives
\[
\frac{M_{n,m}}{2x}\longrightarrow H_m=
\begin{pmatrix}1&-m\\m/2&-1/2\end{pmatrix}.
\]
At \(m=3\), the smaller squared singular value of \(H_3\) equals \((25-\sqrt{369})/4\), since \(\lVert H_3\rVert_F^2=25/2\) and \(|\det H_3|=4\). Therefore
\[
\lim_{n\to\infty,\ n\text{ odd}}\frac{s_{\min}(M_{n,3})}{x}
=\sqrt{25-\sqrt{369}}.
\]
For each fixed even \(m\ge2\), the lower row of \(A_{n,m}\) tends, up to sign, to \((1,0)\) and \(|\det A_{n,m}|\sim mx\); therefore \(s_{\min}(M_{n,m})/x\to2m\ge4\). For each fixed odd \(m\ge5\), the determinant/Frobenius estimate gives
\[
\lim_{n\to\infty}\frac{s_{\min}(M_{n,m})}{x}=2s_{\min}(H_m)
\ge\frac{2(m^2-1)}{\sqrt{5(m^2+1)}}\ge\frac{48}{\sqrt{130}}>\sqrt{25-\sqrt{369}}.
\]
The nonzero singular value in frequency \(m=1\) divided by \(x\) tends to \(\sqrt{10}>\sqrt{25-\sqrt{369}}\); the positive singular value at frequency zero stays bounded away from zero as \(x\to0\).

**4. Exclusion of frequencies escaping to infinity.** The comparisons above must be uniform because a candidate minimum could have frequency depending on \(n\). By conjugation it is enough to take \(2\le m\le k\), so \(0<\alpha=mx<\pi/2\). The inequalities \(\sin t\ge2t/\pi\) for \(0\le t\le\pi/2\), \(h\le x/2\), and \(\cos(x/2)\ge\cos(\pi/10)\) show that the displayed determinant formulas yield universal constants \(c_1,c_2>0\) such that
\[
|\det A_{n,m}|\ge
\begin{cases}c_1\alpha^2,&m\ge3\text{ odd},\\c_2\alpha,&m\ge2\text{ even}.
\end{cases}
\]
Indeed in the odd case \(\sin^2(\alpha/2)-h^2\ge\alpha^2/\pi^2-x^2/4\ge(1/\pi^2-1/36)\alpha^2>0\), as \(m\ge3\). The odd-frequency matrix has Frobenius norm \(\lVert A_{n,m}\rVert_F\le C\alpha\): its upper row is bounded by \((x,\alpha)\), and its lower row, since \(m\) is odd, by \((\alpha/2,x/2)\). For even frequencies \(\lVert A_{n,m}\rVert_F\le C\), with \(g^2-\sin^2(\alpha/2)\) uniformly positive. For any invertible \(2\times2\) matrix, \(s_{\min}(A)=|\det A|/s_{\max}(A)\ge|\det A|/\lVert A\rVert_F\). It follows that
\[
s_{\min}(M_{n,m})\ge c\,\alpha=c m x
\]
for a universal \(c>0\) and all nonrigid \(2\le m\le k\). Hence \(s_{\min}(M_{n,m})/x\to\infty\) whenever \(m\to\infty\), eliminating every escaping-frequency sequence. Since the fixed-frequency minimum is strictly at \(m=3\), compactness of the remaining finite set of frequencies implies that, for all sufficiently large odd \(n\), the smallest positive singular value is exactly \(s_{\min}(M_{n,3})\), attained only at \(m=3,n-3\). Multiplication by \(n x=\pi\) establishes the announced constant. \(\square\)

## Verification
A standalone Python standard-library checker is supplied as `verify.py`. Run `python3 verify.py` from the extracted package. Its independent direct-coordinate Jacobian and cyclic Fourier formula agree for odd orders \(5,7,9,11,13\); it tests determinant identities for several orders, numerically selects the third mode over odd orders \(7\) to \(301\), and checks convergence through order \(1601\). The test reports 233 passing finite assertions and the limiting coefficient 7.559841305462. These calculations support but do not replace the proof of the limit or the eventual frequency selection.

## Relationship to prior work
Reinhardt's classical extremal theorem shows that regular odd polygons attain the maximal perimeter subject to unit diameter; that global extremal statement is not new. Guo and Luo, *Reinhardt's Maximum-Perimeter Polygon Problem at n=16, 32, and 64: Computer-Assisted Proof Candidates* (first posted 8 August 2026, arXiv:2608.08001), formulate quantitative near-regularity and Fourier/Dirichlet controls for saturated difference-body codes in even powers of two. They do not calculate the Euclidean singular spectrum of the separate side-and-diameter length derivative on all odd regular polygons. Their global claims are explicitly styled proof candidates, not independently established here. Mulansky and Potschka, *A zonogon approach for computing small convex polygons of maximum perimeter* (arXiv:2404.01841; article online 21 June 2025), give a zonogon and diameter-graph optimization framework, not the present sharp spectral limit. Ayala Hoffmann and Ayala Coppola, *First Order Geometry of Equilateral Small Polygons* (17 November 2026, arXiv:2611.23066), develop a qualitative first-order local-maximality criterion and inspect selected even polygons; their Jacobian includes an additional common-side-length variable and they do not prove the specified odd regular rigidity-gap asymptotic. This later work provides a relevant comparison, but not a theorem implying the present spectral asymptotic. Fourier block diagonalization of circulant geometric operators is classical; the new proposition is the specific sharp third-mode, all-odd-order conditioning law and its exact constant.

## Limitations
This is a local linearized statement about 2n selected edge-distance outputs in the ordinary Euclidean norm. It is not a bound on nonlinear perturbations with arbitrary amplitude; such consequences require controlling quadratic Taylor remainders. It is neither a new global optimizer classification nor a result for even-sided polygons, all graph edge sets, or arbitrary weightings. The exact finite threshold at which the third harmonic becomes uniquely weakest is not proved here. Novelty is provisional pending specialist examination of the broader spectral-framework literature; no independent mathematical audit is claimed. The standalone numerical tests do not certify the asymptotic theorem.

## References
- J. Guo and Y. Luo, *Reinhardt's Maximum-Perimeter Polygon Problem at n=16, 32, and 64: Computer-Assisted Proof Candidates*, arXiv:2608.08001 (first posted 2026-08-08), https://arxiv.org/abs/2608.08001.
- B. Mulansky and A. Potschka, *A zonogon approach for computing small convex polygons of maximum perimeter*, arXiv:2404.01841 (first posted 2024-04-03); Math. Program. (online 2025-06-21), https://doi.org/10.1007/s10107-025-02244-x.
- J. Ayala Hoffmann and T. Ayala Coppola, *First Order Geometry of Equilateral Small Polygons*, arXiv:2611.23066 (first posted 2026-11-17), https://arxiv.org/abs/2611.23066.
- K. Reinhardt, *Extremale Polygone gegebenen Durchmessers* (1922), classical perimeter bounds, as quoted and referenced by Guo–Luo and Mulansky–Potschka.
