# Sharp hemispheric latitude-ring sampling for a single spherical-harmonic degree

## Finding

For an integer \(\ell\ge1\), let \(\mathcal H_\ell\) be the complex \((2\ell+1)\)-dimensional space of spherical harmonics of **exactly** degree \(\ell\), with the surface-area \(L^2(S^2)\) norm. The smallest number of distinct absolute latitude levels \(|z|\) that can support any positive-weighted tight point-sampling frame on \(\mathcal H_\ell\) is
\[
\boxed{r_\ell=\left\lceil(\ell+1)/2\right\rceil.}
\]
This lower bound applies to arbitrary longitudes and arbitrary strictly positive weights: any such tight frame has at least \(r_\ell\) distinct squared heights \(u=z^2\). It is attained using **only the open northern hemisphere**, with exactly \(r_\ell\) latitude circles and \(2\ell+1\) equally spaced longitudes per circle.

For a complete specification of the minimal separated-ring construction, let
\[
d\nu(u)=\frac{du}{2\sqrt u},\quad 0<u<1,
\qquad\int_0^1u^k\,d\nu(u)=\frac1{2k+1}.
\]
Choose \(r=r_\ell\) distinct nodes \(0<u_1<\cdots<u_r<1\) and positive weights \(w_i\) of total mass one. Place samples at heights \(z_i=\sqrt{u_i}\), with longitudes \(\phi_j=2\pi j/(2\ell+1)\), \(0\le j\le2\ell\). Then the exact identity
\[
\boxed{\|f\|_{L^2(S^2)}^2=\frac{4\pi}{2\ell+1}\sum_{i=1}^{r}\sum_{j=0}^{2\ell}w_i\left|f\!\left(\sqrt{1-u_i}\cos\phi_j,\sqrt{1-u_i}\sin\phi_j,\sqrt{u_i}\right)\right|^2}
\]
holds for every \(f\in\mathcal H_\ell\) **if and only if** the radial rule \(\sum_i w_ip(u_i)=\int p\,d\nu\) is exact for all polynomials of degree at most \(\ell\).

The complete latitude-and-weight classification at the minimum \(r\) has a parity distinction. Write \(\pi_n\) for the monic degree-\(n\) polynomial orthogonal for \(\nu\), with \(\pi_0=1\):
\[
\pi_n(u)=\frac{P_n^{(0,-1/2)}(2u-1)}{\binom{2n-1/2}{n}},
\]
where \(P_n^{(\alpha,\beta)}\) is a standard Jacobi polynomial.

If \(\ell=2r-1\) is odd, the \(r\) distinct squared latitudes are **uniquely** the zeros of \(\pi_r\), and their positive quadrature weights are unique. If \(\ell=2r-2\) is even, the minimal designs form precisely the one-parameter family whose nodes are the zeros of
\[
\boxed{q_{r,c}(u)=\pi_r(u)+c\pi_{r-1}(u),\qquad -\frac{2r(2r-1)}{(4r-1)(4r-3)}<c<\frac{(2r-1)^2}{(4r-1)(4r-3)}.}
\]
The weights in each case are uniquely determined by polynomial interpolation and are positive. Choosing the latitude signs independently gives other constructions with the same diagonal properties; the displayed construction uses only positive heights. The classification describes separated equiangular rings or azimuthally averaged rings, not every possible arrangement of angular samples.

For example, \(\ell=1\) needs one ring at \(z=1/\sqrt3\). For \(\ell=2\), two equal-weight northern rings may be chosen at
\[
u_\pm=\frac13\pm\frac{2}{3\sqrt5},\qquad z_\pm=\sqrt{u_\pm},\qquad w_+=w_-=\frac12.
\]
This even-degree design is distinct from the Gaussian-Jacobi rule, illustrating the genuine family of minimizers.

## Assumptions and scope

The sphere is \(S^2=\{(x,y,z)\in\mathbb R^3:x^2+y^2+z^2=1\}\), with total area \(4\pi\). Spherical harmonics are complex-valued and are orthonormal with respect to the unnormalized surface-area measure. A positive sampling frame means a finite family of points \(\omega_s\in S^2\) with real weights \(a_s>0\) for which \(\sum_s a_s|f(\omega_s)|^2=A\|f\|^2\) for all \(f\in\mathcal H_\ell\), with \(A>0\). The theorem's global lower bound counts the number of **distinct absolute heights** among all sampling points, not the total number of points; the construction has \(r(2\ell+1)\) points and does not claim globally minimal cardinality. For classification of the separated construction, all radial nodes lie in \((0,1)\); poles and equator are excluded there.

