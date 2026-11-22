# A sharp affine sixth-moment profile for spherical Fourier extension

## Finding

Let \(\mu\) be the rotation-invariant probability measure on \(\mathbb S^2\subset\mathbb R^3\), and let
\[
Tf(x)=\int_{\mathbb S^2}e^{-ix\cdot\omega}f(\omega)\,d\mu(\omega),\qquad x\in\mathbb R^3.
\]
For every nonzero complex affine datum \(f(\omega)=a+v\cdot\omega\) with \(a\in\mathbb C\), \(v\in\mathbb C^3\), define its first-harmonic energy fraction
\[
\beta=\frac{|v|^2}{3\|f\|_{L^2(\mu)}^2}\in[0,1],\qquad
\|f\|_{L^2(\mu)}^2=|a|^2+\frac{|v|^2}{3}.
\]
Then the *sharp constrained sixth-moment profile* is
\[
\boxed{\ \|Tf\|_{L^6(\mathbb R^3)}^6\le
\pi^2\|f\|_{L^2(\mu)}^6
\left(\frac12-\frac9{35}\beta^2-\frac6{245}\beta^3\right).\ }
\]
For each fixed \(\beta\in[0,1]\), equality is attained. When \(0<\beta<1\), equality holds precisely when, up to a nonzero complex scalar, the datum has the form
\[
f(\omega)=c+i t\,u\cdot\omega,
\quad c,t\in\mathbb R\setminus\{0\},\quad |u|=1,
\]
with the specified energy fraction. At \(\beta=0\), equality is attained by all nonzero constants; at \(\beta=1\), equality is attained precisely by complex scalar multiples of real nonzero linear harmonics \(u\cdot\omega\).

In particular, the best affine deficit at first-harmonic fraction \(\beta\) is exactly
\[
\frac{\pi^2}{2}\|f\|_2^6-\sup\|Tf\|_6^6
=\pi^2\|f\|_2^6\left(\frac9{35}\beta^2+\frac6{245}\beta^3\right).
\]
Its quadratic vanishing in \(\beta\) quantifies the fourth-order tangency of affine harmonics to the modulated constant extremizer orbit.

## Assumptions and scope

All integrals use Lebesgue measure in \(\mathbb R^3\); the spherical measure \(\mu\) has total mass one. The assertion is restricted to the complex vector space \(\mathcal H_0\oplus\mathcal H_1\), consisting of constants plus degree-one spherical harmonics. The Fourier phase convention is \(e^{-ix\cdot\omega}\). There are no sign or reality restrictions on \(a\) or \(v\). The claim is not a global stability inequality for arbitrary \(L^2(\mathbb S^2)\) data.

## Proof

