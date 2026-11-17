# Sharp six-sample reconstruction of real quadratic spherical harmonics from two great circles

## Finding
Let \(\sigma\) be normalized area measure on the unit sphere \(\mathbb S^2\), and let \(\mathcal H_2\) denote the five-dimensional real space of homogeneous quadratic spherical harmonics. For two unoriented great circles \(C_+,C_-\), write \(t=|n_+\cdot n_-|\in[0,1]\) for the absolute inner product of their unit normals. On each circle choose **any** equispaced triple (angles separated by \(2\pi/3\)); let \(p_1,\ldots,p_6\) be the six observations, counted with multiplicity if two observation sites coincide. Put
\[
Q_t(f)=\frac16\sum_{j=1}^{6}|f(p_j)|^2,\qquad
\lambda(t)=\inf_{0\ne f\in\mathcal H_2}\frac{Q_t(f)}{\|f\|_{L^2(\sigma)}^2}.
\]
The number \(\lambda(t)\) is independent of the two in-circle rotation phases. It has the exact formula
\[
\boxed{\lambda(t)=\min\left\{\frac{15(1-t)}{16},\;
\frac{45t^2+55-\sqrt{(45t^2-55)^2+300t^2}}{64}\right\}.}
\]
In particular, over **all** such two-triple sampling layouts,
\[
\boxed{\max_{0\le t\le1}\lambda(t)=\frac5{12},\qquad
\text{uniquely when }t=\frac59.}
\]
Thus the optimal acute angle between the two planes (or their normals) is \(\arccos(5/9)\), not a right angle. At this angle, the optimal lower sampling inequality is
\[
\frac16\sum_{j=1}^6|f(p_j)|^2\ge\frac5{12}\|f\|_{L^2(\sigma)}^2,
\qquad f\in\mathcal H_2.
\]
The constant cannot be raised within this layout family. Choose coordinates with
\[
n_\pm=\left(\frac{\sqrt7}{3},\;\pm\frac{\sqrt2}{3},\;0\right).
\]
Every nonzero equality case lies precisely in the two-dimensional space
\[
\boxed{\mathcal E=\operatorname{span}_{\mathbb R}\big\{xz,\;8x^2-7y^2-z^2\big\}.}
\]
The same configuration enjoys the **sharp spectral stability remainder**
\[
Q_{5/9}(f)-\frac5{12}\|f\|_{L^2(\sigma)}^2
\ge \frac59\operatorname{dist}_{L^2(\sigma)}(f,\mathcal E)^2.
\]
Equality in this remainder occurs exactly for \(f\in\mathcal E+\operatorname{span}_{\mathbb R}\{xy\}\). When \(t=0\) (perpendicular planes) or \(t=1\) (coincident planes), one has \(\lambda(t)=0\) and stable recovery fails.

## Assumptions and scope
The sphere has radius one; all measures are probability measures. A quadratic harmonic is \(f_A(u)=u^{\mathsf T}Au\) for a real symmetric \(3\times3\) matrix \(A\) with \(\operatorname{tr}A=0\). Its global norm satisfies
\[
\|f_A\|_{L^2(\sigma)}^2=\frac2{15}\operatorname{tr}(A^2).
\]
The observation measure is the equally weighted six-term multiset obtained by choosing three equally spaced points on **each** great circle; phases need not be coordinated. The optimization is over the relative angle of these two circles and their phases, not over arbitrary six-point sets, non-equal observation weights, or all spherical polynomials through degree two. The planes are unoriented, so every configuration is equivalent by a rotation/reflection and a normal-sign choice to a parameter \(t\in[0,1]\).

## Proof
**1. Exactly three values reproduce the continuous circle energy.** Parametrize a great circle by \(u(\phi)=v\cos\phi+w\sin\phi\) for orthonormal \(v,w\). Every quadratic restriction \(f_A(u(\phi))\) is a trigonometric polynomial supported at frequencies \(0,\pm2\). Consequently \(|f_A(u(\phi))|^2\) is supported at frequencies \(0,\pm2,\pm4\). Averaging at any three equally spaced phases kills each nonconstant frequency. Therefore
\[
\frac13\sum_{j=0}^2 |f_A(u(\phi_0+2\pi j/3))|^2
=\frac1{2\pi}\int_0^{2\pi}|f_A(u(\phi))|^2\,d\phi.
\]
This equality holds for every rotation phase and for every \(A\); thus \(Q_t\) equals the average of the two continuous circle energies, exactly, not asymptotically.

**2. The sampling Gram matrix.** Let \(n_\pm=(c,\pm s,0)\), with \(c=\sqrt{(1+t)/2}\) and \(s=\sqrt{(1-t)/2}\). The five real functions
\[
 e_1=\sqrt{15}\,xy,\quad e_2=\sqrt{15}\,xz,\quad
 e_3=\sqrt{15}\,yz,\quad
 e_4=\frac{\sqrt{15}}2(x^2-y^2),\quad
 e_5=\frac{\sqrt5}2(x^2+y^2-2z^2)
\]
are an orthonormal basis of \(\mathcal H_2\) in \(L^2(\sigma)\). For a uniform point \(u\) on the circle normal to \(n\), put \(P=I-nn^{\mathsf T}\). Its fourth moments obey
\[
\mathbb E[(u^{\mathsf T}Au)(u^{\mathsf T}Bu)]
=\frac{\operatorname{tr}(PA)\operatorname{tr}(PB)+2\operatorname{tr}(PAPB)}8.
\]
Substituting the two normals and averaging, the quadratic form \(Q_t\) in the displayed orthonormal basis has Gram matrix
\[
G(t)=\begin{pmatrix}
\frac{45}{32}(1-t^2)&0&0&0&0\\
0&\frac{15}{16}(1-t)&0&0&0\\
0&0&\frac{15}{16}(1+t)&0&0\\
0&0&0&\frac{45t^2}{32}&-\frac{5\sqrt3t}{32}\\
0&0&0&-\frac{5\sqrt3t}{32}&\frac{55}{32}
\end{pmatrix}.
\]
The last two eigenvalues are
\[
\lambda_\pm(t)=\frac{45t^2+55\pm\sqrt{(45t^2-55)^2+300t^2}}{64}.
\]
The scalar eigenvalues \(45(1-t^2)/32\) and \(15(1+t)/16\) are each at least \(15(1-t)/16\). The displayed formula for \(\lambda(t)\) follows.