## Proof

**1. Necessary radial moment condition for any positive tight sampler.** Let \(Y_\ell^m\), \(-\ell\le m\le\ell\), be the standard orthonormal spherical harmonics. For \(u=z^2\), their squared magnitudes depend on the point only through \(u\):
\[
F_m(u)=|Y_\ell^m(\arccos\sqrt u,0)|^2
=\frac{2\ell+1}{4\pi}\frac{(\ell-m)!}{(\ell+m)!}(1-u)^m[P_\ell^{(m)}(\sqrt u)]^2,
\quad 0\le m\le\ell.
\]
Here \(P_\ell\) is the Legendre polynomial; the superscript in \(P_\ell^{(m)}\) denotes an ordinary derivative, rather than an associated-Legendre normalization. Because the derivative has parity \(\ell-m\), its square is a polynomial in \(u\), making \(F_m\) a polynomial of degree at most \(\ell\). Moreover,
\[
P_\ell^{(m)}(1)=\frac{(\ell+m)!}{2^m m!(\ell-m)!}\ne0.
\]
Thus \(F_m\) has a zero of *exactly order* \(m\) at \(u=1\). The \(\ell+1\) polynomials \(F_0,\ldots,F_\ell\) are therefore linearly independent and form a basis of all polynomials of degree at most \(\ell\).

For an arbitrary tight sampler with weights \(a_s\), the spherical addition formula yields
\[
\sum_{m=-\ell}^\ell |Y_\ell^m(\omega)|^2=(2\ell+1)/(4\pi),
\]
so summing the diagonal frame identities shows \(A=(\sum_s a_s)/(4\pi)\). Divide weights by their total mass. The diagonal identities become
\[
\sum_s\frac{a_s}{\sum_t a_t}F_m(z_s^2)=\frac1{4\pi}=\int_0^1F_m(u)\,d\nu(u).
\]
Since the \(F_m\) form a polynomial basis, grouping points with identical squared heights gives a positive quadrature rule for \(\nu\), exact through degree \(\ell\).

**2. Sharp lower bound on absolute latitudes.** Suppose that quadrature uses \(s\) distinct squared heights \(u_i\) with positive mass. If \(2s\le\ell\), the polynomial \(Q(u)=\prod_{i=1}^s(u-u_i)^2\) has degree at most \(\ell\), vanishes at every node, and has strictly positive integral against \(\nu\). Exactness would say that this positive integral is zero, a contradiction. Hence \(2s>\ell\), or \(s\ge\lceil(\ell+1)/2\rceil\).