**Step 1: exact radial moments.** Set \(\phi(r)=\sin r/r\) (continuously extended at zero), \(\psi(r)=\phi'(r)\), and for \(k=0,1,2,3\) put
\[
R_k=4\pi\int_0^\infty r^2\phi(r)^{6-2k}\psi(r)^{2k}\,dr.
\]
All integrals converge absolutely, since \(\phi,\psi=O((1+r)^{-1})\) at infinity and \(\psi=O(r)\) at zero. Their **exact** values are
\[
\boxed{(R_0,R_1,R_2,R_3)
=\pi^2\left(\frac12,\frac1{10},\frac{29}{630},\frac{107}{1890}\right).}
\]
Here is a finite rational derivation. Define \(u(t)=\mathbf1_{[-1,1]}(t)\), \(v_1(t)=t\mathbf1_{[-1,1]}(t)\), and \(h_k=u^{*(6-2k)}*v_1^{*(2k)}\). Since
\[
\phi(r)=\tfrac12\int_{-1}^1e^{irt}\,dt,\qquad
\psi(r)=\tfrac i2\int_{-1}^1t e^{irt}\,dt,
\]
the Fourier distribution identity \(\int_{\mathbb R}r^2e^{irs}\,dr=-2\pi\delta''(s)\) gives
\[
R_k=\frac{(-1)^{k+1}\pi^2}{16}\,h_k''(0).
\]
Every \(h_k\) is twice continuously differentiable at zero. For \(b_{a,j}(t)=(t-a)_+^j/j!\), the elementary convolution rule is \(b_{a,j}*b_{c,\ell}=b_{a+c,j+\ell+1}\). The two factors expand as
\[
u=b_{-1,0}-b_{1,0},\qquad
v_1=b_{-1,1}-b_{-1,0}-b_{1,1}-b_{1,0}.
\]
Six finite convolutions and differentiation at zero yield, in order \(k=0,1,2,3\),
\[
\big(h_0''(0),h_1''(0),h_2''(0),h_3''(0)\big)
=\left(-8,\frac85,-\frac{232}{315},\frac{856}{945}\right).
\]
All these operations are rational and reproduced by the standalone `verify.py`.

**Step 2: exact sixth-power identity.** Multiply \(f\) by a unit complex scalar so that \(a\ge0\) is real (if \(a=0\), choose any phase). Write \(v=p+iq\) with \(p,q\in\mathbb R^3\), and set
\[
A=a^2,\quad P=|p|^2,\quad Q=|q|^2,\quad S=P+Q,\quad H=p\cdot q,
\quad D=PQ-H^2\ge0.
\]
Because \(T1(x)=\phi(|x|)\) and \(T\omega_j(x)=i\psi(|x|)x_j/|x|\), for \(x=r\theta\) we have
\[
Tf(r\theta)=a\phi(r)-\psi(r)q\cdot\theta+i\psi(r)p\cdot\theta.
\]
The spherical angular averages used when expanding its sixth power are, for \(\theta\) uniform on \(\mathbb S^2\) and a symmetric \(3\times3\) matrix \(M\),
\[
\mathbb E(\theta^TM\theta)^2=\frac{(\operatorname{tr}M)^2+2\operatorname{tr}M^2}{15},\quad
\mathbb E(\theta^TM\theta)^3=\frac{(\operatorname{tr}M)^3+6\operatorname{tr}M\operatorname{tr}M^2+8\operatorname{tr}M^3}{105},
\]
\[
\mathbb E(q\cdot\theta)^2(\theta^TM\theta)
=\frac{|q|^2\operatorname{tr}M+2q^TMq}{15}.
\]
Taking \(M=pp^T+qq^T\), using \(\operatorname{tr}M=S\), \(\operatorname{tr}M^2=S^2-2D\), and \(\operatorname{tr}M^3=S^3-3SD\), and inserting the four radial moments gives the **exact identity**
\[
\begin{aligned}
\frac{\|Tf\|_6^6}{\pi^2}
={}&\frac12A^3+\frac12A^2S+\frac{29}{210}AS^2+\frac{107}{13230}S^3\\
&-P\left(\frac25A^2+\frac{58}{525}AS\right)
-D\left(\frac{58}{525}A+\frac{214}{11025}S\right).
\end{aligned}
\]
This is an equality for **every** complex affine datum, not merely an inequality. Its last two terms are nonpositive because \(A,P,S,D\ge0\).

**Step 3: optimization and endpoint equality.** Let \(N^2=\|f\|_2^2=A+S/3\). The nonnegative deficit terms show that the maximum at fixed \((A,S)\) is
\[
\pi^2\left(\frac12A^3+\frac12A^2S+\frac{29}{210}AS^2+\frac{107}{13230}S^3\right).
\]
With \(A=N^2(1-\beta)\) and \(S=3N^2\beta\), expanding this cubic gives the stated sharp profile. If \(A,S>0\), its first deficit term vanishes only if \(P=0\); this forces \(p=0\), so \(v\) is purely imaginary in the phase convention where \(a>0\). If \(A=0\) and \(S>0\), the second deficit term vanishes exactly when \(D=0\), i.e. \(p,q\) are linearly dependent; equivalently \(v\) is a complex scalar multiple of a real vector. The constant case \(S=0\) is immediate. Each equality configuration exists at every admissible energy fraction.

## Verification

Running `python verify.py` reproduces the four rational radial moments by finite truncated-power convolutions, symbolically checks the complete deficit identity and the normalized cubic profile, and (when NumPy and SciPy are installed) independently tests three complex examples by angular/radial quadrature. The rational calculations and symbolic identity constitute exact computational corroboration; numerical quadrature is diagnostic only. The proof above establishes the all-parameter result without relying on finite tests.

## Relationship to prior work

Xu, *Sharp radial–angular mixed norm Fourier extension and global stability on spheres* (arXiv:2610.19648, first posted 14 October 2026), gives sharp mixed radial–angular extension bounds and a global quadratic spectral deficit. Its radial–angular mixed norm is **not** the ordinary \(L^6(\mathbb R^3)\) norm used here, and its spectral gap does not identify the present complex affine conditional sixth-moment profile.

Oliveira e Silva and Quilodrán, *Global maximizers for adjoint Fourier restriction inequalities on low dimensional spheres* (arXiv:1909.10230), prove the sharp ordinary \(L^2\to L^6\) maximum and all global extremizers. That theorem supplies the unconditional bound \(\|Tf\|_6^6\le(\pi^2/2)\|f\|_2^6\) but not the strictly smaller sharp value at each fixed positive \(\beta\) inside the affine space, nor the phase-polarization identity or its equality cases. Ciccone and Sousa (DOI:10.1007/s00041-025-10201-7) address mixed-norm modal comparisons and local extremizers, not this exact ordinary sixth-power polynomial. A related published conditional fourth-power result for a *mixed* norm likewise does not imply the present ordinary sixth-power statement.

## Limitations

The sharp constrained profile is specific to the four-complex-dimensional affine input subspace in dimension three and exponent six. It does not establish a positive global deficit at a fixed mean for all \(L^2\) inputs: modulated characters leave the ordinary extension norm unchanged and can have a nontrivial first-harmonic projection. The fourth-order tangency statement concerns the affine truncation of such modulation curves, not a full nonlinear distance-to-orbit stability theorem. An unindexed prior exact affine calculation cannot be categorically excluded; no independent mathematical audit has been carried out.

## References

1. Zewei Xu, *Sharp radial–angular mixed norm Fourier extension and global stability on spheres*, arXiv:2610.19648, first public 14 October 2026. https://arxiv.org/abs/2610.19648
2. Diogo Oliveira e Silva and René Quilodrán, *Global maximizers for adjoint Fourier restriction inequalities on low dimensional spheres*, arXiv:1909.10230, 2019. https://arxiv.org/abs/1909.10230
3. Valentina Ciccone and Mateus Sousa, *Global and local maximizers for some Fourier extension estimates on the sphere*, *Journal of Fourier Analysis and Applications* 31 (2025), article 70. https://doi.org/10.1007/s00041-025-10201-7
