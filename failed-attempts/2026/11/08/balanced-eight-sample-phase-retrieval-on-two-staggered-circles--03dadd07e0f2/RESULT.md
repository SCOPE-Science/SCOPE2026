# Balanced eight-sample phase retrieval on two staggered circles

## Finding
For \(r,s>0\), \(\phi\in\mathbb R\), define the two-circle quadrature design
\[
\mathcal Z_{r,s,\phi}=\{ri^k:k=0,1,2,3\}\cup\{se^{i\phi}i^k:k=0,1,2,3\}.
\]
For every quadratic polynomial \(p(z)=a+bz+cz^2\) with complex coefficients, its eight pointwise magnitudes on this set determine \(p\) up to a single unit-modulus constant **if and only if**
\[
r\ne s,\qquad\sin(2\phi)\ne0.
\]
When these conditions hold, for \(v(z)=(1,\overline z,\overline z^{\,2})^T\) the real linear lifting operator \(\mathcal M(H)=(v(z)^*Hv(z))_{z\in\mathcal Z}\) on Hermitian \(3\times3\) matrices has the exact kernel
\[
\ker\mathcal M=\mathbb R\,\operatorname{diag}(r^2s^2,-r^2-s^2,1).
\]
Eight is the smallest possible number of rank-one intensity measurements that is globally phase retrieving on \(\mathbb C^3\), even without the circle-geometry restriction.

In particular, this is a **balanced** minimum-cardinality design: exactly four samples are used in each channel. The angular staggering is essential. If the two grids are aligned modulo quarter turns, distinct polynomials with identical data are
\[
p(z)=z^2+irs,\qquad q(z)=\sqrt{r^2+s^2}\,z.
\]
At coincident radii, \(z-2r\) and \(2z-r\) have identical magnitudes at every point of the circle of radius \(r\).

## Assumptions and scope
All radii are positive and finite; the angular offset is arbitrary real. Complex quadratic coefficients, including degenerate lower-degree polynomials and zero, are allowed. Samples are labeled by channel, and exact noiseless magnitudes or squared magnitudes are used. The stated lifting-kernel formula applies when \(r\ne s\) and \(\sin(2\phi)\ne0\). The global phase is one scalar of modulus one; at the zero polynomial, uniqueness is immediate.

## Proof
**(1) Four-point Fourier extraction.** For \(H=(h_{jk})_{0\le j,k\le2}\in\operatorname{Herm}_3\), directly expand the real trigonometric polynomial
\[
\begin{aligned}
F_H(\rho,\theta)&=v(\rho e^{i\theta})^*Hv(\rho e^{i\theta})\\
&=h_{00}+\rho^2h_{11}+\rho^4h_{22}\\
&\quad+2\operatorname{Re}\!\left[e^{i\theta}(\rho h_{10}+\rho^3h_{21})+e^{2i\theta}\rho^2h_{20}\right].
\end{aligned}
\]
For the four angles \(\theta_0+k\pi/2\), their discrete Fourier coefficients recover exactly the real zeroth harmonic, the complex first harmonic, and the real number \(\operatorname{Re}(e^{2i\theta_0}h_{20})\), where all these quantities must vanish if the sampled intensities vanish. The factor \(2\rho^2\) on the last term is nonzero.

**(2) Exact lifting kernel.** Suppose \(r\ne s\) and every sample of \(F_H\) vanishes. The first harmonics on the two radii give
\[
r h_{10}+r^3h_{21}=0,\qquad s h_{10}+s^3h_{21}=0.
\]
Since \(rs(s^2-r^2)\ne0\), both entries vanish. The fourfold second harmonics give \(\operatorname{Re}(h_{20})=0\) and \(\operatorname{Re}(e^{2i\phi}h_{20})=0\). When \(\sin(2\phi)\ne0\), both real and imaginary parts of \(h_{20}\) vanish. The two zeroth harmonics then give
\[
h_{00}+r^2h_{11}+r^4h_{22}=0,\qquad
h_{00}+s^2h_{11}+s^4h_{22}=0.
\]
Solving yields \(h_{11}=-(r^2+s^2)h_{22}\), \(h_{00}=r^2s^2h_{22}\). This proves the exact kernel formula, including its dimension one. The generator has nonzero determinant \(-r^2s^2(r^2+s^2)\), so every nonzero kernel element has rank three.

**(3) Global phase uniqueness.** Write the coefficient vector of \(p\) as \(x\). Then \(|p(z)|^2=v(z)^*xx^*v(z)\). Equal intensities for \(p\) and \(q\) imply \(xx^*-yy^*\in\ker\mathcal M\). The difference has rank at most two, whereas a nonzero kernel element has rank three. Hence \(xx^*=yy^*\), so \(x\) and \(y\) differ by a unimodular scalar (or both vanish).

**(4) Necessity of staggering and two radii.** If \(\sin(2\phi)=0\), the eight sampled points satisfy \(\operatorname{Im}(z^2)=0\) and \(|z|\in\{r,s\}\). The two displayed non-proportional polynomials obey
\[
|z^2+irs|^2=|z|^4+r^2s^2=(r^2+s^2)|z|^2
=|\sqrt{r^2+s^2}\,z|^2
\]
at every sampled point. When \(r=s\), the identity \(|z-2r|=|2z-r|\) for all \(|z|=r\) gives a different explicit failure, regardless of \(\phi\).