**3. Sharp angular optimization.** The scalar branch \(b(t)=15(1-t)/16\) strictly decreases on \([0,1]\). The other branch \(\lambda_-(t)\) strictly increases there. Indeed, setting \(v=t^2\), the smaller root \(\ell(v)\) satisfies
\[
\ell^2-\frac{45v+55}{32}\ell+\frac{75v}{32}=0,
\qquad
\ell'(v)=\frac{75-45\ell(v)}{45v+55-64\ell(v)}>0.
\]
Here \(0\le\ell(v)\le45v/32\le45/32<5/3\), so the numerator is positive; the denominator is positive because it equals \(32\) times the strict gap between the two eigenvalues of the last block. At the endpoints, \(\lambda_-(0)=0<b(0)\) and \(\lambda_-(1)=5/4>b(1)=0\). There is exactly one crossing. Substituting \(b(t)\) into the characteristic polynomial of the last block yields
\[
\det\big(G_{\{4,5\}}(t)-b(t)I\big)=\frac{75}{512}(t+1)^2(9t-5).
\]
Thus the unique crossing and maximizer is \(t=5/9\), with \(b(5/9)=5/12\).

**4. Equality and stability.** At \(t=5/9\) the ordered spectrum is
\[
\frac5{12},\quad\frac5{12},\quad\frac{35}{36},\quad
\frac{35}{24},\quad\frac{125}{72}.
\]
The two smallest eigendirections are \(e_2\) and \(5\sqrt3\,e_4+e_5\), which equal the stated coordinate polynomials up to nonzero factors. The next eigenvalue is \(35/36\), so the exact gap above the minimum is \(35/36-5/12=5/9\), giving the stability inequality and equality classification. The endpoint degeneracies follow directly from \(\lambda(0)=\lambda(1)=0\).

## Verification
Run `python3 verify.py` from the directory containing that standalone source file (requires SymPy). The checker constructs the six observations at five exact angles with several independent in-circle phases, computes the complete \(5\times5\) Gram matrix directly from the sample values, derives it independently from the fourth-moment projection tensor, and confirms the optimal spectrum, equality eigenspace, and gap using exact radicals and rationals. Its terminal marker is `ALL_TWO_GREAT_CIRCLE_SAMPLING_CHECKS_OK`. The infinite-angle optimization and equality classification are proved in the preceding argument, not inferred from a finite search.

## Relationship to prior work
The spherical Slepian theory of Simons, Dahlen, and Wieczorek (2006), particularly its region-integral eigenvalue problem in Section 4, supplies the larger conceptual framework of bandlimited concentration. That treatment integrates over spherical regions of positive area; it does not provide the singular six-point observation spectrum or optimize the separation of two sampling great circles. McEwen and Price (2015), particularly Section III and their Funk–Radon harmonic multipliers, analyze **integrals** over great circles and full angular families of those integrals, rather than complete function traces on just two circles or two three-point samplings. Ivanov and Petrushev (2014) address stable irregular sampling and reconstruction for much larger spherical-polynomial spaces, but not this six-observation, two-triple sharp angular design. The circle quadrature identity and spherical tensor moments are elementary tools; novelty is not asserted for those components in isolation. Literature comparisons found no directly subsuming theorem, but unpublished or unindexed equivalents remain possible.

## Limitations
The optimality is *only within the equal-weight two-equilateral-triple family* and the real, exact degree-two harmonic subspace. There is no claim of global optimality among all six-node spherical designs, arbitrary nonuniform weights, higher-degree harmonics, functions with degrees zero or one added, noisy nonlinear recovery, or higher-dimensional spheres. Possible equivalent older finite-frame or optimal-experimental-design formulas have not been exhaustively excluded. The finding is not independently audited.

## References
1. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral Concentration on a Sphere*, SIAM Review **48** (2006), 504–536, doi:10.1137/S0036144504445765. Lawful author reprint: https://geoweb.princeton.edu/people/simons/PDF/reprints/SIAM-2006.pdf (public electronic date August 1, 2006).
2. J. D. McEwen, M. A. Price, *Scale-discretised ridgelet transform on the sphere*, arXiv:1510.01595, initially posted October 6, 2015. https://arxiv.org/abs/1510.01595.
3. K. Ivanov, P. Petrushev, *Irregular sampling of band-limited functions on the sphere*, Applied and Computational Harmonic Analysis **37** (2014), 545–562, doi:10.1016/j.acha.2014.05.001. https://doi.org/10.1016/j.acha.2014.05.001.
