# Quantitative singular decay of geometrically weighted Cesàro averaging via a periodic operator

## Finding

Fix \(0<q<1\). On \(H_q=\{x:\sum_{j\ge1}q^j|x_j|^2<\infty\}\), let \((C_qx)_j=j^{-1}\sum_{k=1}^jx_k\). Write \(r=\sqrt q\), \(p(\theta)=1+r^2-2r\cos\theta\), and
\[
 \kappa=\frac1{2\pi}\int_0^{2\pi}p(\theta)^{-1/2}\,d\theta,
 \qquad L=2\pi\kappa,\qquad
 \mu_r=\frac1{16L}\int_0^{2\pi}\frac{p'(\theta)^2}{p(\theta)^{3/2}}\,d\theta>0.
\]
For the singular values of the infinite compact operator, in decreasing order with multiplicities,
\[
 s_n(C_q)=\frac{\kappa}{n}-\frac{\kappa^3\mu_r}{2n^3}+O_q(n^{-4}).
\]
In particular the remainder from the leading law is of order \(n^{-3}\) with a nonzero coefficient, and the count above \(t>0\) is \(\kappa/t+O_q(1)\) as \(t\downarrow0\).

The structural identification is exact: define \(x(\theta)=\int_0^\theta p(\eta)^{-1/2}\,d\eta\) on the circle of circumference \(L\) and \(z(x)=p(\theta(x))^{1/4}\). The periodic operator \(-\partial_x^2+z''/z\) has one zero eigenvalue; its positive eigenvalue list, with multiplicities, is the list \(s_n(C_q)^{-2}\) with each entry repeated twice. The usual elliptic form of the leading coefficient is \(\kappa=2K(2\sqrt r/(1+r))/(\pi(1+r))\), where \(K\) is the complete elliptic integral in modulus convention. The contribution here concerns the periodic spectral identification and the quantitative correction, not the leading limit.

## Assumptions and scope

All spaces are complex Hilbert spaces; the weight is exactly \(q^j\) on \(j\ge1\). The asymptotics are for each fixed \(q\in(0,1)\). No uniformity at \(q=1\), finite-section asymptotic, or claim about eigenvalues of \(C_q\) in place of its singular values is intended.

## Proof

**Inverse on the positive modes.** Multiplication by \(q^{j/2}\) unitarily transfers \(C_q\) to \(A=D(I-rS)^{-1}\) on \(\ell^2(\mathbb N)\), where \(S\) is the forward shift and \(D\) multiplies the \(j\)-th coordinate by \(j^{-1}\). This is compact, injective and has dense range \(\operatorname{ran}D\). Let \(J=D^{-1}\) on its natural domain. The closed inverse is \(B=(I-rS)J\). The closed form \(\|Bf\|^2\), with domain \(\operatorname{dom}J\), defines \(B^*B=(AA^*)^{-1}\), so its eigenvalues are exactly the reciprocals of the squared singular values. Equivalently, for finitely supported \(f\), its form matrix is
\[
 J\big((1+r^2)I-r(S+S^*)\big)J.
\]
Finite sequences are a form core since \((1-r)\|Jf\|\le\|Bf\|\le(1+r)\|Jf\|\).

**Separation on the circle.** On the full circle of angle \(\theta\), the smooth positive function \(p\) defines the closed form \(\int p|f_\theta|^2\,d\theta\) on periodic \(H^1\), giving the operator \(-\partial_\theta(p\partial_\theta)\). In the orthonormal Fourier basis its matrix has entries \(jk\,\widehat p(j-k)\). The only nonzero Fourier coefficients of \(p\) are at \(0,\pm1\). Thus the negative and positive modes do not couple, and every matrix entry joining them to mode zero vanishes from the factor \(jk\). The positive-mode form is the inverse form above, the negative-mode form is unitarily identical by \(j\leftrightarrow -j\), and the constant is a simple nullspace. These decompositions hold for the closed forms by the Fourier form core, so the spectrum has exactly the asserted duplication. Changing variables to \(x\) and sending \(f\) to \(v(x)=z(x)f(\theta(x))\) is unitary in ordinary Lebesgue measures. Under this transformation the form becomes
\[
 \int_0^L|v'-(z'/z)v|^2\,dx
 =\int_0^L\bigl(|v'|^2+(z''/z)|v|^2\bigr)\,dx.
\]
The functions and derivatives here are periodic. Integration by parts gives \(L^{-1}\int_0^L z''/z\,dx=L^{-1}\int_0^L(z'/z)^2\,dx=\mu_r\), because \(z'/z=p_\theta/(4\sqrt p)\). This proves the reduction and the formula for the mean of the real smooth potential \(V=z''/z\).

**High eigenvalues and the correction.** The free periodic operator \(-\partial_x^2\) has a simple zero and a double eigenvalue \(E_n=(2\pi n/L)^2=(n/\kappa)^2\) for each \(n\ge1\). The min–max principle moves any eigenvalue by at most \(\|V\|_\infty\); hence for all sufficiently large \(n\) the two eigenvalues in the \(n\)-th cluster of the perturbed spectrum are the copies of \(s_n^{-2}\), with no index shift. For the projection \(P_n\) onto the two plane waves of frequencies \(\pm 2\pi n/L\), set \(Q_n=I-P_n\). For \(|\lambda-E_n|\le\|V\|_\infty\), the inverse of the free operator minus \(\lambda\) on \(Q_n\) has norm \(O_q(n^{-1})\), by the adjacent gaps of the free spectrum. If \(v\) is a perturbed eigenfunction at \(\lambda\), projecting its equation and applying this inverse yields
\[
 \|Q_n v\|\le O_q(n^{-1})(\|P_n v\|+\|Q_n v\|),
 \qquad \|Q_n v\|\le O_q(n^{-1})\|P_n v\|.
\]
The diagonal entries of \(P_n V P_n\) are both \(\mu_r\), and its off-diagonal entries are conjugate Fourier coefficients at indices \(\pm 2n\). They are \(O_q(n^{-1})\) by one periodic integration by parts. Consequently the projected equation gives \(|\lambda-E_n-\mu_r|\|P_nv\|\le O_q(n^{-1})\|P_nv\|\); the projection is nonzero by the previous inequality. Therefore \(s_n^{-2}=E_n+\mu_r+O_q(n^{-1})\). Taking inverse square roots establishes the claimed expansion. Since \(r>0\), \(p'\) is not identically zero and the coefficient is strictly negative. Also \(s_n^{-1}=n/\kappa+O_q(n^{-1})\), implying the bounded counting error with the strict threshold convention.

## Leading-law context and verification

The expression for \(K\) follows from the half-angle identity for \(p\) and symmetry of the integral. The established leading law also implies the familiar consequences \(C_q\in\mathcal S_a\) exactly for \(a>1\) and \((\log N)^{-1}\sum_{n\le N}s_n\to\kappa\). Indeed the remainder here is summable. The leading coefficient increases strictly in \(r\) by the expansion \(\sum_{m\ge0}[\binom{2m}{m}/4^m]^2r^{2m}\), and \(\kappa=\pi^{-1}\log(8/(1-r))+o(1)\) as \(r\uparrow1\) by the standard complete elliptic integral asymptotic.

The accompanying `checker.py` compares finite SVDs with finite inverse bidiagonal Gram matrices and compares the leading coefficient and a Hilbert–Schmidt norm formula numerically. Those finite checks do not prove the infinite form identification or test the cubic-order correction as an asymptotic assertion. The infinite result follows from the form decomposition, periodic change of variable, and two-mode estimate above.

## Relationship to prior work and limitations

Albanese–Bonet–Ricker, *Spectrum and compactness of the Cesàro operator on weighted \(\ell_p\) spaces* (2015, DOI `10.1017/S1446788715000221`), cover compactness and the ordinary eigenvalues for the geometric case. After reindexing and taking parameter \(r\), the leading singular-value law, including the same elliptic constant, is exactly the scalar assertion in Resultary `2026/11/22/SCOPE-exterior-power-ordering-and-an-elliptic-singular-value-law-for-c--9192576eedcf`. The period-two leading-law extension `2026/11/22/SCOPE-period-two-geometric-weights-singular-weyl-law-and-contrast-rigi--aa2e3f6295b0` specializes to it at equal parity weights. Neither inspected leading-law claim identifies a positive correction to the inverse-square eigenvalue asymptotic or its effect on singular values. The shared catalogue date does not establish priority. The differential-operator transformation and two-mode asymptotic use standard periodic spectral methods; the specific reduction and coefficient for this infinite averaging operator are the claim. The argument uses the single Fourier band of \(p\); it does not give a general higher-band or periodic-weight correction. No claim of exhaustive historical priority or uniformity with respect to the weight is made.