**3. Construction and radial sufficiency.** For \(r=\lceil(\ell+1)/2\rceil\), Gaussian quadrature for the positive measure \(\nu\) has \(r\) nodes in \((0,1)\), strictly positive weights, and exactness through degree \(2r-1\ge\ell\). Use these nodes at positive heights as in the finding. Write \(f=\sum_{m=-\ell}^\ell c_mY_\ell^m\). On each ring, Fourier orthogonality of \(2\ell+1\) equally spaced azimuths cancels every cross term, because \(0<|m-m'|\le2\ell\) is never a multiple of \(2\ell+1\). The surviving diagonal coefficient is \(4\pi\sum_iw_iF_{|m|}(u_i)=1\). This proves the exact frame identity. Conversely, its diagonal part forces radial polynomial exactness, proving the stated if-and-only-if condition.

**4. Classification at the sharp number of rings.** For any positive \(r\)-point rule exact through degree \(\ell\), let \(q(u)=\prod_i(u-u_i)\), monic of degree \(r\). Testing the exact rule against \(q(u)p(u)\), for every polynomial \(p\) of degree at most \(\ell-r\), shows \(\int qp\,d\nu=0\). If \(\ell=2r-1\), \(q\) is orthogonal to degrees at most \(r-1\), hence \(q=\pi_r\), and Gaussian weights are forced by interpolation. If \(\ell=2r-2\), \(q\) is orthogonal to degrees at most \(r-2\), hence \(q=\pi_r+c\pi_{r-1}\) for a unique real \(c\).

Conversely, if \(q\) has distinct roots in \((0,1)\) and has this orthogonality, define \(w_i=\int L_i(u)\,d\nu(u)\), where \(L_i\) are degree-\(r-1\) Lagrange cardinal polynomials. Division by \(q\) proves exactness through degree \(2r-2\). It also proves positivity, since \(w_i=\int L_i(u)^2\,d\nu(u)>0\) using exactness for \(L_i^2\).

The Jacobi endpoint formulas and interlacing of consecutive orthogonal polynomials establish that the roots of \(\pi_r+c\pi_{r-1}\) all lie strictly in \((0,1)\) exactly when
\[
-\frac{\pi_r(1)}{\pi_{r-1}(1)}<c<-\frac{\pi_r(0)}{\pi_{r-1}(0)}.
\]
Using \(\pi_n=P_n^{(0,-1/2)}(2u-1)/\binom{2n-1/2}{n}\) reduces these endpoints to the explicit interval in the finding. At either endpoint one root reaches \(0\) or \(1\), excluded from the specified open-latitude classification. This completes the all-degree proof.

## Verification

The standalone script `check_ring_sampling.py` uses exact symbolic Legendre polynomials to check the basis property in degrees \(1\) through \(10\), exact rational moment orthogonality and Jacobi interval endpoints for rules of up to six nodes, and directly assembled complex spherical-harmonic sampling Gram matrices in degrees \(1\) through \(10\). It additionally verifies the non-Gaussian equal-weight degree-two example. Run `python check_ring_sampling.py` with NumPy, SciPy and SymPy installed. The run produced `PURE_DEGREE_LATITUDE_PASS` and `PURE_DEGREE_LATITUDE_GRAM_PASS`. The proof above, not these finite tests, establishes the claims for every degree.

## Relationship to prior work

The spherical harmonic normalization and ordinary iso-latitude reconstruction framework are standard. Nafees, Khalid, Kennedy and McEwen (first arXiv version 2017-09-08) study stable placement of iso-latitude rings for the **whole low-pass band**, not tight restricted sampling for one degree. Elahi, Khalid, Kennedy and McEwen (2018) address spin-weighted low-pass sampling, again not the present pure-degree radial moment problem. Wieczorek and Meschede (2018) document general Gauss-Legendre latitude sampling with \(L+1\) rings for harmonics through degree \(L\). Classical Gaussian quadrature and Jacobi-polynomial theory are essential mathematical inputs, explicitly credited rather than claimed as discoveries. The new specific statement is the sharp **absolute-latitude count**, equivalence with the squared-latitude moment problem, and full parity-dependent classification of minimal positive ring rules. This does not assert a smaller global point count than established spherical sampling schemes.

## Limitations

The result applies to signals of **one exact spherical harmonic degree**, not a direct sum of several degrees. The sharp lower bound concerns distinct \(|z|\) values, not sample-point cardinality. Off-diagonal cancellation in the construction requires an equiangular rule with \(2\ell+1\) longitudes on each ring; arbitrary angular placements that merely satisfy the radial moment rule need not be tight. The minimal-rule classification assumes strictly interior squared latitudes and positive weights; equality at the displayed parameter endpoints changes the admissible geometry. Historical priority remains provisional because an equivalent single-degree cubature theorem may have been expressed in another notation.

## References

1. W. Nafees, Z. Khalid, R. A. Kennedy, J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations*, arXiv:1709.02497 (first version 2017-09-08), https://arxiv.org/abs/1709.02497.
2. M. A. Wieczorek, M. Meschede, *SHTools: Tools for Working with Spherical Harmonics*, Geochemistry, Geophysics, Geosystems 19 (2018), DOI:10.1029/2018GC007529, https://doi.org/10.1029/2018GC007529.
3. U. Elahi, Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling for Spin-s Functions on the Sphere*, arXiv:1809.01321 (first version 2018-09-05), https://arxiv.org/abs/1809.01321.
4. Classical Gauss-Jacobi quadrature, interlacing and quasi-orthogonal polynomial theory (standard background; no new claim of those general results).