**(5) Global eight-measurement lower bound.** In any complex dimension-three intensity measurement problem with at most seven samples, the associated real linear map on the nine-dimensional space \(\operatorname{Herm}_3\) has a kernel of dimension at least two. If the measurement vectors do not span \(\mathbb C^3\), recovery plainly fails. Otherwise no nonzero positive- or negative-semidefinite matrix can belong to that kernel: each such matrix would force all sampling vectors into its nullspace. Take real-linearly independent kernel elements \(A,B\). The real continuous odd function \(t\mapsto\det(A\cos t+B\sin t)\) changes sign (or is identically zero) under \(t\mapsto t+\pi\), so a nonzero singular kernel element exists. Such a singular element cannot be semidefinite and therefore must have one positive and one negative eigenvalue. Its positive-minus-negative spectral decomposition is \(xx^*-yy^*\) for distinct rank-one positive-semidefinite matrices, furnishing ambiguous coefficient vectors. Thus no seven-or-fewer-sample system is globally phase retrieving.

**(6) Two-Gaussian-channel corollary.** Fix \(a>0\), tone spacing \(\Omega>0\), base frequency \(\xi\in\mathbb R\), and a three-tone periodic signal
\[
f(t)=\sum_{j=0}^2c_j e^{2\pi i(\xi+j\Omega)t}.
\]
For two Gaussian-modulated integrable kernels \(g_b(t)=e^{-\pi a t^2}e^{2\pi i\nu_b t}\) with real carrier frequencies \(\nu_b\), convolution is well-defined and Gaussian Fourier integration gives
\[
(f*g_b)(t)=C_b e^{2\pi i\xi t}p(R_b e^{2\pi i\Omega t}),
\]
where \(C_b=a^{-1/2}e^{-\pi(\nu_b-\xi)^2/a}>0\), \(R_b=e^{2\pi\Omega(\nu_b-\xi)/a}>0\) and
\[
p(z)=\sum_{j=0}^2c_j e^{-\pi j^2\Omega^2/a}z^j.
\]
The transformation from \((c_0,c_1,c_2)\) to polynomial coefficients is invertible. Sample the first channel at times \(k/(4\Omega)\), and the second at times \((\phi/(2\pi)+k/4)/\Omega\), for \(k=0,1,2,3\). After dividing by the known strictly positive \(C_b^2\), their eight squared magnitudes are precisely the two-circle design with radii \(R_0,R_1\). Therefore they recover all three complex tone coefficients up to phase exactly when \(\nu_0\ne\nu_1\) and \(\sin(2\phi)\ne0\). This is an algebraic statement about periodic three-tone signals (not a claim that those signals lie in \(L^2(\mathbb R)\)).

## Verification
The included `CHECK.py` constructs the full real measurement matrix on a basis of Hermitian matrices, checks representative generic and degenerate ranks, evaluates the analytic null matrix and explicit ambiguities, and independently tests the Gaussian transform with numerical quadrature. It prints `BALANCED_QUADRATURE_CHECKS_PASSED` on success. These are finite corroborations, not substitutes for the unrestricted proof above.

## Relationship to prior work
Pohl, Li and Boche (2017) proved that eight intensity samples suffice for phase retrieval of three complex coefficients and constructed a **five-plus-three** two-radius design using an outer/inner factorization. Thus neither the eight-sample count nor two-radius phase retrieval in general is new. The distinguishing claim here is the complete **four-plus-four quadrature classification**, including the necessity of angular staggering and the explicit one-dimensional lifting kernel. Bodmann and Hammen (2013) constructed eight-sample systems using distinct geometric circle arrangements, not the present balanced concentric quadrature. Chalendar and Partington (2024) treat **continuous** phase retrieval on pairs of circles, not this discrete balanced design. Liu, Ning, Wu and Zhang (2026) study sampled two-channel Gaussian-type transform magnitudes for bandlimited signals using infinite sampling sequences; their continuous-signal theorem does not imply a four-plus-four finite quadratic design. An earlier equivalent computation in specialized finite phase-retrieval literature is a remaining originality risk.

## Limitations
No general finite-dimensional higher-degree balanced construction or sharp noisy conditioning estimate is asserted. The recovery is noiseless and assumes known radii, offsets, Gaussian window parameters and tone locations. Eight-sample minimality for dimension three is already known in the literature and is reproved only to contextualize the balanced classification. The current comparison does not constitute independent publication-priority certification.

## References
- B. Liu, M. Ning, L. Wu, Q. Zhang, *Phase Retrieval of Bandlimited Signals Using a Morlet Wavelet and an Admissible Companion*, arXiv:2610.39145, first public 2026-10-29.
- V. Pohl, N. Li, H. Boche, *Phase Retrieval in Spaces of Analytic Functions on the Unit Disk*, SampTA 2017, DOI 10.1109/SAMPTA.2017.8024411. Author presentation: https://www.ce.cit.tum.de/fileadmin/w00cgn/lti/pdf/vortraege/Pohl-Phase_Retrieval_in_Spaces_of_Analytic_Functions_on_the_Unit_Disk.pdf
- B. G. Bodmann and N. Hammen, *Stable Phase Retrieval with Low-Redundancy Frames*, arXiv:1302.5487.
- I. Chalendar and J. R. Partington, *Phase Retrieval on Circles and Lines*, arXiv:2403.16255.
- A. Conca, D. Edidin, M. Hering and C. Vinzant, *An Algebraic Characterization of Injectivity in Phase Retrieval*, Appl. Comput. Harmon. Anal. 38 (2015), 346–356.
